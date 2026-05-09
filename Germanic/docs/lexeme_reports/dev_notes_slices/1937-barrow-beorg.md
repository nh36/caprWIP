---
row_id: 1937
concept: barrow
counterpart: beorg
proto: *bérgą
protoform: *bérgą
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files: []
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 1937 barrow / beorg

## Current row state

- CONCEPT: `barrow`
- COUNTERPART: `beorg`
- PROTO: `*bérgą`
- PROTOFORM: `*bérgą`
- DERIVATION_CLASS: `regular`
- Live TSV row: the current Old English row keeps `COUNTERPART = beorg`, `PROTO = *bérgą`, `PROTOFORM = *bérgą`, and `DERIVATION_CLASS = regular`; the source column contains inherited-etymology placeholders rather than a row-local explanatory note [Germanic/data/germanic-aligned-final.tsv:20-20].
- Current implementation trace: the published derivation snapshot already reaches the live target without repair branching — `Proto Input: *bérgą`, then `OE Breaking: *béorgą`, then `OE Heavy Syllable Nasal Apocope: *béorg`, with surface `Outcome: beorg` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:45-64].
- Existing report infrastructure: `coverage_audit.md` still lists row 1937 as `regular` with `NOTE? no`, `Report status -`, and requirement basis `none`, so there is currently no packet, research memo, or attached row report to reuse [Germanic/docs/lexeme_reports/coverage_audit.md:191-193].

## Development-note summary

DEV_NOTES does not preserve a long lexeme-specific philological dossier for `barrow / beorg`. The materially relevant support is instead implementation history: row 1937 appears as one of the concrete examples used to motivate and validate the heavy-syllable deletion of final proto `*-ą` in Old English. In the archived 2026-02-06 note, the project says it implemented an experimental rule deleting `*-ą` after heavy syllables, describes that as an “empirically-derived phonological finding,” and explicitly warns that “Neither source explicitly extends this pattern to *-ą” even though the model improvement strongly favored doing so [Germanic/docs/DEV_NOTES.md:1591-1615]. `*bergą → beorg` is then listed among the showcase successes of that change: “`*bergą → beorg` ✓ (was: beorga)” [Germanic/docs/DEV_NOTES.md:1622-1628].

For row 1937, that is the core substance that needs preserving. DEV_NOTES is not mainly arguing about lexical identity, source selection, or an alternative protoform; it is documenting that the row's old failure state was spurious final `-a` (`beorga`), and that the adopted repair was heavy-syllable-conditioned nasal apocope after a heavy stem [Germanic/docs/DEV_NOTES.md:1617-1628]. The current derivation trace still reflects exactly that chronology: breaking applies first (`*béorgą`), and the final vowel is then removed by `OE Heavy Syllable Nasal Apocope`, yielding `beorg` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:54-64].

A second DEV_NOTES passage is relevant, but only as diagnostic history. In the 2026-01-01 `OE i-umlaut/fronting bucket diagnostics`, the row appears inside a heuristic subgroup labelled “back_vowel_follow_only: 98 (likely **a-restoration** contexts per Hogg),” with the concrete example “`*bergą → beorga` (expected beorg)” [Germanic/docs/DEV_NOTES.md:2595-2605]. That passage shows where the row sat during error triage, but it should not be mistaken for the final analysis. The live trace now shows that the `eo` vocalism is already present before the last step, so the surviving row-specific problem was not failure to produce `beor-`; it was failure to delete the final vowel after a heavy stem [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:54-64].

Accordingly, the replacement working note should be conservative. DEV_NOTES support for row 1937 is real, but it is narrow: it chiefly records a resolved implementation issue (`beorga` → `beorg`) and the project's willingness to generalize heavy-syllable apocope to proto `*-ą` despite thin explicit handbook wording [Germanic/docs/DEV_NOTES.md:1604-1615,1622-1628]. It does **not** preserve a substantial row-local literature review on `beorg` as a noun, nor a debate about `PROTOFORM`, nor a packet/memo workflow. The row therefore looks stable enough to document, but still thin in lexeme-specific DEV_NOTES substance [Germanic/docs/lexeme_reports/coverage_audit.md:191-193].

## Relevant DEV_NOTES fragments

### `Archived: Heavy Syllable Nasal Apocope (2026-02-06) — EMPIRICAL DISCOVERY`

- Source line or section hint: `lines 1591-1636`
- Fragment type: `copied_shared_lexeme_fragment`
- Status: `current`
- Issue tags: `heavy_syllable_nasal_apocope`; `final_vowel_extra`; `shared_implementation_history`; `resolved_row_mismatch`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This is the main DEV_NOTES fragment for row 1937. It says the project implemented “experimental rule deleting proto *-ą after heavy syllables,” calls the result an “empirically-derived phonological finding,” and states the literature problem plainly: “Neither source explicitly extends this pattern to *-ą” [Germanic/docs/DEV_NOTES.md:1595-1615]. The row then appears in the success list as a direct before/after example: “`*bergą → beorg` ✓ (was: beorga)” [Germanic/docs/DEV_NOTES.md:1622-1628]. For `barrow / beorg`, this is the passage that explains why the live row is now regular: the important project history is deletion of the old final `-a`, not reassignment of counterpart or proto input.

### `OE i-umlaut/fronting bucket diagnostics (2026-01-01)`

- Source line or section hint: `lines 2595-2605`
- Fragment type: `superseded_or_diagnostic_for_lexeme`
- Status: `superseded`
- Issue tags: `heuristic_bucket`; `a_restoration_diagnostic`; `beorga_stage`; `triage_history`
- Recommended next use: `use_only_for_project_history`
- Shared with row IDs:

This fragment is worth preserving because it shows the row's earlier diagnostic classification before the later apocope fix stabilized it. DEV_NOTES grouped many cases as “back_vowel_follow_only: 98 (likely **a-restoration** contexts per Hogg)” and included `*bergą → beorga (expected beorg)` among the examples [Germanic/docs/DEV_NOTES.md:2599-2605]. For row 1937, that is diagnostic rather than authoritative: it records that `beorga` was once surfacing in a broad fronting/umlaut audit bucket, but the current published trace shows the decisive missing step was final-vowel deletion after breaking had already produced `beor-` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:54-64].

## Superseded or diagnostic material

- The 2026-01-01 fronting/umlaut bucket note should not be over-read as the row's settled analysis. Its value is historical triage only: it preserves that `*bergą → beorga` once appeared inside a heuristic “a-restoration” bucket, not that row 1937 genuinely required an a-restoration solution [Germanic/docs/DEV_NOTES.md:2599-2605].
- The 2026-02-06 heavy-syllable apocope note is itself headed `Archived`, but the fragment remains materially current for this row because the present published derivation still uses `OE Heavy Syllable Nasal Apocope` as the final successful step from `*béorgą` to `*béorg` [Germanic/docs/DEV_NOTES.md:1591-1597; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:54-64].
- `coverage_audit.md` currently shows no packet, memo, or prior report attachment for row 1937, so later indexing should not assume that a larger lexeme-report infrastructure already exists behind this slice [Germanic/docs/lexeme_reports/coverage_audit.md:191-193].

## Open questions for later work

- If a later packet or research memo is created for row 1937, add a source audit for the lexical equation `*bérgą > beorg` itself; the current DEV_NOTES evidence is strong on implementation history but thin on lexeme-specific literature handling.
- Decide whether this slice is strong enough for eventual indexing, or whether it should remain effectively no-index because its substantive DEV_NOTES support is mostly one shared implementation fragment plus one diagnostic triage fragment [Germanic/docs/DEV_NOTES.md:1591-1636,2595-2605; Germanic/docs/lexeme_reports/coverage_audit.md:191-193].
- If future cleanup revisits the old “back_vowel_follow_only / likely a-restoration” bucket, make sure row 1937 remains classified under resolved heavy-stem final-vowel deletion rather than being reabsorbed into a broader and less precise fronting bucket [Germanic/docs/DEV_NOTES.md:2599-2605].
