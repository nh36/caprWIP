---
row_id: 2178
concept: sheath
counterpart: sċēaþ
proto: *skáiθiz
protoform: *skáiθiz
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2178 sheath / sċēaþ

## Current row state

- The live OE row currently reads `CONCEPT = sheath`, `COUNTERPART = sċēaþ`, `PROTO = *skáiθiz`, `PROTOFORM = *skáiθiz`, `DERIVATION_CLASS = regular` [Germanic/data/germanic-aligned-final.tsv:962-962].
- `PROTO` and `PROTOFORM` are identical. The row is therefore not using a special OE-facing substitute input, an oblique-form workaround, or a paradigm-cell retargeting; the same Proto-Germanic form serves both as comparative label and as derivational input for the attested OE target [Germanic/data/germanic-aligned-final.tsv:962-962].
- DEV_NOTES writes the protoform as `*skaiθiz` without the acute accent, while the live TSV and the current derivation trace use `*skáiθiz`. In context this is only a notation difference, not a different stage form and not a competing row policy: DEV_NOTES treats `*skaiθiz` as the same i-stem source that yields `*skāθiz > *ʃǣθ > *ʃēaθ`, and the live trace does the same with the accented spelling [Germanic/docs/DEV_NOTES.md:11175-11196; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4038-4057].
- `oe_known_problems.tsv` has no surviving entry for row `2178`, for `sheath`, for `sċēaþ`, or for `*skáiθiz/*skaiθiz`, so the row is no longer being tracked as a live unresolved OE exception [Germanic/data/oe_known_problems.tsv:1-8].
- Coverage infrastructure still shows no linked packet, research memo, or dossier for this row; the coverage audit lists row `2178` as `regular` with all linked-report fields blank and issue status `none` [Germanic/docs/lexeme_reports/coverage_audit.md:346-346].
- The current published derivation trace is an exact match and preserves the live stage sequence now used by the grammar: `PWGmc Ai Monophthongization: *skāθiz`, `PGmc Final Z Deletion: *skāθi`, `OE Sk Palatalization: *ʃāθi`, `OE I Umlaut: *ʃǣθi`, `OE Ws Palatal Diphthongization: *ʃēaθi`, `OE High Vowel Apocope: *ʃēaθ`, with orthographic outcome `sċēaþ` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4037-4057].

## Development-note summary

Row `2178` does have a dedicated DEV_NOTES section, and unlike many replacement slices it is not merely inferred from shared background audits. The section opens as a mismatch note — “Row 2178 in the TSV: `*skaiθiz` → expected `sċēaþ`, got `sċǣþ`” — but its lasting value is the explicit philological claim that both forms are attested and that the dataset's selected target is specifically the West Saxon palatal-diphthongized form. DEV_NOTES quotes Campbell §185 directly: “with ǣ, the mutation of ā: `sǣǣþ` sheath, beside `sċēaþ`,” then states that “both `sċǣþ` and `sċēaþ` are valid OE forms” and that the `ēa` form arises from West Saxon palatal diphthongization after an initial palatal [Germanic/docs/DEV_NOTES.md:11173-11186]. The row dossier therefore has to preserve a distinction between **possible OE reflexes in general** and the **particular OE target chosen for this row**. The fix was not from “impossible” to “possible”; it was from one attested reflex (`sċǣþ`) to the attested West Saxon reflex (`sċēaþ`) that the row is meant to model [Germanic/docs/DEV_NOTES.md:11177-11186; Germanic/data/germanic-aligned-final.tsv:962-962].

The section is also unusually explicit about chronological layers, and those layers should not be collapsed into the row header. The live row keeps `PROTO = PROTOFORM = *skáiθiz`, while DEV_NOTES' derivation lists `PGmc *skaiθiz`, `PWGmc *skāθiz`, OE `*skǣθ`, OE `*ʃǣθ`, and finally West Saxon `sċēaþ` [Germanic/data/germanic-aligned-final.tsv:962-962; Germanic/docs/DEV_NOTES.md:11190-11196]. These are not rival stored protoforms. `*skaiθiz/*skáiθiz` is the comparative and OE-facing input in current row policy; `*skāθiz`, `*ʃǣθ(i)`, and `*ʃēaθ(i)` are chronological stage forms inside the derivation; and `sċēaþ` is the attested OE target selected in the TSV [Germanic/docs/DEV_NOTES.md:11190-11196; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4044-4057]. The accent difference between `*skaiθiz` and `*skáiθiz` is just house notation, whereas the later starred forms reflect genuine chronological stages.

The core analytical point preserved in DEV_NOTES is the rule ordering. The note says plainly that “**i-umlaut must precede WS palatal diphthongization** for the `ēa` outcome” [Germanic/docs/DEV_NOTES.md:11198-11200]. DEV_NOTES then spells out why. Under the old order, `sk` palatalizes first and the form reaches West Saxon diphthongization as `*ʃāθiz`; because that rule targets `ǣ`, not `ā`, it does nothing, and later i-umlaut yields only `sċǣþ` [Germanic/docs/DEV_NOTES.md:11202-11217]. Under the reordered chronology, the `*-iz` tail first triggers `*ā > *ǣ`, producing `*ʃǣθ`, and only then does West Saxon palatal diphthongization apply, giving `*ʃēaθ` and surface `sċēaþ` [Germanic/docs/DEV_NOTES.md:11219-11234]. The current published derivation trace now mirrors exactly that successful order on the live row: `*skāθi > *ʃāθi > *ʃǣθi > *ʃēaθi > *ʃēaθ > sċēaþ` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4050-4057].

The implementation result inside DEV_NOTES is also still current enough to preserve, because it records that the proposed rule reorder was actually adopted and kept. DEV_NOTES states: “Moved OEIUmlaut before OEWsPalatalDiphthongization,” then records the outcome `*skaiθiz → sċēaþ ✓ (was sċǣþ)` and notes that the total mismatch count remained unchanged at that check-point [Germanic/docs/DEV_NOTES.md:11272-11278]. The same block also records a trade-off against `*geftiz`, but the row-local conclusion is explicit: “Keep the i-umlaut reordering because: 1. The sċēaþ fix is well-documented (Campbell §185)” [Germanic/docs/DEV_NOTES.md:11280-11299]. That matters for this slice because it means the `sheath` row is not just an old proposal site; it is the named control case that justified the currently retained chronology.

The later `gift` correction note makes that control-case status even clearer. In arguing that regular `*geftiz` should yield `ġift`, not `ġieft`, DEV_NOTES says: “This chronology is confirmed by the `*skaiθiz → sċēaþ` case documented above. For `sċēaþ` to show `ēa` (from `ǣ` via WS palatal diph), the i-umlaut (`*ā → *ǣ`) must have already applied” [Germanic/docs/DEV_NOTES.md:11324-11329]. So row `2178` is not only a repaired mismatch; it is also preserved in project history as the positive argument for the live ordering of i-umlaut relative to West Saxon palatal diphthongization. Combined with the exact-match trace and the absence of any `oe_known_problems.tsv` entry, the conservative present-tense conclusion is that row `2178` is a regular, indexable control lexeme with a dedicated current DEV_NOTES rationale, while the older “incorrect order” subsection should be cited only as resolved bug history [Germanic/docs/DEV_NOTES.md:11202-11234,11272-11299,11324-11329; Germanic/data/oe_known_problems.tsv:1-8].

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-11173-11200

- Source heading: `I-Umlaut / WS Palatal Diphthongization Chronology (2026-03-17)`
- Source line or section hint: `lines 11173-11200`
- fragment_type: `lexeme_specific`
- current_status: `current`
- Issue tags: `ws_palatal_diphthongization`; `i_umlaut`; `attested_variant`; `protoform_vs_target`
- recommended_next_use: `cite_in_final_report`
- Shared with row IDs:

This is the controlling lexeme-specific fragment for row `2178`. It names the row directly, states the former mismatch `*skaiθiz -> sċǣþ`, preserves the crucial Campbell quotation, and then gives the row-specific historical chain `PGmc *skaiθiz > PWGmc *skāθiz > OE *skǣθ > OE *ʃǣθ > WS sċēaþ` [Germanic/docs/DEV_NOTES.md:11173-11200]. For later reporting, the most important use of the fragment is not the old failure state by itself but the explicit source-backed claim that both `sċǣþ` and `sċēaþ` are attested while the `ēa` form is the West Saxon palatal-diphthongized outcome [Germanic/docs/DEV_NOTES.md:11180-11196]. That makes the fragment securely indexable as current row authority.

### DEV_NOTES:line-11272-11299

- Source heading: `Implementation Result (2026-03-17)`
- Source line or section hint: `lines 11272-11299`
- fragment_type: `lexeme_specific`
- current_status: `current`
- Issue tags: `rule_order_fix`; `resolved_mismatch`; `campbell_support`; `project_history`
- recommended_next_use: `cite_in_final_report`
- Shared with row IDs:

This fragment records the actual closure decision rather than only the proposed chronology. DEV_NOTES says the grammar was changed by moving `OEIUmlaut` before `OEWsPalatalDiphthongization`, and it then records the concrete row result `*skaiθiz → sċēaþ ✓ (was sċǣþ)` [Germanic/docs/DEV_NOTES.md:11272-11278]. The same note matters because it preserves why the change was kept despite collateral effects elsewhere: “The `sċēaþ` fix is well-documented (Campbell §185)” and the mismatch total did not worsen in aggregate [Germanic/docs/DEV_NOTES.md:11280-11299]. For row `2178`, this is current policy-setting material, not merely a stale to-do list.

### DEV_NOTES:line-11324-11329

- Source heading: `Why i-umlaut precedes WS palatal diphthongization`
- Source line or section hint: `lines 11324-11329`
- fragment_type: `phenomenon_context_for_lexeme`
- current_status: `current`
- Issue tags: `chronology_control_case`; `i_umlaut`; `ws_palatal_diphthongization`; `shared_sound_change`
- recommended_next_use: `cite_in_final_report`
- Shared with row IDs:

This short follow-up is valuable because it shows that DEV_NOTES continued to use `sheath / sċēaþ` as the evidentiary control for the final chronology. In resolving the separate `gift` issue, DEV_NOTES says the ordering is “confirmed by the `*skaiθiz → sċēaþ` case” because `sċēaþ` can only show `ēa` if i-umlaut has already converted `*ā` to `*ǣ` before West Saxon palatal diphthongization applies [Germanic/docs/DEV_NOTES.md:11324-11329]. This is not the primary lexeme note, but it is strong current supporting context for why the row's derivation should be treated as settled in the present grammar.

## Superseded or diagnostic material

### DEV_NOTES:line-11202-11234

- Source heading: `Current FST Rule Order (INCORRECT)` / `Proposed Fix: Reorder Rules`
- Source line or section hint: `lines 11202-11234`
- fragment_type: `superseded_or_diagnostic_for_lexeme`
- current_status: `diagnostic_only`
- Issue tags: `old_rule_order`; `resolved_bug_history`; `sċǣþ_output`; `implementation_diagnostic`
- recommended_next_use: `use_as_project_history_only`
- Shared with row IDs:

This block should be preserved, but only as diagnostic history. It records the former incorrect order in `germanic.txt`, explains why that order produced `sċǣþ`, and sketches the rule reorder that would fix the row [Germanic/docs/DEV_NOTES.md:11202-11234]. The explanation remains useful because it makes the former bug mechanically transparent: palatalization created initial `ʃ`, but the vowel was still `ā`, so West Saxon palatal diphthongization had nothing to target until it was too late [Germanic/docs/DEV_NOTES.md:11213-11217]. What is no longer current is the label “INCORRECT” plus the proposal framing itself; the live trace and the later implementation-result note show that the reorder has already been adopted for the published derivation [Germanic/docs/DEV_NOTES.md:11272-11299; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4050-4057].

- The adjacent action list (`Move OEIUmlaut ...`, `Verify sċēaþ now works`, `Check for regressions`) is likewise superseded as an action tracker, because the row now matches exactly in the published derivation trace and the implementation-result note records the fix as already applied [Germanic/docs/DEV_NOTES.md:11263-11268,11272-11278; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4037-4057].
- The stale part of the dossier is therefore the project-history framing, not the linguistic core. Campbell's attestation of both forms, the `*skāθiz > *ʃǣθ(i) > *ʃēaθ(i)` chronology, and the row's role as a control case for i-umlaut ordering all remain live and suitable for later index integration [Germanic/docs/DEV_NOTES.md:11180-11200,11295-11299,11324-11329].

## Open questions for later work

- If a packet or final report is later written, keep the notation layers explicit near the top: comparative/live row `PROTO = PROTOFORM = *skáiθiz`, DEV_NOTES house spelling `*skaiθiz` as the same input, intermediate chronological stages such as `*skāθiz` and `*ʃǣθ(i)`, and attested OE target `sċēaþ` [Germanic/data/germanic-aligned-final.tsv:962-962; Germanic/docs/DEV_NOTES.md:11175-11196; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4044-4057].
- If later philological polishing wants a one-sentence dialect note, it should say plainly that `sċǣþ` is still an attested OE form but that this row deliberately indexes the West Saxon palatal-diphthongized reflex `sċēaþ`, following the DEV_NOTES reading of Campbell §185 [Germanic/docs/DEV_NOTES.md:11180-11186; Germanic/data/germanic-aligned-final.tsv:962-962].
- If `dev_notes_slices/index.tsv` is updated later, the safest current anchors are `DEV_NOTES:line-11173-11200` and `DEV_NOTES:line-11272-11299`, with `DEV_NOTES:line-11324-11329` optional as shared chronology support. Do not index `11202-11234` or the action list as though they were still live row policy [Germanic/docs/DEV_NOTES.md:11202-11234,11263-11268,11272-11299,11324-11329].
