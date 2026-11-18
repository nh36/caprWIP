# SC059: rainbow and stressed-target domains

**Current scoped verdict:** RESTRICT, jointly adopted with SC046 by the
user's 17 November 2026 closeout instruction. The original three research
trials and their expectations are preserved unchanged. The earlier DEFER
below records the research decision before that explicit scoped adoption.

## Identity

- **SC id:** SC059, coordinated research comparison with SC046.
- **Executable identifier:** `OEBackMutation`; no stage is inferred from it.
- **Date / branch / base commit:** 2026-11-17;
  `research/rainbow-stress-domains`;
  `4bb89958b0b5392c0d9cca5d1ee8f73a86c61d38`.

## Question

Can the inherited `*régna-bùgô` hypothesis derive *reġnboga* with
second-root early lowering and ordinary unstressed-linker syncope when
both restoration and back mutation exclude unstressed targets?
Failure of a source-supported positive, loss of a stressed root, or an
unexplained corpus delta would refute a production-ready correction.

## Current state (before any edits)

The registry calls SC059 “OE Back Mutation”, stage “Old English”,
scope `english_specific`, confidence A, previously unadjudicated.
Production uses plain *e/æ* and acute *é*, with one intervening labial
or liquid. It does not positively restrict the plain vowels to stressed
targets. Its executable slot follows `OEJClusterCoalescence` and precedes
`OEWsPalatalUmlaut`; this is not itself a historical dating argument.

Row2148 selects `*régna-bùgô`, target *reġnboga*; row1963 independently
selects `*búgô`, target *boga*. Row2336 selects `*érθa-kùnðǭ`,
target *eorþcunde*. No lexical cell, corpus membership, frozen fingerprint
or production rule is changed here. The earlier SC046 DEFER and rainbow
SC017 adoption remain historical authorities for their respective trials.

## Diagnosis

Canonical `SC059 --evidence` rebuilt the manifest-validated stage bins,
confirmed production/sandbox equivalence on394 rows, and found exactly
five live firings: *heaven, milk, seven, spear, world*. All have stressed
*é* immediately before the operation and belong within the present proxy.
There is no live selected-corpus *æ* firing; a separate source-backed
staged control is therefore essential. The earlier SC046 census has
the identical FST/corpus hashes and its21 firings are not recertified
as a new SC046 execution.

The four comparisons reproduce:

| Intervention | Rainbow after SC046 | After SC059 | After SC114 | Endpoint |
|---|---|---|---|---|
| Current | `*régnabogô` | `*réʝnabogô` | `*réʝnbogô` | *reġnboga* |
| Restrict SC046 only | `*régnæbogô` | `*réʝneabogô` | `*réʝneabogô` | predicted `*reġneafoga` |
| Restrict SC059 only | `*régnabogô` | `*réʝnabogô` | `*réʝnbogô` | *reġnboga* |
| Restrict both | `*régnæbogô` | `*réʝnæbogô` | `*réʝnbogô` | *reġnboga* |

The second-root vowel is already *ò* at SC017, then *o* after its existing
decoder, in every run. Syncope places underlying *b* after *n* in the
joint run; positional realization leaves a stop. In the SC046-only run,
the retained diphthong leaves *b* postvocalic, giving *β* and later *f*.
There is no new postnasal hardening law.

Earthly retains its unstressed *æ* under the joint restriction and loses
it at SC114: `*éorθækùndǣ > *éorθkùndǣ > eorþcunde`.
The original current path retracts that linker to *a* before deleting it.
Neither path changes the endpoint.

Every selected row is retained in each comparison with its complete
output set. Only the SC046-only intervention changes any endpoint:
row2148, *reġnboga* to predicted `*reġneafoga`,386 to385 matches.
SC059-only, joint, and the annotation-only control remain386/394,
with the same eight mismatches, no rejections and no ambiguity.
The [source-bound records](rainbow-stress-evidence/README.md) include all
three trials and their actual compiler inputs, not just plans.

Witness roles: rainbow is the interaction/unstressed-target negative;
earthly is a convergent unstressed-linker negative; *boga* is the independent
early-lowering positive; the five live SC059 firings and staged *ealu*
are stressed positives. Constructed marked/unmarked compounds are
notation controls, not historical chronology witnesses or lexical admissions.

## Literature

Read the [source assessment](../literature_dossiers/rainbow-stress-domains/01-source-assessment.md)
and [holding record](../../../../docs/references/rainbow_stress_domains/README.md).
The prior SC046 source cards, rainbow ledger, SC059 book dossier and
chronology card were consulted; their old displacement experiments
are not rerun or promoted into new historical edges.

Orel2003 pp.61,300 supplies the bow noun and reconstructed whole compound
with *a*. Kroonen2013 pp.82,408 independently supplies the constituents,
not the complete accented compound. Ringe and Taylor2014 pp.27–29,
Hogg pp.54–55 §§3.10–11 and Colman2011 pp.95–98 support early stressed
root lowering; extending it to the subordinate compound root remains
an explicit inference under the working inherited analysis.

Purnell, Raimy and Salmons2019 e461–e463, especially the page-image-checked
e462, explicitly require a stressed target for restoration and back
mutation. Hogg pp.220–222 §§6.14–18 supports unstressed nonhigh syncope.
Hogg pp.156–157 §5.106 and n.6 supplies West Saxon *ealu* < `*ælu`,
with paradigm-supported mutation, as a stressed short-*æ* positive within
the liquid environment. Its declared entry is immediately before SC059,
not an invented full-cascade PGmc reconstruction. Both current and
restricted SC059 give `*ealu`. Mercian *heafuces/geabuli* are distinct
second-fronting histories. Purnell et al.'s dental *steaðul* lies outside
the executable labial/liquid proxy and is not mislabelled a West Saxon
positive for that proxy.

Čermák2005 pp.35–45 distinguishes obscuration mechanisms but does not
date rainbow. Crawford1922 p.107, Genesis9:13–16, the Helsinki transcription,
and Bosworth–Toller25654 establish English *renbogan/boga/renboga*
contexts, not a prehistoric linker or compound formation date.
The supplied DOCX is an unauthenticated memorandum with some superseded
implementation descriptions. Lockwood's original and the OEN summary
page remain unavailable; the indirectly supplied summary is not cited
as if either original had been read.

## Historical analysis

- **Stage/scope:** English back mutation has dialect-specific domains.
  The labial/liquid fragment is not a reconstruction of all Mercian
  second fronting or all back mutation. No new universal WS scope claim
  or chronology edge is warranted.
- **Conditioning:** stressed front target; the following back vowel's
  quality is a separate condition. For the inherited rainbow hypothesis,
  subordinate stressed *u* lowers before its own nonhigh ending, while
  the intervening unstressed linker is eligible for later syncope.
- **Counterexamples and falsification:** anchoring plain vowels to a
  word/foot's first nucleus is insufficient after SC044 decodes secondary
  `ǽ/à/è`. The first trial demonstrates this information collision.
  The next trial preserves those labels to SC059, but decoding there
  lets SC114 delete a restored subordinate *a*. The final trial carries
  them through syncope: the marked bake-root schema retains *a* there,
  and the marked heaven-root schema back-mutates; unmarked counterparts
  do not receive those privileges. Full cascades also show the surviving
  medial *a* later fronting to *e* under existing weak-vowel processing.
  These constructed endpoints are not attested words, but expose a
  remaining whole-cascade secondary-stress limitation rather than
  license an arbitrary historical deaccentuation.
- **Analogy:** no positive evidence requires replacement from *boga*.
  Later composition of already developed rain and bow is a different,
  equally viable formation history, not evidence for analogical repair.
- **Proxy versus history:** the joint restrictions provide the desired
  inherited vowel/linker derivation and pass the real lexical controls.
  The wider annotation lifecycle is not yet a complete model of all
  subordinate-stressed vowels. The review diff makes that limitation
  visible instead of hiding it in a successful rainbow endpoint.
- **Chronology:** no new registry edge. The working SC017-to-syncope
  dependency is conditional on inheritance; surviving English spelling
  does not independently establish a formation date.

## Original research verdict

**DEFER production promotion; retain the literature-supported joint
restriction as a reviewable research proposal.**

The registry verdict at that research checkpoint was SC059=DEFER.

The joint restrictions derive the requested inherited history without
changing any selected endpoint and preserve the source-backed stressed
controls. They do not prove that the compound was inherited rather than
formed later. The secondary-stress representation requires more than two
first-nucleus guards; the tested companion changes and their remaining
later weak-vowel limitation must be reviewed together. No production
change is silently made to settle that broader issue.

## Propagation (only after verdict)

The original documentary-only propagation was followed by the adoption
below; immutable workers, plans, observations and patch remain unchanged.

Update the rainbow model and ledger with both viable histories, source
limits and the conditional joint derivation. Link this follow-up from
SC046 and SC059, retain both older SC046 trial records and all new trials,
and provide an unapplied semantic-checked FST diff. Add inexpensive
evidence regressions; no routine compiler, shared-bin rebuild, widened
runtime fixture or corpus sweep is introduced. Refresh publication through
the canonical interface. Production/corpus/baseline effect: none.

## Residue

The compound's formation date and actual prehistoric linker remain
unobserved. Secondary-stress lifetime beyond the investigated rules,
including late weak-vowel fronting of the constructed bake-root control,
is not solved here. Existing SC046 geminate/restoration-history questions
remain deferred; this research is not an omnibus adjudication of them.
Lockwood's original and an authenticated later DOCX version remain
unavailable, explicitly not prerequisites invented to invalidate the
sources already in hand.

## Verdict

Registry-verdict: SC059=RESTRICT

Adopt the exact tested joint patch with SC046, including preservation of
secondary low/front labels through SC114 and the intervening consumers.
The literal primary/positive-foot targets and explicit secondary targets
now implement the stressed domain of the present labial/liquid proxy.
The current corpus and all frozen baselines remain unchanged. No general
Mercian implementation or new lexical admission is part of this decision.

The live cumulative route must show `*r*é*g*n*æ*b*o*g*ô` after restoration,
`*r*é*ʝ*n*æ*b*o*g*ô` after back mutation, and
`*r*é*ʝ*n*b*o*g*ô` after SC114, with selected endpoint *reġnboga*.
Early lowering at SC017, independent *boga*, earthly and the stressed
restoration/back-mutation positives remain controls. Staged West Saxon
`*ælu > *ealu` is the source-backed short-*æ* positive; the dental comparison
remains outside the current consonantal proxy.

The secondary bake-root schema retains restored *a* through SC114 but
later has *e* under existing weak-vowel processing. That wider-cascade
limitation remains explicitly acknowledged, not repaired or presented as
an attested lexical counterexample here. Neither this adoption nor the
shared English endpoint decides inherited formation versus later composition.

The refreshed corpus census has 19 SC046 firings rather than 21: rainbow
and earthly are the two excluded unstressed targets. SC059 still has the
same five stressed firings. Moving the decoder also moves thousand's
`*θ*ū*s*è*n*d > *θ*ū*s*e*n*d` from the SC044 composite to SC114:
the composite counts change from 51 to 50 and from 4 to 5 respectively.
That is annotation decoding, not new breaking or syncope of a vowel.
All 394 complete endpoint records, including acceptance, cardinality and
match status, equal the prior baseline exactly; the inherited eight
mismatches are buck, fowl, fire, rust, straw, tap, wolf and wool.

### Adoption regression execution and cost review

The existing production owner
`test_sc046_adjudication.py::test_current_production_restoration_positives_and_scoped_residue`
keeps the same eleven selected rows. It now batches seven rather than
three manifest-validated lookups to cover SC017, both target rules, SC114
and positional *b*. It prepares no definitions and invokes no compiler.
The existing strict all-corpus owner supplies the 394-row endpoint check.

`test_rainbow_stress_domains.py::test_staged_west_saxon_ae_and_stress_domain_live`
adds one finite-domain composition of current SC059 over four explicitly
staged inputs. It catches loss of stressed short-*æ* mutation, mutation of
an unstressed medial vowel, loss of a marked secondary target, or accidental
widening to the dental environment. Reusing the corpus owner cannot test
this positive: no selected row has *æ* immediately before SC059.
The test shares the verified isolated session definitions when their identity
matches; it performs no image preparation itself, full-cascade rebuild,
corpus sweep or concurrency change. It records the actual compiler input,
one network, one compiler call, setup/end-to-end wall and actual Linux
Foma-child peak RSS through the existing JUnit receipt workflow. Full-source
opt-in remains explicit through the existing fixture.

The historical proposal test also checks that the adopted definition bodies
are exactly those in the executed final trial. Earlier expected answers
remain independent frozen observations, not rewritten for the new production.
Measured adoption costs and final source-bound validation are recorded with
the landing commit; no timeout substitutes for the cost review.


## SC047/SC048 interaction qualification,18 November2026

The stress restriction above is retained unchanged. The new coordinated
SC047/048 assay finds that the literal parallel clauses accept an a-trigger
for e despite their written u-only environments. Delayed nasalization
therefore still gives steolan/weofan. A separately compiled strict-WS
composition removes those differences while preserving all394 outputs;
it is a reviewable, unadopted alternative, not a reopened rainbow decision.
The SC048/SC059 edges are consequently model-local rather than independently
dated West Saxon chronology. See sc048-adjudication.md and its source
assessment for Ringe--Taylor319--327/Hogg149--157 and the exact records.
