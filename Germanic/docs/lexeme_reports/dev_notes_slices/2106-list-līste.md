---
row_id: 2106
concept: list
counterpart: līste
proto: "*lī́stōn"
protoform: "*lḯstōn"
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file: ""
linked_research_memo_file: ""
linked_dossier_or_analysis_files:
  - Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2106 list / līste

## Current row state

- Live OE row `2106` is currently a regular exact-match row with `COUNTERPART = līste`, `PROTOFORM = *lḯstōn`, `DERIVATION_CLASS = regular`, and concept-level `PROTO = *lī́stōn`; the neighboring Dutch, English, and German rows still keep plain `*līstōn`, so the OE row's `ḯ` is a row-local OE-cascade encoding choice rather than a different cognate-set reconstruction [Germanic/data/germanic-aligned-final.tsv:680-683].
- The row therefore needs the three-way distinction kept explicit throughout later reporting: `PROTO = *lī́stōn` is the comparative/shared headword notation, `PROTOFORM = *lḯstōn` is the live OE-facing derivational input, and `COUNTERPART = līste` is the attested/target OE surface form [Germanic/data/germanic-aligned-final.tsv:682-682].
- `old_english_wiktionary.tsv` independently gives `list -> līste`, so the target lemma itself is not a substitute paradigm cell or emergency replacement [Germanic/data/old_english_wiktionary.tsv:168-168].
- The current published derivation trace is exact and short: `PROTO: *lḯstōn`, `EXPECTED: līste`, `OUTPUTS: līste`, with stage sequence `NWGmc N Stem N Loss: *lḯstǭ`, `OE Unstressed Long Vowel Shortening: *lḯstæ`, `OE Unstressed AE Merger: *lḯste`, then surface `Outcome: līste` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2924-2942].
- Required support-file checks are negative for any pre-existing row dossier. `coverage_audit.md` lists `2106 | list | līste | regular | no | - | - | - | none`; `oe_known_problems.tsv` contains no row-local exception entry for this lexeme; and `report_manifest.tsv` still contains only the pilot-report rows, not row `2106` [Germanic/docs/lexeme_reports/coverage_audit.md:296-296; Germanic/data/oe_known_problems.tsv:1-8; Germanic/docs/lexeme_reports/report_manifest.tsv:1-14].

## Development-note summary

No row-specific DEV_NOTES block for `list / līste` survives apart from the stressed-long-`ī` migration inventory. That has to be said plainly. The usable `DEV_NOTES.md` material is therefore thin and mostly **shared-background-only**: it explains why the OE row now uses machine-safe `*ḯ` notation, records that row `2106` was one of the migrated stressed-root `*ī` rows, and shows that the migration cohort was regression-checked afterward [Germanic/docs/DEV_NOTES.md:41893-42051].

For this row, the main interpretive burden is notation rather than lexical controversy. DEV_NOTES states: “The diaeresis is purely notational. Semantically `*ḯ` = stressed long *ī” [Germanic/docs/DEV_NOTES.md:41938-41939]. That sentence controls the row. It means `*lī́stōn` and `*lḯstōn` are not rival proto-stages for the noun; they are two notation layers for the same inherited item, with `*lḯstōn` adopted only because the OE transducer needed a single-codepoint way to distinguish stressed root long `ī` from unstressed suffixal `*ī` elsewhere in the system [Germanic/docs/DEV_NOTES.md:41925-41939].

The current row behavior matches that explanation exactly. The published trace takes `*lḯstōn` as input and derives ordinary `līste` with no exception label, no target replacement, and no sign of analogical rescue [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2924-2942]. The only direct row-explicit DEV_NOTES attachment is the Batch 2 migration line `2103, 2105, 2106 | līm, līne, līste`, which is real evidence of deliberate migration history but not a lexeme-specific etymological note [Germanic/docs/DEV_NOTES.md:42020-42023].

So the safest replacement note is conservative. Support for row `2106` is currently: (a) **shared-background-only** stressed-long-`ī` notation policy; (b) one **row-specific** batch-entry showing that `līste` was migrated intentionally; and (c) **diagnostic** cohort verification plus the live exact-match trace. No surviving DEV_NOTES material argues that `līste` is irregular, problematic, or dependent on a substitute form.

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-41923-41957

- Source heading: `§17.46 Stressed long-ī tier (*ḯ) — B. Notation / C. Pipeline plumbing`
- Source line hint: `Germanic/docs/DEV_NOTES.md:41923-41957`
- Fragment type: `phenomenon_context_for_lexeme`
- Status: `shared-background-only`
- Issue tags: `stressed_long_i`; `notation_policy`; `proto_vs_protoform`; `surface_mapping`
- Recommended next use: `cite if explaining why row 2106 has *lḯstōn in OE-facing input but *lī́stōn as shared proto notation`
- Shared-with rows if relevant: `1998`; `2047`; `2101`; `2103`; `2105`; `2106`; `2153`; `2182`; `2188`; `2197`; `2257`; `2285`; `2286`; `2290`; `2296`

This is the controlling surviving fragment even though it is not a `līste` dossier. DEV_NOTES records the input-tokenization problem in direct sequence: combining-acute `ī́` “compiles, prints correctly via `print upper-words`, but `apply down ī́ → ???`,” while single-codepoint `ḯ` “works, single codepoint. **Adopted.**” [Germanic/docs/DEV_NOTES.md:41925-41936]. It then gives the sentence that should be preserved verbatim for this row: “The diaeresis is purely notational. Semantically `*ḯ` = stressed long *ī” [Germanic/docs/DEV_NOTES.md:41938-41939].

For row `2106`, the rest of the fragment matters just as much. DEV_NOTES says `OldEnglishRemoveStars` maps `{*ḯ} -> ī`, and immediately explains why: “OE orthography does **not** distinguish stressed-root from unstressed-suffix long ī. The tier exists only to gate one rule (`NWGmcInStemNLoss`); from the moment that rule fires (or doesn't), the two collapse for orthography” [Germanic/docs/DEV_NOTES.md:41952-41957]. That is the exact bridge needed here between shared `PROTO = *lī́stōn`, live OE-facing `PROTOFORM = *lḯstōn`, and surface `COUNTERPART = līste`. Support for row `2106` in this fragment is therefore real but explicitly **shared-background-only**, not row-local philological argument.

### DEV_NOTES:line-42006-42026

- Source heading: `§17.46 Stressed long-ī tier (*ḯ) — E. TSV migration (Phase 4)`
- Source line hint: `Germanic/docs/DEV_NOTES.md:42006-42026`
- Fragment type: `lexeme_specific`
- Status: `row-specific`
- Issue tags: `tsv_migration`; `row_explicit`; `stressed_long_i`; `implementation_history`
- Recommended next use: `cite if documenting the row's surviving direct DEV_NOTES anchor`
- Shared-with rows if relevant: `2103`; `2105`

This is the one securely attachable fragment that names row `2106` directly. DEV_NOTES inventories the stressed-root `*ī` rows and then lists Batch 2 as `2103, 2105, 2106 | līm, līne, līste` [Germanic/docs/DEV_NOTES.md:42010-42023]. The force of that line is narrow but important: `līste` was not left on `*lḯstōn` accidentally or by silent drift; it was part of the deliberate OE-row migration from older plain/combining-acute `*ī` notation into the stressed-`*ḯ` cohort.

The fragment should still be used cautiously. It is **row-specific** in the limited sense that it names `2106`, but the substance is engineering history, not lexical controversy. Unlike rows that carry parenthetical warnings in the same migration table, `līste` appears without any note about umlaut side-effects, analogical repair, or mismatch persistence [Germanic/docs/DEV_NOTES.md:42023-42025]. The silence is meaningful: current DEV_NOTES does not preserve any claim that `list / līste` was a problem row beyond needing the shared stressed-long-`ī` encoding repair.

### DEV_NOTES:line-42031-42051

- Source heading: `§17.46 Stressed long-ī tier (*ḯ) — F. Verification`
- Source line hint: `Germanic/docs/DEV_NOTES.md:42031-42051`
- Fragment type: `diagnostic_project_history_for_lexeme`
- Status: `diagnostic`
- Issue tags: `verification`; `migration_regression_check`; `cohort_history`; `not_row_specific`
- Recommended next use: `use only as supporting cohort history, then pair with the live row trace`
- Shared-with rows if relevant: `all migrated *ḯ rows`

This verification block does not probe `līste` by name. Its direct examples are `swīną`, `swḯną`, `fúrxtīn`, `skḯnaną`, and `tḯdiz` [Germanic/docs/DEV_NOTES.md:42035-42040]. For row `2106`, support here is therefore only **diagnostic** and cohort-level: it shows that the stressed-`*ḯ` migration was probed immediately afterward and that the mismatch total held at `13` through phase-4 batches `1–5` [Germanic/docs/DEV_NOTES.md:42043-42051].

That matters, but only modestly. It supports the claim that row `2106` entered a verified migration cohort rather than an untested one. The actual row-local confirmation still comes from the live published derivation trace `PROTO: *lḯstōn / OUTPUTS: līste` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2924-2942]. This fragment should therefore remain explicitly diagnostic, not the main authority for the row.

## Superseded or diagnostic material

- Older/shared spelling `*lī́stōn` must remain visible in this slice because it is still the row's `PROTO` value and the cognate-set-wide notation across neighboring non-OE rows [Germanic/data/germanic-aligned-final.tsv:680-683]. But DEV_NOTES is explicit that the move to `*lḯstōn` was an input-tokenization repair, not a new etymology or a change in intended OE output [Germanic/docs/DEV_NOTES.md:41925-41939]. For this row, `*lī́stōn` is therefore best treated as a preserved comparative/shared notation layer, not as superseding evidence against the live OE-facing input.
- No surviving DEV_NOTES fragment gives a row-local lexical discussion of `list / līste` beyond the migration table. That absence should be preserved as part of the evidence state. The slice is conservative because the surviving support is thin, not because the row is unstable [Germanic/docs/DEV_NOTES.md:42020-42023; Germanic/docs/lexeme_reports/coverage_audit.md:296-296].
- The verification block is diagnostic only. Preserve it as proof that the migration cohort was checked, but do not cite it as if `līste` itself were one of the explicit probe forms [Germanic/docs/DEV_NOTES.md:42031-42051].

## Open questions for later work

- If a fuller lexeme report is later written, add direct external support for the noun's stem-class/morphological interpretation, since the current trace uses `NWGmc N Stem N Loss: *lḯstǭ` but DEV_NOTES does not preserve a row-specific literature discussion of that point [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2930-2936].
- If later report prose needs to discuss the row's proto labels, keep the present distinction explicit: `PROTO = *lī́stōn` is the shared comparative notation, `PROTOFORM = *lḯstōn` is the live OE-facing encoding, and neither should be collapsed into the attested OE target `līste` without explanation [Germanic/data/germanic-aligned-final.tsv:682-682; Germanic/docs/DEV_NOTES.md:41938-41957].
- If `dev_notes_slices/index.tsv` is revisited later, row `2106` still looks like a likely no-index slice. Its only strong row-explicit DEV_NOTES anchor is the Batch 2 migration line, and that line documents implementation history rather than a substantive lexeme-specific argument [Germanic/docs/DEV_NOTES.md:42020-42023].
