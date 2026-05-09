---
row_id: 1963
concept: bow
counterpart: boga
proto: *búgô
protoform: *búgô
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files: Germanic/docs/dossiers/bugan-scufan-paradigm-cell-review.md
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 1963 bow / boga

## Current row state

- The live Old English row reads `CONCEPT = bow`, `COUNTERPART = boga`, `PROTO = *búgô`, `PROTOFORM = *búgô`, and `DERIVATION_CLASS = regular`; the row-level `NOTE` field is blank, and the only source text in the TSV is duplicated Wiktionary etymology metadata [Germanic/data/germanic-aligned-final.tsv:121-121].
- `coverage_audit.md` still marks row 1963 as uncovered: no packet, no research memo, no linked dossier/analysis file, overall status `none` [Germanic/docs/lexeme_reports/coverage_audit.md:207-207]. This slice therefore has to do the replacement-note work without any row-local packet or memo infrastructure.
- `oe_known_problems.tsv` does not list `*búgô` among the currently tracked OE exception or wont-fix items; the file's active rows cover other lexemes such as `*búkkaz`, `*fúglaz`, `*wúlfaz`, `*fūri`, and `*táppô` instead [Germanic/data/oe_known_problems.tsv:1-8]. For row 1963, that absence is materially relevant because DEV_NOTES explicitly treats `buga/boga` as an ordinary FST bug rather than a documented lexical exception.
- A shared dossier exists only as cross-row background, not as a dedicated 1963 report. In the `būgan / sċūfan` paradigm-cell review, row 1963 is mentioned merely to distinguish the noun `*búgô / boga` from the co-radical verbal rows, and the bibliography notes Bammesberger 1990 as relevant only for that noun row [Germanic/docs/dossiers/bugan-scufan-paradigm-cell-review.md:402-404; Germanic/docs/dossiers/bugan-scufan-paradigm-cell-review.md:576-578].

## Development-note summary

DEV_NOTES support for row 1963 is present but comparatively thin, and the slice should say so plainly. No surviving long-form DEV_NOTES subsection is organized around simplex `*búgô -> boga` alone. The most direct lexeme-specific evidence is an early OE triage note on `u`-lowering, plus a later compound discussion whose second element is the same noun stem [Germanic/docs/DEV_NOTES.md:2967-2973,16807-16906].

The clearest explicit claim comes from the `u → o before back vowel` troubleshooting note. There DEV_NOTES names this lexeme directly among the affected forms: `*bugô → buga (expected boga)` [Germanic/docs/DEV_NOTES.md:2967-2969]. The note then states the underlying rule claim in unmistakable terms: `NWGmcULowering should lower *u → *o before non-high vowels in a following syllable`, and for this pair `the expected form IS the lowered one (boga)`, so `u`-retention is `a FST bug, not a documented exception` [Germanic/docs/DEV_NOTES.md:2971-2973]. For row 1963, this is the single most important surviving DEV_NOTES judgment. It means the live `boga` target is not being carried as an analogical workaround, a dubious dictionary preference, or an exception bucket item; DEV_NOTES treats it as the regular expected outcome of `*búgô` once the lowering bug is not interfering.

A second materially relevant cluster is the compound note on `*regnă-bugô → reġnboga`. That section is not about row 1963 as a simplex noun, but it bears directly on the same lexical base and preserves useful source-backed claims about how `boga` behaves in OE. DEV_NOTES identifies the wrong output `reġnafoga`, insists that the correct target is `reġnboga`, and diagnoses two concrete errors: the linking vowel should syncopate, and `b` should remain a stop rather than leniting to `f` [Germanic/docs/DEV_NOTES.md:16814-16824]. The note then quotes Ringe & Taylor on general syncope of unstressed nonhigh vowels and adds the lexeme-specific comparator `elnboga 'elbow'`, explicitly glossed as `eln + boga`, where `b` likewise remains a stop [Germanic/docs/DEV_NOTES.md:16825-16831,16857-16864]. Even though this is compound evidence, it still matters for the simplex row: DEV_NOTES is treating `boga` as the ordinary OE noun shape inside compounds and as a stable enough lexical element to anchor diagnostics about stop retention.

The implementation/result lines from the same compound section are worth preserving because they show the project accepted `reġnboga` as the repaired outcome after adding the linking-vowel syncope rule, not as a speculative target [Germanic/docs/DEV_NOTES.md:16887-16906]. That does not prove simplex `boga` by itself, but it does show that later DEV_NOTES continued to treat the noun stem as `boga`, not `buga`, and that the pipeline work around this lexeme was aimed at recovering `-boga` outputs.

The only other direct lexical support inside DEV_NOTES is not derivational but notational. In the project accent/quantity table, `*búgô` appears as an example of a stressed long root vowel [Germanic/docs/DEV_NOTES.md:20572-20575]. This is thin evidence, but still useful for replacement-note purposes: it confirms that the live row's spelling with acute `ú` and circumflex `ô` matches the notation system DEV_NOTES itself was standardizing, rather than being an unsourced later respelling.

Taken together, the conservative working conclusion is straightforward. DEV_NOTES does support row 1963, but mostly through one explicit `u`-lowering bug note and one shared compound section, not through a dedicated noun dossier. The safest replacement note therefore keeps `PROTO = PROTOFORM = *búgô`, keeps `COUNTERPART = boga`, states openly that the surviving support is somewhat sparse, and preserves the central DEV_NOTES claim that `buga` was the bug while `boga` was the expected regular target [Germanic/docs/DEV_NOTES.md:2967-2973].

## Relevant DEV_NOTES fragments

### Germanic/docs/DEV_NOTES.md:2967-2973

- Source heading: `A. u-lowering (u → o before back vowel)`
- Fragment type: `shared_problem_definition_with_row_specific_example`
- Status: `current`
- Issue tags: `u_lowering`; `expected_lowered_form`; `regular_outcome`; `not_an_exception`
- Recommended next use: `primary_anchor_for_final_report`

This is the most important fragment for the row because it names the lexeme directly and states both the bug and the intended outcome. DEV_NOTES lists `*bugô → buga (expected boga)` among the affected items, then explains: `NWGmcULowering should lower *u → *o before non-high vowels in a following syllable` and concludes that `buga/boga ... [is] a FST bug, not a documented exception` [Germanic/docs/DEV_NOTES.md:2969-2973]. For row 1963, that is the clearest surviving statement that `boga` is the regular expected OE reflex.

### Germanic/docs/DEV_NOTES.md:16807-16864

- Source heading: `Compound Words: *regnă-bugô → reġnboga 'rainbow' (2026-04-11)`
- Fragment type: `copied_shared_lexeme_fragment`
- Status: `current`
- Issue tags: `compound_evidence`; `stop_retention`; `reġnboga`; `source_quote`
- Recommended next use: `cite_as_supporting_background`

This shared section is materially relevant even though it concerns the compound `reġnboga` rather than the simplex noun row. DEV_NOTES sets the target as `reġnboga`, rejects `reġnafoga`, and says the failure involves both surviving linking vowel and incorrect lenition: `*b → f` is wrong because the target has `b` as a stop [Germanic/docs/DEV_NOTES.md:16814-16824]. It then preserves a useful source quotation from Ringe & Taylor: `"Short vowels in unstressed word-internal open syllables were lost under particular conditions... Nonhigh *æ ... and *e ... were usually lost"`, followed by the explicit lexeme comparator `elnboga 'elbow' (= eln + boga) where b remains a stop` [Germanic/docs/DEV_NOTES.md:16825-16831,16857-16864]. For row 1963, this fragment is best used as supporting evidence that DEV_NOTES continued to treat `boga` as the normal noun element in OE compounds.

### Germanic/docs/DEV_NOTES.md:16887-16906

- Source heading: `Compound Words: *regnă-bugô → reġnboga 'rainbow' (2026-04-11)` / `Implementation` and `Result`
- Fragment type: `verification_snapshot`
- Status: `current`
- Issue tags: `implemented_fix`; `compound_linking_syncope`; `recovered_boga_output`
- Recommended next use: `use_to_show_later_dev_notes_state`

The implementation note matters because it shows what later DEV_NOTES considered the repaired outcome after grammar changes. DEV_NOTES records the targeted rule `OECompoundLinkingSyncope` and then the result line `*regnă-bugô → reġnboga ✓ (was reġnafoga)` [Germanic/docs/DEV_NOTES.md:16889-16906]. For row 1963, this is not simplex proof, but it is good evidence that the project's later accepted OE noun stem was still `-boga`, not `-buga`.

### Germanic/docs/DEV_NOTES.md:20572-20575

- Source heading: `Accent/quantity notation table`
- Fragment type: `notation_support_for_lexeme`
- Status: `current`
- Issue tags: `protoform_notation`; `long_vowel_marking`; `orthographic_consistency`
- Recommended next use: `cite_if_protoform_spelling_needs_justification`

This is a thin but legitimate row-relevant fragment. DEV_NOTES uses `*búgô` as one of its examples for the category `Stressed long root vowel` [Germanic/docs/DEV_NOTES.md:20572-20575]. The fragment does not discuss the OE reflex, but it does support the exact live protoform spelling carried by the row and helps show that the notation itself is repo-standard rather than ad hoc.

## Superseded or diagnostic material

- The bad output `buga` should be preserved as diagnostic history only. DEV_NOTES does not present it as an attested rival form or as a candidate retargeting; it presents it specifically as the erroneous output created when `NWGmcULowering` failed to apply [Germanic/docs/DEV_NOTES.md:2969-2973].
- Likewise, `reġnafoga` in the compound note is diagnostic only. Its value is procedural: it shows how surviving linking vowel plus over-lenition can corrupt the `-boga` element in compounds, not that row 1963 itself is philologically doubtful [Germanic/docs/DEV_NOTES.md:16814-16824,16889-16906].
- No surviving DEV_NOTES passage was located that argues for a current alternative OE target for row 1963, labels the row exceptional, or proposes changing `PROTOFORM` away from `*búgô`. The thinness of the record should remain explicit, but the surviving support all points in the same direction.

## Open questions for later work

- If row 1963 ever gets a full packet or final report, add direct lexicographic citations for simplex OE `boga`; the present DEV_NOTES support is enough for a conservative working slice, but much of it is still indirect compound evidence rather than a row-local noun dossier.
- Decide whether the shared `reġnboga` / `elnboga` material is strong enough to make the slice index-worthy, or whether row 1963 should remain effectively no-index until it has dedicated lexical-source coverage.
- If future cleanup revisits the bow cogset, keep the three lexemes sharply separated in prose: row 1961 `*báugijaną → bīeġan` (weak causative), row 1962 `*báug → bēag` under `*béuganą` (strong-verb paradigm cell), and row 1963 `*búgô → boga` (noun).
