# Validation performance and proportional workflow

## Scope and measurement identities

The reference integration is `1a3d149a2e3cfa6840a11465e039b86a99a49fcc`.
Portable benchmark code is
`7addaaf4b04ae8f0a2f23476ef1ac7bda1634def`; the subsequent
`9804a9fd4fde37d8faccc988d0e242662c7fdfa9` bounds the synthetic runtime
compiler inside its backend worker. Neither changes executable sound laws,
lexical selections, corpus population, approved Christiansen/little scholarship
or frozen scientific expectations.

Local measurements used an eight-logical-CPU arm64 Mac with 16 GiB RAM,
Python 3.14.3, pytest 9.0.3 and xdist 3.8.0. Runs were sequential, on the same
scientific inputs, without a concurrent compiler benchmark. Filesystem caches
were not forcibly purged: these are ordinary warm-development measurements,
not cold-cache guarantees or promises about GitHub hardware.

Authentic receipts, complete logs, JUnit, profiles, source identities and
comparison inventories are retained under
`.capr-work/validation-performance-2026-11-10/`. This report records measurements,
not a scientific certificate. Final strict and Actions results belong to their
exact tested commit and are published separately with that commit; an older
certificate is not transferred.

## Original costs and baseline qualification

Successful original Actions artifacts establish substantial variation:

| Original run | Validation step | Pytest console wall | Pytest JUnit wall |
|---|---:|---:|---:|
| #185 | 1241 s | 1165.68 s | 1166.744 s |
| #186 | 823 s | 766.93 s | 767.661 s |

Both reported 1925 passed, 73 skipped and 9758 passing subtests, with 1998
collected nodes. These artifact-derived time bases differ from the earlier
rounded attribution of 19 minutes 29 seconds; step, subprocess and JUnit
durations must not be conflated.

The first local instrumentation of the unchanged original runner took
1045.23 s, including 986.86 s in its regression subprocess and a pytest-reported
981.30 s. It was not a clean baseline: supplying
`PYTEST_ADDOPTS=--durations=40` correctly tripped receipt tests rejecting hidden
options. Its 17 failed reports involved 13 distinct nodes; all 13 passed with
nine subtests in 3.66 s when rerun with empty environment options and explicitly
recorded arguments. The failed run and its original exit status are retained.
Its duration is not used for a green-to-green speedup claim.

The dominant repeated work was evidence-universe construction and analytical
validation, not Foma in the portable lane:

* `ReadingScopeTests` consumed 764.833 s and 479.139 s in the two original
  Actions artifacts. Its module contains 201 survey-load callsites, including
  147 in that class and 123 analytical loads there.
* Analytical link validation repeatedly rebuilt the entire available-key set.
  Reviewed core rows also repeatedly scanned the complete forms table.
* Survey validation repeatedly resolved and checked the same holding paths:
  6601 form rows cite only 30 distinct verification-basis paths.
* Original analytical-load profiling recorded 11,059,843 calls / 10.290 s,
  including 28,399 `links` calls costing 7.048 s and 5,319,962 `ids` calls.
  Original survey-load profiling recorded 1,956,329 calls / 1.330 s, including
  13,365 path resolutions and 6769 opens.

The instrumented original regression used about 928.51 aggregate child CPU
seconds over 986.86 wall seconds: repeated Python work and path preparation
were material, not simply an idle subprocess wait. This does not establish
physical-disk contention. Git-history, rendering and subprocess work remain,
but were not grounds for speculative caches or broad fixture rewrites.
No active local validation hook, configured hook path or test-running commit
wrapper was found; sample hooks are not active hooks.

## Implemented reuse and freshness

Analytical validation now uses direct dict/set membership, materializing other
iterables once. A lazy forms-by-row index is built once per validation call.
Survey validation prepares root-relative paths, file status and holding
readability once per call, while retaining every per-record provenance,
containment and evidence assertion.

Nothing survives into a later validation invocation. Changed evidence, tools,
holdings or bibliography are reread through the existing loader and dependency
system. There is no persistent result cache, source snapshot, filename-only
artifact reuse or new general caching framework.

The corresponding profiles were 586,244 calls / 0.279 s for analytical load
and 1,065,311 calls / 0.488 s for survey load. Profiler ratios are not promised
unprofiled speedups. Paired ordinary renders observed portable 5.721 to 1.469 s
and full 5.571 to 1.459 s.

Old and new implementations rendered byte-identical outputs in both validation
modes when supplied the same current provenance inputs. Canonical control-plane
refresh changed only the two validator-source hashes in survey provenance.
Scientific/publication content and runtime inputs did not change.
Focused negative tests verify fresh preparation on the next call, missing and
changed evidence, per-record errors despite reused preparation, multiroot
links, duplicate/unknown/required links and bounded complete-table scans.

## Portable concurrency and reporting

The audit examined 415 mutation/subprocess candidates across 57 files:
tracked writes, fixed scratch names, publication builders, manifests,
environment/global changes, temporary Git repositories and fixture ownership.
Unmarked tests were not presumed independent.

* A stale-projection test now invokes the real generator check on a uniquely
  allocated copy instead of temporarily editing the tracked annotation file.
* SC097 synthetic controls are runtime-marked and execute the same assertions
  inside the provisioned backend. Portable explicitly skips them; no host Foma
  is invoked. The backend owns compiler termination/temporary cleanup at the
  unchanged 600-second limit; the outer command allows 660 seconds.
* The reproduced xdist `PosixPath` failure was reporting metadata: converting
  the subtest label to a string preserves all five underlying assertions and
  allows execnet serialization.
* `--dist loadfile` keeps module-local state together. Incremental diagnostics
  have one owning module; automatic consecutive-full-trace comparison remains.
  Disposable publication fixtures and temporary repositories remain isolated.

No portable test needs a supplementary serial lane after these fixes.
`conftest.py` and its runtime-in-worker rejection remain unchanged. Actual
runtime/evidence execution is never parallelized against authoritative bins.
Full-lane collection independently proved an exact disjoint union:
1916 independent + 69 runtime-serial + 26 exclusive = 2011 nodes.

The runner defaults to serial and accepts explicit `--workers 1`, `2` or `4`.
It retains runtime skips rather than deselecting capabilities. It streams
genuine verbose test output while saving original bytes, reports phase
START/END/status/elapsed time, writes machine-readable timings after every
phase, and publishes completed-phase Actions summaries before final completion.
There is no arbitrary whole-suite timeout or repetitive heartbeat.
A quiet named fixture is visible, but silence alone does not establish a hang.

Original nonzero subprocess statuses win over supplementary JUnit diagnostics.
Missing/malformed/failing JUnit cannot produce a success claim. Tests exercise
missing executables, early pytest failure, missing XML, nonzero exits and a real
child handshake proving output arrives before child exit, including split UTF-8.
Logs, JUnit, timings, skips, failures and slow cases remain available.

## Equivalent-coverage measurements

Each successful run had 1938 passed, 73 explicitly skipped, 9762 passing
subtests, 2011 collected nodes, zero failures and zero deselections. All 1998
original nodes remain; 13 added infrastructure cases and four added subtests
cover the optimizations and runner. Moving the formerly unmarked synthetic
compiler into strict execution accounts for the deliberate local capability
change; original Actions already skipped it without Foma.
All five JUnit testcase/status multisets and suite totals agree exactly:
11773 test/subtest results each.

| Sequential run | Workers | Complete measured wrapper wall | Regression subprocess wall |
|---|---:|---:|---:|
| Serial | 1 | 245.106 s | 206.612 s |
| Two, first | 2 | 153.625 s | 116.370 s |
| Four, first | 4 | 120.189 s | 82.789 s |
| Two, repeat | 2 | 149.373 s | 112.279 s |
| Four, repeat | 4 | 120.061 s | 82.714 s |

The wrapper includes authenticated measurement overhead; runner timing JSON
is slightly smaller. Full phase breakdowns are retained with every run.
Four workers were consistently fastest on this host: approximately two minutes
overall versus 2.5 minutes with two and 4.1 minutes serial. This is a controlled
new-serial/new-parallel comparison, not a same-hardware original-CI speedup.
The historical 13.7-20.7 minute Actions range is informative, not controlled.

The optimized serial leaders were `ReadingScopeTests` 44.588 s,
`ArtifactGraphTests` 27.064 s, `EditorialPublicationTests` 22.829 s,
`LiveAnalyticalTests` 12.523 s and incremental regression about 11.955 s.
The two/four-worker executions use more aggregate child CPU
(about 245.5-251.2 / 267.1-268.9 s versus serial 231.5 s) to reduce wall time.
The largest-child RSS high-water over the series was about 1.88 GiB; this is
not the summed concurrent-worker footprint or a per-variant memory comparison.

CI installs the existing xdist requirement and chooses four workers on at
least four available CPUs, two on two/three, otherwise one. Actual CPU/memory
and timings are logged, not inferred from the Mac. Update pushes, PRs and
manual branch checks retain the comprehensive portable gate, without duplicate
development push/PR jobs or filename-based exemptions. Cancellation is scoped
to superseded automatic event/ref groups; manual audits are independent.
Existing preflight and bibliography provide useful early failures without a
second expensive full job.

## Bounded strict-runtime investigation

The preserved consolidation evidence includes two 600-second failures
(`experiment.foma` and focused common definitions) and an identical
common-definition source completing in 310.4445 s. The successful compiler used
305.2444 user + 5.0986 system CPU seconds and 2,317,692 KiB peak RSS, about
2.2 GiB. Source SHA256:
`37b7811ca68c0358d26e25d58fe5d697e7d560a61a1896190c5c72f93583af0e`.
The original exact profile script identity and complete failed/successful
records remain with consolidation evidence.

The backend uses native aarch64 Foma 0.10.0alpha, not emulation; Docker exposed
eight CPUs and about 7.65 GiB without a CPU quota. The successful sample was
CPU-bound. No contemporaneous resource trace establishes why failed attempts
were slower: contention or memory pressure remains a hypothesis, not a finding.
No extra repeated expensive profiling compiles were started merely to obtain
a favorable sample, and the 600-second limit was not raised.

The SC037 worker prepares one current common-definition image and 13 recipe
compilations: 14 expected compiler invocations from static inspection, not a
new instrumented invocation count. Its recipe defines 15 closeout tails plus
staged/component networks, even when selecting one node. The image-reuse
implementation checks source/environment/compiler/library/startup/image
identities and restores macros; it is not an existence-only cache. Other
isolated assays have a separate session image.

The independently executable dart selector remains a separate runtime task.
The concrete early-filtering/current-cascade/AF66Good/AF66Closed proposal and
focused-versus-full equality requirements remain in
[the regression-control review](REGRESSION_CONTROLS_PILOT_REVIEW.md#bounded-independent-control-proposal).
A casual single-node selector still constructs unrelated models and is not
the proposed improvement. Neither that selector nor the 17-record register is
implemented here.

## Operational outcome and retained assurance

[Live validation instructions](CI_VALIDATION.md) and
`.github/copilot-instructions.md` now require focused A during development,
canonical B after coherent SOURCE/dependency changes, and final strict C once
the scientific/publication or validation-execution state is stable.
Pure administration does not trigger repeated hour-long certification when
dependency analysis establishes no scientific/publication consequence.
Documentation is not automatically exempt; older exact-state receipts remain
historical, not fresh execution.

The canonical target remains 394 accepted derivations, 386 matches and eight
inherited mismatches. Original-source checks, frozen expectations, historical
replay, publication/index requirements, strict serial/exclusive boundaries,
research worktrees and the protected dirty source-plan checkout are preserved.
No archives, remote branches or filesystem layout are retired or relocated.
Remaining expensive current-model Foma construction and its unexplained
variability warrant separate bounded runtime work, not weakened assurances.
