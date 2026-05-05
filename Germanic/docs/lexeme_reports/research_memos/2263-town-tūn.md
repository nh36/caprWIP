# Research memo — 2263 town / tūn

## Starting point

- **ID:** 2263
- **CONCEPT:** town
- **COUNTERPART:** tūn
- **PROTO:** *tūną
- **PROTOFORM:** *tūną
- **DERIVATION_CLASS:** regular
- **NOTE:** Proto: oblique *tūnăn→*tūną (n. a-stem nom.sg.; Kroonen)

This is a note-bearing regular row. No pilot or full lexeme report for this lexeme was found under `Germanic/docs/lexeme_reports/`; `coverage_audit.md` flags row 2263 for coverage because the TSV `NOTE` is non-empty.

## Packet evidence assessment

**Authoritative/current:** the live TSV row; the packet's compact derivation trace showing that the current pipeline derives `*tūną → tūn`; and the packet's lexical-table confirmation from `old_english_wiktionary.tsv` that the OE lexeme is `tūn`. These support the current project treatment of the row as a regular derivation whose live input already matches the intended OE citation form.

**Useful background:** the packet correctly shows that there is no `oe_known_problems.tsv` entry and no row-specific dossier/analysis hit. Its repetition of the TSV note is useful as a signal that the real issue is not the FST output but how the proto/headword background is being described.

**Stale or superseded:** no genuine row-specific stale dossier was surfaced in the packet. What the packet has instead is a note-derived formulation that still needs verification against the actual reference files.

**Irrelevant or misleading:** the packet's `DEV_NOTES.md` hit about `burch 'town' < PWGmc *burg` is a false-positive concept-name collision and is not evidence for row 2263. More importantly, the packet reproduces the TSV note's claim about `oblique *tūnăn`, but direct repo-local Kroonen evidence gives lemma-style `*tūna-` rather than `*tūnăn`; that wording should therefore be treated as project metadata needing correction, not as independent authority.

## Additional repo research

Checked beyond the packet:

- `Germanic/data/oe_known_problems.tsv` — no entry for row 2263, `*tūną`, or `tūn`.
- `Germanic/docs/lexeme_reports/coverage_audit.md` — confirms the row needs report coverage because of `NOTE`, not because of a modelling failure.
- `docs/refs.bib` — confirms usable keys `[@Kroonen2013]`, `[@Orel2003]`, `[@ClarkHall1960]`, `[@BosworthToller1898]`, and `[@Campbell1959]`.
- `docs/references/kroonen_etymological_dictionary_pgmc.vision.txt` and `docs/references/legacy/etymological_dictionary_of_proto_germanic_kroonen.txt` — give the comparative lemma as `*tūna-` n. 'fenced area', with OE `tūn` m. 'enclosed piece of ground, yard; town' [@Kroonen2013].
- `docs/references/orel_handbook_germanic_etymology.vision.txt` — gives an alternative headword presentation `*tūnan ~ *tūnaz` sb.m./n., again with OE `tūn` [@Orel2003].
- `docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt` — gives `tūn` m. 'enclosure, garden, field, yard ... group of houses, village, town' [@ClarkHall1960].
- `docs/references/brunner_1965_altenglische_grammatik.vision.txt` — cites `tūn` as a regular OE reflex of West Germanic `ū`, supporting the uncomplicated phonological path to the vowel in the target form.
- `Germanic/data/old_english_wiktionary.tsv` — supplementary confirmation of OE `tūn`.

No full dossier or analysis file named in the packet or TSV note was found beyond these reference files, and no pilot report exists for this lexeme.

## Reconstruction and early-stage forms

This row needs three levels kept separate:

1. **Cognate-set proto / etymological headword:** TSV `PROTO` is `*tūną`, but the comparative dictionaries in the repo cite headword-style forms `*tūna-` n. [@Kroonen2013] or `*tūnan ~ *tūnaz` sb.m./n. [@Orel2003]. Those are cognate-set lemma conventions, not the OE output.
2. **Project input form:** TSV `PROTOFORM` is also `*tūną`. The live row therefore uses the nominative/accusative singular input directly; it is **not** currently using `*tūnăn` as a derivational input.
3. **OE target form:** `tūn`, the attested OE citation form.

The project trace is straightforward: no special PWGmc/NWGmc reshaping is needed in the live derivation, and OE heavy-syllable nasal apocope yields `*tūn`, surfacing as `tūn`. The note's `*tūnăn` is not supported by the checked Kroonen entry and should not be collapsed into either the cognate-set headword or the live project input.

## Old English philology

`tūn` is directly attested in the repo's lexicographic materials, so this is not a reconstructed-OE case. Clark Hall gives `tūn` as a masculine headword with the semantic range 'enclosure, garden, field, yard ... village, town' [@ClarkHall1960], and Kroonen's daughter-language line likewise lists OE `tūn` m. [@Kroonen2013]. The supplementary Wiktionary table agrees on the citation form.

Philologically, the row target is the ordinary OE citation form, not a special inflected cell. The main caution is grammatical, not phonological: the comparative proto lemma is presented as neuter in Kroonen, while the OE headword is given as masculine in the repo's lexicographic sources. The memo and any later report should therefore avoid wording that makes OE `tūn` itself look like a neuter-only form just because the PGmc cognate-set headword is neuter.

No dialect or manuscript restriction is supported by the repo-local evidence checked here.

## Project problem and solution

The project problem is representational rather than derivational. The live row already derives the correct OE form regularly, but the TSV note currently blurs together three things: comparative lemma convention, possible stem/oblique background, and the actual project input used by the FST.

The current project solution should remain simple: keep the row as a **regular** derivation with `PROTO = PROTOFORM = *tūną`, deriving attested OE `tūn` directly. In the future final report, treat Kroonen/Orel headword spellings as comparative background only, and do not imply that the row should instead be driven from an oblique `*tūnăn`.

## Paradigm probe

A paradigm probe is **not required** for the current row. The row is not using a selected OE paradigm cell to rescue the output; it already lands on the ordinary citation form and there is no live inflectional-cell dispute blocking the analysis.

If the team later wanted a purely illustrative probe, the optional cells would be the citation-form **nom./acc.sg.** `tūn` plus ordinary strong singular obliques such as **gen.sg.** `tūnes` and **dat.sg.** `tūne`; but that would be explanatory expansion, not a current requirement.

## Recommended final report

Recommend a brief final report stating that the project regularly derives attested OE `tūn` from project input `*tūną`, while comparative sources cite cognate-set headwords such as `*tūna-` or `*tūnan ~ *tūnaz`. The report should explicitly reject treating `*tūnăn` as the live row input and should keep PGmc gender/history separate from the OE citation form.

## Data-change recommendations

- **TSV `PROTO`:** no change recommended.
- **TSV `PROTOFORM`:** no change recommended.
- **TSV `COUNTERPART`:** no change recommended.
- **TSV `DERIVATION_CLASS`:** no change recommended.
- **TSV `NOTE`:** **change recommended.** The note should stop attributing `oblique *tūnăn` to Kroonen and instead distinguish clearly between the comparative headword tradition (`*tūna-` in Kroonen; `*tūnan ~ *tūnaz` in Orel) and the row's actual derivational input `*tūną`. It should also avoid implying that the OE target itself is neuter just because the cognate-set proto is.
- **`oe_known_problems.tsv`:** no change recommended.
- **DEV_NOTES / dossier text:** no change recommended. There is no dedicated dossier for this lexeme, and the packet's sole `DEV_NOTES` hit is an unrelated `burg`/`burch` false positive rather than row-specific evidence.
