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

## T5: integrated hypotheses and ordering graph

The [stack receipt](stack-traces.json.gz) applies a single
comparison panel on canonical, A and B2. It retains all
stage-local and admitted entries, including complete oblique
cells. Explicit compound-domain lookups are separate; an
ordinary cascade cannot silently erase the research boundary
and still test it. TD replaces only the relevant full ‘hay’
and ‘district’ entries with the separately labelled Dahl
inputs. Its early receipt carries *au > ǣo* before deletion
of nasal *ą*, then branches to the representative English
mid and high outputs before final-palatal loss. This is a
conditional projection at a defined entry point, not a fully
validated early parser or an implementation of analogy.

| Stack | Distinct proposition | Discriminating result in A |
|---|---|---|
| T0 / T1 | Frozen order / S1 only | S1 repairs ‘call’ without adding any hiatus resolution. |
| T2 / T2-late | Direct nonfinal collapse in *d, þ/ð, n* before / after HVD; leave absolute final hiatus in this comparison | Both give *ġecēd* and *strēne*. Only the later implementation preserves the supplied ‘flock’ ending (*ēde* vs. *ēd*); its early suffix remains conditional. |
| T3 | Early consonantal gliding, later narrowed assimilation | *heġ* and nonfinal length; early cluster formation can feed HVD (*ēd*). Palatal identity and later merger create additional predictions absent from T2. |
| T3N | Early nuclear incorporation, later matched merger | *hei* with a single complex nucleus and the same nonfinal lengths; assigned nuclear weight in this implementation likewise feeds HVD. At the edge the orthographic match to H0 is not a phonological match. |
| T4 | Lengthen after final gliding; separately test absorption after a long nucleus | *hēġ* is viable without transfer, but new length needs independent conditioning. Long-root absorption is not a source of short-root lengthening. |
| T5 | Early back-vowel incorporation, late front incorporation and matched nonfinal merger, independent *hw* treatment, and contraction or absorption where later *h*-loss creates a suitable sequence | Keeps *ēde* and *strēne*, and gives *clēa/cnēo/trēo* and *sēon*. It wrongly suppresses the retained-sequence interpretation of early *streide* if applied uniformly to that gloss; it does not produce West Saxon high ‘hay’ directly from short *e.i*. |
| TD | Differentiation of nuclear *au* before nasal loss, mutation before loss of exposed final palatal; protected nuclei retain the consonant | Gives direct *hē* or *hīe*, with protected *hēġes/hīeġes*. Direct written ⟨g⟩ needs restoration in Dahl’s history. The same loss erroneously predicts *cǣ* in the independent ‘key’ control. |

| Edge in the historical graph | Standing and prospective discriminator |
|---|---|
| Raising of final *ō* > early *w*-loss before *u* > back-diphthong realization | Source-supported for the plural histories; Hogg's hiatus and Ringe–Taylor's early nuclear inputs converge. An independently disyllabic form persisting after the early loss would discriminate a longer interval. |
| I-mutation > *w*-loss before weak *i* > general short-vowel syncope > intervocalic *h*-loss | Source-supported relative order, not derived from order of components. The *eowu* class transfer and *gierwan : gierede* are independent comparisons; the fact that *h*-loss creates hiatus later supports, but does not require, a later shared resolution stage. |
| Identical-vowel collapse > unlike-vowel resolution | A serious proposal, not fixed for every environment: identical *glī/nī-* and early unlike *streide* may favour it, but spellings and poetic archaism cannot date all changes. The executable split and the borrowed boundary cases do not prove the edge. |
| Early gliding/incorporation > HVD, or HVD > late resolution | Alternative orders. The former feeds HVD in local ‘flock’; the latter preserves the supplied ending. Confirming the early ending and its quantity could make it a historical discriminator. The unobserved ‘couch’ nominative cannot independently adjudicate it. |
| Consonantal formation > assimilation, or incorporation > monophthongization | Definitional for each serial analysis, not a demonstrated chronology. Early written or metrical preservation of the distinction and independent analogous nuclei could discriminate. |
| Approximant assimilation vs. *ʝ > j* | Inverting these operations changes the ‘rain’ result. Separately dated retention/loss evidence, ideally within the same dialect, is needed before promoting the executable dependency. |
| Nasal apocope vs. Dahl’s *au* differentiation | Reversal changes the input to final exposure; no independent date orders them this way in ‘hay’. ‘Key’ counters the broad absolute loss regardless of the executable order tested. |
| Compound-member exposure vs. compound-medial loss | A separate relation, not inferred from absolute finality. The comparison needs independently inflected or endingless first members and independently motivated compound stress; the charter ⟨hei weg⟩ alone does not provide both. |

### Scholarly limits on unification

Goering’s “A sound change that never was” (first online
2025, print 2026), §8 pp. 313–314 and the discussion of
metrical archaism, separates **postconsonantal** *h*-loss
from **intervocalic** loss and contraction. Heavy poetic
scansion of *feore* can preserve the prosody of historical
*feorhǣ* without requiring ordinary long *fēore*; the limited
southwestern name evidence does not justify a general rule.
Goering likewise contrasts the metrical shapes of *hēan*
at *Beowulf* 713b and 116a. The precedent helps explain why
metrical *strēd* cannot by itself date unlike resolution.
The experimental stack does not use blanket lengthening after
postconsonantal loss.

The abstract and indexed excerpts of de Chene & Anderson
(1979: 505–535, JSTOR 413316) distinguish coda consonant
weakening from nuclear monophthongization and argue that
the decomposition is independently necessary in some
languages. This supports the *possibility* of two steps
without showing that a weak OE vowel became a fricative,
or that the same nucleus formed from a vowel and from newly
vocalized *ʝ*. Kavitskaya’s 2017 critique, as checked in
the joint dossier, also blocks use of prior quantity contrast
as a universal proof. The JSTOR `pdfplus` endpoint returned
HTML, not an inspectable full page copy; Cambridge’s public
record provides an abstract. The publisher preview of de
Chene’s revision identifies the first three chapters with
the 1979 dissertation (one noted change), not the additional
chapters, and does not expose the necessary complete passages.
No prior source-access status is upgraded on that basis.

Mosionek and Zembrzuski (2019 §§2–6), already checked
in the joint dossier, separate phonotactic template matching,
gliding, glide insertion and contraction. *Nerian/lōcian*
are prevocalic, not newly formed word-final *j*. Opalińska’s
original 2002/2004/2006 arguments remain indirect through
these reports; her institutional publications list confirms
the identity of the 2004 article, not access to its argument.
Jordan’s 1974 pp. 120–123 remain inaccessible in the located
controlled-loan edition. Ross–Stanley Book II was not
recovered; the accessible Ross *Studies in the Accidence*
is not that index. None of these limits undermines the
manuscript-verified Aldred ⟨heg/heig⟩ loci or promotes their
spellings into a quantitative census.

The source results motivate **separate historical windows
and one reusable type of syllabicity change**, not one
identical template and merger at every stage. T5 is the
broadest constructive hypothesis for the subsequent audit,
not the winner by endpoint count. Replay:
`bash Germanic/articles/hay/research/hiatus-cycle2/run-container.sh --stacks --stage-cache "$cache"`.
