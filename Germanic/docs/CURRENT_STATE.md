# Germanic project — current state (living entry point)

Keep this file tiny. Per-SC facts (status, verdicts, stages, memos) live only
in the canonical registry; do not duplicate them here.

## Current phase

Sequential per-SC adjudication of the sound-change cascade on branch
`sc001-sc020-chronology-audit`, one SC per instructed task.
**Next SC in sequence: SC024.**

Method: `Germanic/docs/RESEARCH_ADJUDICATION_PROTOCOL.md` +
`Germanic/docs/sound_changes/audits/ADJUDICATION_TEMPLATE.md` are mandatory
for any sound-change history/chronology/staging/scope/FST-semantics work.

## Canonical sources

- `Germanic/docs/sound_changes/registry/sc_registry.tsv` — all SC metadata.
- `Germanic/docs/sound_changes/registry/chronology_edges.tsv` — all
  chronology relations and witnesses.
- `Germanic/docs/sound_changes/registry/sc_inventory_annotations.tsv` —
  inventory-view annotations.
- Settled verdicts (generated view):
  `Germanic/docs/sound_changes/registry/settled_verdicts.md`.
- Navigation and the SOURCE/GENERATED/ARCHIVE map: `Germanic/docs/README.md`.

## Frozen baselines (must not change silently)

Recorded in
`Germanic/docs/sound_changes/cascade_baseline/cascade_baseline_summary.json`
and pinned by `Germanic/tests/test_cascade_baseline.py`:

- legacy-380 corpus fingerprint:
  `a72bdeb8451039206ab0b90110547f50171c209d5b9c08c71219ed45df5165fc`
- expanded-383 corpus fingerprint:
  `7bed2ba862d91f82a0b7553e1a98fc78d9137483d39d94af0050af5aa18bdd33`

A fingerprint may change only as the explicit, row-level-diagnosed
consequence of an adjudication verdict (protocol step 13), never as a
routine refresh.

## Standard commands

- Prepare an adjudication packet: `python3 Germanic/tools/adjudicate.py SCNNN --prepare`
- Regenerate views after registry edits: `python3 Germanic/tools/generate_registry_views.py`
- Verify views clean: `python3 Germanic/tools/generate_registry_views.py --check`
- Validate propagation: `python3 Germanic/tools/adjudicate.py SCNNN --check`
- Full test suite: `cd Germanic/tests && python3 -m pytest -q`

## Instruction precedence

1. The current explicit user instruction.
2. `Germanic/docs/RESEARCH_ADJUDICATION_PROTOCOL.md` (adjudication work).
3. `.github/copilot-instructions.md` (repo-wide conventions).
4. `docs/AGENTS.md` — container sanity checks remain good practice; its
   Tier-3 approval gates do not govern explicitly instructed adjudication
   tasks.
5. Anything under `Germanic/docs/archive/` is historical record, never
   instruction.
