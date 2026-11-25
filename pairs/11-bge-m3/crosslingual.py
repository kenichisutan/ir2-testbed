"""Cross-lingual check: the 300 SciFact test queries in English and in French, against the English corpus, for each mode.

Usage: python pairs/11-bge-m3/crosslingual.py   → runs/crosslingual/ and results_crosslingual.json
"""
import csv
import json
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1]))
import testbed

RUNS = HERE / "runs" / "crosslingual"
OUT = HERE / "results_crosslingual.json"
N_WORST = 5
MODES = ["dense", "sparse", "multi-vec", "dense+sparse", "all"]       # as method.MODES, without loading the model


def get_runs(lang, queries):
    """The five modes for one language. Runs are saved, so scoring can be redone without encoding again."""
    paths = {mode: RUNS / f"{mode.replace('+', '_')}_{lang}.json" for mode in MODES}
    if not all(path.exists() for path in paths.values()):
        import method                                   # loads BGE-M3, only when a run is missing
        # the corpus encoding comes from method.py's cache; English uses the cached test queries
        runs = method.search("scifact", queries=None if lang == "en" else queries)
        for mode, run in runs.items():
            testbed.save_run(run, paths[mode])
    return {mode: json.load(open(path)) for mode, path in paths.items()}


def recall20(run, qids):
    """Per-query Recall@20, the paper's auxiliary metric on MKQA (Table 13); its main one is Recall@100 (Table 2)."""
    import pytrec_eval
    _, _, qrels = testbed.load("scifact")
    ranked = {q: {d: float(testbed.K - i) for i, d in enumerate(sorted(run[q], key=run[q].get, reverse=True)[:testbed.K])} for q in qids}
    s = pytrec_eval.RelevanceEvaluator({q: qrels[q] for q in qids}, {"recall.20"}).evaluate(ranked)
    return np.array([s[q]["recall_20"] for q in qids])


def summary(ndcg, recall, r20, ndcg_en, recall_en, r20_en):
    return {"ndcg10": round(float(ndcg.mean()), 4), "recall20": round(float(r20.mean()), 4), "recall100": round(float(recall.mean()), 4),
            "ndcg10_vs_en": testbed.compare(ndcg, ndcg_en), "recall20_vs_en": testbed.compare(r20, r20_en),
            "recall100_vs_en": testbed.compare(recall, recall_en)}


def main():
    _, queries_en, _ = testbed.load("scifact")
    queries_fr = json.load(open(HERE / "queries_fr.json", encoding="utf-8"))
    checked = {r["qid"] for r in csv.DictReader(open(HERE / "check_30.csv", encoding="utf-8")) if r["correct"] == "1"}

    runs_en, runs_fr = get_runs("en", queries_en), get_runs("fr", queries_fr)
    results = {}
    for mode in MODES:
        run_en, run_fr = runs_en[mode], runs_fr[mode]
        qids, ndcg_en, recall_en = testbed.score_run(run_en, "scifact")
        _, ndcg_fr, recall_fr = testbed.score_run(run_fr, "scifact")
        r20_en, r20_fr = recall20(run_en, qids), recall20(run_fr, qids)
        ok = np.array([q in checked for q in qids])       # the hand-checked queries translated correctly

        # queries that lose the most nDCG@10 in French, for the error analysis
        loss = ndcg_en - ndcg_fr
        worst = [{"qid": qids[i], "ndcg10_en": round(float(ndcg_en[i]), 3), "ndcg10_fr": round(float(ndcg_fr[i]), 3),
                  "en": queries_en[qids[i]], "fr": queries_fr[qids[i]]} for i in np.argsort(-loss)[:N_WORST]]

        results[mode] = {
            "en": {"ndcg10": round(float(ndcg_en.mean()), 4), "recall20": round(float(r20_en.mean()), 4),
                   "recall100": round(float(recall_en.mean()), 4)},
            "fr": summary(ndcg_fr, recall_fr, r20_fr, ndcg_en, recall_en, r20_en),
            "fr_checked": dict(n_queries=int(ok.sum()), **summary(ndcg_fr[ok], recall_fr[ok], r20_fr[ok],
                                                                   ndcg_en[ok], recall_en[ok], r20_en[ok])),
            "worst": worst,
        }

    json.dump(results, open(OUT, "w"), ensure_ascii=False, indent=1)

    for metric in ("ndcg10", "recall20", "recall100"):
        print(f"\n| Mode | {metric} EN | {metric} FR | Δ [95% CI] | p |")
        print("|---|:-:|:-:|:-:|:-:|")
        for mode, r in results.items():
            c = r["fr"][f"{metric}_vs_en"]
            print(f"| {mode} | {r['en'][metric]:.3f} | {r['fr'][metric]:.3f} | {c['delta']:+.3f} [{c['ci95'][0]:+.3f}, {c['ci95'][1]:+.3f}] "
                  f"| {c['p']:.2g} |")
    for mode, r in results.items():
        c = r["fr_checked"]["ndcg10_vs_en"]
        print(f"{mode}, {r['fr_checked']['n_queries']} checked queries: Δ nDCG@10 {c['delta']:+.3f}, p {c['p']:.2g}")


if __name__ == "__main__":
    main()
