# Research memo — 2202 span / spannan

## Starting point

- **ID:** 2202
- **CONCEPT:** span
- **COUNTERPART:** spannan
- **PROTO:** `*spánnaną`
- **PROTOFORM:** `*spánnaną`
- **DERIVATION_CLASS:** `regular`
- **NOTE:** OE target: `spann -> spannan` (inf. of strong verb class VII; noun `spann` in `*spannō` row).

The live TSV already treats this as the **verb** row. The separate noun material now lives in row 2203 (`span / spanne`), so the packet has to be read with special care wherever old project history still talks about noun `spann`.

## Packet evidence assessment

- **Authoritative/current:** the live TSV row; the packet's compact derivation trace showing `*spánnaną -> spannan`; and the live FST lookup, which still returns `spannan` uniquely from `*spánnaną`.
- **Useful background:** the packet's preservation of the row note, because it shows why this regular verb row still needs a memo at all: it is mainly a disambiguation note against the separate noun row.
- **Stale or superseded:** the packet's inherited noun-oriented `DEV_NOTES` hits about `*spannō -> span/spanne` are row-2203 history, not evidence about row 2202 itself; likewise `Germanic/docs/germanic_notes/analogical_leveling_analysis.md` still preserves an older stage where this verb was wrongly treated as `*spannăną -> spann` and marked "needs investigation."
- **Irrelevant or misleading:** `old_english_wiktionary.tsv`'s `span -> spann` hit is noun/citation-form orientation only, not evidence that the verbal target here should be `spann`; and the packet's noun-row references can mislead if read as if they described the present verb row.

## Additional repo research

Checked beyond the packet:

- `Germanic/data/germanic-aligned-final.tsv` around rows 2202-2203.
- `Germanic/data/oe_known_problems.tsv`.
- `Germanic/docs/DEV_NOTES.md` at the noun-row sections around 13790-14030 and the current `§17.12` resolution at 28061-28135.
- `Germanic/docs/lexeme_reports/pilot/span.md` and `Germanic/docs/lexeme_reports/research_memos/2203-span-spanne.md` as background only.
- `Germanic/docs/germanic_notes/analogical_leveling_analysis.md` 136-151.
- Live OE FST lookups via `oe_paradigm_probe.py` and `oe_full_trace_report.py`.

Main findings from the extra check:

- No dedicated dossier or span-specific analysis file for the **verb** turned up beyond the packeted material and the stale analogical-leveling note.
- `oe_known_problems.tsv` has no entry for row 2202, so the project is not treating this as a live exception or unmodelled mismatch.
- Current repo-local validation is simple and positive: `*spánnaną -> spannan`.
- The noun row is now clearly row 2203 `spanne`, with its own late-analogy memo and pilot report, so row 2202 should not keep talking as if the noun row's target were still `spann`.

## Reconstruction and early-stage forms

This row needs a three-way distinction, even though two of the values coincide:

1. **Cognate-set proto / verbal lexeme headword:** TSV `PROTO` `*spánnaną`.
2. **Project derivational input:** TSV `PROTOFORM` `*spánnaną`.
3. **OE target represented by the row:** `spannan`, the Old English infinitive.

Unlike row 2203, there is no paradigm-cell substitution here. `PROTO` and `PROTOFORM` are identical because the project is modelling the verb directly at the infinitive level. The separate noun lexeme belongs to a different cognate set input (`*spannō`, with project-input `*spánnai` for row 2203), so the memo must keep the verb and noun analyses apart.

## Old English philology

Repo-local evidence supports a conservative reading: `spannan` is the intended **infinitive** of a strong class-VII verb, while `spann` belongs elsewhere in the project either as noun/citation-form orientation or as a non-infinitival verbal form. The packet's own note already points in that direction by glossing the row explicitly as "inf. of str.v. class VII."

Just as importantly, the extra repo checks did **not** produce an independent lexical-table attestation for `spannan`; the only lexical-table hit I found was noun-like `spann`. So the eventual final report should present `spannan` as the project's selected OE infinitive target supported by the live derivation, but it should avoid pretending that the repo's lexical tables themselves settle every philological detail beyond that.

## Project problem and solution

The live derivation is not the problem here: `*spánnaną -> spannan` already works and the row remains correctly labelled `regular`. The real project problem is **documentation drift**. Earlier project history briefly confused this verb with noun/preterite-looking `spann`, and the surviving TSV note still points readers to "noun `spann` in `*spannō` row" even though the current noun row is the separate `spanne` memo case.

The right project solution is therefore:

- keep the verb row itself unchanged as a regular infinitive mapping;
- keep the noun analysis in row 2203, not here; and
- tighten the row-2202 note so it disambiguates against the noun row without repeating stale noun-target wording.

## Paradigm probe

A paradigm probe is **not required** for row 2202. This row is not justified by a contrast between competing paradigm cells: TSV `PROTO` and `PROTOFORM` are the same, and the live FST already returns the target directly (`*spánnaną -> spannan`).

If the project later wants an optional verb-control probe, the only relevant extra cell would be a bare-stem or preterite comparator to show why `spann` is not the target of this row; but that is not needed for the final report workflow.

## Recommended final report

Recommend a short final report that says row 2202 is an ordinary inherited verb row: keep `PROTO`/`PROTOFORM` `*spánnaną`, identify `spannan` as the OE infinitive, and mention only briefly that older project history sometimes conflated this with noun/preterite-looking `spann`. The final report should not import the noun row's late-analogy argument except as a cautionary distinction.

## Data-change recommendations

- **TSV `PROTO`:** **no change recommended.** `*spánnaną` is the correct lexeme-level verbal proto.
- **TSV `PROTOFORM`:** **no change recommended.** The project input is correctly the same as `PROTO`.
- **TSV `COUNTERPART`:** **no change recommended.** `spannan` is the intended OE target.
- **TSV `DERIVATION_CLASS`:** **no change recommended.** This remains a regular row.
- **TSV `NOTE`:** **change recommended.** The current note's wording about "noun `spann` in `*spannō` row" is stale now that the separate noun row is row 2203 `spanne`. The note should be rewritten to say that row 2202 is the verbal infinitive and is distinct from the separate noun row, without naming obsolete noun-target wording as if it were current.
- **`oe_known_problems.tsv`:** **no change recommended.** This is not a live exception case.
- **DEV_NOTES/dossier text:** **no change required for this row.** Current `DEV_NOTES` material is mainly the noun-row history, and no dedicated dossier for the verb was found. If broader cleanup is undertaken, the stale `analogical_leveling_analysis.md` entry for `*spannăną -> spann` could be corrected, but that is background cleanup rather than a row-2202 data requirement.
