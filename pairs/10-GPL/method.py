import sys
from pathlib import Path
from sentence_transformers import SentenceTransformer

HERE = Path(__file__).resolve().parent
PROJECT_ROOT = HERE.parents[1]

sys.path.insert(0, str(PROJECT_ROOT))

import testbed

ROOT = HERE
MODELS_ROOT = ROOT / "runs" / "Models"   # runs/Models/models_<tag>/<método>_<estudiante>/<dataset>/
EVAL_ROOT = ROOT / "runs" / "Eval"       # runs/Eval/eval_<tag>/<método>_<estudiante>/<dataset>.json


# 1. CONFIGURATION

# Experiments to evaluate (model_tag values from run_training)
MODEL_TAGS = [
    "base",
    "base_neg10",
    "base_neg20",
    "base_neg30",
    "base_neg40",
    "base_stepx4",
]

DATASETS = ["scifact", "nfcorpus", "arguana"]

STUDENTS = {
    "BGE": "BAAI/bge-small-en-v1.5",
    "MiniLM": "sentence-transformers/all-MiniLM-L6-v2",
    "GPL_distilbert": "GPL/msmarco-distilbert-margin-mse",
}

METHODS = ["gpl", "genq", "gpl_bm25"]

MODELS = [f"{method}_{student}" for method in METHODS for student in STUDENTS]


# 2. EVALUATE ALL CHECKPOINTS

data = {dataset: testbed.load(dataset) for dataset in DATASETS}

for model_tag in MODEL_TAGS:
    for dataset in DATASETS:
        corpus, queries, _ = data[dataset]

        for model_name in MODELS:
            checkpoint = MODELS_ROOT / f"models_{model_tag}" / model_name / dataset
            output_path = EVAL_ROOT / f"eval_{model_tag}" / model_name / f"{dataset}.json"

            print(f"\n{'=' * 50}")
            print(f"Experiment: {model_tag} | Dataset: {dataset} | Model: {model_name}")
            print(f"{'=' * 50}")

            if output_path.exists():
                print(f"Already evaluated, skipping: {output_path}")
                continue

            if not checkpoint.is_dir():
                print(f"Checkpoint not found: {checkpoint}")
                continue

            model = SentenceTransformer(str(checkpoint), device=testbed.device())


            query_prefix = testbed.BGE_QUERY if model_name.endswith("_BGE") else ""

            # Same preprocessing and ranking as testbed dense baselines
            run = testbed.dense_search(
                model,
                corpus,
                queries,
                query_prefix=query_prefix,
                batch_size=16,
            )

            output_path.parent.mkdir(parents=True, exist_ok=True)
            testbed.save_run(run, output_path)
            print(f"Saved run: {output_path}")

            del model

print("\nAll evaluations completed.")