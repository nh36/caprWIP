# Research memo — 2251 thorn / þorn

## Starting point

- **ID:** 2251
- **CONCEPT:** thorn
- **COUNTERPART:** þorn
- **PROTO:** *θúrnaz
- **PROTOFORM:** *θúrnaz
- **DERIVATION_CLASS:** regular
- **NOTE:** Adopt *θurnăz (m. a-stem; Kroonen *θurna-). A u-stem reformation *θurnuz is reflected in Gothic þaurnus (u-stem), and Old Norse also shows an ija-stem variant þyrnir 'thorn' (alongside þorn).

This is a note-bearing regular row. No pilot or full lexeme report for this lexeme was found in the repo, so the packet and wider repo evidence have to be treated as the live basis for the memo.

## Packet evidence assessment

- **Authoritative/current:** the live TSV row; the packet's compact derivation trace showing `*θúrnaz -> þorn`; the absence of a row-specific `oe_known_problems.tsv` entry; and the lexical-table hit `thorn -> þorn`, which confirms the intended OE lemma.
- **Useful background:** the packet's note preserving the comparative alternatives `*þurna-` and `*þurnuz`; and the bibliography suggestion `[@Kroonen2013]`, which is genuinely relevant once checked against the repo references.
- **Stale or superseded:** the packet's resurfaced `DEV_NOTES.md:90` sentence saying that “thorn” had already been solved by adopting a paradigm form. That line reflects earlier project history, not the current live row, because the present TSV still uses `PROTO = PROTOFORM = *θúrnaz` and does not encode a special paradigm-cell workaround.
- **Irrelevant or misleading:** the packet's `DEV_NOTES.md` hits at 2944, 8304, 8314, and 8325 are about the repo-wide `θ/þ` encoding convention, not about the thorn lexeme; they should not be read as lexical evidence. The packet also does not surface the older diagnostic `*θurnuz -> þōrn` history, so the memo has to distinguish current row design from earlier experiments explicitly.

## Additional repo research

Checked beyond the packet:

- `Germanic/data/oe_known_problems.tsv` — no entry for row 2251, `*θúrnaz`, or `þorn`.
- `Germanic/docs/lexeme_reports/coverage_audit.md` — confirms this row needs report coverage because the TSV `NOTE` is non-empty, not because of a live modelling failure.
- `Germanic/docs/DEV_NOTES.md` at line 90 and around line 2621 — useful for project chronology, especially the earlier “paradigm form” wording and the older diagnostic example `*θurnuz -> þōrn`.
- `Germanic/docs/dossier-shoulder-2026.md` around line 642 — mentions `*þurnaz > þorn` only as an indirect control example in another dossier, not as a thorn-specific authority.
- `Germanic/data/old_english_wiktionary.tsv` — gives `thorn -> þorn` as the ordinary inherited lemma.
- `docs/references/kroonen_etymological_dictionary_pgmc.vision.txt` — gives `*þurna- n. 'thorn': ... OE þorn` [@Kroonen2013].
- `docs/references/orel_handbook_germanic_etymology.vision.txt` — gives `*þurnuz ~ *þurnaz sb.m.: Goth þaurnus ... OE ðorn` [@Orel2003].
- `docs/references/bright_anglo_saxon_reader.vision.txt` — gives `þorn, m., thorn` with plural `þornas`, confirming ordinary OE attestation [@BrightCassidyRingler1971].
- `docs/refs.bib` — confirms usable bibliography keys for those sources.

No full thorn dossier, no thorn-specific analysis file, and no pilot report were found. The only dossier hit was the indirect shoulder control note above, which should not be weighted like row-specific evidence.

## Reconstruction and early-stage forms

This row needs the standard three-way distinction.

1. **Cognate-set proto / comparative headword:** the repo's checked reference works are not identical. Kroonen gives neuter `*þurna-` [@Kroonen2013], while Orel gives masculine `*þurnuz ~ *þurnaz` [@Orel2003]. Those are comparative reconstructions for the cognate set, not automatically the same thing as the live OE row input.
2. **Project input form for derivation:** the live TSV uses `PROTO = PROTOFORM = *θúrnaz`. That is the form the project currently feeds into the OE derivation, and the compact trace shows that it yields the intended OE output directly.
3. **OE target form:** `þorn`, the ordinary OE citation form attested in the repo's lexical materials [@BrightCassidyRingler1971].

The present TSV note compresses these layers too tightly. Its wording “Adopt *θurnăz (m. a-stem; Kroonen *θurna-)” can be misread as though Kroonen directly supports the row's exact masculine nominative-style input. The repo references instead show a real comparative split: Kroonen's headword is neuter `*þurna-`, whereas Orel explicitly preserves masculine `*þurnuz ~ *þurnaz`. The live row is therefore best understood as choosing `*θúrnaz` for the project derivation while citing Kroonen and the other cognates as comparative background.

## Old English philology

`þorn` is an attested OE noun, not a reconstructed convenience form. `old_english_wiktionary.tsv` gives the inherited lemma, and Bright's glossary explicitly lists `þorn, m.` with plural `þornas` [@BrightCassidyRingler1971].

Nothing checked in the repo suggests that row 2251 should target a special inflected cell, a dialect-restricted form, or a manuscript-only spelling. The live row is aimed at the ordinary citation form `þorn`. Gothic `þaurnus` and Old Norse `þyrnir` are useful comparative evidence for alternative Germanic stem formations, but they are not direct authority for the OE target itself.

## Project problem and solution

The project problem here is mainly one of documentation and project chronology, not a live derivational failure. Older repo history still remembers a stage where “thorn” was grouped with paradigm-form repairs, and `DEV_NOTES.md` preserves an older diagnostic example `*θurnuz -> þōrn`. But the current row no longer works that way: the live TSV uses the citation-form input `*θúrnaz`, the compact derivation trace returns `þorn`, and the row is classified as `regular`.

The current project solution is therefore:

- keep the row as a regular derivation `*θúrnaz -> þorn`;
- treat `*þurna-` and `*þurnuz` as comparative background, not as competing live row inputs;
- avoid describing the row as if it still depended on a special paradigm-cell rescue.

## Paradigm probe

A paradigm probe is **not required** for this row. The live analysis does not depend on selecting among competing OE paradigm cells; the current input already yields the intended attested citation form.

If the project later reopens the comparative reconstruction question, an optional exploratory comparison could test `*θúrnaz` against alternatives such as neuter-style `*θúrną` or u-stem `*θúrnuz`, but that would be a reconstruction-control exercise, not a required paradigm probe for the present row.

## Recommended final report

Recommend a brief final report saying that row 2251 is currently a regular derivation `*θúrnaz -> þorn`, while the note/report prose should distinguish the live project input from the broader comparative background: Kroonen's neuter `*þurna-` and Orel's masculine `*þurnuz ~ *þurnaz`. It should also note that older `DEV_NOTES` references to a paradigm-form solution are historical only, not the present row design.

## Data-change recommendations

- **TSV `PROTO`:** no change recommended. The live row is coherent as a derivational input and already matches the OE target.
- **TSV `PROTOFORM`:** no change recommended. The current project is not using a separate paradigm-cell form here.
- **TSV `COUNTERPART`:** no change recommended. `þorn` is the correct OE target.
- **TSV `DERIVATION_CLASS`:** no change recommended. `regular` matches the live derivation.
- **TSV `NOTE`:** **change recommended.** It should explicitly distinguish the live project input `*θúrnaz` from Kroonen's neuter `*þurna-` and Orel's masculine `*þurnuz ~ *þurnaz`, rather than compressing them into the misleading phrase “m. a-stem; Kroonen *θurna-”.
- **`oe_known_problems.tsv`:** no change recommended.
- **`DEV_NOTES` / dossier text:** **minor DEV_NOTES cleanup recommended; no dossier change required.** `DEV_NOTES.md` should mark the line grouping “thorn” with paradigm-form fixes, and the older `*θurnuz -> þōrn` diagnostic example, as historical/superseded relative to the live row. There is no dedicated thorn dossier text that needs revision from the material checked.
