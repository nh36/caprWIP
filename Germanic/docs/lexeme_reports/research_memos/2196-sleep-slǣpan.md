# Research memo — 2196 sleep / slǣpan

## Starting point

- **ID:** 2196
- **CONCEPT:** sleep
- **COUNTERPART:** `slǣpan`
- **PROTO:** `*slḗpaną`
- **PROTOFORM:** `*slḗpaną`
- **DERIVATION_CLASS:** `regular`
- **NOTE:** `OE target: slǣp→slǣpan (inf. of str.v. class VII 'to sleep')`

The live row already derives correctly. The real issue is lexical framing: the row represents the Old English strong-verb infinitive `slǣpan`, but packet background material also surfaces `slǣp`, which is useful as a lookup hit yet unsafe as the row's actual OE target.

## Packet evidence assessment

- **Authoritative/current:** the live TSV row and the packet's compact derivation trace are the main evidence. They agree that row 2196 uses `*slḗpaną` and currently derives `slǣpan`.
- **Useful background:** the packet's `old_english_swadesh.tsv` hit (`to sleep` → `slǣpan`) supports the infinitive/citation-form target. The packet also correctly shows that no `oe_known_problems.tsv`, `DEV_NOTES`, dossier, or analysis file currently governs this row.
- **Stale or superseded / diagnostic only:** there is no clear row-specific stale project history in the packet. The only diagnostic tension is that the note's shorthand `slǣp→slǣpan` is not itself a good lexical analysis of the row.
- **Irrelevant or misleading:** the packet's `old_english_wiktionary.tsv` hit `sleep -> slǣp` is low-authority lexical-table evidence and does not identify the row's verbal infinitive. It is especially misleading because repo-local reference works cite the verb as `slǣpan/slæpan` or variant `slēpan`, while preterite forms are `slēp/slēap`, not `slǣp` [@ClarkHall1960; @BrightCassidyRingler1971].

## Additional repo research

Checked beyond the packet:

- `Germanic/data/germanic-aligned-final.tsv` around cognate set 457, confirming that the OE row in this set is the verb `slǣpan` from verbal `*slḗpaną`; the live row is not being rescued by a different paradigm-cell input.
- `Germanic/data/oe_known_problems.tsv` (checked; no row-specific entry).
- `Germanic/docs/lexeme_reports/coverage_audit.md`, confirming that row 2196 requires report coverage because of its non-empty `NOTE`.
- `Germanic/docs/lexeme_reports/source_inventory.md`, which explicitly ranks `old_english_wiktionary.tsv` and `old_english_swadesh.tsv` as supplementary/low-authority rather than primary philological authority.
- `docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt`, which gives `slæpan` with preterite `slēp, slēap` and also cross-references `slēpan` [@ClarkHall1960].
- `docs/references/bright_anglo_saxon_reader.vision.txt`, which lists `slæpan (slāpan), slēp slēpon slēpen` [@BrightCassidyRingler1971].
- `docs/references/brunner_1965_altenglische_grammatik.vision.txt` and `docs/references/bulbring_altenglisches_elementarbuch.txt`, which note West Saxon `slāpan/slæpan` and Anglian/Kentish `slēpan`, with analogical reshaping in the tradition [@SieversBrunner1965; @Bulbring1902].
- `docs/references/kroonen_etymological_dictionary_pgmc.vision.txt` and `docs/references/fulk_comparative_grammar_early_germanic.vision.txt`, which support PGmc `*slēpan-` / `*slēb-` as the comparative background behind OE `slæpan` [@Kroonen2013; @Fulk2018].

No row-specific dossier, analysis memo, or pilot report for this lexeme was found in the repo, and none was named in the packet or TSV note.

## Reconstruction and early-stage forms

Three levels need to stay separate:

1. **Cognate-set proto / etymological headword:** verbal PGmc `*slḗpaną` in the TSV, corresponding to comparative-dictionary `*slēpan-` [@Kroonen2013].
2. **Project input form for row 2196:** also `*slḗpaną`. This row is not using an alternate oblique cell, analogical rescue input, or reconstructed OE-stage substitute.
3. **OE target form:** `slǣpan`, i.e. the normalized infinitive/citation form chosen for the OE row.

The packet's derivation trace is internally consistent with that choice: Northwest Germanic long-*ē* lowering gives `*slǣpaną`, and the OE weak-tail steps surface `slǣpan`. Nothing in the repo evidence suggests that TSV `PROTO` or `PROTOFORM` should be replaced with a different proto shape. The real caution is that note-level shorthand `slǣp→slǣpan` should not be mistaken for the row's actual input history.

## Old English philology

Repo-local philology supports `slǣpan/slæpan` as the verbal citation form and shows a small but important web of related forms:

- **Attested/citation form:** local dictionaries and readers support verb `slæpan` / normalized `slǣpan` as the infinitive headword [@ClarkHall1960; @BrightCassidyRingler1971].
- **Inflected forms:** `slēp, slēap` are preterite singular forms; `slēpon` and `slēpen` belong to the rest of the strong-verb paradigm [@ClarkHall1960; @BrightCassidyRingler1971].
- **Dialect/spelling background:** Brunner and Bülbring indicate West Saxon `slāpan/slæpan`, with Anglian/Kentish `slēpan`; `slæpan` is thus a reasonable normalized OE target, but the row should not overclaim a single manuscript spelling beyond that [@SieversBrunner1965; @Bulbring1902].
- **Headword issue:** packet `slǣp` is better understood as noun/background lexical noise, not as the verbal lemma for row 2196. Even if one wanted to mention the noun `slǣp` 'sleep', that is a separate lexical item from the infinitive verb.

So the main philological point is simple: row 2196 is about the verb 'to sleep', and the citation form is `slǣpan`, not `slǣp`.

## Project problem and solution

This is not a sound-change failure and not an unresolved modelling gap. The FST already produces the intended OE form.

The project problem is that the row note and packet background can blur three different things:

- the verbal proto (`*slḗpaną`);
- the OE infinitive target (`slǣpan`);
- and low-authority lexical/headword noise (`slǣp`).

The correct project solution is therefore:

- keep row 2196 as the **verbal** row with `COUNTERPART` `slǣpan`;
- keep `PROTO` and `PROTOFORM` as `*slḗpaną`;
- treat `slǣp` in packet background as non-authoritative support material, not as the row's target or as evidence that the row needs a different derivation class.

## Paradigm probe

A paradigm probe is **not required** for this row. The live citation-form input already yields the intended OE infinitive `slǣpan`, and there is no unresolved choice of hidden paradigm cell driving the current solution.

If a purely optional philological probe were ever wanted, the relevant cells would be the infinitive/citation form `slǣpan`, preterite singular `slēp/slēap`, preterite plural `slēpon`, and past participle `slēpen`; but none of those probes is needed to settle the row's current project treatment.

## Recommended final report

Recommend a short final report stating that row 2196 represents the OE strong-verb infinitive `slǣpan` from verbal `*slḗpaną`, that the current derivation is already regular, and that packet `slǣp` material is supplementary headword noise rather than authority against the infinitive target. A brief note on attested variant spellings (`slāpan`, Angl./Kent. `slēpan`) would be useful background, but the report need not become a long dossier.

## Data-change recommendations

- **TSV `PROTO`:** no change recommended.
- **TSV `PROTOFORM`:** no change recommended.
- **TSV `COUNTERPART`:** no change recommended.
- **TSV `DERIVATION_CLASS`:** no change recommended.
- **TSV `NOTE`:** change recommended. The current `slǣp→slǣpan` wording is misleading because it blurs the verbal infinitive with a noun/background form and with non-citation paradigm material. It should instead say directly that row 2196 targets the OE infinitive `slǣpan` (strong verb, class VII), with `slǣp`-type packet hits treated only as supplementary background if mentioned at all.
- **`oe_known_problems.tsv`:** no change recommended.
- **`DEV_NOTES` or dossier text:** no change recommended. There is no row-specific dossier text to clean up, and no current `DEV_NOTES` entry needs correction for this lexeme.
