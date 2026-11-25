# Error analysis: French queries on the English SciFact corpus

From `results_crosslingual.json` (`worst`: the 5 queries that lose the most nDCG@10 per mode).

**Sparse loses most (−0.197 nDCG@10, Recall@100 0.894 → 0.758).** Its score only counts tokens that appear in both the query and the document, so a correct French query shares almost nothing with an English abstract. Its five worst queries all fall from 1.0 to 0. Four are translated correctly, for example *Taxation of sugar-sweetened beverages…* → *La taxation des boissons sucrées…*; the fifth, 532, turns *bypass* into *contournement*. What survives is names and acronyms (Fz/PCP, TNF-α), which are the same in both languages.

**Dense and multi-vec lose about 0.05.** Most of their worst queries are translated correctly and still drop:
- Dense: 837 (*NR5A2… endometrial tissues*), 743 (*Macrolides protect against myocardial infarction*) and 729 (*…SHP-2 MAPK pathway*) are correct translations
- Multi-vec: 644 (*Insulin increases risk of severe kidney failure*), 793 (*Mitochondria are uninvolved in apoptosis*), 598 and 501 are correct translations
- Two are translation problems: 1204, *quiescent* → *silencieux*, attached to the follicle (one of the 4 errors in `check_30.csv`, worst for both modes), and 513, *fitness* → *aptitude*, a literal translation (dense)

So for the dense and multi-vector heads the loss is mostly the model, not the translation: a correct French claim can still land far from its English abstract.

**Dense+Sparse and All** also lose 532 and 533, where *bypass* became *contournement* instead of *pontage*. Sparse alone loses 960, where *Polymeal* became *polymère*; the other modes keep it at 1.0.

**All stays level with multi-vec in French (0.634 each), so the fusion gain over multi-vec disappears.** Sparse adds noise once it stops matching words, while Recall@100 doesn't move (0.914 → 0.915).

**The 26 hand-checked queries lose much less (All −0.008, p = 0.68).** This doesn't show that the full loss comes from translation errors: these 26 were picked for having the most acronyms and numbers, which match in both languages. They are not a random sample.
