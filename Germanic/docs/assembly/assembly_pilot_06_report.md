# Assembly pilot 06 report

## Summary

- Trace display converted from Markdown table to boxed two-panel display: **yes**
- Form alignment improved: **yes**
- `pilot_assembled.md` regenerated: **yes**
- `pilot_assembled.tex` regenerated: **yes**
- `pilot_assembled.pdf` regenerated: **yes**
- Original model entries edited: **no**

## Layout implementation

The trace display now uses a PDF-oriented raw LaTeX block rather than an ordinary Markdown table. The implementation uses:

- `\fbox`
- paired `minipage`s for the two side-by-side panels
- inner `tabularx` environments for change/form alignment
- `array` support for the aligned change/form columns

No `tcolorbox` or `mdframed` package was needed. The layout uses the simpler and more robust `\fbox + minipage + tabularx` path so it stays compatible with the Docker-backed `pandoc/latex` image.

Required support changes:

1. `Germanic/docs/assembly/pilot_metadata.yaml` now includes:
   - `\usepackage{array}`
   - `\usepackage{tabularx}`
2. `build_pilot.sh` and `build_pilot_docker.sh` now invoke Pandoc with `markdown+raw_tex+citations` so the raw LaTeX trace blocks survive into the LaTeX/PDF path.

The trace display is intentionally optimized for the LaTeX/PDF assembly path. No duplicate plain-text fallback was added in the assembled Markdown, because that would have duplicated the trace content in the PDF output.

## Trace rendering

Stage labels are parsed from the compact trace source and rendered as bold headers inside each panel.

Rendering rules:

- `Proto-West Germanic` is displayed as `West Germanic`
- `Northwest Germanic` remains `Northwest Germanic`
- `Old English` remains `Old English`

Each panel is structured as:

1. bold stage header
2. either `[no change]` or a compact two-column `tabularx` block

Within each stage's change block:

- the change name occupies the left internal column
- the resulting form occupies the right internal column
- the form column has a consistent width and is right-aligned

This gives the forms a consistent vertical start position within each panel, even when the change label wraps.

No-change stages are shown plainly under the stage header as:

- `West Germanic`
- `[no change]`

without inventing a separate visible form header.

## PDF inspection

The regenerated PDF renders the boxed two-panel traces acceptably for the inspected entries:

1. **bake / bacan**
   - boxed trace present
   - left panel shows `West Germanic` and `Northwest Germanic`
   - right panel shows `Old English` with aligned forms for the five OE steps
2. **bow / bēag**
   - boxed trace present
   - right panel aligns `OE Au Fronting` and `OE Diphthong Leveling` cleanly with their forms
3. **thistle / þistles**
   - boxed trace present
   - Old English panel renders acceptably with:
     - `Anglo Frisian Brightening` -> `*θístilæs`
     - `OE L Adjacent Syncope` -> `*θístlæs`
     - `OE Unstressed AE Merger` -> `*θístles`
4. **weapon / wǣpn**
   - boxed trace present
   - `NWGmc Long E Lowering` and `OE Heavy Syllable Nasal Apocope` are clearly separated into their correct panels with aligned form positions
5. **will / willa**
   - boxed trace present
   - `PWGmc J Gemination`, `OE I Umlaut`, `OE Unstressed Long Vowel Shortening`, and `OE J Loss After Heavy` render as paired change/form lines inside the box
6. **youth / ġeoguþ**
   - boxed trace present
   - Earlier Germanic panel renders acceptably with:
     - `OE Ws Palatal Glide` -> `*jéugunθ`
     - `NWGmc Nasal Spirant Lengthening` -> `*jéugūnθ`
     - `NWGmc Nasal Spirant Loss` -> `*jéugūθ`
   - Old English panel renders acceptably with:
     - `OE Diphthong Leveling` -> `*jéogūθ`
     - `OE Unstressed Long Vowel Shortening` -> `*jéoguθ`

Additional checks:

- No visible trace-level `Form` header appears
- Stage headers are bold and visually distinct
- Forms remain italic, not monospaced
- Citations and bibliography still render
- Unicode still renders correctly

## Remaining issues

- The outer box is simple and functional, but not yet typographically refined.
- Panels are still somewhat narrow when a change name is especially long.
- Some change labels still wrap, although the aligned form column now stays visually stable.
- The layout depends on raw LaTeX, so it is primarily a PDF-oriented solution rather than a generic Markdown-rendering solution.
- No obvious unwanted bolding or code-font regressions remain inside the trace boxes.
- No page-break failure was seen in the pilot pages inspected, but boxed raw-LaTeX displays are less flexible than plain Markdown if the corpus is scaled up later.

## Recommendation

**Decision: A. Boxed trace display is acceptable; proceed to one general pilot style pass.**

The boxed two-panel display solves the main trace-display problem: the trace now reads like a compact derivational display, stage headers are clear, and forms align in stable columns within each panel. What remains is visual refinement, not a structural rework.

## Scope confirmation

- No original model entries were changed.
- No TSV source data, FST files, manifest files, packets, dev-note slices, research memos, bibliography files, OCR/reference files, or citation-locator reports were edited.
- Changes were limited to:
  - `Germanic/docs/assembly/build_pilot.sh`
  - `Germanic/docs/assembly/build_pilot_docker.sh`
  - `Germanic/docs/assembly/pilot_metadata.yaml`
  - regenerated pilot outputs (`pilot_assembled.md`, `pilot_assembled.tex`, `pilot_assembled.pdf`)
  - this report
