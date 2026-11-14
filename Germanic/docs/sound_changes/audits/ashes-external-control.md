# Ashes as an external control for the flask root-vowel hypothesis

## Identity

- **SC id:** SC043/SC108/SC046/SC051, bounded external-control research;
  no whole-rule adjudication or registry verdict.
- **Executable identifiers:** `EAFBrightening`,
  `EAFBrighteningLongFinal`, `OEARestoration`,
  `OESkPalatalization`; identifiers are not historical dates.
- **Date / branch / base commit:** 14 November 2026,
  `research/flask-inherited-paradigm`,
  `5df7b9daef1a4da88abba30f0c9681c8e91d9a36`.
  This branch does not include the separate PR10 pretonic-marker repair.

## Question

- **Hypothesis:** an independent weak feminine with the same relevant
  phonological ending can distinguish regular root-a retention/retraction
  before sk from levelling of the nominative after back-root obliques.
- **Confirmation / refutation:** back-root asce alone fits both. A secure
  front-root nominative in the identical conditioning environment would
  require an explanation beyond categorical retention. A dated/dialectally
  controlled distribution could independently favour a phonological
  condition. Case-ambiguous glosses cannot substitute for such a distribution.
- **Predictions recorded before execution:** the experiment's frozen
  `PREDICTIONS` distinguishes the published Wright formulation, the narrow
  sk-plus-final-ā experiment, and the levelling account. The three
  computations keep production palatalization and its timing identical.

## Current state (before any edits)

- **Historical characterization:** the registry leaves SC046 and SC051
  unadjudicated, Old English, English-specific. No new historical stage,
  scope, chronology edge or rule is proposed for adoption here.
- **Executable behavior:** the candidate's early final nasal bimoric merger
  removes the nasal-ending restoration trigger. The existing experiments
  either protect stressed a before `*skā#` during brightening or retract
  fronted æ in that environment before final ā-fronting.
- **Selected-input assumptions:** flask stays `*fláskōn`, comparator flasce.
  Ashes is not admitted to the corpus. EWA, s.v. aska², supplies the
  reconstructed n-stem `*askōn-`, not a complete nominative. The probe
  `*áskōn` is CAPR's parallel weak-feminine citation encoding, not an EWA
  quotation of a full case form.
- **Shared ending:** on that weak-feminine analysis, ashes and flask have
  the same relevant later nominative `*-ā`. Ringe and Taylor2014 p192
  explicitly give flaskā > flæskǣ; applying the class analysis to ashes
  reconstructs askā, rather than importing a different ending to obtain
  the desired root. This is a class-based reconstruction, not a preserved
  ashes token. Ringe2017 p312 does not supply a certain feminine nominative:
  the paradigm prints question marks there.
- **Existing records consulted:** the flask source ledger and inherited
  paradigm audit, the SC051 medial-context research and its exact retention/
  retraction definitions, the current registry/control plane and protocol.

## Diagnosis

- **Firing census:** not applicable to a production adoption: only two
  external nominative probes and three root treatments are authorized.
  No new 394-row census, full strict run or book rebuild is claimed.
  Production and the selected corpus remain untouched.
- **Principal witness traces:** measured results are preserved beside the
  reproducible driver under `ashes-external-control-evidence/`.
  Every named relation is compiled from the pinned source in the existing
  backend, then applied serially. These are component-cascade executions,
  not fresh whole-root variant compiles. Canonical runtime bins from a
  different branch are not treated as this source's bins.
- **Normal entry versus diagnostics:** all six raw noun/variant runs
  are accepted after the same `normalize_proto` conversion as ordinary
  corpus input: reconstructed `*áskōn` is passed as `áskōn`, and
  `*fláskōn` as `fláskōn`. All six match separately labelled entry
  immediately after `EnglishProtoInput`; none requires that bypass.
  Every intermediate in each normal run is a singleton.
- **Witness roles:** ashes = independent lexical conditioning control;
  flask = comparator of the root intervention. The written x/cx/cs
  witnesses constrain consonantal explanations independently; they are
  not a new order-sensitivity experiment.

### Decisive measured traces

The shared ending path is `*áskōn → *áskǭ → *áskā`, with the same
changes after fl- in flask. Token separators are suppressed below;
these are internal model forms, not independently dated attestations.
Final-vowel fronting is the retained technical helper SC108, not a
new historical long-vowel claim.

| Noun / treatment | After early ending merger | After root fronting/retention | After optional retraction | After final-vowel fronting and unchanged restoration | After SC051 | Surface |
|---|---|---|---|---|---|---|
| ashes / baseline | *áskā | *æskā | — | *æskǣ | *æʃǣ | æsċe |
| ashes / retain | *áskā | *askā | — | *askǣ | *aʃǣ | asċe |
| ashes / retract | *áskā | *æskā | *askā | *askǣ | *aʃǣ | asċe |
| flask / baseline | *fláskā | *flæskā | — | *flæskǣ | *flæʃǣ | flæsċe |
| flask / retain | *fláskā | *flaskā | — | *flaskǣ | *flaʃǣ | flasċe |
| flask / retract | *fláskā | *flæskā | *flaskā | *flaskǣ | *flaʃǣ | flasċe |

Retraction and retention converge before final-vowel fronting. All
three treatments leave the late following-front-vowel clause in place,
so even root-a outputs retain a palatal model consonant. They are
root-vowel fits, not derivations of written acxe/axan. No displacement
or high-front-vowel restriction has silently entered this comparison.

Successful execution was at 13:32:13-13:32:15 UTC on14 November2026:
snapshot `ashes-root-only-5df7b9da-v3`, source SHA256
`21f86e76dd3d7f3f76633fabd679d3fab2d40548a5b8dc84596c6760d11b52d6`.
The 115 isolated relations were compiled once at13:24:36-13:29:46.
The successful run records every binary checksum and reuses that
unchanged build. Its pinned driver, payload and source are in the sealed
snapshot; the committed `observed.json` retains changed stages, named
checkpoints and the final rather than duplicating every identity stage.

Two preliminary harness records remain archived, not historical
rejections: the first misclassified an empty rejection list; the second
passed the scholarly reconstruction asterisk literally to the tokenizer.
The corrected run uses the shared normalizer and accepts both nouns
normally. Neither preliminary record is evidence against an inherited
form. The normalizer correction did not require a second Foma build.

## Literature

- **Existing dossiers checked:** the flask source ledger, SC051 research
  audit and first inherited-paradigm research.
- **Original sources inspected:** Wright and Wright1908 pp37-38, §57;
  Wright1857 I pp62,66,284 and appendix opening; Wright1873 II pp1,16;
  Wright-Wülcker1884 I col294, especially note8; Cockayne1864 I
  pp334-335,340,370-371 and preface pp lxxv-lxxvii,lxxxiv.
  BT Supplement p48, asce, supplies the leads, not independent token
  verification. EWA s.v. aska² supplies the stem/class comparison.
  Campbell1959 p61 §158 and Luick1914 pp152-153 §161 retain their
  previously verified flask/oblique levelling account; they are not
  newly independent attestations.
- **Published conditioning:** Wright and Wright §57 treats retention
  before an originally back vowel in the next syllable: in open
  syllables, and in closed syllables before doubled consonants except
  hh, and before sc/st. This is broader than CAPR's trial `*skā#`;
  it does not single out a weak noun as the condition.
  Crucially, p38 itself admits “æsce, ash, cinders” beside a.
  It would be a misquotation to say their actual discussion excludes
  every æ-form categorically.
- **A consequential textual correction:** the Supplement's Æsce,
  Wrt.Voc.I66,43, is not a clean diplomatic æsce token in the cited
  original edition. Wright1857 prints `Finis, ærce` in the fire vocabulary.
  Wright-Wülcker1884 col294 retains that reading and note8 proposes:
  “An error for cinis, æsce, I suppose.” The gloss's fire context makes
  the correction plausible; its status remains an editorial correction,
  not a contextual front-root nominative. The front vowel is visible even
  in ærce, but identifying the word and its sc involves the correction.
- **Case-critical result:** `seó acxe` is the strongest back-root
  nominative singular inspected. The strongest front-root nominative
  lead is the corrected glossary form, weaker than that contextual
  nominative. Independently, `on hátre æscan` supplies an unambiguous
  front-root dative singular. This is not a clean front-nominative /
  exclusively-back-oblique distribution.
- **Source versus modelling:** ashes here always means burnt residue.
  Latin cinis, the fire-vocabulary context and the burnt horn/head/fox
  recipes exclude ash-tree æsc. Neither ordinary sc nor the experimental
  rendering ċ supplies an independent phonetic date.

### Attestations and coverage

The [token table](ashes-external-control-evidence/attestations.tsv)
distinguishes all eight inspected readings, including the conjecture
and apparatus variants. The [facsimile register](ashes-external-control-evidence/sources.tsv)
pins download URLs, exact sheets and PDF hashes. The editions, not manuscript images, were
collated. The old editions' century assignments are explicitly reported
as editorial datings; no new palaeographic or dialect attribution is
claimed. In particular, Cockayne's base is V, Cotton Vitellius C.iii:
preface p lxxv gives approximately1050 and his wider1000-1066 estimate.
His supplied headings marked `[MS.O.]` must not turn these passages
into an alleged wholesale switch to an O-recension.
H and B are Harley585 and Hatton76 (preface p lxxxiv).

The first-volume asce and second-volume acse glosses both come from
Cotton Cleopatra A.iii, although different collections are printed.
They must not be counted as two independent manuscripts. The front
gloss belongs to the Brussels vocabulary; Wright1857 p62 identifies
the Royal Library but does not establish a shelfmark here.
The 1884 second volume is an index, not the original1873 second
volume cited by BT.

This short pass follows the requested dictionary leads and inspects
the three most useful medical contexts. It does not claim a complete
DOE-corpus search or that no other contextual front-root nominative
exists. Uninspected Phoenix/Orosius/Guthlac/Gospel leads are not promoted
to newly verified tokens. BL's legacy manuscript link redirected to
a general digitisation page; the attempted Bodleian catalogue page
presented a bot-access challenge. Neither yielded a new manuscript date.

## Historical analysis

- **Stage and scope:** no new assignment; root fronting/restoration
  and the written OE outcomes are kept distinct. The editions' dates
  do not date the underlying change.
- **Regular conditioning:** the experimental condition is stressed
  a followed by sk and final long ā. It is phonological, not “weak
  feminine” as a grammatical trigger. The shared class only motivates
  the independently specified input ending.
- **Counterexamples:** the proposed æsce nominative is too textually
  qualified to be a decisive secure-token refutation in this pass.
  The genuine front oblique æscan prevents any claim that all back
  inflected forms are the only surviving paradigm. A complete account
  still owes an explanation of the two root grades.
- **Analogy:** back-root acxan/axan supplies actual possible donors for
  back-root nominative acxe; it does not demonstrate a levelling event
  or its direction. Conversely, front æscan cannot simply be hidden
  as noise. No lexical diffusion or grammatical sound-law condition is
  introduced to reconcile them.
- **Proxy versus historical account:** protecting/retracting a in the
  narrowly specified nominative environment is only a tested model.
  Wright's broader formulation also concerns st and geminates. Its
  scope cannot be inferred from this two-noun trial.
- **Chronology evidence:** none newly established. Plain sc is
  compatible with distinct realizations; cs/cx/x gives additional
  written hard/metathesized-cluster evidence but does not choose
  whether metathesis preceded palatalization or followed later
  redistribution. Palatalization timing is deliberately not varied.

## Verdict

- **Disposition:** DEFER production adoption; retain both independent
  root histories for comparison and keep the selected flask comparator.
- **Machine-readable line:** n/a, bounded external-control research,
  not a whole-SC registry adjudication.
- **What this decides:** the cited front nominative cannot be deployed
  as an unqualified diplomatic counterexample. Back-root nominative
  acxe and possible back-root donors fit both retention and levelling.
  The ashes evidence therefore does not independently select levelling
  or establish the exact narrow law. Where the two nominative accounts
  tie on these witnesses, CAPR's priority gives the regular account
  provisional explanatory preference, not the status of an adopted law.
  That preference does not settle the full paradigm's economy, the
  two-root distribution, or the consonant timing. Flask can retain a
  regular root-vowel working hypothesis without pretending that its
  full production derivation is solved.

## Propagation

- **Affected files:** this research audit, attestation/evidence tables
  and a focused reproducible driver only. No reader, registry,
  production-rule, selected-vocabulary or baseline change.
- **Checks:** focused probes only; the precise run and trace record
  accompany the driver. Publication regeneration and full strict
  certification are deliberately outside this work order.
- **Baseline effect:** none authorized. No new whole-corpus execution
  is claimed.

## Residue

A secure, syntactically nominative æsce in a securely identified
manuscript/dialect, or a dated distribution following an independently
defined phonological context, would materially distinguish the accounts.
The current correction and mixed-root obliques do not supply that
distribution. Neither does a two-noun output fit establish the narrow
skā condition, distinguish retention from retraction, or justify an
ashes/Flask-specific exception. A complete regular paradigm analysis
remains separate from the present nominative control.

## Paragraph suitable for the book

The weak feminine *asce* ‘ashes, cinders’ supplies a useful but
inconclusive comparison with *flasce* ‘flask’. The contextual nominative
*seó acxe* occurs beside back-root inflected *acxan*, but the medical
texts also preserve front-root *æscan* after *on hátre* (Cockayne1864,
I, pp334,340,370). The glossary form *æsce* cited by the dictionary
requires qualification: the cited edition prints *ærce*, for which
Wülcker proposes *æsce* (Wright1857, I, p66; Wright-Wülcker1884,
I, col294 n8). Back-root nominatives are compatible both with regular
retention and with levelling from inflected forms, while the inspected
evidence does not establish a conditioning-based distribution between
the two roots; Wright and Wright themselves admit *æsce* beside *asce*
(1908, pp37-38, §57). Regular retention accordingly retains explanatory
priority where the accounts tie, without yet establishing a categorical
rule or the relative chronology of the consonantal developments.
