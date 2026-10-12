---
row_id: 2167
concept: salve
counterpart: sealf
proto: *sálbō
protoform: *sálbō
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2167 salve / sealf

## Current row state

- CONCEPT: `salve` [Germanic/data/germanic-aligned-final.tsv:919-919]
- COUNTERPART: `sealf` [Germanic/data/germanic-aligned-final.tsv:919-919]
- PROTO: `*sálbō` [Germanic/data/germanic-aligned-final.tsv:919-919]
- PROTOFORM: `*sálbō` [Germanic/data/germanic-aligned-final.tsv:919-919]
- DERIVATION_CLASS: `regular` [Germanic/data/germanic-aligned-final.tsv:919-919]
- `oe_known_problems.tsv` currently has no row-local entry for row `2167`, lexeme `sealf`, concept `salve`, or proto/protoform `*sálbō`; the live problem list is presently limited to unrelated `u`-lowering and analogy cases, which is consistent with the row's regular status [Germanic/data/oe_known_problems.tsv:1-8].
- The current derivation trace already reaches the target without repair logic: `PROTO: *sálbō`, `EXPECTED: sealf`, `OUTPUTS: sealf`. The trace spells out `NWGmc Final Long O Raising: *sálbu`, then `Anglo Frisian Brightening: *sælbu`, `OE Breaking: *sealbu`, `PGmc B Allophony: *sealβu`, `OE High Vowel Apocope: *sealβ`, and finally surface `Outcome: sealf` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3853-3872].
- Coverage/report infrastructure currently shows no attached packet, research memo, or other linked analysis file for this row; the coverage audit lists row `2167 | salve | sealf | regular | no | - | - | - | none` [Germanic/docs/lexeme_reports/coverage_audit.md:337-337].

## Development-note summary

No dedicated `salve / sealf` memorandum survives in `Germanic/docs/DEV_NOTES.md`. The main securely attachable DEV_NOTES authority is therefore a shared audit table rather than a row-specific essay. That table lists row `2167` as `| 2167 | *sálbō | sealf | breaking |`, which is the crucial project-history classification to preserve: the OE target is being treated as an ordinary breaking outcome in the `*a + lC` environment, not as an exception, paradigm-cell substitution, or row-specific repair [Germanic/docs/DEV_NOTES.md:30604-30634]. The live TSV agrees completely with that status: `PROTO = PROTOFORM = *sálbō`, `COUNTERPART = sealf`, and `DERIVATION_CLASS = regular` [Germanic/data/germanic-aligned-final.tsv:919-919].

Because DEV_NOTES is classificatory rather than discursive here, the current derivation trace becomes important supporting row context. It shows the exact regular pathway that the inventory label `breaking` presupposes: inherited `*sálbō` first undergoes Northwest Germanic final long-`ō` raising to `*sálbu`, then Anglo-Frisian brightening to `*sælbu`, then OE breaking to `*sealbu`, then `b`-allophony to `*sealβu`, and finally high-vowel apocope to `*sealβ`, with orthographic `sealf` as the surface result [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3862-3872]. For replacement-note purposes, that means later reports should keep the row-level distinction explicit but simple: the comparative `PROTO` and OE-facing `PROTOFORM` are both still `*sálbō`, and the chosen OE target `sealf` is the regular outcome of that same form rather than of some alternative citation cell [Germanic/data/germanic-aligned-final.tsv:919-919; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3853-3872].

The later DEV_NOTES side-effect audit sharpens the practical implication. After broader A-restoration cleanup work, DEV_NOTES says: “For breaking-conditioned rows (`*xármaz, *márkō, *kálbaz, *fállaną` etc., 21 rows total), A-restoration is bled by breaking; unaffected” [Germanic/docs/DEV_NOTES.md:36628-36629]. Row 2167 is not re-listed there by number, but the earlier inventory had already put `*sálbō -> sealf` inside that same breaking-conditioned class [Germanic/docs/DEV_NOTES.md:30631-30632]. So the stable project reading is not merely that `sealf` happens to work today; it is that later restoration-oriented fixes were explicitly understood not to disturb rows of this type. The row's continued absence from `oe_known_problems.tsv` is exactly what that history predicts [Germanic/data/oe_known_problems.tsv:1-8].

One more useful but secondary DEV_NOTES observation is that the notes elsewhere use the same `salb-` root in weak-verb examples such as `*salbōdun > sealfodon` and `*salbōþi > sealfaþ` [Germanic/docs/DEV_NOTES.md:2810-2819]. Those are not authorities for the noun row's suffixal history, because they belong to a different morphological discussion. Even so, they confirm that the project independently expects inherited `salb-` to surface as OE `sealf-` once the ordinary brightening, breaking, and consonant developments apply. That shared-root evidence is useful as supporting context, but the row's governing current authority remains the inventory classification plus the live regular derivation trace [Germanic/docs/DEV_NOTES.md:2810-2819; Germanic/docs/DEV_NOTES.md:30604-30634; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3853-3872].

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-30604-30634

- Source heading: `Words in the TSV with proto *-aCl-* or *-aCr-* before a back-vowel tail`
- Source line or section hint: `lines 30604-30634`
- Fragment type: `phenomenon_context_for_lexeme`
- Status: `current`
- Issue tags: `breaking`; `regular_row`; `a_restoration_scope`; `a_plus_lc`; `protoform_vs_proto`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs: `1975,2008,2025,2077,2118,2166,2204,2271`

This is the main securely attachable DEV_NOTES fragment for row 2167. The note is an inventory for a broader audit, not a dedicated `sealf` essay, but it names the row directly and gives the classification later work must preserve: `| 2167 | *sálbō | sealf | breaking |` [Germanic/docs/DEV_NOTES.md:30631-30632]. That line establishes two concrete things. First, `sealf` belongs to the ordinary OE breaking class for inherited `*a` before `l` plus consonant; second, row 2167 is not the problem case the audit is trying to repair. The fragment therefore supports keeping `PROTO = PROTOFORM = *sálbō` and treating the OE target as regular, while also being honest that the surviving DEV_NOTES evidence is classificatory rather than lexeme-specific argumentation [Germanic/docs/DEV_NOTES.md:30604-30634; Germanic/data/germanic-aligned-final.tsv:919-919].

### DEV_NOTES:line-36625-36629

- Source heading: `side-effect audit after the A-restoration cleanup`
- Source line or section hint: `lines 36625-36629`
- Fragment type: `copied_shared_lexeme_fragment`
- Status: `current`
- Issue tags: `breaking`; `a_restoration`; `stability_after_fix`; `shared_row_class`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs: `1975,2008,2025,2077,2118,2166,2204,2271`

This later audit is short, but it is the clearest surviving statement of why row 2167 remained stable during later cleanup work. DEV_NOTES says: “For breaking-conditioned rows (`*xármaz, *márkō, *kálbaz, *fállaną` etc., 21 rows total), A-restoration is bled by breaking; unaffected” [Germanic/docs/DEV_NOTES.md:36628-36629]. Row 2167 is linked to that generalization by the earlier inventory entry `*sálbō | sealf | breaking` [Germanic/docs/DEV_NOTES.md:30631-30632]. For replacement-note purposes, the important takeaway is procedural: later work should not reopen `sealf` as an A-restoration casualty or as a silent regression, because DEV_NOTES explicitly treats rows of this class as outside the danger zone [Germanic/docs/DEV_NOTES.md:36625-36629].

### DEV_NOTES:line-2810-2819

- Source heading: `Non-final *ō (medial syllables)`
- Source line or section hint: `lines 2810-2819`
- Fragment type: `phenomenon_context_for_lexeme`
- Status: `background`
- Issue tags: `shared_root_example`; `salb_stem`; `breaking`; `b_allophony`; `medial_ō`
- Recommended next use: `keep_as_general_background`
- Shared with row IDs:

This is not a row-2167 note in the narrow sense, but it is the most useful same-root material elsewhere in DEV_NOTES. In a discussion of medial unstressed `*ō`, the notes give `*salbōdun 'they anointed' -> OE sealfodon` and `*salbōþi '(s)he anoints' -> OE sealfaþ` [Germanic/docs/DEV_NOTES.md:2810-2819]. Those forms should not be used to rewrite row 2167's noun-specific suffix history, because they belong to weak-verb morphology rather than to the nominal row now in the TSV. Their value is narrower and safer: they show that elsewhere in the project the inherited `salb-` root is independently expected to emerge as OE `sealf-`, which supports the current row's phonological plausibility without changing its `PROTOFORM` or derivational classification [Germanic/docs/DEV_NOTES.md:2810-2819; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3864-3872].

## Superseded or diagnostic material

No securely attachable row-specific superseded `sealf` dossier currently survives. The honest diagnostic fact is that DEV_NOTES never turned row 2167 into a live controversy; it preserved the row mostly as a control inside shared breaking audits [Germanic/docs/DEV_NOTES.md:30604-30634; Germanic/docs/DEV_NOTES.md:36625-36629]. Later writeups should resist inventing a lost debate about paradigm choice, analogical repair, or an OE-facing alternate protoform when the surviving project record does not support one.

One search hit needs explicit quarantine even though it looks temptingly close: DEV_NOTES also says `Class II weak iptv. 2sg *salbō -> OE sealfa` while discussing trimoric final `*ō` and the special `{*ô}` symbol in the FST [Germanic/docs/DEV_NOTES.md:2741-2756]. That passage is useful only as diagnostic background. It shares the same consonantal root and confirms that `salb-` can surface as `sealf-`, but it does **not** describe the noun row's actual suffixal pathway, because the note is about weak-verb morphology and explicitly about trimoric `*ō`, whereas row 2167's current derivation trace runs through `NWGmc Final Long O Raising: *sálbu` and then final-vowel apocope [Germanic/docs/DEV_NOTES.md:2741-2756; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3864-3872].

## Open questions for later work

- If a final lexeme report is drafted, decide whether the report should quote the current derivation trace alongside DEV_NOTES, since the row-specific DEV_NOTES evidence is chiefly classificatory and the trace is what preserves the exact modern rule sequence `*sálbō > *sálbu > *sælbu > *sealbu > *sealβu > *sealβ > sealf` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3862-3872; Germanic/docs/DEV_NOTES.md:30631-30632].
- Decide whether the same-root weak-verb examples (`sealfodon`, `sealfaþ`, and diagnostic `sealfa`) merit a brief background footnote in any future report or whether they should stay confined to background/diagnostic discussion so the noun row's morphology remains cleanly separated [Germanic/docs/DEV_NOTES.md:2741-2756; Germanic/docs/DEV_NOTES.md:2810-2819].
- If `dev_notes_slices/index.tsv` is later updated, the securely current anchors are the shared breaking inventory (`30604-30634`) and the later A-restoration side-effect audit (`36625-36629`); the same-root weak-verb passage is better indexed, if at all, as background rather than as the row's main authority [Germanic/docs/DEV_NOTES.md:2810-2819; Germanic/docs/DEV_NOTES.md:30604-30634; Germanic/docs/DEV_NOTES.md:36625-36629].
