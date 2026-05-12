# Assembly pilot 02 report

## Summary

- `pilot_assembled.md` regenerated: **yes**
- `pilot_assembled.tex` generated: **yes**
- `pilot_assembled.pdf` generated: **yes**
- Pandoc version used: **3.9.0.2**
- PDF engine used: **xelatex**
- Font used: **Noto Serif** with **Noto Sans Mono** for monospaced text (Docker-backed run)
- Original model entries edited: **no**

## Toolchain

- Build path used: **Docker-backed**
- Host availability:
  - local `pandoc`: **missing**
  - local `xelatex`: **missing**
  - local `lualatex`: **missing**
  - Docker CLI: **present**
  - Docker daemon: **available after starting Docker Desktop**
- Exact commands run:

```bash
open -ga Docker
bash Germanic/docs/assembly/build_pilot.sh
bash Germanic/docs/assembly/build_pilot_docker.sh
```

The Docker wrapper uses `pandoc/latex:latest` under `linux/amd64` and performs:

```bash
apk add --no-cache font-noto
pandoc Germanic/docs/assembly/pilot_assembled.md \
  --standalone \
  --from=markdown+citations \
  --to=latex \
  --metadata-file=Germanic/docs/assembly/pilot_metadata.yaml \
  --bibliography=docs/refs.bib \
  --citeproc \
  -o Germanic/docs/assembly/pilot_assembled.tex

pandoc Germanic/docs/assembly/pilot_assembled.md \
  --standalone \
  --from=markdown+citations \
  --metadata-file=Germanic/docs/assembly/pilot_metadata.yaml \
  --bibliography=docs/refs.bib \
  --citeproc \
  --pdf-engine=xelatex \
  -o Germanic/docs/assembly/pilot_assembled.pdf
```

- Dependencies still missing on the host:
  - `pandoc`
  - a local Unicode-capable LaTeX engine (`xelatex` or `lualatex`)

## LaTeX output inspection

- Citations resolved: **yes**
- Bibliography appeared: **yes**
- Tables compiled: **yes**
- Unicode characters survived: **yes, after metadata/font changes**
- Current citation mode: **`--citeproc` immediate rendering**, not deferred BibLaTeX commands

Inspection findings:

1. `pilot_assembled.tex` contains a `CSLReferences` bibliography block at the end of the document.
2. No unresolved `@Key` citation syntax remained in the generated LaTeX.
3. The earlier duplicate-title problem was fixed: the body no longer contains a first-section copy of the document title.
4. The earlier metadata-line collapse was fixed: row metadata (`PROTO`, `PROTOFORM`, `COUNTERPART`, `DERIVATION_CLASS`) is now rendered as a small table in the assembled Markdown and compiles cleanly to LaTeX.
5. The first Docker-backed PDF attempt exposed missing glyphs in default Latin Modern for characters such as `θ`, `ǣ`, and `ḗ`. This was fixed by using `Noto Serif` plus `Noto Sans Mono` in `pilot_metadata.yaml` and installing `font-noto` in the Docker wrapper.

Non-blocking note:

- The Docker-backed Pandoc runs emitted `Ticker: poll failed: Interrupted system call` messages, but both `.tex` and `.pdf` were still produced successfully and the outputs inspected cleanly.

## PDF output inspection

- PDF opens: **yes**
- Old English and reconstructed forms render correctly: **yes**
- Tables are acceptable: **yes for pilot purposes**
- Bibliography / citations render acceptably: **yes**

Inspection basis:

1. The PDF was generated successfully as `Germanic/docs/assembly/pilot_assembled.pdf`.
2. Text extraction from the PDF succeeds and preserves representative forms including:
   - `bēag`
   - `cræft`
   - `wǣpn`
   - `ġeoguþ`
   - `*θístilas`
   - `*wḗpną`
   - `Kluge-Seebold`
3. No tofu boxes or missing-character warnings remained after the Noto font fix.

Visible/layout cautions still worth carrying forward:

- This pilot is readable enough to scale technically, but final publication typography still needs later refinement.
- Some ordinary line breaking / hyphenation remains visible in extracted text, which is acceptable for a pilot but not yet a final style pass.

## Script or metadata changes

Changed files:

- `Germanic/docs/assembly/build_pilot.sh`
  - fixed the assembled-document generator so the document title is not duplicated in the body
  - rewrote the top row metadata lines into a compact Markdown table in the assembled copy
  - changed the missing-`pandoc` path to regenerate Markdown and exit cleanly with a clear message
- `Germanic/docs/assembly/build_pilot_docker.sh` **(new)**
  - adds a Docker-backed render path using `pandoc/latex`
  - installs `font-noto` in the container and renders both `.tex` and `.pdf`
- `Germanic/docs/assembly/pilot_metadata.yaml`
  - added `pdf-engine: xelatex`
  - added `mainfont: "Noto Serif"`
  - added `monofont: "Noto Sans Mono"`
- `Germanic/docs/assembly/README.md`
  - documented the Docker-backed render path and the validated pilot-02 result

Regenerated outputs:

- `Germanic/docs/assembly/pilot_assembled.md`
- `Germanic/docs/assembly/pilot_assembled.tex`
- `Germanic/docs/assembly/pilot_assembled.pdf`

## Recommendation

**Decision: B. Toolchain-backed pilot mostly works; fix specific technical issues first.**

Reasoning:

1. The assembly pipeline now works end-to-end through Markdown, LaTeX, and PDF.
2. Citations, bibliography generation, tables, and the key Old English / reconstructed characters survive the Docker-backed render path.
3. The pilot uncovered and fixed real assembly bugs (duplicate title, collapsed metadata block, missing Unicode glyph coverage).
4. Before full-corpus assembly, the project should decide whether Docker is the supported default render path or whether local `pandoc` + `xelatex` should be installed and documented as the primary toolchain.

## Scope confirmation

- No TSV source data, FST files, `report_manifest.tsv`, packets, dev-note slices, research memos, bibliography files, local OCR/reference files, citation-locator reports, or original model-entry prose files were edited.
- Changes were limited to in-scope assembly files and newly generated assembly outputs under `Germanic/docs/assembly/`.
