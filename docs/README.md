# CAPR Documentation Index

This index points to the working documents we rely on most often. Use it as the
jumping-off point before editing code or linguistics files.

**WARNING — `{*ǭ}` is a temporary Germanic vowel marker.** The transducer uses
`{*ǭ}` as a stop-gap during West Germanic *au* → *ō*; make sure any follow-up
work either preserves the guard or replaces it with a more principled
chronology before the placeholder leaks into downstream tooling.

## Getting the stack running
- [`README.md`](../README.md) – quick start plus project overview.
- [`docs/runbook.md`](runbook.md) – step-by-step checklist (Docker, Caddy,
  regression harness, tear-down).
- [`SETUP.md`](../SETUP.md) – full install notes (Docker vs. manual).
- [`USAGE.md`](../USAGE.md) – interface walkthrough and basic FST debugging tips.

## Day-to-day reference
- [`DEV_NOTES.md`](../DEV_NOTES.md) – latest hand-off; add a dated section for
  each session.
- [`docs/regression_checks.md`](regression_checks.md) – design of the API smoke
  test harness (`server/tools/api_regression.py`).
- [`docs/REFISHING_BEHAVIOR.md`](REFISHING_BEHAVIOR.md) – backend behaviour when
  toggling “Use new FST?”.

## Germanic workbench
- [`docs/germanic_transducer_report.md`](germanic_transducer_report.md) –
  coverage stats, recent fixes, next steps.
- [`docs/germanic_notes/README.md`](germanic_notes/README.md) – links to the
  supporting Word docs from the October 2025 push.
- [`docs/germanic_refresh_template.md`](germanic_refresh_template.md) – repeatable
  checklist for exporting/comparing Germanic snapshots.

## Backend & pipeline
- [`server/README.md`](../server/README.md) – Flask routes and dependencies.
- [`server/pipeline/README.md`](../server/pipeline/README.md) – lexicon/pipeline
  scripts.
- [`cognate-app/README.md`](../cognate-app/README.md) – Svelte interface notes.

When adding a new reference doc, drop it into `docs/` (or a subfolder) and
update this index so future hand-offs stay discoverable.
