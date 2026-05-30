# Sound-change production reports

This directory is the **assembled book layer** for sound changes, parallel to
`Germanic/docs/lexeme_reports/`. It now contains both finished production prose
and scaffold placeholders so that the whole sound-change half can be assembled
even though only a small part of it is fully written.

Source dossiers, architecture reports, audit notes, chronology cards, and
similar files remain drafting material. The entries listed in
`report_manifest.tsv` are the book-facing Markdown units intended for assembly.

## Layout

- `report_schema.md` — schema for finished reports and scaffold placeholders
- `report_manifest.tsv` — manifest-backed list of assembled entries
- `sound_change_half_scaffold.tsv` — full 70-change unit scaffold for the sound-change half
- `sound_change_half_coverage_report.md` — generated summary of scaffold coverage
- `pilot/` — pilot production entries
- `full/` — future promoted production entries, if and when added
- `scaffold/` — concise buildable placeholders for units that still need
  literature work, human review, or full prose drafting

## Finished reports versus scaffold placeholders

Pilot/full reports are the real production layer. Scaffold placeholders exist
to make the whole sound-change half visible and buildable, not to pretend the
prose is complete. They should read cleanly in the assembled volume while
stating plainly that they are scaffold entries.

## Build relation

Use:

```bash
bash Germanic/docs/assembly/build_sound_change_volume.sh
```

The current build assembles the full half to
`Germanic/docs/assembly/sound_change_volume_alpha_01.md` and, where local
`pandoc` support is available, renders
`Germanic/docs/assembly/sound_change_volume_alpha_01.tex` and an uncommitted
PDF. Source reports may use inline code spans for linguistic forms during
authoring, but the assembly step converts those spans to reader-facing
linguistic formatting while preserving genuine code, paths, and commands,
following the lexical-volume convention.
