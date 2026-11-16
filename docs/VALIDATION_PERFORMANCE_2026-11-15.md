# Assertion-directed validation performance

## Scope and measurement

The base is current `update`,
`54b15a2d3a764d5ac92c9ce0c1ecaf398aed878f`. This performance work is independent
of the SC044 review branch. Production grammar, corpus and input contexts,
chronology, expected strings, frozen baselines and historical receipts are
unchanged. All 17 original SC037 test bodies are AST-identical to the base.

Measurements used the provisioned Docker/Foma backend on an eight-logical-CPU,
16 GiB arm64 Mac, Python 3.14.3. Compilers ran sequentially, with ordinary warm
filesystem caches; no cold-cache guarantee or hardware-independent budget is
claimed. The baseline uses the unchanged worker with a private pass-through
observer to retain its actual JSON, recipes, calls and checkpoint inputs.
No captured result substitutes for live execution.

Complete baseline/candidate JSON, logs, JUnit, source-bound execution receipts,
comparison scripts and timing records are outside the checkout, under this
session's `files/validation-performance/` directory. Original exit statuses and
failed development checks are retained. The final review records the exact
tested source identity and strict receipts separately; these measurements are
not a certificate for a later commit.

## Baseline and retained coverage

Collection proves a disjoint union of 1,947 independent, 94 runtime and 26
exclusive nodes: exactly the 2,067-node strict reference. The live baseline
passed 1,947 independent tests, 89 runtime tests and 26 exclusive tests, with
the five prescribed historical-replay skips. Independent/runtime subtests
numbered 9,781/40. The opt-in historical replays and ordinary archive-integrity
checks remain available.

| Baseline phase | Measured wall |
|---|---:|
| Independent full, four workers, loadfile | 82.94 s |
| Serial runtime | 3466.56 s |
| Exclusive evidence interface | 417.39 s |
| Strict split total | 3966.90 s (66m07s) |

The SC037 fixture setup was 2717.33 s; the worker itself took 2716.10 s.
Chronology setup was 572.15 s, including initial preparation of the session's
shared definitions. Its five-model compilation/evaluation took 210.06 s.
The independent lane's longest calls were graph freshness (32.45 s),
publication freshness (27.02 s) and citation-range validation (10.08 s).
This does not warrant another survey-loader optimization.

## Dart pilot and default SC037 plan

The existing fixture derives the request from the actually selected module
nodes. Selecting only the dart node requests one current raw-input endpoint
and AF66Good/AF66Closed, not a population sweep or unrelated models.
The normal module requests the full assertion dependency plan.

```sh
python3 -m pytest -q Germanic/tests/test_sc037_intervention.py::test_selected_dart_protects_closed_final_pre_l_nonapplication
```

The pilot passed in 388.03 s pytest wall (388.61 s receipt-wrapper wall).
The endpoint and good tail freshly give `sċytel`; the closed-final foil
freshly gives `sċytl`. The raw tail input is the provenance-validated canonical
checkpoint before `OELAdjacentSyncope`, not an expected answer. Sparse raw
fidelity records override display forms where the canonical schema requires
it. Input contexts and historical stages use the existing readers/resolver.

The compiler's default behavior and `components_only` semantics are unchanged.
`include_final=False` omits only the complete root, retaining requested staged
networks. Filtering precedes Foma emission, including helper/tail definitions.
Generic component exports belong only to current; all 15 consumed closeout
tails remain in the full plan. Replacements and insertion positions are
unchanged in every variant.

| Emitted network/call inventory | Legacy full | Planned and measured full | Dart only |
|---|---:|---:|---:|
| Complete variant roots | 13 | 8 | 1 |
| Distinct staged suffixes | 52 | 11 | 0 |
| Generic component exports | 169 | 13 | 0 |
| Closeout tails | 15 | 15 | 2 |
| Total exported networks | 249 | 47 | 3 |
| Actual Foma subprocesses, including fresh definitions | 14 | 14 | 2 |
| Actual lookup subprocesses | 132 | 64 | 3 |
| Submitted forms, before boundary markers | 715 | 536 | 3 |

Fewer networks do not imply fewer full-module compiler subprocesses.
The first optimized full worker took 1343.47 s versus 2716.10 s baseline.
Definition preparation was 343.04 s versus 364.61 s; recipe compilation
totalled 987.41 s versus 2309.29 s. These are sequential observations, not
repeated-run confidence intervals. The current recipe itself varied upward
from 431.20 s to 466.88 s; the reduction is not a uniform per-compile speedup.

Semantic comparison proves:

- all 394 complete selected records are equal, including raw/contextual inputs,
  comparators, output sets, rejection and multiplicity;
- every consumed full-module result, requested lookup input/output set and
  unique raw checkpoint agrees with the legacy run;
- all variant composition orders and required definition bodies agree;
- dart-only results equal the full-run slice, and the same original assertions
  execute in the full module.

The independent pytest strings still distinguish every relevant wrong model.
New tests cover unknown requests, missing/duplicate checkpoints, missing
fidelity, rejected/ambiguous states, transitive definition filtering,
staged-only compilation and preservation of existing compiler defaults.
Instrumentation is tested with a real child process and a real nonzero exit.

## Routine checkpoint versus promotion

The measured owning command includes the full SC037 module, its planning tests
and all existing isolated-compiler tests:

```sh
python3 -m pytest -q Germanic/tests/test_sc037_execution_plan.py \
  Germanic/tests/test_anglo_frisian_experiments.py \
  Germanic/tests/test_sc037_intervention.py
python3 Germanic/tools/run_portable_checks.py --workers 4
```

Owning tests: 81 passed, 152 passing subtests, 1345.65 s wrapper wall.
Portable: 1,980 passed, 98 explicit capability skips, 9,784 passing subtests,
116.09 s wrapper wall. Combined checkpoint: 1461.77 s (24m22s).
No regeneration was required by these test/compiler changes.
The full checkpoint therefore still exceeds ten minutes. The largest costs
are fresh common definitions (5m43s) and current-model staged/component/tail
compilation (7m47s), before the remaining counterfactuals.

Final promotion retains the full independent/runtime/exclusive split and
its fresh scientific execution. A portable pass or focused dart pass does
not certify that gate. Collection, actual outcomes and final source-bound
receipts are checked against the baseline, not inferred from planned counts.

## Refresh, publication and exclusive rebuild

Restoring this base's provisioned runtime after switching from SC044 required
an initial 491.53 s refresh; its log explicitly rebuilt stale runtime bins.
This is reported separately from the already provisioned strict baseline.

On the unchanged candidate, warm refresh took 59.72 s, status 30.11 s,
and the real strict indexed Docker publication 381.17 s. The exact runtime
manifest bytes remained unchanged in all three phases: runtime bins were
verified fresh, not rebuilt. Publication-only generated PDF/log changes
were restored to their original blobs after measurement; no book change
belongs to this performance patch.

The exclusive baseline separately forced its real SC024 CLI rebuild and
ran production/sandbox equivalence, graph verification, census and witnesses.
It took 417.39 s. A warm refresh is not a second forced build, and a fresh
manifest cannot stand in for proof of this invocation's rebuild. No build
reuse or receipt-contract shortcut is adopted here. The standalone exclusive
path and stale/degenerate-bin failures remain intact. Any future sharing
requires an independently reviewed, run-scoped build/candidate/runtime/bin-set,
equivalence and census contract with negative receipt tests.

SC037 pruning alone cannot establish a ten-minute final gate. Chronology's
repeated complete compositions are the next independently reviewed change;
the exclusive forced build and fresh definition preparation remain visible
costs rather than silently weakened assertions.
