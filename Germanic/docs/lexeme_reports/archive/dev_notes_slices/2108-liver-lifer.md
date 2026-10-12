---
row_id: 2108
concept: liver
counterpart: lifer
proto: *líbrō
protoform: *líbrō
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
  - Germanic/docs/analysis/notable_findings.md
  - Germanic/docs/germanic_notes/final_vowel_apocope_investigation.md
  - Germanic/docs/germanic_notes/heavy_syllable_apocope_experiment_results.md
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2108 liver / lifer

## Current row state

- The live TSV row is `2108 | liver | lifer | *líbrō | *líbrō | regular`; the source-note field still consists only of Wiktionary-derived placeholders, not a row-local working rationale [Germanic/data/germanic-aligned-final.tsv:690-690].
- `PROTO` and `PROTOFORM` are currently the same string, `*líbrō`; for this row that means the comparative headword and the actual OE-directed input have **not** been split. The accent notation is also deliberate: DEV_NOTES' symbol inventory uses acute-marked short stressed vowels, and `*líbrō` is given there as an example of a primary-stressed short root vowel [Germanic/data/germanic-aligned-final.tsv:690-690; Germanic/docs/DEV_NOTES.md:20570-20578].
- `oe_known_problems.tsv` has no entry for `*líbrō`, `lifer`, or `liver`, so the row is not currently being triaged as an exception bucket or unresolved mismatch [Germanic/data/oe_known_problems.tsv:1-8].
- Coverage/report infrastructure is still absent: `coverage_audit.md` marks row `2108` as `none`, and `report_manifest.tsv` has no row-specific manifest entry for it [Germanic/docs/lexeme_reports/coverage_audit.md:297-297; Germanic/docs/lexeme_reports/report_manifest.tsv:1-13].
- The current published derivation snapshot already matches the live row without repair notes: `PROTO: *líbrō`, `EXPECTED: lifer`, `OUTPUTS: lifer`, with the condensed chain `*líbrō → *líbru → *líβru → *líβr → *líβer → lifer`. The important negative fact is that no `*i > *e` lowering stage appears in the successful current derivation [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2943-2962].

## Development-note summary

No standalone **row-specific DEV_NOTES block** survives for `liver / lifer`. The surviving evidence is thinner and has to be handled conservatively: the best row-relevant material is embedded inside shared i-lowering diagnostics, plus one Campbell quotation copied into DEV_NOTES from a different lexeme discussion [Germanic/docs/DEV_NOTES.md:5352-5424,5738-5792,17397-17472,22650-22653].

The safest current reading is therefore narrow. The live row's policy is simply `PROTO = *líbrō`, `PROTOFORM = *líbrō`, `COUNTERPART = lifer`, `DERIVATION_CLASS = regular`, and the present trace reaches `lifer` by final `-ō` raising, `b` allophony, high-vowel apocope, and final-cluster epenthesis, not by any analogue or manually substituted protoform [Germanic/data/germanic-aligned-final.tsv:690-690; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2950-2962].

What DEV_NOTES preserves for this row is mainly the **negative control** value of `lifer`. In the shared i-lowering investigation, `liver` is one of the words showing that an unconditional `*i > *e` rule would be wrong for Old English: the notes repeatedly contrast hypothetical `lefer` with actual `lifer`, and later treat `lifer` as one of the crucial OE facts suggesting that a coda labial can block lowering [Germanic/docs/DEV_NOTES.md:5410-5415,5740-5748,17401-17420]. `analysis/notable_findings.md` distills the same project conclusion, explicitly listing `*librō → *lifer` among the forms that must keep `*i` when i-lowering is conditioned by place features [Germanic/docs/analysis/notable_findings.md:1065-1080].

The only direct primary-source quotation in DEV_NOTES that names the OE form is split across two contexts and must not be overread. Fulk is quoted for the fact that OE has retained-`i` `lifer` beside lowered continental forms; Campbell is quoted for the fact that `Lifer` participates in later parasite-vowel history. Neither quotation, by itself, is the project's current `PROTOFORM` policy, and neither constitutes a self-contained row dossier [Germanic/docs/DEV_NOTES.md:17408-17413,22650-22653].

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-17397-17472

- Source heading: `Where did the coronal-only constraint come from?` / `The lifer case is crucial:`
- Source line hint: `Germanic/docs/DEV_NOTES.md:17397-17472`
- Fragment type: `row_specific_evidence_embedded_in_shared_i_lowering_audit`
- Status: `current`
- Issue tags: `retained_i`; `labial_blocking`; `Fulk_quote`; `shared_rule_vs_row_fact`
- Recommended next use: `primary_anchor_for_retained_i_problem`
- Shared-with rows if relevant: `2107 live / lifeþ`; `2189 sieve / sife`; `2099 lick / liccian`; `2283 wether / weþer`

This is the strongest surviving row-relevant DEV_NOTES material because it explicitly treats `lifer` as probative evidence, not as a stray mention. The table sets up `*librō` as a theory-testing case — `Fulk predicts` lowering, `Our rule predicts` blocking, `OE attested` `lifer` — and then preserves the key quotation: `"OHG lebara, MLG lever (cf. **OIcel. lifr, OE lifer**, OFris. livere) 'liver'"` [Germanic/docs/DEV_NOTES.md:17399-17413]. The useful row-specific substance here is limited but real: OE `lifer` is explicitly being used as evidence that Old English retained `i` where continental comparanda lowered.

The same fragment also marks the limit of the evidence. DEV_NOTES immediately says that Fulk "does NOT explain WHY OE blocked lowering here" and that the project's coronal-only / labial-blocking rule is stricter than Fulk's explicit formulation [Germanic/docs/DEV_NOTES.md:17411-17420,17424-17432]. So the retained-`i` fact is row-specific support; the blocking explanation is **shared-background-only current analysis**, not a quotation that can be attributed back to Fulk.

### DEV_NOTES:line-5352-5424

- Source heading: `Applying the Theory to Our Data` / `Experimental Implementation and Results`
- Source line hint: `Germanic/docs/DEV_NOTES.md:5352-5424`
- Fragment type: `shared_background_only`
- Status: `current`
- Issue tags: `i_lowering`; `regression_test`; `labial_coda`; `project_rule_state`
- Recommended next use: `cite_when_explaining_why_current_trace_has_no_lowering_stage`
- Shared-with rows if relevant: `2099 lick / liccian`; `2107 live / lifeþ`; `2189 sieve / sife`; `2200 sorrow / sorg`; `2283 wether / weþer`

This passage is not a row dossier, but it is the main shared background explaining why `liver` kept appearing in the notes. DEV_NOTES first classifies `liver | *librō | -br- | labial + coronal | blocking | lifer ✓`, then states the generalization: `"every form that retained *i has a velar or labial consonant in the coda"` [Germanic/docs/DEV_NOTES.md:5365-5378]. It then records the failed unrestricted implementation, where `liver | *librō | lefer | lifer | labial *b` appears in the regression table [Germanic/docs/DEV_NOTES.md:5410-5415].

For row 2108, this support is explicitly **shared-background-only**. Its value is that it preserves the project's reason for treating `lifer` as a control case: if the system lowers blindly before a following non-high vowel, the row breaks immediately. It does **not** provide a row-local origin story beyond that negative test.

### DEV_NOTES:line-5738-5792

- Source heading: `Test cases` / `Implementation successful (2026-03-09)`
- Source line hint: `Germanic/docs/DEV_NOTES.md:5738-5792`
- Fragment type: `shared_background_only`
- Status: `current`
- Issue tags: `positive_control`; `labial_blocking`; `implementation_result`; `current_rule`
- Recommended next use: `use_as_current_project_rule_state_not_as_lexeme_dossier`
- Shared-with rows if relevant: `1999 lid / hlid`; `2034 fright / fyrhte`; `2099 lick / liccian`; `2189 sieve / sife`; `2283 wether / weþer`

This later implementation block keeps `liver` in the test matrix after the rule was tightened. The test-case table says `liver | No | Yes (*b labial) | Block | lifer ✓`, and the results table keeps `*librō | lifer | lifer | lifer | ✓ No change (labial *b in coda)` [Germanic/docs/DEV_NOTES.md:5740-5748,5779-5787]. For this row, that is the clearest current project statement that the present system regards `lifer` as a successful blocked-lowering outcome rather than as an unresolved exception.

Still, the support remains shared and partly diagnostic. Much of the surrounding section is really about the broader onset-velar refinement that fixed other rows, not about `liver` itself [Germanic/docs/DEV_NOTES.md:5738-5792]. The row should therefore inherit only the locally relevant part: coda labial `*b` is treated as compatible with blocking, and `*librō` remained stable under the revised rule.

### DEV_NOTES:line-22650-22653

- Source heading: `Campbell §589.5` quotation inside the `soul / sāwol` note
- Source line hint: `Germanic/docs/DEV_NOTES.md:22650-22653`
- Fragment type: `diagnostic_primary_source_quote_embedded_in_shared_note`
- Status: `diagnostic_only`
- Issue tags: `parasitic_vowel`; `Campbell_quote`; `historical_background`; `not_current_protoform_policy`
- Recommended next use: `preserve_for_historical_background_only`
- Shared-with rows if relevant: `2201 soul / sāwol`

This is the only DEV_NOTES-embedded primary quotation that names OE `Lifer` directly in connection with parasite-vowel history: `"**Sāwol** soul (Gothic saiwala), and **Lifer** liver (OHG lebara), had syncopation of medial a in all cases (§ 341), but parasiting subsequently arose in nom. sg., though saul, sæwl also occur."` [Germanic/docs/DEV_NOTES.md:22650-22653]. It is worth preserving because it explains why `lifer` can serve as a historical comparator for later `-er/-ol` parasiting.

But for row 2108 this material is **diagnostic, not controlling**. The current row does **not** use a trisyllabic protoform with an overt medial `a`; it uses `*líbrō`, and the current trace reaches `lifer` through `*líβr > *líβer` [Germanic/data/germanic-aligned-final.tsv:690-690; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2952-2962]. So Campbell's quotation survives as historical background for the surface-type, not as direct authority for the live `PROTOFORM` string.

## Superseded or diagnostic material

- Earlier apocope diagnostics treated `*librō` as one of the remaining `*-ō` cases not solved by fixes aimed at `*-ą`; both the heavy-syllable apocope experiment note and the broader final-vowel apocope investigation list `*librō → librō (expected lifer)` among unresolved outputs [Germanic/docs/germanic_notes/heavy_syllable_apocope_experiment_results.md:49-62; Germanic/docs/germanic_notes/final_vowel_apocope_investigation.md:304-318]. Those notes are now diagnostic history only, because the current published OE trace does derive `lifer` successfully [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2943-2962].
- Campbell's `"syncopation of medial a"` quotation is still worth copying, but it is superseded as a literal description of the current pipeline input. Live row policy is `PROTO = PROTOFORM = *líbrō`, not an explicitly trisyllabic preform with medial `a` [Germanic/data/germanic-aligned-final.tsv:690-690; Germanic/docs/DEV_NOTES.md:22650-22653].
- There is still no row-specific packet, memo, or manifest scaffold to inherit. Later work should not mistake that absence for missing extraction; the row was mainly preserved in DEV_NOTES as a **diagnostic control for i-lowering**, not as a long lexeme dossier [Germanic/docs/lexeme_reports/coverage_audit.md:297-297; Germanic/docs/lexeme_reports/report_manifest.tsv:1-13].

## Open questions for later work

- If this row is ever literature-expanded, reconcile the current project rule (`coda labial *b blocks lowering`) with DEV_NOTES' own caution that this is stricter than Fulk's explicit account, even though `lifer` is one of the facts forcing the stricter analysis [Germanic/docs/DEV_NOTES.md:17411-17432,17466-17472].
- Decide whether Campbell's `Lifer ... had syncopation of medial a` should remain only as historical background for the `-er` surface type, or whether the row eventually needs an explicit note connecting that older philological description to the live `*líbrō` input [Germanic/docs/DEV_NOTES.md:22650-22653; Germanic/data/germanic-aligned-final.tsv:690-690].
- If later indexing work attaches DEV_NOTES fragments to this row, the safest anchors are the retained-`i` discussion and the shared i-lowering test matrices; there is no surviving dedicated `liver` subsection to cite instead [Germanic/docs/DEV_NOTES.md:5352-5424,5738-5792,17397-17472].
