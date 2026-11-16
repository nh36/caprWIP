# Current chronology control execution

## Scope and unchanged authority

This follows the SC037 pruning on `perf/validation-sc037` at
`3cefc206d70eb7981e897115ec1857c7d5368b5d`, originally based on `update`
`54b15a2d3a764d5ac92c9ce0c1ecaf398aed878f`. Scientific work remains paused.
Grammar, corpus/context inputs, chronology, expected strings, frozen baselines
and historical receipts are unchanged. This is execution engineering, not a
new chronology adjudication or interpretation of an interaction.

All original chronology test bodies and the pinned historical fixture and
complete-composition evaluator remain AST-identical. The current variant
construction was extracted without changing any executable member, insertion
position or removal. All five maps and every original absence-of-effect
assertion remain in the current test.

## Live prefix/remainder evaluation

`oe_pipeline.stages()` supplies the executable sequences. Their longest common
prefix determines the last unique named cumulative checkpoint; intervening
inline members remain in the variant remainder. Current identity uses the
manifest-validated production bin. The counterfactual boundaries at this base
are derived, not hardcoded:

| Counterfactual | Last common checkpoint | Remainder members |
|---|---|---:|
| Remove glide | OldEnglishOrthography | 2 |
| Earlier lowering | OEFinalUnstressedOLowering | 25 |
| Before umlaut | OEInterStressRaising | 66 |
| Delayed umlaut | OEInterStressRaising | 66 |

Each cumulative bin receives the existing contextual `evaluation_input(row)`.
Every resulting intermediate is evaluated through its live variant remainder.
No canonical suffix answer evaluated on unmodified forms is reused.

Unrestricted remainder compilation alone was insufficient: it took 190.74 s
in the sequential prototype versus 210.06 s for the five complete reference
models. A complete owning-plus-portable checkpoint still took 628.73 s
(10m29s). The long umlaut remainders dominated.

The adopted compiler expression therefore restricts each remainder to the
finite union of its freshly evaluated intermediate inputs, before composing
the unchanged executable members. This limits compilation, not the expected
outputs. Domains are neither supplied by assertions nor read from an archive.
All branches are retained, and final outputs use the original evaluator's
usable-output/deduplication semantics.

Foma literal characters must be separated: adjacent escaped characters can
become one multichar symbol. A failed private prototype exposed this by
rejecting every valid counterfactual input; it was not adopted. The corrected
encoding has live composition checks, including literal operators, zero,
Unicode and an empty domain. Original failed logs/receipts are preserved.

An epsilon intermediate selects complete composition rather than feeding an
empty line to `flookup`. Rejection stays rejection; all branches are evaluated
and deduplicated. A missing unique common checkpoint or empty remainder uses
complete composition. Stale/missing canonical bins and malformed lookup
records fail closed. No ordinary freshness manifest is treated as proof of
an invocation-fresh rebuild.

## Equivalence and measured checkpoint

Measurements use the same provisioned Docker/Foma backend, scientific sources,
four complete row/context payloads and toolchain as the captured reference in
the [SC037 report](VALIDATION_PERFORMANCE_2026-11-15.md). Compiler experiments
ran sequentially, with warm filesystem caches and no cold-cache guarantee.
Glide removal was evaluated first, earlier lowering second, then all five maps.
Every map on all four rows agrees with the complete-composition reference.
The same independent expected strings pass in the original pytest body.

Synthetic live relations additionally demonstrate multiple intermediate and
final outputs, duplicate paths, rejection and epsilon/full fallback against
complete composition. Portable tests exercise dynamic boundaries, inline
members, missing/duplicate endpoints, malformed records, stale manifests,
unsupported literal inputs and actual compiler-count instrumentation.

| Measured quantity | Complete reference | Adopted finite-domain path |
|---|---:|---:|
| Complete assay roots | 5 | 0 |
| Remainder exports | 0 | 4 |
| Assay Foma invocations | 1 | 1 |
| Assay lookup invocations | 20 | 36 |
| Compilation/evaluation worker | 210.06 s | 6.21 s |
| Current test setup, including fresh shared definitions | 572.15 s | 365.76 s |

Both default paths additionally prepare one fresh disposable definition image
per owning pytest session. The adopted worker reports one actual compiler call;
that does not count the separately timed session-fixture preparation. Its extra
lookups are the sixteen live cumulative-prefix evaluations. A different
session's definition preparation must not be attributed to this optimization.
Timing variance is visible: fresh common preparation remains about six minutes
in the adopted owning run.

```sh
python3 -m pytest -q Germanic/tests/test_chronology_execution.py \
  Germanic/tests/test_chronology_consistency.py
python3 Germanic/tools/run_portable_checks.py --workers 4
```

Owning: 27 passed, one prescribed historical replay skip; 367.01 s wrapper
wall. Portable: 1,994 passed, 99 explicit capability skips, 9,784 passing
subtests; 119.19 s. Combined chronology checkpoint: 486.20 s (8m06s), with no
regeneration needed. The SC037-owning checkpoint still exceeds ten minutes;
this is not a claim that arbitrary owning sets or final promotion fit.

The fixture emits compiler/lookup timings, plans, raw inputs, prefix states,
finite domains and assertion owners in `.ci-results/chronology-current.json`
and JUnit's `chronology_execution` property. These are replaceable invocation
diagnostics, never a result cache. Complete logs, JSON, JUnit, comparisons and
source-bound receipts are retained outside the checkout in this session's
`files/validation-performance/`. The final review records the settled source
identity, strict split results and committed-blob delivery proof separately,
without retroactively claiming a precommit run tested the delivery commit.

## Final gate and build reuse decision

The complete independent/runtime/exclusive split remains required. Its
collection and actual outcomes are compared with the original strict reference
and the first SC037 patch. Five historical replays remain opt-in; archive
integrity, original holding checks, protected baseline and all live scientific
assertions remain ordinary requirements.

The separately measured warm refresh/status and real strict publication took
59.72 s, 30.11 s and 381.17 s respectively, with exact runtime-manifest bytes
unchanged: none rebuilt bins. Source-switch provisioning did rebuild before
the baseline, and the later exclusive test forced another build of that same
restored source. That is distinct from a warm routine checkpoint; it must not
be presented as a saving delivered here.

The real SC024 CLI integration still performs its unconditional rebuild under
the runtime lock, production/sandbox equivalence, graph verification, firing
census and chronology witnesses. Stale/degenerate-bin failures remain intact.
No equal-coverage single-build command/receipt contract was demonstrated, so
the existing strict path is retained. An ordinary manifest or prior level-C
receipt cannot prove that a forced build happened in a new invocation or bind
its exact bins to a downstream census. Sharing would need a distinct reviewed
invocation with run-scoped build, candidate/source, runtime, exact-bin-set,
equivalence and census binding, plus stale/incomplete-receipt negatives.

No command/receipt bypass is introduced. Publication time remains separate;
this test-only follow-up does not alter its scientific or assembly inputs.
The remaining final-gate bottlenecks are SC037's live compositions, fresh
common definitions and the exclusive forced rebuild, not survey loading.
