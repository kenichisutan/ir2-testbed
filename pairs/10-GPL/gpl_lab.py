import sys
from pathlib import Path
import gpl


PROJECT_ROOT = Path.cwd()
sys.path.insert(0, str(PROJECT_ROOT))

from gpl_generate import run_generation
from gpl_train import run_training, ROOT


# Original datasets (BEIR format)
DATASETS = {
    "scifact": PROJECT_ROOT / "data" / "scifact",
    "nfcorpus": PROJECT_ROOT / "data" / "nfcorpus",
    "arguana": PROJECT_ROOT / "data" / "arguana",
}

# Resized corpus size, queries per passage, and GPL training steps for each dataset.
# gpl_steps = new_size * queries_per_passage / 32  ->  one pass over all queries
CONFIGS = {
    "scifact": {"new_size": 2592, "queries_per_passage": 3, "gpl_steps": 243, "neg_per_query": 50},
    "nfcorpus": {"new_size": 1816, "queries_per_passage": 4, "gpl_steps": 227, "neg_per_query": 50},
    "arguana": {"new_size": 2892, "queries_per_passage": 3, "gpl_steps": 271, "neg_per_query": 50},
}

STUDENTS = {
    "BGE": "BAAI/bge-small-en-v1.5",
    "MiniLM": "sentence-transformers/all-MiniLM-L6-v2",
    "GPL_distilbert": "GPL/msmarco-distilbert-margin-mse",
}


# Base generation experiment: neg_50 and x1
run_generation(DATASETS, CONFIGS, tag="base")

# Neg_per_query experiment
CONFIGS_neg_query_10 = {
    "scifact": {"new_size": 2592, "queries_per_passage": 3, "gpl_steps": 243, "neg_per_query": 10},
    "nfcorpus": {"new_size": 1816, "queries_per_passage": 4, "gpl_steps": 227, "neg_per_query": 10},
    "arguana": {"new_size": 2892, "queries_per_passage": 3, "gpl_steps": 271, "neg_per_query": 10}}
run_generation(DATASETS, CONFIGS_neg_query_10, tag="Neg_query_10")

CONFIGS_neg_query_20 = {
    "scifact": {"new_size": 2592, "queries_per_passage": 3, "gpl_steps": 243, "neg_per_query": 20},
    "nfcorpus": {"new_size": 1816, "queries_per_passage": 4, "gpl_steps": 227, "neg_per_query": 20},
    "arguana": {"new_size": 2892, "queries_per_passage": 3, "gpl_steps": 271, "neg_per_query": 20}}
run_generation(DATASETS, CONFIGS_neg_query_20, tag="Neg_query_20")

CONFIGS_neg_query_30 = {
    "scifact": {"new_size": 2592, "queries_per_passage": 3, "gpl_steps": 243, "neg_per_query": 30},
    "nfcorpus": {"new_size": 1816, "queries_per_passage": 4, "gpl_steps": 227, "neg_per_query": 30},
    "arguana": {"new_size": 2892, "queries_per_passage": 3, "gpl_steps": 271, "neg_per_query": 30}}
run_generation(DATASETS, CONFIGS_neg_query_30, tag="Neg_query_30")

CONFIGS_neg_query_40 = {
    "scifact": {"new_size": 2592, "queries_per_passage": 3, "gpl_steps": 243, "neg_per_query": 40},
    "nfcorpus": {"new_size": 1816, "queries_per_passage": 4, "gpl_steps": 227, "neg_per_query": 40},
    "arguana": {"new_size": 2892, "queries_per_passage": 3, "gpl_steps": 271, "neg_per_query": 40}}
run_generation(DATASETS, CONFIGS_neg_query_40, tag="Neg_query_40")

CONFIGS_neg_query_50 = {
    "scifact": {"new_size": 2592, "queries_per_passage": 3, "gpl_steps": 243, "neg_per_query": 50},
    "nfcorpus": {"new_size": 1816, "queries_per_passage": 4, "gpl_steps": 227, "neg_per_query": 50},
    "arguana": {"new_size": 2892, "queries_per_passage": 3, "gpl_steps": 271, "neg_per_query": 50}}
run_generation(DATASETS, CONFIGS_neg_query_50, tag="Neg_query_50")   # CORREGIDO: antes usaba CONFIGS_neg_query_40


# Training steps experiment
CONFIGS_steps_x2 = {
    "scifact": {"new_size": 2592, "queries_per_passage": 3 * 2, "gpl_steps": 243 * 2, "neg_per_query": 50},
    "nfcorpus": {"new_size": 1816, "queries_per_passage": 4 * 2, "gpl_steps": 227 * 2, "neg_per_query": 50},
    "arguana": {"new_size": 2892, "queries_per_passage": 3 * 2, "gpl_steps": 271 * 2, "neg_per_query": 50}}
run_generation(DATASETS, CONFIGS_steps_x2, tag="Step_x2")

CONFIGS_steps_x3 = {
    "scifact": {"new_size": 2592, "queries_per_passage": 3 * 3, "gpl_steps": 243 * 3, "neg_per_query": 50},
    "nfcorpus": {"new_size": 1816, "queries_per_passage": 4 * 3, "gpl_steps": 227 * 3, "neg_per_query": 50},
    "arguana": {"new_size": 2892, "queries_per_passage": 3 * 3, "gpl_steps": 271 * 3, "neg_per_query": 50}}
run_generation(DATASETS, CONFIGS_steps_x3, tag="Step_x3")

CONFIGS_steps_x4 = {
    "scifact": {"new_size": 2592, "queries_per_passage": 3 * 4, "gpl_steps": 243 * 4, "neg_per_query": 50},
    "nfcorpus": {"new_size": 1816, "queries_per_passage": 4 * 4, "gpl_steps": 227 * 4, "neg_per_query": 50},
    "arguana": {"new_size": 2892, "queries_per_passage": 3 * 4, "gpl_steps": 271 * 4, "neg_per_query": 50}}
run_generation(DATASETS, CONFIGS_steps_x4, tag="Step_x4")


TRAINING_EXPERIMENTS = [
    {"model_tag": "base", "gen_tag": "base", "lr": 2e-5, "scheduler": "constantlr", "rescale_range": (-2.0, 2.0)},

    # Negative mining models experiment
    {"model_tag": "base_neg10", "gen_tag": "Neg_query_10", "lr": 2e-5, "scheduler": "constantlr", "rescale_range": (-2.0, 2.0)},
    {"model_tag": "base_neg20", "gen_tag": "Neg_query_20", "lr": 2e-5, "scheduler": "constantlr", "rescale_range": (-2.0, 2.0)},
    {"model_tag": "base_neg30", "gen_tag": "Neg_query_30", "lr": 2e-5, "scheduler": "constantlr", "rescale_range": (-2.0, 2.0)},
    {"model_tag": "base_neg40", "gen_tag": "Neg_query_40", "lr": 2e-5, "scheduler": "constantlr", "rescale_range": (-2.0, 2.0)},

    # Experiment: increasing training steps and generated queries
    {"model_tag": "base_stepx4", "gen_tag": "Step_x4", "lr": 2e-5, "scheduler": "constantlr", "rescale_range": (-2.0, 2.0)},
]

for exp in TRAINING_EXPERIMENTS:

    model_dir = ROOT / f"models_{exp['model_tag']}"
    if model_dir.exists():
        print(f"Already trained, skipping: {exp['model_tag']}")
        continue

    run_training(
        datasets=DATASETS,
        students=STUDENTS,
        gen_tag=exp["gen_tag"],
        model_tag=exp["model_tag"],
        lr=exp["lr"],
        scheduler=exp["scheduler"],
        rescale_range=exp["rescale_range"],
    )