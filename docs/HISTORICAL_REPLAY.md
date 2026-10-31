# Historical replay: inventory, incremental regression, and explicit reproduction

This document records the audit of every mechanism in the repository that
retrieves historical Git commits or compiles historical Foma models, the
resulting validation architecture (current-state, incremental, historical),
and the explicit procedure for reproducing immutable historical receipts.

The governing principle: ordinary CAPR testing validates the current
scientific model and examines what changed relative to its immediate
predecessor. Reconstructing historical grammars is a deliberate
reproducibility operation, not a recurring cost of ordinary development.

## 1. Inventory of historical mechanisms (audited 2026-10-30)

### 1.1 Historical Foma compilation (moved to the explicit replay lane)

These tests reconstructed a complete commit-pinned historical cascade in a
disposable container (`tests/historical_sc035.py:historical_runtime`) on
every strict Level C run. Each compiles the full historical grammar
(~6–11 minutes each). All verify **immutable receipts by live
re-execution**; the receipts themselves are separately checked without
Foma by the remaining ordinary tests in the same files.

| Test | Historical commit | What it recompiles | Scientific assertion |
|---|---|---|---|
| `test_sc035_prosody.py::test_fresh_commit_pinned_comparison_reproduces_the_entire_receipt` | receipt `accepted_base_commit` | full cascade + SC035 prosody experiment (3 models) | recorded prosody receipt is reproducible by live execution |
| `test_sc035_model_comparison.py::test_fresh_foma_comparison_reproduces_every_recorded_intermediate` | receipt `accepted_base_commit` | full cascade + model-comparison experiment | every recorded intermediate stage is reproducible |
| `test_sc035_prefix_reduction.py::PrefixReductionTests::test_fresh_container_assay_reproduces_census_controls_and_counterfactuals` | receipt `accepted_base_commit` | full cascade + prefix-reduction experiment incl. counterfactual variants | recorded census/controls/counterfactuals are reproducible |
| `test_rainbow_2148_adoption.py::test_fresh_container_capture_and_private_controls_match_committed_receipts` | adoption commit | full cascade + 109-stage capture + private controls | before/after/controls captures are reproducible |
| `test_chronology_consistency.py::test_original_displacement_is_contingent_on_the_retired_early_glide` | superseded-experiment commit | historical grammar + 4 historical ordering variants | the archived displacement result was contingent on the retired early glide |

Each answers the audit questions as follows: they execute Foma against the
historical source (not merely a record), reconstruct the complete
historical cascade, compile experimental variants (prefix-reduction,
chronology), do not share compilation with any other test (five separate
container builds per Level C run), and their scientific assertions are
**reproducibility** assertions — the corresponding receipt-integrity
assertions (hashes, provenance, internal consistency) are preserved by
other tests in the same modules and still run ordinarily.

`test_chronology_consistency.py::test_current_lowering_displacement_and_written_surface_controls`
previously shared the historical fixture; its assertions concern the
**current** grammar's ordering contingencies, so its current-variant
compilation remains in the ordinary runtime lane, now separated from the
historical half.

### 1.2 Historical Git retrieval without Foma (retained in ordinary runs)

`git show <commit>:<path>` text/hash checks that verify provenance,
source identity, preservation and adoption diffs. No compilation; cheap;
unchanged:

- `test_sc015_adoption.py`, `test_sc015_r_adverb_research.py` (fixture
  fetches four files; Foma is explicitly prohibited via mock),
  `test_sc017_sc019_adoption.py`, `test_sc017_nasal_vowel.py`,
  `test_sc034_adjudication.py`, `test_sc035_generality.py` (text diff
  only), `test_sc035_prosody.py`/`test_sc035_prefix_reduction.py`/
  `test_sc035_model_comparison.py` (non-runtime record checks),
  `test_sc036_adjudication.py`, `test_lexical_witness_input_gate.py`
  (base-diff guard), `test_palatal_class_split.py`,
  `test_rust_input_adoption.py`, `test_wether_input_adoption.py`,
  `test_world_2302_adjudication.py`, `test_sc112_lexical_publication.py`,
  `test_lexical_editorial_publication.py`,
  `test_anglo_frisian_experiments.py` (released-state hash pins),
  `test_chronology_consistency.py` (registry text checks),
  `tools/check_rename_gate.py`, `tools/check_reader_facing_semantics.py`
  (fallback only).

### 1.3 Current-model runtime tests (unchanged)

Runtime-marked tests that compile or execute only the **current** grammar
(`run_in_runner`, canonical bins, isolated current-variant compiles) are
current-state validation and stay in the ordinary serial runtime lane:
SC065/SC066-068/SC087/SC112/world-2302 production checks,
`test_sc035_prosody.py::test_fresh_adopted_cascade_and_phonological_components`,
the Anglo-Frisian private assays, `test_portable_provenance.py`,
`test_infrastructure_authorities.py`, and the chronology current-variant
test above.

`test_evidence_interface.py` (exclusive lane) rebuilds the authoritative
canonical bins from the current source. It is **not** historical
compilation and is explicitly preserved.

### 1.4 Fully mocked lifecycle tests (unchanged)

`test_historical_runtime_lifecycle.py` exercises the replay container
lifecycle with all subprocess calls mocked; it compiles nothing.

## 2. The three validation forms

**A. Current-state correctness** — the ordinary strict suite (all three
lanes of `docs/CI_VALIDATION.md`), `adjudicate.py --status`, the artifact
graph, protected fingerprints and frozen baselines. Protected scientific
fingerprints remain independent assertions precisely because consecutive
incremental comparisons cannot detect cumulative drift from an older
accepted result.

**B. Incremental regression** — `Germanic/tools/incremental_regression.py`
compares consecutive versions of the **committed canonical full-trace
report** (`Germanic/docs/debug_snapshots/oe_full_trace_report.txt`), which
Git already stores for every model state. The comparison therefore
retrieves both sides with `git show` and performs **zero Foma compilations
and zero lookups**; it never re-evaluates a historical model to
reconstruct a report Git already holds. It runs automatically during
Level C (lane 1,
`test_incremental_regression.py::test_level_c_runs_the_consecutive_version_comparison_automatically`);
a standalone command remains for debugging:

```sh
python3 Germanic/tools/incremental_regression.py             # automatic states
python3 Germanic/tools/incremental_regression.py --worktree  # explicit worktree
python3 Germanic/tools/incremental_regression.py --json out.json --fail-on-change
```

State resolution: staged executable inputs differing from `HEAD` compare
**staged vs HEAD** (unstaged work is explicitly excluded; `--worktree`
compares the working tree and may refresh a stale worktree report through
the artifact-graph `runtime_bins`/`full_trace` nodes — the canonical
generator, never a parallel evaluation path); a clean index compares
**HEAD vs HEAD^1** (first parent; merge commits use the first parent and
say so; an unavailable parent is an explicit error, never a silent pass).
Each report is validated against the source files of its *own* version
(Git blobs, via the shared provenance core in
`Germanic/tools/oe_trace_parse.py`); a missing, stale or non-canonical
report on either side is an explicit failure. Reports carry a versioned
provenance contract: **v2** (current) also records hashes of the
evaluation helpers `oe_pipeline.py`, `sound_change_order_sensitivity.py`
and `capr_runtime.py`, so changing evaluation code without regenerating
the report makes the canonical report stale; v1 reports from earlier
commits remain readable under their own contract, with the
evaluation-helper limitation stated explicitly. Both sides additionally
undergo **structural validation** against their own declared firing
summary (complete, ordered, non-duplicated stage sequences per entry;
parseable outputs; referentially coherent fidelity records); identical
but malformed reports are rejected rather than fast-pathed.

The comparison covers every named stage of every entry (identity:
concept + PROTO + EXPECTED): intermediate changes with identical final
outputs, first divergence/reconvergence (with previous/current forms
recorded at every divergent stage in the JSON report), final outputs, stage
order/membership, corpus membership and contextual inputs, and
firing-population changes. Rejection states and raw context-marked forms
come from the report's `RAW STAGE FIDELITY` section; older reports
without it are compared display-level with that limitation stated, never
silently reconstructed. Changed dependencies are classified by executable
consequence (recompilation / renewed evaluation / presentation-only /
none), covering the grammar, corpus, context metadata and the evaluation
tools (`oe_pipeline.py`, `generate_oe_sandbox.py`,
`oe_full_trace_report.py`, batch-lookup helpers), so a change to
evaluation code is never classified as irrelevant merely because
`germanic.txt` is unchanged. Differences are **reported for
adjudication**, not automatically rejected. Diagnostics are written to
`.ci-results/incremental_regression.txt` and `.json` (stable untracked
names, replaced each run).

The compile cache (`.capr_compile_cache/`, gitignored) now serves
historical replay only; the former evaluated-results cache was removed
because Git itself is the content-addressed store for committed reports.

**C. Historical reproducibility** — explicit replay of the receipts in
§1.1:

```sh
cd Germanic/tests
python3 -m pytest -q -m historical_replay --historical-replay
```

Without `--historical-replay`, these tests are reported as explicitly
skipped ("historical replay: explicit lane"), never silently dropped;
the collected test count is unchanged. Replay uses the same
content-addressed cache so an immutable grammar is compiled at most once
per cache lifetime; a cached build is verified by its recorded digest
before reuse, and the replay report distinguishes a cache-backed
execution from a fully fresh compile.

Run the replay lane when a historical claim is reconsidered, when an
experimental script or its execution infrastructure changes, when a
recorded result is suspected, or during a deliberate reproducibility
audit. Verifying a receipt's integrity (ordinary suite) and reproducing
it by live Foma execution (this lane) are different assurance levels and
are reported separately.

## 3. Coverage change, stated plainly

Removing live historical replay from routine execution deliberately
changes coverage: an ordinary green run no longer demonstrates that the
five historical receipts can be re-derived by fresh execution; it
demonstrates their recorded integrity. The replay lane restores the
stronger claim on demand. No historical evidence, experimental script,
receipt or adjudication record was deleted.
