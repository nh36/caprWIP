---
row_id: 1995
concept: dream
counterpart: drēam
proto: *dráugmaz
protoform: *dráugmaz
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files: Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 1995 dream / drēam

## Current row state

- The live aligned row is `1995	dream	drēam	PROTO *dráugmaz	PROTOFORM *dráugmaz	DERIVATION_CLASS regular`, so the comparative label, the OE-facing derivational input, and the selected OE counterpart are currently aligned rather than split across different spellings [Germanic/data/germanic-aligned-final.tsv:248-250].
- The published derivation trace is an exact match and shows the present operative chain explicitly: `Proto Input: *dráugmaz`, `Gm Simplification: *dráumaz`, then `PGmc Final Z Deletion: *dráuma`, `OE Au Fronting: *dráeuma`, `OE Diphthong Leveling: *drēama`, `PWGmc Final Bare A Loss: *drēam`, with final `Outcome: drēam` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:975-995].
- `oe_known_problems.tsv` has no entry for row `1995`, for `dream`, for `drēam`, or for `*dráugmaz`; the row is therefore not being tracked as a live OE exception at present [Germanic/data/oe_known_problems.tsv:1-8].
- No reusable packet or research memo turned up for this exact row. The coverage audit still lists row `1995` as `none`, and `report_manifest.tsv` currently contains only pilot/report rows and no entry for `1995` [Germanic/docs/lexeme_reports/coverage_audit.md:226-226; Germanic/docs/lexeme_reports/report_manifest.tsv:1-13].

## Development-note summary

No standalone drēam-only DEV_NOTES subsection survives in the same way that some harder rows have dedicated packets or memos. The usable material for row `1995` comes instead from a shared `*gm`-cluster investigation opened around `tēam` and from the later fix note that explicitly says `drēam` was updated along with `tēam` [Germanic/docs/DEV_NOTES.md:16029-16067,16167-16223]. This means the support here is real but partly shared: later writers should not pretend that DEV_NOTES preserved a long dream-only dossier when it mostly preserved comparative-source quotations and a project-level implementation decision.

The key philological substance that does survive is still worth carrying forward verbatim. DEV_NOTES preserves Kroonen's dream entry as `*drauma-` and quotes: `"*drauma- m. 'dream' — ON draumr m. 'id.' ... OE dréam m. 'id.' ... G Traum m. 'id.' > *d*roug*-mo- (DRV). Continuing *draugma-, a mo-stem derived from the strong verb *dreugan- (q.v.)"` [Germanic/docs/DEV_NOTES.md:16042-16051]. That quotation matters because it distinguishes a post-loss citation form from an earlier derivational stage: Kroonen cites `*drauma-`, but explicitly derives it from `*draugma-`. DEV_NOTES also preserves Orel's shorter headword `"*draumaz sb.m.: ON draumr 'dream', OE dreám 'joy, pleasure', OFris dràm 'dream', OS dròm id., OHG troum id."`, which shows a different editorial practice but still a post-loss `*draumaz` rather than an overt `*draugmaz` citation form [Germanic/docs/DEV_NOTES.md:16061-16063].

The project history inside DEV_NOTES has two stages that should not be collapsed. In the earlier analysis, `drēam` was treated as the already-post-loss comparator and was used as an argument for normalizing `tēam` to match it: DEV_NOTES says, `Our TSV already uses "*draumăz" for drēam, not "*draugmăz"` and then records `Row 1995: PROTOFORM "*draumăz", PROTO "*draumăz", expected "drēam" ✓` [Germanic/docs/DEV_NOTES.md:16097-16098,16161-16162]. That is now stale project history, not the live row state.

The later fix note supersedes that recommendation. DEV_NOTES then decides: `Implement as FST sound change rule (Option B with refinement)` and explicitly records that both affected rows were moved to the Verner-voiced `*g` stage, including `drēam: "*draumăz" → "*draugmăz" (all language rows)` [Germanic/docs/DEV_NOTES.md:16169-16185,16207-16214]. The live row now shows the same decision in current orthography as `*dráugmaz`, and the trace confirms that the grammar itself performs `Gm Simplification` before the usual OE vocalic developments [Germanic/data/germanic-aligned-final.tsv:248-250; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:975-995].

The main distinction to preserve, then, is four-way rather than two-way: (1) Kroonen's citation form `*drauma-`, (2) Orel's citation form `*draumaz`, (3) the project's earlier internal row state `*draumăz`, now superseded, and (4) the current live project input `*dráugmaz`, which the transducer reduces to `*dráumaz` before later OE steps [Germanic/docs/DEV_NOTES.md:16042-16063,16097-16098,16161-16162,16207-16214; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:984-995]. The attested OE-side target remains `drēam`; the question is only how much earlier derivational structure the project chooses to preserve in `PROTO/PROTOFORM`.

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-16042-16051

- Source label line: `DEV_NOTES:line-16042-16051`
- Source heading: `Source Research: Reconstruction Forms`
- Source line or section hint: `lines 16042-16051`
- Fragment type: `copied_shared_source_fragment`
- Status: `current`
- Issue tags: `source_reconstructions`; `kroonen`; `drv`; `gm_loss`; `citation_form_vs_derivational_stage`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs: 2241

This is the most important surviving source quotation for row `1995`, even though it was preserved inside a shared `*gm` discussion rather than a dream-only note. DEV_NOTES quotes Kroonen's entry in full enough to retain the crucial distinction between headword and pre-form: `"*drauma- m. 'dream' ... > *d*roug*-mo- (DRV). Continuing *draugma-, a mo-stem derived from the strong verb *dreugan- (q.v.)"` [Germanic/docs/DEV_NOTES.md:16042-16051]. For later work, the value of this fragment is not merely that it gives a lexeme gloss list; it also shows that Kroonen's preferred citation form is already post-loss, while the etymological discussion still overtly presupposes an earlier `*draugma-`.

That distinction maps cleanly onto the current row if handled carefully. The live project row does **not** simply reuse Kroonen's printed headword `*drauma-`; instead it keeps the earlier derivational stage as `*dráugmaz`, then lets the grammar produce `*dráumaz` by `Gm Simplification` [Germanic/data/germanic-aligned-final.tsv:248-250; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:984-989]. This fragment is therefore current evidence for the philological background of the row, but not direct authority for the exact current project spelling.

### DEV_NOTES:line-16061-16063

- Source label line: `DEV_NOTES:line-16061-16063`
- Source heading: `Source Research: Reconstruction Forms`
- Source line or section hint: `lines 16061-16063`
- Fragment type: `copied_shared_source_fragment`
- Status: `current_with_caution`
- Issue tags: `source_reconstructions`; `orel`; `post_loss_citation`; `comparative_support`
- Recommended next use: `cite_as_secondary_support_only`
- Shared with row IDs: 2241

DEV_NOTES also preserves Orel's dream entry: `"*draumaz sb.m.: ON draumr 'dream', OE dreám 'joy, pleasure', OFris dràm 'dream', OS dròm id., OHG troum id."` [Germanic/docs/DEV_NOTES.md:16061-16063]. This is weaker than the Kroonen fragment for present project purposes, because it does not discuss the earlier `*draugma-` stage and because DEV_NOTES itself uses Orel mainly to highlight mixed editorial practice across related lexemes.

Even so, the fragment should be kept in the slice because it shows that a reputable secondary source can cite dream with a post-loss headword while the project now prefers an earlier derivationally explicit `*g` stage internally. It is therefore useful comparative context, but later prose should not overstate it as direct support for the exact live row spelling `*dráugmaz`.

### DEV_NOTES:line-16167-16223

- Source label line: `DEV_NOTES:line-16167-16223`
- Source heading: `Fix Applied (2026-04-09)`
- Source line or section hint: `lines 16167-16223`
- Fragment type: `copied_shared_decision_fragment`
- Status: `current`
- Issue tags: `fst_decision`; `gm_simplification`; `verners_law`; `current_row_policy`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs: 2241

This is the fragment that governs the live row. DEV_NOTES states the project decision plainly: `Implement as FST sound change rule (Option B with refinement)` and then explains why the consonant should be written as voiced `*g` rather than voiceless `*x`: Kroonen marks both `*tauma-` and `*drauma-` as `(DRV)`, so the relevant segment is interpreted as Verner-voiced [Germanic/docs/DEV_NOTES.md:16169-16185]. The note is shared because it was written as a two-lexeme policy change, but it is row-relevant in the strongest possible sense: it explicitly lists `drēam: "*draumăz" → "*draugmăz" (all language rows)` and then reports `*draugmăz → drēam ✓` [Germanic/docs/DEV_NOTES.md:16207-16214].

For row `1995`, this fragment should be treated as present project authority even though the live TSV now writes the same decision with the acute-accent house style `*dráugmaz` rather than the older breve-based spelling `*draugmăz` [Germanic/data/germanic-aligned-final.tsv:248-250]. The published trace confirms that this was not only an editorial note but an implemented derivation: `Proto Input: *dráugmaz`, `Gm Simplification: *dráumaz`, and final `Outcome: drēam` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:984-995].

## Superseded or diagnostic material

### DEV_NOTES:line-16095-16166

- Source label line: `DEV_NOTES:line-16095-16166`
- Source heading: `Analysis: Which Approach is Better?` / `Recommendation`
- Source line or section hint: `lines 16095-16166`
- Fragment type: `superseded_project_history_fragment`
- Status: `superseded`
- Issue tags: `option_a`; `post_loss_normalization`; `old_row_state`; `project_reversal`
- Recommended next use: `use_as_project_history_only`
- Shared with row IDs: 2241

This fragment matters because it preserves the project decision that was **not** kept. DEV_NOTES first argued for normalizing `tēam` to the same post-loss practice then thought to be used by `drēam`: `Our TSV already uses "*draumăz" for drēam, not "*draugmăz". Using "*taumăz" would be parallel` [Germanic/docs/DEV_NOTES.md:16097-16098]. The same section then records the stale state explicitly: `Row 1995: PROTOFORM "*draumăz", PROTO "*draumăz", expected "drēam" ✓` [Germanic/docs/DEV_NOTES.md:16161-16162].

That material should now be cited, if at all, only as project chronology. It no longer describes the live row, because the immediately following fix note reversed the recommendation and moved the project to FST-handled `*gm > *m` plus Verner-voiced `*g`, yielding current `*dráugmaz` > `drēam` [Germanic/docs/DEV_NOTES.md:16167-16223; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:975-995]. Its value is diagnostic: it explains why older discussions or stale local notes may refer to `*draumăz` for this row.

## Open questions for later work

- If a later packet or final report cites Kroonen or Orel, it should state explicitly that their printed dream headwords are post-loss citation forms (`*drauma-`, `*draumaz`), whereas the current live project row intentionally keeps an earlier derivational stage `*dráugmaz` and lets the grammar perform the simplification [Germanic/docs/DEV_NOTES.md:16042-16063,16167-16223; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:984-995].
- If the row is ever indexed in `dev_notes_slices/index.tsv` later, the safest current anchors are the Kroonen source fragment and the fix-applied fragment. The Option A discussion should be indexed, if at all, only as superseded project history [Germanic/docs/DEV_NOTES.md:16042-16051,16095-16223].
- There is still no row-specific packet or memo for `1995`, so any future longer-form writeup should say plainly that the surviving DEV_NOTES support is partly shared with `2241 tēam` rather than pretending that a dream-only dossier survives [Germanic/docs/lexeme_reports/coverage_audit.md:226-226; Germanic/docs/lexeme_reports/report_manifest.tsv:1-13].
