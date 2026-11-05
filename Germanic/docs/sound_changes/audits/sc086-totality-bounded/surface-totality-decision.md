# Surface totality: surviving gamma and parser-domain defects

## Identity

Independent totality investigation on `research/full-cascade-functionality`,
reference `e842319430f9f41ac3cb9f1beb8173e1c3d07fb8`; source SHA256
`33d062fe6624a7eae3bf541dbf22a2f89eb4da101fcde5d2a4e8d702b27f41f6`.
This is not a new historical SC or a propagated orthographic adoption.

## Question

Does a general mapping of the surviving velar-fricative tier repair the
representational gap, and does it establish totality over the actual parser
domain? Finite word success cannot establish the latter.

## Current state (before any edits)

`totality-followup.md` is preserved. The actual complete trace for `ɣó` reaches
`*ɣo` before physical110, `OldEnglishSurfaceFilter`. The earlier memo's simplified
`ɣo` omitted the surviving star: both orthographic conversion and ordinary
star-removal coverage lack gamma. This correction annotates, not erases, that
historical record. Production orthography and parser remain unchanged.

## Diagnosis

The private candidate inserts `{*ɣ} -> g,` at the start of
`OldEnglishOrthography`; source SHA256
`c7fe01dc68c1dae78e17bd1e199aae4a3b14041d6d8513210a009569d468346b`.
It maps the general surviving late starred fricative class, not the particular
word and not pre-palatalization gamma. Earlier palatal and postnasal outcomes
have already received their separate representations. The surface inventory
is not broadened.

The complete selected391 final-output comparison has zero differences.
`ɣó` becomes `go`; `ɣí` and `gí` retain `ġi`, and `ángi` retains `enġ`.
`ággi` is parser-rejected and therefore is not a valid complete-word geminate
control. The separately preserved13 component controls and391 selected
comparisons remain the applicable class-conservation evidence.

The actual parser accepts epsilon with epsilon output; the full cascade rejects
it at physical110. The parser also accepts `ô` and the explicitly accented
`ḗô`; the latter reaches `ā*ô` and is rejected. These are independently replayed
actual-network paths/rejections, not a projection mistake.

Let D be the actual parser's upper language and C the complete relation.
Compiled regular-language differences establish:

| Difference | Result | Arcs |
|---|---|---|
| D minus original C.domain | nonempty, epsilon | 535522 |
| D minus mapped C.domain | nonempty, epsilon | 493364 |
| HGeneral minus mapped C.domain | nonempty, `ô` | 134247 |
| HMarked minus mapped C.domain | nonempty, `ḗô` | 130944 |
| HProsodic minus mapped C.domain | nonempty, `ḗô` | 51676 |
| HProsodic minus D | empty | 0 |

The exact domain definitions, ATT hashes and accepting/reachable-state
certificates are in the capsule. No unsupported native `test empty` result is
used. The first attempted snapshot remains FAILED, including that diagnostic
and its separate undefined-domain serialization mistake.

## Literature

The existing totality account and accepted palatalization/class distinctions
were retained. This candidate repairs a late representation omission; it does
not add a phonetic sound law, change its historical environment, or infer a date
from the executable tier. No new historical source claim is required for the
regular-language counterexamples. Campbell1959 §§71–72,87–89 supports the
separate stress-domain discussion, not a definition by cascade survival.

## Historical analysis

Stage/scope/chronology changes: none. Positive analogy evidence: none.
The mapping is conditioned on the surviving late starred velar-fricative class,
not grammatical membership. Its finite conservation and local success warrant
a separate bounded adoption proposal, not a theorem about all possible inputs.
Input orthography, normalized accent/quantity, nonempty word structure,
historical phonotactics and late output coverage require independent contracts.
Rejecting every unsuccessful string would be circular.

## Verdict

DEFER production adoption of the mapping and any parser restriction.
The mapping repairs a genuine general representation gap but does not prove
totality, even on the tested stress screens. No registry-verdict line applies
to this domain/representation investigation; no registry value is altered.
Full-cascade functionality still fails independently at SC086.

## Propagation (only after verdict)

None. No canonical FST, parser, baseline, corpus or reader mapping is changed.
There is no strict production certification for this private candidate.
Its zero391 final differences are a finite regression result, not totality
or functionality certification.

## Residue

Specify the intended historical input language independently of counterexamples,
including empty inputs, exceptional legacy input symbols, quantity and
unstressed sentence contexts. Then test regular-language inclusion again.
Preserve the SC086 ambiguity and gamma omission as distinct defects.
