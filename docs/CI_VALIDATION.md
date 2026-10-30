# Germanic validation capabilities

The Actions job validates **portable** capabilities explicitly. A green portable
job does not certify full local science validation, availability of original
holdings, repeated page-image inspection, or a fresh Foma execution.

## Commands

From the repository root:

```sh
python3 Germanic/tools/run_portable_checks.py
python3 -m pytest -q --validation-mode=portable Germanic/tests
python3 Germanic/tools/pgmc_reconstruction_survey.py --mode portable
python3 Germanic/tools/artifact_graph.py --check --mode portable
```

The runner preflights the survey once, runs bibliography, regression, artifact
graph and index checks, writes complete logs and JUnit results to `.ci-results/`,
and produces the Actions job summary. Scratch files stay inside that directory.
A missing required tracked basis stops at preflight, rather than producing
hundreds of dependent failures.

Actions fetches repository history because the lexical-publication preservation
tests compare current models with the committed errata baseline. A portable
checkout excludes untracked holdings and runtime assets, not the historical Git
objects needed by those assertions.

The coordinated lexical merge also refreshes four existing knee-table index
override locators after paragraph insertion, and excludes two newly exposed
prose candidates: the ordinary word "reconstruction" and the explicitly
counterfactual buy illustration in the thought report. These are scoped index
decisions, not changes to scholarly prose, reconstructed inputs or scientific
baselines.

Strict local defaults have not changed:

```sh
python3 Germanic/tools/pgmc_reconstruction_survey.py
python3 -m pytest -q Germanic/tests
python3 Germanic/tools/artifact_graph.py --check
```

Full survey validation requires **every declared holding**, including excluded
holdings and PDF-only sources. The command verifies actual available input
hashes against recorded provenance. Provision the declared library first;
the pytest suite performs the same holding/evidence preflight once. Completeness
flags such as `--require-feature-alignment-complete` retain their independent
reading, attribution and analytical gates in either mode.

Full pytest and graph validation additionally require the canonical isolated Foma runner,
compiled stage bins and build manifests. Portable mode never executes the
`runtime_bins`, `full_trace`, `lexical_sources` or `interaction_matrix` nodes,
even if local binaries happen to exist. Synthetic runtime-validator tests and
integrity checks over committed runtime receipts still run; these are not new
runtime evidence.

The pytest `runtime` category checks the full graph's runtime nodes once in
full mode, not once per adjudicated SC. Missing runtime manifests are strict
failures, not automatic success or availability-based skips. Portable selection
records this category as explicitly not run, with the provisioning cause.
The live `SC024 --evidence` integration tests belong to that category too:
portable mode skips every runtime-marked test even when Docker happens to be
available. Full mode retains the live rebuild and the strict runtime freshness
gate. Container availability alone must not expand a portable invocation's
declared capabilities.
The older SC021--SC027 live-probe decorators and the local build-version
comparison carry the same explicit marker; their committed-evidence and
synthetic validator tests remain portable.

## Three-level development validation workflow

Running the entire strict suite after every intermediate edit is unnecessary;
running it once against the final candidate state is mandatory. The levels are
cumulative capabilities, not alternatives, and a previous full pass never
certifies a subsequently changed scientific or publication state.

**Level A — focused development checks** (seconds to a few minutes). Run the
tests owning the files being edited, for example during lexical publication
work:

```sh
cd Germanic/tests && python3 -m pytest -q \
    test_lexical_editorial_publication.py test_pgmc_lexical_integration.py \
    test_lexical_editorial_order.py
python3 Germanic/docs/tools/check_reader_facing_semantics.py
```

**Level B — integrated consistency** (a few minutes). After a coherent group
of SOURCE edits:

```sh
python3 Germanic/tools/adjudicate.py --refresh   # must end CONTROL PLANE CLEAN
python3 Germanic/tools/adjudicate.py --status    # read-only three-axis report
```

`--status` reports scientific adjudication state, baseline fingerprints,
artifact-graph freshness and lexical publication obligations (including
explicitly selected articles that are missing, unassembled or unledgered),
and states explicitly that full validation is a separate axis it cannot attest.

**Level C — full strict validation** (the authoritative final gate). Once the
SOURCE state is final:

```sh
cd Germanic/tests
python3 -m pytest -q --ignore=test_evidence_interface.py
python3 -m pytest -q test_evidence_interface.py   # exclusive: rebuilds canonical bins
```

Level C validates the **current** scientific state. Five historical-replay
tests (listed below) report as explicitly skipped here by design; they are an
independent reproducibility lane, not part of current-state correctness.

Intermediate commits may land with their validation status stated honestly;
the full strict suite runs once against the final candidate tree, and again
only if repairs change what was certified. Record the exact tested commit.
A portable GitHub Actions pass is never equivalent to this gate.

## Current state, incremental regression, historical reproducibility

Ordinary validation distinguishes three forms (full architecture, inventory
and rationale in `docs/HISTORICAL_REPLAY.md`):

**A. Current-state correctness** — the Level A–C workflow above: the current
executable model, corpus, registries, artifact graph, provenance, protected
fingerprints and frozen baselines. Protected baselines remain independent
assertions precisely because consecutive comparisons cannot detect cumulative
drift from an older accepted result.

**B. Incremental regression** — compare the current model with its immediate
predecessor only (uncommitted executable inputs vs `HEAD`, otherwise `HEAD`
vs its first parent; merge commits and parentless states are reported
explicitly):

```sh
python3 Germanic/tools/incremental_regression.py [--json out.json] [--fail-on-change]
```

The report covers final OE outputs, every named-stage snapshot, rule order,
corpus membership/inputs and firing populations. Differences are documented
and adjudicated, not automatically rejected. Builds and evaluations are
reused through the content-addressed cache (`.capr_compile_cache/`,
untracked; keyed by grammar, corpus, context metadata, build tools and image
— never by a bare commit id), so identical executable inputs trigger no
fresh Foma execution at all.

**C. Historical reproducibility** — live reconstruction of commit-pinned
historical models, run only when a historical claim is reconsidered, replay
infrastructure changes, a recorded result is suspect, or a deliberate audit
is requested:

```sh
cd Germanic/tests
python3 -m pytest -q -m historical_replay --historical-replay
```

The five tests moved out of routine execution into this lane (still
collected, reported as skipped with the explicit reason by default — the
suite count does not silently shrink):

- `test_sc035_prosody.py::test_fresh_commit_pinned_comparison_reproduces_the_entire_receipt`
- `test_sc035_model_comparison.py::test_fresh_foma_comparison_reproduces_every_recorded_intermediate`
- `test_sc035_prefix_reduction.py::PrefixReductionTests::test_fresh_container_assay_reproduces_census_controls_and_counterfactuals`
- `test_rainbow_2148_adoption.py::test_fresh_container_capture_and_private_controls_match_committed_receipts`
- `test_chronology_consistency.py::test_original_displacement_is_contingent_on_the_retired_early_glide`

Their immutable receipts, provenance and hash checks still run routinely;
what the ordinary suite deliberately no longer provides is live re-derivation
of those receipts. Verifying a receipt and reproducing it by fresh Foma
execution are different assurances and are reported separately. The exclusive
`test_evidence_interface.py` canonical-rebuild test is current-grammar
validation, not historical replay, and is unchanged.

## Safe parallel execution (optional, full mode)

The suite divides into three concurrency classes:

1. **Independent tests** (unmarked): pure source/projection checks using
   read-only authorities or disposable temporary directories. Safe in
   separate processes.
2. **Runtime tests** (`-m runtime`): share the single authoritative Foma
   binary directory and backend container (`capr_runtime.layout()`); two
   concurrent compilations against those bins are forbidden. Serial only;
   `conftest.py` fails any runtime-marked test that executes inside a
   pytest-xdist worker rather than risking shared-artifact corruption.
3. **Exclusive runtime** (`test_evidence_interface.py`): rebuilds the
   canonical bins and `oe_build_manifest.json`; always runs alone, last.

Canonical parallel invocation (requires `pytest-xdist`, pinned in
`Germanic/tests/requirements-test.txt`):

```sh
cd Germanic/tests
python3 -m pytest -q -m "not runtime" -n 4 --dist loadfile \
    --ignore=test_evidence_interface.py        # lane 1: parallel
python3 -m pytest -q -m runtime \
    --ignore=test_evidence_interface.py        # lane 2: serial runtime
python3 -m pytest -q test_evidence_interface.py  # lane 3: exclusive
```

`--dist loadfile` keeps each test module's shared fixtures on one worker. The
three lanes together collect exactly the tests of the serial Level C commands
(measured 2026-10-29: 1584 + 45 + 24 = 1653 collected tests); verify with
`--collect-only -q` when in doubt. Each xdist worker repeats the
session holding/evidence preflight (a few seconds per worker). The serial
route remains the reference; use the lanes when iterating on large changes.

Measured on an 8-core M-series host (2026-10-29): the full serial Level C
run (everything except `test_evidence_interface.py`) takes 77 minutes
(1629 tests, 9152 subtests); lane 1 with `-n 4` runs in
about 13 minutes against roughly 18 minutes serially; lane 2 is about 47
minutes and is the dominant cost, spent waiting on container Foma work
(user CPU under six seconds), so xdist cannot reduce it and the overall
full-suite gain is modest. Since 2026-10-30 the five historical-replay
reconstructions are no longer part of lane 2 (they are the explicit
`--historical-replay` lane above), which removes their historical cascade
compilations from every routine run; the remaining lane-2 cost is
current-model container work. The honest recommendation is: use Level A/B
during development, parallelise lane 1 when iterating broadly, and accept
the serial runtime lane until its container work is itself restructured
(for example by reusing one immutable compiled snapshot across read-only
runtime tests), which is future work requiring its own adjudication of
evidence-freshness semantics.

## Portable evidence and provenance

Portable validation requires bibliography keys, declared library-contained
holding paths, readable tracked non-original verification bases, reciprocal
evidence/review links and the existing analytical identity/attribution checks.
The only absence exemption is an **untracked declared original PDF**. An
original PDF used as a historical evidence basis must belong to that evidence's
declared source. Missing tracked PDFs, text bases, unsafe paths and source/hash
regressions remain failures. Stiles1986a/b need not acquire invented text
derivatives: PDF-only declarations are valid.

Historical `page_image_checked` and other verification records are preserved,
not upgraded or rerun. Portable rendering reports unavailable holding paths
explicitly. Available sources are still hashed. Provenance freshness compares
all available input hashes and population/analysis metadata; only declared
unavailable originals are exempt from an impossible current-byte comparison.

Regenerate through the canonical control plane:

```sh
python3 Germanic/tools/adjudicate.py --refresh
python3 Germanic/tools/adjudicate.py --refresh --mode portable
```

The first command remains strict and includes runtime validation/builds. The
second refreshes portable projections only. Its survey provenance identifies
`validation_mode: portable`, unavailable holdings and the fact that image
verification was not repeated. Previously recorded hashes of missing originals
move unchanged into `historical_unavailable_inputs`; a genuinely unrecorded
original has an explicit `null`, never a fabricated or replacement hash.
Current tracked hashes can therefore refresh without original PDFs. Full
validation, once originals are available, compares their real hashes with
those historical values and fails on a mismatch or absent recorded hash.

## Repaired regression authorities

The 2026-10-11 Actions log (run `38177868157`, commit `7848f762`) contained
2453-versus-2456 production and 2365-versus-2368 printable-count failures.
Comparing generated occurrences against the preceding `5beb487c` state traced
the three removed occurrences to the evolved cud model: the old `*kwedu-2`
span and redundant `cweodu`/`cudu` mentions disappeared. Adder and cud source
line locators also moved. This was not an extractor regression.

Frozen historical count dictionaries and scientific baselines remain intact.
Live expectations now derive from the **complete** canonical production
pipeline (including table and broad-prose decisions), with exact occurrence
multisets, print partitions, book/emission joins and regenerated graph freshness
still enforced. The obsolete cud checker sentinel is no longer required in
publication prose.

The historical cud variety-audit locator can rebase read-only from line 32 to
line 39 only when exactly one surviving current occurrence retains an exact
historical `.iv` tag with the same source path, form sort key and variety.
Missing, changed or ambiguous anchors fail; audit evidence and judgments are
not edited.

The graph inventory test omitted the already-existing reconstruction-survey
and lexical-integration projection nodes. Both are now declared in its expected
inventory, with output ownership and archive exclusion checks retained.
Registry/memo agreement now checks registry and memo verdicts directly, rather
than rerunning the entire binary-dependent graph for every adjudicated SC.
`adjudicate SCNNN --check` still performs the full strict propagation check.
The next-SC test derives its expectation from current eligible registry rows
and the administrative programme start, rather than pinning SC032 and failing
when that adjudication completes.

An actual dedicated-branch Actions run also exposed an output-introspection
bug: listing the lexical-integration node's owners invoked its full renderer
and unnecessarily required original PDFs. Its output declaration now uses the
integration module's canonical `OUTPUT_NAMES`, without validation or builds.
The renderer and freshness check retain their explicit capabilities. Hidden
`.ci-results/` log uploads are explicitly enabled, with only log/XML/summary
files selected, not scratch directories.

The provenance refresh also exposed two pre-existing stale tracked
reading-accountability hashes; canonical regeneration updates their hashes,
not the evidence. All declared holdings now participate in provenance, rather
than silently omitting nonconsulted declarations.

## Coordinated recovery verification

The CI release `fc6ded21` survived the agent's later quota failure and was
verified against its successful Actions run `38223318332`. On the combined
lexical/SC032 tree, portable pytest passed 1,319 tests and 7,360 subtests with
the single runtime-category skip. After the scoped index repairs above,
206 affected tests and nine subtests passed, the index checker passed, and
the strict graph and SC032 propagation checks passed. The strict local runtime
test separately passed against 107 fresh bins; no Foma rebuild or new
page-image inspection was performed.

A clean staged checkout without the 32 untracked originals or runtime assets
passed portable survey, graph and index checks without regeneration. Its
publication preservation tests passed once the required errata Git object was
available. Default full survey validation rejected that checkout at the missing
Orel PDF, while full validation with the actual local holdings passed. Two
existing CRLF worktree receipts were restored to their declared LF encoding;
their committed SOURCE content did not change. FST, corpus/context data,
survey evidence, adopted registry decisions and frozen baselines are unchanged
by this CI integration. These are local combined-state results, not a claim
that the merged commit has already run on GitHub Actions.
