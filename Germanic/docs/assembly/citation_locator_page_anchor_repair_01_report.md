# Citation locator page-anchor repair 01 report

## Summary

- broad citations before: **295**
- broad citations after: **284**
- `page_markers_unreliable` before: **82**
- `page_markers_unreliable` after: **8**
- rows inspected in this pass: **79**
- locators added in this pass: **11**
- rows reclassified out of `page_markers_unreliable`: **63**
- rows left page-anchor blocked after direct inspection: **5**
- rows not reinspected in this pass: **3**
- compact alpha regenerated: **yes** (`.md`, `.tex`, `.pdf`)

This pass repaired the page-anchor bucket by separating true anchor failures from two other situations that had been mixed into the same queue: rows where a printed page had in fact been recovered but the sentence still needed claim isolation, and rows where the available local witness did not safely preserve the needed headword block at all. The result is that `page_markers_unreliable` is now a small residual tail rather than the dominant unresolved bucket.

## Manifest update

`citation_locator_remaining_master.tsv` was refreshed from the claim-isolation-03 baseline:

1. **11** verified locator rows were removed from the remaining-broad manifest.
2. **30** rows were reclassified from `page_markers_unreliable` to `claim_not_isolated` because a recoverable printed page existed but the current prose still combines multiple claims.
3. **20** rows were reclassified from `page_markers_unreliable` to `headword_not_found`.
4. **13** rows were reclassified from `page_markers_unreliable` to `source_preparation_needed`, chiefly in `BosworthToller1898`.
5. One surviving `BosworthToller1898` row was refreshed so its citation span and sentence match the live prose after Bright was localized:
   - `CLMM01-0345` (`meed / meorde`, `BosworthToller1898`)

Current remaining-status distribution:

| status | rows |
| :--- | ---: |
| `claim_not_isolated` | 104 |
| `headword_not_found` | 75 |
| `general_background` | 59 |
| `source_preparation_needed` | 15 |
| `source_quarantined` | 14 |
| `multi_page_discussion` | 9 |
| `page_markers_unreliable` | 8 |

The localized rows also appear in the regenerated `lexical_volume_regular_compact_alpha_01.md`, so the repaired manifest and current reader-facing Markdown are synchronized.

## Primary-source verification

Every new locator added in this pass has a matching row in `citation_locator_primary_source_evidence.tsv`.

New evidence rows added for:

- `CLMM01-0126` — `Kroonen2013, 575`
- `CLMM01-0149` — `ClarkHall1960, 341`
- `CLMM01-0189` — `ClarkHall1960, 180`
- `CLMM01-0230` — `ClarkHall1960, 810`
- `CLMM01-0232` — `Orel2003, 319`
- `CLMM01-0257` — `Orel2003, 197`
- `CLMM01-0259` — `ClarkHall1960, 170`
- `CLMM01-0261` — `Orel2003, 201`
- `CLMM01-0289` — `Kroonen2013, 54`
- `CLMM01-0304` — `Kroonen2013, 206`
- `CLMM01-0344` — `BrightCassidyRingler1971, 328`

All 11 were checked directly in the cited local source files before being inserted into prose. No OCR line numbers, file offsets, search-result positions, or unverified PDF image-page numbers were used.

## Sources worked through

The pass concentrated on the highest-yield dictionary-style blockers:

| source | start rows | inspected | localized | reclassified | remaining `page_markers_unreliable` | finding |
| :--- | ---: | ---: | ---: | ---: | ---: | :--- |
| `ClarkHall1960` | 43 | 43 | 4 | 39 | 0 | Printed page numerals are usable, but most survivors were misbucketed: they are really claim-isolation or headword-search problems. |
| `BosworthToller1898` | 13 | 13 | 0 | 13 | 0 | The available witness is too supplement-like or incomplete for safe base-dictionary localization; these rows belong in `source_preparation_needed`. |
| `BrightCassidyRingler1971` | 5 | 5 | 1 | 4 | 0 | Glossary pages are recoverable, but most Bright survivors needed claim isolation rather than page repair. |
| `Orel2003` | 9 | 9 | 3 | 4 | 2 | The local dictionary witness is usable for several entries, but `sieve` and `fright` still lack safe printed-page anchoring. |
| `Kroonen2013` | 9 | 9 | 3 | 3 | 3 | The local dictionary witness is usable for several entries, but `sea` and `whale` still remain unsafe to anchor from the current text. |
| `Kroonen2011` | 1 | 0 | 0 | 0 | 1 | Deferred singleton tail; current witness still lacks a safe printed-page anchor. |
| `Seebold1970` | 1 | 0 | 0 | 0 | 1 | Deferred singleton tail. |
| `Sweet1953` | 1 | 0 | 0 | 0 | 1 | Deferred singleton tail. |

## Successful page-anchor recoveries

| entry | source | locator | note |
| :--- | :--- | :--- | :--- |
| `wash / wascan` | `Kroonen2013` | `575` | recovered the comparative headword `*waskan-` in the local dictionary stream |
| `wasp / wæfs` | `ClarkHall1960` | `341` | localized the dictionary headword practice cited for later `wæps`-type spellings |
| `sap / sæp` | `Orel2003` | `319` | recovered Orel's comparative notation `*sapōn ~ *sapan` safely on a printed page |
| `whale / hwæl` | `Orel2003`; `ClarkHall1960` | `197`; `170` | localized both the comparative headword and the OE dictionary headword |
| `meed / meorde` | `BrightCassidyRingler1971` | `328` | recovered the glossary entry `mēd (meord)` and refreshed the surviving Bosworth row accordingly |

## Rows deliberately left broad after direct inspection

| entry | source | final status | reason |
| :--- | :--- | :--- | :--- |
| `begin / beġinnan` | `ClarkHall1960` | `claim_not_isolated` | the page for `beginnan` is recoverable, but the sentence also compresses broader derivational material and needs splitting before safe localization |
| `bone / bān` | `BosworthToller1898` | `source_preparation_needed` | the available local witness is not a safely citable base-dictionary layer for the needed headword block |
| `sea / sǣ` | `Kroonen2013` | `page_markers_unreliable` | the local witness remained too noisy to recover a printed page anchor safely |
| `sieve / sife` | `Orel2003` | `page_markers_unreliable` | the exact Orel entry was not safely page-anchored in the available witness |
| `fright / fyrhte` | `Orel2003` | `page_markers_unreliable` | candidate hits landed in the wrong lexical neighborhood, so no printed page was added |

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
