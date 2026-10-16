# SC015: consonant-conditioned lowering, its counterevidence, and its computational consequences

Adoption notice, 16 October 2026: the later explicit scientific decision
adopts unified Candidate B and three independently attested *leorn-* targets.
See [the canonical adjudication](../sc015-adjudication.md).
The research-only recommendations and measurements below retain their
original historical scope; no experimental receipt has been revised.

## Identity

SC015, executable identifier `PNWGmcILowering`. Research base:
`1cf14edcdc87a0bc29046c7465a703e1b1c9d2ca`, branch `update`.
This is an experimental investigation, not a canonical adjudication or an
authorization to adopt a rule, reconstruction, paradigm cell, chronology edge,
or baseline. It deliberately supplies no `Registry-verdict:` assignment.
The nine sections follow the adjudication template; the adoption and propagation
steps remain gated by the user's explicit research-only instruction.

The recommendation is to reformulate the historical account and pursue
component-specific consonantal conditioning, while retaining the incumbent
executable temporarily. The existing rule is not vindicated by its output
score. Conversely, the checked evidence does not yet justify substituting one
unqualified pan-Germanic `i > e / _ {z,st,r}` law. Two material counterarguments
and the exact selected-cell consequences must remain visible.

Companion evidence:

- `experiments.json.gz`: complete 387-row baseline, seven recipes, all changed
  checkpoints/finals, 192 component inputs, outputs, source citations and
  protected-artifact hashes.
- `chronology.json`: independent short-vowel lengthening and extended-domain
  supplement, including the inherited-*irha-* counterexample.
- `experiment.py` and `chronology.py`: exact private drivers. They use the
  repository's existing isolated runner and derived cascade, not a second
  hand-maintained production cascade.
- `provenance.json`: source, driver, receipt and reference hashes, plus the
  independent protection results.

Reproduction requires the pinned source/corpus and the backend container.
The primary driver writes an incremental argument-path checkpoint but emits
its complete final receipt, including the protection comparison, on stdout;
`experiments.json.gz` preserves that final stdout, not an incomplete checkpoint.
The supplement consumes the primary receipt after decompression. These are
private research drivers, not new canonical generation entry points.

## Question

Three falsifiable hypotheses were compared.

| Hypothesis | Claimed primary conditioner | Principal discriminators |
| --- | --- | --- |
| Traditional | A following non-high vowel, with independently justified consonantal restrictions | Non-high-vowel participles/adverbs without lowering; final monosyllables without a following vowel |
| Hill | Immediately following consonants, particularly tautosyllabic *z*, *st*, and *r* | *iz, hiz, hir*; *st* versus *sk*; class-I participles; later mutation of lowered derivatives |
| Hybrid | A narrower common development, with separately evidenced later processes and paradigm histories | The precise date/domain of each consonantal component; demonstrable lost triggers or analogical models, not rescue by assertion |

Positive outcomes alone cannot choose between these. *Nest*, *meed* and *wer*
satisfy both following-vowel and consonantal descriptions. Conversely, *fiskaz*
and *wiskō* distinguish Hill from indiscriminate vowel-conditioned lowering,
but do not distinguish Hill from CAPR's already coronal-restricted version.
Final *iz/hiz/hir*, dental participles and the uninflected *nidana* evidence do
more discriminating work [@Hill2017, pp. 150--158].

A shared Proto-Germanic or Northwest Germanic development is a serious
unifying hypothesis here. Independent daughter changes, lexical diffusion,
grammatical sound laws and unrestricted appeals to analogy are not adopted
to evade counterexamples. Particular published analogical proposals are
reported below with their evidence and objections.

## Current state (before any edits)

### Canonical characterization and actual matcher

The registry describes SC015 as an active historical sound change,
`pnwgmc / pan_pnwgmc`, confidence `A`, unadjudicated. This is a recorded
current characterization, not a conclusion of this investigation.
The existing reader instead calls it “Leveling of early unstressed front
vowels”; both routed dossiers build an unstressed-vowel rationale around it.
That account describes the wrong phenomenon. The matcher targets the first
vowel, not an unstressed medial vowel.

The operative definition is:

```foma
define PNWGmcILowering Ctx([
    [
    {*i} -> {*e} || .#. EnglishStarNonVelarConsonant* _ EnglishStarCoronal+ EnglishStarNonHighVowel,
    {*í} -> {*é} || .#. EnglishStarNonVelarConsonant* _ EnglishStarCoronal+ EnglishStarNonHighVowel
]
]);
```

The derived full wrapper has 107 physical stages including
`EnglishProtoInput`; SC015 is stage 19 on that explicitly stated counting
basis. This coordinate is not a historical date. In particular, dental
hardening and j-gemination already precede it, whereas final *z*-loss,
rhotacism, SC036, breaking and i-mutation follow it.

### Independent condition audit

| Condition | Actual implementation | Scientific assessment |
| --- | --- | --- |
| Stressed first-syllable short *i* | Both unmarked `i` and acute `í`; a consonant-only left context excludes earlier vowels | First-syllable approximation, not a general stress detector. Acute is root notation, not sentence stress. Long *ī* is excluded. Prefixes and noninitial stressed roots are not covered by this matcher. |
| Following non-high vowel | Required immediately after the coronal sequence | Supported by the traditional formulation, but not required by Hill's final-monosyllable evidence. This is a substantive hypothesis, not neutral infrastructure. |
| Permitted interveners | Exactly `d,l,r,s,t,z,ð,θ`, one or more | Not the same as Hill's *z/st/r* domain. It admits *t*, *d*, *ð* and *θr* without independent lexical evidence for every such environment. |
| Intervening velars/labials | Excluded anywhere in the right-context cluster | Preserves fish/wisp/lid classes, but the source comments overstate the support for this exact generalized blocking rule. |
| Nasals | Any nasal anywhere in that intervening cluster prevents matching | Broader than a statement about a following tautosyllabic nasal plus consonant. It blocks *zn* in learn even though the immediate conditioner is *z*. |
| Preceding velars | Any velar anywhere between word start and *i* prevents matching | Not merely immediately preceding *k/g*. The comment explicitly extrapolates a North Germanic restriction to protect OE *hlid*. That extrapolation is not independently established. |

The compiled coronal inventory was enumerated, not inferred from its name.
The non-high inventory recognizes `a,ā,ą,e,ē,ḗ,o,ō,ǭ,ô,à,è,ò`; high
`i,u,ī,ū` are excluded. Nasal *ǭ*, oral *ō* and trimoric *ô* remain distinct
symbols. The textual class also lists `{*ɔ̆}`, but the compiled acceptor
did not recognize the corresponding probe. That is recorded as a technical
qualification, not counted as a successful non-high control or silently
repaired. No current firing depends on that diagnostic.

The 165 schematic onset × cluster × following-vowel combinations vary
five onsets (`zero,x,k,xl,b`), eleven intervening sequences
(`r,st,d,θr,sk,b,nt,n,sj,z,zd`) and three vowels (`a,i,u`).
Together with 23 source/current-form probes and four additional controls,
they make 192 component inputs. They are controlled strings, not 192 lexical
witnesses. Additional controls separate noninitial *i*, long *ī*, acute
notation and the context wrapper.

### Selected inputs are not interchangeable with dictionary citations

The 387 determinate selected derivations have eight existing mismatches:
1973, 2013, 2030, 2162, 2224, 2240, 2298 and 2300. The six other OE research
rows have no selected runnable target and are not silently included in this
denominator. No non-OE cascade was evaluated.

Meed selects a dative, not Hill's nominative. World selects a documented
mixed-stage transponent, not an uncomplicated full Proto-Germanic compound.
The citation/input/stage axes remain independent throughout.

## Diagnosis

### Exhaustive live census

`adjudicate.py SC015 --prepare` supplied the routed reading list.
`--evidence` rebuilt and checked canonical runtime evidence in the backend
container; the derived private identity subsequently reproduced production
over all 387 selections. There are exactly four SC015 applications.

| ID / lexeme | Selected input | Immediately before SC015 | Immediately after SC015 | Final / witness role |
| --- | --- | --- | --- | --- |
| 2124 meed | *mízdai* | `*m*í*z*d*ē` | `*m*é*z*d*ē` | *meorde*; live lowering before *zd*, after an earlier ending change; supports both main hypotheses |
| 2137 nest | *nístą* | `*n*í*s*t*ą` | `*n*é*s*t*ą` | *nest*; live *st* witness; does not alone distinguish consonantal from following-vowel conditioning |
| 2283 wether | *wíθrą* | `*w*í*θ*r*ą` | `*w*é*θ*r*ą` | *weþer*; live computational application, but unsupported as a historical *i*-grade lowering witness on the checked comparative evidence |
| 2302 world | *wír-àldu* | `*w*í*r*à*l*d*u` | `*w*é*r*à*l*d*u` | *weorold*; live application and conditional computational interaction, with mixed-stage input and independently defensible *wer-* alternative |

The entire live population is given, rather than the single world example
on the chronology card. Classification as a live application does not itself
establish a historically valid input or a historical ordering edge.

### Complete-corpus experiment results

Every variant produced exactly one final for each of 387 selected inputs.
All eight original mismatch identities remain mismatches in every trial.
The identity reproduces all 387 production finals. The table reports new
differences, not a scientific ranking by match count.

| Private variant | Rows with changed sampled checkpoints | Changed finals | New mismatches / total mismatches |
| --- | --- | --- | --- |
| Incumbent identity | None | None | 0 / 8 |
| Current right condition, no onset-velar guard | 2100 | 2100 | 1 / 9 |
| Hill, immediate *z/st/r*, no following-vowel condition | 2095, 2250, 2283, 2313, 2314 | 2095, 2283, 2313, 2314 | 4 / 12 |
| Hill, *z* restricted to preconsonantal/final position | Same five | Same four | 4 / 12 |
| Skip SC015 | 2124, 2137, 2283, 2302 | All four | 4 / 12 |
| Current SC015 displaced just after SC036 | 2124, 2137, 2283, 2302 | 2302 | 1 / 9 |
| Hill immediate rule displaced just after SC036 | 2095, 2124, 2137, 2250, 2283, 2302, 2313, 2314 | 2095, 2283, 2313, 2314 | 4 / 12 |

All changed native results are:

| Variant / affected selection | Selected input | Production final | Private final |
| --- | --- | --- | --- |
| No onset guard: 2100 lid | *xlídą* | *hlid* | *hled* |
| Both Hill rules, early or late: 2095 learn | *líznōjaną* | *liornian* | *leornian* |
| Both Hill rules, early or late: 2283 wether | *wíθrą* | *weþer* | *wiþer* |
| Both Hill rules, early or late: 2313 learn imperative | *líznô* | *liorna* | *leorna* |
| Both Hill rules, early or late: 2314 learn third singular | *líznōθi* | *liornaþ* | *leornaþ* |
| Skip: 2124 meed | *mízdai* | *meorde* | *miorde* |
| Skip: 2137 nest | *nístą* | *nest* | *nist* |
| Skip: 2283 wether | *wíθrą* | *weþer* | *wiþer* |
| Skip or displaced incumbent: 2302 world | *wír-àldu* | *weorold* | *wuruld* |

The fifth Hill-affected row is thistle 2250, selected *θístilas*:
`*θ*í*s*t*i*l*a*s` becomes `*θ*é*s*t*i*l*a*s` at lowering, but
i-mutation subsequently restores the high vowel. Both paths finish
*þistles*. This is a real live-corpus example of convergence masking a
different earlier history, not an additional final-output regression.

For learn, the candidate changes *líz-* to *léz-*, followed by the existing
rhotacism *lérn-*. The selected long *ō* intervenes between root and *j*;
the high-front-triggered component experiment on *leznijana* is therefore
not a derivation of the actual selected *líznōjaną*. Current later operations
yield *léo-* instead of *lío-*. Hill explicitly reports both OE *leornian*
and *liornian* and relates the alternation to the historical weak-III
paradigm [@Hill2017, p. 153, n. 25]. This is specific relevant evidence,
not permission to change three selected cells or introduce an optional
lexical sound rule. Kroonen's different *liznōn-* citation and formation
argument must also be retained [@Kroonen2013, p. 340].

### Positive and negative supplementary evidence

The following are component-stage predictions. Source *h* is serialized as
CAPR *x*. Source close *ẹ* is represented by CAPR *e* for this diagnostic;
this is not a claim that all authors' vowel inventories are identical.

| Probe | Historical/source status | Current component | Hill component | What it establishes |
| --- | --- | --- | --- | --- |
| *iz, hiz* | PGmc pronouns | Retain *i* | *ez, hez* | Genuine distinction: no following vowel exists [@Hill2017, pp. 137--138, 153] |
| *hir* | Early-PGmc antecedent under Hill's argument, not his late-PGmc citation | Retain *i* | *her* | Distinguishes conditioners and feeds the independent lengthening test [@Hill2017, pp. 156--158] |
| *wiraz* | Early inherited-*i* reconstruction; established *wer-* is an alternative endpoint | *weraz* | *weraz* | Positive, but not a discriminator by itself [@Hill2017, p. 156; @RingeTaylor2014, pp. 34--36] |
| *nistan* | Hill's PGmc neuter citation; not silently identified with CAPR *nístą* | *nestan* | *nestan* | Positive *st* witness [@Hill2017, p. 153] |
| *mizdōn* | Source nominative, not the selected dative | *mezdōn* | *mezdōn* | Positive *z* witness; selected-cell distinction survives [@Hill2017, p. 153] |
| *fiskaz* | PGmc masculine a-stem | Retains *i* | Retains *i* | *sk* negative; a broad non-nasal intervener rule instead gives *feskaz* [@Hill2017, p. 154] |
| *wiskō* | PGmc feminine citation; OE evidence is compound *gran-wisc* | Retains *i* | Retains *i* | Another *sk* negative, not an attested simple OE noun [@Hill2017, pp. 154--155] |
| *bitanaz* | PNWGmc participial antecedent | *betanaz* | Retains *i* | Substantive dental negative to the incumbent domain [@Hill2017, pp. 150--152] |
| *biðanaz* | PNWGmc Verner participial antecedent | *beðanaz* | Retains *i* | Same formal contrast, but its North Germanic evidence is disputed below [@Hill2017, pp. 151--152; @Fulk2018, pp. 58--59] |
| *nidana* | Controlled antecedent-shaped probe based on the cited OHG adverb, not an independently quoted complete PGmc word | *nedana* | Retains *i* | Noninflecting dental negative; removes a simple appeal to inflectional levelling [@Hill2017, p. 152; @Lloyd1966, p. 741] |
| *xlidą* | Current lid input with acute omitted only for a notation control | Retains *i* | Retains *i* | Hill excludes *d* without a velar-onset exception; removing only the incumbent guard lowers it |

The derivative controls are equally important:

| Controlled chain | Result | Scope |
| --- | --- | --- |
| *nistijana → nestijana → nistijana* | Lowering, then existing i-mutation restores *i* | Earlier-*i* control of Hill's source *nẹstijana* |
| *listiz → lestiz → listiz* | Same | Explains why high-vowel derivatives do not alone refute earlier *st*-lowering |
| *liznijana → leznijana → liznijana* | Same | A source-matched front-trigger derivative, not a substitute for current learn's *ōj* selection |

Hill supplies the lowered source forms and the more recent mutation
interpretation [@Hill2017, p. 153, including n. 25]. The requested shorter
*nestijan* was tested as a stem-shaped component probe too; it was not
mislabelled as a complete PGmc citation or admitted to the corpus.

All twelve supplementary full-prefix inputs were deterministic in all seven
recipes. Under the incumbent, raw *iz/hiz/hir* give *ī/hī/hir*; the early
Hill recipes give *ē/hē/her*. The late Hill trial misses *z*-conditioning
after *z* has already disappeared and again gives *ī/hī*.
Full-prefix *bítanaz/bíðanaz* give *betan/bedan* under the incumbent and
*bitan/bidan* under Hill. These expose the root contrast; neither set of
endings is certified here as the complete history of OE *-biten/-biden*.
Raw *mízdōn* happens to yield *meorde*; that coincidence does not turn
the nominative into evidence for the selected dative.

Other full-prefix controls: *wiraz → wer*, CAPR *nístą → nest*,
*fískaz → fisċ*, *wískō → wisċu*, *nístjaną → nistan* and *lístiz → list*
under both early descriptions. They are diagnostic outputs, not admissions
or claims that every source form's native suffix/quantity is fully modelled.
The absence of *hēr* from raw *hir* specifically exposes the missing
lengthening operation rather than refuting Hill's conditioning.

## Literature

The existing `014-015-opening-vowel-prelude.dossier.md`, its matching
`.book-dossier.md`, and `reader_facing/014-015-opening-vowel-prelude.md`
were read through the SC015 prepare routing. Their unstressed-levelling
interpretation was checked against the literal matcher and all four
applications, rather than reused as historical authority.

### Reference ingestion and verification

The supplied Downloads holding `nowele.70.2.02hil.pdf` was identified as
Eugen Hill's 2017 NOWELE article, volume 70.2, pp. 135--170,
DOI `10.1075/nowele.70.2.02hil`. The original is retained unchanged in
`docs/references/hill_2017_west_germanic_lengthening.pdf`; its SHA256 is
`73278c5e5e7cdc845fc09b160993c43f2673b0e83fb58ef9091ceedeb530659e`.
The original Downloads copy is retained too.

The searchable native-text extraction preserves all 36 sheets and printed
folios 135--170, with printed-page markers. Exactly 36 BACKSPACE controls
immediately preceding reconstruction asterisks were removed; no linguistic
Unicode normalization or silent authorial correction was applied. Every page
149--158 was checked against its rendered original. The entire argument
through p. 165 was read, including the *hiri* discussion, not just the
favoured lowering tables. The final bibliography is retained.
Hill's p. 158 “raising” in the lowering argument is preserved as printed.
The `Hill2017` bibliography entry and the resource index register the
holding and verification limits. Other pages have not received exhaustive
diplomatic glyph certification.

### Source comparison

| Source and checked printed pages | Argument and appropriate weight |
| --- | --- |
| Campbell 1959, p. 43, §§114--116 | Traditional next-vowel description; OE *nest*, *wer* and *spec/spic*; nasal-plus-consonant restriction. This is not support for unrestricted nasal blocking or an anywhere-in-onset velar guard. |
| Lloyd 1966, pp. 738--745 | Sustained criticism of a regular general *i*-a-umlaut, including participles and noninflecting adverbs; shared *r*-conditioned history is not excluded by the anti-umlaut argument. |
| Cercignani 1979, pp. 72--82 | Phonemic *e/i* opposition and criticism of global allophony. This question must not be conflated with the existence of particular conditioned changes. |
| Cercignani 1980, pp. 126--134, especially pp. 130--132 | Rejects a single inherited early-umlaut package; discusses consonantal and analogical alternatives. Explicitly says the North Germanic onset restriction cannot simply be assumed for West Germanic. |
| Ringe--Taylor 2014, pp. 33--37 | Rejects a general WGmc *i*-lowering rule, allows older *e* in key examples, and supplies a competing account of *here*. Later interstress/compound history on p. 326 is a separate argument, not a proof of SC015's current conditioner. |
| Fulk 2018, pp. 55--59 | Traditional non-high-vowel account with substantial qualifications; lowering less systematic in English, possible older dating. Specifically defends a class-I analogical interpretation and cites ON *beðinn*; p. 59 n. 6 challenges the alternative contamination account. |
| Hill 2017, pp. 149--158, 159--165 | Participles/adverbs, *z/st/sk/r*, masked Gothic evidence, lowering before monosyllabic-*r* lengthening, and the substantive *hiri* objection. Stronger than a mere consonantal reinterpretation of *nest*, but not immune to counterexamples. |
| Howell--Salmons 1997, pp. 83--86, 94--101 | Independent place/geminate sensitivity in umlaut processes. Its detailed Upper German high-back-vowel fronting and WS back-mutation examples do not directly establish CAPR's exact early *i*-lowering coronal class or onset guard. The local legacy filename contains 1988; the held article is 1997. |
| Seebold 1970, pp. 94--95 | Actual await paradigm with *beðenn*; proposes contact with the bid verb, explicitly acknowledging the competing regular-lowering interpretation. This is concrete counterevidence to Hill's printed table, not a newly verified original of Seebold's separate 1966 article. |

### What survives the comparison

Hill's strongest point against indiscriminate following-vowel conditioning is
the conjunction of dental/noninflecting negatives with final monosyllabic
positives. A following low vowel is not present in *iz/hiz/hir*; merely
preserving those forms through a rule requiring that vowel misses the
observed source histories. His *st/sk* contrast is a useful consonantal
discriminator, and his later-mutation account supplies an explicit trigger,
not a stipulation that high-vowel derivatives are exceptional
[@Hill2017, pp. 150--156].

However, the supposed universal class-I evidence is not clean. Hill's
original p. 151 really prints ON *biðinn*. Fulk instead uses *beðinn* and
argues that a frequent verb can preserve an older lowered participle while
other paradigms level it out. His n. 6 expressly says *biðinn* does not occur
and questions the antiquity and independent support of contamination from
*biðja* [@Fulk2018, pp. 58--59]. Seebold's original p. 94 really prints
*beðenn (!)*; he prefers formal contact with the bid verb, and points to
actual OE formal interference, but also states the alternative that this
is the one class-I participle preserving expected *e*
[@Seebold1970, pp. 94--95].

Thus Hill's particular ON table cell cannot be accepted uncritically.
Fulk supplies a specific alternative argument, not just “analogy happened”.
Nevertheless frequency and an available long-*ī* present do not by themselves
demonstrate the exact short-*i* remodelling, date and paradigm path needed
for every participle. The attestations and chronology of *beðinn/biðja*
remain a discriminating question. OE *-biten/-biden* and the adverbs retain
their evidential force; the disputed ON cell is not used to erase them
[@Hill2017, pp. 151--152; @Fulk2018, pp. 58--59].

The other serious counterexample is *irh*. Hill does not ignore it:
he cites a loan account with specific bibliography
[@Hill2017, p. 156, n. 30]. But Kroonen reconstructs inherited *irha-*,
adduces the animal and leather forms and external comparisons, and discusses
their difficulties [@Kroonen2013, p. 270]. The original page was checked.
If that inheritance is right, an unrestricted immediately-pre-*r* rule
predicts *erha-* and is wrong. Both private Hill components do exactly that;
the current coronal-only rule preserves *irha-* because of intervening *h*.
The loan explanation is a named competing hypothesis, not established merely
because it protects Hill. The later EWA and Frings passages cited by Hill
have not been independently verified in this investigation; their reported
status is retained.

The source evidence therefore favours a serious consonant-sensitive common
development over treating the current broad coronal matcher as established,
but does not settle the unrestricted *r* domain by author count or recency.

## Historical analysis

### Reassessment of the four current witnesses

Nest 2137. Kroonen's *nista-* and Orel's *nistan* preserve the relevant
*st* and connect the formation with ‘down’ plus ‘sit’. The source folios
are printed 391 and 287, respectively, not a PDF-sheet coordinate
[@Kroonen2013, p. 391; @Orel2003, p. 287].
CAPR's nasal neuter ending is a separate input convention. This is a sound
positive witness for the root change under both descriptions, but not
independent evidence that the next vowel rather than *st* caused it.
Neither a different ending notation nor a successful *nest* final dates
the event [@RingeTaylor2014, pp. 33--35; @Hill2017, p. 153].

Meed 2124. Kroonen gives *mizdō(n)-* and Orel *mizđō(n)* with a secondary
West Germanic alternative; the actual printed pages are 370 and 272.
Both originals were checked. Older ledger references to 410/311 confuse
sheet and printed pagination and are not adopted here
[@Kroonen2013, p. 370; @Orel2003, p. 272].
The selected dative *mízdai → meorde* carries retained *z* through lowering
and later rhotacism. It is neither the source nominative *mizdōn* nor an
automatic proof of the r-less *mēd* history. The sources' competing
*z*-loss, lengthening and paradigm accounts require their actual cells;
Ringe's later discussion corrects the older volume's chronology
[@Ringe2017, pp. 120--121; @RingeTaylor2014, pp. 83--85, 284--287].
No dative-to-nominative substitution was made to support a rule.

Wether 2283. The checked comparative entries do not establish the selected
*i*-grade. Kroonen prints *weþru-* and the conditional year/yearling
etymology; the printed “adv.” label is anomalous beside his masculine
animal reflexes and is not silently corrected. Orel gives masculine
*weþruz ~ weþraz*, explicitly retaining stem alternatives
[@Kroonen2013, p. 584; @Orel2003, pp. 459--460].
Neither supports treating *wíθrą* as a securely reconstructed neuter
*i*-grade antecedent. Wether is not weather.
Consequently the loss of lowering in the Hill trial is a selected-input
problem to adjudicate, not evidence for extending Hill to all *θr*.
Private *wéθrą, wéθruz, wéθraz* each yield *weþer* in all seven recipes.
The first is expressly a root-only control retaining the questionable
current ending; the latter two preserve distinct source-backed formation
alternatives. Output convergence selects none of them.

World 2302. Orel gives *wira-alđiz*; Kroonen's man and age component
entries are not an authored complete quotation of CAPR's selected
compound [@Orel2003, pp. 462--463; @Kroonen2013, pp. 20--21, 588].
Ringe--Taylor instead derives the word from established *wer-* through
*weraldiz → weraldu → weruld → weorold/worold*, on printed p. 326, not
sheet 341 [@RingeTaylor2014, p. 326].
CAPR's sidecar already labels the selected *wír-àldu* a mixed-stage
transponent, combining older root *i* with later morphology. It must not
be used as an unqualified PGmc dating witness.
The root-only *wér-àldu* control yields *weorold* under every trial,
including skipped and late lowering. This experimentally removes the
necessity of SC015 for that control without pretending it is a complete
source-quoted replacement input.

### Chronology: separate historical evidence from serialization

Hill's *r* argument is more specific than “NWGmc lowering can be old”.
His proposed common history is early *hir → hẹr → hẹ̄r*, compared with
*wiraz → wẹraz*. The long vowel of the adverb, including Gothic *hēr*,
is the additional argument for lowering before common monosyllabic-*r*
lengthening. Gothic *wair* alone cannot give that result, because later
Gothic breaking can conceal the earlier quality; Gothic *is/mizdō*
can likewise conceal earlier *e* by raising [@Hill2017, pp. 148--149, 156--158].

The independent component supplement models short-*i/e/a/u* lengthening
before final *r*, rather than an *e*-only proxy:

| Input | Lowering then lengthening | Lengthening then lowering |
| --- | --- | --- |
| *hir* | *her → hēr* | *hīr → hīr* |
| acute CAPR *xír* | *xér → xḗr* | *xīr → xīr* |
| inherited *hīr* control | *hīr* | *hīr* |
| *hwar, þar* | *hwār, þār* | *hwār, þār* |

The low-vowel controls are source-discussed adverbs; the short-*u* mapping
is only a schematic completeness control. CAPR *ē/ḗ* here represents the
source close long vowel for the component diagnostic, not an adjudicated
identity with inherited long *ē₁*. A production history would have to keep
Hill's close-*ē₂* interpretation and the existing long-vowel consumers
distinct where necessary. The supplement is not a newly adopted lengthening
law or proof that the current full prefix already implements *hēr*.

This establishes a conditional necessary order from the specified input,
two operations and independently argued target. The original primary
receipt's *e*-only lengthening proxy is explicitly limited and is superseded
for this inference by the generic-short-vowel supplement. It is not used
to make the reverse order look innocuous.

The historical force still depends on Hill's argument for the common
lengthening, his reconstruction of the pronoun-based adverb and his
analysis of the Gothic exception. Ringe--Taylor discusses a different
accentual/ablaut and lengthening explanation for *here*
[@RingeTaylor2014, pp. 36--37]. Hill addresses the apparently exceptional
Gothic *hiri* at length, preferring recent *hi-ri* univerbation to unsupported
blocking or pitch rescues [@Hill2017, pp. 159--165]. That makes the common
PGmc hypothesis substantive, not a demonstrated universal chronology for
every member of the lowering bundle.

The *r*-specific inference does not independently date lowering before
*z* or *st*. Hill's shared PGmc/NWGmc account is a serious candidate;
the directly cited *z/st* positives and their Gothic masking possibilities
must be distinguished from the special additional *hēr* argument.
No independent dialectal innovations are inferred simply to avoid choosing
between accounts [@Hill2017, pp. 153--158].

The relevant relations are:

| Relation | Evidential classification and result |
| --- | --- |
| *i*-lowering before monosyllabic-*r* lengthening | Independently argued, conditional on Hill's common adverb history and domain. Confirmed as a necessary order in the specified short-vowel component experiment; not a new canonical edge. |
| PGmc *r*-lowering before later OE operations | Stage-entailed if the PGmc hypothesis is adopted; stage labels cannot independently prove that hypothesis. |
| SC015 before SC036 on current world | Verified model-local dependency for the incumbent input and incumbent next-vowel matcher. Not an input/formulation-independent historical edge. |
| Lowering before final *z*-loss/rhotacism | Required to recognize original *z* directly; late Hill misses *iz/hiz* after loss. Direct *r* lowering after rhotacism could mimic some outcomes, so final *r* alone does not date original-*z* lowering. |
| Lowering before later i-mutation | Source-supported derivative analysis and successful component/live-thistle convergence; scope is the actual trigger-bearing formation, not every learn cell. |
| Earlier dental developments | *nisd- > nist-* is already presupposed in the source *nistan* input. The assay does not reconstruct or date that earlier change by pretending it fired in the current cascade. Current dental hardening does convert *biðanaz* to *bidanaz* before SC015, and the broad dental matcher still lowers it. |

The world displacement deserves particular precision. In production,
lowering first produces *wéràldu*. SC036 later supplies
`*w*é*r*u*l*d*u` at the relevant serialized level.
With the incumbent moved late, SC036 first gives `*w*í*r*u*l*d*u`.
The resulting high following vowel blocks that incumbent lowering, and
later *wi*-raising produces `*w*ú*r*u*l*d*u → wuruld`.

The late Hill rule has no following-vowel requirement. After SC036 it
still lowers `*w*í*r*u*l*d*u` to `*w*é*r*u*l*d*u`, before *wi*-raising,
and produces *weorold*. Thus even the unchanged *i*-transponent does
not force the old SC015--SC036 relation under the alternative conditioner.
With *wer-* established in the input, neither lowering rule is needed.
The registry's present `independently_demonstrated` world record should
therefore be reconsidered in a later authorized package, not silently
deleted or treated as a uniquely historical result.

## Verdict

This is a prospective recommendation, not an adopted registry verdict.

1. Reformulate the scientific exposition. SC015 is not unstressed
   front-vowel levelling; its live operation concerns initial short *i*.
   The current unstressed rationale and blanket chronology prose should
   not survive the eventual adjudication.
2. Prefer investigation of a restricted consonant-sensitive common
   development over the present all-coronal/non-high-vowel generalization.
   In particular, preserve the distinction between *r*, tautosyllabic *z*
   and *st*, their evidence and their possible dates. A split historical
   interpretation is better supported than treating all current firings
   as proof of one pan-PNWGmc law.
3. Do not retain the onset-velar guard as independently established OE
   phonology. Removing it alone breaks lid, but selective right conditioning
   preserves lid without it. Cercignani expressly warns against the WGmc
   extrapolation, and Fulk limits the cited onset restriction to North
   Germanic [@Cercignani1980, p. 130; @Fulk2018, p. 57, n. 3].
4. Retain the current executable temporarily; defer adoption of a replacement.
   The *irha-* and ON participle counterevidence, learn's selected formations,
   wether's reconstruction and the common-*hēr* representation need explicit
   dispositions. Neither twelve candidate mismatches nor eight incumbent
   mismatches decides those historical questions.
5. Do not reorder production on the strength of either the old world card
   or the successful late-Hill serialization. Reassess the particular edge;
   preserve independently supported early *z* and later mutation relations.

### Exact tested candidate, not a production instruction

The conservative *z* version was:

```foma
define AFTauto [ Ctx([
    {*i} -> {*e} || .#. EnglishStarConsonant* _ [{*z} [EnglishStarConsonant | .#.] | {*s} {*t} | {*r}],
    {*í} -> {*é} || .#. EnglishStarConsonant* _ [{*z} [EnglishStarConsonant | .#.] | {*s} {*t} | {*r}]
]) ];
```

The rival unrestricted-*z* experiment used:

```foma
define AFHill [ Ctx([
    {*i} -> {*e} || .#. EnglishStarConsonant* _ [{*z} | {*s} {*t} | {*r}],
    {*í} -> {*é} || .#. EnglishStarConsonant* _ [{*z} | {*s} {*t} | {*r}]
]) ];
```

They agree on all 387 selected finals, but not over arbitrary probe strings:
intervocalic *wizana* is lowered by the latter and not the former.
Preconsonantal/final *z* is an explicit local proxy for Hill's
tautosyllabic description, not a newly proven general syllabification
algorithm. First-syllable targeting and close-*e* representation also remain
declared modelling approximations. The exact definitions and controlled
counterexamples are retained even though no candidate is presently adopted.

Both formulations improve the particular lid/dental/final-pronoun
contrasts without lexical IDs or grammatical conditions. Neither is yet
a sufficient whole-history package: both predict *erha-* under inherited
*irha-*, both change the selected learn forms and wether, and neither
introduces Hill's earlier *r*-lengthening or resolves the long-vowel
inventory. “Superior in those diagnostics” is not “ready to land unchanged”.

The permissible hybrid is therefore a component-specific common history
plus only independently established subsequent operations. Later i-mutation
is already a justified mechanism in the trigger-bearing derivatives.
The ON bid/await contamination and weak-III levelling remain specific
proposals to test, not blanket exceptions coded into the sound law.

## Propagation (only after verdict)

No production propagation was performed. No Foma rule/comment, corpus field,
stage/context selection, registry, reader, existing dossier, lexical account
or baseline was edited. No baseline was regenerated; no commit or push
was made. Canonical runtime evidence was rebuilt by the authorized evidence
interface before private protections were captured, not replaced by a
private candidate.

Only reference ingestion and this new noncanonical research bundle are
repository changes. Existing frozen SC017--SC019 investigation receipts
and the historical test-maintenance commit remain untouched.
The private full run verified 212 protected container paths unchanged.
An independent comparison verified all 202 host-snapshot paths unchanged;
the host/container sets overlap and are not 414 independent files.
They include source/corpus, runtime evidence, registry, baseline and frozen
investigation material. Receipt hashes are recorded in `provenance.json`.

A later approved package would need, together:

- Exact rule/component/stage decisions, with a separate interpretation of
  inherited *r*-lowering and its close-long-vowel consumer, not a name-prefix
  date.
- A source-backed wether field/cell decision and world entry-stage decision;
  learn's actual paradigm-trigger history and the fate of its three selected
  targets; no automatic edits merely because the candidate has four new
  mismatches.
- Reclassification or substantiation of the world chronology record,
  preserving the historical card; no graph edge promoted from an experiment
  alone.
- Correction of the three routed 014--015 expositions, relevant lexical
  SOURCE accounts and directly affected chapter statements. The unchanged
  SC014 law must not be conflated with SC015.
- Focused positive/negative intermediate and reader-definition tests,
  all selected-row regression, any explicitly approved fingerprint migration,
  canonical finalization and then the publication checks appropriate to
  an adopted change.

Current regression evidence is in the private receipts, not weakened permanent
expectations. The references' bibliography/locator checks are separate from
scientific acceptance. No full-suite or publication rerun is represented as
having occurred for this research-only delivery.

## Residue

The exact remaining decisions are finite:

1. Does *irha-* belong to the inherited Germanic domain? Evaluate the specific
   loan arguments reported by Hill against Kroonen's positive inheritance
   case; do not assume loan status to protect the *r* rule
   [@Hill2017, p. 156, n. 30; @Kroonen2013, p. 270].
2. What are the actual early attestations and paradigm relations of ON
   *beðinn* and *biðja*? Hill's printed *biðinn* conflicts with checked
   independent treatments. This is a factual and chronological question,
   not a choice between a long-*ī* analogy slogan and an exceptionless-law
   slogan [@Hill2017, pp. 151--152; @Fulk2018, pp. 58--59;
   @Seebold1970, pp. 94--95].
3. Which learn cells carried a proximate *i/j* trigger before remodelling,
   and what supports the current *ōj/ô/ōθ* selections and *lio-* targets?
   Hill's p. 153 n. 25 gives a concrete paradigm question, but not an
   exact reconstruction of all three CAPR cells. Preserve Kroonen's
   different formation analysis [@Hill2017, p. 153, n. 25;
   @Kroonen2013, p. 340].
4. Is wether's comparative *e* and masculine u/a formation to replace the
   unsupported current *i*-grade/neuter-shaped input, and which exact cell
   is selected? A root-only score-neutral edit is insufficient
   [@Kroonen2013, p. 584; @Orel2003, pp. 459--460].
5. What input stage and cell best represent world? Established *wer-* is
   historically defensible and removes the present dependency, but a full
   stage/morphology decision cannot be inferred from the experimental
   *wér-àldu* control [@RingeTaylor2014, p. 326].
6. How broadly should *r*-lowering be stated, what exactly is shared
   chronologically with *z/st*, and how is Hill's close long vowel represented
   without confusing it with inherited *ē₁*? The *hēr* argument must be weighed
   against the competing adverb account, not generalized to every consonantal
   component [@Hill2017, pp. 148--158, 159--165;
   @RingeTaylor2014, pp. 36--37].

These gaps justify temporary executable retention, not retention of misleading
historical prose as an authoritative scientific conclusion. No lexical
selection, chronology record or sound law has been changed to manufacture
a cleaner result.
