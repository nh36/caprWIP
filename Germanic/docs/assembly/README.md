# Germanic assembly pilot and lexical-volume design

This directory now contains two connected layers of work:

1. the validated **pilot assembly** used to settle entry layout, trace display,
   and citation behavior; and
2. the **book-architecture and class-manifest design** for a future full lexical
   derivation volume.

The pilot is deliberately small. The book-design layer is where the full
corpus-ordering logic now lives.

## Pilot status

The pilot format is now stable enough to serve as the basis for a full lexical
assembly alpha:

- generated derivation summary under each headword
- boxed derivation trace
- model-entry prose below the trace
- live internal citation links in PDF output
- Unicode-safe Docker-backed PDF rendering

See `assembly_pilot_01_report.md` through `assembly_pilot_08_report.md` for the
incremental pilot passes.

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

See the pilot reports for the exact build results and the layout decisions that
landed during those passes.

## Book architecture and class manifests

The current design layer for full lexical assembly includes:

- `book_architecture.md` — proposed structure of the lexical derivation volume
- `book_architecture_01_report.md` — summary report for the architecture pass
- `full_assembly_design.md` — design note for a future full assembly script
- `section_introductions_draft.md` — placeholder section-opening prose
- `build_class_manifests.py` — helper that scans current `.model.md` entries and
  writes class-based manifests
- `manifest_regular.tsv`
- `manifest_early_analogy.tsv`
- `manifest_late_analogy.tsv`
- `manifest_unexplained.tsv`
- `manifest_all_by_class.tsv`
- `manifest_summary.md`

These files are design and scaffolding artifacts only. They do **not** generate
the full 147-entry lexical PDF in this phase.

## Next planned step

After review of the architecture and manifests, the next planned step is a
**full lexical assembly alpha by class**. That later pass should:

1. use the class manifests as the ordering source;
2. insert section-introduction scaffolding above each class part;
3. preserve the current per-entry summary + boxed-trace layout; and
4. continue to keep the later sound-change volume or report separate.

## Known blockers before full assembly

1. Decide how to handle the small review bucket of entries with non-canonical
   derivation-class labels before the first full lexical alpha.
2. Install local `pandoc` to enable host-native Markdown-to-LaTeX conversion, or
   use the Docker wrapper.
3. Keep a Unicode-capable font path available for the PDF engine (`Noto Serif` /
   `Noto Sans Mono` are used in the Docker-backed pilot).
4. After any toolchain change, rerun the pilot and inspect trace boxes,
   bibliography rendering, and citation links before scaling to the full corpus.
