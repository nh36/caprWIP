---
row_id: 2024
concept: fodder
counterpart: fōdor
proto: "*fōdrą"
protoform: "*fōdrą"
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
  - Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md
  - Germanic/docs/germanic_notes/final_vowel_apocope_investigation.md
  - Germanic/docs/analysis/arestoration_r_l_research.md
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2024 fodder / fōdor

## Current row state

- CONCEPT: `fodder`.
- COUNTERPART: `fōdor`.
- PROTO: `*fōdrą`.
- PROTOFORM: `*fōdrą`.
- DERIVATION_CLASS: `regular`.
- Live TSV row: row `2024` currently keeps Old English `fōdor` for concept `fodder`, with `PROTO`/`PROTOFORM` both `*fōdrą`; the source field is explicitly textual and says `Source: Wiktionary etymology (Wiktionary etymology bullet (fodder → Old English fōdor))`, so the present row is attached to an attested OE lemma rather than to a reconstructed placeholder [Germanic/data/germanic-aligned-final.tsv:364-364].
- Upstream data-population context: `old_english_wiktionary.tsv` likewise records `fodder → fōdor` as a `text` mapping rather than an inherited-template scrape, matching the live row's source note and confirming that this pair came through a manual/etymology-based population path [Germanic/data/old_english_wiktionary.tsv:365-365].
- Report infrastructure status: `coverage_audit.md` still marks row `2024` as `regular` with no packet, no memo, no attached slice, and `none` under the current infrastructure columns; `report_manifest.tsv` has no row-2024 entry either, so there is no pre-existing packet stem to reuse and the canonical filename `2024-fodder-fōdor.md` is appropriate here [Germanic/docs/lexeme_reports/coverage_audit.md:246-246; Germanic/docs/lexeme_reports/report_manifest.tsv:1-14].
- Known-problems status: no row-specific exception entry exists in `oe_known_problems.tsv`, so the current repository does not treat `*fōdrą > fōdor` as a known modelling failure or exception bucket [Germanic/data/oe_known_problems.tsv:1-8].
- Current derivational behaviour: the published OE trace already lands on the live target without repair logic, showing `Proto Input: *fōdrą`, then `OE Heavy Syllable Nasal Apocope: *fōdr`, then `OE Epenthetic Vowel: *fōdor`, with `EXPECTED: fōdor` and `OUTPUTS: fōdor` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1483-1502].

## Development-note summary

No substantial row-local DEV_NOTES dossier for `fodder / fōdor` survives in the live repository. The only direct row mention in `DEV_NOTES.md` is operational rather than philological: during the Old English population pass the project records that it “annotated `fodder fōdor` ... manually,” which means the present OE counterpart was not one of the fully automatic inherited-template fills [Germanic/docs/DEV_NOTES.md:2392-2395]. That point matters because it explains why the row's source note is textual/Wiktionary-based rather than a more formulaic inherited citation [Germanic/data/germanic-aligned-final.tsv:364-364; Germanic/data/old_english_wiktionary.tsv:365-365].

Beyond that operational note, the support for row 2024 is mostly shared phonological/diagnostic material, and the slice should say so plainly. The archived heavy-syllable nasal-apocope note in `DEV_NOTES.md` argues that proto `*-ą` was empirically being deleted after heavy stems in Old English, even though the team did not initially have an explicit literature statement for that exact extension [Germanic/docs/DEV_NOTES.md:1591-1645]. The linked investigation file then names `*fōdrą` as one of the heavy long-vowel stems and explicitly lists the pre-fix output `*fōdrą → fōdra (exp. fōdor)` [Germanic/docs/germanic_notes/final_vowel_apocope_investigation.md:148-150,282-282]. In other words, the current row is not supported by a bespoke lexeme essay; it is supported by a thin but coherent combination of manual OE lemma attachment plus shared phonological work that now yields the expected `fōdor` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1483-1502].

A second caution is that some repo-local diagnostic material preserves a late West Saxon variant-looking form `*foddor`, not the row's current target `fōdor`. The A-restoration research file quotes Campbell on forms such as “lW-S *hlǣdder* ladder, *foddor* fodder, *mēddor* mother ... (all after infl. forms)” [Germanic/docs/analysis/arestoration_r_l_research.md:89-97]. That quotation is useful because it shows that `fodder` participates in a broader analogical/gemination discussion elsewhere in the literature, but it should not be silently substituted for the current row. Row 2024 is presently keyed to attested `fōdor`, with no row-level note saying that the counterpart should be changed to `foddor` or that the regular-class derivation is in doubt [Germanic/data/germanic-aligned-final.tsv:364-364].

## Relevant DEV_NOTES fragments

### DEV_NOTES:2392-2395

- Source heading: `Old English data population`
- Source line or section hint: `2025-12-12`, lines `2392-2395`
- Fragment type: `row_specific_operational_note`
- Status: `current`
- Issue tags: `manual_annotation`; `attested_lemma_population`; `source_provenance`
- Recommended next use: `preserve_as_row_provenance`
- Shared with row IDs: 2024

This is the only direct, row-specific DEV_NOTES fragment now surviving for `fodder / fōdor`, so it needs to be copied into the replacement slice rather than hand-waved away. DEV_NOTES says: “Ran the helper across all 376 English concepts so the Old English rows now have attested lemmas (373 entries auto-filled; annotated `fodder fōdor` and `tongs tange` manually, marked `knob` as lacking an OE cognate per the etymology)” [Germanic/docs/DEV_NOTES.md:2393-2394]. For row 2024, the important content is not an extended sound-change argument but the provenance claim: `fōdor` was intentionally inserted as a manual OE lemma match during data population, and the live TSV's textual source note is the downstream reflection of that decision [Germanic/data/germanic-aligned-final.tsv:364-364; Germanic/data/old_english_wiktionary.tsv:365-365].

### DEV_NOTES:1591-1645

- Source heading: `Archived: Heavy Syllable Nasal Apocope (2026-02-06) — EMPIRICAL DISCOVERY`
- Source line or section hint: `lines 1591-1645`
- Fragment type: `shared_phonology_fragment`
- Status: `current_but_shared`
- Issue tags: `heavy_syllable_nasal_apocope`; `shared_support_only`; `regular_derivation`
- Recommended next use: `cite_when_explaining_regular_output`
- Shared with row IDs:

This fragment does not mention `fōdor` by name, but it is the main surviving DEV_NOTES material that explains why row 2024 can remain `regular`. DEV_NOTES summarizes an archived empirical finding: after heavy stems, proto `*-ą` was being deleted in Old English, yielding a major reduction in spurious final-vowel outputs; the note states that “the same heavy/light conditioning that applied to *-i/*-u also applied to *-ą” in the project's modelling, even though the team did not yet have that extension explicitly formulated in its literature base [Germanic/docs/DEV_NOTES.md:1595-1615]. For `*fōdrą`, that matters because the stem is heavy by vowel quantity, so deletion of final `*-ą` is precisely the step that prevents non-target `*fōdra` and allows the regular cascade to reach `fōdor` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1492-1502].

The linked investigation named by DEV_NOTES makes the row-level relevance explicit. It lists `*fōdrą` among the “60 'HEAVY' cases” and later gives the concrete diagnostic line `*fōdrą → fōdra (exp. fōdor)` [Germanic/docs/germanic_notes/final_vowel_apocope_investigation.md:148-150,282-282]. That diagnostic predates the current successful trace, but together the files show the same story: row 2024 relies mainly on shared heavy-stem apocope work, not on a lexeme-specific exception narrative.

### DEV_NOTES:no-exact-fodder-philology-section

- Source heading: no dedicated `fodder` / `fōdor` subsection survives in `DEV_NOTES.md`
- Source line or section hint: direct hits are limited to line `2394` plus the shared apocope note at `1591-1645`
- Fragment type: `negative_result`
- Status: `current`
- Issue tags: `missing_row_specific_authority`; `shared_not_row_local`; `keep_conservative`
- Recommended next use: `do_not_overstate_row_history`
- Shared with row IDs:

The negative result is itself important enough to preserve. A direct repository search does not recover a dedicated DEV_NOTES argument about whether OE `fōdor` is reconstructed, attested, analogically remodelled, or in need of a different proto input; instead, the row survives on one operational population note and one shared phonology note [Germanic/docs/DEV_NOTES.md:1591-1645,2392-2395]. This slice should therefore resist turning row 2024 into a bigger controversy than the repo actually documents. The current row is well supported enough to stay live, but the support is mostly generic/shared rather than a bespoke `fodder` dossier [Germanic/docs/lexeme_reports/coverage_audit.md:246-246].

## Superseded or diagnostic material

- `coverage_audit.md` is diagnostic bookkeeping, not philological argument. Its `none` entry for row `2024` should be read literally: before this slice, the repo had no packet, memo, or attached DEV_NOTES extraction for `fōdor` [Germanic/docs/lexeme_reports/coverage_audit.md:246-246].
- The final-vowel investigation preserves an older pre-fix failure state — `*fōdrą → fōdra (exp. fōdor)` — and is useful exactly because it explains what had to be fixed in the shared OE pipeline; it is not evidence that the current row should now be normalized to `fōdra` [Germanic/docs/germanic_notes/final_vowel_apocope_investigation.md:282-282].
- The published derivation trace is likewise diagnostic rather than a DEV_NOTES fragment, but it is the cleanest implementation check available: the current cascade already derives `fōdor` from `*fōdrą` through heavy-syllable nasal apocope plus epenthetic vowel insertion, with no exception handling [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1483-1502].
- The Campbell quotation preserved in repo-local A-restoration research should be handled conservatively. It records a late West Saxon-looking form in a list of analogically influenced words: “... lW-S *hlǣdder* ladder, *foddor* fodder, *mēddor* mother, *tēddor* progeny, (all after infl. forms) ...” [Germanic/docs/analysis/arestoration_r_l_research.md:89-97]. That is valuable comparative material for later variant work, but in the current row it is only diagnostic. The live counterpart remains `fōdor`, and no row-local note yet says to elevate `*foddor` into the TSV target [Germanic/data/germanic-aligned-final.tsv:364-364].

## Open questions for later work

- Should row 2024 eventually gain a stronger lexicographic citation than the present Wiktionary-derived text note, or is the current manual-attestation provenance already sufficient for a regular row [Germanic/data/old_english_wiktionary.tsv:365-365; Germanic/docs/DEV_NOTES.md:2392-2395]?
- Should the late West Saxon-looking `*foddor` material be captured somewhere as a variant/diagnostic note for the lexeme family, or is it better left attached only to broader analogical/gemination research until a row-specific need appears [Germanic/docs/analysis/arestoration_r_l_research.md:89-97]?
- If later indexing work wants row 2024 represented in broader DEV_NOTES infrastructure, should it be indexed under shared heavy-stem `*-ą` apocope evidence rather than under a non-existent row-local controversy [Germanic/docs/DEV_NOTES.md:1591-1645; Germanic/docs/lexeme_reports/coverage_audit.md:246-246]?
