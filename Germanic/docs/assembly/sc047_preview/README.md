# SC047 combined-book research preview

From the repo root, run `python3 Germanic/docs/assembly/build_sc047_preview.py`.
It reads the same assembled inputs as the production book, inserts
the comparative chapter at the end of the sound-change part and the
technical appendix after the lexical catalogue, and writes only to
`.capr-work/sc047-parallel/book/preview.md`. It neither refreshes
artifacts nor changes the sound-change reader manifest. The
[proposed reader corrections](reader-corrections.md) remain review
copy, not modifications to the included canonical entries.

Run `bash Germanic/docs/assembly/sc047_preview/render.sh` for LaTeX and
PDF using the canonical filters, headers and metadata and a second,
preview-only bibliography. The PDF requires Pandoc, XeLaTeX, the
configured fonts and `makeindex`. Set `SC047_PREVIEW_MONOFONT` to an
installed substitute if Noto Sans Mono is unavailable.
