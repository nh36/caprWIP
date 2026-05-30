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

Documented sound-change assembly command:

```bash
bash Germanic/docs/assembly/build_sound_change_volume.sh
```

These files are also designed to remain parallel to the lexical assembly
pipeline:

```bash
bash Germanic/docs/assembly/build_full_lexical_volume.sh
bash Germanic/docs/assembly/build_full_lexical_volume_docker.sh
```

The sound-change build currently assembles manifest-backed production reports to
`Germanic/docs/assembly/sound_change_volume_alpha_01.md` and, where local
`pandoc` support is available, renders
`Germanic/docs/assembly/sound_change_volume_alpha_01.tex` and an uncommitted PDF.
Source reports may use inline code spans for linguistic forms during authoring,
but the assembly step converts those spans to reader-facing linguistic
formatting while preserving genuine code, paths, and commands, following the
lexical-volume convention.
