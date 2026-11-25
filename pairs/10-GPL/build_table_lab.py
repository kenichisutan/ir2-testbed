"""Builds results_lab.md from baselines/scores.json (project root) and results_exp/results_*.json (next to this script). Runs by itself on every push to main."""
import json
import sys
from pathlib import Path
import numpy as np

HERE = Path(__file__).resolve().parent          # pairs/NN/
ROOT = HERE.parents[1]                          
sys.path.insert(0, str(ROOT))
import testbed                                  # testbed.py en la raíz

NAMES = {"scifact": "SciFact", "nfcorpus": "NFCorpus", "arguana": "ArguAna"}
HEAD = "| Method | nDCG@10 | Recall@100 | Compared with | Δ nDCG@10 [95 % CI] | p |\n|---|:-:|:-:|---|:-:|:-:|"


def row(pair, r, link):
    c = r["ndcg10_vs_baseline"]
    delta = f"{c['delta']:+.3f} [{c['ci95'][0]:+.3f}, {c['ci95'][1]:+.3f}]"
    if c["p"] < 0.05 and c["ci95"][0] * c["ci95"][1] > 0:      # bold only what survives both tests
        delta = f"**{delta}**"
    p = "< 0.001" if c["p"] < 0.001 else f"{c['p']:.3f}"
    return f"| {pair['method']} ([{pair['pair']}]({link})) | {r['ndcg10']:.3f} | {r['recall100']:.3f} | {testbed.LABELS[r['baseline']['name']]} | {delta} | {p} |"


def main():
    base = testbed.stored()                     # lee baselines/scores.json de la raíz
    pairs = []
    for path in sorted((HERE / "results_exp").glob("results_*.json")):
        pairs.append((json.load(open(path)), f"results_exp/{path.name}"))
    lines = ["# Shared results table", "",
             "Built by `build_table.py` from `baselines/scores.json` and `results_exp/results_*.json`: do not edit by hand.",
             "A difference is in bold only when its p-value is below 0.05 and its confidence interval excludes zero.",
             "Pair 00 is the instructor's worked example from the model presentation.", ""]
    for name in testbed.DATASETS:
        lines += [f"## {NAMES[name]}", "", HEAD]
        for s in testbed.SYSTEMS:
            if s in base.get(name, {}):
                nd, rc = np.mean(base[name][s]["ndcg10"]), np.mean(base[name][s]["recall100"])
                lines.append(f"| *{testbed.LABELS[s]}* | {nd:.3f} | {rc:.3f} | | | |")
        for pair, link in pairs:
            if name in pair["datasets"]:
                lines.append(row(pair, pair["datasets"][name], link))
        lines.append("")
    (HERE / "RESULTS_lab.md").write_text("\n".join(lines))


if __name__ == "__main__":
    main()