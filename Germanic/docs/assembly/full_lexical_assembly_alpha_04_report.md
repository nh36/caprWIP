# Full lexical assembly alpha 04 report

## Summary

- trace-box internal geometry was changed
- a flexible middle gutter was introduced and now absorbs the spare horizontal
  space between the Earlier Germanic and Old English halves
- label/form pairs are now closer together within each side
- dynamic width logic remains in use and now drives compact side-pair widths
- `adjustbox` was **not** used
- Markdown, TeX, and PDF were regenerated
- original model entries were not edited

## Layout change

- The old layout still behaved like two wide local panels. Even after the alpha 03
  width tuning, each label/form pair could end up stretched across too much local
  space, so short labels such as `OE High Vowel Apocope` could still wrap or feel
  detached from their forms.
- The new layout uses:
  1. a compact Earlier Germanic side box,
  2. a flexible centre gutter,
  3. a compact Old English side box.
- Each side now renders its trace rows as a compact two-column `tabular`
  (label column + nearby form column with a modest fixed gap), rather than as a
  full-width local `tabularx` that pushed forms to the far edge of the side.
- The outer trace box uses an internal `tabularx` with:
  - fixed-width left side,
  - flexible middle `X` gutter,
  - fixed-width right side.
- Content-sensitive widths are still chosen from simple per-side metrics:
  - number of non-`[no change]` rows
  - total change-name length
  - maximum change-name length
  - presence of known long labels such as `OE High Vowel Apocope`,
    `OE Heavy Syllable Nasal Apocope`, and
    `OE Unstressed Long Vowel Shortening`
- Current width modes:
  - balanced: `0.41 / gutter / 0.41`
  - Old-English-heavy: `0.30 / gutter / 0.50`
  - Earlier-Germanic-heavy: `0.50 / gutter / 0.30`

## Specific PDF checks

- beech / bōc — page 3
  - checked
  - `OE High Vowel Apocope *bōk` now reads as a clear pair
- bier / bǣr — page 4
  - checked
  - `NWGmc Final Long O Raising *bḗru`
  - `NWGmc Long E Lowering *bǣru`
  - `OE High Vowel Apocope *bǣr`
  - all read as clear label/form pairs
- lind / lind — page 24
  - checked
  - `OE High Vowel Apocope *línd` now reads as a clear pair
- both / bū — page 6
  - checked
  - `NWGmc Stressed Monosyllable O Raising *bū` reads as a clear pair
  - Old English `[no change]` still renders sensibly
- adder / nǣdre — page 2
  - checked
  - `OE Unstressed Long Vowel Shortening *nǣdræ` now reads as a clear pair
- bake / bacan — page 2
  - checked
  - `OE Heavy Syllable Nasal Apocope *bakan` now reads as a clear pair

## Regression checks

- derivation summaries still use `>`: **yes**
- Part page breaks remain: **yes**
- References page/heading remains: **yes**
- citation links remain: **yes** (`1043` PDF link annotations detected)
- Unicode and boxed traces remain OK: **yes**

## Remaining issues

- The trace boxes are materially improved, but a full visual sweep is still worth
  doing for any edge-case wraps beyond the sampled entries.
- The references section now begins on page 127 rather than 126 because the new
  trace layout slightly changes pagination; this is not a regression, but it is a
  page-number shift from alpha 03.
- The Docker wrapper still does not preserve a LaTeX log artifact, so overfull-box
  diagnostics are not yet collected automatically.

## Recommendation

**A. Trace-box readability is acceptable; proceed to broader visual/style review.**

## Scope confirmation

- no model-entry prose or metadata was edited
- no TSV, FST, `report_manifest.tsv`, compact trace, packet, dev-note, research
  memo, bibliography, OCR/reference, or citation-locator report files were edited
- changes were limited to assembly scripts, regenerated outputs, and this report
