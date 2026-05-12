# Assembly pilot 01 report

## Summary

- Model entries included: **8**
- Output files created: `Germanic/docs/assembly/README.md`, `pilot_manifest.tsv`, `pilot_metadata.yaml`, `build_pilot.sh`, `pilot_assembled.md`, `assembly_pilot_01_report.md`
- Pandoc Markdown-to-LaTeX succeeded: **no** (`pandoc` not installed in the local environment)
- PDF generation attempted: **no**
- PDF generation succeeded: **no**
- Original model entries edited: **no**

## Pilot selection

The pilot used the suggested representative set:

1. `1934-bake-bacan.model.md` — regular row with localized conditional-source citations
2. `1962-bow-bēag.model.md` — late-analogy paradigm-cell solution
3. `1981-craft-cræft.model.md` — early-analogy stem-class comparison with a short table
4. `2030-fowl-fugol.model.md` — unexplained unmodelled exception with mixed citation types
5. `2250-thistle-þistles.model.md` — late-analogy entry retaining broad `KlugeSeebold2011`
6. `2278-weapon-wǣpn.model.md` — regular row with special form discussion and multiple locators
7. `2293-will-willa.model.md` — regular noun row carrying the corrected `KlugeSeebold2011` key
8. `2308-youth-ġeoguþ.model.md` — early-analogy staging argument with broad older grammar citations

No replacement entries were needed.

## Assembly transformations

- The assembled document uses one document title:
  - `# Germanic Lexeme Report Assembly Pilot 01`
- Each included model entry is rewritten only in the assembled copy so that:
  - source `#` entry titles become `##`
  - internal section headings become `###`
- Tables were preserved as Pandoc-compatible pipe tables.
- Citations were preserved exactly as they appear in the source `.model.md` files.
- Content intentionally excluded from the assembled body:
  - implementation reports
  - reviewer checklists
  - source ledgers
  - packets
  - dev-note slices
  - research memos

No philological prose was revised during assembly.

## Citation handling

- The assembled Markdown passes citations through in Pandoc syntax exactly as found in the selected model entries.
- The pilot build script is wired to use `docs/refs.bib`.
- No new citations or locators were added in this pass.
- `KlugeSeebold2011` remains broad where it appears in the pilot entries; no page locators were introduced for it.

## Build result

Command run from the repository root:

```bash
bash Germanic/docs/assembly/build_pilot.sh
```

Observed result:

```text
Generated /Users/nathanhill/Code/capr-v3-working/Germanic/docs/assembly/pilot_assembled.md
pandoc not found; unable to build pilot_assembled.tex or pilot_assembled.pdf.
```

The script therefore succeeded in:

1. reading `pilot_manifest.tsv`
2. assembling `pilot_assembled.md`
3. preserving entry order and heading normalization

It did **not** produce:

- `pilot_assembled.tex`
- `pilot_assembled.pdf`

because `pandoc` was not available locally.

The script is already wired to attempt this LaTeX build when `pandoc` becomes available:

```bash
pandoc Germanic/docs/assembly/pilot_assembled.md \
  --standalone \
  --from=markdown+citations \
  --to=latex \
  --metadata-file=Germanic/docs/assembly/pilot_metadata.yaml \
  --bibliography=docs/refs.bib \
  --citeproc \
  -o Germanic/docs/assembly/pilot_assembled.tex
```

If `xelatex` or `lualatex` is later available, the same script will then attempt PDF generation as a second step.

## Blockers before full assembly

1. `pandoc` is not installed in the local environment, so the pilot cannot yet emit `.tex`.
2. No Unicode-capable LaTeX engine (`xelatex` or `lualatex`) is installed locally, so PDF generation cannot yet be exercised safely.
3. Because the LaTeX stage did not run, table rendering, bibliography rendering, and Unicode/font behavior still need one real toolchain-backed verification pass before scaling up.

## Recommendation

**Decision: B. Pilot assembly mostly works; fix specific technical issues before full assembly.**

The assembly-side Markdown transformation is working and the selected pilot set assembles cleanly into one document. The remaining work is technical rather than editorial: install `pandoc` and a Unicode-capable LaTeX engine, rerun the pilot, and inspect the resulting `.tex`/`.pdf` before attempting a full-corpus assembly.

## Scope confirmation

- No TSV source data, FST files, `report_manifest.tsv`, packets, dev-note slices, research memos, bibliography files, local OCR/reference files, or citation-locator reports were edited.
- No original model-entry prose files were rewritten.
- New work was limited to `Germanic/docs/assembly/` and the generated `pilot_assembled.md` inside that directory.
