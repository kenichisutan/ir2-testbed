# GPL: Generative Pseudo Labeling for Unsupervised Domain Adaptation of Dense Retrieval (Wang et al., NAACL 2022)

Pair 10: Francesc, Marina. Method: a T5 model writes queries for the target corpus, dense retrievers (or BM25) mine hard negatives, a cross-encoder scores the margins, and the student is trained to match them with MarginMSE (GenQ: same queries, no teacher). How to run, in at most 10 lines:


```
pip install -r pairs/10-GPL/requirements_gpl.txt     # training environment (GPL toolkit). In Python 3.10
cd pairs/10-GPL && python gpl_lab.py && cd ../..      # generate data and train every variant into runs/
pip install -r pairs/10-GPL/requirements_ir.txt      # evaluation environment (testbed)
python pairs/10-GPL/method.py                         # test-set runs in pairs/10-GPL/runs/Eval/
python testbed.py score pairs/10-GPL/runs/Eval/eval_base/gpl_BGE --method "gpl_BGE (eval_base) vs bge" --pair 10-GPL --against bge
python pairs/10-GPL/student.py                        # why the labels are rescaled -> students_table.md
```

Notebooks (one Colab GPU): `reproduce.ipynb` (our from-scratch pipeline and the key-result reproduction), `demo.ipynb` (live demo, see `demo.md`), `paired_tests.ipynb` (per-query tests).
