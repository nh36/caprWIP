---
row_id: 2176
concept: shame
counterpart: sċamu
proto: *skámō
protoform: *skámō
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2176 shame / sċamu

## Current row state

- The live OE row currently reads `CONCEPT = shame`, `COUNTERPART = sċamu`, `PROTO = *skámō`, `PROTOFORM = *skámō`, `DERIVATION_CLASS = regular` [Germanic/data/germanic-aligned-final.tsv:954-954].
- `PROTO` and `PROTOFORM` are identical in the live row. No alternate OE-facing stem, no substitute paradigm cell, and no analogical repair input is encoded for this row at present; the same `*skámō` serves both as the comparative label and as the form fed into the current derivation trace [Germanic/data/germanic-aligned-final.tsv:954-954; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3995-4015].
- The same cognate-set neighborhood simultaneously shows unaccented `*skamō` in the English and German sister rows while the OE row keeps accented `*skámō`. In the surviving row materials, that looks like notation-level stress marking rather than evidence for different chronological stages or a different OE-directed protoform, because the row itself still keeps `PROTO = PROTOFORM = *skámō` and the live trace consumes that exact accented form directly [Germanic/data/germanic-aligned-final.tsv:953-955; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3995-4015].
- `oe_known_problems.tsv` has no row-local entry for row `2176`, for `shame`, for `sċamu`, or for `*skámō`; this lexeme is not currently tracked as an OE exception, wontfix item, or special repair case [Germanic/data/oe_known_problems.tsv:1-8].
- The current published derivation trace is an exact match and makes the active pathway explicit: `PROTO: *skámō`, `EXPECTED: sċamu`, `OUTPUTS: sċamu`; the only named historical steps are `NWGmc Final Long O Raising: *skámu` and then `OE Sk Palatalization: *ʃámu`, followed by orthographic `sċ*ámu` and surface `sċamu` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3995-4015].
- Coverage infrastructure currently lists row `2176` as `regular` with `NOTE? = no`, no attached report path, and requirement basis `none`, so this slice is replacement working documentation rather than evidence that the row is already a report-required exception bucket item [Germanic/docs/lexeme_reports/coverage_audit.md:344-344].

## Development-note summary

No dedicated `shame / sċamu / *skámō` mini-dossier appears to survive in `Germanic/docs/DEV_NOTES.md`. For row `2176`, the securely usable evidence is therefore shared rule-level DEV_NOTES material plus the live row state, the current published derivation trace, and one older transducer-status note that is only diagnostic history. Those sources all point in the same direction: row `2176` is currently a regular exact-match derivation with `PROTO = PROTOFORM = *skámō` and attested OE target `sċamu`, and the live system already derives that target directly without stem replacement, oblique-cell substitution, or analogical override [Germanic/data/germanic-aligned-final.tsv:954-954; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3995-4015].

The crucial positive DEV_NOTES evidence is the project’s explicit three-way analysis of word-final `*ō`. DEV_NOTES states under “Path A” that “PGmc word-final bimoric `*-ō` became short `*-u` in unstressed syllables in PNWGmc” and gives the implementation line `NWGmcFinalLongORaising: {*ō} → {*u} || _ .#.` [Germanic/docs/DEV_NOTES.md:2711-2720]. That is exactly the first step shown in the live trace for this row, `*skámō > *skámu` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4004-4009]. Just as importantly, DEV_NOTES immediately distinguishes this pathway from two other final-`*ō` histories: later word-final bimoric `*ō`, which goes to PWGmc `*a` and ultimately OE `-e`, and trimoric `*ō`, which remains a different class and ultimately yields OE `-a` [Germanic/docs/DEV_NOTES.md:2722-2745]. Row `2176` is therefore not a hidden `-e` row and not a hidden `-a` row. It is a straightforward Path-A `*-ō > *-u` row.

The second visible step in the current row behavior is not separately documented in surviving DEV_NOTES material for this lexeme, but it is explicit in the published trace: after final-`*ō` raising, the OE cascade applies `OE Sk Palatalization`, producing `*ʃámu`, and the orthographic layer writes that as `sċamu` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4008-4015]. For present row policy, that means the dossier should keep the levels distinct. `PROTO` and `PROTOFORM` are the same inherited pre-OE input `*skámō`; `sċamu` is the attested OE output after the row has passed through ordinary NWGmc final-vowel development and ordinary OE `sk > sċ` treatment. The lack of a row-local DEV_NOTES paragraph on this palatalization step should be stated plainly rather than hidden: the current positive authority here is the live derivation trace, not a surviving lexeme-specific prose note.

One older project note is still useful because it shows a now-rejected failure mode that directly affected this lexeme class. The January/February 2026 transducer-status report explicitly includes `*skamō → sċamu` in its audit of `*ō`-final OE rows and records that the old `EnglishLiquidLowering` rule was misconceived: it created final `*ɔː` values that never shortened and therefore contradicted correct OE outcomes such as `nosu`, `sacu`, `sċamu`, and `nǣdre` [Germanic/docs/germanic_transducer_report.md:11-16,39-48]. That material is not the current derivation account for row `2176`; the current derivation uses `NWGmcFinalLongORaising`, not `LiquidLowering`. But it is worth preserving as diagnostic history because it explains why an apparently simple `*-ō` row once needed chronology cleanup before settling into its present regular state.

The notation mismatch inside the cognate set should also be described conservatively. The English and German rows beside `2176` show unaccented `*skamō`, while the OE row uses accented `*skámō` [Germanic/data/germanic-aligned-final.tsv:953-955]. Nothing in the surviving DEV_NOTES evidence treats those as different chronological reconstructions. In this row dossier they are best understood as notation variants at different editorial layers, with the live OE row policy being the only binding one: `PROTO = PROTOFORM = *skámō`, target `sċamu`, derivation regular [Germanic/data/germanic-aligned-final.tsv:954-954; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3995-4015].

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-2711-2720

- Source heading: `The Three Fates of Word-Final *ō`
- Source line or section hint: `lines 2711-2720`
- Fragment type: `phenomenon_context_for_lexeme`
- Status: `current`
- Issue tags: `final_ō_raising`; `regular_pathway`; `protoform_vs_proto`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This is the strongest current DEV_NOTES fragment for row `2176` because it states the exact rule the live derivation now uses. DEV_NOTES says: “PGmc word-final bimoric `*-ō` became short `*-u` in unstressed syllables in PNWGmc,” and then gives the implementation line `NWGmcFinalLongORaising: {*ō} → {*u} || _ .#.` [Germanic/docs/DEV_NOTES.md:2711-2720]. For row `2176`, that is not generic background only; it is the precise explanation of the trace step `*skámō > *skámu` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4004-4009].

The practical row consequence is direct. Because the row is already word-final in `*-ō` at the PGmc stage, it does not need a revised `PROTOFORM`, a hidden oblique cell, or any special OE-side fix to get final `-u`. The live row’s `PROTO = PROTOFORM = *skámō` is therefore not merely convenient formatting; it matches the currently documented rule path exactly [Germanic/data/germanic-aligned-final.tsv:954-954; Germanic/docs/DEV_NOTES.md:2711-2720].

### DEV_NOTES:line-2722-2745

- Source heading: `The Three Fates of Word-Final *ō`
- Source line or section hint: `lines 2722-2745`
- Fragment type: `phenomenon_context_for_lexeme`
- Status: `current`
- Issue tags: `final_ō_typology`; `guardrail`; `not_path_b`; `not_path_c`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This adjoining fragment matters because it keeps the row from being misclassified once the final `-u` is observed. DEV_NOTES explicitly separates Path B, where bimoric `*ō` only becomes word-final later and ends up as PWGmc `*a` > OE `-e`, from Path C, where trimoric `*ō` ultimately yields OE `-a` [Germanic/docs/DEV_NOTES.md:2722-2745]. Row `2176` fits neither of those branches.

That negative evidence is useful at row level because `sċamu` could otherwise be described too loosely as just “some shortened final vowel.” The surviving DEV_NOTES material is more specific than that. It says the row belongs to the early word-final bimoric `*-ō > *-u` branch, and therefore the live target `sċamu` should be treated as a regular Path-A feminine ending, not as a reflex of the later `-e` pathway and not as a trimoric `-a` outcome [Germanic/docs/DEV_NOTES.md:2711-2745; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3995-4015].

## Superseded or diagnostic material

- No securely attachable row-local `shame / sċamu` dossier presently survives in `DEV_NOTES.md`; the usable current evidence is shared rule-level material, not a dedicated lexeme memorandum [Germanic/docs/DEV_NOTES.md:2711-2745].
- The main diagnostic project history is the now-superseded `EnglishLiquidLowering` investigation. The transducer-status report used `*skamō → sċamu` as one of the counterexamples showing that the deleted rule produced impossible long final vowels instead of the short/reduced outcomes that OE actually has [Germanic/docs/germanic_transducer_report.md:11-16,39-48]. That material should be preserved only to explain an older failure mode, not as the row’s current derivation account.
- The only other noticeable irregularity in the live row materials is editorial, not phonological: the cognate set mixes unaccented `*skamō` in neighboring non-OE rows with accented `*skámō` in the OE row [Germanic/data/germanic-aligned-final.tsv:953-955]. Nothing in the surviving DEV_NOTES evidence turns that into a stage distinction, so later reporting should not manufacture a `PROTO`/`PROTOFORM` split from accent marks alone.

## Open questions for later work

- If a later indexing pass includes regular control rows backed only by shared rule-level DEV_NOTES fragments, the strongest current anchors for row `2176` are the Path-A final-`*ō` rule (`2711-2720`) and the adjacent guardrail excluding the `-e`/`-a` pathways (`2722-2745`) [Germanic/docs/DEV_NOTES.md:2711-2745].
- If a future shared note on OE `sk > sċ` is written, row `2176` would benefit from citing it explicitly; at present the palatalization step is visible in the published derivation trace, but no securely attachable row-local DEV_NOTES prose for that step has been identified [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4008-4015].
- If the cognate-set proto spellings are ever normalized, decide whether the mixed `*skamō` / `*skámō` notation should be regularized across sibling rows. The current row itself is unaffected so long as `PROTO = PROTOFORM = *skámō` remains explicit in the OE line [Germanic/data/germanic-aligned-final.tsv:953-955].
