"""
Train each student model using three methods:
    gpl      -> GPL (MarginMSE) with dense hard negatives
    genq     -> GenQ (MultipleNegativesRankingLoss) with synthetic queries
    gpl_bm25 -> GPL (MarginMSE) with BM25 hard negatives

Trained models are saved in:
    runs/Models/models_<model_tag>/<method>_<student>/<dataset>/

Usage from a notebook:
    from gpl_train import run_training
    run_training(DATASETS, STUDENTS, gen_tag="base", model_tag="base")
"""
import math

from beir.datasets.data_loader import GenericDataLoader
from beir.retrieval.train import TrainRetriever
from sentence_transformers import losses, models
from torch.utils.data import DataLoader

from gpl.toolkit import (
    load_sbert,
    MarginDistillationLoss,
    GenerativePseudoLabelingDataset,
    rescale_gpl_training_data,
)

from gpl_generate import ROOT, QGEN_PREFIX, get_paths


# 1. CONFIGURATION

BATCH_GPL = 32
BATCH_GENQ = 75
MAX_SEQ_LENGTH = 350

# Both student models normalize their embeddings, so their score margins lie in [-2, 2],
# while the cross-encoder produces logit margins (approximately [-15, 15]).
# Therefore, the teacher's margins are rescaled (using rescale_range in run_training).
GPL_SCORE_FUNCTION = "cos_sim"

WARMUP_RATIO = 0.1  # Only used with "warmup..." schedulers. GPL defaults to 1,000 warmup steps,
                    # but our training runs are shorter than that.

REQUIRED_FILES = [
    "corpus.jsonl",
    f"{QGEN_PREFIX}-queries.jsonl",
    f"{QGEN_PREFIX}-qrels/train.tsv",
    "hard-negatives.jsonl",
    "gpl-training-data.tsv",
]


def warmup_for(steps, scheduler):
    """Warmup steps: 0 for 'constantlr' and 10% of total training steps for other schedulers."""
    if scheduler.lower() == "constantlr":
        return 0
    return max(1, int(steps * WARMUP_RATIO))


# 2. PREPARE GPL TRAINING DATA

def prepare_gpl_data(path, rescale_range):
    """
    Check that all required files exist and rescale the margins if needed.
    Return the path to the .tsv file used for training.
    """
    missing = [f for f in REQUIRED_FILES if not (path / f).exists()]
    if missing:
        raise FileNotFoundError(f"Missing files in {path}: {missing}")

    if rescale_range is None:
        return path / "gpl-training-data.tsv"

    new_min, new_max = rescale_range

    suffix = f"rescaled_{new_min}_{new_max}"
    rescaled_file = path / f"gpl-training-data.{suffix}.tsv"
    if rescaled_file.exists():
        rescaled_file.unlink()

    print(f"Rescaling margins in {path} to [{new_min}, {new_max}]")
    rescale_gpl_training_data(str(path), new_min, new_max, suffix=suffix)
    return rescaled_file


# 3. GPL TRAINING (MarginMSE)

def train_gpl(data_path, gpl_data_file, student, output_dir, lr, scheduler):
    corpus, gen_queries, _ = GenericDataLoader(
        str(data_path), prefix=QGEN_PREFIX).load(split="train")

    train_dataset = GenerativePseudoLabelingDataset(str(gpl_data_file), gen_queries, corpus)
    train_dataloader = DataLoader(
        train_dataset, shuffle=False, batch_size=BATCH_GPL, drop_last=True)

    # One pass over all generated data (= the gpl_steps defined during generation)
    steps = len(train_dataloader)

    model = load_sbert(student, max_seq_length=MAX_SEQ_LENGTH)

    # Note: with "cos_sim", the GPL loss does NOT normalize embeddings (it only
    # computes the dot product). BGE and MiniLM already have a final Normalize layer;
    # if another student lacks one, we add it to ensure true cosine similarity.
    has_normalize = any(isinstance(module, models.Normalize) for module in model)
    if GPL_SCORE_FUNCTION == "cos_sim" and not has_normalize:
        model.append(models.Normalize())

    train_loss = MarginDistillationLoss(model=model, similarity_fct=GPL_SCORE_FUNCTION)

    warmup_steps = warmup_for(steps, scheduler)
    print(f"GPL steps: {steps} | scheduler: {scheduler} | warmup: {warmup_steps} | lr: {lr}")
    print(f"Data: {gpl_data_file}")

    model.fit(
        train_objectives=[(train_dataloader, train_loss)],
        epochs=1,
        steps_per_epoch=steps,
        scheduler=scheduler,
        warmup_steps=warmup_steps,
        optimizer_params={"lr": lr},
        output_path=str(output_dir),
        use_amp=False)


# 4. GENQ TRAINING (MultipleNegativesRankingLoss)

def train_genq(data_path, student, output_dir, lr, scheduler):
    corpus, gen_queries, gen_qrels = GenericDataLoader(
        str(data_path), prefix=QGEN_PREFIX).load(split="train")

    model = load_sbert(student, max_seq_length=MAX_SEQ_LENGTH)

    # Pairs (synthetic query, source passage); other passages in the batch serve as negatives
    retriever = TrainRetriever(model=model, batch_size=BATCH_GENQ)
    train_samples = retriever.load_train(corpus, gen_queries, gen_qrels)
    train_dataloader = retriever.prepare_train(train_samples, shuffle=True)
    train_loss = losses.MultipleNegativesRankingLoss(model=retriever.model)

    steps = math.ceil(len(train_samples) / BATCH_GENQ)
    warmup_steps = warmup_for(steps, scheduler)
    print(f"GenQ steps: {steps} | scheduler: {scheduler} | warmup: {warmup_steps} | lr: {lr}")

    retriever.fit(
        train_objectives=[(train_dataloader, train_loss)],
        epochs=1,
        scheduler=scheduler,
        warmup_steps=warmup_steps,
        optimizer_params={"lr": lr},
        output_path=str(output_dir),
        use_amp=False)


# 5. MAIN FUNCTION (called from the notebook)

def run_training(datasets, students, gen_tag, model_tag, lr=2e-5, scheduler="constantlr",
                 rescale_range=(-2.0, 2.0), methods=("gpl", "genq", "gpl_bm25")):
    """
    Train all student models using the specified methods across all datasets.

    datasets:      Dataset names (the same dictionary used in run_generation)
    students:      {short_name: Hugging Face model}
    gen_tag:       Generated data to use (runs/data_generated/generated_<gen_tag>/)
    model_tag:     Experiment name; models are saved in runs/Models/models_<model_tag>/
    lr:            Learning rate
    scheduler:     "constantlr", "warmupconstant", or "warmuplinear"
    rescale_range: Target range for rescaling margins (None = no rescaling)
    methods:       Training methods to use
    """
    for dataset_name in datasets:
        dense_path, bm25_path = get_paths(gen_tag, dataset_name)

        # Validate and rescale the data once per directory 
        if "gpl" in methods:
            dense_gpl_file = prepare_gpl_data(dense_path, rescale_range)
        if "gpl_bm25" in methods:
            bm25_gpl_file = prepare_gpl_data(bm25_path, rescale_range)

        for student_name, student in students.items():
            for method in methods:
                output_dir = ROOT /'Models'/ f"models_{model_tag}" / f"{method}_{student_name}" / dataset_name

                print(f"\n{'=' * 50}")
                print(f"Experiment: {model_tag} | Dataset: {dataset_name} | Model: {method}_{student_name}")
                print(f"{'=' * 50}")

                if method == "gpl":
                    train_gpl(dense_path, dense_gpl_file, student, output_dir, lr, scheduler)
                elif method == "genq":
                    train_genq(dense_path, student, output_dir, lr, scheduler)
                elif method == "gpl_bm25":
                    train_gpl(bm25_path, bm25_gpl_file, student, output_dir, lr, scheduler)


    print("\nAll training completed.")
