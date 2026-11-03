# Proto-Germanic parser: exact functionality and canonical input

## Identity

SC001 is a technical input-support stage, not a dated sound change. This
investigation starts at `ee73f189d2c4af2fab6170f7af066d96611ce749` on the isolated
`integration/parser-four-cells` worktree. It preserves the two previous repairs
and their failed native gates. No result here changes SC040, SC063, SC065 or
SC066, and parser certification does not certify the complete Old English
cascade.

The primary successful actual-production candidate experiment is
`parser-four-cells-certified-candidate-06`. Its snapshot, receipts, compiled ATT
relations, certificates, complete mappings and measured four-cell approval are
preserved with the other experiments in the accompanying evidence archive.
Production SOURCE adoption and final-source certification are subsequent,
separately recorded operations.

## Question

There are two distinct questions: whether the inherited parser actually
assigns different representations to the same spelling, and whether the
repaired productive parser's native failure denotes real nonfunctionality.
A finite corpus with one observed output cannot answer either global
question. A concrete two-output accepting-path witness refutes functionality;
a complete input-synchronized twin certificate establishes it over the
actual compiled relation.

## Current state (before any edits)

The inherited `EnglishProtoInput`, preserved as `EnglishProtoNative`, combines
optional inherited root constituents, prefixes and atomic diphthongs. The
second attempted productive repair makes the root nucleus compulsory and
restricts its continuation so that diphthong segmentation is no longer
ambiguous inside `PGCellRoot` or `PGCellPlain`. Its productive continuations
are cyclic: their accepted language is not a finite vocabulary.

The previous repair nevertheless gave native functionality/unambiguity results
of 0/1 for root, plain, complete productive input and its newly admitted
domain. The prefixed component gave 1/1. Neither a passing unambiguity test
nor production's previously selected vocabulary justified assuming
functionality. The separate SC040 formal-resolution precedent establishes
that equivalent alignment representations can matter to this native gate.

The historically approved selections remain
`fúnðanai → fundne`, `xámaraz → hamer`, `sáiwalǭ → sāwle` and
`wéstą → west`. They are not exceptions in the parser grammar. Their historical
research remains in the three soul dossiers and the preceding four-cell
integration record.

## Diagnosis

### A real inherited ambiguity

The inherited parser's shortest independent counterexample is `biu`.
The complete distinct lower-side outputs, as actual ATT symbols, are:

| Interpretation | Lower symbols | Zero-based ATT arc path |
|---|---|---|
| Prefix `bi` followed by a vowel-initial `u` root | `["*","b","*","i","*","u"]` | `5,582,613,631,669,2842` |
| Root onset `b` followed by atomic `iu` | `["*","b","*","i","u"]` | `5,582,613,632,4038` |

These are different linguistic segmentations, not duplicate accepting paths
for one representation. The paths belong to the archived native ATT with
SHA256 `0aec3dc3517b2137877db6b08f703738ad03e34307d00e56688b8a331ea2e461`;
the path verifier checks source/target continuity, identical upper strings,
acceptance and distinct lower sequences. Exhaustive fixed-word extraction
also agrees with actual native lookup on the diagnostic probes.

The written string alone does not encode whether `i` belongs to the prefix
or to the root diphthong. Existing primary-stress notation supplies that
information: `bíu` yields `*b*íu`, whereas `biú` yields `*b*i*ú`.
Inherited optional constituents also allow redundant computational paths and
vowelless forms. Those are different issues; no historical interpretation is
deduced merely from the number of such paths.

### The productive parser is mathematically functional

Direct global analysis of the actual compiled second-repair root, plain,
prefixed, input and newly admitted-domain relations establishes functionality.
The root and plain graphs have 384 and 425 live twins respectively; their
maximum residual delay is one lower symbol. These are exhaustive graph
certificates, not bounded word samples.

The overlap that remains in the unrestricted union of plain and prefixed
grammars is real: bare spellings can denote a root diphthong or a prefix plus
a vowel-initial root. It must not be resolved by a third plain-before-prefix
priority. The canonical convention below resolves this notation problem
explicitly and generally.

### Why the native tests disagree

The installed implementation is Foma commit
`82f9acdef234eae8b7619ccc3a386cc0d7df62bc`, version `0.10.0alpha`, in image
`sha256:91065f6b1fe4c180737956d44b5ce0158787d396cb9c1557a5f4d86023b12b13`.
The source and its Apache-2.0 licence are preserved with the diagnostic.

`fsm_isfunctional` tests identity of the output-side self-composition.
`fsm_isunambiguous` first replaces lower arc labels with per-exit path codes,
including output-epsilon exits, and then uses the same identity machinery.
They therefore present different alignments and discrepancy strings to
`fsm_isidentity`; the latter is not an independent mathematical test.

The pinned `fsm_isidentity` releases `newstring` after lending that allocation
to a state's discrepancy. A subsequent arc iteration can read or copy the
freed discrepancy. Isolated instrumentation records `aliases_current=1` at
the release. A diagnostic-only variant retaining borrowed allocations changes
the root, plain and delayed-identity failures to passes, while the genuinely
ambiguous inherited parser still fails. Instrumentation itself changes heap
layout and can change the native unambiguity result: these are
allocation/alignment-sensitive diagnostics, not dependable counterexamples.
The archive preserves original source, instrumented source, both builds,
commands and complete traces.

No installed runtime or production checker was patched. Retaining allocations
is a diagnostic lifetime experiment, not a proposed production memory-management
fix. Other suspicious epsilon bookkeeping is not represented as the proven
active cause.

### Independent global proof and its completeness

`functionality.py` reads the actual unweighted ATT relation, with state 0
initial, explicit final states and indivisible labels. It does not call any
Foma identity, functionality or unambiguity test.

1. Construct every reachable pair of transducer states. Match equal
   non-epsilon upper labels; allow each side's upper-epsilon arcs
   independently. This covers every pair of runs with the same upper string,
   including delayed or differently interleaved epsilon alignments.
2. Retain exactly those pairs with a common accepting continuation. A dead
   branch cannot witness ambiguity.
3. Propagate the two output strings after cancelling their longest common
   prefix. A live pair must have one residual delay, and an accepting pair
   must have empty delay. Check every live outgoing edge, including cycles.
4. If leading residual symbols disagree, or a live pair acquires a second
   delay, append its recorded accepting continuation. At least one of the
   two prefix paths is a genuine two-output witness; return and verify
   the original arc paths.

Necessity follows because a fixed common accepting continuation determines
one possible residual: two different residuals cannot both be cancelled by
the same two finite continuation outputs. Sufficiency follows inductively
from the edge equations and empty delays at all accepting pairs. The graph
has finitely many state pairs; each receives one delay or a counterexample.
No word-length or output-delay bound is assumed. Productive cycles are
checked by closure, not unrolled a fixed number of times.

The certificate contains the ATT hash and the delay for every live pair.
`verify()` reconstructs reachable/coaccessible pairs and checks complete
coverage, the initial delay, every edge equation and all accepting delays.
Its checks remain active under Python optimisation.

Unknown/identity symbolic arcs are rejected, not silently approximated.
The actual parser graphs contain none. All actual upper labels are single
Unicode codepoints, so the abstract upper-symbol language also represents
the native written input strings without a separate multicharacter-token
segmentation ambiguity. Lower labels are treated exactly as exported:
`*ai` is represented by successive `*`, `a`, `i` labels, not by an invented
single ATT label.

Controls include functional, many-to-one, genuinely nonfunctional,
epsilon-delayed, functional cyclic and nonfunctional epsilon-cycle relations,
actual diphthong-segmentation counterexamples, redundant same-output paths,
dead branches and multicharacter atomic labels. Additional tests reject
tampered certificate domains, delays and relation hashes.

For an independent replay from the repository root:

```sh
mkdir -p .capr-work/parser-proof-replay
tar -xzf Germanic/docs/sound_changes/audits/parser-formal-resolution/evidence.tar.gz \
    -C .capr-work/parser-proof-replay
python3 Germanic/docs/sound_changes/audits/parser-formal-resolution/functionality.py \
    .capr-work/parser-proof-replay/experiments/parser-four-cells-certified-candidate-06/results/EnglishProtoInput.att \
    .capr-work/parser-proof-replay/rechecked-EnglishProtoInput.json
```

The archive manifest supplies every member's SHA256, all experiment outcomes
and the archive SHA256. Repeat for `PGCellInput.att` or the archived equivalence
unions; the command verifies its newly produced certificate. It performs no
native Foma execution and needs no corpus sampling. Native experiments must
instead use their preserved snapshots/layouts inside the backend container,
with new experiment identifiers; never overwrite a failed or successful record.

## Literature

The historical premises are unchanged. The sources and page verification
remain in `soul-fulk-oblique`, `soul-syncope-resolution` and
`soul-lexical-reassessment`; the latter preserves the selected-cell evidence,
competing attestations and limits of the held Campbell pages. The original
four-cell stopping record and SC040 formal-resolution programme were consulted
before this focused investigation.

The new stress convention is a user-authorised canonical computational
notation, not a claimed discovery about historical stress or a sound change.
The global proof rests on the explicit finite-state argument above and the
actual pinned source, not a secondary-source assertion about software.

## Historical analysis

### Canonical convention and exact domain

The user explicitly selected “Require explicit stress for genuinely
ambiguous spellings (recommended)”. Use existing primary-stress marking to
distinguish both legitimate readings rather than choose an undocumented
default:

| Rejected ambiguous bare spelling | Explicit alternatives |
|---|---|
| `biu` | `bíu`, `biú` |
| `gailanai` | `gáilanai`, `gaílanai` |
| `biulanai` | `bíulanai`, `biúlanai` |

Let N be the inherited relation and P the unrestricted productive
plain/prefixed union. The canonical relation preserves every unique inherited
analysis and admits unique productive analyses only outside the inherited
domain:

```
unambiguous_part(N) ∪
unambiguous_part((domain(P) − domain(N)) ○ P)
```

Inherited-domain precedence is a documented, general compatibility policy,
not a word-specific or unprefixed-reading priority. For example, inherited
`gaiulō` uniquely means `*g*a*iu*l*ō`; a greedy longest-diphthong tokenizer
would silently replace it with `*g*ai*u*l*ō`. The canonical relation preserves
the old unique reading. Stress-marked alternatives make new readings explicit.
Ambiguous inherited inputs are rejected rather than recovered from a
preferred productive analysis. Existing inherited empty/vowelless acceptances
are conserved; this task does not claim to repair all lexical well-formedness.

The independent ambiguity-domain construction follows delay-augmented live
twins, collapsing irreversibly different leading outputs to a divergence
state. The returned graph is closed under every transition. This construction
need not terminate for every arbitrary transducer, but it does terminate
completely for these actual graphs: 2643 states for N and 970 for P.
An independent epsilon-closure DFA-product check verifies the exact Boolean
canonical-domain formula over 1219 reachable product states. Thus native
`_unambpart` is not merely assumed to mean output-uniqueness: its actual
accepted domain is checked against the independently derived domain.

### Equivalent native-compatible representation

The productive canonical relation only inserts literal stars and otherwise
preserves upper characters. Separate lexical tokenisation from morphological
acceptance:

```foma
define PGCellCanonical _unambpart(PGCellRaw);
define PGCellStrip [
    {*}:0 | pgrmInitSimple.u | pgrmShortVowel.u |
    pgrmLongVowel.u | pgrmNasalVowel.u
]*;
define PGCellInput [PGCellStrip.i .o. PGCellCanonical.l];
```

Star erasure is the inverse of this productive relation on its lower domain.
The factored relation is globally equivalent to `PGCellCanonical`: the union
is independently functional and the domains are exactly equal (191 reachable
DFA-product states). Neither an input restriction nor a changed output
interpretation is hidden in this representation.

The complete parser compiles the canonical union directly. Recomposition
through the equivalent factored helper re-exposes the pinned checker defect;
experiment `parser-four-cells-certified-candidate-04` preserves that failed
representation, its independent equivalence certificate and its native 0/1
result. Generic input-first subsequential alignment likewise remained
equivalent but failed the native gate and was not adopted. The successful
representation uses native-compatible equivalent alignments at each compiled
scope; it does not substitute a different test or waive a gate.

The actual production candidate in experiment 06 gives:

| Actual relation | Native functional | Native unambiguous | Independent global |
|---|---|---|---|
| `PGCellInput` | 1 | 1 | functional |
| `EnglishProtoInput` | 1 | 1 | functional |
| `OENonHighSyn` | 1 | separately unchanged gate | kernel equivalent |
| Complete `OldEnglish` | 0 | not certified here | unresolved |

The complete candidate parser is also independently equivalent to the
previously certified canonical relation: union functionality and exact
domain equality both pass. No installed C implementation was replaced.

### Mapping conservation and phonological comparison

The machine-readable canonical experiment compares internal outputs for all
799 frozen inputs: 391 selected, 380 historical and 28 research candidates.
Native accepts 786; the canonical parser accepts 798, retaining the one
previously rejected research candidate's rejection. Every native-accepted
internal mapping is conserved, and there are zero differences from frozen
Model K's input stage across all 799 inputs.

Additional path probes cover prefix/root readings, longer counterparts,
atomic diphthongs versus vowel sequences, repeated productive continuations
(including 24 repeated stem units), all four selections and previously
rejected malformed strings. The full actual-production assay independently
verifies native-analysis conservation, rejection of all six original malformed
controls, serial/composed equality, all frozen K outputs and exact positive
and negative syncope-component equality.

The measured candidate has 391 accepted records, 383 matches, the same eight
standing mismatches and no ambiguous outputs. Its approved selected-input
fingerprint is
`ed765acdd0ddd7417941234a65be386cb7e617967a22549cbee20ca9d5d288f6`;
the active historical-380 projection is
`4a5b126eae3dadf38f6ffd50b778009d79edae40407601a7c79de3d367688ed9`.
These are candidate measurements, not authority to hand-edit protected
baselines.

## Verdict

REFORMULATE the technical parser representation and canonical notation.
The inherited ambiguity is real; the second repaired productive relation is
globally functional. The contradictory native diagnostics arise from the
pinned identity implementation's discrepancy lifetime/alignment defect.
An equivalent canonical representation passes the unchanged actual native
gates and an independent global certificate. The formal stop is resolved;
the authorised four-cell adoption may proceed through the controlled SOURCE
and protected-baseline interfaces.

## Propagation (only after verdict)

SC001 owns the input-support improvement; SC036 owns retirement of
`OESoulProxy` while retaining `OELHWeakRaising`; newly registered SC114 owns
the bounded early nonhigh syncope phase. The preceding approval still owns
the four lexical selections. Each historical decision needs its own
memorandum, registry status and finalisation; none is silently attributed
to SC001 or to a mathematical parser theorem.

The first-stage evidence worker now compares the parser snapshot against
actual canonical evaluation inputs, rather than inventing a nonexistent
preceding transducer. It validates only the fresh target bin for stage zero;
all subsequent stages retain the existing two-bin comparison.

Experiment 05 passed the actual formal gate and scientific comparisons, but
its final canonical-tree guard detected a concurrent edit to `sc_evidence.py`
and correctly vetoed the receipt. Experiment 06 repeats the complete assay
with that tree held fixed and verifies protection unchanged. Infrastructure
failures, unavailable historical generated bytecode, the failed recomposition
and every earlier failed representation remain explicit in the archive.

Final production derivations, four-row approval/adoption, metadata and article
updates, strict serial/exclusive validation and rendered publication inspection
must be recorded after propagation. Earlier research receipts do not certify
that final state.

## Residue

The full composed `OldEnglish` network still fails native functionality.
This investigation has not established whether that separate failure is real,
another native false negative or both. Its independent follow-up must specify
the fully defined valid canonical input domain and prove both at-most-one
output and totality for the fixed historical cascade. Corpus agreement alone
cannot establish the intended exactly-one invariant.

The wider soul paradigm, unsyncopated competing attestations and historical
phonological limits remain in their preserved research dossiers. They are
not reasons to reject the supported four selected cells, nor are they
resolved by the parser proof.
