# Sound-change production reports

This directory is the **production-report layer** for sound changes, parallel to
`Germanic/docs/lexeme_reports/`.

Source dossiers, architecture reports, audit notes, chronology cards, and similar
files remain drafting material. The production entries listed in
`report_manifest.tsv` are the book-facing Markdown units intended for later
assembly.

## Layout

- `report_schema.md` — concise schema for production sound-change entries
- `report_manifest.tsv` — manifest-backed list of pilot/full production entries
- `pilot/` — pilot production entries
- `full/` — future promoted production entries, if and when added

## Build relation

These files are intended to enter the same Pandoc/LaTeX/PDF pipeline already
documented for the lexical half.

Documented existing assembly commands are:

```bash
bash Germanic/docs/assembly/build_full_lexical_volume.sh
bash Germanic/docs/assembly/build_full_lexical_volume_docker.sh
```

The exact **sound-change** assembly/Pandoc build command has not yet been
identified in this pass; this directory mirrors the lexeme-report production
structure so that it can be integrated into the existing book build.
