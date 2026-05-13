# Full lexical assembly alpha 01 report

## Summary

- entries assembled: **147**
- counts by section:
  - regular: **70**
  - attested variant: **4**
  - early analogy: **35**
  - late analogy: **28**
  - reconstructed Old English comparator: **3**
  - known but unmodelled remodelling: **2**
  - unexplained or deliberately unmodelled exception: **5**
- outputs generated:
  - `lexical_volume_alpha_01.md`
  - `lexical_volume_alpha_01.tex`
  - `lexical_volume_alpha_01.pdf`
- PDF produced: **yes**
- original model entries edited: **no**

## Assembly inputs

- manifest source: `Germanic/docs/assembly/manifest_all_by_class.tsv`
- section-introduction source: `Germanic/docs/assembly/section_introductions_draft.md`
- trace source: `Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.compact.md`
- bibliography: `docs/refs.bib`
- metadata file: `Germanic/docs/assembly/full_volume_metadata.yaml`

## Seven-section structure

1. Regular derivations — **70**
2. Attested variants and selected comparison forms — **4**
3. Early analogy and pre-Old-English input selection — **35**
4. Late analogy and paradigm-cell selection — **28**
5. Reconstructed Old English comparators — **3**
6. Known but unmodelled remodellings — **2**
7. Unexplained or deliberately unmodelled exceptions — **5**

## Build result

- commands run:
  - `python3 Germanic/docs/assembly/build_full_lexical_volume.py`
  - `./Germanic/docs/assembly/build_full_lexical_volume_docker.sh`
- Docker image used: `pandoc/latex:latest` on `linux/amd64`
- Pandoc version: `pandoc 3.9.0.2`
- PDF engine: `xelatex`
- fonts: `Noto Serif`, `Noto Sans Mono`
- output file sizes:
  - `lexical_volume_alpha_01.md`: `421519` bytes
  - `lexical_volume_alpha_01.tex`: `570952` bytes
  - `lexical_volume_alpha_01.pdf`: `513285` bytes

## Output inspection

- Markdown:
  - all **147** lexical entries are present as `###` entry headings
  - the seven sections appear in the agreed order
  - no support-package files, ledgers, reviewer checklists, packets, or implementation reports were pulled into the assembled body
- TeX:
  - citeproc scaffolding is present
  - bibliography scaffolding is present
  - **147** boxed trace blocks were emitted
  - no obvious malformed raw-TeX trace blocks were found in spot inspection
- PDF:
  - the file opens and was parsed successfully
  - page count: **124**
  - link annotations detected: **1043**
  - part headings for the seven-section sequence are present in the rendered text
  - Unicode Old English and reconstructed forms survived the render in spot checks
  - bibliography content is present on the closing pages

## Problems found

- No blocking technical failures were found in alpha 01.
- Part openings are readable, but they are not yet forced onto fresh pages; that is a style/layout issue for a later pass, not a structural blocker.
- The Docker/Pandoc render emitted transient `Ticker: poll failed: Interrupted system call` messages while still completing successfully; this should be monitored on later runs, but it did not prevent `.tex` or `.pdf` output here.
- The Docker wrapper does not currently preserve a LaTeX log file, so warning-level diagnostics such as overfull boxes are not yet collected automatically.

## Recommendation

**A. Full lexical alpha works; proceed to visual/style review.**

## Scope confirmation

- no model-entry prose or metadata was edited
- no TSV, FST, `report_manifest.tsv`, compact trace, packet, dev-note, research memo, bibliography, OCR/reference, or citation-locator report files were edited
