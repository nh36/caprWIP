# Germanic project — current state (living entry point)

Keep this file tiny. Per-SC facts (status, verdicts, stages, memos) live only
in the canonical registry; do not duplicate them here.

## Current phase

SC112 scientific implementation and lexical publication are complete; the
[publication receipt](sound_changes/audits/sc112-lexical-publication.md)
records the evidence and validation. Current lexical counts live in the
[generated population summary](lexeme_reports/pgmc_integration/population_summary.md).
The next priority is the paved-road architecture for cheaper coding agents. It
has no separate worktree: it extends the control plane, adjudication interface,
CI validation and cleanup commits already on `update`. Entry points and the
editorial-projection principle are in [README.md](README.md) ("Routine
operations"); lexical presentation order is now editorial
(`assembly/lexical_editorial_order.tsv`).

For subsequently authorized per-SC adjudication, the next SC is derived from
the registry and the explicit programme policy, never stated here:
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
  `43de8a47b7aaf17f860c9e3009617002ddb36e4d32a90ede1a99525858a417ce`
- selected-389 corpus fingerprint (`outputs_sha256`):
  `53769ef582dd6d119bacc18f808612980a1f02dfed2f94a6e30645bb9de00a9e`
- lexical-input projection (`lexical_outputs_sha256`):
  `c44d73698e2fa2717366e951a75bbb02d19aa677faf51fc86dfa25187556b6da`

The SC112 expansion adds only rows 2333 and 2334 (*there* and *where*):
389 selected rows, 381 matches and the same eight mismatches. Every prior
387 input, target, context and output is preserved in `*_pre_sc112_expansion.*`;
the original-393 comparative survey remains a distinct historical scope
from the current 395-row audit inventory.

The immutable legacy380 archive still hashes to
`fae656520e9ebf446854643907a1ba48a511877fc25b1fae39649d5b97e9a6cf`.
The authorized wether lexical selection uses masculine `*wéθruz`, preserving
all 387 finals and the eight established mismatches. Its exact named receipt
is `approved_wether_input_migration.json`; the separate
`*_pre_sc015_wether_input.*` archive preserves the preceding active baseline.
That lexical-only decision changed no sound law, verdict or chronology.
The subsequent authorized SC015 adoption is a separate transition:
`approved_sc015_targets_migration.json` preserves `*_pre_sc015.*`
and selects independently attested `leornian`, `leorna`, `leornaþ`
for2095/2313/2314, with unchanged inherited inputs. All387 selections
remain deterministic,379 match and the same eight mismatches remain.
The canonical memo records the working hypothesis and unresolved
comparative counterevidence; no stage/context or rule-order change is made.
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

The supplementary SC017 rust selection changes only row2162's PROTO and
PROTOFORM from *rústō to masculine *rústaz, retaining rust, predicted rost
and `unexplained_unmodelled`. `approved_rust_input_migration.json` authorizes
the exact input-only baseline transition; `*_pre_sc017_rust_input.*`
preserves the post-SC034 state. The original-380 archive remains immutable
and the migration TSV makes its old rust identity recoverable. All387
finals and the same eight mismatches are unchanged. SC017's earlier RETAIN
verdict, registry reference, definition and chronology remain intact.

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
