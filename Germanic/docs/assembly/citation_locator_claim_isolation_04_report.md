# Citation locator claim-isolation 04 report

## Summary

- broad citations before: **284**
- broad citations after: **262**
- `claim_not_isolated` before: **104**
- `claim_not_isolated` after: **82**
- rows inspected in this pass: **86**
- locators added in this pass: **19**
- sentences split in this pass: **2**
- unsupported broad citations removed after direct inspection: **3**
- rows reclassified in this pass: **0**
- page-anchor carryover rows resolved: **22**
- compact alpha regenerated: **yes** (`.md`, `.tex`, `.pdf`)

This pass focused first on the `claim_not_isolated` rows that had been reclassified out of `page_markers_unreliable` during page-anchor repair 01. Those were the highest-yield cases because the page had already been recovered, but the prose still combined dictionary or glossary evidence with broader derivational discussion. The edits in this pass were therefore concentrated on sentence-isolation and citation cleanup in the carryover tranche, while a wider non-carryover handbook/grammar inspection was used to map the remaining hard cases without forcing unsafe locators.

## Manifest update

`citation_locator_remaining_master.tsv` was refreshed from the page-anchor-repair-01 baseline:

1. **19** verified locator rows were removed from the remaining-broad manifest.
2. **3** rows were resolved by removing broad Clark Hall citations that were no longer needed after direct inspection:
   - `CLMM01-0034` (`gang / gang`, `ClarkHall1960`)
   - `CLMM01-0035` (`gang / gang`, `ClarkHall1960`)
   - `CLMM01-0072` (`net / nett`, `ClarkHall1960`)
3. No non-carryover rows were reclassified in this pass; those direct inspections were recorded for triage but left in place unless the prose itself changed.

Current remaining-status distribution:

| status | rows |
| :--- | ---: |
| `claim_not_isolated` | 82 |
| `headword_not_found` | 75 |
| `general_background` | 59 |
| `source_preparation_needed` | 15 |
| `source_quarantined` | 14 |
| `multi_page_discussion` | 9 |
| `page_markers_unreliable` | 8 |

The localized rows also appear in the regenerated `lexical_volume_regular_compact_alpha_01.md`, so the remaining manifest and current reader-facing Markdown are synchronized.

## Inspection coverage

The pass inspected **86** `claim_not_isolated` rows in total:

| source | rows inspected |
| :--- | ---: |
| `ClarkHall1960` | 24 |
| `Campbell1959` | 18 |
| `RingeTaylor2014` | 17 |
| `SieversBrunner1965` | 13 |
| `Kroonen2013` | 5 |
| `Orel2003` | 5 |
| `BrightCassidyRingler1971` | 4 |
| **total** | **86** |

Of these, **22** were page-anchor carryover rows from the page-repair pass. That carryover tranche produced all of this pass's file edits.

## Primary-source verification

Every new locator added in this pass has a matching row in `citation_locator_primary_source_evidence.tsv`.

New evidence rows added for:

- `CLMM01-0003` — `ClarkHall1960, 34`
- `CLMM01-0017` — `ClarkHall1960, 115`
- `CLMM01-0018` — `BrightCassidyRingler1971, 277`
- `CLMM01-0022` — `ClarkHall1960, 106`
- `CLMM01-0100`, `CLMM01-0101` — `ClarkHall1960, 281`
- `CLMM01-0127` — `ClarkHall1960, 343`
- `CLMM01-0181` — `ClarkHall1960, 159`
- `CLMM01-0216` — `ClarkHall1960, 162`
- `CLMM01-0221` — `ClarkHall1960, 210`
- `CLMM01-0234` — `ClarkHall1960, 247`
- `CLMM01-0249` — `ClarkHall1960, 276`
- `CLMM01-0265` — `ClarkHall1960, 171`
- `CLMM01-0335` — `ClarkHall1960, 197`
- `CLMM01-0365` — `BrightCassidyRingler1971, 347`
- `CLMM01-0374` — `ClarkHall1960, 193`
- `CLMM01-0383` — `ClarkHall1960, 48`
- `CLMM01-0419` — `BrightCassidyRingler1971, 346`
- `CLMM01-0443` — `ClarkHall1960, 245`

All 19 were checked directly in the cited local source files before being inserted into prose. No OCR line numbers, file offsets, search-result positions, or unverified PDF image-page numbers were used.

## Sources worked through

The edited carryover tranche concentrated on the now-page-usable dictionary and glossary sources:

- `ClarkHall1960`
- `BrightCassidyRingler1971`

The wider direct-inspection tranche also revisited the handbook and comparative tail without forcing edits:

- `Campbell1959`
- `RingeTaylor2014`
- `SieversBrunner1965`
- `Kroonen2013`
- `Orel2003`

## Successful split-and-localize fixes

| entry | source | locator | note |
| :--- | :--- | :--- | :--- |
| `begin / beġinnan` | `ClarkHall1960` | `34` | isolated Clark Hall's `beginnan` headword from the broader prefix and palatalization discussion |
| `fell / fell` | `ClarkHall1960`; `BrightCassidyRingler1971` | `115`; `277` | kept the lexical evidence sentence but separated the dictionary and glossary support from the derivational statement |
| `summer / sumer` | `ClarkHall1960` | `281` | localized both the main sentence and the form note on the same Clark Hall headword page |
| `shove / sċēaf` | `BrightCassidyRingler1971` | `347` | trimmed the Old English evidence sentence to the clean principal-parts line instead of citing both the paradigm and a quoted passage at once |
| `show (iptv.2sg) / sċēawa` | `BrightCassidyRingler1971` | `346` | localized the imperative-singular claim directly in the glossary entry |

## Rows deliberately left broad after direct inspection

Representative rows that were checked directly and still left broad:

| entry | source | final status | reason |
| :--- | :--- | :--- | :--- |
| `timber / timber` | `ClarkHall1960` | `claim_not_isolated` | the available Clark Hall witness only gave a weak cross-reference/variant trail, not a clean noun-headword block for the exact sentence |
| `night / niht` | `ClarkHall1960` | `claim_not_isolated` | direct inspection surfaced many incidental `niht` occurrences but not a clean headword block supporting the whole sentence safely |
| `wake / wacan` | `ClarkHall1960` | `claim_not_isolated` | the headword area remained mixed with contrastive verb-family material, so the prose still needs narrowing before a safe locator can be added |
| `forlorn / lēosan` | `RingeTaylor2014` | `claim_not_isolated` | the prefixed verb evidence and the participial pathway are still compressed into one broader analytical sentence |
| `staff / stæf` | `Campbell1959`; `SieversBrunner1965`; `RingeTaylor2014` | `claim_not_isolated` | the stem-class comparison remains a multi-source analytical argument rather than one locator-safe claim |

## Non-carryover inspection outcome

Beyond the edited carryover tranche, this pass directly inspected **64** non-carryover `claim_not_isolated` rows. That broader inspection confirmed that many handbook/grammar survivors still need genuine prose-level isolation rather than another blind locator sweep.

The main patterns were:

1. multi-source comparative sentences that still compress several source-specific claims into one clause;
2. phonological discussions where the source supports background analysis rather than a single locator-safe statement;
3. a smaller set of future candidates that may become localizable in a later pass, but were not edited here because this round stayed focused on the page-anchor carryover work.

## Safety checks

- Every newly added locator has a matching primary-source evidence row.
- No OCR line numbers were used as locators.
- No file offsets were used as locators.
- No search-result positions were used as locators.
- No unverified PDF page indexes were used as locators.
- No generated TeX or PDF was hand-edited.

## Output inspection

- Markdown regenerated: **yes**
- TeX regenerated: **yes**
- PDF regenerated: **yes**
- bibliography block still present: **yes** (`CSLReferences` found in regenerated TeX)

## Scope confirmation

- No TSV source data were edited.
- No FST files were edited.
- No compact trace source was edited.
- No bibliography files were edited.
