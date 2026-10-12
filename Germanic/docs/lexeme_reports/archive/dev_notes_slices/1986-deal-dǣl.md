---
row_id: 1986
concept: deal
counterpart: dǣl
proto: *dáiliz
protoform: *dáiliz
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files: []
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 1986 deal / dǣl

## Current row state

- CONCEPT: `deal`
- COUNTERPART: `dǣl`
- PROTO: `*dáiliz`
- PROTOFORM: `*dáiliz`
- DERIVATION_CLASS: `regular` [Germanic/data/germanic-aligned-final.tsv:215-215]
- Repo-local OE lexeme table independently keeps the same pairing `deal` → `dǣl`, so the live row is not standing alone as an uncrosschecked target selection [Germanic/data/old_english_wiktionary.tsv:52-52].
- Existing row infrastructure is still minimal. `coverage_audit.md` records row 1986 as `regular`, with no packet, no research memo, no attached dossier/analysis file, and `none` under current lexeme-report coverage [Germanic/docs/lexeme_reports/coverage_audit.md:221-221].
- The current derivation snapshot already reaches the live target without workaround: `*dáiliz` passes through `PWGmc Ai Monophthongization: *dāliz`, then `PGmc Final Z Deletion: *dāli`, then OE `I Umlaut: *dǣli`, then `High Vowel Apocope: *dǣl`, with published outcome `dǣl` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:834-853].

## Development-note summary

DEV_NOTES support for row 1986 is real but thin, and the thinness should be stated explicitly. No dedicated `deal / dǣl` dossier or long row-local argument survives in `Germanic/docs/DEV_NOTES.md`; the materially relevant evidence consists of two short implementation notes that mention `*dailiz → dǣl` directly [Germanic/docs/DEV_NOTES.md:2608-2612,14036-14043]. That means this replacement note should preserve project history conservatively rather than pretending there was a larger lexical controversy.

The earlier of the two passages is an OE surface/orthography repair note. It says the project added `{*ǣ} -> ǣ` to `OldEnglishRemoveStars` “so OE surface accepts long fronted a (e.g., *dailiz → dǣl, *xaiθiz → hǣþ)” [Germanic/docs/DEV_NOTES.md:2608-2612]. The substance here is not that row 1986 needed a new etymology or a new target; it is that the phonological path to fronted long `ǣ` was already part of the intended derivation, but the surface-stripping layer needed an explicit starred-`ǣ` mapping so forms like `*dǣl` could reach printable OE output cleanly.

The later passage is a regression-style verification note from 2026-04-06. After another implementation change, DEV_NOTES records the test result `Stressed *ai forms still work: *bainą → bān, *dailiz → dǣl` [Germanic/docs/DEV_NOTES.md:14036-14043]. For row 1986, that is the clearest current-state DEV_NOTES claim: the shared stressed-`*ai` machinery still yields `dǣl`, so the row remains a regular success case rather than an unresolved mismatch bucket.

Taken together, these passages preserve a specific project chronology. First, the row's pathway depended on allowing OE surface `ǣ` to survive star removal; later, after unrelated subsequent changes, the project explicitly rechecked that the stressed-`*ai` path still delivered `dǣl`. What DEV_NOTES does **not** preserve is equally important: there is no surviving note that row 1986 is exceptional, analogical, semantically suspect, or trapped in `oe_known_problems.tsv`. In current repo state, `deal / dǣl / *dáiliz` is best described as a regular row with brief but positive DEV_NOTES confirmation, not as a no-evidence placeholder and not as a superseded exception narrative [Germanic/data/germanic-aligned-final.tsv:215-215; Germanic/docs/DEV_NOTES.md:2608-2612,14036-14043].

## Relevant DEV_NOTES fragments

### DEV_NOTES:no-row-local-dossier

- Source heading: no dedicated `deal / dǣl` section survives
- Source line or section hint: direct hits are confined to `lines 2608-2612` and `14036-14043`
- Fragment type: `negative_result_with_thin_positive_support`
- Status: `current`
- Issue tags: `thin_support`; `no_row_local_dossier`; `shared_rule_background`
- Recommended next use: `state_conservatively_in_final_report`
- Shared with row IDs:

A direct review of DEV_NOTES does **not** uncover a longer row-specific narrative for `deal / dǣl`. The usable support is confined to the OE `ǣ` surface-fix note and the later stressed-`*ai` regression check [Germanic/docs/DEV_NOTES.md:2608-2612,14036-14043]. That absence matters because later reporting should not inflate the documentation level for row 1986: the row has explicit positive mentions, but it does not have a bespoke DEV_NOTES dossier.

### DEV_NOTES:line-2608-2612

- Source heading: `OE ai cleanup + ǣ surface fix (2026-01-01)`
- Source line or section hint: `lines 2608-2612`
- Fragment type: `implementation_fix_with_row_example`
- Status: `current`
- Issue tags: `oe_surface`; `remove_stars`; `long_fronted_a`; `explicit_row_example`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This is the most concrete DEV_NOTES passage for the row because it names the lexeme directly. The note says: `Added {*ǣ} -> ǣ to OldEnglishRemoveStars so OE surface accepts long fronted a (e.g., *dailiz → dǣl, *xaiθiz → hǣþ)` [Germanic/docs/DEV_NOTES.md:2608-2610]. The point to preserve is narrow but important: row 1986 was not being reanalyzed lexically here; rather, the project was fixing an OE output-layer bottleneck so a derivation that already produced fronted long `ǣ` would surface correctly as `dǣl`.

### DEV_NOTES:line-14036-14043

- Source heading: `Test results` within the 2026-04-06 implementation note
- Source line or section hint: `lines 14036-14043`
- Fragment type: `verification`
- Status: `current`
- Issue tags: `stressed_ai`; `regression_check`; `regular_outcome`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This fragment is the cleanest late-project confirmation of current row policy. DEV_NOTES records: `Stressed *ai forms still work: *bainą → bān, *dailiz → dǣl` [Germanic/docs/DEV_NOTES.md:14036-14038]. For row 1986, that sentence preserves the fact that after subsequent code changes the project still regarded `*dailiz → dǣl` as a working regular derivation, not as a fragile special-case patch.

## Superseded or diagnostic material

- No superseded row-specific exception analysis was located for `deal / dǣl`. That absence is itself diagnostic: unlike rows that preserve an old mismatch-bucket story, row 1986 currently retains only positive implementation notes plus the published successful trace [Germanic/docs/DEV_NOTES.md:2608-2612,14036-14043; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:834-853].
- The published derivation trace is useful diagnostic support but is **not** a DEV_NOTES fragment. It should be cited as implementation evidence for the current pathway (`*dāliz > *dāli > *dǣli > *dǣl`), not mistaken for historical note prose [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:843-853].
- `coverage_audit.md` is likewise diagnostic rather than argumentative. Its `none` entry confirms that no packet, memo, or prior attached lexeme-report infrastructure presently exists for row 1986 [Germanic/docs/lexeme_reports/coverage_audit.md:221-221].

## Open questions for later work

- Decide whether two brief but explicit DEV_NOTES mentions are enough to make row 1986 worth indexing, or whether it should remain a no-index slice until a fuller packet/memo or literature-facing report exists.
- If a later packet or memo is prepared, add a compact literature check on the lexical equation `*dáiliz` ↔ OE `dǣl`; the present slice is adequate for DEV_NOTES replacement purposes, but its support is mostly implementation-facing rather than philological.
- If DEV_NOTES later grows a consolidated shared note on OE outcomes of stressed PGmc `*ai` plus subsequent fronting/umlaut behavior, row 1986 should attach to that shared discussion rather than being made to carry more row-local controversy than the current record supports.
