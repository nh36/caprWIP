---
row_id: 2112
concept: lock
counterpart: locc
proto: *lúkkaz
protoform: *lúkkaz
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
  - Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2112 lock / locc

## Current row state

- The live OE row is `2112 | lock | locc | *lúkkaz | *lúkkaz | regular`. `PROTO` and `PROTOFORM` coincide as `*lúkkaz`, while `COUNTERPART` is the attested/target OE form `locc`; the row carries only duplicated provenance text (`template:inh`) and no row-local explanatory note [Germanic/data/germanic-aligned-final.tsv:704-704].
- The adjacent OE row `2111 | lock | loc | *lúką | *lúką | regular` remains a separate lexeme/pathway. For this slice, that adjacency matters because the dataset is already distinguishing `*lúką -> loc` from `*lúkkaz -> locc`; the `-cc-` row should not be collapsed into the nasal-stem/zero-suffix row beside it [Germanic/data/germanic-aligned-final.tsv:702-704].
- `coverage_audit.md` classifies row `2112` as a regular row with no note and no report requirement: `| 2112 | lock | locc | regular | no | - | - | - | none |`. This means the present slice is replacement documentation for a previously uncovered row, not a rewrite of an existing packet/report chain [Germanic/docs/lexeme_reports/coverage_audit.md:299-300].
- `oe_known_problems.tsv` currently tracks only the genuine OE trouble spots such as `*búkkaz`, `*fúglaz`, `*wúlfaz`, `*wúllō`, `*rústō`, `*fūri`, and `*táppô`; `*lúkkaz` is not in that problem inventory, which is positive evidence that the row is not presently treated as an exception or mismatch case [Germanic/data/oe_known_problems.tsv:1-8].
- The published derivation trace is an exact match: `PROTO: *lúkkaz`, `EXPECTED: locc`, `OUTPUTS: locc`, with the regular path `*lúkkaz > *lókkaz > *lókka > *lókk > locc` through Northwest Germanic `u`-lowering, final `-z` deletion, final bare `-a` loss, and OE orthographic rendering of geminate `kk` as `cc` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3004-3023].

## Development-note summary

No row-specific DEV_NOTES block survives for `lock / locc / *lúkkaz`. Direct project support has to be reconstructed conservatively from the live row and from shared DEV_NOTES material on Northwest Germanic `u`-lowering rather than from a dedicated lexeme memo. That absence should be stated plainly: there is no honest `DEV_NOTES` passage that says, in row-local terms, “`*lúkkaz -> locc` requires special handling.”

The best surviving shared material is the `NWGmc u-lowering Exceptions Near Labials` section. Its opening statement is broad and current: “Our NWGmcULowering rule lowers stressed *u → *o before non-high vowels in a following syllable ... This is correct and well-established” [Germanic/docs/DEV_NOTES.md:70-70]. Row `2112` fits that regular description neatly: stressed initial `*u` in `*lúkkaz` lowers to `*o`, and the trace confirms exactly that development [Germanic/docs/DEV_NOTES.md:70-70; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3011-3023].

The same DEV_NOTES section is also useful because it marks the exception boundary. The listed lexemes with retained `u` are `*fullăz`, `*wulfăz`, `*fuglăz`, `*bukkăz`, `*wullō`, `*lubō`, and `*rustō` [Germanic/docs/DEV_NOTES.md:72-78]. `*lúkkaz` is not among them. That matters especially because `*bukkăz -> bucc` is superficially close to `*lúkkaz -> locc`: both involve a geminate velar stop and OE `<cc>`, but DEV_NOTES explicitly treats `bucc` as an exception with unresolved `u`-retention, whereas `locc` stays on the regular lowering path [Germanic/docs/DEV_NOTES.md:72-78,136-154].

The stress-restriction note is the other shared fragment that still bears on this row. DEV_NOTES records Schuhmacher’s clarification that “Such lowering affects **only stressed vowels**,” and the implementation fix restricts `NWGmcULowering` to first-syllable `*u` [Germanic/docs/DEV_NOTES.md:150-150,171-194]. For `*lúkkaz`, that restriction does not create a complication; it simply confirms why the initial vowel is eligible for lowering. So the row’s working-note status is conservative and stable: regular row, regular lowering, no current mismatch, no surviving row-specific DEV_NOTES block.

## Relevant DEV_NOTES fragments

### Fragment 1

- Source heading: `NWGmc u-lowering Exceptions Near Labials`
- Source line hint: `Germanic/docs/DEV_NOTES.md:63-86`
- Fragment type: `shared_background_rule_with_exception_boundary`
- Status: `current; shared-background-only for row 2112`
- Issue tags: `nwgmc_u_lowering`; `regular_lowering`; `exception_boundary`; `contrast_with_buck`
- Recommended next use: `use to justify the regular *u > *o step and to keep row 2112 out of the u-retention exception bucket`
- Shared-with rows if relevant: `1973 buck / bucc; 2030 fowl / fugol; 2162 rust / rust; 2298 wolf / wulf; 2300 wool / wull; 2111 lock / loc`

This fragment supplies the main surviving phonological frame. DEV_NOTES says: “Our NWGmcULowering rule lowers stressed *u → *o before non-high vowels in a following syllable ... This is correct and well-established” [Germanic/docs/DEV_NOTES.md:70-70]. It then immediately distinguishes a narrow exception set where “several lexemes retain *u where *o is predicted,” including `*bukkăz -> bucc` [Germanic/docs/DEV_NOTES.md:70-78]. For row `2112`, the substance is mostly boundary-setting rather than bespoke analysis: `*lúkkaz` belongs on the regular side of the rule, not in the retained-`u` bucket.

The embedded scholarly quotation is still relevant because it explains why the exception list must stay narrow. R/T are quoted as concluding of the retained-`u` items: “We do not really know why *u failed to lower in these forms” [Germanic/docs/DEV_NOTES.md:86-86]. That unresolved statement is not row-specific support for `locc`; it is contrastive evidence that `locc` should not be overinterpreted as another mysterious `u`-preserving lexeme merely because `bucc` exists nearby in the lexicon.

### Fragment 2

- Source heading: `NWGmc u-lowering Exceptions Near Labials`
- Source line hint: `Germanic/docs/DEV_NOTES.md:134-154`
- Fragment type: `decision_note_plus_exception_specific_diagnostic`
- Status: `current decision; row-relevant only as contrast`
- Issue tags: `implementation_policy`; `exception_handling`; `buck_specific_diagnostic`; `not_row_specific`
- Recommended next use: `cite when explaining why no exception annotation is needed for row 2112 and why buck-style discussion should not be imported here`
- Shared-with rows if relevant: `1973 buck / bucc and other retained-u exception rows`

The implementation decision is explicit: “Accept the mismatches. The FST correctly models the regular NWGmc u-lowering as a phonological rule. The u-preserving forms are genuine lexical exceptions for which no phonological conditioning has been established” [Germanic/docs/DEV_NOTES.md:134-142]. For row `2112`, the usable substance is the first half of that decision: the rule itself is already considered correct. Since the current trace yields `locc` exactly, this row does not need the exception-side annotation policy.

The same block preserves the only lexeme-specific quotation that could tempt misapplication here: on `bucc`, Schuhmacher says, “There may be additional complications such as the possibility that *bucc originally may have been a u-stem word, in which case the vowel of Old English *bucc would be what we expect” [Germanic/docs/DEV_NOTES.md:152-154]. That is diagnostic material for `*búkkaz`, not support for `*lúkkaz`. Its main value in this slice is defensive: it shows that any special pleading about geminate velars and OE `<cc>` belongs to the `bucc` problem file, not to the already regular `locc` row.

### Fragment 3

- Source heading: `Stress restriction fix (2026-03-20)`
- Source line hint: `Germanic/docs/DEV_NOTES.md:171-212`
- Fragment type: `shared_rule_scope_and_conditioning`
- Status: `current; shared-background-only`
- Issue tags: `stress_condition`; `rule_scope`; `initial_syllable`; `regular_application`
- Recommended next use: `use if later work questions whether the lowering in *lúkkaz is licensed by the current implementation`
- Shared-with rows if relevant: `all rows depending on NWGmcULowering, especially 2111 lock / loc and the retained-u comparison rows`

This fragment records the implementation narrowing prompted by Schuhmacher: “Such lowering affects **only stressed vowels**,” and the rule was revised so that only first-syllable `*u` lowers [Germanic/docs/DEV_NOTES.md:173-194]. DEV_NOTES illustrates the repaired logic with `*wulfaz`, where the initial `*u` is matched and lowered before a following consonant cluster plus non-high vowel [Germanic/docs/DEV_NOTES.md:205-212]. Row `2112` is not quoted here, but it falls under the same conditioning profile: initial stressed `*u`, following `kk + a`, then ordinary later deletions. The fragment is therefore shared-background-only, but it is the clearest surviving DEV_NOTES support for why `*lúkkaz > *lókkaz` is licensed under the current implementation.

## Superseded or diagnostic material

- No row-specific `lock / locc` DEV_NOTES memo survives. The main evidential limitation here is missing row-local prose, not a superseded row-local theory.
- The `bucc` discussion inside DEV_NOTES is diagnostic-only for row `2112`. It is valuable because it marks what an actual retained-`u` exception looks like in project terms, but it should not be reused as if `locc` needed the same kind of rescue argument [Germanic/docs/DEV_NOTES.md:72-78,152-154].
- `coverage_audit.md` is workflow evidence only. Its `none` status for row `2112` explains why this slice had to be written, but it is not phonological authority [Germanic/docs/lexeme_reports/coverage_audit.md:299-300].
- The published derivation trace is strong current-state evidence, but it is still diagnostic infrastructure output rather than DEV_NOTES prose. It shows that the implemented path is stable; it does not create a lost row-specific note retroactively [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3004-3023].

## Open questions for later work

- If a later packet or memo is created, the most useful addition would be an explicit row-local statement that `*lúkkaz -> locc` is simply a regular NWGmc-lowering case and should be kept separate from `*búkkaz -> bucc` exception logic.
- If the orthographic layer is ever documented more granularly, it may be worth recording explicitly that the trace’s pre-orthographic `*lókk` surfaces as OE `locc`; the current trace shows the result but does not spell out that final orthographic mapping in prose [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3011-3023].
- If this row is ever considered for index-style attachment, the honest line anchors currently available are shared-rule anchors (`63-86`, `134-154`, `171-212`), not a genuine `lock / locc` block. Any future indexing should preserve that distinction.
