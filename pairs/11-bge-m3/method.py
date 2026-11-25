"""BGE-M3 on the testbed, with the five retrieval modes of the paper (section 4.1).

Same setup as the paper: dense search with Faiss, sparse search with Lucene (Pyserini impact index).
Each corpus is encoded once, cached in runs/cache/, and all five modes are computed from that encoding.

Modes:
    dense          Faiss (exact inner product) over all docs, ranked by s_dense
    sparse         Lucene impact index over all docs, ranked by s_lex
    multi-vec      rerank the dense top-200 by s_mul
    dense+sparse   rerank the union of dense top-1000 (Faiss) and sparse top-1000 (Lucene) by 1·s_dense + 0.3·s_lex
    all            rerank the dense top-200 by 1·s_dense + 0.3·s_lex + 1·s_mul

Usage: python method.py                          → all datasets, all five modes, scored against RRF
       python method.py arguana --mode sparse    → one dataset, one mode
Writes runs/ (mode all) and runs_<mode>/ (the others), then results.json and results_<mode>.json.

Extra requirements: faiss-cpu (or faiss-gpu), pyserini (needs Java 21 or later).
"""
import argparse
import json
import os
import pickle
import shutil
import subprocess
import sys
import time
from pathlib import Path

# on macOS faiss and torch each ship their own OpenMP; with the JVM loaded too, the second one segfaults.
# One OpenMP thread and loading the model before faiss avoid it (Faiss flat search is fast without threads).
if sys.platform == "darwin":
    os.environ.setdefault("OMP_NUM_THREADS", "1")

import numpy as np
import torch
from FlagEmbedding import BGEM3FlagModel
from tqdm import tqdm

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1]))          # repo root, for testbed.py
import testbed

DEVICE = "cuda" if torch.cuda.is_available() else "mps" if torch.backends.mps.is_available() else "cpu"
model = BGEM3FlagModel("BAAI/bge-m3", use_fp16=True, devices=DEVICE)

import faiss

# pyserini needs a JDK: install one only if the machine has none
if shutil.which("javac") is None and "JAVA_HOME" not in os.environ:
    import jdk
    java_dir = Path.home() / ".jdk"
    found = list(java_dir.glob("jdk-21*")) if java_dir.exists() else []
    home = str(found[0]) if found else jdk.install("21", path=str(java_dir))
    os.environ["JAVA_HOME"] = home
    os.environ["PATH"] = home + "/bin:" + os.environ["PATH"]

from pyserini.search.lucene import LuceneImpactSearcher

MODES = ["dense", "sparse", "multi-vec", "dense+sparse", "all"]
W_DENSE, W_LEX, W_MUL = 1.0, 0.3, 1.0             # the paper's weights for MIRACL / MKQA
N_CAND = 200                                      # dense candidates reranked (multi-vec, all), as in the paper
N_HYBRID = 1000                                   # top-k from dense and from sparse (dense+sparse), as in the paper
MAX_LEN = 512                                     # 200 words fit; ArguAna queries are full arguments
CHUNK = 1000                                      # encode in chunks to keep RAM low
QUANT = 100                                       # Lucene stores integer impacts: weight -> round(weight * 100)
CACHE = HERE / "runs" / "cache"                   # encodings, git-ignored
INDEX_DIR = HERE / "indexes"


def encode(texts):
    """Encode texts with the three BGE-M3 heads.

    Returns:
        dense:   np.ndarray (n_texts, 1024), one normalized [CLS] vector per text
        lexical: list of n_texts dicts {token id (str): weight}, only non-zero tokens
        mul_vec: list of n_texts np.ndarray (n_tokens_i, 1024), one vector per token, fp16
    """
    dense, lexical, mul_vec = [], [], []
    for i in range(0, len(texts), CHUNK):
        out = model.encode(texts[i:i + CHUNK], batch_size=32, max_length=MAX_LEN,
                           return_dense=True, return_sparse=True, return_colbert_vecs=True)
        dense.append(np.asarray(out["dense_vecs"], dtype=np.float32))
        lexical += [{t: float(w) for t, w in x.items()} for x in out["lexical_weights"]]
        mul_vec += [np.asarray(v, dtype=np.float16) for v in out["colbert_vecs"]]
    return np.vstack(dense), lexical, mul_vec


def cached_encode(name, part, texts):
    """encode(texts), saved to runs/cache/<name>/<part>/ the first time and read back afterwards."""
    folder = CACHE / name / part
    if not (folder / "colbert_offsets.npy").exists():
        t0 = time.time()
        dense, lexical, mul_vec = encode(texts)
        folder.mkdir(parents=True, exist_ok=True)
        np.save(folder / "dense.npy", dense)
        pickle.dump(lexical, open(folder / "lex.pkl", "wb"))
        np.save(folder / "colbert.npy", np.concatenate(mul_vec))       # all token vectors, one text after the other
        np.save(folder / "colbert_offsets.npy", np.cumsum([0] + [len(v) for v in mul_vec]))
        print(f"{name} {part}: {len(texts)} texts encoded in {time.time() - t0:.0f}s on {DEVICE}", flush=True)
    colbert, off = np.load(folder / "colbert.npy"), np.load(folder / "colbert_offsets.npy")
    mul_vec = [colbert[off[k]:off[k + 1]] for k in range(len(off) - 1)]
    return np.load(folder / "dense.npy"), pickle.load(open(folder / "lex.pkl", "rb")), mul_vec


def faiss_index(D_dense):
    """Exact inner-product index (vectors are normalized, so this is cosine)."""
    index = faiss.IndexFlatIP(D_dense.shape[1])
    index.add(D_dense)
    return index


# Sparse: Lucene (Pyserini impact index)
def quantize(weights):
    """{token id: float weight} -> {token id: int impact}, dropping tokens that round to 0."""
    return {tok: int(round(x * QUANT)) for tok, x in weights.items() if round(x * QUANT) > 0}


def to_query_string(weights):
    """Pyserini encodes string queries by counting tokens: repeat each token id by its integer weight."""
    return " ".join(" ".join([tok] * w) for tok, w in quantize(weights).items())


def lucene_index(name, ids, D_lex):
    """Write the doc weights as a JsonVectorCollection and build a Lucene impact index (once per dataset)."""
    index_path = INDEX_DIR / f"{name}_lucene"
    if index_path.exists():
        return index_path
    coll_dir = INDEX_DIR / f"{name}_collection"
    coll_dir.mkdir(parents=True, exist_ok=True)
    with open(coll_dir / "docs.jsonl", "w") as f:
        for doc_id, w in zip(ids, D_lex):
            f.write(json.dumps({"id": doc_id, "contents": "", "vector": quantize(w)}) + "\n")
    subprocess.run([sys.executable, "-m", "pyserini.index.lucene",
                    "--collection", "JsonVectorCollection",
                    "--input", str(coll_dir),
                    "--index", str(index_path),
                    "--generator", "DefaultLuceneDocumentGenerator",
                    "--threads", "8",
                    "--impact", "--pretokenized"], check=True)
    return index_path


def lex_score(q, d):
    """s_lex = sum over shared tokens of w_q,t * w_p,t (exact float weights, as in FlagEmbedding)."""
    return sum(x * d[t] for t, x in q.items() if t in d)


def colbert_batch(q, docs):
    """Late interaction for one query against all its candidates at once:
    each query token takes its best document token, averaged over query tokens."""
    # docs have different token counts, so pad them with zeros to the longest one (L)
    # and stack them in a single tensor D of shape (candidates, L, 1024)
    L = max(len(d) for d in docs)
    D = np.zeros((len(docs), L, q.shape[1]), dtype=np.float16)
    mask = np.zeros((len(docs), L), dtype=bool)
    for k, d in enumerate(docs):
        D[k, :len(d)] = d
        mask[k, :len(d)] = True
    q = torch.from_numpy(np.asarray(q, dtype=np.float16)).to(DEVICE)
    D, mask = torch.from_numpy(D).to(DEVICE), torch.from_numpy(mask).to(DEVICE)
    sim = torch.einsum("qh,kdh->kqd", q, D).float()
    sim = sim.masked_fill(~mask[:, None, :], float("-inf"))
    return sim.max(dim=2).values.mean(dim=1).cpu().numpy()


def search(name, modes=MODES, queries=None):
    """Runs of the given modes on one dataset: {mode: {qid: {doc id: score}}}.

    queries=None takes the test queries and caches their encoding; other queries (French) are encoded each time.
    """
    corpus, test_queries, _ = testbed.load(name)
    ids = list(corpus)
    pos = {doc_id: j for j, doc_id in enumerate(ids)}
    D_dense, D_lex, D_mul = cached_encode(name, "docs", testbed.doc_texts(corpus))   # same text as the baselines
    if queries is None:
        queries = test_queries
        Q_dense, Q_lex, Q_mul = cached_encode(name, "queries", list(test_queries.values()))
    else:
        Q_dense, Q_lex, Q_mul = encode(list(queries.values()))          # no query prefix for M3
    qids = list(queries)

    # first stages, run once at the deepest cut any mode needs (Faiss and Lucene return sorted lists)
    _, dense_hits = faiss_index(D_dense).search(Q_dense, N_HYBRID)
    if "sparse" in modes or "dense+sparse" in modes:
        searcher = LuceneImpactSearcher(str(lucene_index(name, ids, D_lex)), query_encoder=None)
        sparse_hits = [searcher.search(to_query_string(Q_lex[i]), k=N_HYBRID) for i in range(len(qids))]

    runs = {mode: {} for mode in modes}
    for i, q in enumerate(tqdm(qids, desc=name)):
        dense_top = dense_hits[i][dense_hits[i] >= 0]
        pool = dense_top[:N_CAND]
        if "multi-vec" in modes or "all" in modes:
            s_mul = colbert_batch(Q_mul[i], [D_mul[j] for j in pool])
        for mode in modes:
            if mode == "dense":
                cand = dense_top[:testbed.K + 1]
                s = Q_dense[i] @ D_dense[cand].T
            elif mode == "sparse":
                hits = sparse_hits[i][:testbed.K + 1]
                cand = np.array([pos[h.docid] for h in hits], dtype=int)
                s = np.array([h.score for h in hits], dtype=float)
            elif mode == "dense+sparse":
                cand = np.union1d(dense_top, [pos[h.docid] for h in sparse_hits[i]]).astype(int)
                s_lex = np.array([lex_score(Q_lex[i], D_lex[j]) for j in cand])
                s = W_DENSE * (Q_dense[i] @ D_dense[cand].T) + W_LEX * s_lex
            elif mode == "multi-vec":
                cand, s = pool, s_mul
            else:
                s_lex = np.array([lex_score(Q_lex[i], D_lex[j]) for j in pool])
                cand, s = pool, W_DENSE * (Q_dense[i] @ D_dense[pool].T) + W_LEX * s_lex + W_MUL * s_mul
            order = np.argsort(-s)[:testbed.K + 1]                  # top 101 (ArguAna drops the query itself)
            runs[mode][q] = {ids[cand[k]]: float(s[k]) for k in order}
    return runs


def suffix(mode):
    return "" if mode == "all" else "_" + mode.replace("+", "_")


def label(mode):
    return {"dense": "Dense", "sparse": "Sparse", "multi-vec": "Multi-vec", "dense+sparse": "Dense+Sparse", "all": "All"}[mode]


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("datasets", nargs="*", default=testbed.DATASETS, help="default: all three")
    parser.add_argument("--mode", choices=MODES, help="default: all five")
    args = parser.parse_args()
    modes = [args.mode] if args.mode else MODES

    for name in args.datasets:
        for mode, run in search(name, modes).items():
            testbed.save_run(run, HERE / ("runs" + suffix(mode)) / f"{name}.json")
        print(name, "done", flush=True)

    # same scoring as `python testbed.py score`, against RRF, the spring pipeline
    for mode in modes:
        testbed.cmd_score(argparse.Namespace(run_dir=str(HERE / ("runs" + suffix(mode))), method=f"BGE-M3 ({label(mode)})",
                                             pair="11-bge-m3", against="rrf", out=str(HERE / f"results{suffix(mode)}.json")))

    # per-query scores, small enough for git, so reproduce.ipynb can run paired tests without the runs
    path = HERE / "results_per_query.json"
    per_query = json.load(open(path)) if path.exists() else {}
    for name in args.datasets:
        for mode in modes:
            qids, ndcg, recall = testbed.score_run(json.load(open(HERE / ("runs" + suffix(mode)) / f"{name}.json")), name)
            per_query.setdefault(name, {"qids": qids})[mode] = {"ndcg10": ndcg.round(4).tolist(), "recall100": recall.round(4).tolist()}
    json.dump(per_query, open(path, "w"))
