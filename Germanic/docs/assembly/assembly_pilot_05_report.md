# Assembly pilot 05 report

## Summary

- Trace-table headers changed: **yes**
- Visible `Form` headers removed from trace tables: **yes**
- Stage labels converted into headers: **yes**
- `Proto-West Germanic` changed to `West Germanic`: **yes**
- `pilot_assembled.md` regenerated: **yes**
- `pilot_assembled.tex` regenerated: **yes**
- `pilot_assembled.pdf` regenerated: **yes**
- Original model entries edited: **no**

## Trace-table rendering change

The pilot-04 trace layout used a four-column structure with visible headers for both change and form columns. That kept change/result pairing explicit, but it made the trace read like a flat spreadsheet rather than as two structured derivational sides.

The new pilot-05 layout replaces that with a two-side trace table:

1. `Earlier Germanic changes`
2. `Old English changes`

Within each side, stage labels are now rendered as bold headers, and the individual sound changes are listed underneath them with the resulting form kept on the same line where space permits. This means the trace now reads as a structured stage list rather than as four equally weighted columns.

The stage handling is now:

- `Proto-West Germanic` -> `West Germanic`
- `Northwest Germanic` -> `Northwest Germanic`
- `Old English` -> `Old English`

Centering was not added, because the row-based Markdown grid-table approach was the robust path that preserved stage/header separation through Pandoc and XeLaTeX. The stage headers are bold, but not centered.

## PDF inspection

The regenerated PDF matches the requested structural changes:

1. The trace headers now read `Earlier Germanic changes` and `Old English changes`.
2. No visible trace-table `Form` headers remain.
3. `Proto-West Germanic` no longer appears; it is rendered as `West Germanic`.
4. `West Germanic`, `Northwest Germanic`, and `Old English` now behave as bold stage headers rather than ordinary change rows.
5. Change/result-form pairs remain clearly paired under the correct stage, even when a long line wraps.

Entry-specific inspection:

1. **bake**: the PDF shows `West Germanic` and `Northwest Germanic` as stage headers on the left, and `Old English` as a stage header on the right with the expected sequence beneath it.
2. **thistle / þistles**: the PDF now shows:
   - `West Germanic`
   - `[no change]`
   - `Northwest Germanic`
   - `[no change]`
   - `Old English`
   - `Anglo Frisian Brightening: *θístilæs`
   - `OE L Adjacent Syncope: *θístlæs`
   - `OE Unstressed AE Merger: *θístles`
3. **weapon / wǣpn**: the PDF shows `West Germanic`, `Northwest Germanic`, and `Old English` as stage headers, with `NWGmc Long E Lowering: *wǣpną` and `OE Heavy Syllable Nasal Apocope: *wǣpn` clearly attached to their stages.
4. **will / willa**: the PDF shows `West Germanic` with `PWGmc J Gemination: *wélljô`, then `Northwest Germanic` with `[no change]`, and `Old English` with the expected i-umlaut / shortening / j-loss sequence.
5. **youth / ġeoguþ**: the PDF now shows the intended staged structure:
   - `West Germanic`
   - `[no change]`
   - `Northwest Germanic`
   - `OE Ws Palatal Glide: *jéugunθ`
   - `NWGmc Nasal Spirant Lengthening: *jéugūnθ`
   - `NWGmc Nasal Spirant Loss: *jéugūθ`
   - `Old English`
   - `OE Diphthong Leveling: *jéogūθ`
   - `OE Unstressed Long Vowel Shortening: *jéoguθ`

Additional checks:

- Forms remain in normal text font and italic, not monospaced code.
- Citations and bibliography still render.
- Unicode still renders correctly.

## Remaining issues

- Stage headers are bold, but not centered.
- Some trace cells are still dense, especially where several changes fall under one stage.
- Long change/result lines can still wrap across multiple visual lines in the PDF.
- No semicolon-separated change strings remain in the inspected trace tables.
- No obvious unwanted bolding appeared outside the intended stage headers.
- The trace structure is now correct, but there is still room for one general style/tightness pass.

## Recommendation

**Decision: A. Trace-table structure is now acceptable; proceed to one more general pilot style pass.**

The requested structural fix is now in place: the trace reads as two staged derivational sides, stage labels behave as headers, the `Form` headers are gone, and the inspected examples for bake, thistle, weapon, will, and youth all render in the intended direction. The remaining issues are visual polish, not parser structure.

## Scope confirmation

- No original model entries were changed.
- No TSV source data, FST files, manifest files, packets, dev-note slices, research memos, bibliography files, OCR/reference files, or citation-locator reports were edited.
- Changes were limited to `Germanic/docs/assembly/build_pilot.sh`, regenerated pilot outputs (`pilot_assembled.md`, `pilot_assembled.tex`, `pilot_assembled.pdf`), and this report.
