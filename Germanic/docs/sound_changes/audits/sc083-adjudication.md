# SC083 adjudication: protect the stressed head from weak-vowel deletion

## Identity

- SC083, `OEUnstressedEIContraction`, manifest position 98
  (stage 99 in the one-based compatibility tracer). Its position is
  unchanged within each selectable cascade.
- Base: integrated `update` at `113101ac5f169b589e1a9647cdf24d32cdd4d919`;
  work branch `integration/sc083-foot-domain`, 28 November 2026.
- This scoped case follows the SC047 adoption because both mature
  selectable cascades must be tested. The saved ordinary programme still
  points to SC050; no intervening work is closed or canonically reordered.

## Question

Can a pretonic vowel license deletion of a stressed head once earlier
rules have consumed the acute, and can the existing foot domain prevent
this without blocking genuine weak reductions? A change in the weak
positives, an unexplained difference elsewhere, or failure to protect
the independently motivated stressed domain would count against adoption.

## Current state (before any edits)

The registry had active, unadjudicated “OE Unstressed EI Contraction,”
historical scope `english_specific`, stage `oe`, confidence A. The
incumbent was:

```foma
define OEUnstressedEIContraction [
    {*e} -> 0 || EnglishStarVocalic [EnglishStarConsonant | EnglishPalatalConsonant]+ _ {*i}
];
```

The rule follows SC082 and acts on the executable plain `*e*i` sequence.
The selected PGmc weak forms supply the inherited suffix, not an
already reduced Old English vowel. Unscored developmental forms retain
the same independently motivated root accent in the submitted inputs.
Consulted ordinary SC083 preparation/evidence, the SC082 adjudication,
the existing SC083 chronology card and terminal-cluster book dossier,
and the read-only SC083 preparation and component A1 panel/receipt.
A1 identifies hypotheses and controls, not production authority.

## Diagnosis

In A/B2 prefixed present `gakáwiθi` and participle `gakáwid`, the
annotated first syllable survives while brightening consumes the
explicit root accent and the loss of intervocalic labial material
exposes root hiatus. The rule-local inputs are `*ᶠ*ʝ*e*k*e*i*θ` and
`*ᶠ*ʝ*e*k*e*i*d`. The incumbent deletes the root `*e`; the pretonic
`*e` supplies the positive left context. The candidate leaves both head
vowels intact. These are out-of-domain artifacts, independent of
whether later stages predict the attested long vowel. The compatibility
cascade and the simplex present reach different nuclei upstream and
are non-trigger controls, not evidence that the incumbent is safe
where the two vowels do surface.

Genuine weak application witnesses: ‘bore’ 1956, ‘handle’ 2055,
‘learn’ 2095, ‘lick’ 2099, ‘make’ 2117, ‘show’ 2186, ‘spare’ 2205,
and ‘sunder’ 2232. The ordinary baseline census fired on exactly
these eight of 396 selected rows, immediately after SC082. For
example, `*l*í*k*k*e*i*a*n` > `*l*í*k*k*i*a*n` is the live ‘lick’
anchor. The freshly compiled paired relations agreed on all
sixteen archived and active weak anchors in each order. The ‘world’
and ‘believe’ traces are whole-word
nonapplication controls. ‘Love’ supplies a stage-local reduction,
`*l*u*b*e*i*a*n` > `*l*u*b*i*a*n`; the full comparison has a
different upstream vowel and consonant representation, even though
it reaches *lofian*. This is not repaired here. A projected stage-local
infinitive for ‘lick’ likewise reduces; it is not the attested token.

## Literature

Ringe & Taylor (2014:32, 35, 228) describe weak formations and the
later raising of *-ej-* to /-ij-/ after weak shortening and unrounding,
then syncope to /-j-/ only before a heavy following syllable. Early
glosses and the ‘make’ forms support the vowel development; Campbell
(1959:§§754–755) supplies the weak paradigms. Sweet (1885:Ps. 71:9)
edits attested *liciað*; the reconstructed base and the local
infinitival test are distinct from that attestation.

Campbell (1959:§74 n. 5) supplies the distinction between stress on
prefixes and on roots, and §237.1b treats stressed contraction in
‘call’ after the loss of *w*. Ringe & Taylor (2014:260, 318) explain
the independent history of its long root vowel; Sweet (1885:416)
supplies the separate participial comparison. These sources motivate
a stressed-root retention test, not the exact encoded experiment
inputs or the candidate’s developmental endpoints.

## Historical analysis

The phenomenon is English-specific, in Old English weak-syllable
history. Its phonological conditioning is weak position before a
palatal; later syncope has narrower weight conditioning. The eligible
prosodic contrast is not a class of spellings, lexical membership or
analogy. There is no positive evidence for analogy here.

The existing representation telescopes the historical stages into
SC082 output `e.i` and SC083 deletion `e.i` > `i`. It is not a
literal law deleting syllabic *e* whenever followed by *i*. In
`OEStressFootContext`, a structured single pretonic syllable before
an explicitly accented head licenses insertion of `*ᶠ`.
`FootCtx` uses `SentenceCtx` to lift this marked pretonic syllable
outside the string on which the rule computes its environment; it
does not manufacture a new stress mark at SC083. In the unmarked
branch normal context remains. Sentence annotations and pretonic
material are preserved. Independently accented heads with later
weak sequences are not the same as a reduced stressed head.

The two unchanged reciprocal SC082/SC083 displacement records are
classified `independently_demonstrated` in the registry: ‘bore’,
‘handle’, ‘learn’, ‘lick’ and ‘make’ test executable feeding. They
are not an independent chronology of a real syllabic *i* stage.
The search toward SC087 is a no-break observation, not an edge.
No historical ordering constraint arises from the guard.

## Verdict

Registry-verdict: SC083=RESTRICT

Keep the historical characterization and position. Apply the
existing foot guard to the existing proxy:

```foma
define OEUnstressedEIContraction FootCtx([
    {*e} -> 0 || EnglishStarVocalic [EnglishStarConsonant | EnglishPalatalConsonant]+ _ {*i}
]);
```

The literature distinguishes the weak development from hiatus in
the stressed ‘call’ root; the deletion rule does not independently
encode that distinction once the acute is gone. The existing
annotation is sufficient to block the proven error without importing
an SC085 change or a new sound change.

## Propagation (only after verdict)

The Foma source, registry, reader chapter, cluster dossier and
chronology card record the change. The selectable-model refresh
records a new source-bound capture; immutable historical observations
remain separate. Owning tests reuse the capture for weak application
and prefixed-head retention; they compile no extra fixture. The book
uses the source-bound active traces and renders both official model
companions with the shared catalogue.

The prefixed present and the proposed ‘lick’ finite are research
controls, not new admissions. No target, selected input or citation
form changes for SC083. The assembled ‘learn’, ‘show’, ‘spare’ and
‘sunder’ dossiers explain the same weak histories and display the
same paths; the other four firing identities are corpus comparisons,
not new owning dossiers. No substantive lexical prose change is
needed. The separate SC047 rest and hue metadata
corrections are documented in the
[integration record](../../models/sc047/integration-record.md).

The before/after replay covered 2,370 paths: all 394 archived and
396 active inputs in each of compatibility, A and B2. There were
eight SC083 firings per panel per order, 48 in total, with identical
rule-local input/output pairs. There was no changed corpus stage,
endpoint or output cardinality, including the diagnostic model
overlays checked separately. Compatibility stayed at 386/394 and
388/396, A at 382/394 and 387/396, and B2 at 385/394 and 388/396
(archive and active respectively). This is a domain correction,
not an accuracy optimization.

The two unscored A/B2 prefixed controls are the exceptions to trace
parity. SC083 no longer deletes the root vowel, and the difference
persists through SC085’s existing marker cleanup, palatal fricative
merger and orthography to predicted *ġeceiþ* and *ġeceid* rather
than *ġeciþ* and *ġecid*. Each control still has one output.
Compatibility continues to predict *ġecēaiþ* and *ġecēaid*;
its root has a different stage-local nucleus and does not fire
in either revision.

## Residue

- The marker covers one structured pretonic syllable; it cannot protect
  a decoded head after two pretonic syllables. An already decoded
  secondary accent is likewise indistinguishable from plain `*e`.
  The synthetic tests document both limitations; neither is evidence
  for a novel historical rule.
- The developmental ‘call’ endpoints are not corpus targets and
  do not implement stressed contraction. Retain the unrelated
  full ‘love’ discrepancy and defer any general stress redesign.
- Do not replace the proxy with a new general *ej* law, move SC083,
  add a chronology edge, or refactor SC085 within this decision.
