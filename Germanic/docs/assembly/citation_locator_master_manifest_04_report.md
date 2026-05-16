# Citation locator master manifest 04 report

## Summary

- broad citations before: **397**
- broad citations after: **387**
- `not_yet_inspected` before: **132**
- `not_yet_inspected` after: **0**
- rows inspected in this pass: **132**
- locators added in this pass: **10**
- rows left broad after direct inspection: **122**
- non-regular rows inspected: **127**
- regular book-prose rows inspected: **5**
- compact alpha regenerated: **yes** (`.md`, `.tex`, `.pdf`)

Newly classified former `not_yet_inspected` rows:

| status | rows |
| :--- | ---: |
| `claim_not_isolated` | 68 |
| `page_markers_unreliable` | 32 |
| `general_background` | 11 |
| `headword_not_found` | 8 |
| `multi_page_discussion` | 3 |

The pass achieved the narrow goal of this round: the remaining `not_yet_inspected` queue has been eliminated rather than merely reduced.

## Manifest update

`citation_locator_remaining_master.tsv` was refreshed in place from the live pass-03 tail:

1. all ten rows that received verified locators were removed from the remaining-broad manifest;
2. all other former `not_yet_inspected` rows were reclassified with explicit statuses, reasons, and next actions;
3. the manifest now reflects a remaining-broad queue of **387** rows with **0** `not_yet_inspected`.

Current remaining-status distribution:

| status | rows |
| :--- | ---: |
| `claim_not_isolated` | 173 |
| `page_markers_unreliable` | 80 |
| `general_background` | 55 |
| `headword_not_found` | 54 |
| `source_quarantined` | 14 |
| `multi_page_discussion` | 9 |
| `source_preparation_needed` | 2 |

## Primary-source verification

Every new locator added in this pass has a matching row in `citation_locator_primary_source_evidence.tsv`.

New evidence rows added for:

- `CLMM01-0064`, `CLMM01-0066` — `Lloyd1966, 738`
- `CLMM01-0307` — `SieversBrunner1965, §245`
- `CLMM01-0334` — `SieversBrunner1965, §226`
- `CLMM01-0337` — `SieversBrunner1965, §231`
- `CLMM01-0360` — `ClarkHall1960, 257`
- `CLMM01-0400`, `CLMM01-0409` — `Orel2003, 285`
- `CLMM01-0417`, `CLMM01-0421` — `Orel2003, 337`

All ten were checked directly in the cited local source files before being added to prose.

## Sources worked through

| source | inspected | locators added | main unresolved outcome(s) |
| :--- | ---: | ---: | :--- |
| `RingeTaylor2014` | 29 | 0 | mostly `claim_not_isolated` finite-cell or development sentences |
| `ClarkHall1960` | 18 | 1 | mostly `page_markers_unreliable` headword evidence |
| `Kroonen2013` | 16 | 0 | mostly `claim_not_isolated` or `general_background`; a few `headword_not_found` |
| `Orel2003` | 16 | 4 | mix of successful lexeme-level dictionary locators and unresolved broad comparative background |
| `Campbell1959` | 16 | 0 | all left `claim_not_isolated` |
| `SieversBrunner1965` | 15 | 3 | mix of successful section locators and unresolved broader phonological discussion |
| `BosworthToller1898` | 5 | 0 | all left `page_markers_unreliable` |
| `BrightCassidyRingler1971` | 4 | 0 | all left `page_markers_unreliable` |
| `Fulk2018` | 3 | 0 | split among `claim_not_isolated`, `general_background`, `multi_page_discussion` |
| `Lloyd1966` | 2 | 2 | both localized |
| `Kroonen2011` | 2 | 0 | one `page_markers_unreliable`, one `headword_not_found` |
| `Adamczyk2001` | 1 | 0 | `claim_not_isolated` |
| `Crist2002` | 1 | 0 | `multi_page_discussion` |
| `Kilday2024` | 1 | 0 | `multi_page_discussion` |
| `Bulbring1902` | 1 | 0 | `claim_not_isolated` |
| `Sweet1953` | 1 | 0 | `page_markers_unreliable` |
| `Seebold1970` | 1 | 0 | `page_markers_unreliable` |

## Successful locator additions

| entry | source | locator | source file checked | note |
| :--- | :--- | :--- | :--- | :--- |
| `lid / hlid` | `Lloyd1966` | `738` | `docs/references/lloyd_1966_a_umlaut_of_i.txt` | localized both the main sentence and the form note |
| `hammer / hameres` | `SieversBrunner1965` | `§245` | `docs/references/brunner_1965_altenglische_grammatik.txt` | localized the `hamor — hamores` paradigm line |
| `man / mannes` | `SieversBrunner1965` | `§226` | `docs/references/brunner_1965_altenglische_grammatik.txt` | localized `man mannes` |
| `man / mannes` | `SieversBrunner1965` | `§231` | `docs/references/brunner_1965_altenglische_grammatik.txt` | localized the word-final simplification clause |
| `shoulder / sċuldrum` | `ClarkHall1960` | `257` | `docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt` | localized the ordinary dictionary headword |
| `lick (iptv.2sg) / licca` | `Orel2003` | `285` | `docs/references/orel_handbook_germanic_etymology.vision.txt` | localized the lexeme-level weak-verb reconstruction |
| `lick (3sg) / liccaþ` | `Orel2003` | `285` | `docs/references/orel_handbook_germanic_etymology.vision.txt` | same Orel entry reused for the 3sg companion row |
| `show (iptv.2sg) / sċēawa` | `Orel2003` | `337` | `docs/references/orel_handbook_germanic_etymology.vision.txt` | localized the lexeme-level weak-verb citation |
| `show (3sg) / sċēawaþ` | `Orel2003` | `337` | `docs/references/orel_handbook_germanic_etymology.vision.txt` | same Orel entry reused for the 3sg row |

## Rows deliberately left broad after direct inspection

| entry | source | final status | reason |
| :--- | :--- | :--- | :--- |
| `span / spannan` | `SieversBrunner1965` | `claim_not_isolated` | the available Brunner hit is embedded in a broader phonological discussion rather than a clean locator-safe citation sentence |
| `town / tūn` | `SieversBrunner1965` | `headword_not_found` | the local Brunner text did not yield a safe direct hit for the exact citation claim |
| `neck / hnecca` | `Kroonen2011` | `page_markers_unreliable` | the n-stem discussion is present, but the available local text did not give a stable printed page anchor |
| `spare / sparian` | `Kroonen2013` | `claim_not_isolated` | the current sentence merges inherited class-III background with later class-II refashioning |
| `meed / meorde` | `Fulk2018` | `multi_page_discussion` | the disputed `mēd / meorde` history is discussion-level and not safely reducible to one locator |
| `withy / wīþiġ` | `Orel2003` | `general_background` | Orel is useful for the wider cognate set, but not for a tighter locator-safe suffix argument as currently phrased |

## Safety checks

- No OCR line numbers were used as locators.
- No file offsets were used as locators.
- No search-result positions were used as locators.
- No unverified PDF page indexes were used as locators.
- No locators were copied from prior reports without direct rechecking in the local source file.
- No invented page ranges were introduced.
- No new `KlugeSeebold2011` locators were introduced.
- No `p.` / `pp.` syntax remains inside Pandoc page locators in the edited source/output files checked for this pass.

## Output inspection

- Markdown regenerated: **yes**
- TeX regenerated: **yes**
- PDF regenerated: **yes**
- TeX still contains the citeproc bibliography block: **yes**
- PDF still contains annotation objects / URI links: **yes**

## Scope confirmation

- No TSV source data were edited.
- No FST files were edited.
- No compact trace source was edited.
- No bibliography files were edited.
- Generated TeX/PDF were regenerated, not hand-edited.

## Recommendation

**A. Continue with another manifest-driven citation pass.**

The remaining queue is now cleaner than it was at the start of pass 04: the stale `not_yet_inspected` tail is gone, and the residue is now explicitly partitioned into real categories (`claim_not_isolated`, `page_markers_unreliable`, `general_background`, `headword_not_found`, `multi_page_discussion`, quarantines, and source-preparation cases). A subsequent pass can therefore target one unresolved class at a time instead of spending effort on initial inspection.
