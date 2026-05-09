---
row_id: 2014
concept: fish
counterpart: fisċ
proto: *fískaz
protoform: *fískaz
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
  - Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md
  - Germanic/docs/analysis/notable_findings.md
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2014 fish / fisċ

## Current row state

- The live OE row is already a regular exact match: `ID 2014`, `CONCEPT fish`, `COUNTERPART fisċ`, `PROTO *fískaz`, `PROTOFORM *fískaz`, `DERIVATION_CLASS regular` [Germanic/data/germanic-aligned-final.tsv:326-326].
- `PROTO` and `PROTOFORM` are identical in the live TSV, so this row is **not** currently using a substitute paradigm cell, a repaired input, or an analogical workaround. DEV_NOTES usually discusses the same item as `*fiskaz` or `*fiskăz`; for this slice those should be treated as notation variants inside DEV_NOTES discussion, not as evidence that row 2014 has a different live derivational input than `*fískaz` [Germanic/data/germanic-aligned-final.tsv:326-326; Germanic/docs/DEV_NOTES.md:5365-5378,5410-5424,5539-5545].
- The current derivation trace is exact and uncomplicated: `PROTO: *fískaz`, `EXPECTED: fisċ`, `OUTPUTS: fisċ`, then `PGmc Final Z Deletion: *físka`, `PWGmc Final Bare A Loss: *físk`, `OE Sk Palatalization: *fíʃ`, `Old English Orthography: *físċ`, `Outcome: fisċ` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1300-1320]. That trace matters because it separates the reconstructed pipeline stages from the attested/normalized OE target: `*físċ` is a project-side orthographic stage, while `fisċ` is the row's chosen OE counterpart.
- No row-specific exception flag survives in `oe_known_problems.tsv`; the file currently lists other exception buckets only, and nothing there is keyed to `2014`, `fish`, `fisċ`, or `*fískaz` [Germanic/data/oe_known_problems.tsv:1-8].
- `coverage_audit.md` classifies the row as `regular`, with `NOTE? no`, no linked packet, no research memo, and `Requirement basis = none`; `report_manifest.tsv` likewise has no `2014` entry in its current pilot list [Germanic/docs/lexeme_reports/coverage_audit.md:238-238; Germanic/docs/lexeme_reports/report_manifest.tsv:1-13]. This slice therefore has to act as a replacement working note for a row that is presently stable but only indirectly documented.
- The surviving DEV_NOTES support is mostly **shared i-lowering control material**, not a dedicated fish dossier. The most directly row-relevant philological quotation preserved in DEV_NOTES is Lloyd's cross-dialect retention list, which includes `"OE fisc, OHG, OS fisk, ON fiskr"`; the most directly row-relevant OE-sound-change quotation preserved there is Campbell's statement that `"sc was palatalized and assibilated after any front vowel ... fisc fish"` [Germanic/docs/DEV_NOTES.md:5651-5660,6388-6395].

## Development-note summary

No row-specific DEV_NOTES section survives for row 2014 in the way that it survives for `fire`, `tap`, or `wether`. What does survive is still substantial enough to support a conservative replacement note. In the shared March-April 2026 work on NWGmc `*i > *e`, `fish` repeatedly functions as the control case showing that OE `fisċ` must **retain** inherited `*i` rather than lower it to `e` before a following non-high vowel [Germanic/docs/DEV_NOTES.md:5363-5378,5408-5424,5738-5786].

The core project claim is specific but should be phrased cautiously. DEV_NOTES argues that unconditional i-lowering is too broad because `fish` patterns with other retained-`i` forms whose post-tonic consonant material includes a velar or labial; in the fish row the relevant blocker is the velar `*k` inside `*-sk-` [Germanic/docs/DEV_NOTES.md:5365-5378,5410-5424]. The strongest direct DEV_NOTES wording is: `"every form that retained *i has a velar or labial consonant in the coda"`; the fish line in that same table is `| fish | *fiskaz | -sk- | coronal + dorsal | blocking | fisċ ✓ |` [Germanic/docs/DEV_NOTES.md:5376-5378,5365-5369]. That is current project analysis, but it is still shared-policy material rather than a fish-only scholarly consensus statement.

The literature-facing support preserved in DEV_NOTES is narrower than the project inference. Lloyd's quotation `"OE fisc, OHG, OS fisk, ON fiskr"` supports the comparative fact that this lexeme retains `i` broadly across Germanic and therefore belongs in the retained-`i` set [Germanic/docs/DEV_NOTES.md:5653-5656]. It does **not** by itself prove that Old English had an explicitly recognized coda-velar blocking law. DEV_NOTES itself makes that broader methodological caution elsewhere in the same i-lowering discussion: some of the blocking analysis is the project's explanatory synthesis rather than a verbatim inherited rule from the handbooks [Germanic/docs/DEV_NOTES.md:5662-5687].

A second distinction that must be preserved is retained vowel quality versus later OE palatalization/orthography. The fish row is not difficult because DEV_NOTES doubts the OE target `fisċ`; the row is stable. The point is that the stressed vowel remains `i`, while later OE `sk` palatalization and spelling conventions yield `fisċ`. DEV_NOTES preserves Campbell's wording exactly: `"sc was palatalized and assibilated after any front vowel, original or due to umlaut, e.g. æsc ash, disc dish, fisc fish ..."` [Germanic/docs/DEV_NOTES.md:6388-6392]. So the current row state is best summarized as: inherited `*i` is retained under the shared blocking analysis, and the expected OE consonant/orthographic development then gives `fisċ` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1307-1320; Germanic/docs/DEV_NOTES.md:6388-6395].

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-5651-5660

- Source heading: `Lloyd (1966): OE hlid retains *i, but why?`
- Source line or section hint: `lines 5651-5660`
- Fragment type: `bibliography_or_source_audit_for_lexeme`
- Status: `current`
- Issue tags: `retained_i`; `comparative_attestation`; `shared_i_lowering_literature`
- Recommended next use: `cite when a later report needs literature-facing support for fish as a retained-*i lexeme, but pair with a caution that the blocking mechanism is project analysis`
- Shared with row IDs: `2100`

This is the cleanest literature-bearing fragment that still names the fish row directly. DEV_NOTES quotes Lloyd's retained-`i` list as `"OE fisc, OHG, OS fisk, ON fiskr; OE, OS witan, ON vita, OHG wizzan; ON hliþó, OE hlid (Eng. lid), OHG (h)lit"` and then uses that quotation to argue that these lexemes belong to the cross-dialect retention set [Germanic/docs/DEV_NOTES.md:5653-5656]. For row 2014, the value of the fragment is straightforward: it preserves a directly quotable scholarly source showing that `fisc/fisċ` is not an isolated OE oddity but part of a wider Germanic retention pattern.

The limitation is just as important. In DEV_NOTES this quotation appears inside a wider discussion whose main target is `lid`, not `fish`, and the surrounding prose says Lloyd does **not** explain the retained vowel by an onset- or coda-velar OE sound law; his point is broader skepticism about a regular i-lowering change [Germanic/docs/DEV_NOTES.md:5658-5660]. So this fragment should be used for attestation and comparative grouping, not overstated as proof that scholarship explicitly endorses the repo's fish-specific blocking account.

### DEV_NOTES:line-5363-5424

- Source heading: `Applying the Theory to Our Data` plus `Experimental Implementation and Results`
- Source line or section hint: `lines 5363-5424`
- Fragment type: `shared_rule_context_for_lexeme`
- Status: `current`
- Issue tags: `i_lowering`; `coda_velar_block`; `regression_diagnostic`; `shared_control_case`
- Recommended next use: `primary DEV_NOTES citation when explaining why unconditional i-lowering is rejected for fish`
- Shared with row IDs: `2014`; `2099`; `2107`; `2108`; `2137`; `2189`; `2288`

This is the main surviving DEV_NOTES substance for the row, even though it is shared material rather than a fish-only dossier. First, DEV_NOTES lays out the diagnostic table in which `fish` appears as `| fish | *fiskaz | -sk- | coronal + dorsal | blocking | fisċ ✓ |`; it then generalizes the pattern with the sentence `"every form that retained *i has a velar or labial consonant in the coda, while the two forms that show lowering (nest, wer) have purely coronal clusters"` [Germanic/docs/DEV_NOTES.md:5365-5378]. That is the clearest current statement of why row 2014 is treated as a retained-`i` control item.

The same DEV_NOTES block also preserves the crucial negative evidence. When an unconditional `NWGmcILowering` rule was tried, the regression table explicitly recorded `| fish | *fiskăz | fesċ | fisċ | velar *k |`, and DEV_NOTES immediately comments that `"Every regression involves a velar or labial consonant — exactly as predicted by Howell & Salmons"` [Germanic/docs/DEV_NOTES.md:5410-5424]. For this slice that pre-fix `fesċ` form is diagnostic history, not current row state, but it is still valuable because it shows exactly what the project was trying to prevent: without the blocking condition, the row would be forced into a false lowered-vowel analysis.

### DEV_NOTES:line-5738-5786

- Source heading: `Test cases` plus `Implementation successful (2026-03-09)` / `Results`
- Source line or section hint: `lines 5738-5786`
- Fragment type: `implementation_result_for_lexeme`
- Status: `current`
- Issue tags: `test_case`; `resolved_output`; `shared_blocking_rule`; `no_regression`
- Recommended next use: `cite when a later report needs the repo's current project-state proof that fish remains stable under the adopted i-lowering rule`
- Shared with row IDs: `2034`; `2099`; `2100`; `2108`; `2137`; `2283`

This fragment is the current project-side resolution note. In the test-case table DEV_NOTES lists `fish` as `Velar before? No`, `Velar/labial after? Yes (*k)`, `Predicted Block`, `Actual OE fisċ ✓`; in the results table it then gives `| *fiskăz | fisċ | fisċ | fisċ | ✓ No change (velar *k in coda) |` [Germanic/docs/DEV_NOTES.md:5740-5786]. That is stronger than the earlier exploratory table because it records the post-implementation state after the revised rule was accepted.

For row 2014, this fragment is useful precisely because it is modest. It does not claim that fish needed a special exception entry, a different `PROTOFORM`, or a TSV workaround. Instead it shows that once the shared i-lowering rule was narrowed, fish simply stayed correct. That matches the live row, the lack of an `oe_known_problems.tsv` entry, and the exact debug trace already published for the row [Germanic/data/oe_known_problems.tsv:1-8; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1300-1320].

### DEV_NOTES:line-6388-6395

- Source heading: `Campbell (1959) §442 (Palatalization of sc)`
- Source line or section hint: `lines 6388-6395`
- Fragment type: `shared_source_quote_for_surface_form`
- Status: `current`
- Issue tags: `palatalization`; `orthography`; `surface_fisċ`; `handbook_quote`
- Recommended next use: `cite when a later note must explain why retained *i still surfaces as OE fisċ rather than plain fisc in project orthography`
- Shared with row IDs: `2020`

This fragment is not about i-lowering at all, but it is still part of the minimum row file because it preserves the best DEV_NOTES quotation for the final OE shape. DEV_NOTES quotes Campbell: `"sc was palatalized and assibilated after any front vowel, original or due to umlaut, e.g. æsc ash, disc dish, fisc fish, risc rush, the suffix -isc, and after an umlauted vowel flǣsċ flesh"` [Germanic/docs/DEV_NOTES.md:6390-6392]. For row 2014, the relevant point is the inclusion of `fisc fish` itself among Campbell's examples.

That quotation keeps two layers distinct. The fish row's real DEV_NOTES question is whether `*i` lowers; Campbell's quotation is about what happens **after a front vowel is already there**, namely palatalization/assibilation of `sc`. Using this fragment alongside the trace prevents a later writer from collapsing those stages into one. The vowel-retention argument comes from the i-lowering dossier; the final `fisċ` surface shape is then compatible with Campbell's palatalization statement and with the row's published trace [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1311-1320].

## Superseded or diagnostic material

The most important diagnostic-only fish material is the abandoned regression `fesċ`. DEV_NOTES preserves it because it was the visible failure produced by an over-broad i-lowering rule: `| fish | *fiskăz | fesċ | fisċ | velar *k |` [Germanic/docs/DEV_NOTES.md:5410-5413]. That form should never be cited as if it were a live row output. Its value is historical and methodological only: it shows why the project stopped treating fish as a possible lowered-vowel case and instead used it as evidence that the rule needed consonant conditioning.

A second misleading survivor is the Modern English sandbox material. Early in DEV_NOTES, `fish` appears in the non-OE pronunciation sweeps as part of the `"fish/give/six/will"` KIT cluster [Germanic/docs/DEV_NOTES.md:2308-2322]. That material belongs to the Modern English sandbox, not to the OE derivational cascade. It should therefore be ignored for row 2014 except as a warning that raw keyword hits on `fish` in DEV_NOTES can pull in irrelevant later-English phonology.

There is also no surviving row-specific fish packet, research memo, or manifest entry to supersede. That absence matters. The current repository state treats `fish` as a regular row whose note burden comes from shared i-lowering diagnostics, not from an unresolved lexeme-specific controversy [Germanic/docs/lexeme_reports/coverage_audit.md:238-238; Germanic/docs/lexeme_reports/report_manifest.tsv:1-13].

## Open questions for later work

- If a later full report is wanted, decide whether it should normalize the notation explicitly as `project *fískaz = DEV_NOTES *fiskaz/*fiskăz = Lloyd OE fisc comparative set`; the current slice preserves the distinction, but DEV_NOTES never turns it into a row-specific policy statement [Germanic/data/germanic-aligned-final.tsv:326-326; Germanic/docs/DEV_NOTES.md:5365-5378,5653-5656].
- If later writers want stronger literature support for the blocking account, they should revisit the shared i-lowering bibliography rather than overstating Lloyd. The current slice can securely say that Lloyd preserves `fisc` in the retained-`i` set, but the stricter claim that coda velars block OE i-lowering remains repo-level analysis synthesized from the wider discussion [Germanic/docs/DEV_NOTES.md:5653-5660,5662-5687].
- If the row is ever indexed more centrally, keep the vowel issue and the consonant/orthography issue separate: retained `*i` is one question, while `sk > sċ/sc` after a front vowel is another. The present row trace and the Campbell quotation fit together cleanly only if those stages remain distinct [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1311-1320; Germanic/docs/DEV_NOTES.md:6388-6395].
