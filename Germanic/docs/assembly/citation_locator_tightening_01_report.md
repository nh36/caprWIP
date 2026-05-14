# Citation locator tightening 01 report

## Summary

- Broad citation occurrences scanned in the baseline compact-alpha Markdown: **502**
- Broad citation occurrences after this pass: **475**
- Net reduction: **27** broad occurrences
- Broad occurrences localized in this pass: **27**
- Broad occurrences left broad after regeneration: **475**
- Repository files changed: **15**
- Compact alpha regenerated: **yes** (`.md`, `.tex`, `.pdf`)
- Model entries edited: **no**

This pass stayed opportunistic. It tightened only claims that could be verified safely from the local page-marked sources, and it limited source edits to the regular-entry compact book-prose overlay.

## Method

- The current `lexical_volume_regular_compact_alpha_01.md` was inventoried first as the baseline.
- Regular entries were edited in `Germanic/docs/assembly/book_prose/regular_all_01/*.book.md`.
- No non-regular `.model.md` entry was changed in this pass, because the safe gains found here were all in the regular overlay layer.
- Locators were added only where the local source text gave a verifiable printed page marker tied to the cited headword or claim.
- No OCR line numbers, file offsets, search-result positions, or unverified PDF image-page numbers were used as locators.

## Source-by-source results

| Source | Broad before | Locators added | Left broad after | Notes |
| :--- | ---: | ---: | ---: | :--- |
| `Kroonen2013` | 82 | 6 | 76 | Tightened where the local OCR gave a clean PGmc headword page (`*burdi-`, `*baina-`, `*helma-`, `*hindō-`, `*meluk-`). |
| `Orel2003` | 49 | 2 | 47 | Tightened where the local OCR gave a clean dictionary headword page (`*bainan`, `*skellingaz`). |
| `ClarkHall1960` | 94 | 11 | 83 | Best yield of the pass; clean page-marked dictionary headwords made regular-entry tightening straightforward. |
| `BrightCassidyRingler1971` | 18 | 2 | 16 | Tightened the principal-parts citations for `helpan` and `healdan`. |
| `RingeTaylor2014` | 96 | 3 | 93 | Tightened only tightly anchored form-development discussions (`liehtan`, `meoluc`, and the harvest discussion already paired with Bammesberger). |
| `Campbell1959` | 66 | 0 | 66 | Left broad here; the surviving compact claims still needed claim-by-claim re-verification beyond the scope of this pass. |
| `Fulk2018` | 10 | 1 | 9 | Tightened the `līehtan` derivation where the local OCR gave a clean page marker. |
| `SieversBrunner1965` | 24 | 0 | 24 | Not targeted in this pass. Remaining citations are honest broad handbook/background citations. |
| `BosworthToller1898` | 31 | 0 | 31 | Left broad in this pass unless already localized elsewhere; the local supplement/base-dictionary split still limits safe bulk tightening. |
| `KlugeSeebold2011` | 12 | 0 | 12 | Still quarantined. |
| `Bammesberger1997` | 2 | 2 | 0 | Fully tightened for `harvest / hierfest` because the article pages directly anchor the relevant claims. |

## Entry examples

- `birth / byrd`:
  `[@Kroonen2013]` -> `[@Kroonen2013, 122]`
- `bone / bān`:
  `[@Kroonen2013; @Orel2003]` -> `[@Kroonen2013, 86; @Orel2003, 71]`
- `help / helpan`:
  `[@BrightCassidyRingler1971]` -> `[@BrightCassidyRingler1971, 57]`
- `light / līehtan`:
  `[@Fulk2018; @RingeTaylor2014]` -> `[@Fulk2018, 81; @RingeTaylor2014, 264]`
- `harvest / hierfest`:
  `[@Bammesberger1997; @RingeTaylor2014]` -> `[@Bammesberger1997, 224; @RingeTaylor2014]`

## Left broad

Important broad citations intentionally left broad include:

- `Campbell1959` cases such as `hold / healdan` and `shilling / sċilling`, where the compact claim still summarizes broader grammatical discussion rather than a single securely anchored page in this pass.
- `BosworthToller1898` cases such as `bone / bān` and other dictionary-headword citations where the local supplement/base-dictionary split still prevents safe page recovery from the available local text.
- `Kroonen2013` in `shilling / sċilling`, where the local material and internal notes support the analysis but this pass did not verify a clean page-specific headword citation strong enough to replace the broad reference.
- Background sources such as `SieversBrunner1965`, which were not the target of this opportunistic page-tightening pass.
- Quarantined `KlugeSeebold2011`, which remains broad throughout.

## Safety checks

- No OCR line numbers were used as locators.
- No source-file offsets were used as locators.
- No unverified PDF page-image indexes were used as locators.
- No invented page ranges were introduced.
- Pandoc regeneration of the compact Markdown, TeX, and PDF succeeded.

## Output inspection

- Markdown regenerated: **yes**
- TeX regenerated: **yes**
- PDF regenerated: **yes**
- Citation links still work: **yes** — the rebuilt PDF still contains link annotations (`960` `/Link` annotations detected by PDF parsing).
- Bibliography still appears: **yes** — the regenerated PDF ends with a visible `References` section and the expected bibliography entries.

## Recommendation

**A. Locator tightening was successful; continue with another targeted pass.**

This pass produced a real reduction in broad citations without crossing the source-safety rules. The next sensible step would be another targeted regular-entry pass or a deliberately scoped conditional-source pass, not a blanket saturation attempt.

## Scope confirmation

- No TSV source data were edited.
- No FST files were edited.
- No compact trace source was edited.
- No bibliography files were edited.
- No generated TeX/PDF was hand-edited.
