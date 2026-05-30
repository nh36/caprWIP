# Sound-change report schema

## Purpose

This schema defines the **production sound-change report** for the book-facing
sound-change layer.

Source dossiers are not final prose. Literature dossiers, book dossiers,
chronology cards, audit packets, and related working files remain source
material unless they are explicitly promoted into the manifest.

## Production reports vs source material

- A **production sound-change report** is a Markdown file listed in
  `Germanic/docs/sound_changes/change_reports/report_manifest.tsv` with status
  `pilot` or `full`.
- Working dossiers, packets, memos, architecture reports, and audit views are
  source material for drafting, not production prose.
- Production entries live under `change_reports/pilot/` or later
  `change_reports/full/`.

## Entry structure

Each production entry should be concise, book-facing Markdown suitable for later
Pandoc / LaTeX integration. The standard section order is:

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
documented for the lexical half. The exact sound-change assembly command has not
yet been identified in this pass; the directory mirrors the lexeme-report
production structure so it can be integrated into the existing build.
