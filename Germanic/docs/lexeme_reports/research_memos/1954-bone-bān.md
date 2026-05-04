# Research memo — 1954 bone / bān

## Starting point

- **ID:** 1954
- **CONCEPT:** bone
- **COUNTERPART:** bān
- **PROTO:** *báiną
- **PROTOFORM:** *báiną
- **DERIVATION_CLASS:** regular
- **NOTE:** Proto: oblique *bainăn→*bainą (n. a-stem nom.sg.; Kroonen)

This is a note-bearing regular row. No pilot or full lexeme report for this lexeme was found in `Germanic/docs/lexeme_reports/`; `coverage_audit.md` flags row 1954 as needing report coverage because the TSV `NOTE` is non-empty.

## Packet evidence assessment

**Authoritative/current:** the live TSV row; the packet's compact derivation trace showing `*báiną → bān`; and the packet's lexical-table hits confirming OE `bān` in the repo's supplementary tables. These support the current project treatment of the row as a regular nominative/accusative singular match.

**Useful background:** `DEV_NOTES.md` 2259-2263 and 14036-14038, which show that the current pipeline explicitly handles stressed PGmc `*ai` via WG monophthongization and still derives `*bainą → bān` successfully.

**Stale or superseded:** `DEV_NOTES.md` 1569-1572 (`*bainăn → bānan`, expected `bān`) is best read as historical debugging evidence for an over-inflected input choice, not as current lexical authority. It records a rejected path, not the present row design.

**Irrelevant or misleading:** the packet duplicates the 2262-2263 DEV_NOTES excerpt, and the packet has no dossier/analysis hits that would independently settle the distinction between Kroonen's etymological headword and the TSV's derivational input. The packet therefore needs augmentation from repo reference files.

## Additional repo research

Checked beyond the packet:

- `Germanic/data/oe_known_problems.tsv` — no entry for row 1954, `*báiną`, or `bān`.
- `Germanic/docs/lexeme_reports/coverage_audit.md` — confirms this row needs report coverage because of `NOTE`, not because of a modelling failure.
- `docs/refs.bib` — confirms usable keys `[@Kroonen2013]`, `[@Orel2003]`, `[@ClarkHall1960]`, `[@BosworthToller1898]`, and `[@BrightCassidyRingler1971]`.
- `docs/references/kroonen_etymological_dictionary_pgmc.vision.txt` and `docs/references/legacy/etymological_dictionary_of_proto_germanic_kroonen.txt` — give the comparative lemma as `*baina-` n. 'bone, leg', with OE `bān` [@Kroonen2013].
- `docs/references/orel_handbook_germanic_etymology.vision.txt` — gives `*bainan` sb.n. with OE `bán` [@Orel2003].
- `docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt` — gives headword `bān` n. 'bone' [@ClarkHall1960].
- `docs/references/bosworth_toller_anglo_saxon_dictionary.vision.txt` — gives `bān` with plural and compound evidence, confirming ordinary noun use [@BosworthToller1898].
- `docs/references/bright_anglo_saxon_reader.vision.txt` — explicitly lists `bān, n., bone` with `ds. bāne` and plural accusative/nominative forms [@BrightCassidyRingler1971].
- `Germanic/data/old_english_wiktionary.tsv` and `Germanic/data/old_english_swadesh.tsv` — supplementary confirmation of OE `bān`.

## Reconstruction and early-stage forms

The row needs three levels kept distinct:

1. **Cognate-set proto / etymological headword:** TSV `PROTO` is `*báiną`, while the comparative dictionaries in the repo cite lemma-style forms `*baina-` [@Kroonen2013] and `*bainan` [@Orel2003]. These are etymological headword conventions for the cognate set, not the OE output.
2. **Project input form:** TSV `PROTOFORM` is also `*báiną`. The live row is therefore using the nominative/accusative singular input directly; it is **not** currently using the oblique `*bainăn` named in the note.
3. **OE target form:** `bān`, the OE noun attested as dictionary headword and as a normal neuter paradigm form [@ClarkHall1960; @BosworthToller1898; @BrightCassidyRingler1971].

The packet's derivation trace is internally coherent for the project pipeline: PGmc `*báiną` passes through WG monophthongization to `*bāną`, then OE heavy-syllable nasal apocope yields `*bān`, surfacing as `bān`. The note's oblique `*bainăn` is background morphology, not a competing TSV input.

## Old English philology

`bān` is directly attested in the repo's lexicographic materials, so this is not a reconstructed-OE case. Clark Hall gives `bān` as the noun headword [@ClarkHall1960], Bosworth-Toller gives `bān` with plural evidence and compounds [@BosworthToller1898], and Bright's glossary explicitly distinguishes inflected cells such as dat.sg. `bāne` from the citation form `bān` [@BrightCassidyRingler1971].

Philologically, that means the row's OE target is the ordinary citation / nom.-acc.sg. neuter form, not an oblique-only or paradigm-cell workaround. No dialect or manuscript restriction is needed on current repo evidence. The supplementary Wiktionary and Swadesh tables agree with `bān`, but the stronger evidence is the repo's dictionary and reader files.

## Project problem and solution

The project problem here is mainly one of representation, not derivation. The TSV note compresses an etymological observation from Kroonen into wording that can be misread as though the row ought to feed oblique `*bainăn` into the FST. Historical DEV_NOTES show that doing so produced the wrong suffixed outcome `bānan`.

The current project solution is sound: keep the row as a **regular** derivation with `PROTO = PROTOFORM = *báiną`, derive `bān` directly, and treat the oblique/stem information only as comparative background explaining Kroonen's headword convention. This row is not a paradigm-cell case and not an unmodelled exception.

## Paradigm probe

A paradigm probe is **not required** for the current row. The live TSV does not hinge on choosing among competing OE cells: the selected input and the attested target already coincide as a regular citation-form match.

If a future philological appendix wanted one anyway, the optional cells to compare would be **nom./acc.sg.** `*báiną → bān` and an oblique singular cell behind OE **dat.sg.** `bāne`; but that is explanatory expansion, not a current blocker.

## Recommended final report

Recommend a brief final report that says the row is regular: the project derives attested OE `bān` directly from `*báiną`, while Kroonen/Orel lemma-style forms (`*baina-`, `*bainan`) and the note's oblique `*bainăn` are comparative background only. The report should avoid recasting this as a paradigm-cell solution.

## Data-change recommendations

- **TSV PROTO:** no change recommended.
- **TSV PROTOFORM:** no change recommended.
- **TSV COUNTERPART:** no change recommended.
- **TSV DERIVATION_CLASS:** no change recommended.
- **TSV NOTE:** **change recommended** — clarify that Kroonen's etymological headword/stem is background, while the TSV intentionally uses nom./acc.sg. `*báiną` as the derivational input. As written, the note can be read as if `*bainăn` were the form that should feed the row.
- **`oe_known_problems.tsv`:** no change recommended.
- **DEV_NOTES / dossier text:** no change required. There is no dedicated dossier for this lexeme, and the cited DEV_NOTES passages are acceptable as project history so long as the final report treats 1571 as diagnostic history rather than as current lexical evidence.
