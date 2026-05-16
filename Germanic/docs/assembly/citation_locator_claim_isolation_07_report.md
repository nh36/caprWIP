# Citation locator claim-isolation 07 report

## Summary

- Broad citations before pass: 180
- Broad citations after pass: 164
- `claim_not_isolated` before pass: 56
- `claim_not_isolated` after pass: 39
- Rows inspected: 56
- Locator-safe citation occurrences added: 16
- Sentences split or source clauses separated: 7
- Citations removed: 0

## Reclassification outcomes

- `CLMM01-0028` (`forlorn / lēosan`, `RingeTaylor2014`) -> `general_background`
- `CLMM01-0158` (`dill / dile`, `ClarkHall1960`) -> `source_preparation_needed`

## Source-by-source findings

### ClarkHall1960

This was the highest-yield source in the pass. Direct page-marked witness checks
recovered safe printed pages for:

- `forlēosan / forloren` -> p. 113
- `funden` -> p. 124
- `ræst` -> p. 239
- `timber / timbor` -> p. 294
- `bucca` -> p. 53
- `cnop / -cnoppa` -> p. 79

These let previously mixed dictionary clauses be narrowed without forcing new
analysis.

### SieversBrunner1965

Brunner yielded safe section anchors for the regular handbook rows:

- `token / tācn` -> `§155`
- `wash / wascan` -> `§392`
- `span / spannan` -> `§392`; `§396`

These were localized only where the section text directly named the cited forms.

### Kroonen2013

The local PDF preserved visible printed pages for the remaining comparative
dictionary rows:

- `*staba-` -> p. 471
- `*timbra-` -> p. 517
- `*wakan-` -> p. 568

These supported narrow comparative clauses in `staff / stæf`, `timber /
timber`, and `wake / wacan`.

### Orel2003

The local PDF preserved visible printed pages for:

- `*stabiz ~ *stabaz` -> p. 368
- `*bukkaz` / `*bukkōn` -> pp. 61-62

These allowed the comparative-dictionary clauses in `staff / stæf` and `buck /
bucc` to be split and localized safely.

### Campbell1959

Only one remaining row yielded a clean handbook anchor in this pass:

- `bucca` in the preserved-`u` exception set -> `§115`

This was enough to tighten the Campbell side of `buck / bucc`, but most other
remaining Campbell rows still read as broader phonological background or
multi-step synthesis rather than single locator-safe claims.

### RingeTaylor2014

Ringe and Taylor still contained some direct form evidence already localized in
earlier passes, but the remaining broad `forlorn / lēosan` clause was best
treated as background. After the Clark Hall dictionary clause was localized, the
surviving broad Ringe-Taylor citation no longer marked one clean isolatable
claim, so it was reclassified to `general_background` rather than forced into a
synthetic split.

## Examples of successful split-and-localize fixes

- `find / fundene`: the broad OE-evidence sentence was split so Clark Hall now
  carries `p. 124` for `funden` / `tō-fundennes`.
- `staff / stæf`: the comparative stem-class disagreement now separates
  Kroonen `p. 471` from Orel `p. 368`, instead of leaving both inside one broad
  mixed-source sentence.
- `buck / bucc`: the reconstruction clause now isolates Orel `pp. 61-62`, and
  the OE-evidence clause separately localizes Campbell `§115` and Clark Hall
  `p. 53`.

## Rows deliberately left broad or reclassified

- `forlorn / lēosan` (`RingeTaylor2014`): reclassified to
  `general_background`. The remaining broad citation now functions as overall
  derivational framing rather than a single locator-safe claim.
- `dill / dile` (`ClarkHall1960`): reclassified to
  `source_preparation_needed`. The current witness only yields the
  cross-reference-style `dile = dyle`, and this pass did not recover a safe
  printed-page anchor for that notice.
- The rest of the surviving `claim_not_isolated` bucket remains dominated by
  handbook-style synthetic arguments, especially in `Campbell1959` and
  `RingeTaylor2014`, where further atomization would risk misleadingly precise
  citation practice.

## Verification and evidence discipline

- Every locator added in this pass received a new row in
  `citation_locator_primary_source_evidence.tsv`.
- No OCR line numbers, file offsets, search-result positions, or unverified PDF
  page indexes were used as locator evidence.
- PDF-based locators were added only where the printed page number was visible
  in the local PDF witness itself.

## Outcome summary by status movement

- Localized and removed from the remaining-broad manifest: 16 rows
- Reclassified out of `claim_not_isolated` but still broad: 2 rows
  - to `general_background`: 1
  - to `source_preparation_needed`: 1

## Recommendation

**C. Do a final broad-citation classification review.**

This pass harvested the clean remaining wins from Clark Hall, Brunner,
Kroonen, Orel, and one Campbell clause. The surviving `claim_not_isolated`
rows are now disproportionately synthesis-heavy, so the next useful step is not
another aggressive localization pass but an honest review of which remaining
broad citations should stay broad, move to `general_background`, or be carried
as genuine multi-page discussion.
