# SC037 assertion-selected research checkpoint

The PR #15 measurements below are retained as historical comparisons. The
[bounded closeout](#bounded-validation-closeout) gives the current complete
routine command and enforceable cost-review policy.

## Scope and source identity

This validation-only change is stacked on PR #14,
`522ef70708c26201349b18991b28599e49117de1`, itself stacked on PR #13,
`3cefc206d70eb7981e897115ec1857c7d5368b5d`. Both open PR heads and remote
branches were verified before creating `perf/sc037-research-checkpoint`.
Production grammar, corpus selections, chronology decisions, protected
baselines, SC044 and archived scientific evidence are unchanged.

Each measurement has an authentic command receipt binding its HEAD, changed-file
SHA256 map, original exit status, stdout/stderr and JUnit when applicable.
The review bundle contains both previous PRs' evidence and this change's raw
comparisons, diagnostics and receipts. `selected-final-summary.json` and
`selected-final-validated-identity.json` identify the settled strict candidate;
the delivery proof maps those exact validated bytes into the review commit.
The final strict totals and artifact location are reported on the stacked PR.

## Measured normal checkpoint

The provisioned Docker/Foma machine is the same arm64 Mac with eight logical
CPUs and 16 GiB RAM used for the previous measurements. Canonical runtime bins
were already fresh and manifest-validated; definitions were freshly prepared,
not retrieved from a persistent cache. Competing compilers ran sequentially.

| Phase | Wall seconds |
|---|---:|
| Owning, planning and compiler tests | 368.78 |
| Portable validation, four workers | 122.50 |
| Complete checkpoint driver | 491.29 (8m11s) |
| Required regeneration | 0: validation-only edits |

The owning run executed 104 tests and 156 subtests, explicitly deselecting only
the two extended SC037 nodes. All 18 routine SC037 assertion owners executed.
Portable validation passed 1,997 tests and 9,784 subtests, with 103 explicit
capability skips. This is down from the previous SC037 checkpoint's
1,461.77 seconds (24m22s), a 66.4% reduction, not a dart-only timing.

From the repository root, with `EVIDENCE` naming an existing directory outside
the checkout, the measured owning command was:

```sh
python3 -m pytest -q -m "not sc037_extended" \
  Germanic/tests/test_sc037_execution_plan.py \
  Germanic/tests/test_anglo_frisian_experiments.py \
  Germanic/tests/test_chronology_execution.py \
  Germanic/tests/test_sc037_intervention.py \
  Germanic/tests/test_glossary_h_loss.py::test_clay_has_a_front_ending_with_h_then_hiatus_then_contraction \
  Germanic/tests/test_sc065_adjudication.py::SC065AdjudicationTests::test_firing_population_over_all_rows_is_the_consolidated_population \
  Germanic/tests/test_sc065_adjudication.py::SC065AdjudicationTests::test_negative_controls_pass_the_stage_untouched \
  --durations=12 --durations-min=0 \
  --junitxml="$EVIDENCE/routine-01-owning.junit.xml"
python3 Germanic/tools/run_portable_checks.py --workers 4
```

`checkpoint.py` in the bundle times both commands together, checks their
original statuses and receipts, snapshots worker/image diagnostics and compares
consumed results. Diagnostic flags are not passed to formal strict receipts.
The checkpoint receipt predates the final documentation and restoration of an
existing planning-test node name; the executed assertions are unchanged.

For a representative, narrowly scoped `OELAdjacentSyncope` investigation, select
both closed-final nonapplication and open-medial application:

```sh
python3 -m pytest -q \
  Germanic/tests/test_sc037_intervention.py::test_selected_dart_protects_closed_final_pre_l_nonapplication \
  Germanic/tests/test_sc037_intervention.py::test_selected_nettle_has_live_open_medial_deletion
```

That exact two-owner union was also executed: two passed in 306.22 seconds,
including fresh definitions; the worker itself took 4.67 seconds, with one Foma
call, three bounded exports and nine lookups. No other variant or population
sweep ran. For a narrow research checkpoint, follow owning tests with portable
validation, adding owning planning/compiler tests whenever that machinery
changes. The broad measured command above demonstrates the complete routine
scope including those tests, rather than estimating it from this example.

If edited SOURCE requires regeneration, canonical refresh/status must precede
portable freshness checks and its measured time must be added. This
validation-only measurement does not promise that grammar-changing checkpoints
with regeneration fit ten minutes.

## Execution plan and actual costs

| Work | PR #14 full worker | New routine | New complete module |
|---|---|---|---|
| Current raw endpoints | Recompiled identity-style root and 394-row sweep | Production bin; requested endpoints only | Same |
| All-row production invariant | Repeated in SC037 and clay/fringe | Unchanged clay/fringe owner | Same |
| Unrestricted complete roots | 8 | 0 | 0 |
| Counterfactual raw cascades | Complete roots | Exact finite domains, four variants | Exact finite domains, seven variants |
| Staged work | 11 distinct unrestricted suffix compositions | Requested exact-domain remainders | Same, with complete assertion union |
| Components/closeout tails | 13 generic component exports plus 15 tails | Requested bounded queries; all 15 tail definitions consumed | Same |
| Compiled variants | 13 | 10 | 13 |
| Bounded exports | None | 54 | Recorded by full-run diagnostics |
| Worker Foma calls | 14 including private preparation | 10, plus one shared preparation | Recorded by full-run diagnostics |

More bounded exports do not mean more unrestricted compositions. Each variant
is compiled once, with only the required helper-definition closure and queried
finite inputs. Original replacement and insertion placement is preserved.
The old full/dart reference worker remains explicitly runnable with
`--reference`; ordinary pytest never silently falls back to it.

Fresh shared-image preparation took 322.91 seconds (323.14 including its runner).
SC037's worker took 36.54 seconds, including 89 `flookup`, ten Foma and ten `ldd`
calls. Its subprocess lookup phases totalled 3.50 seconds. Per-variant model
preparation/compilation wall times, excluding their subsequent lookup phases:

| Variant | Seconds |
|---|---:|
| `no-weight` | 3.63 |
| `current` | 3.42 |
| `no-high` | 3.29 |
| `opaque-umlaut` | 3.45 |
| `no-unrounding` | 3.16 |
| `late-n-loss` | 3.15 |
| `no-n-loss` | 3.12 |
| `old-w-loss` | 3.14 |
| `early-high` | 3.36 |
| `late-high` | 3.21 |

The longest owning setup was 360.07 seconds, which includes fresh shared
preparation and the SC037 worker. The protected-baseline owner's setup took
6.07 seconds. Raw receipts retain all call/setup durations; subprocess profiles
separate compilation from lookups.

Every model actually loaded the same session image, with an identical image
receipt and no fallback. The former SC037-only
`CAPR_AF_DEFINITION_ISOLATED=1` wrapper changed the compiler environment identity
and prevented reuse. Removing that unnecessary flag, rather than weakening
identity validation, permits sharing. The existing live compiler test proves
both actual full-source fallback with that differing environment and actual
image loading after restoring it.

Production-only selections request no definition image. A separate live
nettle-plus-fee selection passed both tests in 1.42 seconds: 0.92 worker seconds,
five lookups, no Foma calls and no image preparation.

## Equivalence and failure controls

Before switching endpoints, live manifest-validated `old_english.bin` matched
the captured SC037 identity-style reference on 399 unique raw forms: every one
of the 394 selected records and all additional raw queries, including `féxu`,
`féxą`, and the three compound inputs `sáli-wàrðaz`, `sáli-wàrðuz`,
`sáli-wàrðą`. Record/context payloads and output sets agreed; neither evaluator
rejected or produced ambiguous outputs on these inputs. Expected strings remain
in the pytest assertions, independent of this comparison.

The routine report matched all 67 consumed legacy probes, their exact recipe
orders and the live checkpoint inputs. The dart/nettle run matched its legacy
slice. The final complete-module comparison additionally checks every full
probe and both selected-run slices against the same source-bound full report.
Comparison uses output sets, not serialized Foma bytes.

Cumulative stage bins consume raw `evaluation_input(row)`, never independently
staged forms. Dart's live `OELAdjacentSyncope` input and output are both
`*ʃ*y*t*i*l`; nettle changes `*n*e*t*i*l*ǣ` to `*n*e*t*l*ǣ`.
Their production endpoints are independently asserted as `sċytel` and `netle`.
The existing overbroad dart foil changes the live pre-stage form to `*ʃ*y*t*l`;
the exact same nonapplication assertion raises on that result. Both original
live dart tails are also retained, independently asserting `sċytel` versus
`sċytl`. No cached trace is offered as fresh evaluation.

Pillow retains its declared entry after `PWGmcFinalBareALoss` and is evaluated
through the actual variant remainder. Synthetic live full-versus-bounded
comparisons cover branching, rejection, duplicate inputs, epsilon input and
epsilon final outputs under the original evaluator's output-filter semantics.
An explicit input adapter avoids treating a blank `flookup` line as a query.
Stage lookup retains all branches and epsilon intermediates. Unknown selections,
missing results and missing/ambiguous required checkpoints fail explicitly.
Instrumentation tests retain subprocess failures and count actual calls.

One development run failed because the backend Python does not support
`zip(strict=True)`; the new uses were removed and the rerun passed 83 tests and
152 subtests. The failed receipt and original exit status remain in the bundle.

## Assertion ownership and deferred comparisons

All existing SC037 test node IDs are retained. The complete module runs every
comparison, including the two explicitly extended nodes, without special flags.

| Existing assertion owner or distinction | Routine coverage | Additional full/triggered coverage |
|---|---|---|
| Compound three-wrong-account comparison | New current/weight owner retains all three `seleweard` outputs and `no-weight` contrasts | Original complete owner retains `old-early`, `bad-breaking`; trigger: compound syncope, breaking or compound input hypotheses |
| Independent furthest/companion stages | Unchanged outputs and weight/high-vowel/opaque-umlaut foils | Same |
| Selected weight, previous breaking/umlaut histories | Widow, knee, filth, spindle and explicit mære/flask outputs remain | Same |
| Selected-population count, outputs, ambiguity and mismatch invariant | Existing clay/fringe fixture compares every live production record with the protected baseline; duplicate SC037 sweep removed | Same unchanged owner |
| Weak/root breaking and front blockers | Original component outputs remain | Same |
| Closed medial/secondary stress/atomic `iu` | Original component and stage assertions remain | Same |
| Filth/spindle order | Early/late/omitted high-vowel deletion remain live; mutation and degemination contrasts retained | Same |
| Early `n` loss, late livestock and fright | Original stage and component foils remain | Same |
| Independently staged pillow | General/old `w` loss and omitted `n` loss remain live | Same |
| Fee transponent | Original three endpoints and explicit selected record remain | Same |
| Weak unrounding/light/positional labials | Original components, companion foil and current `reġnboga` remain | Relocated original `early-b` assertion in its own extended node; trigger: placement of labial realization |
| Little and inherited livestock | Both retained vowels, shortening and wrong-deletion tails remain | Same |
| Dart | Original endpoint/tails plus live nonapplication and falsifying stage foil | Same |
| Open medial/light root/kettle | Original tails plus new live nettle stage/endpoint owner | Same |
| Fright/heaven shortening and `n` scope | Original wrong-model tails remain | Same |
| Sea/dew/pillow `w` scope | All original narrowed/overbroad foils remain | Same |
| Unselected strong plural | Original accusative-gate assertion remains | Same |
| Full HVD firing population and negative controls | Separate unchanged SC065 owners explicitly executed | Same |

No expected output was weakened to obtain a timing improvement. The default
worker selection is complete, not routine; any unmapped pytest owner fails
rather than silently receiving a full or incomplete result.

## Strict promotion remains separate

The final settled candidate uses the documented complete split: independent
full tests with four workers and `--dist loadfile`, runtime tests serially
without an extended-marker exclusion, then the exclusive evidence-interface
suite alone. Collection and JUnit comparisons require all PR #14 nodes and all
original executed/skipped outcomes; the five prescribed archival live-replay
skips remain. Full holding checks and the protected baseline are not removed.

The real SC024 forced-build CLI-path integration is unchanged. Earlier warm
refresh measurements showed no second canonical build to save there; no build
reuse or receipt-contract shortcut is introduced. The previous strict run took
2,244.98 seconds (37m25s). Final strict receipts report the new actual total,
phase times and remaining bottleneck independently of the under-ten-minute
research checkpoint. No publication build is included or required by this
validation-only patch.

## Bounded validation closeout

The closeout starts from PR #15 at
`33f63f6fb56d8d9504319960dd37dec4014b69ee`; live #13--#15 heads were verified.
The authoritative new/enlarged-regression policy is
[regression execution and cost review](CI_VALIDATION.md#regression-execution-and-cost-review),
linked from the repository Copilot instructions. This is not a new validation
system or a CI timeout gate.

The raw single-input record parser is shared only by the current chronology and
SC037 workers. It preserves epsilon, rejection, branches and first-seen
deduplication, rejecting absent, malformed and wrong-input records. Each caller
retains its error/evaluation policy: chronology's epsilon fallback and SC037's
epsilon-input adapter remain separate. The helper is outside canonical trace
hash dependencies because neither the trace generator nor its hashed evaluators
imports it. All `SOURCE_PATHS` bytes, SC037 reference function bodies and the
chronology historical test file were checked unchanged.

Pytest explicitly passes SC037 `session` or `full-source` intent.
`--fresh-isolated-definitions` neither prepares nor loads an image, even with an
ambient image variable. Normal compiling selections require the verified session
image; production-only selections request none. Standalone `--definitions auto`
deliberately retains the previous private preparation behavior.

Portable tests execute the real worker with preparation/compiler spies and
inspect the actual compiler's emitted script. They protect exact probe unions,
unmapped-owner failures, production-only zero compilation/preparation, subset
scope, finite domains and shared-image use. A small live worker case proves both
definition modes with branching, rejection and duplicate inputs, rather than
merely checking the generic compiler option.

### Paired checkpoint and normal command

The same provisioned machine, source, actual Foma binary and workload were used
sequentially. Canonical bins were already fresh; each session image was freshly
prepared and disposable. OS caches were not flushed.

| Phase | Two extended nodes excluded | Complete module |
|---|---:|---:|
| Owning/planning/compiler command | 366.69s; 118 passed, two deselected | 371.75s; 120 passed |
| Portable, four workers | 117.41s | 112.33s |
| End-to-end checkpoint | 484.10s (8m04s) | 484.09s (8m04s) |
| Shared definition preparation | 318.71s | 316.09s |
| SC037 worker | 39.09s | 46.84s |
| SC037 fixture setup | 358.31s | 363.37s |
| Compiled variants / bounded exports / worker Foma calls | 10 / 54 / 10 | 13 / 57 / 13 |
| Worker lookups | 89 | 92 |

Both owning runs passed 156 subtests; both portable runs passed 2,010 tests and
9,784 subtests, with 104 explicit capability skips. The worker's additional
7.75 seconds were offset by variation elsewhere; the equal totals are observed
measurements, not a claim that extra compilation is free.
No regeneration was required: its measured contribution is zero. Required
SOURCE regeneration must still be included for a scientific checkpoint.

The normal command, with `EVIDENCE` naming an existing directory outside the
checkout, is:

```sh
python3 -m pytest -q \
  Germanic/tests/test_sc037_execution_plan.py \
  Germanic/tests/test_anglo_frisian_experiments.py \
  Germanic/tests/test_chronology_execution.py \
  Germanic/tests/test_sc037_intervention.py \
  Germanic/tests/test_glossary_h_loss.py::test_clay_has_a_front_ending_with_h_then_hiatus_then_contraction \
  Germanic/tests/test_sc065_adjudication.py::SC065AdjudicationTests::test_firing_population_over_all_rows_is_the_consolidated_population \
  Germanic/tests/test_sc065_adjudication.py::SC065AdjudicationTests::test_negative_controls_pass_the_stage_untouched \
  --durations=12 --durations-min=0 \
  --junitxml="$EVIDENCE/complete-owning.junit.xml"
python3 Germanic/tools/run_portable_checks.py --workers 4
```

This includes every SC037 comparison as well as planning/compiler owners, the
unchanged all-row protected-baseline owner and the separate HVD census/negative
controls. Targeted dart/nettle and other individual selectors remain available.

### Validation cost entry

The selected portable execution guards are
`test_production_only_worker_never_prepares_or_compiles_definitions`,
`test_worker_sends_only_bounded_selected_compositions_through_shared_definitions`,
`test_full_source_intent_and_standalone_preparation`,
`test_missing_session_image_fails_instead_of_preparing_a_private_one` and
`test_pytest_fixture_passes_definition_intent_without_accidental_preparation`
in `test_sc037_execution_plan.py`. They add no Foma work: compiler/preparation
spies catch work the declarative plan alone cannot see.

The added live owner in that file is
`test_sc037_worker_shared_and_explicit_full_source_execute_the_same_small_live_case`.
The existing generic compiler-equivalence test was considered for reuse but
does not exercise the SC037 private-preparation fallback. This additional case
uses a tiny grammar instead of recompiling production. Before: no added call.
After: one tiny image preparation and two single-network compilations of the
same current probe under shared/full-source modes. Setup printed 0.00s,
call 0.43s and isolated pytest end-to-end 0.46s; the paired run's call was 0.24s.
The maximum actual Foma child RSS was 17,304 KiB (16.9 MiB).

The normal checkpoint also widens from 18 to 20 SC037 owners: the existing
`test_canonical_compound_hypotheses_discriminate_three_wrong_accounts` and
`test_early_labial_realization_changes_rainbow` catch wrong compound accounts
and early labial placement. Before/after counts and setup/end-to-end costs are
in the paired table. Reuse of current production endpoints and existing shared
definitions is retained; no unrestricted root, extra corpus sweep, rebuild or
concurrency is added. Actual Foma peak RSS for `old-early`, `bad-breaking` and
`early-b` was respectively 1,179,012, 1,176,896 and 1,176,972 KiB; the existing
`no-weight` comparison measured 1,177,012 KiB in the same diagnostic.

Memory used Linux `os.wait4` child `rusage.ru_maxrss`, in KiB, for the actual
Foma processes inside the backend, including process startup, not host Python
or a sum of serial peaks. The variant diagnostic reused a verified disposable
image captured from this checkpoint solely for measurement and then deleted
it; ordinary validation did not use a persistent cache. The three extra live
comparisons are justified in routine review by their measured sub-ten-minute
complete checkpoint and unchanged serial memory/concurrency policy.

### Evidence and promotion boundary

The #13--#15 draft artifact was downloaded through authenticated `nh36`
repository-admin/collaborator access, its archive SHA256 was checked, and the
portable verifier rechecked 282 files, 52 successful receipts, retained failures,
399 production comparisons, 70 legacy probes and selected slices. All three
committed-byte proofs were additionally checked against their Git blobs.
This is authenticated owner/admin verification, not an independent second
reviewer's approval. Fresh live manifest-validated production lookups also
matched all 399 archived outputs.

`paired-summary.json`, per-command JUnit/receipts, `memory.json`,
`variant-memory.json`, `prior-review-verification.json` and
`live-production-parity.json` are in the closeout review evidence. Final strict
certification and the exact-byte delivery proof bind the settled candidate;
their results are recorded in the promotion review without transferring the
older candidate's certificate.

The serial runtime guard, real exclusive SC024 rebuild, receipt requirements
and five prescribed historical skips remain. No scientific or SC044 assets
change. Promotion is reviewed in stack order; this closeout does not authorize
further definition-preparation optimization, rebuild reuse, parallel Foma
execution or unrelated evaluator migration.
