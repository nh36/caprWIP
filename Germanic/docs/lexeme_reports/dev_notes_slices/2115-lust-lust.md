---
row_id: 2115
concept: lust
counterpart: lust
proto: *lústuz
protoform: *lústuz
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files: []
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2115 lust / lust

## Current row state

- The live TSV row is fully regular on its face: `PROTO = *lústuz`, `PROTOFORM = *lústuz`, `COUNTERPART = lust`, `DERIVATION_CLASS = regular`, and the note field is empty apart from duplicated Wiktionary-source placeholders rather than a row-local analysis [Germanic/data/germanic-aligned-final.tsv:717-717].
- `PROTO` and `PROTOFORM` are not split for this row. That matters because the surviving DEV_NOTES material treats `*lustuz` precisely as the kind of u-stem nominative singular that can be used directly, not as a comparative headword that needs a cell-switch or analogical rescue [Germanic/data/germanic-aligned-final.tsv:717-717; Germanic/docs/DEV_NOTES.md:92-98].
- `oe_known_problems.tsv` has no entry for `*lústuz` or `lust`, so the row is not currently triaged as an exception, mismatch bucket, or known bug case [Germanic/data/oe_known_problems.tsv:1-8].
- Lexeme-report scaffolding is absent: `coverage_audit.md` marks row `2115` as `none`, and `report_manifest.tsv` has no entry for it, so there is no inherited packet or memo to mine for row-specific prose [Germanic/docs/lexeme_reports/coverage_audit.md:302-302; Germanic/docs/lexeme_reports/report_manifest.tsv:1-13].
- The current published derivation snapshot already matches the row with no repair note: `PROTO: *lústuz`, `EXPECTED: lust`, `OUTPUTS: lust`, with the condensed chain `PGmc Final Z Deletion: *lústu` and `OE High Vowel Apocope: *lúst`, then `Outcome: lust` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3044-3063].
- The fuller trace confirms the same rule profile in more detail: `NWGmcULowering` does nothing, the form remains `*l*u*s*t*u` through the shared OE pipeline, and only `HighVowelApocope` removes the final high vowel before orthographic `lust` surfaces [Germanic/docs/debug_snapshots/oe_full_trace_report_2026-03-11.txt:8583-8636].

## Development-note summary

No dedicated row-specific DEV_NOTES block survives for `lust / lust`. The usable material is instead a very compact but unusually direct sentence inside the shared u-lowering-exception discussion: DEV_NOTES cites `*lustuz` itself as the positive example of why a real u-stem nominative singular preserves `u` regularly, writing, “For example, *lustuz (u-stem nom.sg.) → OE lust with preserved u” [Germanic/docs/DEV_NOTES.md:92-98].

For row 2115, that sentence is not a speculative workaround. It aligns exactly with the live row state: the row already uses `*lústuz` as both `PROTO` and `PROTOFORM`, and the current trace reaches `lust` without any exceptional blocking rule, analogical reshaping, or stem-class override [Germanic/data/germanic-aligned-final.tsv:717-717; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3044-3063].

The larger shared context also matters because it explains why `lust` appears there at all. DEV_NOTES opens by reaffirming the regular law that stressed `*u` lowers to `*o` before a following non-high vowel, then asks whether problematic forms like `wulf`, `fugol`, and `bucc` could be rescued by adopting a paradigm cell with high-vowel endings. In that argument, `*lustuz` is the control case showing what a genuine u-stem escape cell looks like. For row 2115, the safest conclusion is therefore conservative and positive: no special problem survives; the row is regular because its live protoform already has the high-vowel ending that keeps u-lowering from being triggered [Germanic/docs/DEV_NOTES.md:68-70,88-98].

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-88-98

- Source heading: `Could we use paradigm forms? (Why we decided not to)` / `Approach A: Use a u-stem or root-noun form.`
- Source line hint: `Germanic/docs/DEV_NOTES.md:88-98`
- Fragment type: `row_specific_example_embedded_in_shared_background`
- Status: `current`
- Issue tags: `u_stem`; `u_lowering`; `positive_control`; `proto_equals_protoform`
- Recommended next use: `primary_row_anchor`
- Shared-with rows if relevant: `1973 buck / bucc`; `2030 fowl / fugol`; `2162 rust / rust`; `2298 wolf / wulf`; `2300 wool / wull`

This is the single most important surviving DEV_NOTES fragment for row 2115 because it names the row's protoform directly. The shared discussion asks whether certain apparent u-lowering exceptions could be regularized by switching to a paradigm form with high-vowel endings. DEV_NOTES then states the general rule in a form that is directly usable here: “R/T notes that u-stems and root nouns regularly preserve *u because their paradigms have predominantly high-vowel suffixes (nom.sg. *-uz, acc.sg. *-ŷ, gen.sg. *-iz, dat.sg. *-i, nom.pl. *-iz, etc.).” It immediately gives the row-specific example: “For example, *lustuz (u-stem nom.sg.) → OE lust with preserved u (R/T p.45)” [Germanic/docs/DEV_NOTES.md:92-93].

For row 2115, the first sentence is shared-background-only, but the second is row-specific support in the narrowest possible sense: the surviving note does not merely mention an analogous lexeme; it uses this lexeme as the demonstration that a genuine u-stem nominative singular is already regular. The rest of the fragment is mostly about why this move is illegitimate for `wulf`, `fugol`, and `bucc`, because “Using a u-stem nom.sg. would require us to posit a stem-class that is not attested in any daughter language. This would be philologically indefensible” for those rows [Germanic/docs/DEV_NOTES.md:95-98]. That negative material is not row-local evidence for `lust`, but it is still useful diagnostic context: it shows that `lust` functioned in DEV_NOTES as the accepted control example, not as one more doubtful rescue attempt.

### DEV_NOTES:line-932-969

- Source heading: `R/T (vol.2, p.385) on OE u-stems` / `Why u-lowering doesn't apply`
- Source line hint: `Germanic/docs/DEV_NOTES.md:932-969`
- Fragment type: `shared_background_only_current_rule_state`
- Status: `current`
- Issue tags: `u_stem`; `stem_class`; `rule_explanation`; `diagnostic`
- Recommended next use: `use_only_for_general_mechanism`
- Shared-with rows if relevant: `1992 door / dor`; `2143 nose / nosu`; `other OE u-stem rows`

This later DEV_NOTES block is not about `lust`, but it preserves the current project explanation of why true u-stem forms are regular rather than exceptional. In the `door` discussion, DEV_NOTES writes out the relevant contrast explicitly: `*durą` (a-stem) gives regular lowered `dor`, while `*duruz` (u-stem) gives `duru`, and “The u-stem nominative singular *-uz has a high vowel in the ending, so the root vowel *u is not before a non-high vowel. U-lowering is not triggered” [Germanic/docs/DEV_NOTES.md:963-969].

For row 2115 this fragment is shared-background-only, not row-specific evidence. Still, it preserves the clearest surviving prose statement of the mechanism already implicit in the `*lustuz → lust` example above. Combined with the live trace, it supports a plain working conclusion: `*lústuz` is being treated as the right kind of input for regular OE `lust`, not as a hidden exception or a later analogical reshaping [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3044-3063].

### Debug snapshot: current published derivation

- Source heading: `lust`
- Source line hint: `Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3044-3063`
- Fragment type: `row_specific_current_state`
- Status: `current`
- Issue tags: `trace`; `regular_derivation`; `no_exception_handling`
- Recommended next use: `use_to_confirm_live_pipeline`
- Shared-with rows if relevant: none

This is not DEV_NOTES, but it is necessary row-specific support because DEV_NOTES itself gives only the control-example sentence and not a full current derivation. The published trace shows exactly the regular pipeline that the DEV_NOTES example presupposes: `PROTO: *lústuz`, `EXPECTED: lust`, `OUTPUTS: lust`; earlier Germanic development reduces only final `-z` (`*lústu`), and the OE side then applies `OE High Vowel Apocope: *lúst`, yielding `Outcome: lust` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3044-3063]. This confirms that the row's current status is genuinely regular and that no extra note about exception handling is missing from the live system.

## Superseded or diagnostic material

No row-specific superseded DEV_NOTES block survives for `lust / lust`, and there is no sign that row 2115 ever underwent the kind of paradigm-cell rollback seen for `wulf`, `fugol`, `bucc`, or `rust` [Germanic/docs/DEV_NOTES.md:25940-26197]. For this row, the absence is meaningful: `*lustuz` appears in DEV_NOTES as the accepted positive control, not as an abandoned experiment.

The only diagnostic caution worth preserving is small but real. The raw full trace prints the header as `PROTO: *lustuz` without the acute accent, whereas the live TSV and published derivation report both use accented `*lústuz`; this is a display-level normalization difference, not evidence for a competing `PROTOFORM` [Germanic/data/germanic-aligned-final.tsv:717-717; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3044-3047; Germanic/docs/debug_snapshots/oe_full_trace_report_2026-03-11.txt:8583-8588].

Coverage infrastructure is also diagnostically empty rather than silently missing. `coverage_audit.md` says `none`, and `report_manifest.tsv` has no row entry, so later work should not assume there is an unextracted packet or memo somewhere else in the repo [Germanic/docs/lexeme_reports/coverage_audit.md:302-302; Germanic/docs/lexeme_reports/report_manifest.tsv:1-13].

## Open questions for later work

- If a later full lexeme report is written, decide whether to make the u-stem morphology explicit in the row prose (`u-stem nom.sg. *-uz`) rather than leaving that information implicit in the protoform and trace [Germanic/docs/DEV_NOTES.md:92-93,963-969].
- If later literature review is desired, check whether independent handbook citation for `lust` as a masculine u-stem should be copied into row-local materials; the present slice only preserves the DEV_NOTES-mediated R/T example, which is enough for current workflow but still second-order evidence [Germanic/docs/DEV_NOTES.md:92-93].
- If packet scaffolding is ever added for this row, keep the scope narrow: there is no surviving problem dossier to reconstruct, only a regular derivation plus one directly relevant DEV_NOTES control-example sentence [Germanic/docs/lexeme_reports/coverage_audit.md:302-302; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3044-3063].
