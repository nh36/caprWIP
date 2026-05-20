# Sound-change architecture scaffold 01 report

## Summary

- Directories created:
  - `Germanic/docs/sound_changes/`
  - `Germanic/docs/sound_changes/change_entries/`
  - `Germanic/docs/sound_changes/literature_dossiers/`
  - `Germanic/docs/sound_changes/order_tests/`
  - `Germanic/docs/sound_changes/order_tests/runs/`
  - `Germanic/docs/sound_changes/order_tests/summaries/`
- `Germanic/docs/assembly/source_page_maps/` already existed and was reused.
- Files created:
  - `Germanic/docs/sound_changes/README.md`
  - `Germanic/docs/sound_changes/sound_change_inventory.tsv`
  - `Germanic/docs/sound_changes/sound_change_aliases.tsv`
  - `Germanic/docs/sound_changes/sound_change_literature_matrix.tsv`
  - `Germanic/docs/sound_changes/sound_change_order_sensitivity.tsv`
  - `Germanic/docs/sound_changes/change_entries/043-anglo-frisian-brightening.change.md`
  - `Germanic/docs/sound_changes/change_entries/063-oe-high-vowel-apocope.change.md`
  - `Germanic/docs/sound_changes/sound_change_architecture_scaffold_01_report.md`
- Rule-source files found: `Germanic/fsts/germanic.txt` and `Germanic/fsts/old_english_sandbox.txt`.
- Number of rules found in rule source: **95** current ordered sandbox stages.
- Number of unique trace labels found: **78** in `Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.compact.md`.
- Matched / unmatched rules: **78 matched trace labels**, **0 unmatched trace labels**, **17 source-only stages not currently surfacing as compact trace labels**.
- Outputs or lexical volume files touched: **no**.

## Existing lexical architecture reused

The scaffold mirrors the existing lexical-volume architecture rather than replacing it. The lexical volume uses the aligned manifest (`Germanic/docs/assembly/manifest_all_by_class.tsv`), the compact trace report (`Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.compact.md`), entry prose (`Germanic/docs/lexeme_reports/model_entries/*.model.md` and `Germanic/docs/assembly/book_prose/regular_all_01/*.book.md`), the assembler (`Germanic/docs/assembly/build_full_lexical_volume.py`), and the shared bibliography (`docs/refs.bib`).

The sound-change side reuses the same trace report and bibliography, but swaps the lexical manifest/entry focus for a rule inventory keyed to the FOMA source and sandbox order. The new TSVs are the rule-centered equivalents of the lexical manifest, while `change_entries/*.change.md` are the eventual rule-entry counterparts to the lexical entry files.

## Rule-source discovery

Relevant rule/build/run files found:

- `Germanic/fsts/germanic.txt` — authoritative FOMA source for the Old English stack and supporting rule definitions.
- `Germanic/fsts/old_english_sandbox.txt` — one-snapshot-per-stage sandbox that mirrors the live cascade and saves `old_english_sandbox_after_*.bin` checkpoints.
- `Germanic/tools/rebuild_oe_bins.sh` — Docker/Foma rebuild script for `germanic.txt` and `old_english_sandbox.txt`.
- `Germanic/tools/oe_full_trace_report.py` — stage list and corpus-wide trace runner over the sandbox bins.
- `Germanic/tools/oe_derivation_class_trace_report.py` — grouped trace report writer used upstream of the compact trace report.
- `Germanic/tools/compact_trace_report.py` — post-processor that humanizes stage labels and rewrites the grouped trace report into the compact Markdown form.
- `Germanic/tools/trace_old_english_sandbox.py` — single-lexeme sandbox tracer.
- `Germanic/tools/oe_mismatch_report.py` — corpus-wide output-checking and mismatch bucketing runner.
- `Germanic/tests/test_english_apply_down_stats.py` — existing apply-down stats test illustrating the current test style around transducer runners.

Rule order is explicit in two places:

1. `Germanic/fsts/germanic.txt` defines the real composed chain (`OldEnglishCore`, `OldEnglishRules`, `OldEnglishReflexes`), but some historical phases are bundled.
2. `Germanic/fsts/old_english_sandbox.txt` linearizes that chain into one saved stage per rule application, including duplicated applications such as early/late `OEPrefixAReduction`.

For scaffold work, the sandbox file is the cleanest authoritative statement of **current order**, because it already exposes the exact checkpoint sequence used by the trace machinery.

Rule display names are represented in three layers:

- FOMA/internal names in `germanic.txt`, e.g. `OEHighVowelApocope`.
- Sandbox stage names in `old_english_sandbox.txt`, often the same but sometimes stage-specific aliases (for example early/late prefix reduction).
- Reader-facing trace labels in the compact trace report, produced by `compact_trace_report.py` via camel-case splitting (`OEHighVowelApocope` → `OE High Vowel Apocope`).

So the FOMA names do **not** match the trace labels exactly as strings, but they do match deterministically after alias normalization. The main exceptions are support stages such as `ProtoInput`, plus `OldEnglishRemoveStars`, which the compact trace post-processor rewrites to `Outcome:` rather than leaving it as a visible stage label.

## Initial sound-change inventory

The first-pass `sound_change_inventory.tsv` contains all **95** current sandbox stages in order, with:

- current order from `old_english_sandbox.txt`;
- rule anchors and raw FOMA definitions from `germanic.txt`;
- compact-trace occurrence counts and example lexemes from `oe_derivation_class_trace_report.compact.md`;
- initial placeholders for literature and order-sensitivity status.

Stages represented in the inventory:

1. Proto-Germanic consonant inheritance
2. Proto-West Germanic developments
3. Northwest Germanic developments
4. Old English
5. Orthography & surface

Most common rules in the current compact trace sample:

- `OE Heavy Syllable Nasal Apocope` — 158 occurrences
- `PGmc Final Z Deletion` — 113
- `Anglo Frisian Brightening` — 89
- `OE Secondary Nasalization` — 87
- `OE Weak Tail Reduction` — 87
- `OE High Vowel Apocope` — 65

Rules/stages present in source but not currently seen as compact trace labels: **17**. These include genuine low-frequency or currently non-triggered rules, plus support/checkpoint stages such as `Proto Input`. Examples include `PWGmc Syllabic J`, `NWGmc Unstressed Ai Monophthongization`, `OE J Cluster Coalescence`, `OE Nasal Dissimilation`, `OE Weight Markers`, `OE Medial Syncope`, and `OE Dental Assimilation`.

Trace labels not matched to rule-source definitions: **0** in this first pass.

## Literature dossier architecture

The dossier architecture is split between a row-level matrix and longer per-rule notes:

- `sound_change_literature_matrix.tsv` is the structured working table. Each row should capture one source claim, locator, quotation or paraphrase, conditioning statement, chronology claim, terminology, and disagreement note.
- `literature_dossiers/*.dossier.md` should hold the longer synthesis for each rule: chronological source ordering, competing terminologies, open disputes, and any source-page-map notes that are too bulky for the TSV.

The TSV should remain the canonical evidence ledger used for later assembly. The markdown dossiers should be interpretive working notes built from that ledger. Existing `docs/references/` PDFs/OCR and `Germanic/docs/assembly/source_page_maps/` can be reused later for locator work; this scaffold pass does not add new reference assets.

## Order-sensitivity architecture

The eventual order-sensitivity runner needs to work against the real transducer, not a hand-maintained checklist. The existing machinery already gives most of the necessary pieces:

- compile current bins with `Germanic/tools/rebuild_oe_bins.sh`;
- read the OE lexical corpus from the same aligned TSV used by the lexical stack;
- run the corpus through `old_english.bin` and/or the sandbox bins;
- compare outputs against the expected Old English counterparts;
- summarize failures with logic similar to `oe_mismatch_report.py`.

What is still needed is a dedicated runner that can perturb rule order safely. The cleanest approach is:

1. parse the current ordered stage list from `old_english_sandbox.txt`;
2. build temporary reordered copies of the sandbox/main cascade for one target stage at a time;
3. compile those temporary variants inside Docker/Foma;
4. run the relevant lexical corpus through the reordered build;
5. compare against the current-good outputs and expected OE targets;
6. record which lexemes fail one step earlier / one step later / farther outside the safe window;
7. write raw run artifacts under `order_tests/runs/` and summarized TSVs/markdown under `order_tests/summaries/`.

`sound_change_order_sensitivity.tsv` is the top-level summary table for those results: earliest safe position, latest safe position, counts of failures, representative lexemes, and current pass/fail totals.

## Proposed eventual volume structure

1. Introduction to the sound-change volume
2. Method: FOMA stack, sandbox checkpoints, and lexical verification
3. Earlier Germanic changes
4. Old English changes
5. Rule-order diagnostics and sensitivity windows
6. Bibliography

Each change entry can then pull from the same scaffold fields: rule definition, plain-English description, dossier synthesis, conditioning, current stack position, and order-sensitivity diagnostics.

## Next recommended task

**C. Complete the sound-change inventory and alias mapping.**

That should come first so the later dossier and runner work target a stable rule list. After that, **A** (order-sensitivity runner skeleton) and **B** (first literature dossier pilot) can proceed in parallel.
