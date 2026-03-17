# CAPR Shared Documentation

This directory contains documentation that applies to the **shared infrastructure** 
used by both Germanic and Burmish pipelines.

## Shared Operations

- [runbook.md](runbook.md) — Day-to-day Docker/Caddy operational checklist
- [regression_checks.md](regression_checks.md) — API smoke test design
- [REFISHING_BEHAVIOR.md](REFISHING_BEHAVIOR.md) — Backend refishing behavior

## Reference Materials

- [references/](references/) — Scholarly sources (PDFs + text extracts)
  - Grammars, etymological dictionaries, journal articles
  - See [references/README_resources.md](references/README_resources.md) for index

## Project-Wide Setup

- [../SETUP.md](../SETUP.md) — Full installation guide
- [../USAGE.md](../USAGE.md) — UI walkthrough
- [../WORKFLOW.md](../WORKFLOW.md) — Development workflow

## Component-Specific Documentation

For pipeline-specific documentation, see:

- **[../Germanic/docs/](../Germanic/docs/)** — Proto-Germanic → OE research
  - `DEV_NOTES.md` — Research log with source citations
  - `debug_snapshots/` — Timestamped mismatch reports
  - `analysis/` — Investigation notes
  - `REFERENCES.md` — Germanic-specific source index

- **[../Burmish/README.md](../Burmish/README.md)** — Proto-Burmish pipeline

## Application Documentation

- [../app/README.md](../app/README.md) — Flask + Svelte web application
