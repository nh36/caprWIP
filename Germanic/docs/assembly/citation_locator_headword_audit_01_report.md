# Citation locator headword audit 01 report

## Summary

- broad citations before: **246**
- broad citations after: **219**
- `headword_not_found` before: **75**
- `headword_not_found` after: **39**
- rows inspected in this pass: **53**
- locators added in this pass: **26**
- manifest rows resolved from the queue in this pass: **27**
- rows reclassified in this pass:
  - `claim_not_isolated`: **2**
  - `page_markers_unreliable`: **7**

This pass concentrated on the dictionary-heavy tail of the locator queue and treated `headword_not_found` literally: each row was revisited with layered searching for spelling variants, normalized forms, prefixed forms, reconstructed spellings, and likely OCR distortions. The productive sources were `ClarkHall1960`, `Kroonen2013`, and `Orel2003`; several apparent misses turned out to be recoverable headwords, while a smaller but important cluster proved to be page-anchor failures rather than genuine headword failures.

## Manifest update

`citation_locator_remaining_master.tsv` was refreshed from the claim-isolation-05 baseline:

1. **27** rows were removed from the remaining-broad manifest after direct source verification.
2. **9** rows were reclassified in place:
   - **7** from `headword_not_found` to `page_markers_unreliable`
   - **2** from `headword_not_found` to `claim_not_isolated`
3. The rest of the inspected rows were left in place as genuine `headword_not_found` cases.

Current remaining-status distribution:

| status | rows |
| :--- | ---: |
| `claim_not_isolated` | 68 |
| `general_background` | 59 |
| `headword_not_found` | 39 |
| `source_preparation_needed` | 15 |
| `page_markers_unreliable` | 15 |
| `source_quarantined` | 14 |
| `multi_page_discussion` | 9 |

The localized rows also appear in the regenerated `lexical_volume_regular_compact_alpha_01.md`, so the manifest and reader-facing Markdown remain synchronized.

## Headword-audit inventory

Created:

- `Germanic/docs/assembly/citation_locator_headword_audit_01_inventory.tsv`

The inventory records **53** inspected rows with:

- layered search terms actually used
- whether a headword, cross-reference, or example was found
- whether a safe page or section marker was present
- whether the row was resolved, reclassified, or left unresolved

## Primary-source verification

Every newly added locator in this pass has a matching row in `citation_locator_primary_source_evidence.tsv`.

New evidence rows were added for:

- `CLMM01-0026`, `CLMM01-0027` — `Kroonen2013, 374`; `Orel2003, 282`
- `CLMM01-0038` — `ClarkHall1960, 134`
- `CLMM01-0045`, `CLMM01-0046` — `Kroonen2013, 260`
- `CLMM01-0089` — `Kroonen2013, 493`
- `CLMM01-0102`, `CLMM01-0105` — `Orel2003, 426`
- `CLMM01-0118`, `CLMM01-0119` — `Kroonen2013, 566`; `ClarkHall1960, 356`
- `CLMM01-0133`, `CLMM01-0134`, `CLMM01-0136` — `Kroonen2013, 618`; `Orel2003, 492`; `Kroonen2013, 618`
- `CLMM01-0143` — `Kroonen2013, 611`
- `CLMM01-0175` — `ClarkHall1960, 63`
- `CLMM01-0202` — `Kroonen2013, 384`
- `CLMM01-0226`, `CLMM01-0228` — `Kroonen2013, 423`; `Orel2003, 320`
- `CLMM01-0236` — `Orel2003, 319` (manifest/evidence synchronization for a live locator already present in prose)
- `CLMM01-0319` — `ClarkHall1960, 188`
- `CLMM01-0339`, `CLMM01-0342` — `Kroonen2013, 410`; `Orel2003, 311`
- `CLMM01-0356`, `CLMM01-0357` — `Kroonen2013, 445`
- `CLMM01-0379` — `ClarkHall1960, 193`
- `CLMM01-0391`, `CLMM01-0396` — `ClarkHall1960, 186`

## Sources worked through

This pass focused on the highest-yield `headword_not_found` sources:

- `ClarkHall1960`
- `Kroonen2013`
- `Orel2003`

Inspection counts by source in this pass:

| source | rows inspected |
| :--- | ---: |
| `ClarkHall1960` | 23 |
| `Kroonen2013` | 16 |
| `Orel2003` | 14 |

## Examples of successful recoveries

| entry | source | locator | recovery |
| :--- | :--- | :--- | :--- |
| `give / ġiefan` | `ClarkHall1960` | `134` | recovered from nearby lemma and form lines (`giefan`, `geaf`, `giefen`) rather than the exact first-search spelling |
| `town / tūn` | `Kroonen2013`; `ClarkHall1960` | `566`; `356` | both comparative and OE dictionary headwords were present once the search was run against the actual noun form rather than only normalized prose |
| `will / willa` | `Kroonen2013`; `Orel2003` | `618`; `492` | recovered by switching from verb-side search assumptions to the noun-side headword entries |
| `nose / nosu` | `Kroonen2013`; `Orel2003` | `423`; `320` | recovered by distinguishing the remodeled zero-grade `*nusō` line from Orel's full-grade `*nasō` notation |
| `learn (iptv.2sg) / liorna`; `learn (3sg) / liornaþ` | `ClarkHall1960` | `186` | recovered through the dictionary headword `leornian`, which safely supports the finite-cell comparison even though the exact finite form is not the dictionary lemma |

## Reclassified but still broad

The most useful reclassification pattern in this pass was:

1. **Found but not safely pageable** → `page_markers_unreliable`
   - `wind / windan`
   - `wold / weald`
   - `brand / brandes`
   - `lung / lungen`
   - `bore (3sg) / boraþ`

2. **Found, but the current sentence overstates what the localized source directly shows** → `claim_not_isolated`
   - `sap / sæp` (`Kroonen2013`)
   - `withy / wīþiġ` (`ClarkHall1960`)

These were useful outcomes: they reduce the genuinely missing-headword bucket and clarify what kind of follow-up work is actually needed.

## Rows left unresolved after layered search

Examples deliberately left as genuine `headword_not_found` after layered search:

| entry | source | reason |
| :--- | :--- | :--- |
| `hedge / heġġ` | `ClarkHall1960` | only compound material surfaced, not a safe simplex dictionary headword |
| `shilling / sċilling` | `Kroonen2013` | the internal `*skeld-linga-` analysis was visible, but not the exact cited headword pair `*skellinga- ~ *skillinga-` |
| `spar / spearra` | `Orel2003` | no safe entry-level hit was recovered for the noun after layered search |
| `live / lifeþ` | `ClarkHall1960` | only cross-reference material surfaced, not enough for the current finite-form sentence |
| `tap / tæppa` | `Orel2003` | only index-level material surfaced in this witness, not a safe entry paragraph |

Among the **53** inspected rows, **17** remained genuinely `headword_not_found` after layered search.

## Support-package updates

All changed non-regular model entries had their paired support files updated:

- `.source_ledger.md`
- `.reviewer_checklist.md`
- `.model_implementation_report.md`

Each received a short headword-audit note recording the verified source used for the tightened or reclassified citation.

## Safety checks

- No OCR line numbers were used as locators.
- No file offsets were used as locators.
- No search-result positions were used as locators.
- No unverified PDF page indexes were used as locators.
- Clark Hall rows were only localized where a printed page number was directly visible in the local witness.
- Every newly added locator has a matching primary-source evidence row.

## Output inspection

- Markdown regenerated: **yes**
- TeX regenerated: **yes**
- PDF regenerated: **yes**

## Scope confirmation

- No TSV source data were edited.
- No FST files were edited.
- No compact trace source was edited.
- No bibliography files were edited.
- No generated TeX/PDF files were hand-edited.

## Recommendation

**B. return to claim isolation.**

This pass removed most of the easy dictionary/glossary false negatives from `headword_not_found`, dropping that bucket from **75** to **39**. The largest unresolved bucket is now again `claim_not_isolated` (**68**), and the headword audit has already flushed a separate page-anchor problem into `page_markers_unreliable`, so the next highest-yield work is once more sentence-level claim isolation rather than another broad headword sweep.
