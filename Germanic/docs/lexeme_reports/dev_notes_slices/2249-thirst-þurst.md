---
row_id: 2249
concept: thirst
counterpart: þurst
proto: *θúrstuz
protoform: *θúrstuz
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
  - Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2249 thirst / þurst

## Current row state

- CONCEPT: `thirst` [Germanic/data/germanic-aligned-final.tsv:1237]
- COUNTERPART: `þurst` [Germanic/data/germanic-aligned-final.tsv:1237]
- PROTO: `*θúrstuz` [Germanic/data/germanic-aligned-final.tsv:1237]
- PROTOFORM: `*θúrstuz` [Germanic/data/germanic-aligned-final.tsv:1237]
- DERIVATION_CLASS: `regular` [Germanic/data/germanic-aligned-final.tsv:1237]
- The live OE row keeps `PROTO` and `PROTOFORM` identical. That matters here because the row does **not** currently depend on a separate paradigm-cell workaround, alternate proto input, or repaired `COUNTERPART`; the same `*θúrstuz` is both the comparative headword used in the row and the FST input for the OE target `þurst` [Germanic/data/germanic-aligned-final.tsv:1237].
- `coverage_audit.md` still shows row `2249` as uncovered and with no packet, memo, dossier, or prior slice infrastructure to reuse: `| 2249 | thirst | þurst | regular | no | - | - | - | none |` [Germanic/docs/lexeme_reports/coverage_audit.md:392-392].
- `oe_known_problems.tsv` has no row-local entry for `2249`, `*θúrstuz`, `thirst`, or `þurst`; this row is not presently tracked as an OE exception or wontfix item [Germanic/data/oe_known_problems.tsv:1-8].
- The current published OE derivation trace is already an exact match: `PROTO: *θúrstuz`, `EXPECTED: þurst`, `OUTPUTS: þurst`, with the explicit path `*θúrstuz > *θúrstu` by final `-z` deletion, then `*θúrst` by `OE High Vowel Apocope`, then surface `þurst` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:5235-5255].

## Detailed development-note summary

No dedicated thirst-specific dossier currently survives in `Germanic/docs/DEV_NOTES.md`, so this replacement working note has to be explicit about what the project *does* still have. The usable DEV_NOTES support is not a row-local controversy narrative but two shared current stem-class / u-lowering fragments that explain why a Proto-Germanic form in nominative singular `*-uz` keeps root `*u` instead of undergoing NWGmc u-lowering. That is enough to support the live row conservatively, because row `2249` is exactly such a form: `PROTO = PROTOFORM = *θúrstuz`, `COUNTERPART = þurst`, and the live trace already derives the target without repair [Germanic/data/germanic-aligned-final.tsv:1237; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:5235-5255].

Comparative dictionaries support the lexical equation and also help keep the label distinctions straight. Kroonen gives `*þurstu- m. ‘thirst’` and lists `OE þurst, þyrst m. 'id.'`, while Orel gives `*þurstuz ~ *þurstiz sb.m.` with `OE ðurst id.` [@Kroonen2013, p. 553; @Orel2003, p. 430]. Those handbook lemmas are compatible with the live row's `PROTO *θúrstuz`, but they should not be collapsed into the row labels carelessly: in this project `PROTO` is the comparative row headword, `PROTOFORM` is the row's actual derivational input, and for row `2249` the two happen to be the same form rather than separate values [Germanic/data/germanic-aligned-final.tsv:1237].

The first shared DEV_NOTES fragment relevant to this row states the general stem-class principle directly. While discussing genuine u-lowering exception candidates, DEV_NOTES notes that “u-stems and root nouns regularly preserve `*u` because their paradigms have predominantly high-vowel suffixes (nom.sg. `*-uz`, acc.sg. `*-ŷ`, gen.sg. `*-iz`, dat.sg. `*-i`, nom.pl. `*-iz`, etc.)” and gives the concrete model example `*lustuz (u-stem nom.sg.) → OE lust with preserved u` [DEV_NOTES:line-92-93; @RingeTaylor2014, p. 45]. That statement is not about `þurst` by name, but it is directly portable to row `2249`, because `*θúrstuz` is exactly the same structural type: a u-stem nominative singular in `*-uz`, where the following high vowel means the root `*u` is not in the environment for NWGmc lowering.

The second shared DEV_NOTES fragment makes the same point in even more explicit rule language. In the `duru` note, DEV_NOTES says: `*duruz (u-stem) → no u-lowering → *duru ✓` and then explains why: “The u-stem nominative singular `*-uz` has a high vowel in the ending, so the root vowel *u is not before a non-high vowel. U-lowering is not triggered” [DEV_NOTES:line-961-969]. For row `2249`, that is the clearest current project statement of why `*θúrstuz > þurst` is regular rather than exceptional. The current published trace matches the same logic exactly: once final `-z` is deleted (`*θúrstuz > *θúrstu`) and OE high-vowel apocope removes the final vowel (`*θúrstu > *θúrst`), the surface form `þurst` follows without any special repair layer [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:5242-5255].

The conservative row-level conclusion should therefore stay narrow and explicit. Row `2249` is not a known-problems exception, not a lexical u-retention anomaly of the `wulf/fugol/rust` type, and not a row that currently needs a substitute `PROTOFORM`. It is a regular u-stem nominative-singular continuation whose surviving DEV_NOTES support is shared phenomenon prose rather than a thirst-only memo. That evidentiary shape is perfectly adequate for a replacement working note, but it is still thin and shared enough that the row should probably remain no-index unless later work produces a dedicated packet, memo, or thirst-specific DEV_NOTES block.

## Relevant DEV_NOTES fragments with line-based refs

No dedicated thirst-only DEV_NOTES section survives, but two shared current fragments are genuinely relevant because both explain why a u-stem nominative singular in `*-uz` preserves root `*u`.

### DEV_NOTES:line-92-93

- Source heading: `Could we use paradigm forms? (Why we decided not to)`
- Source line or section hint: `lines 92-93`
- Fragment type: `copied_shared_lexeme_fragment`
- Status: `current`
- Issue tags: `u_stem`; `u_lowering_blocked`; `high_vowel_suffix`; `shared_stem_class_rule`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This fragment preserves the most compact current statement of the paradigm fact row `2249` depends on. DEV_NOTES says that “u-stems and root nouns regularly preserve `*u` because their paradigms have predominantly high-vowel suffixes” and gives `*lustuz ... → OE lust with preserved u` as the example [DEV_NOTES:line-93-93; @RingeTaylor2014, p. 45]. For `*θúrstuz > þurst`, the relevance is direct rather than analogical hand-waving: the row already has the u-stem nominative singular ending `*-uz`, so preserved `u` is the expected structural outcome, not a repair imported from some different paradigm cell.

### DEV_NOTES:line-961-969

- Source heading: `Why u-lowering doesn't apply`
- Source line or section hint: `lines 961-969`
- Fragment type: `copied_shared_lexeme_fragment`
- Status: `current`
- Issue tags: `u_stem`; `u_lowering_not_triggered`; `stem_class_not_exception`; `shared_rule_statement`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This fragment is the clearest current project wording of the rule itself. DEV_NOTES contrasts `*durą` and `*durō`, where u-lowering would apply, with `*duruz`, where it does not, and then states explicitly: “The u-stem nominative singular `*-uz` has a high vowel in the ending, so the root vowel *u is not before a non-high vowel. U-lowering is not triggered” [DEV_NOTES:line-967-969]. For row `2249`, that statement is effectively the working explanation that later report writers would otherwise have to reconstruct from scratch. It shows that `þurst` belongs with ordinary u-stem preservation, not with the documented lexical exceptions where lowering unexpectedly fails.

## Superseded or diagnostic material

- No superseded thirst-specific DEV_NOTES proposal was located. The real documentary limitation for this row is not abandoned analysis but the absence of a dedicated row-local note block.
- The exact-match derivation trace is important diagnostic support, but it is infrastructure output rather than DEV_NOTES prose. Its value is to confirm that the current rule cascade already reaches `þurst` from the live `PROTOFORM *θúrstuz` without workaround [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:5235-5255].
- `coverage_audit.md` is likewise diagnostic only. Its `none` entry is useful for filename choice and for confirming that no packet or memo stem exists to reuse, but it is not itself an argument about the philology of `þurst` [Germanic/docs/lexeme_reports/coverage_audit.md:392-392].
- The absence of any `oe_known_problems.tsv` entry is also diagnostic rather than argumentative: it confirms that the row is not currently being quarantined as a known OE mismatch, but the positive explanation still has to come from the shared u-stem/u-lowering material above [Germanic/data/oe_known_problems.tsv:1-8].

## Open questions for later work

- If `dev_notes_slices/index.tsv` is revisited later, decide conservatively whether the two shared current fragments above are strong enough to justify indexing, or whether row `2249` should remain a no-index slice until a dedicated thirst-specific note, packet, or memo exists.
- If a later lexeme report is written, keep the label distinction explicit: handbook lemma formatting such as Kroonen's `*þurstu-` and Orel's `*þurstuz ~ *þurstiz` should inform the discussion, but the live row's `PROTO` and `PROTOFORM` remain the project's current `*θúrstuz` unless the TSV itself changes [@Kroonen2013, p. 553; @Orel2003, p. 430].
- If later work builds a shared memo on OE reflexes of PGmc u-stem nominative singular `*-uz`, row `2249` should be grouped with regular preservation cases such as `*lustuz > lust` and the `*duruz > duru` rule illustration, not with the genuine lexical u-lowering exceptions discussed near labials and velars [DEV_NOTES:line-63-137,92-93,961-969].
