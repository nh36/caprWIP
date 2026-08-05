# Queued review-gated tasks (do not execute without review)

Recorded, not executed. These follow from the behaviour-neutral relabelling phase
and the SC004 research task.

## Q1. SC064 — morphology-first audit (next substantive task)

Do **not** rename or restage `SC064 NWGmcInStemNLoss`, and do not begin this audit,
until it is reviewed and scheduled. No stage rename for SC064 is permitted until
this morphology-first audit is complete.

The audit must **begin by testing whether `NWGmcInStemNLoss` represents a sound
change at all**, and must:

1. inventory every corpus application of SC064;
2. reconstruct the complete `īn`-stem paradigm;
3. verify the selected `*fúrxtīnaz` input;
4. compare nominative, accusative, genitive and dative derivations;
5. inspect all other Old English `īn`-stem nouns in the corpus;
6. separate phonological loss from morphological levelling;
7. test removal of SC064;
8. test corrected proto inputs;
9. test a morphology-layer implementation;
10. determine whether SC064 belongs in the sound-change cascade at all.

Only after that audit may a stage decision (and any rename) be considered.

## Q2. SC004 — implementation of the recommended split (Outcome C)

The SC004 research task (this cluster) recommends **Outcome C**: split the bundled
`PWGmcAiMonophthongization` into a later general `*ai/*ái > *ā` (retains SC004,
all witnesses) and an earlier corpus-inert word-final `*-ai > *-ē` (provisional
id). See `sc004_historical_options_report.md`. **Not applied.** Before any
implementation (a separate review-gated task):

1. consult **Versloot 2017** directly and add it to `docs/refs.bib`; confirm the
   PNWGmc dating of the final component and the wave chronology of the general
   component;
2. treat `EAF` for the general component as an operational modelling corridor, not
   a Proto-Anglo-Frisian node claim;
3. record the final component's 0-corpus-load explicitly.

## Q3. `stem` — actionable-phonology / `known_unmodelled` reconciliation

`post_rename_integrity_report.md` §3 diagnoses (and does **not** fix) that a
freshly generated `oe_mismatch_report.txt` reports one actionable core-phonology
mismatch — `stem` `*stámnaz -> stamn` (expected `stefn`) — because
`oe_mismatch_report.py` does not honor the aligned data's
`DERIVATION_CLASS = known_unmodelled`. The previously-cited "0 actionable
phonology" state rested on a stale committed report. Pre-existing (gate B:
outputs_sha256 unchanged since `a5e9ce12`). A separate review must choose among:

1. teach `oe_mismatch_report.py` to exclude `DERIVATION_CLASS = known_unmodelled`
   rows (make the report honor the existing data classification);
2. add `stem` to `oe_known_problems.tsv`;
3. implement the `mn > fn` development so `stem` matches.

No FST, aligned-data, `oe_known_problems.tsv`, or tool change has been made for
this item.
