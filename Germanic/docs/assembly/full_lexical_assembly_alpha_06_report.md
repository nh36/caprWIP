# Full lexical assembly alpha 06 report

## Summary

- form-width metrics were added
- form-column width is now content-sensitive
- a targeted fallback font-size was used for dense long-form trace boxes; `adjustbox` was **not** used
- Markdown, TeX, PDF, and a lightweight build log were regenerated
- original model entries were not edited

## Form-overflow fix

- Alpha 05 still favored label width too strongly. That solved the worst label wrapping, but it could leave the form column too narrow in dense Old English panels with long reconstructed forms, especially when the forms were also set ragged-right against the panel edge.
- The trace metrics now track, per panel:
  - maximum change-label length
  - maximum resulting-form length
  - number of resulting forms
  - count of long resulting forms
- Long forms are detected from the raw reconstructed-form strings, with special pressure starting around 9 characters and a stronger response at 10+ characters.
- The width logic now responds to form pressure in two places:
  - panel width selection widens the heavier side and shrinks the centre gutter sooner when one side contains very long forms
  - per-panel column selection now gives the form column more width when long forms are present, even if that means shrinking the label column slightly
- Label/form pairing was preserved by keeping the compact two-column side tables from alpha 05, reducing the inter-column gap slightly, and moving the form column away from `\raggedleft` so forms are no longer pushed into the box border.
- A small right-side safety margin was added inside the form column, and dense long-form trace boxes can now fall back to `\footnotesize` on a box-by-box basis instead of shrinking all trace boxes globally.

## Specific PDF checks

- spare / sparian — page 70
  - checked directly in the regenerated page image
  - long forms such as `*spærōjaną`, `*sparōjaną`, `*sparejąn`, `*spareian`, and `*sparian` stay inside the right border
  - this box now uses the targeted dense-panel `\footnotesize` fallback
- lung / lungen — page 62
  - checked directly in the regenerated page image
  - long forms such as `*lúngannju`, `*lúngennju`, and `*lúngennj` stay inside the box border
  - the added form width and right-side breathing room are visibly sufficient
- stem / stefn — page 72
  - `NWGmc Final Long O Raising *stébnu`
  - `PGmc B Allophony *stéβnu`
  - `OE High Vowel Apocope *stéβn`
  - the label/form pairs remain compact and readable
- three / þrīe — page 45
  - `PGmc Final Z Deletion *θréje` remains clean and does not show bad regression
- wasp / wæfs — page 46
  - `PGmc Final Z Deletion *wábsa` remains clean and the Old English panel still reads well
- knob / cnobba — page 114
  - `NWGmc U Lowering *knóbbô` remains compact
  - `OE Unstressed Long Vowel Shortening *knóbba` still reflects the longest-label wrapping pressure, but this is a label-wrap issue rather than form overflow

Also rechecked:

- beech / bōc — `OE High Vowel Apocope *bōk` remains clean
- bier / bǣr — `NWGmc Final Long O Raising *bḗru` and `OE High Vowel Apocope *bǣr` remain clean
- adder / nǣdre — no form-overflow issue; the residual pressure is still the long label
- bake / bacan — `OE Heavy Syllable Nasal Apocope *bakan` remains clean

## Regression checks

- language/stage labels remain roman: **yes**
- forms remain italic: **yes**
- derivation summaries still use `>`: **yes**
- Part page breaks remain: **yes**
- References page/heading remains: **yes**
- citation links remain: **yes** (`1043` PDF link annotations)
- bibliography remains: **yes**
- Unicode and trace boxes remain OK: **yes**

## Remaining issues

- the target form-overflow problem appears fixed in the sampled dense boxes
- the longest labels, especially `OE Unstressed Long Vowel Shortening`, can still wrap in a few tighter boxes such as knob and adder
- no trace-related overfull hbox warnings were surfaced in the captured build log; the log only contains the transient `pandoc: Ticker: poll failed` wrapper noise seen in earlier passes
- if another trace-only pass is wanted, it should focus on the remaining longest-label wrap cases rather than on form overflow

## Recommendation

**A. Form overflow is fixed; proceed to broader visual/style review.**

## Scope confirmation

- no model-entry prose or metadata was edited
- no TSV, FST, `report_manifest.tsv`, compact trace, packet, dev-note, research memo, bibliography, OCR/reference, or citation-locator report files were edited
- changes were limited to assembly scripts, regenerated outputs, the build log, and this report
