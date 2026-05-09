---
row_id: 1964
concept: bower
counterpart: būr
proto: *būrą
protoform: *būrą
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files: []
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 1964 bower / būr

## Current row state

- CONCEPT: `bower`
- COUNTERPART: `būr`
- PROTO: `*būrą`
- PROTOFORM: `*būrą`
- DERIVATION_CLASS: `regular`
- Live TSV row: row 1964 currently keeps the straightforward inherited pairing `bower / būr / *būrą`, with no row-local explanatory note beyond inherited-etymology placeholders in the source field [Germanic/data/germanic-aligned-final.tsv:127-127].
- Existing report infrastructure: the coverage audit still lists row 1964 as `regular`, with no packet, no memo, no attached fragment, and overall status `none`, so this slice is replacing absent row-local notes rather than consolidating an existing dossier [Germanic/docs/lexeme_reports/coverage_audit.md:208-208].
- Current implementation trace: the published derivation snapshot already reaches the target exactly, with the whole OE-side work reduced to `OE Heavy Syllable Nasal Apocope: *būr`, yielding surface `būr` from proto input `*būrą` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:490-509].

## Development-note summary

DEV_NOTES support for row 1964 is thin and shared rather than lexeme-specific. No dedicated `bower / būr / *būrą` discussion survives in the live note file, so the replacement slice should not pretend that there was a row-local controversy, protoform swap, or special repair history. The materially relevant DEV_NOTES content is instead the project's shared discussion of **heavy-syllable nasal apocope**: deletion of final proto `*-ą` after heavy stems, treated as an empirically discovered rule that substantially improved OE outputs [Germanic/docs/DEV_NOTES.md:1591-1645].

That archived DEV_NOTES section preserves the substance that matters here. It states that the rule was introduced as `deleting proto *-ą after heavy syllables`, that dataset review found spurious final vowels were concentrated in heavy stems, and that the model therefore extended heavy/light apocope logic beyond the better-documented loss of final short `*i` and `*u` [Germanic/docs/DEV_NOTES.md:1595-1624]. The note is explicit about the evidential balance: Ringe-Taylor and Hogg are quoted for heavy-syllable conditioning on final high vowels, but DEV_NOTES also says that “Neither source explicitly extends this pattern to *-ą” and frames the `*-ą` extension as a learned/model-driven pattern rather than a directly cited handbook rule [Germanic/docs/DEV_NOTES.md:1604-1615].

For row 1964, that shared discussion is enough to explain why the live derivation is regular. `*būrą` is precisely the kind of heavy stem the rule targets: long `ū` plus final nasalized vowel. The published trace shows no need for analogical repair, alternate paradigm-cell input, or exceptional sound law; the only operative OE change is exactly the DEV_NOTES rule deleting final `*-ą`, after which the expected surface is simply `būr` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:499-509; Germanic/docs/DEV_NOTES.md:1617-1623].

A later DEV_NOTES passage shows that this was not just a one-off experiment that vanished from project reasoning. In a separate argument about another lexeme, DEV_NOTES still appeals to the same mechanism in ordinary analytic prose: “Heavy-syllable nasal apocope handles the `*ǭ` final vowel” [Germanic/docs/DEV_NOTES.md:25724-25731]. For row 1964, that matters because it confirms the rule remained part of the working explanatory toolkit even after the original discovery note was archived.

The conservative conclusion is therefore straightforward. Row 1964 is currently well supported as a **regular** `*būrą > būr` case, but the support is mostly rule-level rather than lexeme-level. This slice should preserve that asymmetry explicitly: there is enough DEV_NOTES substance to justify the live row, yet not enough row-specific material to turn `bower / būr` into a packet-grade exception narrative [Germanic/docs/lexeme_reports/coverage_audit.md:208-208; Germanic/docs/DEV_NOTES.md:1591-1645].

## Relevant DEV_NOTES fragments

### [Germanic/docs/DEV_NOTES.md:1591-1645]

- Source heading: `Archived: Heavy Syllable Nasal Apocope (2026-02-06) — EMPIRICAL DISCOVERY`
- Fragment type: `shared_rule_discussion`
- Status: `archived_but_still_materially_relevant`
- Issue tags: `final_-ą_loss`; `heavy_stem_conditioning`; `shared_regular_rule`

This is the main DEV_NOTES material that bears on row 1964. The note says: “Implemented experimental rule deleting proto *-ą after heavy syllables,” then explains that words with spurious final vowels were disproportionately heavy stems and that adding the rule fixed 41 cases [Germanic/docs/DEV_NOTES.md:1595-1602]. It also preserves the important caution that the handbooks do **not** directly formulate the exact rule: “Neither source explicitly extends this pattern to *-ą” [Germanic/docs/DEV_NOTES.md:1604-1608].

For this row, the fragment should be carried forward almost verbatim in substance. `*būrą` is a long-vowel heavy stem, so the rule's own scope matches the row exactly; and the rule implementation note even records the formal device used in the grammar, `OldEnglishHeavySyllableNasalApocope`, which is the same mechanism the published trace now shows firing on `*būrą` [Germanic/docs/DEV_NOTES.md:1617-1623; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:499-509].

### [Germanic/docs/DEV_NOTES.md:25724-25731]

- Source heading: later row-specific analysis (oblique-cell discussion)
- Fragment type: `shared_rule_reuse`
- Status: `current_supporting_usage`
- Issue tags: `rule_reuse`; `nasal_apocope_still_active`; `diagnostic_confirmation`

This later passage is short but useful because it shows the same rule still being used in live analytic reasoning, not merely preserved as dead archive material. DEV_NOTES says, in a list of derivational consequences, “Heavy-syllable nasal apocope handles the `*ǭ` final vowel” [Germanic/docs/DEV_NOTES.md:25730-25730]. The line is not about `būr`, but it confirms that final nasal-vowel deletion after heavy stems remained an accepted explanatory step elsewhere in the project.

## Superseded or diagnostic material

- The main relevant DEV_NOTES section is explicitly **archived**, so it should be cited as background/supporting project history rather than as a polished literature conclusion. Its own wording marks the rule as an empirical/model-driven discovery and acknowledges the lack of direct handbook formulation for final `*-ą` apocope [Germanic/docs/DEV_NOTES.md:1591-1615].
- The coverage audit entry for row 1964 is diagnostic but important: it confirms that no matching packet, research memo, or previously attached lexeme fragment currently exists for `bower / būr` [Germanic/docs/lexeme_reports/coverage_audit.md:208-208].
- The published derivation trace is likewise diagnostic rather than a DEV_NOTES fragment, but it is the clearest current implementation evidence that the row does not need any workaround beyond heavy-syllable nasal apocope [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:490-509].

## Open questions for later work

- Check whether any primary-source discussion more directly supports loss of final neuter `*-ą` after heavy stems in forms like `*būrą`, so the project need not rely only on the archived empirical DEV_NOTES formulation [Germanic/docs/DEV_NOTES.md:1604-1615].
- Decide whether rows like 1964, which are regular and only supported by shared-rule DEV_NOTES material, should remain unindexed unless a lexeme-specific packet or memo is later created [Germanic/docs/lexeme_reports/coverage_audit.md:208-208].
- If a future shared note on heavy-stem final-vowel loss is written, add `*būrą > būr` as a clean example alongside the other heavy-syllable nasal-apocope cases already cited in DEV_NOTES [Germanic/docs/DEV_NOTES.md:1595-1633].
