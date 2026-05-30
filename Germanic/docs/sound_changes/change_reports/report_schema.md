# Sound-change report schema

## Purpose

This schema defines the **assembled sound-change layer** for the book. Source
dossiers are not final prose. Literature dossiers, book dossiers, chronology
cards, audit packets, and related working files remain source material unless
they are explicitly promoted into the manifest-backed assembly layer.

## Entry types

- A **pilot/full production report** is book-facing Markdown listed in
  `Germanic/docs/sound_changes/change_reports/report_manifest.tsv` with status
  `pilot` or `full`.
- A **scaffold placeholder** is short assembly-ready Markdown listed in the
  same manifest with status `scaffold`. Its job is to make the full sound-change
  half visible and buildable without pretending that the prose is complete.
- Working dossiers, packets, memos, architecture reports, chronology cards, and
  audit views remain source material for drafting, not production prose.

Production entries live under `change_reports/pilot/` or later
`change_reports/full/`. Scaffold placeholders live under
`change_reports/scaffold/`.

Documented manifest status values are `full`, `pilot`, `scaffold`,
`needs_literature`, `needs_human_review`, and `grouped_elsewhere`. The current
assembly includes only `full`, `pilot`, and `scaffold`.

## Finished production reports

Each finished pilot/full report should be concise, book-facing Markdown
suitable for later Pandoc / LaTeX integration. The standard section order is:

```md
### Sound-change report

#### Historical formulation

#### Source tradition

#### CAPR implementation

#### Place in the cascade

#### Order evidence

#### Interpretation

#### Remaining cautions
```

Keep the style aligned with the lexical reports: concise prose, selective
quotation, and no dossier-sized audit machinery.

## Scaffold placeholders

Scaffold placeholders are deliberately shorter. A typical scaffold entry uses:

```md
### Sound-change report

#### Historical formulation

#### Current evidence

#### Place in the cascade

#### Order evidence

#### Status
```

The placeholder should say plainly that it is scaffold material rather than
finished prose.

## Citation convention

- Use **pandoc-style citations**: `[@Campbell1959]`,
  `[@Campbell1959, §115]`, `[@RingeTaylor2014, p. 267]`.
- Bibliography keys must come from `docs/refs.bib`.
- If a needed source lacks a key, record it in
  `Germanic/docs/sound_changes/change_reports/missing_bibliography_keys.md`.
- Do **not** invent bibliography keys in report prose.

## Evidence vs inference

Each report must distinguish:

- **literature-backed claims**;
- **CAPR implementation claims**;
- **order-testing evidence**;
- and the book-level interpretation that the project draws from them.

Practical rule:

- state source-backed claims directly;
- signal project inference when moving from handbook description to CAPR
  formalization or from CAPR formalization to order-sensitive interpretation;
- do not present chronology-card boundaries as if they were direct handbook
  quotations.

## Build relation

These entries are intended to enter the same Pandoc/LaTeX/PDF pipeline already
documented for the lexical half. Use:

```bash
bash Germanic/docs/assembly/build_sound_change_volume.sh
```

Source Markdown may use inline code spans for linguistic forms during authoring,
but the assembly step converts those spans to reader-facing linguistic
formatting while preserving genuine code, file paths, and commands, following
the lexical-volume convention.
