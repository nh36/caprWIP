# Source extraction ledger — filth / fȳlþ

Row 2335 was admitted to the selected corpus by the SC065 adjudication
(`sound_changes/audits/sc065-adjudication.md`), with its expansion
receipt in `sound_changes/cascade_baseline/corpus_expansion_sc065.tsv`.
This publication pass changes neither the admission nor the SC065
RETAIN verdict. PROTO and PROTOFORM are identical under the existing
metadata convention; the selected input *fūliþō is an assembled
morphological reconstruction (attested base plus attested suffix), not
a verbatim quotation of any dictionary.

| Source | Date / chronological position | Form(s) given | Stem class / morphology | Old English form(s) | Claim relevant to the entry | Citation key available? | Where this claim was found locally | Confidence / review note |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Kroonen | 2013; comparative citation | `*fūla-`; OS `fulitha` f. 'filth' among reflexes | adjective base; WGmc `-iþō` abstract cited as reflex | OE `fūl` (adjective) | Supports the PGmc base and attests an exact continental `-iþō` abstract on it; the OE noun is not cited there. | `Kroonen2013`, p. 158 | `pgmc_reconstructions/forms.tsv`, `filth-kroonen-2335`; held PDF, printed p. 158 confirmed by the dictionary's own index (fulitha, 158) | `page_image_checked` evidence reused from the SC065 admission; no new page reading claimed. |
| Orel | 2003; comparative citation | `*fūlaz` | adjective base | OE `fūl` 'foul, dirty, rotten' | Supports the base adjective; lists no `-iþō` abstract, so the composite is not attributed to him. | `Orel2003`, p. 121 | `pgmc_reconstructions/forms.tsv`, `filth-orel-2335`; held PDF, running folio 121 | `page_image_checked`; the f-section ends at `*fūōn` with no abstract-noun entry. A negative claim, recorded as such. |
| Toller Supplement | 1921; OE dictionary | `fylþ`; inflected `fylþu`; cognates OS `fúlitha`, OHG `fülida` | feminine abstract | `fylþ`, `fylþu` | Attests the noun (An. Ox. 3323 glossing *putor*; Scint. 38, 19 glossing *putredo*; Germ. 388, 12; An. Ox. 1790 `fylþu`) and names both continental cognates. | `Toller1921`, p. 276 | `pgmc_reconstructions/forms.tsv`, `filth-toller-2335`; `docs/references/bosworth_toller_anglo_saxon_dictionary.vision.txt`, page marker 276 | Supplement headword does not mark vowel quantity; length is taken from Clark Hall, not from Toller. |
| Clark Hall | 1960; OE dictionary | `fýlð` f. | feminine | normalized `fýlð` | Confirms lexical identity, feminine gender and the long root vowel; bracketed base `[ful]`. | `ClarkHall1960`, p. 125 | `pgmc_reconstructions/forms.tsv`, `filth-clarkhall-2335`; `docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt`, markers 125/126 | CAPR writes thorn for the dental fricative; the substitution changes no segment. |
| Campbell | 1959; class statement | `-iþō` abstracts: `strengþu`, `hǣlþ(u)`, `fȳlþ`, `þīefþ`, `wiermþu` | feminine abstracts in `-iþō` | endingless and `-u` nominatives | The class uniformly syncopates the medial vowel; the endingless nominative singular is derived analogically after the `lār` type. | `Campbell1959`, p. 236, §589.6 | `pgmc_reconstructions/forms.tsv`, `filth-campbell-2335`; `docs/references/campbell_old_english_grammar.txt` | Campbell's analogical route and CAPR's phonological route (raising > apocope > syncope) converge on the attested form; the difference is recorded in the entry, not suppressed. |
| Bammesberger | 1990; suffix morphology | `*-iþō`; `*mēriþō` > `mǣrþu`, `*deupiþō`/`*hauhiþō` > `hīehþu` | feminine abstract suffix | parallel OE abstracts | Documents the suffix type with invariant `-i-` before the dental ('durchweg der Vokal -i- vor dem Dental des Suffixes'); `fȳlþ` itself is not his example. | `Bammesberger1990`, pp. 117--118, §4.5 | `pgmc_reconstructions/forms.tsv`, `filth-bammesberger-2335`; `docs/references/bammesberger_1990_morphologie.txt` | Suffix-level evidence only; it licenses the formation type, not the particular composite. |
| Approved selected trace | current model, not historical source testimony | `*fūliþō > *fūliþu > *fȳliþu > *fȳliþ > fȳlþ` | regular feminine abstract; endingless nominative singular selected | `fȳlþ` | SC019 raising, SC055 i-umlaut, SC063 apocope and SC065 syncope yield the target; early syncope would yield unattested `*fūlþ`. | No bibliography attribution; rule links only | `debug_snapshots/oe_derivation_class_trace_report.compact.md`, `# filth`; `sound_changes/audits/sc065-adjudication.md`; SC065 chronology card | Computed trace supports the derivation and the SC055 < SC065 ordering witness, not the reconstruction's independent truth. |

## Attribution and unresolved limits

The six `filth-*-2335` source units in the pgmc_reconstructions
apparatus are used unchanged; all six bibliography keys already exist
in `docs/refs.bib`. The composite *fūliþō is CAPR's assembly of
Kroonen's base with Bammesberger's suffix type, directly paralleled by
OS fulitha and OHG fülida; it is not printed verbatim by Kroonen, Orel,
Campbell or Bammesberger, and the entry says so. Orel's silence on the
abstract is a verified negative (page image read to the end of the
f-section), not an oversight claim.

The dialect and date of the individual attestations (Aldhelm glosses,
*Liber scintillarum*) have not been newly established beyond Toller's
sigla; no manuscript has been newly consulted. Whether the endingless
nominative singular is phonological (apocope before syncope) or
analogical (Campbell's lār-type account) remains undecided by the
corpus; both routes converge on the attested form. The dental
enumeration of the executable SC065 statement is an architecture-level
proxy documented in the adjudication memo, not a claim about the
historical conditioning of the syncope, and this entry asserts nothing
about it.

## Publication ownership

The mature `.model.md` is discovered by the existing class-manifest
builder and matched by lexical item, exact input and exact target to
its own compact trace. It belongs to Part I, Regular derivations, in
ordinary alphabetical headword position; no editorial-order exception
is used. Canonical refresh owns the manifest, population, assembled
prose and index projections. This ledger is internal evidence
documentation and is not assembled as reader-facing text.
