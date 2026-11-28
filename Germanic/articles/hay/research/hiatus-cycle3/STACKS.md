# Cycle 3: matched front-hiatus stacks

## R1: reproduction and matched placement

**Question.** Does changing only the short unlike-front-hiatus
mechanism change independent predictions? A difference in nonfinal
endpoints on the same inputs and at the same sites would falsify
equivalence. A difference confined to a representation control or
an optional edge rule must not decide the nonfinal comparison.

**Identity and current state.** Intake
`fb1d39abab2420faa90ef7bd4a19751ac4a17321`; frozen runtime
`113101ac5f169b589e1a9647cdf24d32cdd4d919`. The runner reads the
cycle 2 scripts from the intake commit, not the live worktree.
The [cycle 2 verdict](../hiatus-cycle2/ADJUDICATION.md) retains
the S1 foot guard in research and identifies T5m as the widest
reference, not a production decision. See the [earlier stress
diagnosis](../hiatus-cycle2/STRESS.md), [nasal dossier](../hiatus-cycle2/COUCH.md),
and [complete component history](../hiatus-cycle2/STACKS.md).
The accepted medial receipt reproduced byte-for-byte, and the
new runner checks the archived T5m panel traces on all three
orders. The accepted reference remains available unchanged.

**Comparison.** T5m-0 removes only the experimental short
front-hiatus operations. All arms retain S1, the early back
operations, intervocalic-only *hw* treatment, back/broken
contraction and high-vowel absorption. D/J/N all test the
same *d, þ/ð, n* environments at the same two sites, before
`OEUnstressedEIContraction` and before `OEContraction`
(after `OEHLoss`). The reference additionally has edge and
prevocalic incorporation; neither policy is part of the matched
medial comparison. The `-edge` arms add only absolute-edge
resolution before the first anchor; an isolated trace contrasts
this with an explicit member boundary and ordinary adjacency.
The latter probes are not asserted historical compound parses.
Serial operations are adjacent in R1; this is not a chronology
search. `PostH` aliases distinguish the second use of the same
network in the receipt rather than overwriting its first trace.

**Diagnostic results.** The 104 common inputs per order include
full submissions and separately entered, independently qualified
historical comparisons. D, J and N all turn the late ‘flock’
injection into *ēde*, the ‘call’ past injection into *ġecēde*,
and the short ‘strike’ injection into *slēþ*. A/B2 give
*strēne* for the conditional ‘couch’ accusative; canonical
still gives *strīene* from its independently different history.
All three also replace the ‘strew’ glossary comparator's
*streide* with *strēde* if the supplied lexical identity stands.
This adverse prediction is retained, not scored away.
The common back-vowel and ‘see’ outputs and both *cǣġ/cǣġe*
controls persist. N additionally contracts the injected atomic
‘gain’ probe: its network cannot distinguish inherited from newly
assembled atomic `*ei`. This is a technical collision on a local
probe, not a new historical feeding witness.

Under A's full ‘hay’ input, the medial-only arms leave syllabic
`*e*i` (rendered *hei*); independent final D, J and N give
*hē*, *heġ* and atomic `*ei` (also rendered *hei*), respectively.
The native canonical and B2 full inputs do not supply the same
short hiatus and are not failed test cases for edge placement.
The same head-domain assumption is used across the new first
steps; the fate of accent during incorporation, the broad scope
of each second step, and the loss of foot information at *h*-loss
must be tested separately.

**Verdict:** retain the common substrate; defer historical choice
among the matched nonfinal mechanisms. This is a comparison of
private operations, not a registry verdict. R1 introduces no
historical chronology edge and no corpus or model propagation.
The firing census on the wider frozen panels is deferred to the
promising integrated alternatives after the lexical checks.

**Replay and validation cost.** One private compilation per
invocation on the existing frozen stage cache, followed by
24 × 104 historical-panel traces and isolated edge probes.
No new default-suite compilation, fixtures, concurrency or
full-corpus reruns are added. Full per-stage receipt:
[integrated-traces.json.gz](integrated-traces.json.gz).

```sh
set -o pipefail
cache=/tmp/capr-hay-stress.lVemXDSn
prior=Germanic/articles/hay/research/hiatus-cycle2
cycle=Germanic/articles/hay/research/hiatus-cycle3
bash "$prior/run-container.sh" --medial --stage-cache "$cache" |
  gzip -n -9 | cmp "$prior/medial-traces.json.gz" -
bash "$cycle/run-container.sh" --stage-cache "$cache" |
  gzip -n -9 | cmp "$cycle/integrated-traces.json.gz" -
```

In a new cache, use the [cycle 2 warm-up commands](../hiatus-cycle2/ADJUDICATION.md#command-and-commit-ledger).
