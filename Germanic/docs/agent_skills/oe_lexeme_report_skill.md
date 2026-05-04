# OE lexeme report skill

## Purpose

Use this skill when drafting a lexeme-level OE research report that will slot
under `### Lexeme report` in the generated derivation report.

## When to use this skill

Draft or revise `### Lexeme report` content only when at least one of these is
true:

1. the Old English TSV row has a non-empty `NOTE`;
2. `DERIVATION_CLASS` is not `regular`;
3. the row already has a manually supplied pilot/full lexeme report.

If a row is `regular`, has an empty `NOTE`, and has no manual pilot/full
report, do **not** generate a `### Lexeme report` for it.

## Model requirement

For substantive lexeme-report drafting or revision, delegated agents must use
**GPT-5.4** (`gpt-5.4`), matching the supervising session model. Do not use a
cheaper or faster fallback model for this stage; final lexeme-report prose is a
high-judgment task.

## Required structure

When a lexeme report is required, use these headings:

- `### Lexeme report`
- `#### Reconstruction and early-stage alternatives`
- `#### Chronological source dossier`
- `#### Old English philology`
- `#### Project problem and solution`
- `#### Paradigm probe` (only when relevant)

## Core rules

1. Treat TSV `NOTE` and `HISTORY` as **source material**, not final prose.
2. Distinguish **evidence** from **inference** explicitly.
3. Preserve distinctions between `PROTO`, `PROTOFORM`, and the attested or
   reconstructed OE target.
4. Do not claim attestation, dialect, manuscript status, or regularity without
   source support.
5. Use bibliography keys from `docs/refs.bib` in pandoc style, e.g.
   `[@Kroonen2013]`.
6. For a required row that does not yet have a full report, preserve the source
   note with a short placeholder rather than dropping it.
7. Do not add a gratuitous report to an ordinary `regular` row with empty
   `NOTE` unless the row is intentionally being covered by a manual pilot/full
   report.

## Source search order

1. `Germanic/data/germanic-aligned-final.tsv`
2. `Germanic/data/oe_known_problems.tsv` if relevant
3. `Germanic/docs/DEV_NOTES.md`
4. `Germanic/docs/analysis/` and `Germanic/docs/dossiers/`
5. `docs/references/`
6. `Germanic/data/old_english_wiktionary.tsv` and
   `Germanic/data/old_english_swadesh.tsv` as supplementary material

## Good output

Good output is:

- concise but source-dense;
- explicit about uncertainty;
- clear about what the project chose and why;
- suitable for later Markdown-to-LaTeX conversion.

## Bad output

Avoid:

- copying TSV notes verbatim as the whole section;
- inventing quotations;
- inventing bibliography keys;
- calling a form attested because it “looks standard”;
- flattening early analogy, late analogy, and unresolved cases into one pattern.
