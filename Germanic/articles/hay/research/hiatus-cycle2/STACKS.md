# Integrated hiatus experiments

## T1: comparison inventory and common substrate

[`panel.tsv`](panel.tsv) extends the pinned first-cycle
[`historical.tsv`](../hiatus/historical.tsv) by key; the receipt
materializes both inventories without overwriting conflicting early
claims. For ‘couch’, the C1–C3 records supersede the alleged bare
token and separate the accusative, conditional genitive and
unattested nominative. The Kentish *hei weg* row records the future
editorial correction **859**, not OCR **839**, without editing the
article. The *cǣġ/cǣġe* pair remains an independent retention check;
‘rainbow’ is related to ‘rain’, not a separate root, and *sēl* is
not counted as attested.

The original 49 rows had 29 admissions, eight rejections and 12
without a submission. In the latest inherited 54, the same 37
submissions split **29 admitted / 8 rejected** in each model;
17 have no submitted full form. The supplement adds eight
admitted full submissions, including two using the same fixed
active-corpus identities as the joint assay. These are counts of
submissions, not of independent witnesses or matching outputs.
Each substrate run now includes 65 traced inputs; the three
explicitly marked compound probes await boundary-aware replay
and the observed Kentish spelling has no submitted input.

All eight older rejections remain visible. For ‘couch’ the gap
is a later final *-u*, not the cluster or encoding (C3).
For ‘call’, ‘strew’, ‘betray’ and ‘prepare’ the earlier long
preterite ending is not accepted in the submitted forms; their
separately justified stage inputs carry a reduced ending and do
not prove its exact earlier quantity. The exact weak tail in
‘flock’ remains disputed; shortening or dropping the vowel to
pass the gateway would pre-judge HVD. ‘Pillow’ is a loan with a
source-supported later state. ‘Brandish’ has a grade/segmental
problem and the retained-vs.-lost palatal comparison is local,
not an amendment to the accepted early lexeme. Stage entries
record the preceding derivation and use the exact before-stage
anchor; an encoded synthetic state is not a historical input.

| Executable site (A/B2, relative to its neighbours) | Historical purpose and constraint |
|---|---|
| `OEIUmlaut` > `OEWLossBeforeI` > `SC047FinalIi` | Mutate the root before losing noninitial *w* before fully weak *i/ī*, leaving *e.i* where both vowels survive. In A/B2 the following experimental baseline already contracts final stressed *i.i*; that component is not a law for unlike nuclei or every medial identical pair. See Ringe–Taylor pp. 258–261, 317–318. |
| `OEBackMutation` > `OEMedLongShort` > `OEHighVowelApocope` > `OEMedialSyncope` | Distinguish mutation, shortening and weight-sensitive deletion. The following medial-syncope anchor is an identity; the quantitative component itself can delete medial high vowels. Contraction/gliding before it can change eligible weight; late placement cannot undo apocope. |
| `OEMedUnstressedILowering1`/`OEMedUnstressedILowering` before `OEJLossAfterHeavy` | Lower weak *i* in the implemented environments, not a nuclear offglide. Heavy-context *j*-loss is not general loss of final *j* after a long nucleus. |
| `OEJStrengtheningAfterFrontDiphthong` > `OEIntervocalicJVocalization` > `OEUnstressedEIContraction` | Separate consonantal strengthening/vocalization from SC083's unstressed initial/member deletion. The common substrate changes only the last operation, to the S1 foot guard. A physical order is not a dated series of independent sound laws. |
| `OEHLoss` > `OEContraction` > `OEPalatalFricativeMerger` > `OldEnglishOrthography` | Intervocalic velar loss provides another source of adjacent nuclei, after ordinary syncope in the historical chronology (Ringe–Taylor pp. 260–261). The separate general contraction component has its own matching domains; the later merger/serialization cannot tell us whether two identical spellings arose via a glide, fricative or nucleus. |

[`panel-traces.json.gz`](panel-traces.json.gz) has all stage
inputs/outputs and the S0/S1 differences. S1 changes only the
root-stress controls: local past of ‘call’ in all orders and
full present and participle in A/B2. The inherited frozen
traces were replayed before applying S1. To reproduce, run
`bash Germanic/articles/hay/research/hiatus-cycle2/run-container.sh --panel --stage-cache "$cache"`
from the repository root with the private cache described in
[STRESS.md](STRESS.md).

## T2: matched resolution, boundary and monophthongization

[`matched.py`](matched.py) executes the same six follow-on classes
for direct contraction (*e.i > ē*), approximant formation plus
assimilation (*e.i > ej > ē*) and nuclear incorporation plus
monophthongization (*e.i > ei̯ > ē*). The first comparison uses
the same post-*w*-loss anchor for both components of the serial
arms, so agreement cannot be an artefact of a different window.
Separate trials delay only the second operation to before
heavy-context loss, immediately before the palatal merger, or
after the merger. The nuclear component uses the existing atomic
`*ei` proxy; its spelling and the lack of a separate stress
tier for that proxy are not evidence of its OE phonetics.

| Comparison | Result |
|---|---|
| Dental stops; all stops; dental obstruents | All resolve A/B2 ‘call’ before a stop, ‘strew’ before *d* and stage-local ‘flock’ before *d*. The first two do not cover the *þ/ð* present; none cover ‘couch’. The local ‘flock’ gives *ēd*, losing an ending that the comparison calls for. The early ‘strew’ gloss, if correctly identified, positively cautions against uniform removal of the second element. |
| *d, þ/ð, n*; all coronals; all consonants | Each gives A/B2 inflected *strēne* on the conditional early ‘couch’ input. Extending beyond this narrow set adds synthetic predictions before *t, s, z, l, r* or further stops/labials; equivalent historical edges in this panel do not license them. Narrowest useful comparison class is not the same as a demonstrated natural class. |
| Word edge and before a following vowel | Compare retention (H0), consonantal and nuclear desyllabification, and direct contraction. With the earlier Anglian ‘hay’ input at the absolute edge, outputs are *hei*, *heġ*, *hei* and *hē*, respectively; the two instances of *hei* are internally different. Adjacent following vowels are separately tested, not treated as an edge or a consonantal coda. Early prevocalic gliding may be undone by frozen intervocalic vocalization. |
| Marked compound boundary | With the same segments, the absolute-edge rule ignores the first-member edge; the member-edge rule reaches it but not ordinary internal adjacency. Neither predicts the unmarked last-member effect; an explicit local accent licenses it. These are isolated component lookups, not whole attested compound reconstructions or a measurement of secondary stress. |
| Palatal origin and merger | Pre-merger approximant assimilation leaves secondary *ʝ* distinct. After the frozen *ʝ > j* merger, the same assimilation reaches ‘rain’ (*rēn*), plausibly a variant but no general replacement for retained *reġn*. ‘Sail’ and ‘way’ remain outside this particular *d, þ/ð, n* merger domain. For a broader fricative treatment the inherited J8 audit shows adverse *sēl* and *wē* predictions (see [Dahl–Jones](../hiatus/DAHL_JONES.md#j8-joint-assay)). |

An unmarked `*ei` before the selected consonant has the same
monophthongization in the stage-local tests whether produced by
hiatus incorporation, vocalization of an approximant, or
vocalization of a fricative. The inherited `*ai` control is not
its input; earlier processes and a different nucleus keep it
outside the rule. Breaking with **retained** *ʝ* gives an
intervening consonant that blocks the tested merger. Conversely,
the rule cannot protect an independent nuclear `*ei` in the
same context without additional, historically justified structure
or chronology. That is a real prediction, not a licence to tag
and exempt inherited outputs. Jones’s phonetic notation supports
keeping *ʝ* distinct, not reclassifying every new glide as a
fricative.

The three histories agree at the short nonfinal endpoints when
scope and chronology are matched; their intermediate states,
palatal-origin effects and potentials for exposure to HVD are
not the same. The standalone phone, boundary and origin controls
and all panel derivations are in
[`matched-traces.json.gz`](matched-traces.json.gz).
Replay: `bash Germanic/articles/hay/research/hiatus-cycle2/run-container.sh --matched --stage-cache "$cache"`.

## T3: quantity, absorption and final-palatal retention

The [quantity receipt](quantity-traces.json.gz) separates
lengthening before and after gliding, lengthening as a
consequence of palatal loss, direct contraction, and absorption
after an independently long nucleus. In A, early gliding gives
*heġ*. Prior lengthening plus immediate gliding gives *hēġ*;
delaying the glide with the same prior lengthening instead
gives *hē*, because ordinary HVD removes the still syllabic
second vowel before the glide can form. Post-glide lengthening
gives *hēġ* too, but also lengthens a supplied, already present
short *ej*: it is not innocuous without an independently
defined scope. Contraction produces *hē* directly, without
that apocope firing; the internal trace distinguishes the
two occurrences of the same spelling. Assimilation before a
consonant is not an explanation for a final *hē*.

The broad absorption probe after long nuclei leaves short
*e.i* untouched and removes syllabic *i* without creating
a palatal or lengthening the first vowel. ‘Sea’ and ‘law’
already end in *sǣ* and *ǣ* in A; this is convergent evidence
for an endpoint, not for the diagnostic rule or its placement.
The early absorption arm yields *lēde* in the local ‘betray’
stem and changes the ‘know’ and ‘crow’ traces; the latter
retain unresolved differences of prefix, vocalism and
ending. These are long-root comparisons, not corroboration
of a short-root contraction law (Ringe–Taylor pp. 259–260,
317–318; Campbell §§237, 406).

Dahl’s literal loss rule distinguishes short monophthong
plus *j* (retained) from long monophthong and either
diphthong plus *j* (lost in the edge probes). No secure
independently quantified short-diphthong lexeme was found in
that environment. Late placement also removes the palatal of
the qualified long-diphthong comparator ‘island’. Crucially,
each tested placement exposed to the independently long
*cǣġ* loses its inherited palatal; protected *cǣġe* remains.
Simply moving the rule before experimental gliding therefore
does not repair its independent counterexample. Doing so
before the merger keeps secondary fricatives separate from
inherited *j*; doing it after the merger does not create
evidence for the historical spread of its target. Short
*weġ* and *dæġ* are retained as secondary-palatal controls,
not independent attestations of short inherited final *j*.
See Hogg (1979: 105), Ringe–Taylor (2014: 235, 286), and
the [Dahl–Jones source checks](../hiatus/DAHL_JONES.md).

The tests sustain **both** regular short *hej* and conditional
long *hēj* after independent lengthening; they do not
give that lengthening its historical motivation. A general
long-vowel final-palatal deletion would require better evidence
than an endpoint fit for ‘hay’. Replay:
`bash Germanic/articles/hay/research/hiatus-cycle2/run-container.sh --quantity --stage-cache "$cache"`.

## T4: back-vowel nuclei and hiatus from *h*-loss

Hogg (1992 §3.19; 2011 reprint pp. 58–59) explicitly
analyses early WGmc incorporation as matching a pre-existing
diphthong template, then restricted to short vowel + *u*.
Loss of *w* between the vowels is one source, not a requisite
feature of the subsequent operation; final *w* vocalization
and independent *u*-raising supply other sources. Campbell
§120.3 likewise distinguishes intervocalic loss in the plural
from final vocalization in the singular. Brunner §§128.1,
129.1, 134 records both the *clēa : clawe* alternation and
the *treo, cneo* alternations, while Luick §126 notes early
and later Anglian written *eu*, including Corpus *treu*.
These are not arguments that an onset followed the nucleus.

- **‘Claw’.** Hogg’s nominative has *klawō > klawu > kla.u
  > klau > klæu > clēa*. Ringe–Taylor (pp. 150, 173)
  give already nuclear PWGmc *klau*, with *klawa* beside it,
  yielding *clēa* and *clawe*. Their reconstruction does not
  require a syllabic intermediate lasting into Old English.
  Campbell §598 also distinguishes the remodelled *clawu*
  and documents surviving *clēa* plural forms. Brunner
  reconstructs the oblique with retained *w*. The experimental
  early *w*-loss plus incorporation supplies *clēa* from the
  PNWGmc input without claiming a correct entire paradigm:
  the protected probe keeps *w* but the A/B2 frozen proxy
  renders *clēawa*, not *clawe*.
- **‘Knees’ and ‘trees’.** PGmc plural *knewō, trewō*
  give early raised *knewu, trewu*, with *w*-loss and
  incorporation giving PWGmc *kneu, treu* (Ringe–Taylor
  pp. 61, 174; Brunner §129.1). Endingless singulars can
  reach the same nuclei by final *w*-vocalization after
  ending loss, not by intervocalic *w*-loss. Obliques and
  Northumbrian *cnewa, trewum* keep labial evidence; later
  *cnēow/trēow* involve levelling. The short syllabic
  inputs yield frozen A/B2 *cneowu/treowu*; incorporation
  before frozen diphthong realization gives *cnēo/trēo*.
  HVD does not by itself convert a retained labial with a
  final syllable into this nucleus. Given an already
  nuclear *eu*, realization alone yields the same endpoint.
- **Independent predictions.** The same operation also yields
  *þrēa* ‘threat’ and neuter plural *fēa* ‘few’ from their
  appropriate *-awu* states (Hogg §3.19; Ringe–Taylor p. 173).
  Direct conversion to consonantal *w* yields different outputs.
  Waiting until the general OE contraction anchor loses some
  inputs to intervening rules and cannot give this uniform
  result. The private unaccented *aeu > ēa* bridge fixes a
  transient-symbol admission gap at `OEEwLongDiphthong`,
  not a new phonological law or a lexical exception.

The independent back-vowel evidence therefore motivates
incorporation as a historical **mechanism**, with its own
early, template-sensitive domain. The later *e.i* need not
have had an equivalent template or subsequently merged in
every environment. Ringe–Taylor’s chronology separates
PWGmc *w*-loss before *u* from OE *w*-loss before weak *i*;
only the later *w*-loss is ordered after i-mutation and
before high-vowel syncope. This is not a single timeless
gliding or merger rule.

**Later *h*-loss.** Ringe–Taylor §§6.7.1, 6.9.3
(pp. 258–261, 314–318) independently place intervocalic
*h*-loss after ordinary syncope and Anglian monophthongization.
For ‘see’, they explicitly derive PGmc *sehʷaną* >
PWGmc *sehwan* > *seohan* > *sēon*. Thus the earlier
cluster is not a typo. The frozen full input retains
*xw* and gives *seohwan*; private intervocalic cluster
reduction gives *seoan*, not completed contraction.
Realizing the broken front nucleus with the following
unstressed vowel after *h*-loss gives *sēon*. The same
contraction also serves local *tēo* ‘draw’ subjunctive,
*hēam* ‘high’ dative and *ēa* ‘river’ nominative; it
does not supply the separately required Anglian smoothing
of ‘see’. The local smoothed *sehan* comparison gives
*sēan* with front + back contraction. ‘Draw’ infinitive
already has a successful *tēon* route; it is not an
instance of short *e.i*. Likewise the shoe plural
projection with a broken long nucleus gives *sċēos*,
whereas the frozen earlier trial is not a successful full
inflectional prediction.

For Anglian ‘strike’, an unlowered *slehiþ* can reach
*slēþ* via any matched dental-fricative mechanism after
*h*-loss. If *i* were lowered before *h*-loss, the cascade
would give the same *slēþ* by existing *e.e* contraction.
Ringe–Taylor specifically reconstruct the unlowered form,
and no separate general lowering in this exact environment
was established here. An *i.i* comparison after *h*-loss
contracts in the frozen rules, independently of A/B2’s
earlier final *i.i* operation. These separate pathways
are evidence against using one position as the date of
all contraction. For ‘high’, long *hēhir-* is compatible
with simple absorption after *h*-loss, unlike ‘strike’.

For **‘river’ obliques**, Ringe–Taylor p. 318 and
Campbell §§254–255 leave inherited root-noun *eahi*
(*iehi/ehi* regionally) versus formation to contracted
*ēa* open. The former is a genuine conditional final
short *e.i > ē* counterexample to general final gliding;
neither original oblique quantity nor inherited origin
is independently secure. Both the short direct-collapse
probe and long absorption probe give written *ē*. The
analogy alternative requires a morphological account,
not another hiatus rule. A single later window for some
old *w*-hiatus and new *h*-hiatus remains plausible;
early *streide* and the metrical *strēd* are discriminators,
not automatic proof of a universal intermediate.

Replay the [source-specific receipts](sources-traces.json.gz)
with `bash Germanic/articles/hay/research/hiatus-cycle2/run-container.sh --sources --stage-cache "$cache"`.
