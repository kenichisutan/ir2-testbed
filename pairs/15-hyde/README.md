# HyDE: Precise Zero-Shot Dense Retrieval without Relevance Labels (Gao et al., ACL 2023)

Pair 15: Xuanru Dai and Juan Kenichi Sutan. Session of Friday 27 November.

Method: an LLM writes hypothetical documents for each query, and the retriever searches with the mean of their embeddings and the query embedding. Generator: Qwen2.5-3B-Instruct, 8-bit, MLX, on a laptop; its output is committed in `generations/` (paper settings) and `generations_plain/` (second run, see `prompts.py`).

```
pip install -r pairs/15-hyde/requirements.txt
jupyter nbconvert --to notebook --execute --inplace pairs/15-hyde/reproduce.ipynb   # reproduction: Contriever with and without HyDE, SciFact and ArguAna
python pairs/15-hyde/method.py
python testbed.py score pairs/15-hyde/runs --method "HyDE + BGE-small (Qwen2.5-3B, N=8)" --pair 15-hyde --against bge
python pairs/15-hyde/generate.py && python pairs/15-hyde/generate.py plain          # optional, Apple silicon, about 6 hours: rewrites both caches
```

Testbed part (`method.py`, `results.json`, `demo.md`): work in progress.

AI assistance: Claude (Anthropic) helped write the code and run the experiments. We chose the experiments, checked the numbers and wrote the conclusions. Also declared in the report.
