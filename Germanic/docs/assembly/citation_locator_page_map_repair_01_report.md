# Citation locator page-map repair 01 report

## Summary

- broad citations before: **187**
- broad citations after: **180**
- `page_markers_unreliable` before: **7**
- `page_markers_unreliable` after: **0**
- `source_preparation_needed` before: **2**
- `source_preparation_needed` after: **2**
- rows inspected: **9**
- locators added: **7**
- rows reclassified by status: **0**
- compact alpha regenerated: **yes** (`.md`, `.tex`, `.pdf`)

This pass treated the remaining source-quality tail as a narrow page-evidence
problem. Clark Hall proved recoverable after a small local page map was built
from visible printed numerals inside the `.vision.txt` witness; Bosworth-Toller
did not, because the surviving `fly` and `live` rows still expose example or
cross-reference material rather than a safely anchorable simplex headword page.

## Manifest update

`citation_locator_remaining_master.tsv` was refreshed from the
source-preparation-triage-01 baseline:

1. **7** rows were removed from the remaining-broad manifest after safe locator
   recovery.
2. **0** rows were reclassified in place.
3. **2** rows remain in the source-quality buckets after direct inspection.

Current remaining-status distribution:

| status | rows |
| :--- | ---: |
| `general_background` | 60 |
| `claim_not_isolated` | 56 |
| `headword_not_found` | 39 |
| `source_quarantined` | 14 |
| `multi_page_discussion` | 9 |
| `source_preparation_needed` | 2 |

The localized rows also appear in the regenerated
`lexical_volume_regular_compact_alpha_01.md`, so the repaired manifest and the
current reader-facing Markdown are synchronized.

## Derived page maps

One derived page-map file was created:

- `Germanic/docs/assembly/source_page_maps/clark_hall_1960_page_map.tsv`

It is deliberately tiny and local. Every row is based only on a visible printed
page numeral inside the relevant Clark Hall OCR block, plus the target headword
or family later in the same block.

No Bosworth-Toller page map was created, because the remaining Bosworth rows do
not yet expose a safely anchorable simplex headword page.

## Primary-source verification

Every new locator added in this pass has a matching row in
`citation_locator_primary_source_evidence.tsv`.

New evidence rows were added for:

- `CLMM01-0140`, `CLMM01-0142` — `ClarkHall1960, 335`
- `CLMM01-0144`, `CLMM01-0145` — `ClarkHall1960, 343`
- `CLMM01-0152` — `ClarkHall1960, 49`
- `CLMM01-0203` — `ClarkHall1960, 191`
- `CLMM01-0272` — `ClarkHall1960, 358`

No OCR line numbers, file offsets, search-result positions, or unverified PDF
page indexes were used as evidence.

## Source-by-source findings

### Clark Hall

Clark Hall was the productive source in this pass. The `.pdf` remained poor for
text search, but the `.vision.txt` witness exposes a repeatable pattern:

1. a block marker such as `=== page 350 ===`
2. a visible printed numeral inside that block, such as `335`
3. the target headword later in the same block

That was enough to recover a safe local page map for five zones:

- **brand** — **p. 49**
- **lungen** family — **p. 191**
- **windan** — **p. 335**
- **weald / wold** — **p. 343**
- **wiðig** — **p. 358**

Those five zones closed all seven remaining `page_markers_unreliable` rows.

### Bosworth-Toller

Bosworth-Toller remains the only unresolved source-quality blocker:

- **fly / flēogan** still yields only example or cross-reference material in the
  current local witnesses, not a clean simplex headword page.
- **live / lifeþ** still yields cross-reference material such as
  `a-libban, -lifian, -leofian` and scattered `libban` examples, but not a safe
  printed page for the simplex headword needed by the sentence.

The current Bosworth witnesses checked again in this pass were:

- `docs/references/bosworth_toller_anglo_saxon_dictionary.pdf`
- `docs/references/bosworth_toller_anglo_saxon_dictionary.vision.txt`
- `docs/references/legacy/anglosaxondictio00tolluoft.txt`

## Examples of successful page-anchor recovery

1. **wind / windan** — the Clark Hall block `=== page 350 ===` exposes printed
   numeral **335**, and `windan.` appears later in the same block, so both Clark
   Hall citation spans are now safely localized to **p. 335**.
2. **brand / brandes** — the Clark Hall block `=== page 064 ===` exposes
   printed numeral **49**, with `brand (ō) m.` later in the same block.
3. **withy / wīþiġ** — the Clark Hall block `=== page 373 ===` exposes printed
   numeral **358**, with `wiðig, wiði(g)e m.` later in the same block.

## Examples deliberately left broad

1. **fly / flēogan** — no safe Bosworth simplex headword page is visible in the
   available witnesses.
2. **live / lifeþ** — the current Bosworth material still exposes only
   cross-reference or example evidence, not a clean `libban` headword page.

## Source preparation still needed

The remaining source-quality tail is now only:

- **Bosworth-Toller** for simplex **flēogan**
- **Bosworth-Toller** for simplex **libban**

What is needed is not more sentence-splitting or Clark Hall page repair, but a
better Bosworth base-dictionary witness or OCR layer that exposes printed pages
for those simplex headwords directly.

## Compliance notes

- Every added locator has primary-source evidence recorded.
- No forbidden locator evidence was used.
- No generated TeX or PDF file was hand-edited.

## Recommendation

**C. return to claim isolation.** The page-map/source-quality tail is now down
to two Bosworth witness problems, and there are no `page_markers_unreliable`
rows left. Further broad-citation gains are more likely to come from the larger
`claim_not_isolated` bucket unless a materially better Bosworth witness is added
first.
