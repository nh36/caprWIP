# Totality: separate post-SC052 assessment

## Declared relation and invariant

Let P be the actual adopted `EnglishProtoInput` relation:
the canonical native union with the canonical productive-cell extension,
as defined in `Germanic/fsts/germanic.txt`. Let D = domain(P), including
the explicit sentence-context convention where supplied. No new stress
priority, input whitelist or grammar restriction is substituted.
Fix the current Old English cascade and modeled variety. Functionality
requires at most one output per x in D; totality requires at least one.
Exactly one requires both. Corpus391 is not D.

The earlier parser proof establishes uniqueness of parsing, not well-formedness
of every historical lexeme represented by this computational grammar.
Neither a unique parse nor functional sound changes entails totality:
a later filter may reject a perfectly unique intermediate representation.

## Checked counterexample

`ɣó` is accepted by P as `*ɣ*ó`. Both original and repaired traces retain
the unpalatalized fricative before the back vowel. Before the final surface
filter it is `ɣo`; the surface filter rejects it. The capsule's
`verified-paths.json` independently checks parser acceptance and complete
fixed-input reachability rejection by the repaired full relation. The
110-step native trace is in `regression.json`. No search cutoff was used.

The immediate representation gap is explicit:
`pgrmInitSimple` admits ɣ and the starred inventory retains it;
`OEGFricativePalatal` handles front/j eligibility but does not palatalize
this back-vowel case. `OldEnglishOrthography` has mappings for palatal
fricatives/glides and other consonants, but no surviving starred-ɣ mapping.
Final star erasure leaves ɣ, which `OldEnglishSurfaceConsonant` excludes.
That is a computational mapping/domain mismatch, not proof that a
historical PGmc lexeme *ɣó existed.

## Alternatives and their limits

A general orthographic mapping of surviving velar-fricative ɣ to g is a
plausible representation correction given the existing class analysis
(Fulk2018 pp.130–132). It would need a separate assessment over all eligible
contexts and the actual final relation, not merely special treatment of
ɣó. It has **not** been implemented or certified here.

Conversely, historical input well-formedness could be narrower than the
computational grammar. It must be defined independently from comparative
segmental inventories, phonotactics, quantity/stress and selected stage
conventions. Excluding ɣó because it fails, or deriving that domain as the
current cascade's domain and calling it historical, would be circular.
Initial voiced-fricative articulation cannot simply be declared impossible
to rescue the theorem: the accepted source account expressly distinguishes
singleton g, including initial g, from gg/ng stops.

Repairing this missing mapping would not prove totality of D. The parser
and final surface acceptor have different segmental/syllabic constraints;
the earlier capsule's additional domain-loss evidence remains valid.
A future proof must compare the parser's upper language with the complete
cascade's upper language as regular acceptors and independently verify
emptiness of D minus domain(cascade). It must state any justified narrower
historical domain explicitly. No such global totality certificate is
claimed in this pass.

## Disposition

SC052 scoping and the residual contraction ambiguity concern single-valuedness.
The missing surviving-ɣ surface realization concerns domain coverage.
They remain separate controlled decisions. Preserve the certified production
and parser unchanged; report the exact current domain loss rather than
silently broadening the surface inventory or narrowing the parser.
