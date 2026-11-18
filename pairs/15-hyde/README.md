# HyDE: Precise Zero-Shot Dense Retrieval without Relevance Labels (Gao et al., ACL 2023)

Pair 15: Xuanru Dai and Juan Kenichi Sutan. Session of Friday 27 November.

Method: an LLM writes hypothetical documents for each query, and the retriever searches with the mean of their embeddings and the query embedding. Generator: Qwen2.5-3B-Instruct, 8-bit, MLX, on a laptop; its output is committed in `generations/` (paper settings) and `generations_plain/` (second run, see `prompts.py`).

```
pip install -r pairs/15-hyde/requirements.txt
jupyter nbconvert --to notebook --execute --inplace pairs/15-hyde/reproduce.ipynb   # reproduction: Contriever with and without HyDE, SciFact and ArguAna
python pairs/15-hyde/method.py
python testbed.py score pairs/15-hyde/runs --method "HyDE + BGE-small (Qwen2.5-3B, N=8)" --pair 15-hyde --against bge
python pairs/15-hyde/run_variants.py                                                # results_variants/: BM25, MiniLM, BGE, Contriever, cross-encoder
python pairs/15-hyde/demo.py nfcorpus PLAIN-817                                     # demo, after method.py (see demo.md)
python pairs/15-hyde/generate.py && python pairs/15-hyde/generate.py plain          # optional, Apple silicon, about 6 hours: rewrites both caches
```

Two protocols. `reproduce.ipynb` follows the paper: full documents, dot product. `method.py`, `run_variants.py` and `results_variants/` follow the testbed: first 200 words, cosine. The Contriever scores differ between them for that reason; the notebook section "Same encoder, two protocols" shows the four combinations.

The caches `generations/` and `generations_plain/` (about 14 MB, ArguAna is the largest) are committed on purpose: they are the LLM output every row depends on, and regenerating them takes about 6 hours on Apple silicon.

`results.json` and `results_variants/` were written on one machine. A re-run on another agrees within 0.001 nDCG@10.

AI assistance: Claude (Anthropic) helped write the code and run the experiments. We chose the experiments, checked the numbers and wrote the conclusions. Also declared in the report.
