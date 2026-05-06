---
row_id: 2159
concept: rope
counterpart: rāp
proto: *ráipą
protoform: *ráipą
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2159 rope / rāp

## Current row state

- The live OE row currently reads `CONCEPT = rope`, `COUNTERPART = rāp`, `PROTO = *ráipą`, `PROTOFORM = *ráipą`, `DERIVATION_CLASS = regular` [Germanic/data/germanic-aligned-final.tsv:888-888].
- `PROTO` and `PROTOFORM` are still identical here. This row is therefore **not** using a special OE-facing substitute protoform, a different paradigm cell, or a workaround input; the same `*ráipą` serves both as comparative label and as derivational input for the OE target `rāp` [Germanic/data/germanic-aligned-final.tsv:888-888].
- `oe_known_problems.tsv` currently has no entry for row `2159`, for `rope`, for `rāp`, or for `*ráipą`; the present file contents are limited to unrelated problem rows [Germanic/data/oe_known_problems.tsv:1-8].
- The current published derivation trace is an exact match and gives the full live pathway now used by the grammar: `PROTO: *ráipą`, `EXPECTED: rāp`, `OUTPUTS: rāp`, with the staged history `PWGmc Ai Monophthongization: *rāpą` and then `OE Heavy Syllable Nasal Apocope: *rāp` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3710-3729].
- Coverage infrastructure still shows no linked packet, research memo, or dossier for this row beyond the slice being created here; the coverage audit lists row `2159` as `regular` with all linked-report fields empty and issue status `none` [Germanic/docs/lexeme_reports/coverage_audit.md:330-330].

## Development-note summary

No securely attachable **row-numbered** rope dossier survives in `Germanic/docs/DEV_NOTES.md`. The usable material for row `2159` is instead shared phonological support plus the live derivation trace. The current grammar already derives the target cleanly as `*ráipą > *rāpą > rāp`, and the shared DEV_NOTES material supports the first half of that chain directly: stressed Proto-/West-Germanic `*ai` becomes `*ā`, not `*ē`, and the later chronology summary repeats that `*ai > *ā` belongs before the specifically Old English processes [Germanic/docs/DEV_NOTES.md:13943-13968,29548-29558; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3710-3729]. For this row, that means the long vowel of OE `rāp` is not a special lexeme-specific adjustment. It is the ordinary stressed-monophthongization outcome of `*ráipą`.

The second half of the derivation is more delicate and the slice needs to preserve that delicacy. The live trace currently labels the final step as `OE Heavy Syllable Nasal Apocope`, but DEV_NOTES does **not** preserve a current rope-specific literature discussion for that rule. What it does preserve is (i) an older general chronology note that word-final `*-a` and `*-ą` are lost very early and that final nasal vowels are denasalized, and (ii) an explicitly **archived** empirical note that experimented with deleting final `*-ą` after heavy syllables because that improved many OE outputs [Germanic/docs/DEV_NOTES.md:1529-1533,1591-1645]. A later weak-tail note then narrows a different final-`*ą` problem (`*-aną > -an`) without turning `rope / rāp` into a mismatch dossier [Germanic/docs/DEV_NOTES.md:2531-2533]. The safest current replacement-note conclusion is therefore conservative: the live model's exact-match output `rāp` is secure, but the slice should not pretend that DEV_NOTES contains a dedicated philological essay proving the row from primary literature line by line.

That conservative framing matters because the literal English gloss **rope** appears elsewhere in DEV_NOTES in ways that are not row authority. One occurrence is Kroonen's headword `*tauma- m. 'rein, bridle, rope'` inside the completely different `tēam` discussion, where the point is loss of `*g` in `*taugma-`, not the etymology of `rāp` [Germanic/docs/DEV_NOTES.md:16001-16040]. Another is the spear note's warning that Greek `sparton` 'rope' is from a different root and is not a cognate of `spere` [Germanic/docs/DEV_NOTES.md:28682-28698]. Those passages are useful only as scope guards: they confirm that a simple search for “rope” in DEV_NOTES returns false positives, so row `2159` should be documented from the shared sound-change notes and the row-local trace, not from unrelated lexeme discussions.

The row-level distinction between `PROTO`, `PROTOFORM`, and OE target is accordingly simple but still worth stating explicitly. `PROTO = *ráipą` is the comparative reconstruction; `PROTOFORM = *ráipą` is the same input because no paradigm-cell substitution or workaround is currently needed; and the selected OE target is the exact regular output `rāp` [Germanic/data/germanic-aligned-final.tsv:888-888; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3710-3729]. This slice should therefore be used as a **shared-support control note**: it preserves the securely relevant DEV_NOTES material that explains why the row is regular, while also recording that no richer row-local DEV_NOTES dossier currently exists.

## Relevant DEV_NOTES fragments

No securely attachable **current row-specific** DEV_NOTES fragment survives for `2159`. The fragments below are the shared current notes that actually support the live row.

### DEV_NOTES:line-13943-13968

- Source heading: `Revised analysis: Two separate changes for *ai (2026-04-06)`
- Source line or section hint: `lines 13943-13968`
- Fragment type: `copied_shared_lexeme_fragment`
- Status: `current`
- Issue tags: `ai_monophthongization`; `stressed_vs_unstressed`; `shared_row_support`; `regular_pathway`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This is the clearest current DEV_NOTES support for the first half of the row's derivation. The note insists that stressed and unstressed `*ai` must be treated as two different historical changes, and it states the point row `2159` needs in explicit terms: “PWGmc `*ai → *ā` (stressed)” is the regular West Germanic monophthongization, while unstressed `*ai` belongs to a different NWGmc development [Germanic/docs/DEV_NOTES.md:13945-13960].

For `*ráipą > rāp`, this fragment establishes that the vowel of the OE target comes from the ordinary stressed pathway, not from a special lexeme-specific repair. Because the `*ai` in `*ráipą` is root-stressed, the row belongs on the `*hailaz > hāl` side of the split, not on the weak-tail `*spannai > spanne` side [Germanic/docs/DEV_NOTES.md:13951-13960]. That is exactly what the live trace now shows when it outputs `PWGmc Ai Monophthongization: *rāpą` before the final-vowel step [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3721-3723].

### DEV_NOTES:line-29548-29558

- Source heading: `Standard relative chronology`
- Source line or section hint: `lines 29548-29558`
- Fragment type: `phenomenon_context_for_lexeme`
- Status: `current`
- Issue tags: `relative_chronology`; `final_nasal_vowel_loss`; `ai_monophthongization`; `shared_row_support`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This shared chronology fragment is the best compact statement of where row `2159` sits in the broader OE pipeline. DEV_NOTES summarizes the sequence as: WGmc loss of final `*-z`, shortening of final unstressed `*-ō`, and “loss of final nasal vowels”; then pre-OE `*a > *æ` in unstressed syllables and `*ai > *ā`; then specifically OE processes such as breaking, back umlaut, and high-vowel apocope by syllable weight [Germanic/docs/DEV_NOTES.md:29548-29558].

For `2159`, this fragment does not replace the row trace, but it does keep later writeups from mislocating the row's changes. It confirms that `*ai > *ā` is a pre-OE/shared development and that final nasal-vowel loss belongs to the general historical chronology rather than to a `rope`-specific exception note [Germanic/docs/DEV_NOTES.md:29552-29558]. Read together with the trace, it supports the practical row-level conclusion `*ráipą > *rāpą > rāp` without requiring any altered `PROTOFORM` or exceptional bucket [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3719-3729; Germanic/data/germanic-aligned-final.tsv:888-888].

## Superseded or diagnostic material

### DEV_NOTES:line-1591-1645

- Source heading: `Archived: Heavy Syllable Nasal Apocope (2026-02-06) — EMPIRICAL DISCOVERY`
- Source line or section hint: `lines 1591-1645`
- Fragment type: `superseded_or_diagnostic_for_lexeme`
- Status: `diagnostic_only`
- Issue tags: `heavy_syllable_nasal_apocope`; `archived_analysis`; `final_ą_loss`; `project_history`
- Recommended next use: `use_as_project_history_only`
- Shared with row IDs:

This archived note is the closest DEV_NOTES comes to naming the exact final step shown in the current `rāp` trace. It reports an experiment that deleted final `*-ą` after heavy syllables, cites large empirical improvements, and lists heavy-stem examples such as `*bergą → beorg`, `*wurdą → word`, and `*blōdą → blōd` [Germanic/docs/DEV_NOTES.md:1595-1633]. That makes it relevant to row `2159`, because after `*ráipą > *rāpą` the stem is likewise heavy and the live trace currently still labels the row's last step `OE Heavy Syllable Nasal Apocope` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3721-3723].

But the note is explicitly archived, and later DEV_NOTES material does not preserve it as a clean current literature-backed rule for this lexeme. A later entry instead replaces a different `*-aną` problem with a narrower weak-tail nasal-vowel rule [Germanic/docs/DEV_NOTES.md:2531-2533]. So for row `2159`, this fragment should be kept only as diagnostic history explaining why the live trace uses that rule name, not as strong standalone authority that the `rāp` row has a dedicated settled `*-ą` essay behind it.

Two additional scope cautions should be preserved even though they are not row authority. First, the `tēam` note quotes Kroonen's `*tauma- m. 'rein, bridle, rope'` and remarks that the original form was `*taugma-`; this is about the `team` family and should not be cited as evidence for `rāp` [Germanic/docs/DEV_NOTES.md:16001-16040]. Second, the spear note's statement that Greek `sparton` 'rope' is from a different root is part of the `spere` etymology discussion and likewise does no row-level work for `2159` [Germanic/docs/DEV_NOTES.md:28682-28698]. Both passages matter only because a literal search for the English gloss can otherwise make DEV_NOTES look richer for this row than it really is.

## Open questions for later work

- If a packet or memo is later created, keep the row's three layers explicit near the top: comparative `PROTO *ráipą`, identical OE-facing `PROTOFORM *ráipą`, and regular OE target `rāp` from the live exact-match derivation [Germanic/data/germanic-aligned-final.tsv:888-888; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3710-3729].
- If later review wants a stronger literature-facing defense of the final `*-ą > ∅` step for heavy stems, that work will need fresh source canvassing. The present slice can securely preserve the archived project-history note and the shared chronology, but it should not claim that DEV_NOTES already contains a dedicated current rope-specific authority for that exact issue [Germanic/docs/DEV_NOTES.md:1591-1645,29548-29558].
- If `dev_notes_slices/index.tsv` is updated later, index only the shared current support (`*ai > *ā` and general chronology) and, if needed, the archived heavy-syllable nasal-apocope note as diagnostic history. Do **not** index the unrelated `tauma-/sparton` passages as though they were rope-row authorities [Germanic/docs/DEV_NOTES.md:13943-13968,1591-1645,29548-29558,16001-16040,28682-28698].
