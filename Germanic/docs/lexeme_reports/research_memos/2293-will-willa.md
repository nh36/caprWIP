# Research memo — 2293 will / willa

## Starting point

- **ID:** 2293
- **CONCEPT:** will
- **COUNTERPART:** `willa`
- **PROTO:** `*wéljô`
- **PROTOFORM:** `*wéljô`
- **DERIVATION_CLASS:** `regular`
- **NOTE:** `Kroonen *weljan- 2 m. 'will, wish' → OE willa m.; cf. G Wille, Du. wil (noun); willan is the verb 'to want' (belongs with *waljăną)`

The live row is a regular noun row, but the concept label `will` sits beside a separate verbal row (`2292 will / willan`). The main issue is therefore not sound change but lexical bookkeeping: the row must keep the noun `willa` distinct from the verb `willan`, and it must not collapse Kroonen's cognate-set headword, the project's derivational input, and the OE target into one undifferentiated "proto."

## Packet evidence assessment

- **Authoritative/current:** the live TSV row; the packet's compact derivation trace showing `*wéljô -> willa`; and the row-cluster evidence in the live TSV that the noun rows (`215/216/217/2293`) are separated from the verb rows (`1662/1663/1664/2292`).
- **Useful background:** the note's citation of Kroonen's noun entry and its comparison with German `Wille` and Dutch `wil`; these are good cognate-family pointers even though Kroonen's dictionary headword is not identical in shape to the project's row input.
- **Stale or superseded:** the packet's final note clause saying that OE `willan` "belongs with `*waljăną`." Repo-local reference evidence instead points to Kroonen's `*weljan- 1` for the verb 'to want'; `*waljan-` is the separate 'choose' verb. That clause should not be treated as current authority.
- **Irrelevant or misleading:** the packet's `old_english_wiktionary.tsv` hit `will -> willan` is verb-only evidence and does not bear directly on noun row 2293; the packet's concept-name hits in `DEV_NOTES`/analysis are unrelated string matches on ordinary English *will* and have no lexical value for this row; and "no manifest entry" / "no known-problems entry" are coverage metadata, not philological evidence.

So the packet is useful mainly for the live derivation and for flagging the noun/verb split. Its lexical-table hit and the `*waljăną` clause are not safe final evidence.

## Additional repo research

Checked beyond the packet:

- `Germanic/data/germanic-aligned-final.tsv` around rows `215-217`, `1662-1664`, and `2292-2293`.
- `Germanic/data/old_english_wiktionary.tsv`.
- `Germanic/data/oe_known_problems.tsv`.
- `Germanic/docs/DEV_NOTES.md` 870-885 and 9508-9516.
- `Germanic/docs/lexeme_reports/coverage_audit.md`.
- `Germanic/tools/oe_paradigm_probe.py`.
- `docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt`.
- `docs/references/kroonen_etymological_dictionary_pgmc.vision.txt`.
- `docs/references/orel_handbook_germanic_etymology.vision.txt`.
- `docs/references/kluge_seebold_etymologisches_woerterbuch.txt`.

Main findings:

- No row-specific dossier, analysis memo, or pilot/full lexeme report for `willa` was found.
- `oe_known_problems.tsv` has no entry for this row.
- The only relevant `DEV_NOTES` material I found is verb-only: it discusses `*weljaną -> willan`, which reinforces that the repo already treats the OE verb as a separate row rather than as evidence for `willa`.
- Clark Hall has a noun headword `willa m.` with senses such as "mind, will, determination, purpose, desire, wish" and separately lists `willan` as the anomalous verb.
- Kroonen distinguishes `*weljan- 1` 'to want' from `*weljan- 2 m.` 'will, wish' and explicitly gives OE `willan` under the former and OE `willa` under the latter.
- Orel gives the noun as `*weljōn sb.m.` with OE `willa`; Kluge likewise gives Germanic `*weljōn m.` behind German `Wille` and cites OE `willa`.

## Reconstruction and early-stage forms

This row needs a clear three-way distinction.

1. **Cognate-set proto / etymological headword:** Kroonen's noun entry is `*weljan- 2 m. 'will, wish'`, while Orel and Kluge represent the noun as a `*weljōn`-type masculine. Those are etymological dictionary headwords, not the literal row input used in the OE derivation trace.
2. **Project input form used for derivation:** TSV `PROTO`/`PROTOFORM` `*wéljô`. In project terms this is the OE-facing nominative-singular input that the live trace sends through WGmc j-gemination and OE i-umlaut/j-loss to `willa`.
3. **OE target form represented by the row:** the noun citation form `willa`, not the verb `willan`.

So the row's current `*wéljô` is best understood as a project derivational input corresponding to the noun family that dictionaries headword as `*weljan- 2` or `*weljōn`. The mistake would be to identify the noun with the separate verb row or to read Kroonen's `*-jan-` headword as if the row ought to target OE `willan`.

## Old English philology

`willa` is an attested OE noun, and the repo-local dictionary evidence treats it as such. Clark Hall separates noun `willa m.` from verb `willan`, which is exactly the distinction this row needs.

Three philological cautions matter:

- **Attested noun vs. related verb:** `willa` and `willan` are related but not interchangeable. The noun row should not borrow the verb's headword evidence or paradigmatic status.
- **Dictionary headword vs. project input:** dictionary etyma such as `*weljan- 2` / `*weljōn` are not the same thing as the project's `*wéljô` input; the former identify the cognate set, while the latter is the row's OE-facing derivational form.
- **Citation form vs. inflected forms:** I found enough repo-local evidence for the noun citation form `willa`, but no row-specific reason to replace it with an oblique or variant form.

I found no repo-local basis for stronger claims about dialect, manuscript restriction, or a need to reconstruct some unattested OE noun instead of `willa`.

## Project problem and solution

This is basically a lexical-disambiguation row, not an exception row.

The project problem is that English *will* covers both a noun and a verb, while the OE dataset correctly splits them:

- row `2292`: verb `willan` from `*wéljaną`;
- row `2293`: noun `willa` from `*wéljô`.

The current project solution is mostly right:

- keep `COUNTERPART = willa`;
- keep the noun on its own row, separate from `willan`;
- keep `DERIVATION_CLASS = regular`;
- preserve the note's noun/verb warning, but fix its proto wording so the verb is not misassigned to `*waljăną`.

## Paradigm probe

A paradigm probe is **not required** for this row.

Reason: this is not a late-analogy, hidden-cell, or finite-form selection problem. `PROTO` and `PROTOFORM` are identical, the live citation-form trace already derives `willa`, and the substantive issue is lexical separation from `willan`, not uncertainty about which OE paradigm cell the row should represent. `oe_paradigm_probe.py` has no built-in `will / willa` spec, but that is not an evidential gap here.

## Recommended final report

Recommend a short final report saying that row 2293 is the attested OE noun `willa` 'will, wish'; that the live project input `*wéljô` is the OE-facing derivational form for the noun family cited by dictionaries as `*weljan- 2` / `*weljōn`; and that the separate verb `willan` belongs to row 2292 and should not be conflated with this noun row.

## Data-change recommendations

- **TSV `PROTO`:** no change recommended. Keep `*wéljô` as the project's noun-row input.
- **TSV `PROTOFORM`:** no change recommended. Keep `*wéljô`.
- **TSV `COUNTERPART`:** no change recommended. Keep `willa`.
- **TSV `DERIVATION_CLASS`:** no change recommended. `regular` is still correct.
- **TSV `NOTE`:** change recommended. Keep the noun/verb distinction, but revise the wording so it says that OE `willan` is the separate verb row and corresponds to Kroonen `*weljan- 1` / TSV `*wéljaną`, not to `*waljăną`. It would also help to say explicitly that Kroonen's `*weljan- 2` is the cognate-set noun headword behind the project's `*wéljô`.
- **`oe_known_problems.tsv`:** no change recommended.
- **`DEV_NOTES` text:** no change recommended. The relevant notes I found are verb-only and not misleading once row 2292 and row 2293 are kept separate.
- **Dossier / analysis text:** no change recommended. I found no row-specific dossier or analysis file needing cleanup.
