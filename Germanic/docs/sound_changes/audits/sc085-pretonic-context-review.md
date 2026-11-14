# PR10 review: preserve pretonic context through h-loss

## Identity

- **SC id:** SC076 and SC085; bounded implementation review, not a new
  historical adjudication.
- **Executable identifiers:** `OEPrefixIReduction`, `OEHLoss`.
- **Date / branch / base commit:** 14 November 2026,
  `candidate/maere-final-nasal-merger`,
  `77f314bf85035c23706b6b09b3a1855aa23c0620`.

## Question

- **Hypothesis:** deleting the positive pretonic annotation at SC076
  disables SC085's adopted protection. Retaining it until after h-loss
  should preserve pretonic h without changing intervening segmental rules.
- **Confirmation/refutation:** execute a cumulative control beginning
  before prefix reduction, inspect retention at h-loss and cleanup at
  the surface, and rerun toe, clay, fringe and the selected corpus.

## Current state (before any edits)

- **Historical characterization:** both rules retain their registered
  Old English, English-specific characterization and confidence A.
  Their existing verdicts and historical conditioning are unchanged.
- **Executable behavior:** SC076 lowered pretonic i and then erased
  `*ᶠ`; SC085's `FootCtx` consequently could not see that annotation.
  A directly annotated atomic h-loss test did not expose this lifecycle
  failure.
- **Selected-input assumptions:** no corpus input, target, context or
  protected baseline changes. The new control is explicitly stage-entry,
  not a newly admitted Proto-Germanic reconstruction.
- **Existing dossiers:** `sc085-adjudication.md` and
  `sc035-prosody-adjudication.md`, reached through the SC085/SC076 packets.

## Diagnosis

- **Census:** one fresh 394-row final-output comparison against the
  protected baseline, first verified byte-identical to the reviewed
  head's baseline. Zero changed rows; 394 accepted, 385 matches,
  nine mismatches, no rejection or ambiguity. No new historical380
  replay or whole-SC firing census is claimed.
- **Principal witness:** entered before SC076 as
  `*ᶠ*b*i*x*í*n*d*a*n`, the control becomes
  `*ᶠ*b*e*x*í*n*d*a*n`, remains so immediately before SC085,
  and leaves SC085 as `*b*e*x*í*n*d*a*n`. Its final output is
  `behindan`, without the annotation.
- **Intervening behavior:** the seven intervening definitions and their
  order are unchanged. At each intervening checkpoint, the annotated
  control agrees with its unannotated replay after erasing only `*ᶠ`.
- **Witness roles:** the pretonic control is a retention negative;
  toe and clay retain h-loss feeding contraction; fringe independently
  retains back/back loss with the complete -um sequence.

## Literature

- **Existing source basis:** Campbell1959 pp. 186–187,
  §§461,464–465, as documented in the existing SC085 dossier,
  supports singleton loss, geminate protection and pretonic retention.
  Hogg §§6.50–6.54 and Ringe–Taylor2014 pp. 334–335 remain the
  existing basis for the unchanged pretonic vowel rule.
- **Source/model distinction:** moving annotation cleanup is an
  implementation repair, not a new source claim, phonetic transcription
  of written h, or historical chronology. No new source acquisition or
  original-page recertification was undertaken in this bounded pass.

## Historical analysis

- **Stage/scope/conditioning:** retained independently of the executable
  identifiers. Protection uses positive prosodic information, not prefix
  membership or grammatical conditioning.
- **Counterexamples:** unprefixed toe/clay/fringe and singleton/geminate
  component controls still pass; both existing deliberate perturbations
  still fail their intended assertions.
- **Analogy:** none invoked.
- **Proxy:** the annotation now survives until its last consumer and is
  erased immediately afterward.
- **Chronology:** no edge changes. SC073–SC085 remains
  `technical_computational` / `boundary_observation`; the conditional
  interpretation of Corpus thoae and independent SC085-before-SC086
  evidence are untouched.

## Verdict

Retain the adopted historical accounts; repair annotation lifetime only.
These are the existing registry verdicts, not new adjudications:

Registry-verdict: SC085=REFORMULATE/RESTRICT; SC076=REFORMULATE

The smallest repair moves the existing erasure from SC076 to immediately
after SC085's guarded relation. No intermediate rule or stage is moved
or rewritten.

## Propagation (only after verdict)

- **Sources:** the two definitions, their reader-source blocks and
  cleanup explanations, and SC076's technical staging note.
  Current component expectations and exact-scope checks are aligned;
  archived observations and fixtures remain intact.
- **Separate operational finding:** `legacy_subset` now checks that
  each migration link preserves output cardinality before chain folding.
  The new `mare -> mare|mære -> mære` regression rejects the ambiguous
  intermediate; existing valid target/output chains remain accepted.
- **Focused checks actually run:** 35 static tests passed with
  409 subtests; two runtime/historical tests were deliberately deselected
  from that static selection. One canonical backend build produced
  114 fresh expected bins. The affected runtime files then passed
  all 24 tests using shared isolated definitions and that canonical
  build. The glossary fixture performed the single 394-row comparison.
- **Baseline effect:** none; output digest remains
  `3fd12209d595843df3f4f56e7d667293ba56611ffc7c96f2aec19eef7b06325a`.
  Authentic build/test receipts and traces are retained under
  `.capr-work/pr10-review-77f314bf/`; the pushed head and routine CI
  status are reported in the PR10 handoff.

## Residue

Per the explicit work order, stop after these focused checks. Generated
publication refresh, full strict serial/exclusive validation and book
rebuild are deferred to the later certification run; this pass does not
claim those gates. Flask and SC051 remain reserved for a later order.
