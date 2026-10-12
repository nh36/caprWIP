# Germanic project — current state (living entry point)

Keep this file tiny. Per-SC facts (status, verdicts, stages, memos) live only
in the canonical registry; do not duplicate them here.

## Current phase

Sequential per-SC adjudication, with separately instructed scoped research
and implementation decisions. The next SC is derived from the registry
and the explicit programme policy, never stated here:
`python3 Germanic/tools/adjudicate.py --next`

`registry/adjudication_programme.json` owns the administrative programme
start. Scoped verdicts cannot skip earlier pending work, and technical
support stages are excluded. Earlier pending cases and support stages
remain accessible through explicit SC commands; routing is not historical
stage, chronology or executable order.

Method: `Germanic/docs/RESEARCH_ADJUDICATION_PROTOCOL.md` +
`Germanic/docs/sound_changes/audits/ADJUDICATION_TEMPLATE.md` are mandatory
for any sound-change history/chronology/staging/scope/FST-semantics work.

## Canonical sources

- `Germanic/docs/sound_changes/registry/sc_registry.tsv` — all SC metadata.
- `Germanic/docs/sound_changes/registry/chronology_edges.tsv` — all
  chronology relations and witnesses.
- `Germanic/docs/sound_changes/registry/sc_inventory_notes.tsv` — human
  inventory judgements only (`sc_inventory_annotations.tsv` is generated from
  it plus `germanic.txt` and the coverage census).
- Settled verdicts (generated view):
  `Germanic/docs/sound_changes/registry/settled_verdicts.md`.
- Navigation and the SOURCE/GENERATED/ARCHIVE map: `Germanic/docs/README.md`.

## Frozen baselines (must not change silently)

Recorded in
`Germanic/docs/sound_changes/cascade_baseline/cascade_baseline_summary.json`
and pinned by `Germanic/tests/test_cascade_baseline.py`:

- active original-380 identity fingerprint (`legacy_subset_sha256`):
  `6e4ee75a2cb225cd9da445bce3b4251a0ad11d93e7381eb87028357519f1c3f6`
- selected-387 corpus fingerprint (`outputs_sha256`):
  `9d5adb68d97b0a280c3fa719e544236348cd3e771b01013cfe01f95f3579b6a5`
- lexical-input projection (`lexical_outputs_sha256`):
  `5c76b77eff81abfaf2cc54158a2e1dbf46eb7de2b8836f4832984142e93ef04d`

The immutable legacy380 archive still hashes to
`fae656520e9ebf446854643907a1ba48a511877fc25b1fae39649d5b97e9a6cf`.
The SC056 adjudication explicitly migrates gift's input by stable row ID.
The SC033 adjudication selects knee's regular dative: *knéwai → cneowe,
preserving citation *knéwą. Its exact input/target/output transition is
declared in `approved_cell_migration.json` and
`approved_input_migrations.tsv`; `*_pre_sc033.*` preserves the previous
baseline. All other 386 finals and the seven existing mismatches remain
protected. Apply only through
`python3 Germanic/tools/adjudicate.py SC033 --adopt-cell-baseline`.

The subsequent approved hue input correction preserves every final but
changes both PROTO and PROTOFORM to *xíwją. Its separate receipt is
`approved_hue_input_migration.json`, selected with
`SC033 --adopt-cell-baseline --approval approved_hue_input_migration.json`.
The distinct `*_pre_sc033_hue.*` archive preserves the post-knee baseline;
the knee receipt and all earlier archives are untouched. Hue lies outside
original380, whose active and immutable fingerprints remain unchanged.

The later SC034 straw correction preserves attested target `strēaw` and
input `*stráwą`; the regular cascade now yields reconstructed `strēa`.
This explicitly adds straw to the seven older mismatches: 379 matches /
eight mismatches, all387 accepted and unambiguous. The exact output and
match-flag receipt is `approved_sc034_output_migration.json`; separate
`*_pre_sc034.*` archives preserve the post-hue baseline. Every older
approval/archive and the other386 finals remain protected. Adoption uses
`SC034 --adopt-cell-baseline --approval approved_sc034_output_migration.json`;
routine refresh never changes it.

The SC031/SC098 context adoption separately changes only you's assembled
evaluator input; its lexical reconstruction and every final are unchanged.
The previous selected387 snapshot is preserved as `*_pre_sc031_sc098.*`.
Context selection lives in `Germanic/data/entry_context_metadata.tsv`;
an absent annotation explicitly selects strong-final citation context.
Routine refresh never refreezes the baseline. The approved transition uses
`python3 Germanic/tools/adjudicate.py SC098 --adopt-context-baseline`.

A fingerprint may change only as the explicit, row-level-diagnosed
consequence of an adjudication verdict (protocol step 13), never as a
routine refresh.

## Standard commands

- Next SC to adjudicate: `python3 Germanic/tools/adjudicate.py --next`
- Prepare an adjudication packet: `python3 Germanic/tools/adjudicate.py SCNNN --prepare`
- Executable evidence (container rebuild + live firing census + witness
  pre/post): `python3 Germanic/tools/adjudicate.py SCNNN --evidence`
- Control-plane refresh after ANY source edit (rule move, registry edit,
  prose edit): `python3 Germanic/tools/adjudicate.py --refresh`
- Finalize after SOURCE edits (control-plane refresh, then SC checks):
  `python3 Germanic/tools/adjudicate.py SCNNN --finalize`
- Full test suite: `cd Germanic/tests && python3 -m pytest -q`
- Debug-only: `python3 Germanic/tools/artifact_graph.py [--check|--refresh]`
  (the same graph `--refresh` drives)

## Instruction precedence

1. The current explicit user instruction.
2. `Germanic/docs/RESEARCH_ADJUDICATION_PROTOCOL.md` (adjudication work).
3. `.github/copilot-instructions.md` (repo-wide conventions).
4. `docs/AGENTS.md` — a short routing rule pointing to the adjudication
   interface. An explicit user request to complete, commit and push an
   adjudication is itself the authorization for those operations.
5. Anything under `Germanic/docs/archive/` or `docs/archive/` is
   historical record, never instruction.
