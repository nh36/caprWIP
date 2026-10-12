---
row_id: 2061
concept: hay
counterpart: hīeġ
proto: *xáwwją
protoform: *xáwwją
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
  - Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md
  - Germanic/docs/lexeme_reports/coverage_audit.md
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2061 hay / hīeġ

## Current row state

- The live OE row is `2061`, `CONCEPT hay`, `COUNTERPART hīeġ`, `PROTO *xáwwją`, `PROTOFORM *xáwwją`, `DERIVATION_CLASS regular`; `PROTO` and `PROTOFORM` are currently identical, but the row’s OE target is the attested WS form `hīeġ`, not a reconstructed placeholder and not the extra-WS forms `hēg/hēje` cited in the literature extracts below [Germanic/data/germanic-aligned-final.tsv:509-509].
- Coverage tracking still marks the row as `2061 | hay | hīeġ | regular | no | - | - | - | none`, so there is no packet, research memo, dossier, or report-manifest wiring for this lexeme at present [Germanic/docs/lexeme_reports/coverage_audit.md:268-268].
- `oe_known_problems.tsv` does not list `*xáwwją` or `hīeġ`; current project state is therefore that this row is solved and not carried as a separate OE exception-table item [Germanic/data/oe_known_problems.tsv:1-8].
- The current published derivation trace is an exact match: `PROTO: *xáwwją`, `EXPECTED: hīeġ`, `OUTPUTS: hīeġ`. The OE-side path shown now is `OE Awj Glide Formation: *xáują`, `OE Au Fronting: *xáeują`, `OE Diphthong Leveling: *xēają`, `OE Velar Fricative Palatalization: *çēają`, `OE Heavy Syllable Nasal Apocope: *çēaj`, `OE I Umlaut: *çīej`, with orthographic output `h*īeġ` and final `Outcome: hīeġ` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2116-2136].

## Development-note summary

There is no long standalone row-only DEV_NOTES essay for `hīeġ`; the surviving material is distributed across shared `*aw+j` and `*ww` workflow sections. Still, the row is unusually well supported. The current row-specific support is: (i) the fix ledger entry `hīeġ: OEAwjGlideFormation *aw(w)+*j → *au+*j`, (ii) the audit-supplement’s explicit five-stage WS path for row `2061`, and (iii) the later Q3 record that Q1/Q2 were implemented and row `2061` now matches [Germanic/docs/DEV_NOTES.md:10410-10410,26816-26823,27120-27125]. Shared-background-only support is also strong and still relevant because the embedded grammar quotations explicitly cite `hīeġ`/`hēg` as the regular OE outcome class for inherited `*hawja/*hauwja` material, alongside `īeġ` and `cīeġan` [Germanic/docs/DEV_NOTES.md:27148-27200]. Superseded or purely diagnostic material survives too, chiefly the earlier exclusion note `*xawwją → heow (expected hīeġ) — *j follows *w, not a vowel`, which records an older rule-shape and failed output but no longer reflects current derivation state [Germanic/docs/DEV_NOTES.md:3652-3654].

The most important working distinction is between row `2061` and the related `*aw+j` verb row `2227`. For `hīeġ`, the relevant `*j` is word-final at the decisive late OE stage, so the current system reaches `*çīej` and spells final `j` as `ġ`; the later intervocalic `*j > ġ/ʒ` rule work was needed for `strīeġan`, not for this noun [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2129-2135; Germanic/docs/DEV_NOTES.md:27120-27125,27392-27399,27454-27458]. That makes the row fully current, but mostly as a solved control case plus a literature anchor for the aw-series `-ġ` class.

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-3652-3654

- Source heading: `Fixes (3 new matches)` / `Correctly excluded`
- Source line hint: `lines 3652-3654`
- Fragment type: `early_row_specific_diagnostic`
- Status: `superseded_diagnostic_only`
- Issue tags: `former_output_heow`; `awj_not_seen`; `pre_fix_exclusion`
- Recommended next use: `cite_only_if_explaining_the_old_failure_signature`
- Shared with rows if relevant: `2227`

This is the earliest terse row-local note that still matters, but only diagnostically. DEV_NOTES says: `*xawwją → heow (expected hīeġ) — *j follows *w, not a vowel` [Germanic/docs/DEV_NOTES.md:3652-3654]. The substance to preserve is narrow: an older rule set handled ordinary `*aw` developments well enough to drift toward `heow`, but it did not yet treat `*aw(w)+*j` as its own environment. This is superseded project history, not a live competitor to the row’s target.

### DEV_NOTES:line-16308-16327

- Source heading: `Rule 2: PWGmc Geminate *ww Simplification` / `Verification of Existing *ww Handling`
- Source line hint: `lines 16308-16327`
- Fragment type: `shared_background_verification`
- Status: `current_shared_background_only`
- Issue tags: `ww_handling`; `control_case`; `implementation_caution`
- Recommended next use: `cite_if_explaining_why_hay_belongs_with_other_ww_rows_but_is_already_solved`
- Shared with rows if relevant: `1976`; `1989`; `2074`

This fragment is not row-specific in composition, but it is still current and important. DEV_NOTES records: `Note: The existing FST already handles *ww inputs correctly via *ww → ēo. Testing *kewwăną → ċēowan ✓, *dawwō → dēaw ✓, *xawwăną → hēawan ✓` and then immediately lists `*xawwją → hīeġ ✓` among the existing `*ww` TSV entries [Germanic/docs/DEV_NOTES.md:16310-16325]. The caution in the same block should be retained: the grammar may be reaching the right answer by “a different mechanism than R/T's two-step analysis” [Germanic/docs/DEV_NOTES.md:16316-16317]. For row `2061`, that means current correctness is secure, but older and newer DEV_NOTES stages use slightly different internal narratives for how the `*ww`/`*awj` sequence is traversed.

### DEV_NOTES:line-26816-26823

- Source heading: `What this means for our two targets`
- Source line hint: `lines 26816-26823`
- Fragment type: `row_specific_ws_path`
- Status: `current_for_row_state_but_old_stage_notation`
- Issue tags: `ws_target`; `five_stage_path`; `awj_chain`
- Recommended next use: `cite_if_needing_the_explicit_DEV_NOTES_stage_sequence_for_row_2061`
- Shared with rows if relevant: `2227`

This is the cleanest row-specific DEV_NOTES path statement. It gives the WS development for the noun itself:

> `Target 1: row 2061 *xáwwją → hīeġ (WS).`
> `WS pathway (stages 1-5):`
> `*xawwją (input already has *aww, stage 1 vacuous)`
> `→ stage 2 → *xaują`
> `→ stage 3 → *xēają`
> `→ stage 4 → *xēag(j)ą`
> `→ stage 5 (WS) → *xīegą → hīeġ ✓` [Germanic/docs/DEV_NOTES.md:26816-26823]

This is current in practical conclusion: row `2061` is the WS aw-series noun and should end at `hīeġ`. It is partly superseded in notation by the modern debug trace, which now shows `*çīej` before orthography rather than an explicit intermediate `*xīegą` stage [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2129-2135]. The two records are best treated as compatible representations of the same solved row unless later rule refactoring proves otherwise.

### DEV_NOTES:line-27120-27200

- Source heading: `§17.10.36-q3 — Q3 RESOLUTION RESEARCH` / `German philological tradition`
- Source line hint: `lines 27120-27200`
- Fragment type: `current_row_status_plus_shared_philological_support`
- Status: `current`
- Issue tags: `row_now_matches`; `aw_series_j_retention`; `ws_vs_extra_ws_forms`
- Recommended next use: `primary_current_citation_for_both_state_and_literature_support`
- Shared with rows if relevant: `2227`

This is the most important current fragment. It begins with a row-state update: `Q1 and Q2 have been implemented ... Row 2061 (*xáwwją → hīeġ) now matches` [Germanic/docs/DEV_NOTES.md:27120-27122]. For row `2061`, that sentence is row-specific current support, and it is stronger than the older diagnostic material. The rest of the block is shared-background philology, but it is directly relevant because the quotations explicitly cite `hay` and distinguish WS from non-WS outcomes.

> `Urg. j im In- und Auslaut nach langen Vokalen = ae. g [j]: cīegan rufen, strēgan streuen, frēogea lieben, fēogea hassen — īeg, īg Insel, hīeġ Heu, ǣg Ei, clǣġ Lehm.` [Germanic/docs/DEV_NOTES.md:27148-27150]

> `§460: "Im ae. Auslaut erscheint urg. j nur nach langen Vokalen oder Diphthongen und wird fast stets g geschrieben: ws. hīeġ, außerws. hēg 'Heu', ws. īeġ, außerws. ēg, ēi, ēiġ 'Insel' (< urg. *haujō, *aujō)."` [Germanic/docs/DEV_NOTES.md:27163-27166]

> `... mit ursprünglichem a: *hauwja- 'Heu', *auwjō- 'Insel', *frauwjō 'Herr', *strauwjan 'streuen', *kauwjan 'rufen' ... Die altenglischen Formen haben die normale Entwicklung durchlaufen ... angl. hēg, ēg, strēgan, cēgan, ws. hīeġ, īeġ, *frīeġea (> frīġea), cīeġan).` [Germanic/docs/DEV_NOTES.md:27192-27199]

The dense takeaway is that the noun belongs to a literature-backed aw-series class where inherited final `*j` after a long vowel/diphthong is preserved orthographically as `g/ġ`; WS gives `hīeġ`, while extra-WS/Anglian material gives `hēg`. That is shared background, but for this row it is still live support rather than antiquarian quotation.

### DEV_NOTES:line-27367-27458

- Source heading: `§17.10.36-q3-probes — REGRESSION PROBES`
- Source line hint: `lines 27367-27458`
- Fragment type: `current_probe_support`
- Status: `current`
- Issue tags: `word_final_j`; `not_touched_by_intervocalic_rule`; `closed_class`
- Recommended next use: `cite_if_explaining_why_later_awj_rule_work_should_not_reopen_this_row`
- Shared with rows if relevant: `2227`

This fragment turns the literature synthesis into a concrete engineering boundary. DEV_NOTES first shows that the entire OE `*Vw+*j` class in the corpus consists of only two rows:

> `509   *xáwwją       hīeġ      (already matches post-Q1/Q2)`
> `1153  *stráwjaną    strīeġan  (target of the proposed rule)` [Germanic/docs/DEV_NOTES.md:27373-27375]

It then gives the post-i-umlaut states and explicitly separates the noun from the verb:

> `xáwwją       → *ç*īe*j            (2 chars: *j word-final, rule will NOT fire — no following vowel. Already matches via orthography {*j} → ġ / _ .#.)` [Germanic/docs/DEV_NOTES.md:27392-27396]

> `The proposed rule requires _ EnglishStarVocalic (vowel must follow). For row 509 hīeġ, *j is word-final at post-i-umlaut (*ç*īe*j, no following vowel). The rule correctly does NOT fire; existing orthography {*j} -> ġ || _ .#. handles it. No interaction.` [Germanic/docs/DEV_NOTES.md:27454-27458]

For row `2061`, this is current and row-specific enough to preserve in full: later aw-series `j`-strengthening work belongs to the intervocalic verb case, while `hīeġ` is already in the correct final-`j` pathway.

## Superseded or diagnostic material

- The old `heow` output is superseded. It documents a real pre-fix state, but it reflects an obsolete environment analysis in which `*aw(w)+*j` was not yet being treated as its own trigger class [Germanic/docs/DEV_NOTES.md:3652-3654].
- The stage notation `*xēag(j)ą` → `*xīegą` in the audit-supplement is best treated as diagnostic-to-explanatory rather than as the authoritative modern derivation trace. The published snapshot now reaches `*çīej` before orthography, so future writing should not flatten those two representations into a falsely precise single internal path without checking the current grammar [Germanic/docs/DEV_NOTES.md:26820-26823; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2129-2135].
- Shared literature quotes about `hēg/hēje` are not rival row targets. They remain relevant because they document the broader aw-series class and the WS vs non-WS distribution, but the live row’s `COUNTERPART` is specifically WS `hīeġ` [Germanic/data/germanic-aligned-final.tsv:509-509; Germanic/docs/DEV_NOTES.md:27158-27166,27192-27199].
- The later intervocalic `*j > ġ/ʒ` work is diagnostic background only for this row. It matters insofar as it proves why row `2061` should be left alone while row `2227` changes; it is not evidence that `hīeġ` itself still needs a new phonological repair [Germanic/docs/DEV_NOTES.md:27120-27125,27392-27399,27454-27458].

## Open questions for later work

- If a future packet or full report is created for this row, preserve the WS/non-WS distinction explicitly: live row target `hīeġ`; comparative non-WS support `hēg/hēje`. Do not collapse those into one undifferentiated “OE hay” citation pool [Germanic/docs/DEV_NOTES.md:27158-27166,27192-27199].
- If OE derivation snapshots are regenerated after rule refactoring, re-check whether the internal late-stage notation remains `*çīej` with orthographic final-`j` spelling or shifts back toward an explicit `*...g/ʒ` intermediate. The row probably remains correct either way, but the replacement note should track whichever representation the live trace actually shows [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2129-2135; Germanic/docs/DEV_NOTES.md:26820-26823].
- If later aw-series work revisits row `2227`, keep `2061` as the solved word-final control case. DEV_NOTES is explicit that the corpus class is only two rows wide and that only the intervocalic one was supposed to move under the later Q3 rule [Germanic/docs/DEV_NOTES.md:27373-27379,27454-27458].
