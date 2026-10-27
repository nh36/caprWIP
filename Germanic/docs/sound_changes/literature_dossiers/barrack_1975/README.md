# Barrack (1975) — source-critical dossier

Charles M. Barrack, *A Diachronic Phonology from Proto-Germanic to Old
English Stressing West-Saxon Conditions* (Janua Linguarum, Series
Practica 144; The Hague and Paris: Mouton, 1975). Bibliographic key:
`Barrack1975` in `docs/refs.bib`; local holding documented in
`docs/references/barrack_1975/` (scan is local-only and never
committed). DOI of the De Gruyter Mouton reprint: 10.1515/9783110873511.

This dossier is the adjudicable register produced by the first Barrack
engagement (visual rule census + bibliographic integration). It makes
no FST, chronology, or corpus changes. Per-SC adjudications that draw
on Barrack require separate authorization and their own audit records
under `Germanic/docs/sound_changes/audits/`.

## Files

| File | Contents |
| --- | --- |
| `rule_census.tsv` | 231 rule headings transcribed visually from printed pp. 38–127, one row per heading, with change summary, conditioning, dialect/geography, exceptions, cited word forms, ordering claims, and legibility grade. Second-pass QC against 300 dpi renders completed; see `quality_control_report.md`. |
| `ocr_reconciliation.tsv` | Disposition of all 211 OCR heading candidates (208 `VERIFIED_ON_PAGE`, 1 `RELOCATED`, 2 `FALSE_POSITIVE`) plus 23 headings present in print but missing from the OCR list (`ADDED_BY_VISUAL_CENSUS`). Printed "PG 311.4a" (p. 77) is the book's own misprint for 331.4a (`VERIFIED_PRINT_MISPRINT`). |
| `capr_crosswalk.tsv` | 97-row crosswalk from CAPR reader entries (all five chapters) to Barrack rule loci. Every row is tranche-derived and pending per-SC adjudication; none is a finding. |
| `barrack_to_capr.tsv` | Complete reverse index: all 231 Barrack headings dispositioned against CAPR with a controlled classification (EQUIVALENT_REPRESENTED / REPRESENTED_DIFFERENT_CONDITIONING / PARTIALLY_REPRESENTED / PLAUSIBLE_MISSING / ALTERNATIVE_ACCOUNT / FORMAL_NOT_HISTORICAL / OUT_OF_SCOPE / HISTORICALLY_DOUBTFUL / UNRESOLVED), confidence, and recommended disposition. 38 rows remain visibly `UNRESOLVED`; nothing is silently classified as covered. |
| `citation_ledger.tsv` | Per-SC citation placement ledger, fully reconciled: 12 `CITED_OK` (page-precise citations already in reader prose), 23 `CITE_WARRANTED`, 32 `CHAPTER_LEVEL`, 24 `NO_CITATION_NEEDED` (with reasons), 6 `DEFER_TO_ADJUDICATION`. |
| `quality_control_report.md` | Second-pass QC findings: substantive description errors corrected (331.6a, 404b/c/d, 400z, 406, 409, 422, 475b, 480.1), propagation audit, 600 dpi p. 136 chart re-read, remaining uncertainty, and backlog changes. |
| `research_agenda.md` | Evidence-ranked queue of the remaining Barrack-related investigations, prepared after the SC087 adjudication (RETAIN); names the SCs, Barrack rules, diagnostic lexemes and required tests per item. |

## How to read Barrack's apparatus

Rule numbers are keyed to the paragraph numbering of Campbell's *Old
English Grammar*, which Barrack names as his principal data source
(p. 21 n. 4); they are reference anchors, not a chronology. Prefixes
mark the dialect stratum of a rule (PG, NWG, WG, Ing.). A `z` suffix
flags a rule that departs from Campbell's account (e.g. 129za, 331.1z);
`n` plus a digit points at a Campbell footnote (e.g. 305n2). Rules are
stated as feature-matrix rewrite rules over "quasi-phonemes"
(pp. 11–15, 24), each typically presented as (I) a glyph-level change,
(II) the feature-matrix formulation, and (III) ordering and residue
discussion.

Reading guide: methodology pp. 11–37; the diachronic rules pp. 38–127;
Input Index (rule numbers) pp. 128–131; Word Index pp. 132–134;
bibliography p. 135; summary ordering chart p. 136.

## Methodological assessment

Three features of Barrack's method matter for CAPR and must not be
imported silently.

1. *Free variation phases.* Barrack models each change as a window of
   overlapping primary and secondary phases rather than an instant
   (pp. 21–23); his example is the overlap of retraction (143a) and
   breaking (143b) yielding attested *æll*/*all*/*eall* variation.
   CAPR's transducers are categorical; where Barrack's phase overlap
   is the substance of a claim, a CAPR adjudication must restate it as
   relative ordering plus conditioning, with corpus witnesses.
2. *Progressive Environment Simplification (PES).* Barrack holds that
   rules persist and progressively lose environmental restrictions
   (pp. 23–25); rule 320 (*weor-* > *wur-*, pp. 75–76) is his showcase.
   PES is a diachronic claim about rule life-cycles, not a licence for
   under-specified conditioning in CAPR rules.
3. *Formal, not chronological, ordering.* Barrack is explicit that
   ordering between rules "only implies a logical relationship—in no
   sense a chronological relationship" (p. 34); external (real-time)
   and internal (formal) ordering are developed separately
   (pp. 26–30), with transitivity closing the chart (pp. 36–37) and a
   worked residual-reversal example (*heolap*, 210 > 355.5, p. 36).
   Consequently the p. 136 chart and any "A before B" statement in the
   rules must never be promoted directly into CAPR chronology edges;
   each needs independent conditioning/witness evidence under the
   research adjudication protocol.

Scope: Barrack treats West Saxon to the beginning of the eleventh
century (p. 19). Claims about other dialects are incidental and flagged
in the census `dialect_geography` column.

CAPR does not adopt Barrack's feature matrices or quasi-phoneme
inventory; the census records the glyph-level statement (I) as primary
and keeps matrix detail only in summary form.

## Coverage certificate

- Pages rendered and read: printed pp. 19–136 (sheet N = printed
  page N in the local scan, SHA-256 verified against the holding
  manifest).
- Rule-heading census: printed pp. 38–127, read page by page in nine
  overlapping tranches with verified continuity across every tranche
  boundary. 231 distinct headings; no duplicates.
- OCR reconciliation: all 211 machine candidates dispositioned; OCR
  "311.4a" is printed 331.4a (p. 77); OCR "425" and "795" are
  artifacts with no heading on the page; 23 printed headings were
  absent from the OCR list and are census-only.
- Index cross-check: Word Index (pp. 132–134) re-read at 300 dpi; the
  apparent citations of rules "309" and "344" are misreadings of
  *meolc* 390 and of 444/434 respectively; every index rule number
  checked resolves to a census heading (including *meord* 139zc).
- Known legibility limits: pp. 38–47 carry dense feature matrices and
  several census rows there are graded PARTIAL (glyph-level statements
  are secure; matrix internals are not). The p. 136 ordering chart was
  re-read at 600 dpi: perimeter labels and rim-adjacent arcs are now
  legible, but the interior chords remain unresolvable, so no ordering
  edge has been inferred from the chart (see
  `quality_control_report.md` §3), and chart edges would in any case
  still have to clear the no-chronology-from-ordering rule above.

## Status and next steps

Workstream A (census) and Workstream B (bibliography, navigation,
chapter-intro context, targeted reader citations) are complete on this
branch, and the second-pass QC, complete reverse index, and citation
reconciliation are recorded in this dossier. The authorized first
per-SC adjudication is SC087 (r-metathesis) against Barrack 459.1/459.3
(pp. 115–117); its record lives under
`Germanic/docs/sound_changes/audits/`. Subsequent research items are
queued from `barrack_to_capr.tsv` dispositions (`RESEARCH_QUEUE`,
`VERIFY_SOURCE`) and the `CITE_WARRANTED`/`CHAPTER_LEVEL` ledger rows.
