# Research memo — 2234 swallow / swealwe

## Starting point

- **ID:** 2234
- **CONCEPT:** swallow
- **COUNTERPART:** swealwe
- **PROTO:** *swálwōn
- **PROTOFORM:** *swálwōn
- **DERIVATION_CLASS:** regular
- **NOTE:** Kroonen *swalwōn- f. ‘swallow (bird)’ → OE swealwe f.; **swelgan** is the verb ‘to swallow’.

The live row already reflects the important project correction: the bird-name row uses proto *swalwōn-, not the verb etymon *swelganą and not the earlier erroneous *swalgwōn.

## Packet evidence assessment

**Authoritative/current:** the live TSV row; the compact derivation trace showing *swálwōn → swealwe; the analysis probe in `arestoration_r_l_research.md` confirming `swálwōn -> swealwe`; and the DEV_NOTES correction that removed the spurious *g from the proto.

**Useful background:** the widuwe dossier material on `swaluwe > swalewan`, because it shows that later parasite-vowel/lowering forms with `-uw-/-ew-` exist for this lexeme family and that `*w` does not block medial unstressed `u`-lowering.

**Stale or superseded:** DEV_NOTES passages citing `*swalgwōn -> swealgwe` are diagnostic history only; they document the old error, not the current row.

**Irrelevant or misleading:** the packet's `old_english_wiktionary.tsv` hit (`swallow -> swelgan`) is a gloss-level collision with the verb ‘to swallow’, not evidence against OE **swealwe** for the bird.

## Additional repo research

Beyond the packet I checked:

- `Germanic/docs/DEV_NOTES.md` around the original correction and later `widuwe` discussion.
- `Germanic/docs/analysis/arestoration_r_l_research.md` for the direct FST probe and affected-row summary.
- `Germanic/docs/dossiers/widuwe-u-preservation.md` as the full dossier named in the packet.
- `Germanic/data/old_english_wiktionary.tsv`.
- Reference texts in `docs/references/`, especially Ringe-Taylor, Campbell, Kroonen, Bülbring, Brunner, Luick, and Clark Hall.
- `Germanic/docs/lexeme_reports/pilot/` and found no existing pilot report for this lexeme.

## Reconstruction and early-stage forms

The cognate-set etymology and the project input should be kept distinct. Kroonen gives Proto-Germanic **\*swalwōn-** (feminine), while Ringe-Taylor cite West Germanic **\*swalwa** as the pre-OE stage relevant to breaking. The project row uses **\*swálwōn** as its derivational input form, i.e. a normalized input that preserves the feminine n-stem shape used by the cascade.

For this row, the important historical choice is already settled: there is no etymological *g in the bird name. The earlier project form `*swalgwōn` belonged to a confusion with the verb **swelgan**. With the corrected input, the cascade's early stages are straightforward: brightening to `*swælw-`, then breaking before `lw`, yielding **swealwe**.

## Old English philology

The row target is the OE citation form **swealwe**, a feminine noun ‘swallow’ (the bird). Repo-local reference material also shows secondary or later spellings such as **swealewe**, **swealuwe**, **swealowe**, **swealewe**, and related oblique/plural material such as **swalewan**. Those are useful philological background, but they are not the same thing as the row's target form.

Ringe-Taylor explicitly give WGmc `*swalwa > *swelwe > WS OE swealwe, Merc. swalwe`, which supports the row's citation-form target. Clark Hall and Kroonen also support **swealwe** as the main OE headword, with variant spellings. Campbell's `swaluwe` / `swalewan` evidence belongs to later parasitic-vowel and lowering behaviour in inflected forms, not to the core nominative singular target of row 2234.

## Project problem and solution

The project problem was not an unresolved OE outcome but an earlier proto-selection mistake. The row had been driven from `*swalgwōn`, which incorrectly imported a *g from the unrelated verb ‘swallow’. That produced the false expectation `swealgwe`. The current solution is correct: keep the row as the bird noun, derive it from **\*swálwōn**, and let ordinary OE breaking before `lw` produce **swealwe**.

The widuwe dossier does not reopen that decision. It only shows that if fuller inflectional coverage is ever modelled, parasite-vowel forms like `swaluwe` and lowered `swalewan` are philologically real and should not be blocked by a rule treating `*w` as a preserver.

## Paradigm probe

A paradigm probe is **not required** for the current memo. The row's citation-form target is already supported and the present project issue is proto disambiguation, not uncertainty about the OE nominative singular outcome.

If a future lexeme report wants to discuss inflectional/late WS variant evidence in more detail, that would be a separate optional probe of oblique or plural cells rather than a required probe for row 2234 itself.

## Recommended final report

Recommend a short lexeme report stating that row 2234 is a regular citation-form noun **swealwe** from corrected proto **\*swálwōn**, explicitly distinguishing it from the verb **swelgan** and noting that dossier evidence about **swaluwe / swalewan** concerns later inflected or variant forms, not the row target.

## Data-change recommendations

- **TSV PROTO:** no change.
- **TSV PROTOFORM:** no change.
- **TSV COUNTERPART:** no change.
- **TSV DERIVATION_CLASS:** no change.
- **TSV NOTE:** no required change; the current note already captures the essential disambiguation from **swelgan**.
- **`oe_known_problems.tsv`:** no change; this row is not a known-problem item.
- **`DEV_NOTES` text:** no change required; the old `*swalgwōn` material is valid as superseded project history, provided the final report treats it as diagnostic only.
- **Dossier text:** no change required; the `widuwe` dossier's `swaluwe / swalewan` material is valid background on unstressed-medial `u` lowering before `w`, but it should not be mistaken for direct citation-form evidence for row 2234.

Overall recommendation: no live data change is needed for row 2234; the main need is a careful final report that separates corrected proto history, current derivational input, and later OE variant evidence.
