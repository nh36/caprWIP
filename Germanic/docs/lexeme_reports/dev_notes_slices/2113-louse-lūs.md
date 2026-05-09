---
row_id: 2113
concept: louse
counterpart: lūs
proto: *lūsz
protoform: *lūsz
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
  - Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md
  - Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.txt
  - Germanic/docs/lexeme_reports/coverage_audit.md
current_status: exact_match_no_row_specific_dev_notes_block
needs_literature_agent: no
---

# DEV_NOTES material — 2113 louse / lūs

## Current row state

- The live OE row is `2113`, with `CONCEPT = louse`, `COUNTERPART = lūs`, `PROTO = *lūsz`, `PROTOFORM = *lūsz`, and `DERIVATION_CLASS = regular`. The row carries source breadcrumbs from the Old English Swadesh list and Wiktionary inheritance/etymology templates, but no live note text and no alternative modelling `PROTOFORM`; for this row the comparative proto label and the live transducer input are currently identical [Germanic/data/germanic-aligned-final.tsv:707-709].
- `oe_known_problems.tsv` has no row-specific entry for `*lūsz`, `louse`, or `lūs`, so the row is not currently being tracked as a known OE exception, wontfix item, or active repair target [Germanic/data/oe_known_problems.tsv:1-8].
- Coverage infrastructure likewise treats the row as uncovered but unproblematic: `coverage_audit.md` lists `| 2113 | louse | lūs | regular | no | - | - | - | none |`, and `report_manifest.tsv` still contains only the pilot-report set, with no row-2113 manifest entry [Germanic/docs/lexeme_reports/coverage_audit.md:301-301; Germanic/docs/lexeme_reports/report_manifest.tsv:1-13].
- Minimal lexical support exists outside DEV_NOTES. `old_english_wiktionary.tsv` gives `louse	lūs	inh	template:inh	louse`, and `old_english_swadesh.tsv` gives `48	louse	lūs	/luːs/`; these are only breadcrumb-level attestational supports, but they do align with the live row target [Germanic/data/old_english_wiktionary.tsv:174-174; Germanic/data/old_english_swadesh.tsv:49-49].
- The current derivation is an exact match. The published derivation snapshot records `PROTO: *lūsz`, `EXPECTED: lūs`, `OUTPUTS: lūs`, with only `PGmc Final Z Deletion: *lūs` shown as an active historical step and no subsequent OE-side change before surface `Outcome: lūs` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3024-3043].
- The full trace says the same thing in more granular form: every rule is `[no-change]` except `PGmcFinalZDeletion`, which maps `*l*ū*s*z` to `*l*ū*s`; the form then passes unchanged through OE rules, orthography, and star-removal to `lūs` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.txt:17210-17324].

## Development-note summary

No securely row-specific `DEV_NOTES` block survives for `2113 louse / lūs`. There is no louse-specific mismatch essay, no row-local repair memo, and no preserved project dispute over `PROTO` versus `PROTOFORM`. The replacement slice therefore has to be conservative: current row-specific evidence comes from the live TSV and the exact-match derivation traces, while the relevant `DEV_NOTES` material is shared-background-only and concerns the chronology of final `*z` loss and rhotacism rather than this lexeme in particular [Germanic/data/germanic-aligned-final.tsv:707-709; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3024-3043; Germanic/docs/DEV_NOTES.md:3459-3540].

That shared material is still genuinely relevant because the live trace shows that the row’s whole derivation reduces to one step: `*lūsz → *lūs`, then no further phonological change before OE surface `lūs` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.txt:17237-17324]. The useful surviving DEV_NOTES substance is therefore the project’s rule-history memory for why final `*z` disappears without any rhotacized intermediate. DEV_NOTES explicitly corrected an earlier mistake and states: “Final `*‑z` was **never rhotacized**. It was already gone by the time rhotacism occurred” [Germanic/docs/DEV_NOTES.md:3471-3494].

For this row, that means three distinctions must stay explicit. First, `PROTO` and `PROTOFORM` are not in tension in the current row state; both are `*lūsz` [Germanic/data/germanic-aligned-final.tsv:709-709]. Second, the attested/target OE form is `lūs`, not a reconstructed intermediate, and the current traces already derive it exactly [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3024-3043]. Third, the surviving DEV_NOTES support is shared-background-only, not row-specific: it justifies treating final-`*z` loss as regular pipeline behavior, but it does **not** preserve a dedicated lexeme dossier for `louse` and should not be stretched into one [Germanic/docs/DEV_NOTES.md:3459-3540].

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-3459-3494

- Source heading: `Historical phonology of final *-z loss and its interaction with rhotacism`
- Source line hint: `3459-3494`
- Fragment type: `shared_background_only_rule_history`
- Status: `current`
- Issue tags: `final_z_loss`; `rhotacism_order`; `exact_match_background`
- Recommended next use: `cite only when explaining why the row's single active change is regular final-*z loss rather than any rhotacized pathway`
- Shared-with rows if relevant: `broadly all OE rows whose successful path depends on final *-z deletion rather than medial rhotacism`

This is the main surviving DEV_NOTES material for row 2113 even though it is not lexeme-specific. DEV_NOTES quotes Ringe-Taylor: “On the WGmc side, the loss of word-final `*z` in unstressed syllables ... must likewise have preceded the merger of `*z` with `*r`,” then adds Hogg’s confirming summary: “Gmc `/z/` yielded `/r/` in intervocalic position in Old English (rhotacism), but in final position it is generally lost” [Germanic/docs/DEV_NOTES.md:3463-3469]. DEV_NOTES then crystallizes the project conclusion in wording worth preserving verbatim: “Final `*-z` was **never rhotacized**. It was already gone by the time rhotacism occurred” [Germanic/docs/DEV_NOTES.md:3471-3477].

For row 2113, this fragment is shared-background-only support, but it is directly applicable to the current trace. The trace’s only active historical rule is `PGmcFinalZDeletion: *lūs`, and the DEV_NOTES section explains why that should be read as ordinary final-`*z` loss rather than as a missing `*z > r` stage or a row-specific exception [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.txt:17237-17245; Germanic/docs/DEV_NOTES.md:3488-3494]. Because no row-local louse note survives, this shared rule-history block is the closest DEV_NOTES comes to substantive support for the row.

### DEV_NOTES:line-3532-3540

- Source heading: `Summary of secondary sources on z-loss and rhotacism`
- Source line hint: `3532-3540`
- Fragment type: `shared_background_only_source_digest`
- Status: `current`
- Issue tags: `literature_summary`; `final_z_loss`; `no_row_specific_block`
- Recommended next use: `use when a later report needs the compact source map behind final-*z-loss claims without re-reading the whole section`
- Shared-with rows if relevant: `all rows documented from the shared final-*z-loss corridor`

This table is not row-specific either, but it is the cleanest compact digest of what DEV_NOTES thought the source base was. It aligns R/T, Hogg, and Luick on the same basic point: final `*z` is lost, rhotacism is medial/intervocalic, and the chronology is `z-loss before rhotacism` [Germanic/docs/DEV_NOTES.md:3532-3540]. For row 2113 that matters less as a new argument than as provenance control: if later writers need to say why `*lūsz` can pass straight to `*lūs`, this table preserves where DEV_NOTES expected that claim to be sourced.

Its status should remain explicitly shared-background-only. The table does **not** mention `louse`, `lūs`, or `*lūsz`; it does not discuss the lexical history of the noun; and it does not settle any finer question about the morphophonological history of the `*-sz` string beyond the broad final-`*z` behavior. Its usefulness is therefore documentary and conservative: it keeps the row anchored to the project’s general final-`*z` literature map without pretending that DEV_NOTES ever gave row 2113 a dedicated lexeme analysis [Germanic/docs/DEV_NOTES.md:3532-3540].

## Superseded or diagnostic material

- No row-specific superseded DEV_NOTES analysis was found for `2113 louse / lūs / *lūsz`. There is no surviving louse-specific mismatch block, no abandoned alternative `PROTOFORM`, and no packet/memo/report chain that would replace or compete with the current row state [Germanic/docs/lexeme_reports/coverage_audit.md:301-301; Germanic/docs/lexeme_reports/report_manifest.tsv:1-13].
- The row-specific material that **does** survive is diagnostic rather than archival prose: the current published and full traces show an exact match and make clear that, in present pipeline behavior, everything except final `*z` deletion is inert for this lexeme [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3024-3043; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.txt:17210-17324].
- Because the DEV_NOTES evidence is thin and shared, later writers should avoid inventing extra row history. At present there is no project-local basis in DEV_NOTES for claiming analogical reshaping, a special `*-sz` sub-rule, or any controversy over whether `lūs` is regular; the live row and the current trace both treat it as straightforward [Germanic/data/germanic-aligned-final.tsv:709-709; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3024-3043].

## Open questions for later work

- If a fuller lexeme report is ever commissioned, the first literature task should be attestation-focused: replace the present Wiktionary/Swadesh breadcrumbs with checked dictionary or handbook support for OE `lūs`, since no row-specific DEV_NOTES source audit survives [Germanic/data/old_english_wiktionary.tsv:174-174; Germanic/data/old_english_swadesh.tsv:49-49].
- If this row ever regresses, the first technical check should be rule ordering around `PGmcFinalZDeletion` versus `PGmcRhotacism`, because the current exact path depends almost entirely on final `*z` disappearing before any later OE work [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.txt:17219-17224,17237-17245; Germanic/docs/DEV_NOTES.md:3488-3494].
- If future indexing groups rows by surviving DEV_NOTES support, row 2113 should be tagged explicitly as `no row-specific DEV_NOTES block; shared final-*z-loss background only`, so later users do not assume a missing louse essay exists somewhere else in the notes [Germanic/docs/DEV_NOTES.md:3459-3540].
