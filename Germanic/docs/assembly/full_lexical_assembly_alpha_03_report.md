# Full lexical assembly alpha 03 report

## Summary

- generated derivation summaries now use `>` rather than `→`
- arrow usage was audited in regenerated Markdown and TeX
- trace-box width logic was changed from fixed widths to a simple dynamic-width
  heuristic
- `adjustbox` was **not** used
- references now begin on a fresh page with a visible heading
- Markdown, TeX, and PDF were regenerated
- original model entries were not edited

## Arrow notation

- Changed `derivation_summary()` in `build_full_lexical_volume.py` so the
  generated summary path now uses plain `>` rather than `$\rightarrow$`.
- `>` is now used in generated derivation summaries such as:
  - `_\*nḗdrōn_ > _nǣdre_`
  - `_\*bákaną_ > _bacan_`
  - `selected input _\*xláðaną_ > _hladan_`
- Audit result:
  - no `→` remains in regenerated Markdown
  - no `\rightarrow` remains in regenerated TeX
- Remaining greater-than notation in the book belongs to ordinary source/model
  prose and quoted or carried-through sound-change sequences, not to the
  generated summary arrow.

## Trace-box width changes

- The old trace layout used fixed panel widths (`0.485 / 0.485`) and a fixed
  internal form column width, which left too little horizontal space for long Old
  English change labels.
- The new layout computes a simple panel-complexity measure from:
  - number of non-`[no change]` rows
  - maximum change-name length
  - total change-name length
- If the Earlier Germanic side is light and the Old English side is heavy, the
  box now widens the Old English panel to about `0.57–0.59\linewidth` and
  narrows the Earlier Germanic side accordingly; the reverse applies when the
  left side is heavier.
- Each panel also gets a form-column width chosen from the same complexity data,
  so long change labels keep more room while form alignment remains stable.
- Form alignment was preserved by keeping the same two-column `tabularx` layout
  inside each panel, with italic forms still in the right-hand aligned form
  column and no reintroduced form header.

## References heading

- The bibliography heading was added by appending raw assembly content:
  - `\clearpage`
  - `## References`
- In the generated TeX this renders as:
  - `\clearpage`
  - `\subsection*{References}`
  - immediately before the `CSLReferences` environment
- Citation links still work after the change (`1043` link annotations detected in
  the PDF).

## Specific PDF checks

- adder / nǣdre:
  - checked
  - `OE Unstressed Long Vowel Shortening *nǣdræ` now extracts as one continuous
    label+form sequence on page 2
- bake / bacan:
  - checked
  - `OE Heavy Syllable Nasal Apocope *bakan` now extracts as one continuous
    label+form sequence on page 2
- additional checked entries:
  - begin / beġinnan — page 3
    - `OE Heavy Syllable Nasal Apocope *bigínnan`
    - `OE Secondary Nasalization *bigínnąn`
    - `OE Weak Tail Reduction *bĕʤínnan`
  - lade / hladan — page 58
    - `OE Heavy Syllable Nasal Apocope *xladan`
    - `OE Secondary Nasalization *xladąn`
    - `OE Weak Tail Reduction *xladan`
  - bone / bān — page 5
    - `OE Heavy Syllable Nasal Apocope *bān`
- references section:
  - checked
  - begins on page 126 with visible heading `References`

## Remaining issues

- No remaining generated summary-arrow issues were found.
- No bibliography heading/page-break regression remains.
- The sampled long Old English labels no longer break awkwardly in the inspected
  cases, but a full visual pass is still worthwhile for any residual edge-case
  wrapping elsewhere in the 147-entry corpus.
- The Docker wrapper still does not preserve a LaTeX log artifact, so overfull-box
  diagnostics are not yet collected automatically.

## Recommendation

**A. Alpha 03 fixes are successful; proceed to broader visual/style review.**

## Scope confirmation

- no model-entry prose or metadata was edited
- no TSV, FST, `report_manifest.tsv`, compact trace, packet, dev-note, research
  memo, bibliography, OCR/reference, or citation-locator report files were edited
- changes were limited to assembly scripts, regenerated outputs, and this report
