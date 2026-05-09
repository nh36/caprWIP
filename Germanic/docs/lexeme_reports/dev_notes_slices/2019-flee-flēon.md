---
row_id: 2019
concept: flee
counterpart: flēon
proto: *fléuxaną
protoform: *fléuxaną
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
  - Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2019 flee / flēon

## Current row state

- CONCEPT: `flee`
- COUNTERPART: `flēon`
- PROTO: `*fléuxaną`
- PROTOFORM: `*fléuxaną`
- DERIVATION_CLASS: `regular`
- Live TSV row: the current Old English row keeps `COUNTERPART = flēon`, `PROTO = PROTOFORM = *fléuxaną`, and `DERIVATION_CLASS = regular`; the source field is only the inherited-etymology placeholder, not a row-local explanatory note [Germanic/data/germanic-aligned-final.tsv:345-345].
- Coverage/infrastructure status: `coverage_audit.md` still marks row 2019 as having no packet, no research memo, no attached DEV_NOTES fragment, and no other report infrastructure, so this slice is standing in for otherwise missing row-local documentation [Germanic/docs/lexeme_reports/coverage_audit.md:242-242].
- Repo reference baseline: `old_english_wiktionary.tsv` simply gives `flee` / `flēon` as inherited (`template:inh`), again without any row-local warning or repair history [Germanic/data/old_english_wiktionary.tsv:84-84].
- Current derivational trace: the published debug snapshot already derives the live target without workaround — `*fléuxaną` > `*flēoxaną` (OE Diphthong Leveling) > `*flēoxan` (Heavy Syllable Nasal Apocope) > `*flēoxąn` (Secondary Nasalization) > `*flēoxan` (Weak Tail Reduction) > `*flēoan` (H Loss) > `*flēon` (Contraction) > `flēon` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1382-1401].

## Development-note summary

No standalone row-specific DEV_NOTES essay for `flēon` survives in the live repository. The usable DEV_NOTES material is instead a **shared implementation audit** on OE contraction, where this lexeme appears because it is the only current TSV case with the pattern `uxă` / `*fléuxăną` and therefore functions as a positive control for whether the special breve-sensitive contraction clauses are actually needed [Germanic/docs/DEV_NOTES.md:21629-21687]. That is real evidence, but it is mainly about rule ordering and tokenization, not about a larger philological dispute specific to row 2019.

The key point preserved there is narrow and important. DEV_NOTES says that although `*fléuxăną` looks like a simple-vowel-before-breve candidate on the surface, it "also reaches contraction as a diphthong because `éu` tokenises as the composite `{*éu}` which breaks to `{*ēo}`" [Germanic/docs/DEV_NOTES.md:21669-21671]. The same section then reports the regression check explicitly: after deleting all nine breve clauses from `OEContraction`, the mismatch count stayed unchanged and `fléuxăną → flēon ✓` still succeeded [Germanic/docs/DEV_NOTES.md:21673-21687]. For row 2019, that is the surviving project-level DEV_NOTES claim: `flēon` is not an exception bucket here, but one of the audit cases showing that ordinary breaking plus `h`-loss plus contraction already suffice.

This slice should therefore keep three distinctions clear. First, the row metadata and live trace use `*fléuxaną`, while the DEV_NOTES audit writes `*fléuxăną`; in context that looks like weak-tail/breve notation inside the contraction audit, not evidence for a different lexical preform [Germanic/data/germanic-aligned-final.tsv:345-345; Germanic/docs/DEV_NOTES.md:21654-21655,21669-21671; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1383-1395]. Second, `COUNTERPART = flēon` is both the live row target and the output of the current cascade [Germanic/data/germanic-aligned-final.tsv:345-345; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1384-1401]. Third, the support here is mostly shared and diagnostic: it confirms that the row behaves regularly inside the present sound-change pipeline, but it does **not** amount to a dedicated lexeme dossier on attestation, class morphology, or alternative OE target selection [Germanic/docs/DEV_NOTES.md:21629-21698; Germanic/docs/lexeme_reports/coverage_audit.md:242-242].

## Relevant DEV_NOTES fragments

### DEV_NOTES:21629-21687

- Source heading: `§17.10.9 — Phase 1c (Role 4) research findings: OEContraction breve clauses are fully redundant`
- Source line or section hint: `lines 21629-21687`
- Fragment type: `copied_shared_lexeme_fragment`
- Status: `current`
- Issue tags: `oe_contraction`; `breve_clause_audit`; `shared_positive_control`; `eu_to_eo`; `row_2019`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This is the only clearly relevant surviving DEV_NOTES fragment for row 2019, and it should be preserved in detail precisely because it is shared rather than lexeme-dedicated. DEV_NOTES sets up a technical hypothesis: the nine `{*V}{*ă}` clauses in `OEContraction` may be redundant, but the audit has to make sure no live TSV item really depends on them [Germanic/docs/DEV_NOTES.md:21629-21649]. The scan then reports a single potentially dangerous environment: `uxă         4  (only form: *fléuxăną — flee)` [Germanic/docs/DEV_NOTES.md:21650-21655]. In other words, `flee / flēon` is not being discussed here because it is aberrant in the lexicon; it is being discussed because it is the one row that could have exposed a bug in the contraction rule inventory.

DEV_NOTES then answers that concern directly. The note says that the "only simple-vowel-before-breve case in the TSV (`*fléuxăną`) also reaches contraction as a diphthong because `éu` tokenises as the composite `{*éu}` which breaks to `{*ēo}`" [Germanic/docs/DEV_NOTES.md:21669-21671]. The empirical check that follows is equally explicit: after the breve clauses were removed, "Total mismatches: 37 (unchanged)" and the retained success list includes `fléuxăną → flēon   ✓` [Germanic/docs/DEV_NOTES.md:21676-21687]. For this row, the fragment's substance is therefore concrete: the cascade does not need a special short-`ă` contraction clause to get `flēon`; the relevant input has already become diphthongal before contraction applies.

### DEV_NOTES:21688-21698

- Source heading: `§17.10.9 — Safety for future Role 1 migration`
- Source line or section hint: `lines 21688-21698`
- Fragment type: `copied_shared_lexeme_fragment`
- Status: `current`
- Issue tags: `future_rule_safety`; `tokenization`; `breaking_before_contraction`; `shared_policy`
- Recommended next use: `cite_if_future_contraction_changes_reopen_the_row`
- Shared with row IDs:

This short continuation matters because it explains why row 2019 is expected to stay stable even if the broader handling of inflectional `ă` changes later. DEV_NOTES says that after Role 1 migrates inflectional `ă → a`, no new simple `{*V}{*a}` contraction feeds should appear, first because no simple stem vowel appears before `x ă` in the TSV outside `*fléuxăną`, and second because `*fléuxăną` itself has composite `éu` that breaks to `ēo`, so "contraction sees a diphthong input regardless" [Germanic/docs/DEV_NOTES.md:21688-21695].

For row 2019 that is not new philology, but it is important project policy. It means the surviving DEV_NOTES support is not just a one-off successful test run; it is an explicit forward-looking claim that the row should remain regular under anticipated cleanup of weak-tail notation as well [Germanic/docs/DEV_NOTES.md:21688-21698]. If later note writers need to explain why `flēon` was not broken by contraction refactors, this is the fragment to quote.

## Superseded or diagnostic material

- No superseded row-specific DEV_NOTES dossier was located for `flēon`. `coverage_audit.md`'s `none` entry appears accurate: there was no packet, no memo, and no pre-existing attached fragment to inherit here [Germanic/docs/lexeme_reports/coverage_audit.md:242-242].
- The published derivation snapshot is diagnostic rather than DEV_NOTES material, but it is still the clearest current-state companion for this row. It shows that the live grammar already reaches `flēon` by ordinary stages — diphthong leveling, apocope/nasal adjustments, `h`-loss, and contraction — with no exception rule and no manual target swap [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1382-1401].
- The DEV_NOTES breve spelling `*fléuxăną` should not be over-read as a distinct comparative reconstruction. In the row metadata and current trace, the form is `*fléuxaną`; inside DEV_NOTES, the breve appears specifically within the contraction audit's discussion of `{*V}{*ă}` feeds [Germanic/data/germanic-aligned-final.tsv:345-345; Germanic/docs/DEV_NOTES.md:21631-21633,21650-21655,21669-21671]. The safest replacement note is therefore to quote the DEV_NOTES spelling when discussing that audit, while keeping the row's own `PROTO` / `PROTOFORM` fields unchanged.

## Open questions for later work

- If a later lexeme report needs more than implementation history, check whether the repo contains a better primary-source or handbook citation for the OE verb `flēon` than the current inherited-template placeholder in `old_english_wiktionary.tsv` [Germanic/data/old_english_wiktionary.tsv:84-84].
- Decide whether future reporting should normalize DEV_NOTES' audit spelling `*fléuxăną` to the row's `*fléuxaną` in prose, or preserve the breve whenever the argument is specifically about the old `{*V}{*ă}` contraction clauses [Germanic/docs/DEV_NOTES.md:21629-21698; Germanic/data/germanic-aligned-final.tsv:345-345].
- If index-level lexeme-report infrastructure is expanded later, decide whether row 2019 should stay a slice built from shared contraction-audit material only, or whether a dedicated memo is needed on the verb's attestation and comparative lexical support. The present evidence is enough for implementation history, but thin for a full philological dossier [Germanic/docs/lexeme_reports/coverage_audit.md:242-242; Germanic/docs/DEV_NOTES.md:21629-21698].
