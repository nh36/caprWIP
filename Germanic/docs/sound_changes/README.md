# Sound-change volume scaffold

This directory is the architecture scaffold for a rule-centered sound-change volume parallel to the lexical derivation volume.

## Layout

- `sound_change_inventory.tsv` — first-pass ordered inventory of the current OE stack, keyed to the live rule source and compact trace report.
- `sound_change_aliases.tsv` — trace labels, internal stage names, and normalized variants for later dossier matching.
- `sound_change_literature_matrix.tsv` — row-level literature dossier workspace for quotations, paraphrases, chronology, and disagreement tracking.
- `sound_change_order_sensitivity.tsv` — runner-facing summary table for earliest/latest safe positions and lexical breakage.
- `change_entries/` — one file per sound-change entry in the eventual volume.
- `literature_dossiers/` — longer per-rule dossier notes and source collation.
- `order_tests/runs/` — raw future order-perturbation run outputs.
- `order_tests/summaries/` — future TSV/markdown summaries of those runs.

## Current scope

Scaffold 01 does **not** assemble the sound-change volume yet. It only:

1. locates the rule source and trace machinery;
2. extracts a first ordered inventory;
3. creates dossier and order-testing templates;
4. adds two pilot change-entry stubs.

See `sound_change_architecture_scaffold_01_report.md` for the source-discovery findings and next recommended task.
