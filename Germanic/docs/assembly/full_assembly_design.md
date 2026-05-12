# Full assembly design

## Purpose

This note describes how a future **full lexical assembly** should work. It does
not create or run that assembly. The goal here is to define the build shape so
that a later full-volume alpha can be generated reproducibly from the current
corpus and class manifests.

## Inputs

The future full assembly should draw from the following sources:

1. `manifest_all_by_class.tsv`
2. class manifests:
   - `manifest_regular.tsv`
   - `manifest_early_analogy.tsv`
   - `manifest_late_analogy.tsv`
   - `manifest_unexplained.tsv`
3. `build_class_manifests.py`
4. current `.model.md` files under
   `Germanic/docs/lexeme_reports/model_entries/`
5. compact trace source:
   `Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.compact.md`
6. assembly metadata:
   `Germanic/docs/assembly/pilot_metadata.yaml`
7. bibliography:
   `docs/refs.bib`
8. volume scaffolding files:
   - `book_architecture.md`
   - `section_introductions_draft.md`

Support-package files such as source ledgers, reviewer checklists, packets,
implementation reports, research memos, and dev-note slices should be excluded
from the assembled body.

## Preflight step

Before future full assembly, run:

```bash
python3 Germanic/docs/assembly/build_class_manifests.py
```

The future full assembly script should read the generated manifests rather than
rescanning the corpus ad hoc. That makes the class order, row order, and review
bucket explicit.

Recommended preflight checks:

1. fail or warn on unknown derivation classes
2. fail or warn on incomplete top metadata
3. fail or warn on non-confident trace matching
4. record whether any entries are intentionally excluded from the alpha because
   they remain in the review bucket

## Class order

The future full lexical volume should be ordered in this sequence:

1. regular
2. early analogy
3. late analogy
4. unexplained / deliberately unmodelled

Entries with unknown class labels should not be silently folded into one of
those sections. They should be either:

- remapped explicitly before assembly, or
- excluded from the first alpha and listed in an editorial review note

## Heading hierarchy

Recommended hierarchy for the future assembled Markdown:

1. `#` volume title
2. `##` front-matter chapters
3. `##` catalogue parts
4. `###` lexical entries
5. `####` internal entry sections

This means the future full assembly should demote the model-entry headings more
deeply than the pilot did.

## Per-entry structure

Each assembled entry should keep the pilot structure:

1. entry heading
2. generated derivation summary
3. boxed derivation trace
4. outcome or target split where needed
5. model-entry prose sections

The current generated derivation-summary rules remain a good basis:

- same citation reconstruction / selected input / target path
- citation reconstruction distinct from selected input
- transducer output distinct from selected target
- fallback if trace matching fails

The current boxed trace design should remain the default PDF-oriented layout.

## Section-introduction handling

The future full assembly should insert section-introduction prose once per class
section, before the first lexical entry in that part.

Recommended source:

- `section_introductions_draft.md` for the initial alpha

Later revisions can replace those placeholders with polished prose without
changing the per-entry assembly logic.

## Front matter handling

The first full lexical assembly alpha does not need completed book prose, but it
should reserve space for:

1. Introduction
2. Data and sources
3. Transducer and derivation method
4. Derivation classes

Those chapters can begin as short scaffold text and expand later.

## Bibliography handling

The full lexical assembly should continue to use:

- `docs/refs.bib`
- Pandoc `--citeproc`
- `link-citations: true`

The pilot-08 build confirmed that this path yields live internal citation links
in the PDF.

## PDF build path

The future full assembly should preserve the current Docker-backed PDF path as
the documented reliable route on this machine:

```bash
bash Germanic/docs/assembly/build_pilot_docker.sh
```

For the eventual full-volume build, a separate script such as
`build_full_lexical_volume.sh` can reuse the same Pandoc/XeLaTeX/Docker pattern,
but no such full build script is created in this pass.

## Suggested future script layout

Possible future files:

- `build_full_lexical_volume.py` or `build_full_lexical_volume.sh`
- `full_volume_metadata.yaml`
- `lexical_volume_assembled.md`
- `lexical_volume_assembled.tex`
- `lexical_volume_assembled.pdf`

Suggested workflow:

1. regenerate manifests
2. build assembled Markdown from front matter + section intros + ordered entries
3. render LaTeX
4. render PDF
5. inspect section breaks, bibliography, trace boxes, and Unicode

## Separation from the later sound-change volume / report

The future lexical assembly should remain a lexical volume only. It should not
absorb:

- full rule chronology
- rule-ordering argumentation at system scale
- broader sound-change diagnostics that belong in a later sound-change
  volume/report

That separation is part of the design, not a temporary omission.
