"""
Generate GPL training data for each dataset.

Steps for each dataset:
    A. Reduce the corpus size (resize)
    B. Generate synthetic queries using T5 (qgen)
    C. Copy corpus, queries, and qrels to the BM25 directory
    D. Dense variant: mine hard negatives using dense retrievers
       and generate pseudo-labels
    E. BM25 variant: mine hard negatives using BM25
       and generate pseudo-labels

If a step has already been completed (its output files exist), it is skipped.
Existing files are never overwritten.

Generated data is saved in:
    runs/data_generated/generated_<tag>/dense/<dataset>/
    runs/data_generated/generated_<tag>/bm25/<dataset>/

Usage from a notebook:
    from gpl_generate import run_generation
    run_generation(DATASETS, CONFIGS, tag="base")
"""
import shutil
from pathlib import Path


from beir.datasets.data_loader import GenericDataLoader
from gpl.toolkit import qgen, resize, NegativeMiner, PseudoLabeler
from huggingface_hub import snapshot_download
from transformers import set_seed


# 1. CONFIGURATION

WORK_DIR = Path(__file__).resolve().parent
ROOT = WORK_DIR / "runs"  

GENERATOR = "doc2query/msmarco-t5-base-v1"       
TEACHER = "cross-encoder/ms-marco-MiniLM-L6-v2" 
RETRIEVERS = [                                   
    "sentence-transformers/msmarco-distilbert-base-v3",
    "sentence-transformers/msmarco-MiniLM-L6-v3",
]

QGEN_PREFIX = "query_gen"

BATCH_GENERATION = 32
BATCH_GPL = 32
MAX_SEQ_LENGTH = 350
TRAINING_FILE = "gpl-training-data.tsv"

# 2. HELPER FUNCTIONS

def get_paths(tag, dataset_name):
    """Return the directories (dense, bm25) where a dataset's data is stored."""
    base = ROOT / "data_generated" / f"generated_{tag}"
    return base / "dense" / dataset_name, base / "bm25" / dataset_name


def labels_done(path):
    """Return True if pseudo-labels have already been generated in this directory."""
    return (path / TRAINING_FILE).exists()

def qgen_done(path):
    """Return True if the resized corpus and synthetic queries already exist."""
    return (path / "corpus.jsonl").exists() \
        and (path / f"{QGEN_PREFIX}-queries.jsonl").exists() \
        and (path / f"{QGEN_PREFIX}-qrels" / "train.tsv").exists()

def dataset_done(tag, dataset_name):
    """Return True if both variants (dense and BM25) have already been generated for the dataset."""
    dense_path, bm25_path = get_paths(tag, dataset_name)
    return labels_done(dense_path) and labels_done(bm25_path)


def download_models(model_names):
    """Download models from the Hub. Cached models are not downloaded again."""
    for model_name in model_names:
        snapshot_download(
            repo_id=model_name,
            max_workers=2,
            ignore_patterns=["*.onnx", "*.msgpack", "*.h5", "*.ot",
                 "onnx/*", "openvino/*", "*openvino*"])
        print(f"Downloaded: {model_name}")


def mine_and_label(path, retrievers, score_functions, gen_queries, corpus, gpl_steps, teacher, neg_per_query):
    """Mine hard negatives and generate pseudo-labels in a directory (dense or BM25)."""

    # Hard negatives: para cada query, documentos parecidos que NO son su positivo
    miner = NegativeMiner(
        generated_path=str(path),
        prefix=QGEN_PREFIX,
        retrievers=retrievers,
        retriever_score_functions=score_functions,
        nneg=neg_per_query,
    )
    miner.run()
    print("Hard negatives generated.")

    # Pseudo-labels: the cross-encoder scores (query, positive) and (query, negative)
    # pairs and stores the difference (margin) in gpl-training-data.tsv.
    # Generates gpl_steps * BATCH_GPL rows, corresponding to gpl_steps training steps.
    pseudo_labeler = PseudoLabeler(
        generated_path=str(path),
        gen_queries=gen_queries,
        corpus=corpus,
        total_steps=gpl_steps,
        batch_size=BATCH_GPL,
        cross_encoder=teacher,
        max_seq_length=MAX_SEQ_LENGTH,
    )
    pseudo_labeler.run()
    print("Pseudo labels generated.")

# 3. DATASET GENERATION

def generate_dataset(dataset_name, dataset_path, config, tag, generator, teacher, retrievers):
    """Generate all GPL training data (dense and BM25) for a dataset."""
    dense_path, bm25_path = get_paths(tag, dataset_name)

    if qgen_done(dense_path):
        print("Corpus and queries already exist, skipping resize + qgen.")
    else:
        # A. Reduce the corpus to a new_size documents
        resize(
            data_path=str(dataset_path),
            output_path=str(dense_path),
            new_size=config["new_size"])
        print("Corpus generated.")

        # B. Generate synthetic queries (and their qrels) from the resized corpus
        qgen(
            data_path=str(dense_path),
            output_dir=str(dense_path),
            generator_name_or_path=generator,
            ques_per_passage=config["queries_per_passage"],
            bsz=BATCH_GENERATION,
            qgen_prefix=QGEN_PREFIX,
        )
        print("Synthetic queries generated.")

    corpus, gen_queries, _ = GenericDataLoader(
        str(dense_path), prefix=QGEN_PREFIX).load(split="train")

    # C. The BM25 directory uses the same corpus, queries, and qrels
    bm25_path.mkdir(parents=True, exist_ok=True)
    for file_name in ["corpus.jsonl", f"{QGEN_PREFIX}-queries.jsonl"]:
        shutil.copy2(dense_path / file_name, bm25_path / file_name)
    shutil.copytree(
        dense_path / f"{QGEN_PREFIX}-qrels",
        bm25_path / f"{QGEN_PREFIX}-qrels",
        dirs_exist_ok=True)

    # D. Dense variant: hard negatives mined using dense retrievers (all with cos_sim)
    if labels_done(dense_path):
        print(f"\nDense already generated, skipping: {dataset_name}")
    else:
        print(f"\nGenerating dense: {dataset_name}")
        mine_and_label(dense_path, retrievers, ["cos_sim"] * len(retrievers),
                       gen_queries, corpus, config["gpl_steps"], teacher,config["neg_per_query"])

    # E. BM25 variant: hard negatives mined using BM25 (requires Elasticsearch)
    if labels_done(bm25_path):
        print(f"\nBM25 already generated, skipping: {dataset_name}")
    else:
        print(f"\nGenerating bm25: {dataset_name}")
        mine_and_label(bm25_path, ["bm25"], ["none"],
                       gen_queries, corpus, config["gpl_steps"], teacher,config["neg_per_query"])


# 4. MAIN FUNCTION (called from the notebook)

def run_generation(datasets, configs, tag, generator=GENERATOR, teacher=TEACHER,
                   retrievers=RETRIEVERS, seed=42):
    """
    Generate GPL training data for all datasets in an experiment.

    datasets:  {name: path to the original dataset}
    configs:   {name: {"new_size": ..., "queries_per_passage": ..., "gpl_steps": ..., "neg_per_query": ...}}
    tag:       experiment name; generated data is saved in runs/data_generated/generated_<tag>/
    seed:      random seed to ensure reproducible corpus resizing and query generation
    """
    download_models([generator, teacher, *retrievers])

    for dataset_name, dataset_path in datasets.items():
        print(f"\n{'=' * 50}")
        print(f"Generating data: {dataset_name} (tag: {tag})")
        print(f"{'=' * 50}")

        # If all data has already been generated, skip to the next dataset
        if dataset_done(tag, dataset_name):
            print(f"Already generated, skipping: {dataset_name}")
            continue

        set_seed(seed)
        generate_dataset(dataset_name, dataset_path, configs[dataset_name], tag,
                         generator, teacher, retrievers)
        print(f"\nGeneration completed: {dataset_name}")

    print("\nAll generation completed.")