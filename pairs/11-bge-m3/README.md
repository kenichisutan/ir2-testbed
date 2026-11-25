# M3-Embedding (BGE-M3, Chen et al., Findings of ACL 2024) — pair 11: Oliver Wakeford, Mathis Lesgourgues

Method: `BAAI/bge-m3` (released checkpoint, no training), three heads from one encoder. Dense uses Faiss, sparse a Lucene impact index, Multi-vec and All rerank the dense top 200, Dense+Sparse the union of both top 1000; weights 1·dense + 0.3·sparse + 1·multi-vec. Compared with `rrf` (the spring pipeline, BM25 + MiniLM).
Run from the repo root (pyserini needs Java 21+): `pip install -r pairs/11-bge-m3/requirements.txt`, then `python pairs/11-bge-m3/method.py` (3 datasets × 5 modes, about 5 min on a Mac with MPS) and `python testbed.py score pairs/11-bge-m3/runs --method "BGE-M3 (All)" --pair 11-bge-m3 --against rrf` (= `results.json`).
Extras: `translate_scifact.py` → `crosslingual.py` (French vs English queries), `tune_weights.py` (grid on the 809 SciFact train queries), `demo.py --build` then `--web` (live demo, see `demo.md`).
`reproduce.ipynb` puts our numbers next to the paper's tables, with paired tests; `results_*.json` and `results_per_query.json` are its inputs, `error_analysis.md` and `check_30.csv` the French-query error analysis.

| Dataset | BGE-M3 All | RRF | Δ nDCG@10 [95% CI] | p |
|---|:-:|:-:|:-:|:-:|
| SciFact / NFCorpus / ArguAna | 0.692 / 0.336 / 0.527 | 0.718 / 0.342 / 0.549 | −0.026 [−0.054, +0.003] / −0.006 [−0.022, +0.010] / −0.022 [−0.036, −0.008] | 0.078 / 0.47 / 0.002 |

AI use: Claude Code helped write code, notebook, README and slides; we ran and checked all results ourselves (details in the report).
