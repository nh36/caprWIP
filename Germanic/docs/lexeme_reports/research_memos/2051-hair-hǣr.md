# Research memo — 2051 hair / hǣr

## Starting point

- **ID / concept / counterpart:** 2051, **hair**, **hǣr**.
- **TSV `PROTO`:** `*xḗrą`.
- **TSV `PROTOFORM`:** `*xḗrą`.
- **`DERIVATION_CLASS`:** `regular`.
- **Current TSV note:** `Wiktionary: PGmc *hērą > OE hǣr; *xazwăz 'grey' is wrong lexeme`.
- `Germanic/docs/lexeme_reports/coverage_audit.md` marks the row as requiring lexeme-report coverage because `NOTE` is non-empty, but there is **no pilot lexeme report** for this lexeme in `Germanic/docs/lexeme_reports/pilot/`.

## Packet evidence assessment

- **Authoritative/current:** the live TSV row; the packet's compact derivation trace showing that the current project input `*xḗrą` already yields `hǣr`; and the packet's statement that there is no live `oe_known_problems.tsv` entry for this row.
- **Useful background:** the packet's lexical-table hits (`old_english_wiktionary.tsv`, `old_english_swadesh.tsv`) confirm that `hǣr` is an OE lexical item; the packet's diagnostic excerpts from `DEV_NOTES` and `analysis/meord_med_chronological_review.md` are useful only for reconstructing earlier project confusion around other lexemes with medial `z`.
- **Stale or superseded:** the packet's `DEV_NOTES` excerpts about `*xazwăz -> hærw/hearw` are diagnostic remnants of an older wrong input, not evidence for the current row. The backup TSV confirms that row 2051 itself formerly carried stale `*xazwăz`, so those hits must not be treated as current lexical authority.
- **Irrelevant or misleading if read too quickly:** the packet's Clark Hall bibliography candidate `hǣr-sife` is not direct evidence that the row should be analysed through a compound or through `hād-`; and the packet's Campbell excerpt about `hād- hair` belongs to a different philological problem (`ON haddr`, `OE heordan`, possible compound material), not to the ordinary simplex `hǣr`.

## Additional repo research

Checked beyond the packet:

- `Germanic/docs/DEV_NOTES.md` (especially the dated diagnostic notes around `*xazwăz`).
- `Germanic/data/germanic-aligned-final.tsv` and `Germanic/data/germanic-aligned-final.tsv.backup-2026-02-06`.
- `Germanic/docs/lexeme_reports/coverage_audit.md`.
- `Germanic/data/oe_known_problems.tsv`.
- `docs/references/kroonen_etymological_dictionary_pgmc.vision.txt`.
- `docs/references/bammesberger_1990_morphologie.txt`.
- `docs/references/campbell_old_english_grammar.txt`.
- `docs/references/ringe_taylor_linguistic_history_vol2.txt`.
- `docs/references/fulk_comparative_grammar_early_germanic.vision.txt`.
- `docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt`.
- `docs/references/bosworth_toller_anglo_saxon_dictionary.vision.txt`.

Main findings from that wider pass:

- `Kroonen` gives the ordinary hair word as **PGmc `*hēra-` n.**, with OE `hær` beside the expected West Germanic cognates (`hair`, `haar`, `Haar`). `Bammesberger` likewise reconstructs `*hēr-a- > OE hǽr`.
- The live row's `PROTO`/`PROTOFORM` `*xḗrą` is therefore best read as the project's normalized derivational notation for the same lexeme, not as a competing etymology.
- `Clark Hall` and `Bosworth-Toller` both treat `hær/hǣr` as an ordinary OE headword (`n. 'hair'`), so the OE target is an attested citation form, not a reconstructed convenience form and not merely a compound fragment.
- `Campbell`, `Ringe-Taylor`, and `Fulk` discuss a **different** lexeme cluster: `ON haddr`, `OE heordan`, and possibly `hād-` in compounds. That material is relevant only as a warning against conflation.
- The live aligned TSV still has mixed cognate-set history around this concept: row 2051 is corrected to `*xḗrą`, but the neighboring English/Dutch/German rows for the same concept still show stale `PROTOFORM` `*xázwaz`. That is wider data drift, not a reason to change OE `hǣr`.
- `oe_known_problems.tsv` has no entry for this lexeme, which matches the fact that the current OE row is not a live derivational failure.

## Reconstruction and early-stage forms

This row only stays clear if three levels are kept distinct, even though two of them coincide in the TSV.

1. **Cognate-set proto / etymological headword:** the comparative evidence checked in the repo points to PGmc `*hēra-` / `*hēr-a-` 'hair' (Kroonen, Bammesberger).
2. **Project input form used for derivation:** TSV `PROTOFORM = *xḗrą`. This is the project's normalized input spelling for the same long-ē stem, not a separate lexeme and not a paradigm-cell workaround.
3. **OE target form:** `hǣr`, the attested Old English headword represented by the row.

Two rival forms must be kept out of this row:

- **`*xazwăz`** is the stale project input that generated earlier diagnostic outputs like `hærw/hearw`; it is superseded for row 2051.
- **`*hazdaz` / `*hazðaz`-type material** belongs to the separate `ON haddr` / `OE heordan` / possible `hād-` dossier. That may matter elsewhere, but it is not the etymological source of the ordinary OE simplex `hǣr` targeted here.

## Old English philology

- **Attested vs. reconstructed:** `hǣr` is directly attested as an OE lexical item. The row does not depend on a reconstructed West Saxon smoothing or on an inferred oblique form.
- **Citation form vs. inflected form:** the target is the citation/headword form, not a selected paradigm cell. `Clark Hall` gives `hær (ā, ē) n. 'hair'`; `Bosworth-Toller` gives `hær` with ordinary singular, plural, and collective uses.
- **Dictionary/headword issue:** the headword is the simplex `hǣr/hær` itself. The packet's `hǣr-sife` hit is only compound background and should not be allowed to replace the direct simplex evidence.
- **Dialect/manuscript caution:** the checked repo-local sources support the lemma securely, but they do not require any special dialectal restriction for this row.
- **Philological boundary:** `hǣr` 'hair' must be kept separate from `heordan` 'hards of flax' and from the debated `hād-` compound material. Those forms are useful as contrast cases precisely because they show how easy it is to collapse distinct lexemes into one hair-related dossier.

## Project problem and solution

The project problem here was lexical identity, not Old English morphology.

- Older project history wrongly aligned row 2051 with `*xazwăz`, producing diagnostic outputs like `hærw/hearw`.
- The current live row fixes that by using `*xḗrą`, which already derives cleanly to `hǣr`.
- The remaining risk is documentary: packet readers can still over-weight stale diagnostics or import the separate `haddr/heordan/hād-` discussion into this row.

So the right project solution is:

- keep the OE row itself as a **regular** derivation from the corrected hair lexeme;
- treat the note as an identity-cleanup note, not as evidence of a remaining sound-law failure;
- quarantine older `*xazwăz` diagnostics and the `*hazdaz` dossier as background for what this row is **not**.

## Paradigm probe

**No paradigm probe is required.**

This row does not hinge on selecting among competing OE paradigm cells, and the current target is the ordinary attested headword rather than an oblique or analogically levelled form. The real issue is lexeme identification, which the present row already resolves.

## Recommended final report

Recommend a short final report stating that OE `hǣr` is the attested ordinary headword continuing the PGmc hair lexeme (`*hēra-`, project input `*xḗrą`), and that older project references to `*xazwăz` or to the separate `haddr/heordan/hād-` complex are background only and should not be treated as this row's evidence base.

## Data-change recommendations

- **TSV `PROTO`:** no change recommended for row 2051.
- **TSV `PROTOFORM`:** no change recommended for row 2051. `*xḗrą` is an acceptable project input for the corrected hair lexeme. **Separate cognate-set cleanup is recommended elsewhere**, because neighboring non-OE rows for the same concept still carry stale `*xázwaz`.
- **TSV `COUNTERPART`:** no change recommended. `hǣr` is the right OE target.
- **TSV `DERIVATION_CLASS`:** no change recommended. `regular` is appropriate.
- **TSV `NOTE`:** change recommended. The note should say more explicitly that the row represents the ordinary PGmc hair lexeme (`*hēra-`, project `*xḗrą`), while both older project `*xazwăz` material and the separate `*hazdaz`/`haddr` dossier belong elsewhere. The current note is directionally right but too compressed.
- **`oe_known_problems.tsv`:** no change recommended.
- **`DEV_NOTES` / dossier text:** no mandatory change recommended for this memo. The dated diagnostics can remain as project history, but they should continue to be treated as superseded background rather than current authority for row 2051.
