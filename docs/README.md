# CAPR Shared Documentation

This is the shared navigation entry point for the Germanic, Burmish and Celtic
pipelines and their Flask/Svelte application. For active Old English research,
start at [Germanic task routing](../Germanic/docs/README.md); this index links
the existing authorities rather than defining another control plane.

## Setup & Usage

- [SETUP.md](SETUP.md) — Full Docker/installation guide
- [USAGE.md](USAGE.md) — UI walkthrough
- [AGENTS.md](AGENTS.md) — Guidelines for AI assistants

## Shared Operations

- [runbook.md](runbook.md) — Day-to-day Docker/Caddy operational checklist
- [regression_checks.md](regression_checks.md) — API smoke test design
- [REFISHING_BEHAVIOR.md](REFISHING_BEHAVIOR.md) — Backend refishing behavior
- [CI_VALIDATION.md](CI_VALIDATION.md) — Portable capabilities and full strict lanes
- [HISTORICAL_REPLAY.md](HISTORICAL_REPLAY.md) — Current validation, incremental
  regression and explicitly requested historical reproduction

## Canonical Owners

| Material or operation | Existing authority |
| --- | --- |
| Executable OE cascade and order | [germanic.txt](../Germanic/fsts/germanic.txt), interpreted by [oe_pipeline.py](../Germanic/tools/oe_pipeline.py) |
| Canonical lexical rows and selected inputs | [germanic-aligned-final.tsv](../Germanic/data/germanic-aligned-final.tsv); [entry_stages.py](../Germanic/tools/entry_stages.py) resolves input stages |
| Scientific identities, chronology and SOURCE ownership | [CONTROL_PLANE.md](../Germanic/docs/sound_changes/registry/CONTROL_PLANE.md) and its registries |
| Preparation, evidence and propagation | [adjudicate.py](../Germanic/tools/adjudicate.py) |
| Generated-output dependencies and freshness | [artifact_graph.py](../Germanic/tools/artifact_graph.py), including its `--inventory`; never a hand-picked generator list |
| Sound-change and lexical arguments | [Germanic SOURCE map](../Germanic/docs/README.md#what-you-may-edit-source), including reader chapters, model entries and source ledgers |
| Generated books, manifests and indexes | [Assembly README](../Germanic/docs/assembly/README.md); edit their SOURCE, not the publications |
| Current-state regression tests | [Germanic/tests](../Germanic/tests/) and the [serial/exclusive validation policy](CI_VALIDATION.md#three-level-development-validation-workflow) |
| Historical tests, certificates and failed-run receipts | [Historical replay](HISTORICAL_REPLAY.md), [frozen baselines](../Germanic/docs/sound_changes/cascade_baseline/) and the existing per-experiment archives; keep exact historical identities |
| Bibliography and private original holdings | [refs.bib](refs.bib), [holding navigation](references/README_resources.md) and the existing intake manifests |
| Linked-worktree retention and private recovery records | [Preservation/consolidation overview](POST_AUDIT_INVENTORY.md); detailed inventories and restricted backups remain local |
| Deferred regression-control work | [Reviewed provisional pilot](REGRESSION_CONTROLS_PILOT_REVIEW.md), not an adopted mandatory register |

## Reference Materials

- [references/](references/) — Scholarly sources (PDFs + text extracts)
  - Grammars, etymological dictionaries, journal articles
  - See [references/README_resources.md](references/README_resources.md) for index

## Component-Specific Documentation

For pipeline-specific documentation, see:

- **[../Germanic/docs/](../Germanic/docs/)** — Proto-Germanic → OE research
  - [README.md](../Germanic/docs/README.md) — SOURCE/GENERATED/ARCHIVE and task routing
  - [CURRENT_STATE.md](../Germanic/docs/CURRENT_STATE.md) — Live phase and baseline pointers
  - [archive/](../Germanic/docs/archive/) — Superseded logs and workflows, not instructions

- **[../Burmish/README.md](../Burmish/README.md)** — Proto-Burmish pipeline
- **[../Celtic/README.md](../Celtic/README.md)** — Celtic pipeline

## Application Documentation

- [../backend/](../backend/) — Flask backend
- [../frontend/](../frontend/) — Svelte frontend
