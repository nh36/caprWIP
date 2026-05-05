# Research memo — 2049 guest / ġiest

## Starting point

- **ID:** 2049
- **CONCEPT:** guest
- **COUNTERPART:** `ġiest`
- **PROTO:** `*gástiz`
- **PROTOFORM:** `*gástiz`
- **DERIVATION_CLASS:** `regular`
- **NOTE:** `R/T vol.2 3857: PGmc *gastiz > WS OE giest`

This is a note-bearing regular row. The live row is not a paradigm-cell rescue: the cognate-set proto and the project input form are the same, and the current derivation already lands on the row target. The real memo task is to pin down what kind of OE form `ġiest` is: a normalized West Saxon outcome within a wider attested variant set, not the only OE spelling for the lexeme.

## Packet evidence assessment

**Authoritative/current:**

- the live TSV row itself;
- the packet's compact derivation trace, which shows an exact match from `*gástiz` to `ġiest`;
- the packet's analysis-file excerpts from Campbell and Ringe & Taylor, which directly support West Saxon `ġiest` versus Anglian `gest`.

**Useful background:**

- `DEV_NOTES.md:12010-12012`, which uses `*gastiz > *gæstiz > ... > ġiest` as a comparison case for AFB + i-umlaut + WS palatal diphthongization;
- the packet's note that there is no `oe_known_problems.tsv` entry, which helps show this is not a live modelling failure;
- the dialect-summary table at `ws_vs_anglian_dialect_differences.md:639`, which is helpful as a comparative sketch of WS `ġiest` versus Anglian `gest`, even though it is not a row-specific argument.

**Stale or superseded:**

- the packet's Old Saxon `*gast` note from `DEV_NOTES.md:35375` is not row-specific authority; it belongs to a different discussion about **rēk** and only uses `gast` as a generic i-stem example;
- the packet has no dedicated dossier or pilot report for this lexeme, so generic repo history should not be promoted to row-specific evidence.

**Irrelevant or misleading:**

- `old_english_wiktionary.tsv: guest -> appear` is plainly irrelevant to this row and should not be used as lexical evidence;
- the packet's lack of a manifest entry is status information only, not philological evidence.

## Additional repo research

Beyond the packet I checked:

- `Germanic/docs/DEV_NOTES.md`
- `Germanic/docs/analysis/ws_vs_anglian_dialect_differences.md`
- `Germanic/data/oe_known_problems.tsv`
- `Germanic/docs/lexeme_reports/coverage_audit.md`
- `Germanic/tools/oe_paradigm_probe.py`
- `docs/references/campbell_old_english_grammar.txt`
- `docs/references/crist_2001_conspiracy_in_historical_phonology.txt`
- `docs/references/bright_anglo_saxon_reader.txt`
- `docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt`
- `docs/references/bosworth_toller_anglo_saxon_dictionary.vision.txt`
- `docs/refs.bib`

Main findings from that wider search:

- I found no row-specific dossier and no existing pilot/full lexeme report for `guest / ġiest`.
- `oe_known_problems.tsv` has no entry for row 2049, matching the row's regular status.
- `coverage_audit.md` marks row 2049 as needing lexeme-report coverage only because the TSV `NOTE` is non-empty.
- Campbell's grammar explicitly lists `giest` among WS palatal-diphthongization examples from earlier `*gæst`.
- The repo's Ringe & Taylor dossier file explicitly contrasts WS `ġiest` with Northumbrian `gest` and Mercian `gesthúsum`.
- Crist's comparative table gives the inherited cognate set `*gastiz` with OE `giest`, confirming that the row's PGmc side is ordinary comparative material rather than a special project reconstruction.
- Bright, Clark Hall, and Bosworth-Toller all support the OE lexeme as attested, while also showing that the spelling set is broader than just normalized `ġiest`: dictionary forms include `gest`, `giest`, `gyst`, and headwording under `gist`.

## Reconstruction and early-stage forms

Three levels should still be kept separate even though two of them coincide here:

1. **Cognate-set proto / etymological headword:** `*gastiz` / TSV `PROTO` `*gástiz`, the inherited Proto-Germanic i-stem noun behind English **guest**, Dutch **gast**, OHG **gast**, and related forms.
2. **Project input form used for derivation:** TSV `PROTOFORM` `*gástiz`, which in this row happens to be the same as the cognate-set proto.
3. **OE target form represented by the row:** normalized WS `ġiest`.

The early stages reflected in the repo are straightforward. After Anglo-Frisian Brightening the pre-OE stem is of the `*gæst-` type; that fronted vowel then participates in the palatal/i-mutation sequence that yields West Saxon `ie` after initial palatal `ġ-`. The important contrast is not between rival PGmc reconstructions, but between later OE dialect outcomes from the same inherited stem:

- **WS target:** `ġiest`
- **Anglian background forms:** `gest`

So this row does **not** need a special project-only OE reconstruction. It needs a clear statement that the live row chooses the West Saxon reflex of an otherwise ordinary PGmc i-stem noun.

## Old English philology

Philologically this is an **attested OE lexeme**, but the exact surface form must be described carefully.

- Campbell and the repo's dialect-analysis file support `giest` / `ġiest` as a West Saxon palatal-diphthongized outcome from earlier `*gæst`.
- Ringe & Taylor's comparative table gives the crucial dialect contrast: WS `ġiest`, Northumbrian `gest`, Mercian dat. pl. `gesthúsum`.
- Bright's glossary has `gyst (giest), m., guest, stranger` with plural `gystas`.
- Bosworth-Toller groups `gæst, gest, giest, gyst` under `gist`, showing that dictionary headwording and manuscript spellings vary.
- Clark Hall likewise cross-references `gest, gēst = giest, gast` and gives `glest (æ, e, i, y) m. 'guest'`.

So the row's `COUNTERPART` `ġiest` is best understood as a **normalized WS target form inside an attested lexical family with multiple spellings**, not as a claim that every OE witness uses exactly dotted `ġiest`, and not as a reconstructed unattested OE form.

## Project problem and solution

The project problem here is not a broken derivation but evidence control.

- The row note points to a real WS outcome, but by itself it does not explain that `ġiest` is specifically a WS reflex within a broader OE variant set.
- The packet also pulls in one irrelevant lexical-table hit (`guest -> appear`) and one non-row-specific Old Saxon stem-class aside, both of which could distract later drafting.

The right project solution is therefore:

- keep the row as a **regular** derivation from `*gástiz`;
- keep `PROTO` and `PROTOFORM` as they are, since the project is not using a special paradigm-cell input here;
- describe `ġiest` in the final report as the normalized WS target, with Anglian `gest` and dictionary spellings `gest/gyst/gist` treated as supporting philological background rather than as reasons to retarget the row.

## Paradigm probe

A paradigm probe is **not required** for this row. The current citation-form input already yields the intended OE target, and the row is not being justified by switching from one paradigm cell to another.

If someone later wanted an optional appendix, the only useful comparison would be a small noun probe contrasting nominative singular `*gástiz` with an oblique/plural cell behind forms like `gestas` or compound `gesthúsum`. But that is not needed to justify the live row or the recommended final report.

## Recommended final report

Recommend a brief final report saying that row 2049 is a regular derivation of PGmc `*gastiz` to normalized WS `ġiest`; that Campbell and Ringe & Taylor support the WS palatal-diphthongized form against Anglian `gest`; and that dictionary evidence shows a wider attested spelling set (`gest`, `giest`, `gyst`, `gist`) which should be mentioned without displacing the row's chosen WS target.

## Data-change recommendations

- **TSV `PROTO`:** no change recommended.
- **TSV `PROTOFORM`:** no change recommended.
- **TSV `COUNTERPART`:** no change recommended; `ġiest` is still a defensible normalized WS target.
- **TSV `DERIVATION_CLASS`:** no change recommended.
- **TSV `NOTE`:** no change required. It is brief, but it already points to the correct PGmc > WS relationship; the memo/final report can supply the needed variant and normalization nuance.
- **`oe_known_problems.tsv`:** no change recommended.
- **`DEV_NOTES` / dossier text:** no change recommended. The relevant `DEV_NOTES` material is either useful background (`12012`) or unrelated diagnostic context (`35375`), and no dedicated dossier exists that needs cleanup.
