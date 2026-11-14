"""HyDE helpers shared by reproduce.ipynb, method.py and demo.py."""
import gzip
import json
from pathlib import Path
import numpy as np

HERE = Path(__file__).resolve().parent


def load_generations(name):
    """{query id: [hypothetical documents]}, the cache written by generate_colab.ipynb."""
    with gzip.open(HERE / "generations" / f"{name}.jsonl.gz", "rt") as f:
        return {r["qid"]: r["docs"] for r in map(json.loads, f)}


def hyde_vectors(model, queries, generations, n=8, with_query=True, query_prefix="", normalize=False):
    """One vector per query: the mean of its first n hypothetical documents and, as in the paper, of the query."""
    docs = [d for q in queries for d in generations[q][:n]]
    E = model.encode(docs, batch_size=32, normalize_embeddings=normalize, convert_to_numpy=True)
    total = E.reshape(len(queries), n, -1).sum(axis=1)
    if not with_query:
        return total / n
    Q = model.encode([query_prefix + t for t in queries.values()], batch_size=32,
                     normalize_embeddings=normalize, convert_to_numpy=True)
    return (total + Q) / (n + 1)


def search(Q, D, qids, ids, k=101):
    """Dot-product ranking as a testbed run: {query id: {document id: score}}."""
    S = Q @ D.T
    top = np.argsort(-S, axis=1)[:, :k]
    return {q: {ids[j]: float(S[i, j]) for j in top[i]} for i, q in enumerate(qids)}
