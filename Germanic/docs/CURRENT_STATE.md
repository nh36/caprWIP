# Germanic project — current state (living entry point)

**This is the "start here" document for the Germanic pipeline.** It is a
living document: update it whenever a sound-change adjudication or other
project-phase change alters what is authoritative.

`Germanic/docs/CANONICAL_STATE.md` is a **frozen historical checkpoint**
(freeze date 2026-05-09). It correctly records the state at that
moment, including "research phase complete / publication mode". That
claim is no longer current: an active sound-change adjudication
programme has since reopened individual rules. Do not treat
CANONICAL_STATE.md, or any frozen audit conclusion, as current state.

## Current phase

Sequential per-SC adjudication of the sound-change cascade
(chronology, historical staging/scope, executable-rule scientific
correctness), performed on branch `sc001-sc020-chronology-audit`,
one SC per instructed task.

**Method:** any work touching Germanic sound-change history,
chronology, staging, scope, FST semantics, or interaction evidence MUST
follow `Germanic/docs/RESEARCH_ADJUDICATION_PROTOCOL.md` and record its
reasoning in a memo based on
`Germanic/docs/sound_changes/audits/ADJUDICATION_TEMPLATE.md`.

## Authoritative registries

- `Germanic/docs/sound_changes/sound_change_inventory.tsv` — rule inventory.
- `Germanic/docs/sound_changes/sound_change_historical_staging_map.tsv` —
  historical stage/scope, display names, cascade positions, action status.
- `Germanic/docs/sound_changes/cascade_baseline/` — frozen baseline
  summary, historical audit table, rename migration manifest.
- `Germanic/docs/sound_changes/order_tests/` — interaction matrix,
  chronology graph (`first_break_edges.tsv`, nodes), candidate lists.
- `Germanic/docs/sound_changes/audits/scNNN-adjudication.md` — per-SC
  adjudication memos (verdicts of record).
- Live corpus TSV plus compact derivation report, lexeme packets,
  manifest, schema, and coverage audit (as listed in CANONICAL_STATE.md;
  those artifact roles are unchanged).

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

## Settled adjudication verdicts (do not reopen without new evidence)

- **SC020** — split (see `sc020-adjudication.md`).
- **SC021** `NWGmcUnstressedORaising` — RETIRED. Successors: SC071
  (*ō > *o shortening), SC099/SC100 (medial-u/final-a split); SC040
  moved later. The identifier SC021 must not be reused or reactivated.
- **SC022** `PNWGmcMnDissimilation` — RETAIN executable rule /
  REFORMULATE metadata: historically late Proto-Germanic / Common
  Germanic, not specifically Northwest Germanic. The `PNWGmc` prefix in
  the executable identifier is retained for stability and carries no
  stage claim.
- **SC023** `PNWGmcNStemNLoss` — RETAIN executable rule byte-for-byte /
  REFORMULATE metadata: (late) Proto-Germanic word-final n-loss
  (Ringe 2017: 101–103); the `{*ō}{*n}` environment is a deliberately
  narrow executable proxy. `do` is a counterfeeding negative chronology
  witness for SC023 < SC047, not a live application.

Next in sequence: SC024 (not yet begun).

## Instruction precedence

1. The current explicit user instruction for the task at hand.
2. `Germanic/docs/RESEARCH_ADJUDICATION_PROTOCOL.md` (for adjudication work).
3. `.github/copilot-instructions.md` (repo-wide conventions).
4. `docs/AGENTS.md` — its container sanity checks and evidence
   discipline remain good practice, but its Tier-3 "always ask before
   editing/committing" gates do **not** govern explicitly instructed
   adjudication tasks, which include commit-and-push in scope.
5. Frozen checkpoints (CANONICAL_STATE.md and audit snapshots) are
   historical records, not instructions.
