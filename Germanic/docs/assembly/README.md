# Germanic assembly pilot

This directory contains **assembly pilot 01**, a small publication-format test that assembles a representative subset of current Germanic `.model.md` entries into one Markdown document and, when the toolchain is available, converts that document to LaTeX and PDF.

## Pilot contents

The pilot includes these eight model entries, in the stable order recorded in `pilot_manifest.tsv`:

1. `1934-bake-bacan.model.md`
2. `1962-bow-bēag.model.md`
3. `1981-craft-cræft.model.md`
4. `2030-fowl-fugol.model.md`
5. `2250-thistle-þistles.model.md`
6. `2278-weapon-wǣpn.model.md`
7. `2293-will-willa.model.md`
8. `2308-youth-ġeoguþ.model.md`

## How to run the pilot

From the repository root:

```bash
bash Germanic/docs/assembly/build_pilot.sh
```

The script is path-stable and can also be run from other working directories.

## Expected outputs

- `pilot_assembled.md` — assembled Markdown with normalized heading levels
- `pilot_assembled.tex` — LaTeX output, if `pandoc` is available
- `pilot_assembled.pdf` — PDF output, if `pandoc` and a Unicode-capable LaTeX engine (`xelatex` or `lualatex`) are available

## Current local result

In the current local environment used for this pilot:

- assembled Markdown generation was exercised successfully;
- `pandoc` was **not installed**, so `.tex` generation did not complete;
- no PDF engine stage was reached.

See `assembly_pilot_01_report.md` for the exact build result and blockers.

## Known blockers before full assembly

1. Install `pandoc` to enable Markdown-to-LaTeX conversion.
2. Install `xelatex` or `lualatex` to enable Unicode-safe PDF generation.
3. After toolchain installation, rerun the pilot and inspect table and bibliography rendering before scaling to the full corpus.
