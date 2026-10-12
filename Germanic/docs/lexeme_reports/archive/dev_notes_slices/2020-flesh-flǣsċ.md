---
row_id: 2020
concept: flesh
counterpart: flǣsċ
proto: *fláiskiz
protoform: *fláiskiz
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
  - Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md
  - Germanic/docs/non_firing_rules_analysis.md
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2020 flesh / flǣsċ

## Current row state

- The live OE row is `ID 2020`, `CONCEPT flesh`, `COUNTERPART flǣsċ`, `PROTO *fláiskiz`, `PROTOFORM *fláiskiz`, `DERIVATION_CLASS regular` [Germanic/data/germanic-aligned-final.tsv:347-350].
- The row presently carries only inherited source markers from Wiktionary etymology and no live exception flag, repair tag, or row-local warning in the aligned TSV [Germanic/data/germanic-aligned-final.tsv:349-349].
- `coverage_audit.md` still lists row `2020` as a regular uncovered row with `NOTE? no`, no packet, no research memo, no dossier, and `Requirement basis = none`, so this slice is replacing absent row-level report scaffolding rather than summarizing an existing packet stack [Germanic/docs/lexeme_reports/coverage_audit.md:243-243].
- `oe_known_problems.tsv` has no entry keyed to `2020`, `flesh`, `flǣsċ`, or `*fláiskiz`; the row is therefore not currently tracked as an active OE exception bucket or wontfix item [Germanic/data/oe_known_problems.tsv:1-8].
- The current published derivation trace is an exact match: `PROTO: *fláiskiz`, `EXPECTED: flǣsċ`, `OUTPUTS: flǣsċ`, with the explicit intermediate chain `*flāskiz > *flāski > *flāʃi > *flǣʃi > *flǣʃ > *flǣsċ > flǣsċ` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1402-1422].
- DEV_NOTES discusses the repair mostly with unaccented forms such as `*flaiskiz`, `*flaiski`, and older `*flaiskăz`; the live row's accented `*fláiskiz` should therefore be read cautiously as current repository notation for the same lexical item, not automatically as a different philological claim [Germanic/docs/DEV_NOTES.md:6358-6448; Germanic/data/germanic-aligned-final.tsv:349-349].

## Development-note summary

Unlike many regular rows, `flesh / flǣsċ` does have a dedicated row-level DEV_NOTES block, and that block preserves a concrete repair history rather than only shared policy. The note says the TSV formerly carried an a-stem proto-form `*flaiskăz`; under that setup the FST yielded `flāsc`, whereas the expected Old English target is `flǣsċ`, specifically “with `ǣ` from i-umlaut and palatal `ċ` from palatalization after front vowel” [Germanic/docs/DEV_NOTES.md:6358-6365]. The surviving DEV_NOTES argument is therefore not that `flǣsċ` is doubtful, but that the earlier proto-side stem-class assignment was wrong for Old English.

The row-specific evidential core is also unusually explicit. DEV_NOTES preserves Orel's statement that OE `flǣsc` is an “**i-stem**,” Ringe & Taylor's repeated PWGmc derivation from `*flaiski` to OE `flǣsċ`/`flǣsc`, Campbell's direct use of `flǣsċ` as an example of palatalization “after an umlauted vowel,” and Campbell's note on spellings such as `flésċ` [Germanic/docs/DEV_NOTES.md:6368-6404]. Those quotations do not all use exactly the same orthography as the live row: DEV_NOTES cites both `flǣsc` and `flǣsċ`, and the comparative reconstruction appears as `*flaiski` or `*flaiskiz` rather than the live row's accented `*fláiskiz`. Still, the shared thrust is stable and specific: Old English is being treated as the branch that preserves an umlaut-triggering i-stem, and the surface OE form accordingly shows both fronted vowel quality and palatalized `sc/sċ` [Germanic/docs/DEV_NOTES.md:6370-6440].

The current row state fits that repair. DEV_NOTES explicitly contrasts the good path for i-stem `*flaiskiz` with the bad path for a-stem `*flaiskaz`, then records the fix as “Changed PROTOFORM from `*flaiskăz` → `*flaiskiz`” [Germanic/docs/DEV_NOTES.md:6414-6440]. The live row now has `*fláiskiz` in both proto columns, and the published derivation reaches exact `flǣsċ` output without any remaining exception handling [Germanic/data/germanic-aligned-final.tsv:349-349; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1402-1422]. What should remain conservative is the phrasing around chronology and notation: DEV_NOTES gives a handbook-backed stem-class argument and a simplified phonological contrast, while the published trace shows the repo's current operational rule ordering. Those are compatible at a practical row level, but they are not identical genres of evidence [Germanic/docs/DEV_NOTES.md:6414-6428; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1413-1422].

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-6358-6375

- Source heading: `OE flǣsċ 'flesh': Fix proto-form *flaiskiz (2026-03-10)` plus `Orel (2003) p.108, s.v. *flaiskaz`
- Source line or section hint: `lines 6358-6375`
- Fragment type: `row_specific_problem_statement_with_literature_quote`
- Status: `current`
- Issue tags: `stem_class_repair`; `i_stem`; `umlaut_trigger`; `row_local_fix`
- Recommended next use: `primary citation when explaining why earlier a-stem input was rejected for OE`
- Shared with row IDs:

This opening fragment preserves the actual row problem statement and should remain the first authority cited for the slice. DEV_NOTES says plainly that the TSV had `*flaiskăz` as “a-stem,” that the FST then produced `flāsc`, and that the expected form is `flǣsċ`, “with `ǣ` from i-umlaut and palatal `ċ` from palatalization after front vowel” [Germanic/docs/DEV_NOTES.md:6360-6365]. That wording is important because it ties the bad output to two separate OE failures at once: no umlauted vowel and no palatalized `sc`.

Orel is then quoted directly: `"*flaiskaz sb.n.: ON flesk 'pork', **OE flǣsc 'meat' (i-stem)**, OFris flāsk id., OS flēsk id., OHG fleisc id. Of uncertain origin."` [Germanic/docs/DEV_NOTES.md:6368-6373]. The safest use of that quotation is narrow but decisive. DEV_NOTES takes it as evidence that OE should be modeled with an i-stem reflex even if the wider lexical family can still be cited under a `*flaiskaz` headword in a comparative dictionary. The quote should not be stretched into a claim that every West Germanic daughter preserved the same stem class, because the rest of the note explicitly allows divergence there [Germanic/docs/DEV_NOTES.md:6373-6375,6430-6435].

### DEV_NOTES:line-6376-6386

- Source heading: `Ringe & Taylor vol.2 pp.234-235 (§6.6.2)`
- Source line or section hint: `lines 6376-6386`
- Fragment type: `row_specific_source_quote_for_protoform`
- Status: `current`
- Issue tags: `pwgmc_i_stem`; `protoform_support`; `comparative_pathway`; `oe_target_support`
- Recommended next use: `best quoted support when a later memo needs the comparative-to-OE pathway spelled out`
- Shared with row IDs:

This is the strongest surviving row-specific comparative quotation. DEV_NOTES reports that Ringe & Taylor “explicitly list `*flaiski` as the PWGmc form for 'flesh'” and then preserves two quotations: `"PWGmc *flaiski 'flesh, meat' (OS flēsk, OHG fleisc) > *flæsci > OE flǣsċ"` and `"PWGmc *flaiski 'flesh, meat' (OF, OS flēsk, OHG fleisc) > *flæsci > OE flǣsc"` [Germanic/docs/DEV_NOTES.md:6376-6385]. The orthographic mismatch between `flǣsċ` and `flǣsc` is already present inside DEV_NOTES itself, so later use should preserve that caution rather than silently normalizing the quotations.

The practical point, however, is clear enough for row work: DEV_NOTES treats Ringe & Taylor as confirming an i-stem nominative in the pre-OE stage and an OE outcome with umlauted front vowel [Germanic/docs/DEV_NOTES.md:6384-6386]. That is the best row-local support for the repair from older `*flaiskăz` to `*flaiskiz`. It also explains why the live row's current `*fláiskiz` should be read as aligned in substance with the DEV_NOTES repair even though the live TSV uses the repo's accented notation rather than the exact typography of the quotation [Germanic/data/germanic-aligned-final.tsv:349-349; Germanic/docs/DEV_NOTES.md:6439-6440].

### DEV_NOTES:line-6388-6404

- Source heading: `Campbell (1959) §442 (Palatalization of sc)` plus `Campbell (1959) §291 (VP and Li. forms)`
- Source line or section hint: `lines 6388-6404`
- Fragment type: `row_specific_surface_form_support`
- Status: `current`
- Issue tags: `palatalization`; `umlauted_vowel`; `scribal_spellings`; `surface_oe`
- Recommended next use: `cite when distinguishing umlaut evidence from later palatalized surface spelling`
- Shared with row IDs: `2014`

Campbell is the key handbook support for the OE surface shape. DEV_NOTES quotes §442: `"sc was palatalized and assibilated after any front vowel, original or due to umlaut, e.g. æsc ash, disc dish, fisc fish, risc rush, the suffix -isc, and **after an umlauted vowel flǣsċ flesh**."` [Germanic/docs/DEV_NOTES.md:6388-6395]. For this row, that quotation matters because it directly joins the two parts of the argument that the bad older output `flāsc` failed to satisfy: the vowel must count as front/umlauted, and once it does, `sc` is expected to palatalize.

DEV_NOTES then adds Campbell §291: `"VP many examples including ... flésċ flesh; ... Li. single occurrences of flésċ, huuēte"` and glosses the `é` spelling as representing “the i-umlaut of `*ai`” [Germanic/docs/DEV_NOTES.md:6397-6404]. That is useful but should still be handled conservatively. The quotation supports umlaut-sensitive spelling evidence and makes `flésċ` part of the documented record preserved in DEV_NOTES; it does not by itself settle every detail of the repo's internal intermediate chronology. Its best use is to show that DEV_NOTES preserved handbook evidence for both umlauted vocalism and palatalized `sc` in the OE tradition.

### DEV_NOTES:line-6405-6412

- Source heading: `Kluge-Seebold (2011) p.318, s.v. 'Fleisch'`
- Source line or section hint: `lines 6405-6412`
- Fragment type: `comparative_source_audit_with_internal_caution`
- Status: `current`
- Issue tags: `comparative_wgmc_base`; `daughter_language_divergence`; `do_not_overcorrect`
- Recommended next use: `cite only when a later note must explain why a WGmc *fleiska- style citation does not automatically overturn the OE i-stem repair`
- Shared with row IDs:

This fragment is valuable mostly because DEV_NOTES already tells the reader how not to misuse it. The preserved quotation is: `"Aus wg. *fleiska- n. 'Fleisch', auch in ae. flǣsc, afr. flēsk; dazu anord. flesk(i) 'Speck'..."` [Germanic/docs/DEV_NOTES.md:6405-6408]. Standing alone, that could be mistaken for evidence that the row should revert to an a-stem-style reconstruction.

DEV_NOTES immediately blocks that inference, adding: `"Kluge-Seebold reconstructs the WGmc root as *fleiska-, but this doesn't conflict with OE being an i-stem — the stem class can differ by daughter language. The OE i-stem is confirmed by the i-umlaut evidence."` [Germanic/docs/DEV_NOTES.md:6410-6412]. For later row work, the fragment should therefore be treated as comparative background plus an explicit warning against flattening all daughter-language stem classes into one live OE input.

### DEV_NOTES:line-6414-6448

- Source heading: `The phonological development`, `Why OE has an i-stem while other WGmc languages have a-stem`, and `The fix`
- Source line or section hint: `lines 6414-6448`
- Fragment type: `row_specific_resolution_and_repo_fix_record`
- Status: `current`
- Issue tags: `phonological_contrast`; `fixed_protoform`; `supersedes_flāsc`; `repo_history`
- Recommended next use: `controlling citation for the final row-level repair history`
- Shared with row IDs:

This closing fragment records the actual decision that changed the row. DEV_NOTES lays out a contrastive mini-derivation. For the i-stem `*flaiskiz`, it gives: `*ai` undergoes i-umlaut from `*-iz`, `*-sk-` becomes palatal after front vowel `ǣ`, and final `*-iz` is lost, yielding `flǣsċ`; for the a-stem `*flaiskaz`, it gives monophthongization to `ā`, lack of palatalization, and loss of final `*-az`, yielding `flāsc` [Germanic/docs/DEV_NOTES.md:6414-6428]. Even if later repository traces express the rule ordering with more operational detail, this is still the clearest preserved statement of what distinction the repair was meant to capture.

The same fragment also states the comparative interpretation and the concrete repo action. DEV_NOTES says that “the PWGmc form was `*flaiski` (i-stem neuter). OE preserved this, while OS and OHG shifted to an a-stem `*fleiska-`,” then records: `Changed PROTOFORM from *flaiskăz → *flaiskiz (i-stem nominative)` [Germanic/docs/DEV_NOTES.md:6430-6440]. The final line `Evaluation: 308/386 OE matches (79.8%)` is best read as contemporaneous batch diagnostics, not as a live warning on row `2020` now that the published trace gives exact `flǣsċ` [Germanic/docs/DEV_NOTES.md:6448-6448; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1402-1422].

## Superseded or diagnostic material

- `non_firing_rules_analysis.md` preserves the older failure as `*flaiskăz -> flāsc (expected flǣsċ)` under the `I-Umlaut Missing` bucket [Germanic/docs/non_firing_rules_analysis.md:493-505]. That is useful diagnostic history, but it is superseded for row-level reporting by the later DEV_NOTES repair and by the current exact published trace.
- The current published trace is positive confirmation, not itself a DEV_NOTES fragment. It shows the row now succeeds with live `*fláiskiz`, but its staged sequence `*flāskiz > *flāski > *flāʃi > *flǣʃi` is the repository's operational derivation display rather than a verbatim handbook quotation [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1411-1422].
- DEV_NOTES itself preserves mixed orthographies (`flǣsc` and `flǣsċ`) and mixed reconstruction spellings (`*flaiski`, `*flaiskiz`, later live `*fláiskiz`) [Germanic/docs/DEV_NOTES.md:6378-6440; Germanic/data/germanic-aligned-final.tsv:349-349]. Those should be retained as notation history and source-specific spelling, not flattened into claims that the row currently has multiple competing lexical analyses.

## Open questions for later work

- If a later packet is created, decide whether the live accented `PROTO/PROTOFORM *fláiskiz` needs an explicit notation note against DEV_NOTES `*flaiskiz/*flaiski`, or whether the present slice's conservative wording is enough [Germanic/data/germanic-aligned-final.tsv:349-349; Germanic/docs/DEV_NOTES.md:6378-6440].
- If later reporting wants to describe chronology in more detail, audit the relationship between DEV_NOTES's simplified i-stem vs a-stem contrast and the published trace's operational rule ordering before claiming more than the current evidence supports [Germanic/docs/DEV_NOTES.md:6414-6428; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1411-1422].
- If this row is indexed later, preserve the distinction between what is handbook-backed and what is repo-side implementation detail: the literature support directly backs OE i-stem status, umlauted/fronted vowel quality, and palatalized `sc/sċ`, while the exact live proto string and trace staging are current repository representations [Germanic/docs/DEV_NOTES.md:6368-6440; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1402-1422].
