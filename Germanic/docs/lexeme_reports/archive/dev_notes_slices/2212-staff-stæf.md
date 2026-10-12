---
row_id: 2212
concept: staff
counterpart: stæf
proto: *stábiz
protoform: *stábaz
derivation_class: early_analogy
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file: Germanic/docs/lexeme_reports/packets/2212-staff-stæf.md
linked_research_memo_file: Germanic/docs/lexeme_reports/research_memos/2212-staff-stæf.md
linked_dossier_or_analysis_files:
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2212 staff / stæf

## Current row state

- The live OE row currently reads `CONCEPT = staff`, `COUNTERPART = stæf`, `PROTO = *stábiz`, `PROTOFORM = *stábaz`, `DERIVATION_CLASS = early_analogy` [Germanic/data/germanic-aligned-final.tsv:1094-1094].
- The row therefore already keeps the comparative headword and the row-specific modelling input distinct: `PROTO` is still the cognate-set label `*stábiz`, while `PROTOFORM` is the OE-facing derivational input `*stábaz` [Germanic/data/germanic-aligned-final.tsv:1094-1094].
- The live TSV note is explicit about why the split exists: “Kroonen: `*staba-` m. ‘staff; letter’ (a-stem). OE `stæf` has `æ` (not `e`), ruling out i-stem `*-iz`. Using a-stem `*stabăz`.” [Germanic/data/germanic-aligned-final.tsv:1094-1094].
- `oe_known_problems.tsv` currently has no row-specific entry for `2212`, for `staff`, for `stæf`, or for `*stábiz`.

## Detailed development-note summary

The durable row-level point in DEV_NOTES is not that Proto-Germanic has been definitively settled as an a-stem across the whole comparative record. The durable point is narrower and stronger: a straight OE derivation from i-stem `*stabiz` is incompatible with the target `stæf`. DEV_NOTES opens the shared `cræft / stæf` note with the concrete mismatch table: old TSV `*stabiz` yielded `stefe`, but the expected OE form is `stæf` [DEV_NOTES:line-4689-4703]. That remains the controlling phonological fact for row `2212`: if the English cascade sees `*-iz`, it predicts i-umlaut and the wrong vowel.

DEV_NOTES is still useful because it preserves the comparative disagreement instead of flattening it. For `*stab-`, Kroonen gives `*staba- m.` and cites “OE stæf” as an a-stem [@Kroonen2013, p. 469], while Orel gives `*stabiz ~ *stabaz` [@Orel2003, p. 378], and Kluge-Seebold gives `g. *stabi-/a-` with “ae. stæf” [@KlugeSeebold2011, s.v. Stab]. DEV_NOTES correctly highlights the important wording here: “Kluge-Seebold explicitly marks uncertainty with the notation `*stabi-/a-`” [DEV_NOTES:line-4724-4732]. That uncertainty is still part of the row history and is the main reason the live row should continue to distinguish `PROTO` from `PROTOFORM` rather than pretending the comparative question is closed.

What survives as current policy is the phonological comparison. DEV_NOTES states that i-stem `*stabiz` would front `*a` and then raise `æ > e`, predicting OE `stefe`, whereas a-stem `*stabăz` fronts the root vowel but does not create either an i-umlaut trigger or a valid a-restoration trigger, predicting OE `stæf` [DEV_NOTES:line-4734-4758]. For row `2212`, that is the decisive argument: the OE target with `æ` excludes a direct inherited `*-iz` input, so the English derivation must be fed from an a-stem-style form even if comparative lexicography leaves the wider stem class open [@Orel2003, p. 378; @Kroonen2013, p. 469].

The live row is now more conservative than the original DEV_NOTES update, and the slice needs to preserve that chronology explicitly. DEV_NOTES originally instructed that both `PROTOFORM` and `PROTO` be rewritten from `*stabiz` to `*stabăz` [DEV_NOTES:line-4806-4810]. The live TSV no longer follows that instruction literally. Instead, it keeps `PROTO = *stábiz` as the comparative label while using `PROTOFORM = *stábaz` as the modelling input [Germanic/data/germanic-aligned-final.tsv:1094-1094]. That split is not accidental drift; it is the current project solution to the comparative-versus-derivational tension.

The OE side is firmer than the PGmc morphology. DEV_NOTES' attestation block includes Luick's `stæf 'Stab', cræft 'Kraft'` among the handbook examples with `æ` [DEV_NOTES:line-4785-4795; @Luick1914, p. 176]. A later DEV_NOTES chronology note quotes Ringe-Taylor's derivation `PGmc *stabaz 'staff, letter' … > PWGmc *stab … > OE stæf`, then adds the project-level clarification that stressed monosyllabic `*á` “does undergo AFB word-finally” in this environment [DEV_NOTES:line-22099-22155; @RingeTaylor2014, §3.1.2]. That matters because it shows that once the row is modelled with an a-stem-style input, the remaining derivation to `stæf` is not an ad hoc exception but a regular stressed-monosyllable fronting outcome after earlier apocope.

Later debugging history is also worth keeping, because it records the main wrong turn after the row had already been converted away from `*stabiz`. A later regression note logs `stabăz → staf (should be stæf)` and then rejects the attempted overbroad A-restoration fix [DEV_NOTES:line-9529-9568]. The preserved handbook quote is useful and should stay visible: “Unstressed `*a` was nasalized, and therefore not fronted, only if it was followed by a nasal in the syllable coda” [DEV_NOTES:line-9557-9560; @RingeTaylor2014, p. 153]. For `*stab.ăz`, there is no such coda nasal, so fronting to `stæf` remains the right prediction. That diagnostic note is not lexical authority on its own, but it is the clearest in-repo statement of why row `2212` belongs under `early_analogy` rather than under an unresolved OE-rule exception bucket.

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-4689-4783

- Source heading: `stem-class disagreement and modelling choice for cræft / stæf`
- Source line or section hint: `lines 4689-4783`
- Fragment type: `lexeme_specific`
- Status: `current`
- Issue tags: `stem_class`; `protoform_vs_proto`; `early_analogy`; `i_umlaut`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs: `1981`

This is the main surviving authority for row `2212`. DEV_NOTES first states the mismatch plainly: old TSV `*stabiz` produced `stefe`, but the expected OE form is `stæf` [DEV_NOTES:line-4696-4703]. It then surveys Kroonen, Orel, and Kluge-Seebold to show that the stem-class disagreement is real, not a typo in the old row [DEV_NOTES:line-4724-4732; @Kroonen2013, p. 469; @Orel2003, p. 378; @KlugeSeebold2011, s.v. Stab]. The crucial phonological contrast follows immediately: i-stem `*stabiz` predicts `stefe`, while a-stem `*stabăz` predicts `stæf` [DEV_NOTES:line-4738-4758]. What should be carried forward is the modelling consequence, not the older suggestion that comparative `PROTO` itself had to be rewritten.

### DEV_NOTES:line-4785-4795

- Source heading: `OE attestation for stæf / cræft and warning against later English back-projection`
- Source line or section hint: `lines 4785-4795`
- Fragment type: `bibliography_or_source_audit_for_lexeme`
- Status: `current`
- Issue tags: `oe_attestation`; `handbook_quote`; `oe_vowel`; `later_english_history`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs: `1981`

This short attestation fragment is worth keeping because it anchors the OE target itself. DEV_NOTES includes Luick's `stæf 'Stab', cræft 'Kraft'` among the examples that show OE `æ` [DEV_NOTES:line-4791-4791; @Luick1914, p. 176]. The same block warns that later English `staff` with `a` belongs to later history, not to the OE stage [DEV_NOTES:line-4794-4795]. For row `2212`, that chronological warning matters: the slice should preserve OE `stæf` as the row target without letting later ModE spelling weaken the vowel argument.

### DEV_NOTES:line-4806-4810

- Source heading: `original row-2212 TSV rewrite instruction`
- Source line or section hint: `lines 4806-4810`
- Fragment type: `superseded_or_diagnostic_for_lexeme`
- Status: `superseded`
- Issue tags: `row_update`; `protoform_vs_proto`; `project_history`
- Recommended next use: `use_to_explain_superseded_analysis`
- Shared with row IDs:

This fragment matters because it records the original project action taken after the stem-class review. DEV_NOTES instructed the team to change both `PROTOFORM` and `PROTO` from `*stabiz` to `*stabăz` and rewrote the row note accordingly [DEV_NOTES:line-4806-4810]. That is no longer the exact live policy. The current row keeps the same phonological conclusion — use `*stábaz` as the modelling input — but no longer lets that modelling input erase the comparative headword in `PROTO` [Germanic/data/germanic-aligned-final.tsv:1094-1094]. The fragment should therefore stay visible as project chronology, but it is superseded for row-state purposes.

### DEV_NOTES:line-22099-22155

- Source heading: `R/T chronology note on word-final *a and monosyllabic fronting`
- Source line or section hint: `lines 22099-22155`
- Fragment type: `phenomenon_context_for_lexeme`
- Status: `current`
- Issue tags: `chronology`; `apocope`; `AFB`; `stressed_monosyllable`
- Recommended next use: `keep_as_general_background`
- Shared with row IDs:

This later chronology fragment is not the source of the stem-class decision, but it is directly useful background for `stæf`. DEV_NOTES quotes Ringe-Taylor's sequence `PGmc *stabaz 'staff, letter' … > PWGmc *stab … > OE stæf` and uses it to argue that loss of final short `*a` precedes OE/Ingvaeonic fronting [DEV_NOTES:line-22104-22120; @RingeTaylor2014, §3.1.2]. The follow-up clarification is the reusable point for this row: stressed `*á` in monosyllables like `*stab` still fronts word-finally, so `stæf` is compatible with the chronology once the pre-OE input has been normalized away from i-stem `*-iz` [DEV_NOTES:line-22151-22155]. This is best kept as background, not as the primary row-policy fragment.

### DEV_NOTES:line-9529-9568

- Source heading: `rejected A-restoration broadening and the staff regression`
- Source line or section hint: `lines 9529-9568`
- Fragment type: `superseded_or_diagnostic_for_lexeme`
- Status: `diagnostic_only`
- Issue tags: `debug_history`; `a_restoration`; `fronting`; `regression`
- Recommended next use: `use_as_project_history_only`
- Shared with row IDs: `1981`

This later debugging fragment is not the source of the lexical decision, but it preserves the main post-resolution failure state for the row. DEV_NOTES logs the regression `stabăz -> staf (should be stæf)` and then rejects the attempted global fix that would make all following `*ă` trigger A-restoration [DEV_NOTES:line-9529-9553]. The row-relevant payoff comes from the Ringe-Taylor quotation immediately after it: “Unstressed `*a` was nasalized, and therefore not fronted, only if it was followed by a nasal in the syllable coda” [DEV_NOTES:line-9557-9560; @RingeTaylor2014, p. 153]. For `*stab.ăz`, no such nasal blocker exists, so the correct outcome remains `stæf`, not `staf`.

## Superseded or diagnostic material

Two older project states need to remain visible but subordinate. First, the March 2026 DEV_NOTES update correctly recognized that the English derivation cannot run from direct i-stem `*stabiz`, but it overshot by recommending that `PROTO` itself be rewritten to `*stabăz` rather than keeping a comparative headword / modelling-input split [DEV_NOTES:line-4806-4810]. Second, the later regression note `stabăz -> staf` belongs to implementation history, not to the row's live OE variation set [DEV_NOTES:line-9529-9568]. It preserves a useful diagnostic principle, but `staf` is a bad output, not an alternate target for this row.

The other caution is source hygiene. DEV_NOTES is reliable on the core phonological contrast and on the comparative stem-class disagreement, but later report writing should still verify exact dictionary phrasing from the cited reference extracts if the final report wants to lean heavily on Kroonen, Orel, or Kluge-Seebold wording. The slice can safely preserve the disagreement and the project decision now; it does not need to overclaim that the broader PGmc morphology has been conclusively settled.

## Open questions for later work

- In the final lexeme report, explain explicitly that live `PROTO` and live `PROTOFORM` now diverge on purpose: comparative headword `*stábiz` versus modelling input `*stábaz`.
- If the final report quotes comparative lexicography directly, verify the exact wording from the source extracts rather than relying only on the DEV_NOTES table, especially for how Orel and Kluge-Seebold encode the uncertainty.
- If index rows are later added, the strongest anchors are the shared stem-class fragment (`4689-4783`), the OE-attestation fragment (`4785-4795`), the superseded row-update fragment (`4806-4810`), and the diagnostic regression fragment (`9529-9568`). The chronology note at `22099-22155` is useful background but is secondary.
