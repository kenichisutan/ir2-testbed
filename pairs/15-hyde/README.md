# HyDE: Precise Zero-Shot Dense Retrieval without Relevance Labels

Pair 15: Xuanru Dai and Juan Kenichi Sutan. Session of Friday 27 November.

Method: an LLM writes hypothetical documents for each query, and the retriever searches with their embedding (Gao et al., ACL 2023).

Work in progress. How to run:

```
python pairs/15-hyde/method.py
python testbed.py score pairs/15-hyde/runs --method "HyDE + BGE-small (Qwen2.5-3B, N=8)" --pair 15-hyde --against bge
```
