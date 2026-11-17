# Demo Queries (Pair 15: HyDE)

Run after `python pairs/15-hyde/method.py`, which writes `runs/`:

    python pairs/15-hyde/demo.py nfcorpus PLAIN-817
    python pairs/15-hyde/demo.py arguana test-health-ppelfhwbpba-pro02a
    python pairs/15-hyde/demo.py scifact 1

## 1. Hero Query (`nfcorpus` / `PLAIN-817`, nDCG@10 +1.000)
- **Selection**: the largest nDCG@10 gain of HyDE + BGE-small over BGE-small on NFCorpus.
- **Query**: `canker sores`
- **Why HyDE wins**: Lay medical query vs. technical abstracts. BGE-small alone confuses "sores" with "muscle soreness" (0 relevant in top 5). Qwen2.5-3B bridges the vocabulary gap by generating medical terms (*aphthous ulcers*, *oral mucosal lesions*), bringing the relevant paper (`MED-4841`) to rank #1.

## 2. Failure Query (`arguana` / `test-health-ppelfhwbpba-pro02a`, nDCG@10 -1.000)
- **Selection**: the largest nDCG@10 loss of HyDE + BGE-small against BGE-small on ArguAna.
- **Query**: Long argument on personhood at birth and partial-birth abortion.
- **Why HyDE fails**: BGE-small already ranks the true counter-argument #1. The 400-word hypothetical response adds generic meta-phrasing (*"several counterarguments"*, *"Definition of Personhood"*), diluting the specific argument and pulling generic abortion documents ahead.

## 3. Wildcard Query (Backup: `scifact` / `1`, nDCG@10 +1.000)
- Ready to run any query ID proposed live from `scifact`, `nfcorpus`, or `arguana` via `python pairs/15-hyde/demo.py <dataset> <qid>`.

## Fallback Recording
- Link: `<TODO: add 2-min screen recording link before Wed Nov 25>`
