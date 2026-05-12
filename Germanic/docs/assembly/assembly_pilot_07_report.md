# Assembly pilot 07 report

## Summary

- Pre-trace metadata table removed: **yes**
- Generated derivation summaries added: **yes**
- Repeated inner `Old English` stage header removed: **yes**
- `pilot_assembled.md` regenerated: **yes**
- `pilot_assembled.tex` regenerated: **yes**
- `pilot_assembled.pdf` regenerated: **yes**
- Original model entries edited: **no**

## Summary-generation rules

The entry-opening summary is now generated mechanically from model metadata plus the matched compact trace data. The assembly script uses these rules:

1. **Citation reconstruction = selected input; trace outcome = target**
   - Template: `Derivation: *X* → *Y* (class).`
   - Example: `bake / bacan`

2. **Citation reconstruction differs from selected input; trace outcome = target**
   - Template: `Derivation: citation reconstruction *X*; selected input *Y* → *Z* (class).`
   - Example: `bow / bēag`, `craft / cræft`, `thistle / þistles`, `youth / ġeoguþ`

3. **Trace outcome differs from selected target**
   - Template: `Derivation: *X* yields regular *Z*; the selected target is *T* (class).`
   - Example: `fowl / fugol`
   - If citation reconstruction and selected input were also different, the generator would include both facts in the same sentence.

4. **Missing or uncertain trace match**
   - Fallback template: `Derivation: selected input *X* and target *Y*; no compact trace was confidently matched in this assembly pass.`
   - This fallback remains implemented, but it was **not used** in the current pilot because all eight pilot entries matched confidently.

Class labels are normalized mechanically:

- `regular` -> `regular`
- `early_analogy` -> `early analogy`
- `late_analogy` -> `late analogy`
- `unexplained_unmodelled` -> `unexplained exception`
- unknown labels -> underscores replaced with spaces

## PDF inspection

The PDF entry openings now read acceptably for the inspected pilot entries:

1. **bake / bacan**
   - Summary reads as compact regular derivation prose.
   - No metadata table remains.
   - Boxed trace still renders.

2. **bow / bēag**
   - Summary clearly distinguishes citation reconstruction `*béuganą` from selected input `*báug`.
   - No raw machine label is shown; `late analogy` appears instead.

3. **craft / cræft**
   - Summary clearly distinguishes citation reconstruction `*kráftiz` from selected input `*kráftaz`.
   - The summary reads acceptably as generated prose rather than as a database row.

4. **fowl / fugol**
   - Summary correctly distinguishes regular transducer outcome `fogol` from selected target `fugol`.
   - `unexplained exception` appears instead of `unexplained_unmodelled`.

5. **thistle / þistles**
   - Summary clearly distinguishes citation reconstruction `*θéstilaz` from selected input `*θístilas`.
   - The boxed trace still renders correctly below it.

6. **will / willa**
   - Summary reads cleanly as `*wéljô → willa (regular).`
   - The trace box still renders, and the right-hand panel no longer repeats an inner `Old English` heading.

7. **youth / ġeoguþ**
   - Summary clearly distinguishes citation reconstruction `*júgunθiz` from selected input `*júgunθ`.
   - The boxed trace still renders and remains readable.

Across the inspected pages:

- the `Item / Value` table is gone
- each entry has a generated derivation summary
- raw machine labels such as `late_analogy` and `unexplained_unmodelled` are no longer visible in the summary
- the boxed derivation trace still renders
- the repeated inner `Old English` stage header is removed from the right-hand trace panel
- citations and bibliography still render
- Unicode still renders correctly

## Remaining issues

- The summaries are intentionally compact and therefore somewhat mechanical in tone.
- The boxed trace remains the visually dominant element, which is correct for this pilot, but the overall page opening could still use one more style pass.
- The generated summaries use a math arrow for robust PDF rendering; this works well in the PDF but is slightly more technical in the raw assembled Markdown.
- No redundant metadata table remains before the trace.
- No obvious trace-box regression, typography regression, or citation/bibliography regression was observed.

## Recommendation

**Decision: A. Entry opening format is acceptable; proceed to one general pilot style pass.**

The opening now reads much more like a report and much less like a database export. The generated summaries carry the key derivational distinctions without forcing the reader through a metadata table, and the boxed trace remains intact underneath them.

## Scope confirmation

- No original model entries were changed.
- No TSV source data, FST files, manifest files, packets, dev-note slices, research memos, bibliography files, OCR/reference files, or citation-locator reports were edited.
- Changes were limited to assembly scripts and regenerated pilot outputs, plus this report.
