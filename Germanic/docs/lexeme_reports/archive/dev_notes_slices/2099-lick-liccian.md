---
row_id: 2099
concept: lick
counterpart: liccian
proto: *líkkōjaną
protoform: *líkkōjaną
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file: null
linked_research_memo_file: null
linked_dossier_or_analysis_files:
  - Germanic/docs/analysis/notable_findings.md
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2099 lick / liccian

## Current row state

- CONCEPT: `lick`
- COUNTERPART: `liccian`
- PROTO: `*líkkōjaną`
- PROTOFORM: `*líkkōjaną`
- DERIVATION_CLASS: `regular` [Germanic/data/germanic-aligned-final.tsv:654-654]
- The live TSV row is bare/clean: no row note, no history note, and no known-problems flag. This is a regular row in current repo policy, not a tolerated mismatch row [Germanic/data/germanic-aligned-final.tsv:654-654; Germanic/data/oe_known_problems.tsv:1-8].
- Current derivation/debug state is fully regular and transparent: the publish snapshot gives `PROTO: *líkkōjaną`, `EXPECTED: liccian`, `OUTPUTS: liccian`, then traces `*líkkōjaną > *líkkōjan > *líkkōjąn > *líkkējąn > *líkkejąn > *líkkejan > *líkkeian > *líkkian`, surface `liccian` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2781-2800].
- The current shared analysis file treats `liccian` as one of the key negative controls for NWGmc `*i > *e` lowering: “\*liccian (velar geminate \*-kk-): blocking ✓”. The same note explains that unconditional i-lowering wrongly regressed this lexeme family and that dorsal geminates belong to the blocking environment, alongside labials and other non-coronal codas [Germanic/docs/analysis/notable_findings.md:1065-1080].
- `coverage_audit.md` currently records row 2099 as uncovered (`report? no`, packet/memo/dossier all absent). This slice is therefore standing in for missing row-level documentation rather than replacing an existing packet [Germanic/docs/lexeme_reports/coverage_audit.md:292-292].
- There is no dedicated row-2099 packet, research memo, or manifest entry. The only nearby lexeme-report infrastructure is for companion finite-cell rows 2315 `licca` and 2316 `liccaþ`, which explicitly treat `liccian` as the separate lemma comparator rather than as a problem case of their own [Germanic/docs/lexeme_reports/research_memo_index.tsv:146-147; Germanic/docs/lexeme_reports/research_memos/2315-lick-(iptv.2sg)-licca.md:13-21,56-59].

## Development-note summary

No standalone row-specific `DEV_NOTES` block for `lick / liccian` survives in current repo materials. What survives is (a) superseded row-specific debugging from the March Class II weak-verb work and (b) current shared-background discussion from the later NWGmc i-lowering analysis. The slice therefore has to be conservative: there is some row-relevant material, but most of the durable support is shared-background-only rather than a dedicated lexeme essay [Germanic/docs/DEV_NOTES.md:2821-2836,2948-2986,5352-5425,5710-5788].

The durable current point is simple: row 2099 is regular now, and the repo uses it as evidence that the system must **not** lower root `*i` before non-high vowels when a dorsal geminate intervenes. `DEV_NOTES` first recorded older false states `liċceian`, `liċca`, and `leccian`; those are no longer live outputs, but they preserve why this lexeme family was being watched during the palatalization and i-lowering work [Germanic/docs/DEV_NOTES.md:2821-2829,2950-2986,5410-5418]. The later current sections then absorb `lick` into the broader blocking analysis and say, first, that “every form that retained \*i has a velar or labial consonant in the coda,” and, second, that the refined hypothesis “correctly predicts all observed cases,” including `lick` with `*kk` and unchanged `liccian` [Germanic/docs/DEV_NOTES.md:5376-5378,5748-5750,5779-5787].

For row 2099 specifically, the practical replacement note is therefore: keep `PROTO` and `PROTOFORM` distinct only if a future data change requires it, because at present they coincide as `*líkkōjaną`; treat `liccian` as the ordinary lemma/citation-form OE target; treat old `liċceian`/`liċca`/`leccian` states as superseded diagnostics only; and use the current i-lowering blocking discussion, not the old Class II debugging table, as the main explanation for why the row is now stable [Germanic/data/germanic-aligned-final.tsv:654-654; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2781-2800; Germanic/docs/DEV_NOTES.md:2981-2986,5354-5378,5779-5787].

## Relevant DEV_NOTES fragments

### DEV_NOTES: 2821-2836

- Source heading: `All 8 Class II Weak Verbs in TSV (all produce -eian)`
- Source line hint: `lines 2821-2836`
- Fragment type: `lexeme_specific_diagnostic`
- Status: `superseded`
- Issue tags: `weak_ii_suffix`; `historical_false_output`; `palatalization_history`
- Recommended next use: `use_only_to_explain_why_the_lexeme_family_entered_debugging`
- Shared-with rows if relevant: `2309; 2310; 2311; 2312; 2313; 2314; 2315; 2316; 2317; 2318`

This table is old but still worth preserving because it is the earliest compact row-specific signal for 2099. It records the then-live false output `*likkōjăną -> liċceian`, expected `liccian`, and classifies the failure as `palatal_extra__j_triggered` [Germanic/docs/DEV_NOTES.md:2823-2829]. The substance to keep is narrow: at that stage the project was not treating `liccian` as philologically doubtful, but as a regular weak-II target being distorted by an implementation bug around `-ōja-` outputs and front-triggered palatal behavior. This fragment is therefore row-specific support only in a historical/diagnostic sense; it is not current authority for the live row.

### DEV_NOTES: 2948-2986

- Source heading: `Results summary`; `C. Spurious palatalization of geminate *kk (*likkô → liċca vs licca)`
- Source line hint: `lines 2948-2986`
- Fragment type: `lexeme_specific`
- Status: `superseded_but_explanatorily_useful`
- Issue tags: `geminate_kk`; `spurious_palatalization`; `family_debug_history`
- Recommended next use: `keep_as_labeled_debug_history_only`
- Shared-with rows if relevant: `2315; 2316`

This is the clearest surviving row-specific `DEV_NOTES` prose for the lexeme family, but it is no longer current row policy. The results table logs `likkô -> liċca` and `likkōθi -> liċceþ`, then the prose states the key diagnosis: “OE palatalization of *k → ċ before front vowels is correct in general, but geminate *kk should NOT be palatalized in this context. The *i in the root is a front vowel, but geminate velars resist palatalization (R/T §6.4.1)” [Germanic/docs/DEV_NOTES.md:2950-2959,2981-2986]. For row 2099, the lasting value of this fragment is not the false finite outputs themselves, but the lexical warning it preserves: this family had been corrupted by spurious treatment of geminate `*kk`, so later clean outputs should be read as a fix, not as a new philological reinterpretation.

The fragment is also a reminder to keep lemma row 2099 separate from its companion finite-cell debugging. The prose is framed around `*likkô` and `*likkōθi`, not directly around row 2099’s infinitive/lemma input, so its support for 2099 is partly shared-family rather than perfectly row-specific. Still, the same `*kk` issue that broke `licca` and `licceþ` is what earlier produced `liċceian` for the lemma row as well [Germanic/docs/DEV_NOTES.md:2823-2829,2958-2959].

### DEV_NOTES: 5352-5425

- Source heading: `Applying the Theory to Our Data`; `Experimental Implementation and Results`
- Source line hint: `lines 5352-5425`
- Fragment type: `shared_background_current`
- Status: `current`
- Issue tags: `i_lowering`; `dorsal_blocking`; `shared_methodology`; `negative_control`
- Recommended next use: `cite_as_current_background_for_why_liccian_stays_with_i`
- Shared-with rows if relevant: `2099; 2096; 2101; 2116; 2246`

This is the main current material that still genuinely supports row 2099. `DEV_NOTES` builds a shared hypothesis for sporadic NWGmc/OE `*i > *e` lowering and then tests the corpus. In that test table `lick` appears with proto `*likkōną`, coda `-kk-`, place features “**dorsal** geminate,” expected “**blocking**,” OE output `liccian ✓` [Germanic/docs/DEV_NOTES.md:5363-5371]. The section then states the generalization in words: “**every form that retained \*i has a velar or labial consonant in the coda**” [Germanic/docs/DEV_NOTES.md:5376-5378]. That sentence is shared-background-only, not row-specific, but row 2099 is one of the concrete exemplars carrying the claim.

The same section also preserves the key negative diagnostic from the failed experimental rule. Once unconditional NWGmc i-lowering was tried, the regression table recorded `lick | *likkōjăną | leccian | **liccian** | velar *kk` [Germanic/docs/DEV_NOTES.md:5408-5418]. For the slice, that material should be tagged diagnostic rather than authoritative philology: it shows exactly what went wrong when the blocker was omitted, and why `liccian` now functions as a must-not-regress test item.

### DEV_NOTES: 5710-5788

- Source heading: `Refined hypothesis (potentially novel)`; `Implementation successful (2026-03-09)`
- Source line hint: `lines 5710-5788`
- Fragment type: `shared_background_current`
- Status: `current`
- Issue tags: `i_lowering_rule`; `blocking_hypothesis`; `post_fix_verification`
- Recommended next use: `treat_as_the_best_current_DEV_NOTES_support_for_row_2099`
- Shared-with rows if relevant: `2099; 2094; 2096; 2101`

This is the strongest current `DEV_NOTES` support because it moves from hypothesis to implemented verification. The refined hypothesis says velars block i-lowering “regardless of position,” while labials block in the intervening position; in the test table, `lick` is one of the predicted blocking cases: `Velar/labial after? **Yes** (*kk)`, `Predicted Block`, `Actual OE liccian ✓` [Germanic/docs/DEV_NOTES.md:5712-5727,5738-5750]. `DEV_NOTES` then says flatly, “**The hypothesis correctly predicts all observed cases**” [Germanic/docs/DEV_NOTES.md:5748-5750].

The post-fix results table is the cleanest current row-relevant verification line in `DEV_NOTES`: `*likkōjăną | liccian | liccian | liccian | ✓ No change (velar *kk in coda)` [Germanic/docs/DEV_NOTES.md:5777-5787]. This is shared-background-only rather than a dedicated `liccian` essay, but it is current and operationally decisive. If later work needs one `DEV_NOTES` citation for why row 2099 is presently stable, use this fragment first.

## Superseded or diagnostic material

- The March weak-II table entry `*likkōjăną -> liċceian` is superseded implementation history only. It documents an old failure mode, not a surviving uncertainty about OE `liccian` [Germanic/docs/DEV_NOTES.md:2823-2829].
- The “spurious palatalization of geminate *kk” note is still useful because it preserves the family-specific bug diagnosis, but for row 2099 it is no longer current policy. The live row is not under a palatalization warning state now; the snapshot already returns `liccian` cleanly [Germanic/docs/DEV_NOTES.md:2981-2986; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2781-2800].
- The failed experimental i-lowering regression `leccian` is diagnostic evidence for rule design, not lexeme philology. Its value is precisely that it shows what happens if the dorsal-geminate blocker is removed [Germanic/docs/DEV_NOTES.md:5408-5418].
- Related `licca` / `liccaþ` materials in the companion-row memo tradition should not be back-projected into row 2099 as if they were lemma evidence. Those memos explicitly distinguish row 2099’s `*líkkōjaną -> liccian` from the finite-cell inputs `*líkkô -> licca` and `*líkkōθi -> liccaþ`, and they mark older `liċca`/`lecca` states as stale debugging history [Germanic/docs/lexeme_reports/research_memos/2315-lick-(iptv.2sg)-licca.md:28-31,56-61,101-112].

## Open questions for later work

- If row 2099 eventually gets a full packet/memo, keep the evidential split explicit: no dedicated row-specific `DEV_NOTES` essay survives; the current support is mainly shared i-lowering background plus old family-level diagnostics.
- If future cleanup touches notation, decide whether the various `DEV_NOTES` spellings (`*likkōjăną`, `*likkōną`) should be normalized against live TSV `*líkkōjaną` in explanatory prose while still acknowledging that the underlying point is the same dorsal-geminate `*kk` blocker, not a proto reconstruction dispute [Germanic/docs/DEV_NOTES.md:2828-2828,5416-5418,5786-5786; Germanic/data/germanic-aligned-final.tsv:654-654].
- If later literature work revisits the palatalization side, keep the current row claim narrow: the live row does not need a new philological rescue, only accurate documentation of why geminate `*kk` and coda dorsals were treated as blockers in the debugging history [Germanic/docs/DEV_NOTES.md:2981-2986,5738-5787].
