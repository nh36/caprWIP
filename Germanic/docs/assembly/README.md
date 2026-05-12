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

If local `pandoc` / LaTeX tools are unavailable but Docker is available, use:

```bash
bash Germanic/docs/assembly/build_pilot_docker.sh
```

That wrapper regenerates `pilot_assembled.md` locally, then renders `.tex` and
`.pdf` inside a `pandoc/latex` container.

## Expected outputs

- `pilot_assembled.md` — assembled Markdown with normalized heading levels
- `pilot_assembled.tex` — LaTeX output, if `pandoc` is available
- `pilot_assembled.pdf` — PDF output, if `pandoc` and a Unicode-capable LaTeX engine (`xelatex` or `lualatex`) are available

## Current local result

In the current local host environment used for pilot 01:

- assembled Markdown generation was exercised successfully;
- `pandoc` was **not installed**, so `.tex` generation did not complete;
- no PDF engine stage was reached.

Pilot 02 adds and validates a Docker-backed render path because Docker is
available even where the host lacks local `pandoc`.

In the validated Docker-backed pilot-02 path:

- `pilot_assembled.md` regenerates on the host;
- `pilot_assembled.tex` renders successfully in `pandoc/latex`;
- `pilot_assembled.pdf` renders successfully with `xelatex`;
- `Noto Serif` / `Noto Sans Mono` are used in the container to preserve the Old
  English and reconstruction characters that the default Latin Modern fonts
  dropped.

See `assembly_pilot_01_report.md` and `assembly_pilot_02_report.md` for the
exact build results and blockers.

## Known blockers before full assembly

1. Install local `pandoc` to enable host-native Markdown-to-LaTeX conversion, or use the Docker wrapper.
2. Keep a Unicode-capable font path available for the PDF engine (`Noto Serif` / `Noto Sans Mono` are used in the Docker-backed pilot).
3. After any toolchain change, rerun the pilot and inspect table and bibliography rendering before scaling to the full corpus.
