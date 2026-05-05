# Research memo — 2232 sunder / sundrian

## Starting point

- **ID:** 2232
- **CONCEPT:** sunder
- **COUNTERPART:** `sundrian`
- **PROTO:** `*súndrōjaną`
- **PROTOFORM:** `*súndrōjaną`
- **DERIVATION_CLASS:** `regular`
- **NOTE:** `OE class II weak verb sundrian 'to sunder, separate' (cf. ā-sundrian; well attested BT, Hall). Direct reflex of PGmc *sundrōjaną (Orel *Handbook* pp. 386-7). Earlier target sundor- erroneously slotted the unrelated adverb sundor < PGmc *sunþraz (different lexeme: comparative *-ter- formation, cf. Goth sundro, ON sundr); cogset siblings (NL afzonderen, E sunder, G sondern) confirm a class-II verb reading. Corrected per §17.29.`

The live row is already a corrected note-bearing `regular` entry. Its current `NOTE` records the essential project fix, while `HISTORY` still preserves the older Wiktionary-extraction provenance that likely caused the original mis-slotting.

## Packet evidence assessment

- **Authoritative/current:** the live TSV row; the packet's compact derivation trace, which gives `*súndrōjaną -> sundrian`; and the packet's cited `DEV_NOTES.md` §17.29 material where Orel, Kluge-Seebold, Hall, and Bosworth-Toller are used to separate verbal `sundrian` from adverbial `sundor` [@Orel2003; @KlugeSeebold2011; @ClarkHall1960; @BosworthToller1898].
- **Useful background:** the packet's mismatch-log chronology shows how the row was corrected; the bibliography candidate `Orel2003` is good; and the packet correctly flags the `old_english_wiktionary.tsv` hit as only supporting/diagnostic, not decisive.
- **Stale or superseded:** the packet's `old_english_wiktionary.tsv` hit `sunder -> sundor-`; the pre-correction state quoted inside `DEV_NOTES` `.1 Context`; and the mismatch-log line `sundrian: target sundor- -> sundrian` are project history, not current OE authority.
- **Irrelevant or misleading:** packet concept-name hits on `sundor`/`syndrian` without row-specific framing can blur three separate lexemes; debug-snapshot repeats of the same trace are not independent evidence.

## Additional repo research

Beyond the packet, I checked:

- `Germanic/data/germanic-aligned-final.tsv` around rows 1656/1655/2232/1654, confirming that the cognate set is verbal (`afzonderen`, `sunder`, `sundrian`, `sondern`) and that only the OE row carries the correction note.
- `Germanic/data/oe_known_problems.tsv`, which has no entry for row 2232 / `*súndrōjaną`.
- `Germanic/docs/DEV_NOTES.md` §17.29 directly, not just the packet extracts.
- `Germanic/docs/lexeme_reports/coverage_audit.md`, which marks row 2232 as report-worthy because `NOTE` is non-empty.
- `Germanic/docs/lexeme_reports/pilot/`, where I found no pilot report for this lexeme.
- `docs/references/legacy/orel_handbook_germanic_etymology.txt` 38011-38038, where Orel separates `*sunþraz`, `*sunþrjanan`, and `*sunþrōjanan`, with OE `sundor`, `syndrian`, and `sundrian` respectively [@Orel2003].
- `docs/references/kluge_seebold_etymologisches_woerterbuch.txt` 86073-86076, where German `sondern` is explicitly compared with OE `gesundrian` and ON `sundra` [@KlugeSeebold2011].
- `docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt` 38789-38790, 39770, and 4111, which distinguish `sundrian`, `syndrian`, and prefixed `āsundrian/āsyndrian` from adverbial `sundor` [@ClarkHall1960].
- `docs/references/bosworth_toller_anglo_saxon_dictionary.vision.txt` 8559-8560, 68308, and 68889-68898, which attest the prefixed verbal family `ā-sundrian` / `ge-syndrian` and keep it distinct from `sundor` [@BosworthToller1898].
- `docs/references/bright_anglo_saxon_reader.vision.txt` 15924-15933 and 25460, which likewise has `ā-sundrian` and separately `sundor`.
- A live FST probe via `oe_full_trace_report.apply_down`, which returns `['sundrian']` for `*súndrōjaną`.

I found no dedicated dossier or analysis file specifically named in the packet or TSV note for this lexeme.

## Reconstruction and early-stage forms

This row only stays clear if three levels are kept distinct.

1. **Comparative/cognate-set background:** Orel distinguishes three related but different items: adverb/adjective `*sunþraz > OE sundor`, class-I weak verb `*sunþrjanan > OE syndrian`, and class-II weak verb `*sunþrōjanan > OE sundrian` [@Orel2003].
2. **Project input form:** TSV `PROTO = PROTOFORM = *súndrōjaną`, the live transducer input for this row. Earlier `DEV_NOTES` prose also shows unaccented `*sundrōjaną`; that spelling difference is orthographic/editorial, not a different modelling choice.
3. **OE target form:** `sundrian`, the class-II weak infinitive/citation form represented by row 2232.

The crucial reconstruction point is that the row is **not** targeting the adverb `sundor`, and it is also **not** targeting the parallel i-mutated class-I verb `syndrian`. The packet note's statement that `sundrian` is the direct reflex of PGmc `*sundrōjaną` is sound so long as that is understood as the class-II verbal derivative, not as the older adverbial base `*sunþraz` itself.

## Old English philology

Repo-local philology supports a real OE verbal family distinct from the adverb.

- Clark Hall gives separate entries for `sundrian` and `syndrian`, both verbal, and separately for `sundor` as the adverb/first compound element [@ClarkHall1960].
- Bosworth-Toller and Bright most clearly attest the **prefixed** verbal family (`ā-sundrian`, `ā-syndrode`, `ge-syndrian`), again distinct from `sundor` [@BosworthToller1898].
- The adverb `sundor` is also visibly productive as a bound first element in compounds, which helps explain why the stale target appeared as `sundor-` with a hyphen rather than as a bare verb lemma.

The safest philological statement for the final report is therefore: row 2232 targets the OE weak-verb citation form `sundrian`; `syndrian` is a related but different verbal formation; and `sundor` is a separate adverbial lexeme. Repo-local evidence does not require stronger dialect or manuscript claims than that.

## Project problem and solution

The project problem was a **lexeme-selection error**, not a sound-law failure. The FST already derived `sundrian` regularly from `*súndrōjaną`; the mismatch existed because the OE `COUNTERPART` had been filled with `sundor-`, apparently from a Wiktionary `template:der` extraction that mixed the adverb and the verbs.

The current project solution is the right one:

- keep row 2232 as the class-II weak verb `sundrian`;
- keep `PROTO = PROTOFORM = *súndrōjaną` as the live project input;
- treat `sundor` as the separate adverbial lexeme and `syndrian` as a related but non-target verbal formation;
- preserve the correction history as background, but not as live uncertainty about the row's target.

## Paradigm probe

A paradigm probe is **not required** for this row.

This is not a late-analogy or hidden-cell case. The decisive issue is lexeme identity, and the live input already yields the intended infinitive `sundrian` uniquely. If someone later wanted a purely explanatory appendix, the only useful comparison would be the infinitive `*súndrōjaną -> sundrian` against a class-I comparator for `syndrian`, but that is not needed to settle row 2232.

## Recommended final report

Recommend a short final report saying that row 2232 is a regular OE class-II weak-verb row: the live input `*súndrōjaną` yields `sundrian`, the earlier target `sundor-` was a stale extraction error from the separate adverb `sundor`, and related `syndrian` should be mentioned only as a parallel non-target formation [@Orel2003; @KlugeSeebold2011; @ClarkHall1960].

## Data-change recommendations

- **TSV `PROTO`:** no change recommended.
- **TSV `PROTOFORM`:** no change recommended.
- **TSV `COUNTERPART`:** no change recommended.
- **TSV `DERIVATION_CLASS`:** no change recommended.
- **TSV `NOTE`:** no change recommended. The live note already captures the essential correction, the lexeme split, and the class-II analysis.
- **`oe_known_problems.tsv`:** no change recommended.
- **`DEV_NOTES` text:** no change recommended. `DEV_NOTES` §17.29 already preserves the correction history clearly enough, and I found no row-specific dossier text to revise.
- **Dossier text:** no change recommended; no dedicated dossier was found.
- **Additional non-requested cleanup:** `Germanic/data/old_english_wiktionary.tsv` still has stale `sunder -> sundor-`. That is outside the required fields above, but it remains the likeliest source of the historical mis-slotting and is worth future cleanup or explicit warning-labeling.
