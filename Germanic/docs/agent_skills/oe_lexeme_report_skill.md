# OE lexeme report skill

## Purpose

Use this skill when drafting a lexeme-level OE research report that will slot
under `### Lexeme report` in the generated derivation report.

## Required structure

Always use these headings:

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

