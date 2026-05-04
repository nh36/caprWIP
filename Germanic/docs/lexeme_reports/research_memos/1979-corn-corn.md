# Research memo — 1979 corn / corn

## Starting point

- **ID:** 1979
- **CONCEPT:** corn
- **COUNTERPART:** corn
- **PROTO:** *kúrną
- **PROTOFORM:** *kúrną
- **DERIVATION_CLASS:** regular
- **NOTE:** Proto: oblique *kurnăn→*kurną (n. a-stem nom.sg.; Kroonen)

This is a note-bearing regular row. No pilot or full lexeme report for this lexeme was found in `Germanic/docs/lexeme_reports/`; `coverage_audit.md` flags row 1979 as needing report coverage because the TSV `NOTE` is non-empty.

## Packet evidence assessment

**Authoritative/current:** the live TSV row; the packet's compact derivation trace showing `*kúrną → corn`; and the packet's lexical-table hit in `old_english_wiktionary.tsv` confirming OE `corn`. These support the current project treatment of the row as a regular nominative/accusative singular match.

**Useful background:** the packet's Kroonen/Orel bibliography candidates, because repo reference files do confirm relevant comparative entries under `*kurna-` / `*kurnan` [@Kroonen2013; @Orel2003].

**Stale or superseded:** `DEV_NOTES.md` 1571 (`*kurnăn → cornan`, expected `corn`) is diagnostic project history showing that an over-inflected oblique input once yielded the wrong suffixed output. It should not be promoted to current lexical authority.

**Irrelevant or misleading:** the packet's supporting/background hits at `DEV_NOTES.md:6123` and `Germanic/docs/dossiers/widuwe-u-preservation.md:1480` are false positives on `Corn` / `corn.` meaning Cornish, not evidence for OE `corn`. The packet therefore needs supplementation from the actual lexicographic and etymological reference files.

## Additional repo research

Checked beyond the packet:

- `Germanic/data/oe_known_problems.tsv` — no entry for row 1979, `*kúrną`, or `corn`.
- `Germanic/docs/lexeme_reports/coverage_audit.md` — confirms this row needs report coverage because of `NOTE`, not because of a modelling failure.
- `docs/refs.bib` — confirms usable keys `[@Kroonen2013]`, `[@Orel2003]`, `[@ClarkHall1960]`, `[@BosworthToller1898]`, and `[@BrightCassidyRingler1971]`.
- `docs/references/kroonen_etymological_dictionary_pgmc.vision.txt` and `docs/references/legacy/etymological_dictionary_of_proto_germanic_kroonen.txt` — give the comparative lemma as `*kurna-` n. 'corn, wheat' with OE `corn` [@Kroonen2013].
- `docs/references/orel_handbook_germanic_etymology.vision.txt` and `docs/references/legacy/orel_handbook_germanic_etymology.txt` — give `*kurnan` sb.n. with OE `corn` [@Orel2003].
- `docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt` — gives headword `corn` n. 'corn, grain' [@ClarkHall1960].
- `docs/references/bosworth_toller_anglo_saxon_dictionary.vision.txt` — gives `corn` as an ordinary noun with citation and contextual evidence [@BosworthToller1898].
- `docs/references/bright_anglo_saxon_reader.vision.txt` — explicitly lists `corn, n.` with gen.sg. `cornes` and acc.sg. `corn` [@BrightCassidyRingler1971].
- `Germanic/data/old_english_wiktionary.tsv` — supplementary confirmation of OE `corn`.

No full dossier or analysis file relevant to this lexeme was named in the packet or row note; the only apparent dossier hit in the packet is the unrelated `widuwe-u-preservation.md` false positive on `corn.` = Cornish.

## Reconstruction and early-stage forms

The row needs three levels kept distinct:

1. **Cognate-set proto / etymological headword:** the comparative dictionaries in the repo cite lemma-style forms `*kurna-` [@Kroonen2013] and `*kurnan` [@Orel2003]. Those are cognate-set headword conventions, not the OE output.
2. **Project input form:** TSV `PROTO` and `PROTOFORM` are both `*kúrną`, an accented nominative/accusative singular input chosen for the derivation pipeline. The live row is therefore **not** using the oblique `*kurnăn` named in the note as its active FST input.
3. **OE target form:** `corn`, the ordinary attested OE citation form [@ClarkHall1960; @BosworthToller1898; @BrightCassidyRingler1971].

The packet's derivation trace is coherent for the project pipeline: starting from `*kúrną`, NWGmc lowering gives `*kórną`, and OE heavy-syllable nasal apocope yields `*kórn`, surfacing as `corn`. The note's `*kurnăn→*kurną` is best understood as comparative background about stem/oblique morphology, not as a rival live TSV input. The accent mismatch also matters: the project row uses accented `*kúrną`, while Kroonen/Orel headword conventions normally do not encode stress this way.

## Old English philology

`corn` is directly attested in the repo's lexicographic materials, so this is not a reconstructed-OE case. Clark Hall gives `corn` as the noun headword [@ClarkHall1960], Bosworth-Toller treats it as an ordinary lexical item [@BosworthToller1898], and Bright's glossary explicitly distinguishes the citation form `corn` from inflected cells such as gen.sg. `cornes` [@BrightCassidyRingler1971].

Philologically, the row's target is therefore the normal citation / nom.-acc.sg. neuter form, not an oblique-only survival and not a paradigm-cell workaround. No dialect or manuscript restriction is supported by the repo evidence checked here. The Wiktionary TSV agrees, but the stronger support comes from the dictionary and reader files.

## Project problem and solution

The project problem here is mainly representational, not derivational. The TSV note compresses a comparative-etymological observation into wording that can be misread as though the row ought to feed oblique `*kurnăn` into the FST. The historical DEV_NOTES example shows why that reading is wrong: `*kurnăn` produced diagnostic `cornan`, not the desired citation form `corn`.

The current project solution is sound: keep the row as a **regular** derivation with `PROTO = PROTOFORM = *kúrną`, derive `corn` directly, and treat `*kurna-`, `*kurnan`, and the note's oblique `*kurnăn` as comparative background only. This row is not a paradigm-cell case and not an unmodelled exception.

## Paradigm probe

A paradigm probe is **not required** for the current row. The live TSV does not hinge on choosing among competing OE cells: the selected input already yields the attested citation form.

If a future appendix wanted an explanatory probe anyway, the optional comparison would be **nom./acc.sg.** `*kúrną → corn` versus a representative oblique singular cell behind OE **gen.sg.** `cornes` (and possibly **dat.sg.** `corne`). That is explanatory expansion, not a current blocker.

## Recommended final report

Recommend a brief final report saying that the row is regular: the project derives attested OE `corn` directly from `*kúrną`, while Kroonen/Orel lemma-style forms (`*kurna-`, `*kurnan`) and the note's oblique `*kurnăn` are comparative background only. The report should explicitly dismiss the old `cornan` debugging path as stale diagnostic history, not as current evidence.

## Data-change recommendations

- **TSV PROTO:** no change recommended.
- **TSV PROTOFORM:** no change recommended.
- **TSV COUNTERPART:** no change recommended.
- **TSV DERIVATION_CLASS:** no change recommended.
- **TSV NOTE:** **change recommended** — clarify that the live row intentionally derives OE `corn` from nom./acc.sg. `*kúrną`, while Kroonen/Orel lemma-style or oblique forms are comparative background only. As written, the note can be read as if `*kurnăn` should feed the row.
- **`oe_known_problems.tsv`:** no change recommended.
- **DEV_NOTES / dossier text:** no change required. `DEV_NOTES.md` 1571 is acceptable as historical debugging evidence if treated as stale diagnostic history, and there is no dedicated dossier for this lexeme that needs cleanup.
