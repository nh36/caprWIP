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

## Q2. SC004 — split task record (closed)

Historical queue entry retained for traceability. The earlier proposal in
`sc004_historical_options_report.md` has now been implemented and closed at
checkpoint `d704a94c`, with publication-prose reconciliation completed on the
current `dublin-resume` line.

Final recorded state:

1. split applied: former bundled `PWGmcAiMonophthongization` was reconciled into
   SC014 and SC004 behaviorally distinct components;
2. **SC014** = unstressed `*ai > *ē`, final and nonfinal, with corpus witnesses
   `span` (`*spánnai`) and `meed` (`*mízdai`);
3. SC014 later chronology boundary = **SC072**;
4. **SC004** = stressed/root `*ái > *ā`;
5. SC004 production application count = **24** rows.

## Q3. `stem` — legacy decision tree superseded (pending targeted follow-up)

The old three-way queue choice is superseded and should not be used as the active
decision framework. Do not execute the prior options:

1. exclude `known_unmodelled` rows in `oe_mismatch_report.py`;
2. add `stem` to `oe_known_problems.tsv`;
3. implement a general `mn > fn` sound change.

Use the targeted row-2216 adjudication plan instead:

1. retain lexeme-level `PROTO = *stámnaz`;
2. test/select English-line `PROTOFORM = *stámniz`;
3. test attested OE `stemn` as deterministic comparator;
4. if trace and sources justify it, reclassify `known_unmodelled -> early_analogy`;
5. do **not** add a general `mn > fn` rule;
6. do **not** broaden `PNWGmcMnDissimilation`;
7. keep unrelated `*stébnō` ('voice/sound') excluded.

Durable planning anchors for this follow-up already exist in
`Germanic/docs/lexeme_reports/model_entries/2216-stem-stefn.model.md` and
`Germanic/docs/sound_changes/cascade_baseline/post_rename_integrity_report.md`.
No FST, aligned-data, `oe_known_problems.tsv`, or tool change is made in this
queue update.
