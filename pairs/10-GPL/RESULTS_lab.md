# Shared results table

Built by `build_table.py` from `baselines/scores.json` and `results_exp/results_*.json`: do not edit by hand.
A difference is in bold only when its p-value is below 0.05 and its confidence interval excludes zero.
Pair 00 is the instructor's worked example from the model presentation.

## SciFact

| Method | nDCG@10 | Recall@100 | Compared with | Δ nDCG@10 [95 % CI] | p |
|---|:-:|:-:|---|:-:|:-:|
| *BM25* | 0.676 | 0.918 | | | |
| *all-MiniLM-L6-v2* | 0.646 | 0.925 | | | |
| *bge-small-en-v1.5* | 0.710 | 0.948 | | | |
| *RRF (BM25 + MiniLM)* | 0.718 | 0.948 | | | |
| *BM25 top-100 + cross-encoder* | 0.688 | 0.918 | | | |
| genq_BGE (eval_base) vs bge ([10_GPL](results_exp/results_eval_base_genq_BGE_vs_bge.json)) | 0.672 | 0.938 | bge-small-en-v1.5 | **-0.038 [-0.059, -0.017]** | < 0.001 |
| genq_GPL_distilbert (eval_base) vs bge ([10_GPL](results_exp/results_eval_base_genq_GPL_distilbert_vs_bge.json)) | 0.596 | 0.894 | bge-small-en-v1.5 | **-0.114 [-0.148, -0.081]** | < 0.001 |
| genq_MiniLM (eval_base) vs minilm ([10_GPL](results_exp/results_eval_base_genq_MiniLM_vs_minilm.json)) | 0.641 | 0.929 | all-MiniLM-L6-v2 | -0.005 [-0.026, +0.016] | 0.651 |
| gpl_BGE (eval_base) vs bge ([10_GPL](results_exp/results_eval_base_gpl_BGE_vs_bge.json)) | 0.511 | 0.859 | bge-small-en-v1.5 | **-0.198 [-0.237, -0.160]** | < 0.001 |
| gpl_GPL_distilbert (eval_base) vs bge ([10_GPL](results_exp/results_eval_base_gpl_GPL_distilbert_vs_bge.json)) | 0.384 | 0.794 | bge-small-en-v1.5 | **-0.326 [-0.374, -0.279]** | < 0.001 |
| gpl_MiniLM (eval_base) vs minilm ([10_GPL](results_exp/results_eval_base_gpl_MiniLM_vs_minilm.json)) | 0.489 | 0.873 | all-MiniLM-L6-v2 | **-0.157 [-0.196, -0.118]** | < 0.001 |
| gpl_bm25_BGE (eval_base) vs bge ([10_GPL](results_exp/results_eval_base_gpl_bm25_BGE_vs_bge.json)) | 0.472 | 0.763 | bge-small-en-v1.5 | **-0.238 [-0.283, -0.194]** | < 0.001 |
| gpl_bm25_GPL_distilbert (eval_base) vs bge ([10_GPL](results_exp/results_eval_base_gpl_bm25_GPL_distilbert_vs_bge.json)) | 0.393 | 0.729 | bge-small-en-v1.5 | **-0.317 [-0.366, -0.269]** | < 0.001 |
| gpl_bm25_MiniLM (eval_base) vs minilm ([10_GPL](results_exp/results_eval_base_gpl_bm25_MiniLM_vs_minilm.json)) | 0.473 | 0.813 | all-MiniLM-L6-v2 | **-0.172 [-0.213, -0.131]** | < 0.001 |
| genq_BGE (eval_base_neg10) vs bge ([10_GPL](results_exp/results_eval_base_neg10_genq_BGE_vs_bge.json)) | 0.669 | 0.945 | bge-small-en-v1.5 | **-0.041 [-0.062, -0.019]** | < 0.001 |
| genq_GPL_distilbert (eval_base_neg10) vs bge ([10_GPL](results_exp/results_eval_base_neg10_genq_GPL_distilbert_vs_bge.json)) | 0.593 | 0.886 | bge-small-en-v1.5 | **-0.117 [-0.152, -0.084]** | < 0.001 |
| genq_MiniLM (eval_base_neg10) vs minilm ([10_GPL](results_exp/results_eval_base_neg10_genq_MiniLM_vs_minilm.json)) | 0.648 | 0.921 | all-MiniLM-L6-v2 | +0.003 [-0.018, +0.023] | 0.805 |
| gpl_BGE (eval_base_neg10) vs bge ([10_GPL](results_exp/results_eval_base_neg10_gpl_BGE_vs_bge.json)) | 0.498 | 0.843 | bge-small-en-v1.5 | **-0.212 [-0.254, -0.171]** | < 0.001 |
| gpl_GPL_distilbert (eval_base_neg10) vs bge ([10_GPL](results_exp/results_eval_base_neg10_gpl_GPL_distilbert_vs_bge.json)) | 0.379 | 0.764 | bge-small-en-v1.5 | **-0.331 [-0.379, -0.285]** | < 0.001 |
| gpl_MiniLM (eval_base_neg10) vs minilm ([10_GPL](results_exp/results_eval_base_neg10_gpl_MiniLM_vs_minilm.json)) | 0.501 | 0.845 | all-MiniLM-L6-v2 | **-0.144 [-0.184, -0.106]** | < 0.001 |
| gpl_bm25_BGE (eval_base_neg10) vs bge ([10_GPL](results_exp/results_eval_base_neg10_gpl_bm25_BGE_vs_bge.json)) | 0.466 | 0.742 | bge-small-en-v1.5 | **-0.244 [-0.289, -0.200]** | < 0.001 |
| gpl_bm25_GPL_distilbert (eval_base_neg10) vs bge ([10_GPL](results_exp/results_eval_base_neg10_gpl_bm25_GPL_distilbert_vs_bge.json)) | 0.376 | 0.703 | bge-small-en-v1.5 | **-0.334 [-0.383, -0.285]** | < 0.001 |
| gpl_bm25_MiniLM (eval_base_neg10) vs minilm ([10_GPL](results_exp/results_eval_base_neg10_gpl_bm25_MiniLM_vs_minilm.json)) | 0.448 | 0.769 | all-MiniLM-L6-v2 | **-0.198 [-0.240, -0.158]** | < 0.001 |
| genq_BGE (eval_base_neg20) vs bge ([10_GPL](results_exp/results_eval_base_neg20_genq_BGE_vs_bge.json)) | 0.670 | 0.942 | bge-small-en-v1.5 | **-0.039 [-0.060, -0.018]** | < 0.001 |
| genq_GPL_distilbert (eval_base_neg20) vs bge ([10_GPL](results_exp/results_eval_base_neg20_genq_GPL_distilbert_vs_bge.json)) | 0.597 | 0.895 | bge-small-en-v1.5 | **-0.113 [-0.148, -0.079]** | < 0.001 |
| genq_MiniLM (eval_base_neg20) vs minilm ([10_GPL](results_exp/results_eval_base_neg20_genq_MiniLM_vs_minilm.json)) | 0.654 | 0.927 | all-MiniLM-L6-v2 | +0.008 [-0.013, +0.029] | 0.441 |
| gpl_BGE (eval_base_neg20) vs bge ([10_GPL](results_exp/results_eval_base_neg20_gpl_BGE_vs_bge.json)) | 0.496 | 0.861 | bge-small-en-v1.5 | **-0.213 [-0.253, -0.174]** | < 0.001 |
| gpl_GPL_distilbert (eval_base_neg20) vs bge ([10_GPL](results_exp/results_eval_base_neg20_gpl_GPL_distilbert_vs_bge.json)) | 0.391 | 0.775 | bge-small-en-v1.5 | **-0.319 [-0.367, -0.274]** | < 0.001 |
| gpl_MiniLM (eval_base_neg20) vs minilm ([10_GPL](results_exp/results_eval_base_neg20_gpl_MiniLM_vs_minilm.json)) | 0.497 | 0.858 | all-MiniLM-L6-v2 | **-0.149 [-0.188, -0.111]** | < 0.001 |
| gpl_bm25_BGE (eval_base_neg20) vs bge ([10_GPL](results_exp/results_eval_base_neg20_gpl_bm25_BGE_vs_bge.json)) | 0.448 | 0.756 | bge-small-en-v1.5 | **-0.262 [-0.308, -0.218]** | < 0.001 |
| gpl_bm25_GPL_distilbert (eval_base_neg20) vs bge ([10_GPL](results_exp/results_eval_base_neg20_gpl_bm25_GPL_distilbert_vs_bge.json)) | 0.377 | 0.698 | bge-small-en-v1.5 | **-0.333 [-0.383, -0.284]** | < 0.001 |
| gpl_bm25_MiniLM (eval_base_neg20) vs minilm ([10_GPL](results_exp/results_eval_base_neg20_gpl_bm25_MiniLM_vs_minilm.json)) | 0.457 | 0.791 | all-MiniLM-L6-v2 | **-0.189 [-0.232, -0.147]** | < 0.001 |
| genq_BGE (eval_base_neg30) vs bge ([10_GPL](results_exp/results_eval_base_neg30_genq_BGE_vs_bge.json)) | 0.671 | 0.946 | bge-small-en-v1.5 | **-0.038 [-0.059, -0.018]** | < 0.001 |
| genq_GPL_distilbert (eval_base_neg30) vs bge ([10_GPL](results_exp/results_eval_base_neg30_genq_GPL_distilbert_vs_bge.json)) | 0.604 | 0.890 | bge-small-en-v1.5 | **-0.106 [-0.139, -0.073]** | < 0.001 |
| genq_MiniLM (eval_base_neg30) vs minilm ([10_GPL](results_exp/results_eval_base_neg30_genq_MiniLM_vs_minilm.json)) | 0.651 | 0.927 | all-MiniLM-L6-v2 | +0.006 [-0.016, +0.028] | 0.591 |
| gpl_BGE (eval_base_neg30) vs bge ([10_GPL](results_exp/results_eval_base_neg30_gpl_BGE_vs_bge.json)) | 0.499 | 0.842 | bge-small-en-v1.5 | **-0.211 [-0.252, -0.171]** | < 0.001 |
| gpl_GPL_distilbert (eval_base_neg30) vs bge ([10_GPL](results_exp/results_eval_base_neg30_gpl_GPL_distilbert_vs_bge.json)) | 0.377 | 0.744 | bge-small-en-v1.5 | **-0.333 [-0.381, -0.286]** | < 0.001 |
| gpl_MiniLM (eval_base_neg30) vs minilm ([10_GPL](results_exp/results_eval_base_neg30_gpl_MiniLM_vs_minilm.json)) | 0.489 | 0.867 | all-MiniLM-L6-v2 | **-0.157 [-0.196, -0.119]** | < 0.001 |
| gpl_bm25_BGE (eval_base_neg30) vs bge ([10_GPL](results_exp/results_eval_base_neg30_gpl_bm25_BGE_vs_bge.json)) | 0.461 | 0.770 | bge-small-en-v1.5 | **-0.249 [-0.294, -0.204]** | < 0.001 |
| gpl_bm25_GPL_distilbert (eval_base_neg30) vs bge ([10_GPL](results_exp/results_eval_base_neg30_gpl_bm25_GPL_distilbert_vs_bge.json)) | 0.393 | 0.733 | bge-small-en-v1.5 | **-0.317 [-0.365, -0.270]** | < 0.001 |
| gpl_bm25_MiniLM (eval_base_neg30) vs minilm ([10_GPL](results_exp/results_eval_base_neg30_gpl_bm25_MiniLM_vs_minilm.json)) | 0.465 | 0.820 | all-MiniLM-L6-v2 | **-0.180 [-0.223, -0.138]** | < 0.001 |
| genq_BGE (eval_base_neg40) vs bge ([10_GPL](results_exp/results_eval_base_neg40_genq_BGE_vs_bge.json)) | 0.672 | 0.941 | bge-small-en-v1.5 | **-0.038 [-0.059, -0.018]** | < 0.001 |
| genq_GPL_distilbert (eval_base_neg40) vs bge ([10_GPL](results_exp/results_eval_base_neg40_genq_GPL_distilbert_vs_bge.json)) | 0.586 | 0.894 | bge-small-en-v1.5 | **-0.124 [-0.160, -0.090]** | < 0.001 |
| genq_MiniLM (eval_base_neg40) vs minilm ([10_GPL](results_exp/results_eval_base_neg40_genq_MiniLM_vs_minilm.json)) | 0.649 | 0.923 | all-MiniLM-L6-v2 | +0.003 [-0.018, +0.025] | 0.767 |
| gpl_BGE (eval_base_neg40) vs bge ([10_GPL](results_exp/results_eval_base_neg40_gpl_BGE_vs_bge.json)) | 0.506 | 0.860 | bge-small-en-v1.5 | **-0.203 [-0.244, -0.164]** | < 0.001 |
| gpl_GPL_distilbert (eval_base_neg40) vs bge ([10_GPL](results_exp/results_eval_base_neg40_gpl_GPL_distilbert_vs_bge.json)) | 0.386 | 0.787 | bge-small-en-v1.5 | **-0.324 [-0.373, -0.276]** | < 0.001 |
| gpl_MiniLM (eval_base_neg40) vs minilm ([10_GPL](results_exp/results_eval_base_neg40_gpl_MiniLM_vs_minilm.json)) | 0.468 | 0.862 | all-MiniLM-L6-v2 | **-0.177 [-0.216, -0.139]** | < 0.001 |
| gpl_bm25_BGE (eval_base_neg40) vs bge ([10_GPL](results_exp/results_eval_base_neg40_gpl_bm25_BGE_vs_bge.json)) | 0.463 | 0.756 | bge-small-en-v1.5 | **-0.247 [-0.293, -0.204]** | < 0.001 |
| gpl_bm25_GPL_distilbert (eval_base_neg40) vs bge ([10_GPL](results_exp/results_eval_base_neg40_gpl_bm25_GPL_distilbert_vs_bge.json)) | 0.376 | 0.708 | bge-small-en-v1.5 | **-0.334 [-0.383, -0.286]** | < 0.001 |
| gpl_bm25_MiniLM (eval_base_neg40) vs minilm ([10_GPL](results_exp/results_eval_base_neg40_gpl_bm25_MiniLM_vs_minilm.json)) | 0.462 | 0.796 | all-MiniLM-L6-v2 | **-0.184 [-0.226, -0.142]** | < 0.001 |
| genq_BGE (eval_base_stepx4) vs bge ([10_GPL](results_exp/results_eval_base_stepx4_genq_BGE_vs_bge.json)) | 0.669 | 0.943 | bge-small-en-v1.5 | **-0.041 [-0.062, -0.021]** | < 0.001 |
| genq_GPL_distilbert (eval_base_stepx4) vs bge ([10_GPL](results_exp/results_eval_base_stepx4_genq_GPL_distilbert_vs_bge.json)) | 0.606 | 0.894 | bge-small-en-v1.5 | **-0.104 [-0.138, -0.071]** | < 0.001 |
| genq_MiniLM (eval_base_stepx4) vs minilm ([10_GPL](results_exp/results_eval_base_stepx4_genq_MiniLM_vs_minilm.json)) | 0.650 | 0.938 | all-MiniLM-L6-v2 | +0.004 [-0.014, +0.023] | 0.658 |
| gpl_BGE (eval_base_stepx4) vs bge ([10_GPL](results_exp/results_eval_base_stepx4_gpl_BGE_vs_bge.json)) | 0.446 | 0.806 | bge-small-en-v1.5 | **-0.264 [-0.308, -0.221]** | < 0.001 |
| gpl_GPL_distilbert (eval_base_stepx4) vs bge ([10_GPL](results_exp/results_eval_base_stepx4_gpl_GPL_distilbert_vs_bge.json)) | 0.366 | 0.728 | bge-small-en-v1.5 | **-0.344 [-0.392, -0.295]** | < 0.001 |
| gpl_MiniLM (eval_base_stepx4) vs minilm ([10_GPL](results_exp/results_eval_base_stepx4_gpl_MiniLM_vs_minilm.json)) | 0.438 | 0.821 | all-MiniLM-L6-v2 | **-0.207 [-0.250, -0.166]** | < 0.001 |
| gpl_bm25_BGE (eval_base_stepx4) vs bge ([10_GPL](results_exp/results_eval_base_stepx4_gpl_bm25_BGE_vs_bge.json)) | 0.436 | 0.771 | bge-small-en-v1.5 | **-0.274 [-0.320, -0.230]** | < 0.001 |
| gpl_bm25_GPL_distilbert (eval_base_stepx4) vs bge ([10_GPL](results_exp/results_eval_base_stepx4_gpl_bm25_GPL_distilbert_vs_bge.json)) | 0.380 | 0.715 | bge-small-en-v1.5 | **-0.330 [-0.378, -0.283]** | < 0.001 |
| gpl_bm25_MiniLM (eval_base_stepx4) vs minilm ([10_GPL](results_exp/results_eval_base_stepx4_gpl_bm25_MiniLM_vs_minilm.json)) | 0.468 | 0.804 | all-MiniLM-L6-v2 | **-0.178 [-0.219, -0.138]** | < 0.001 |

## NFCorpus

| Method | nDCG@10 | Recall@100 | Compared with | Δ nDCG@10 [95 % CI] | p |
|---|:-:|:-:|---|:-:|:-:|
| *BM25* | 0.321 | 0.246 | | | |
| *all-MiniLM-L6-v2* | 0.316 | 0.311 | | | |
| *bge-small-en-v1.5* | 0.340 | 0.304 | | | |
| *RRF (BM25 + MiniLM)* | 0.342 | 0.310 | | | |
| *BM25 top-100 + cross-encoder* | 0.347 | 0.246 | | | |
| genq_BGE (eval_base) vs bge ([10_GPL](results_exp/results_eval_base_genq_BGE_vs_bge.json)) | 0.346 | 0.329 | bge-small-en-v1.5 | +0.006 [-0.004, +0.015] | 0.241 |
| genq_GPL_distilbert (eval_base) vs bge ([10_GPL](results_exp/results_eval_base_genq_GPL_distilbert_vs_bge.json)) | 0.289 | 0.252 | bge-small-en-v1.5 | **-0.052 [-0.070, -0.035]** | < 0.001 |
| genq_MiniLM (eval_base) vs minilm ([10_GPL](results_exp/results_eval_base_genq_MiniLM_vs_minilm.json)) | 0.324 | 0.305 | all-MiniLM-L6-v2 | +0.008 [-0.002, +0.018] | 0.125 |
| gpl_BGE (eval_base) vs bge ([10_GPL](results_exp/results_eval_base_gpl_BGE_vs_bge.json)) | 0.303 | 0.275 | bge-small-en-v1.5 | **-0.038 [-0.054, -0.021]** | < 0.001 |
| gpl_GPL_distilbert (eval_base) vs bge ([10_GPL](results_exp/results_eval_base_gpl_GPL_distilbert_vs_bge.json)) | 0.244 | 0.210 | bge-small-en-v1.5 | **-0.097 [-0.119, -0.075]** | < 0.001 |
| gpl_MiniLM (eval_base) vs minilm ([10_GPL](results_exp/results_eval_base_gpl_MiniLM_vs_minilm.json)) | 0.288 | 0.266 | all-MiniLM-L6-v2 | **-0.028 [-0.043, -0.013]** | < 0.001 |
| gpl_bm25_BGE (eval_base) vs bge ([10_GPL](results_exp/results_eval_base_gpl_bm25_BGE_vs_bge.json)) | 0.310 | 0.269 | bge-small-en-v1.5 | **-0.030 [-0.048, -0.013]** | < 0.001 |
| gpl_bm25_GPL_distilbert (eval_base) vs bge ([10_GPL](results_exp/results_eval_base_gpl_bm25_GPL_distilbert_vs_bge.json)) | 0.245 | 0.211 | bge-small-en-v1.5 | **-0.095 [-0.118, -0.073]** | < 0.001 |
| gpl_bm25_MiniLM (eval_base) vs minilm ([10_GPL](results_exp/results_eval_base_gpl_bm25_MiniLM_vs_minilm.json)) | 0.290 | 0.270 | all-MiniLM-L6-v2 | **-0.026 [-0.041, -0.012]** | < 0.001 |
| genq_BGE (eval_base_neg10) vs bge ([10_GPL](results_exp/results_eval_base_neg10_genq_BGE_vs_bge.json)) | 0.341 | 0.324 | bge-small-en-v1.5 | +0.001 [-0.009, +0.010] | 0.903 |
| genq_GPL_distilbert (eval_base_neg10) vs bge ([10_GPL](results_exp/results_eval_base_neg10_genq_GPL_distilbert_vs_bge.json)) | 0.289 | 0.249 | bge-small-en-v1.5 | **-0.051 [-0.069, -0.033]** | < 0.001 |
| genq_MiniLM (eval_base_neg10) vs minilm ([10_GPL](results_exp/results_eval_base_neg10_genq_MiniLM_vs_minilm.json)) | 0.325 | 0.304 | all-MiniLM-L6-v2 | +0.008 [-0.002, +0.019] | 0.113 |
| gpl_BGE (eval_base_neg10) vs bge ([10_GPL](results_exp/results_eval_base_neg10_gpl_BGE_vs_bge.json)) | 0.304 | 0.271 | bge-small-en-v1.5 | **-0.036 [-0.052, -0.020]** | < 0.001 |
| gpl_GPL_distilbert (eval_base_neg10) vs bge ([10_GPL](results_exp/results_eval_base_neg10_gpl_GPL_distilbert_vs_bge.json)) | 0.247 | 0.203 | bge-small-en-v1.5 | **-0.093 [-0.115, -0.072]** | < 0.001 |
| gpl_MiniLM (eval_base_neg10) vs minilm ([10_GPL](results_exp/results_eval_base_neg10_gpl_MiniLM_vs_minilm.json)) | 0.293 | 0.274 | all-MiniLM-L6-v2 | **-0.023 [-0.037, -0.009]** | 0.002 |
| gpl_bm25_BGE (eval_base_neg10) vs bge ([10_GPL](results_exp/results_eval_base_neg10_gpl_bm25_BGE_vs_bge.json)) | 0.310 | 0.260 | bge-small-en-v1.5 | **-0.030 [-0.046, -0.014]** | < 0.001 |
| gpl_bm25_GPL_distilbert (eval_base_neg10) vs bge ([10_GPL](results_exp/results_eval_base_neg10_gpl_bm25_GPL_distilbert_vs_bge.json)) | 0.252 | 0.207 | bge-small-en-v1.5 | **-0.088 [-0.110, -0.067]** | < 0.001 |
| gpl_bm25_MiniLM (eval_base_neg10) vs minilm ([10_GPL](results_exp/results_eval_base_neg10_gpl_bm25_MiniLM_vs_minilm.json)) | 0.292 | 0.260 | all-MiniLM-L6-v2 | **-0.024 [-0.038, -0.010]** | 0.001 |
| genq_BGE (eval_base_neg20) vs bge ([10_GPL](results_exp/results_eval_base_neg20_genq_BGE_vs_bge.json)) | 0.344 | 0.321 | bge-small-en-v1.5 | +0.003 [-0.006, +0.013] | 0.471 |
| genq_GPL_distilbert (eval_base_neg20) vs bge ([10_GPL](results_exp/results_eval_base_neg20_genq_GPL_distilbert_vs_bge.json)) | 0.290 | 0.249 | bge-small-en-v1.5 | **-0.050 [-0.068, -0.033]** | < 0.001 |
| genq_MiniLM (eval_base_neg20) vs minilm ([10_GPL](results_exp/results_eval_base_neg20_genq_MiniLM_vs_minilm.json)) | 0.332 | 0.302 | all-MiniLM-L6-v2 | **+0.015 [+0.004, +0.028]** | 0.009 |
| gpl_BGE (eval_base_neg20) vs bge ([10_GPL](results_exp/results_eval_base_neg20_gpl_BGE_vs_bge.json)) | 0.302 | 0.271 | bge-small-en-v1.5 | **-0.039 [-0.056, -0.022]** | < 0.001 |
| gpl_GPL_distilbert (eval_base_neg20) vs bge ([10_GPL](results_exp/results_eval_base_neg20_gpl_GPL_distilbert_vs_bge.json)) | 0.243 | 0.208 | bge-small-en-v1.5 | **-0.097 [-0.120, -0.075]** | < 0.001 |
| gpl_MiniLM (eval_base_neg20) vs minilm ([10_GPL](results_exp/results_eval_base_neg20_gpl_MiniLM_vs_minilm.json)) | 0.292 | 0.267 | all-MiniLM-L6-v2 | **-0.024 [-0.039, -0.010]** | 0.001 |
| gpl_bm25_BGE (eval_base_neg20) vs bge ([10_GPL](results_exp/results_eval_base_neg20_gpl_bm25_BGE_vs_bge.json)) | 0.304 | 0.257 | bge-small-en-v1.5 | **-0.036 [-0.052, -0.019]** | < 0.001 |
| gpl_bm25_GPL_distilbert (eval_base_neg20) vs bge ([10_GPL](results_exp/results_eval_base_neg20_gpl_bm25_GPL_distilbert_vs_bge.json)) | 0.246 | 0.207 | bge-small-en-v1.5 | **-0.095 [-0.116, -0.073]** | < 0.001 |
| gpl_bm25_MiniLM (eval_base_neg20) vs minilm ([10_GPL](results_exp/results_eval_base_neg20_gpl_bm25_MiniLM_vs_minilm.json)) | 0.291 | 0.264 | all-MiniLM-L6-v2 | **-0.025 [-0.040, -0.011]** | < 0.001 |
| genq_BGE (eval_base_neg30) vs bge ([10_GPL](results_exp/results_eval_base_neg30_genq_BGE_vs_bge.json)) | 0.343 | 0.323 | bge-small-en-v1.5 | +0.003 [-0.007, +0.013] | 0.570 |
| genq_GPL_distilbert (eval_base_neg30) vs bge ([10_GPL](results_exp/results_eval_base_neg30_genq_GPL_distilbert_vs_bge.json)) | 0.289 | 0.249 | bge-small-en-v1.5 | **-0.051 [-0.069, -0.034]** | < 0.001 |
| genq_MiniLM (eval_base_neg30) vs minilm ([10_GPL](results_exp/results_eval_base_neg30_genq_MiniLM_vs_minilm.json)) | 0.324 | 0.304 | all-MiniLM-L6-v2 | +0.008 [-0.001, +0.018] | 0.091 |
| gpl_BGE (eval_base_neg30) vs bge ([10_GPL](results_exp/results_eval_base_neg30_gpl_BGE_vs_bge.json)) | 0.305 | 0.281 | bge-small-en-v1.5 | **-0.035 [-0.053, -0.018]** | < 0.001 |
| gpl_GPL_distilbert (eval_base_neg30) vs bge ([10_GPL](results_exp/results_eval_base_neg30_gpl_GPL_distilbert_vs_bge.json)) | 0.246 | 0.208 | bge-small-en-v1.5 | **-0.094 [-0.117, -0.072]** | < 0.001 |
| gpl_MiniLM (eval_base_neg30) vs minilm ([10_GPL](results_exp/results_eval_base_neg30_gpl_MiniLM_vs_minilm.json)) | 0.293 | 0.269 | all-MiniLM-L6-v2 | **-0.023 [-0.038, -0.009]** | 0.002 |
| gpl_bm25_BGE (eval_base_neg30) vs bge ([10_GPL](results_exp/results_eval_base_neg30_gpl_bm25_BGE_vs_bge.json)) | 0.310 | 0.259 | bge-small-en-v1.5 | **-0.030 [-0.046, -0.013]** | < 0.001 |
| gpl_bm25_GPL_distilbert (eval_base_neg30) vs bge ([10_GPL](results_exp/results_eval_base_neg30_gpl_bm25_GPL_distilbert_vs_bge.json)) | 0.250 | 0.212 | bge-small-en-v1.5 | **-0.090 [-0.112, -0.069]** | < 0.001 |
| gpl_bm25_MiniLM (eval_base_neg30) vs minilm ([10_GPL](results_exp/results_eval_base_neg30_gpl_bm25_MiniLM_vs_minilm.json)) | 0.291 | 0.262 | all-MiniLM-L6-v2 | **-0.025 [-0.039, -0.012]** | < 0.001 |
| genq_BGE (eval_base_neg40) vs bge ([10_GPL](results_exp/results_eval_base_neg40_genq_BGE_vs_bge.json)) | 0.342 | 0.326 | bge-small-en-v1.5 | +0.002 [-0.007, +0.011] | 0.706 |
| genq_GPL_distilbert (eval_base_neg40) vs bge ([10_GPL](results_exp/results_eval_base_neg40_genq_GPL_distilbert_vs_bge.json)) | 0.292 | 0.251 | bge-small-en-v1.5 | **-0.049 [-0.066, -0.031]** | < 0.001 |
| genq_MiniLM (eval_base_neg40) vs minilm ([10_GPL](results_exp/results_eval_base_neg40_genq_MiniLM_vs_minilm.json)) | 0.328 | 0.308 | all-MiniLM-L6-v2 | **+0.012 [+0.001, +0.023]** | 0.027 |
| gpl_BGE (eval_base_neg40) vs bge ([10_GPL](results_exp/results_eval_base_neg40_gpl_BGE_vs_bge.json)) | 0.301 | 0.272 | bge-small-en-v1.5 | **-0.039 [-0.057, -0.021]** | < 0.001 |
| gpl_GPL_distilbert (eval_base_neg40) vs bge ([10_GPL](results_exp/results_eval_base_neg40_gpl_GPL_distilbert_vs_bge.json)) | 0.244 | 0.202 | bge-small-en-v1.5 | **-0.096 [-0.119, -0.075]** | < 0.001 |
| gpl_MiniLM (eval_base_neg40) vs minilm ([10_GPL](results_exp/results_eval_base_neg40_gpl_MiniLM_vs_minilm.json)) | 0.283 | 0.263 | all-MiniLM-L6-v2 | **-0.034 [-0.049, -0.018]** | < 0.001 |
| gpl_bm25_BGE (eval_base_neg40) vs bge ([10_GPL](results_exp/results_eval_base_neg40_gpl_bm25_BGE_vs_bge.json)) | 0.310 | 0.264 | bge-small-en-v1.5 | **-0.030 [-0.047, -0.013]** | < 0.001 |
| gpl_bm25_GPL_distilbert (eval_base_neg40) vs bge ([10_GPL](results_exp/results_eval_base_neg40_gpl_bm25_GPL_distilbert_vs_bge.json)) | 0.251 | 0.210 | bge-small-en-v1.5 | **-0.089 [-0.111, -0.068]** | < 0.001 |
| gpl_bm25_MiniLM (eval_base_neg40) vs minilm ([10_GPL](results_exp/results_eval_base_neg40_gpl_bm25_MiniLM_vs_minilm.json)) | 0.290 | 0.270 | all-MiniLM-L6-v2 | **-0.026 [-0.041, -0.011]** | < 0.001 |
| genq_BGE (eval_base_stepx4) vs bge ([10_GPL](results_exp/results_eval_base_stepx4_genq_BGE_vs_bge.json)) | 0.346 | 0.321 | bge-small-en-v1.5 | +0.006 [-0.004, +0.015] | 0.247 |
| genq_GPL_distilbert (eval_base_stepx4) vs bge ([10_GPL](results_exp/results_eval_base_stepx4_genq_GPL_distilbert_vs_bge.json)) | 0.298 | 0.261 | bge-small-en-v1.5 | **-0.042 [-0.059, -0.026]** | < 0.001 |
| genq_MiniLM (eval_base_stepx4) vs minilm ([10_GPL](results_exp/results_eval_base_stepx4_genq_MiniLM_vs_minilm.json)) | 0.327 | 0.303 | all-MiniLM-L6-v2 | **+0.011 [+0.000, +0.022]** | 0.049 |
| gpl_BGE (eval_base_stepx4) vs bge ([10_GPL](results_exp/results_eval_base_stepx4_gpl_BGE_vs_bge.json)) | 0.289 | 0.263 | bge-small-en-v1.5 | **-0.051 [-0.070, -0.033]** | < 0.001 |
| gpl_GPL_distilbert (eval_base_stepx4) vs bge ([10_GPL](results_exp/results_eval_base_stepx4_gpl_GPL_distilbert_vs_bge.json)) | 0.240 | 0.209 | bge-small-en-v1.5 | **-0.101 [-0.123, -0.079]** | < 0.001 |
| gpl_MiniLM (eval_base_stepx4) vs minilm ([10_GPL](results_exp/results_eval_base_stepx4_gpl_MiniLM_vs_minilm.json)) | 0.267 | 0.243 | all-MiniLM-L6-v2 | **-0.049 [-0.067, -0.032]** | < 0.001 |
| gpl_bm25_BGE (eval_base_stepx4) vs bge ([10_GPL](results_exp/results_eval_base_stepx4_gpl_bm25_BGE_vs_bge.json)) | 0.291 | 0.243 | bge-small-en-v1.5 | **-0.050 [-0.069, -0.030]** | < 0.001 |
| gpl_bm25_GPL_distilbert (eval_base_stepx4) vs bge ([10_GPL](results_exp/results_eval_base_stepx4_gpl_bm25_GPL_distilbert_vs_bge.json)) | 0.238 | 0.200 | bge-small-en-v1.5 | **-0.102 [-0.124, -0.080]** | < 0.001 |
| gpl_bm25_MiniLM (eval_base_stepx4) vs minilm ([10_GPL](results_exp/results_eval_base_stepx4_gpl_bm25_MiniLM_vs_minilm.json)) | 0.274 | 0.240 | all-MiniLM-L6-v2 | **-0.042 [-0.059, -0.025]** | < 0.001 |

## ArguAna

| Method | nDCG@10 | Recall@100 | Compared with | Δ nDCG@10 [95 % CI] | p |
|---|:-:|:-:|---|:-:|:-:|
| *BM25* | 0.516 | 0.969 | | | |
| *all-MiniLM-L6-v2* | 0.503 | 0.977 | | | |
| *bge-small-en-v1.5* | 0.606 | 0.986 | | | |
| *RRF (BM25 + MiniLM)* | 0.549 | 0.985 | | | |
| *BM25 top-100 + cross-encoder* | 0.422 | 0.969 | | | |
| genq_BGE (eval_base) vs bge ([10_GPL](results_exp/results_eval_base_genq_BGE_vs_bge.json)) | 0.508 | 0.982 | bge-small-en-v1.5 | **-0.098 [-0.112, -0.084]** | < 0.001 |
| genq_GPL_distilbert (eval_base) vs bge ([10_GPL](results_exp/results_eval_base_genq_GPL_distilbert_vs_bge.json)) | 0.476 | 0.972 | bge-small-en-v1.5 | **-0.130 [-0.147, -0.114]** | < 0.001 |
| genq_MiniLM (eval_base) vs minilm ([10_GPL](results_exp/results_eval_base_genq_MiniLM_vs_minilm.json)) | 0.514 | 0.979 | all-MiniLM-L6-v2 | +0.011 [-0.001, +0.023] | 0.065 |
| gpl_BGE (eval_base) vs bge ([10_GPL](results_exp/results_eval_base_gpl_BGE_vs_bge.json)) | 0.360 | 0.900 | bge-small-en-v1.5 | **-0.246 [-0.266, -0.225]** | < 0.001 |
| gpl_GPL_distilbert (eval_base) vs bge ([10_GPL](results_exp/results_eval_base_gpl_GPL_distilbert_vs_bge.json)) | 0.330 | 0.889 | bge-small-en-v1.5 | **-0.276 [-0.296, -0.254]** | < 0.001 |
| gpl_MiniLM (eval_base) vs minilm ([10_GPL](results_exp/results_eval_base_gpl_MiniLM_vs_minilm.json)) | 0.372 | 0.922 | all-MiniLM-L6-v2 | **-0.131 [-0.150, -0.112]** | < 0.001 |
| gpl_bm25_BGE (eval_base) vs bge ([10_GPL](results_exp/results_eval_base_gpl_bm25_BGE_vs_bge.json)) | 0.371 | 0.907 | bge-small-en-v1.5 | **-0.235 [-0.255, -0.215]** | < 0.001 |
| gpl_bm25_GPL_distilbert (eval_base) vs bge ([10_GPL](results_exp/results_eval_base_gpl_bm25_GPL_distilbert_vs_bge.json)) | 0.363 | 0.901 | bge-small-en-v1.5 | **-0.242 [-0.263, -0.222]** | < 0.001 |
| gpl_bm25_MiniLM (eval_base) vs minilm ([10_GPL](results_exp/results_eval_base_gpl_bm25_MiniLM_vs_minilm.json)) | 0.409 | 0.954 | all-MiniLM-L6-v2 | **-0.094 [-0.112, -0.076]** | < 0.001 |
| genq_BGE (eval_base_neg10) vs bge ([10_GPL](results_exp/results_eval_base_neg10_genq_BGE_vs_bge.json)) | 0.524 | 0.983 | bge-small-en-v1.5 | **-0.082 [-0.095, -0.068]** | < 0.001 |
| genq_GPL_distilbert (eval_base_neg10) vs bge ([10_GPL](results_exp/results_eval_base_neg10_genq_GPL_distilbert_vs_bge.json)) | 0.471 | 0.972 | bge-small-en-v1.5 | **-0.135 [-0.152, -0.118]** | < 0.001 |
| genq_MiniLM (eval_base_neg10) vs minilm ([10_GPL](results_exp/results_eval_base_neg10_genq_MiniLM_vs_minilm.json)) | 0.521 | 0.981 | all-MiniLM-L6-v2 | **+0.018 [+0.007, +0.030]** | 0.002 |
| gpl_BGE (eval_base_neg10) vs bge ([10_GPL](results_exp/results_eval_base_neg10_gpl_BGE_vs_bge.json)) | 0.378 | 0.896 | bge-small-en-v1.5 | **-0.228 [-0.248, -0.208]** | < 0.001 |
| gpl_GPL_distilbert (eval_base_neg10) vs bge ([10_GPL](results_exp/results_eval_base_neg10_gpl_GPL_distilbert_vs_bge.json)) | 0.352 | 0.875 | bge-small-en-v1.5 | **-0.254 [-0.274, -0.233]** | < 0.001 |
| gpl_MiniLM (eval_base_neg10) vs minilm ([10_GPL](results_exp/results_eval_base_neg10_gpl_MiniLM_vs_minilm.json)) | 0.374 | 0.912 | all-MiniLM-L6-v2 | **-0.128 [-0.146, -0.110]** | < 0.001 |
| gpl_bm25_BGE (eval_base_neg10) vs bge ([10_GPL](results_exp/results_eval_base_neg10_gpl_bm25_BGE_vs_bge.json)) | 0.390 | 0.925 | bge-small-en-v1.5 | **-0.216 [-0.235, -0.196]** | < 0.001 |
| gpl_bm25_GPL_distilbert (eval_base_neg10) vs bge ([10_GPL](results_exp/results_eval_base_neg10_gpl_bm25_GPL_distilbert_vs_bge.json)) | 0.378 | 0.927 | bge-small-en-v1.5 | **-0.228 [-0.248, -0.208]** | < 0.001 |
| gpl_bm25_MiniLM (eval_base_neg10) vs minilm ([10_GPL](results_exp/results_eval_base_neg10_gpl_bm25_MiniLM_vs_minilm.json)) | 0.401 | 0.951 | all-MiniLM-L6-v2 | **-0.102 [-0.119, -0.084]** | < 0.001 |
| genq_BGE (eval_base_neg20) vs bge ([10_GPL](results_exp/results_eval_base_neg20_genq_BGE_vs_bge.json)) | 0.508 | 0.982 | bge-small-en-v1.5 | **-0.098 [-0.111, -0.084]** | < 0.001 |
| genq_GPL_distilbert (eval_base_neg20) vs bge ([10_GPL](results_exp/results_eval_base_neg20_genq_GPL_distilbert_vs_bge.json)) | 0.461 | 0.971 | bge-small-en-v1.5 | **-0.145 [-0.162, -0.128]** | < 0.001 |
| genq_MiniLM (eval_base_neg20) vs minilm ([10_GPL](results_exp/results_eval_base_neg20_genq_MiniLM_vs_minilm.json)) | 0.524 | 0.982 | all-MiniLM-L6-v2 | **+0.022 [+0.010, +0.033]** | < 0.001 |
| gpl_BGE (eval_base_neg20) vs bge ([10_GPL](results_exp/results_eval_base_neg20_gpl_BGE_vs_bge.json)) | 0.349 | 0.888 | bge-small-en-v1.5 | **-0.257 [-0.277, -0.236]** | < 0.001 |
| gpl_GPL_distilbert (eval_base_neg20) vs bge ([10_GPL](results_exp/results_eval_base_neg20_gpl_GPL_distilbert_vs_bge.json)) | 0.328 | 0.870 | bge-small-en-v1.5 | **-0.278 [-0.298, -0.257]** | < 0.001 |
| gpl_MiniLM (eval_base_neg20) vs minilm ([10_GPL](results_exp/results_eval_base_neg20_gpl_MiniLM_vs_minilm.json)) | 0.358 | 0.910 | all-MiniLM-L6-v2 | **-0.144 [-0.163, -0.125]** | < 0.001 |
| gpl_bm25_BGE (eval_base_neg20) vs bge ([10_GPL](results_exp/results_eval_base_neg20_gpl_bm25_BGE_vs_bge.json)) | 0.372 | 0.919 | bge-small-en-v1.5 | **-0.234 [-0.253, -0.214]** | < 0.001 |
| gpl_bm25_GPL_distilbert (eval_base_neg20) vs bge ([10_GPL](results_exp/results_eval_base_neg20_gpl_bm25_GPL_distilbert_vs_bge.json)) | 0.365 | 0.922 | bge-small-en-v1.5 | **-0.241 [-0.261, -0.220]** | < 0.001 |
| gpl_bm25_MiniLM (eval_base_neg20) vs minilm ([10_GPL](results_exp/results_eval_base_neg20_gpl_bm25_MiniLM_vs_minilm.json)) | 0.398 | 0.946 | all-MiniLM-L6-v2 | **-0.104 [-0.122, -0.087]** | < 0.001 |
| genq_BGE (eval_base_neg30) vs bge ([10_GPL](results_exp/results_eval_base_neg30_genq_BGE_vs_bge.json)) | 0.508 | 0.981 | bge-small-en-v1.5 | **-0.098 [-0.112, -0.084]** | < 0.001 |
| genq_GPL_distilbert (eval_base_neg30) vs bge ([10_GPL](results_exp/results_eval_base_neg30_genq_GPL_distilbert_vs_bge.json)) | 0.480 | 0.974 | bge-small-en-v1.5 | **-0.126 [-0.142, -0.109]** | < 0.001 |
| genq_MiniLM (eval_base_neg30) vs minilm ([10_GPL](results_exp/results_eval_base_neg30_genq_MiniLM_vs_minilm.json)) | 0.524 | 0.982 | all-MiniLM-L6-v2 | **+0.022 [+0.010, +0.033]** | < 0.001 |
| gpl_BGE (eval_base_neg30) vs bge ([10_GPL](results_exp/results_eval_base_neg30_gpl_BGE_vs_bge.json)) | 0.363 | 0.895 | bge-small-en-v1.5 | **-0.243 [-0.263, -0.222]** | < 0.001 |
| gpl_GPL_distilbert (eval_base_neg30) vs bge ([10_GPL](results_exp/results_eval_base_neg30_gpl_GPL_distilbert_vs_bge.json)) | 0.332 | 0.880 | bge-small-en-v1.5 | **-0.274 [-0.295, -0.253]** | < 0.001 |
| gpl_MiniLM (eval_base_neg30) vs minilm ([10_GPL](results_exp/results_eval_base_neg30_gpl_MiniLM_vs_minilm.json)) | 0.360 | 0.913 | all-MiniLM-L6-v2 | **-0.142 [-0.161, -0.123]** | < 0.001 |
| gpl_bm25_BGE (eval_base_neg30) vs bge ([10_GPL](results_exp/results_eval_base_neg30_gpl_bm25_BGE_vs_bge.json)) | 0.386 | 0.921 | bge-small-en-v1.5 | **-0.221 [-0.240, -0.200]** | < 0.001 |
| gpl_bm25_GPL_distilbert (eval_base_neg30) vs bge ([10_GPL](results_exp/results_eval_base_neg30_gpl_bm25_GPL_distilbert_vs_bge.json)) | 0.373 | 0.918 | bge-small-en-v1.5 | **-0.233 [-0.253, -0.213]** | < 0.001 |
| gpl_bm25_MiniLM (eval_base_neg30) vs minilm ([10_GPL](results_exp/results_eval_base_neg30_gpl_bm25_MiniLM_vs_minilm.json)) | 0.399 | 0.950 | all-MiniLM-L6-v2 | **-0.104 [-0.122, -0.086]** | < 0.001 |
| genq_BGE (eval_base_neg40) vs bge ([10_GPL](results_exp/results_eval_base_neg40_genq_BGE_vs_bge.json)) | 0.524 | 0.983 | bge-small-en-v1.5 | **-0.083 [-0.096, -0.069]** | < 0.001 |
| genq_GPL_distilbert (eval_base_neg40) vs bge ([10_GPL](results_exp/results_eval_base_neg40_genq_GPL_distilbert_vs_bge.json)) | 0.470 | 0.973 | bge-small-en-v1.5 | **-0.136 [-0.153, -0.120]** | < 0.001 |
| genq_MiniLM (eval_base_neg40) vs minilm ([10_GPL](results_exp/results_eval_base_neg40_genq_MiniLM_vs_minilm.json)) | 0.514 | 0.980 | all-MiniLM-L6-v2 | **+0.011 [+0.000, +0.022]** | 0.043 |
| gpl_BGE (eval_base_neg40) vs bge ([10_GPL](results_exp/results_eval_base_neg40_gpl_BGE_vs_bge.json)) | 0.360 | 0.904 | bge-small-en-v1.5 | **-0.246 [-0.267, -0.226]** | < 0.001 |
| gpl_GPL_distilbert (eval_base_neg40) vs bge ([10_GPL](results_exp/results_eval_base_neg40_gpl_GPL_distilbert_vs_bge.json)) | 0.338 | 0.893 | bge-small-en-v1.5 | **-0.269 [-0.289, -0.247]** | < 0.001 |
| gpl_MiniLM (eval_base_neg40) vs minilm ([10_GPL](results_exp/results_eval_base_neg40_gpl_MiniLM_vs_minilm.json)) | 0.367 | 0.920 | all-MiniLM-L6-v2 | **-0.136 [-0.154, -0.118]** | < 0.001 |
| gpl_bm25_BGE (eval_base_neg40) vs bge ([10_GPL](results_exp/results_eval_base_neg40_gpl_bm25_BGE_vs_bge.json)) | 0.356 | 0.897 | bge-small-en-v1.5 | **-0.250 [-0.269, -0.230]** | < 0.001 |
| gpl_bm25_GPL_distilbert (eval_base_neg40) vs bge ([10_GPL](results_exp/results_eval_base_neg40_gpl_bm25_GPL_distilbert_vs_bge.json)) | 0.354 | 0.907 | bge-small-en-v1.5 | **-0.252 [-0.272, -0.231]** | < 0.001 |
| gpl_bm25_MiniLM (eval_base_neg40) vs minilm ([10_GPL](results_exp/results_eval_base_neg40_gpl_bm25_MiniLM_vs_minilm.json)) | 0.379 | 0.946 | all-MiniLM-L6-v2 | **-0.124 [-0.142, -0.106]** | < 0.001 |
| genq_BGE (eval_base_stepx4) vs bge ([10_GPL](results_exp/results_eval_base_stepx4_genq_BGE_vs_bge.json)) | 0.533 | 0.982 | bge-small-en-v1.5 | **-0.073 [-0.087, -0.059]** | < 0.001 |
| genq_GPL_distilbert (eval_base_stepx4) vs bge ([10_GPL](results_exp/results_eval_base_stepx4_genq_GPL_distilbert_vs_bge.json)) | 0.515 | 0.980 | bge-small-en-v1.5 | **-0.091 [-0.107, -0.075]** | < 0.001 |
| genq_MiniLM (eval_base_stepx4) vs minilm ([10_GPL](results_exp/results_eval_base_stepx4_genq_MiniLM_vs_minilm.json)) | 0.522 | 0.980 | all-MiniLM-L6-v2 | **+0.020 [+0.007, +0.032]** | 0.002 |
| gpl_BGE (eval_base_stepx4) vs bge ([10_GPL](results_exp/results_eval_base_stepx4_gpl_BGE_vs_bge.json)) | 0.341 | 0.883 | bge-small-en-v1.5 | **-0.265 [-0.285, -0.244]** | < 0.001 |
| gpl_GPL_distilbert (eval_base_stepx4) vs bge ([10_GPL](results_exp/results_eval_base_stepx4_gpl_GPL_distilbert_vs_bge.json)) | 0.326 | 0.861 | bge-small-en-v1.5 | **-0.281 [-0.301, -0.260]** | < 0.001 |
| gpl_MiniLM (eval_base_stepx4) vs minilm ([10_GPL](results_exp/results_eval_base_stepx4_gpl_MiniLM_vs_minilm.json)) | 0.357 | 0.907 | all-MiniLM-L6-v2 | **-0.145 [-0.165, -0.126]** | < 0.001 |
| gpl_bm25_BGE (eval_base_stepx4) vs bge ([10_GPL](results_exp/results_eval_base_stepx4_gpl_bm25_BGE_vs_bge.json)) | 0.343 | 0.875 | bge-small-en-v1.5 | **-0.263 [-0.284, -0.241]** | < 0.001 |
| gpl_bm25_GPL_distilbert (eval_base_stepx4) vs bge ([10_GPL](results_exp/results_eval_base_stepx4_gpl_bm25_GPL_distilbert_vs_bge.json)) | 0.344 | 0.888 | bge-small-en-v1.5 | **-0.262 [-0.283, -0.241]** | < 0.001 |
| gpl_bm25_MiniLM (eval_base_stepx4) vs minilm ([10_GPL](results_exp/results_eval_base_stepx4_gpl_bm25_MiniLM_vs_minilm.json)) | 0.359 | 0.920 | all-MiniLM-L6-v2 | **-0.144 [-0.165, -0.124]** | < 0.001 |
