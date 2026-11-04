# Complete Old English cascade: genuine branching and domain loss

Later post-acquisition work is recorded separately in
[`repair-README.md`](repair-README.md). It proves a private one-character
SC052 context-scoping correction, preserves the accepted production state,
and exposes a distinct downstream contraction counterexample. The original
diagnosis and evidence below remain the historical starting point.

## Identity

SC052, `OEVelarPalatalization`, plus the complete `OldEnglish` relation and final
`OldEnglishSurface` filter. Investigation: 4 November 2026,
`research/full-cascade-functionality`, isolated worktree based on
`c1cfd0a5b2c3dbdefa18da32d05bb229e02543c0`.
Certified scientific/publication SOURCE remains
`1b0698223d7d4c46999a18c03c1d30fd60cd54e9`.
No FST, corpus, scientific registry, baseline or publication projection is edited.

## Question

Does the actual adopted cascade assign exactly one output to every input
accepted by its canonical parser? A complete finite-state certificate can
establish functionality; two accepting paths with equal input and unequal
outputs refute it. One accepted parser input with no accepting complete-cascade
path refutes totality. Neither corpus agreement nor a failing native diagnostic
alone answers these questions.

Let `P` be the actual `EnglishProtoInput`, `D = dom(P)`, and `C` the actual
fixed-variety `OldEnglish` relation. The requested invariant is
`forall x in D: |C(x)| = 1`. Functionality means at most one; totality on `D`
means at least one. They fail separately below.

`D` is the adopted parser's formal language, not a newly invented whitelist of
historically attested words. It admits synthetic forms, including vowelless
pieces and inputs without written primary stress. The explicitly stressed
counterexamples below prevent conflating absence of a written accent with the
entire problem, but do not claim historical attestation or ideal phonotactics.
Any narrower intended historical domain must be independently specified and
proved, not retrofitted to discard inconvenient witnesses.

## Current state (before any edits)

The canonical parser is globally functional and its native gate passes.
The selected population remains the accepted 391 records, 383 matches and eight
established mismatches. This investigation neither re-adopts nor recertifies it.

The authoritative SC052 registry row says `preoe/english_specific`, confidence A,
`REFORMULATE/SPLIT`: class-distinct English velar articulation, with eventual
stop-reflex proxies and a distinct later fricative merger. The existing
`sc052-adjudication.md` retains broad eligibility, distinguishes singleton
fricatives from gg/ng stops, and discloses the disputed merger chronology.
Those scientific decisions remain unchanged.

The actual 110 physical composition stages come from `oe_pipeline.stages()`.
Physical stage numbers are executable positions, not historical dates.
The source snapshot SHA256 is
`18f69deaeb2385c94d65a9599f97a96aed9da2fd3065d908e194e9ab3e6cdb0f`.
`probe.py` exports each actual cumulative relation and the independently
compiled actual `OldEnglish`, not a substitute cascade.

## Diagnosis

### Global localisation

The unchanged accepted `parser-formal-resolution/functionality.py` constructs
input-synchronised twins with independent epsilon moves, trims to common
accepting continuations and checks consistent prefix-cancelled output delays.
All live edges and accepting delays are checked again by its certificate
verifier. The construction is complete for finite closed-alphabet unweighted
transducers: cycles are included, no word-length/output-delay cutoff is used,
and incompatible delays at one live twin yield a distinguishing completion.
Labels are indivisible symbols, not Unicode substrings. Unknown/identity
symbolic arcs are rejected, not sampled or approximated.

All first 61 actual cumulative networks satisfy these assumptions and have
globally verified functionality certificates. Stage 62, SC052, has a concrete
two-output witness. The last passing prefix has 202,932 reachable twins;
the first failing prefix has 236,688 reachable and 77,132 live twins.

Foma first says false at physical stage 2, `PGmcGmSimplification`.
That actual exported relation nevertheless has an independent complete passing
certificate. Thus its native result is a false negative here, established
independently rather than inferred from the earlier parser checker defect.
No new claim about the precise native implementation's internal failure path
is needed or made. The later stage-62 and full-cascade failures are genuine,
not cured by that earlier diagnostic disagreement.

| Relation/question | Result and extent |
|---|---|
| Actual canonical parser | Globally functional |
| Every actual cumulative prefix through stage 61 | Globally functional, independently certified |
| Stage-62 cumulative relation | Nonfunctional, verified accepting paths |
| SC052 stop component | Nonfunctional on a reachable exact input |
| Other individual unrestricted operations | Not globally certified by this investigation |
| Actual complete `OldEnglish` | Nonfunctional, two distinct final outputs |
| Totality of `OldEnglish` over `D` | Refuted independently |

Composition of functions is functional wherever defined. An interaction between
two genuinely functional applicable relations cannot create two outputs.
A functional cumulative prefix does not prove that its last operation is
functional on inputs outside that prefix's range.

### Principal witnesses and complete traces

| Canonical input | Parser output | Before stage 62 | After stage 62 | Actual final outputs |
|---|---|---|---|---|
| `ggai` | `*g*g*ai` | `*g*g*ē` | `*g*ʤ*ē` / `*ʤ*ʤ*ē` | `gġē` / `ġġē` |
| `g-géua` | `*g*g*éu*a` | `*g*g*ēo` | `*g*ʤ*ēo` / `*ʤ*ʤ*ēo` | `gġēo` / `ġġēo` |

The four-character first witness is a short practical formal counterexample,
not a claim of absolute shortestness or an attested lexeme. The second includes
explicit primary stress and a parser-accepted vowelless first compound piece.
Their role is live computational application, not chronology evidence.

The capsule's `counterexample-full-traces.json` records actual native outputs
at every one of the 110 cumulative stages. `verified-witnesses.json` supplies
zero-based ATT arc indices and final states for the parser and both complete
accepting paths for each input. `witnesses.py` independently replays paths and
asserts equal upper strings and genuinely unequal lower strings.
The actual full ATT is 33,475,255 bytes; these are accepting paths in that
network, not merely outputs inferred from a smaller component.

### Bounded component and clause isolation

The branch is localised to the middle parallel-replacement block in
`OEVelarPalatalizationStops`. Mechanically splitting the three existing
composition pieces does not change their definitions.
On the reachable exact input `*g*g*ē`, that block has seven arcs and both
outputs above. The surrounding fricative, k-front and final-j pieces are
identity on that exact input. Their restricted certificates are not global
proofs about the unrestricted components.

`clauses.py` makes one bounded diagnostic comparison: all five original
parallel clauses separately, the first four together, and all five together.
Clause 1 and the first-four block give only `*g*ʤ*ē`; clauses 2-5 individually
are identity. Adding the fifth, geminate-before-j clause to the parallel block
introduces the second output despite the witness lacking that j context.
The complete all-five restriction has the same ATT hash as the original
middle component:
`b73724eaae25749b91e7255d47cdd0ba68fcc9ed3615b7e54e93e0854aa124eb`.
This localises a compiled mixed-length parallel-replacement interaction;
it is not a general proof of the compiler mechanism or a licence to choose
one of the outputs as the historical account.

### Totality, independently

`ɣó` is accepted by the actual parser as `*ɣ*ó`. It retains an output through
physical stage 109, `OldEnglishRemoveStars`, whose output is `*ɣo`.
The final `OldEnglishSurface` filter rejects it. A native exact regular-language
difference on the explicitly accented parser domain also finds `ɣó`.
Independently, complete fixed-input reachability in the actual full ATT explores
four configurations and finds no accepting path. It has no search cutoff.

The simpler parser-accepted `b -> *b` is likewise rejected by the full relation.
It is a deliberately degenerate unstressed-domain witness, not a reconstruction.
Both parser accepting paths and complete rejection receipts are preserved.

For rejection, states are `(network state, consumed input position)`; arbitrary
epsilon-output cycles do not affect existence of an accepting path and are
fully covered by finite reachability. When verifying a specified output, its
consumed position is also tracked. This witness adapter explicitly rejects
multicharacter labels: the actual full ATT's non-epsilon upper/lower labels
were checked to be single codepoints. The global proof itself does not have
that limitation and treats arbitrary explicit labels atomically.

## Literature

Existing sources are consulted through the accepted SC052 memo, not newly
represented as whole-source direct readings: Fulk2018 pp.130-132,
Ringe-Taylor2014 pp.203-214, especially p.204, Hogg1979 pp.102-111, and
Laker2007 pp.166-168, 175-184. The memo supports class distinctions and records
the merger controversy. This formal diagnosis makes no new historical claim,
changes no conditioning, and does not infer a chronology from FST identifiers
or from the interaction assay.

## Historical analysis

Historical stage and geographical/genealogical scope remain the cited SC052
registry characterization, not deductions from stage 62. Regular phonological
conditioning remains unchanged. The witnesses falsify mathematical uniqueness
or totality on `D`, not any attested historical etymology. No analogy is invoked
or evidenced. The exact relationship between the competing compiled stop
outputs and the independently intended singleton/geminate account needs a
controlled decision; final spelling alone cannot select it.
No new chronology edge, whether stage-entailed or independently demonstrated,
is proposed.

## Verdict

Computational verdict: NONFUNCTIONAL and NONTOTAL over the declared parser
domain. RETAIN certified production unchanged pending a specific correction
decision; this is not a generic DEFER or a reversal of SC052's scientific verdict.

Registry-verdict: SC052=REFORMULATE/SPLIT

That line restates the existing registry decision; it does not authorise a new
propagation. A representation-equivalent refactor cannot remove two genuinely
different outputs. Any correction must establish the intended class/context
semantics, account for the mixed-length parallel block, and state the exact
changed relation before adoption. Likewise, the residual `*ɣo` totality failure
requires an explicit domain/representation or orthographic decision, not an
ad hoc exclusion of this input.

## Propagation (only after verdict)

None. Only research evidence/scripts, focused verifier tests and this report
are added. No complete firing census or counterfactual corpus replay was
repeated: no sound law, order, selected grammatical cell or output was edited.
The 391/383/eight result remains the prior certified production result, not a
fresh finite-regression or current-tip strict certificate.

Protected/source fingerprints remain unchanged. The selected corpus SHA256 is
`acecb163dffba5c20109ca4951074056a697854fa69cf1f52bc0f82142b39d62`.
SC114, SC036, SC040, SC063, SC065, SC066, the original-380 archive, all approvals
and inspected publication remain untouched.

## Residue

The next controlled decision is narrowly specified: determine and source-check
the intended singleton/geminate outputs for the reachable SC052 contexts, then
independently certify a bounded replacement-block correction and its complete
downstream effects before production propagation. Separately decide how the
already accepted starred fricative representation should survive orthography/
surface filtering, or justify a general canonical-domain distinction.
These decisions cannot be replaced by output preference, corpus fitting,
lexical IDs or silent grammar restrictions.

The present counterexamples refute the requested invariant on `D`. They do not
prove that every other component is sound, characterise all ambiguous/rejected
inputs, or decide the invariant on an independently narrowed historical domain.
The accepted four-cell integration is not reopened.

## Reproduction and preservation

`evidence.tar.gz` and `evidence-manifest.json` preserve all first-62 ATT exports
and proofs, the actual full ATT, every native prefix receipt, restrictions,
clause isolation, all-stage traces, witness paths, operational logs and exact
scripts/proof snapshot. Every embedded member was checked against its SHA256.
All 110 raw exports and compiled bins remain in the ignored private research
directory; the capsule records their hashes even where they are not embedded.

After extracting the capsule, verify or recompute using the unchanged accepted
proof and the tracked scripts:

```sh
python3 Germanic/docs/sound_changes/audits/full-cascade-functionality/probe.py \
  --analyze /path/to/extracted/networks
python3 Germanic/docs/sound_changes/audits/full-cascade-functionality/witnesses.py \
  /path/to/extracted/networks
```

For fresh native exports, run `probe.py --worker /tmp/NEW_UNUSED_DIRECTORY`
inside the backend container with this worktree's adopted mounts; never use
host Foma. It derives order from `oe_pipeline.stages()` and includes `-e quit`.
`clauses.py` runs in the same container against that export directory.
The preserved follow-up worker/receipts reproduce component and explicit-stress
restrictions. No incomplete traversal is represented as a global proof.

Execution environment: pinned backend Foma `0.10.0alpha`. The focused parser
proof-loader and witness-verifier run passed 24 tests in portable mode; that is
not a strict production/publication certificate. Native exports, complete
prefix certificates and full-network witness verification are separate formal
evidence, not consequences of that finite test run.
