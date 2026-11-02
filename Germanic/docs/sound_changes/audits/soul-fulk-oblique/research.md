# Soul: retained medial vowel, oblique syncope and selected-cell research

## Identity

- SC036 (`OEInterStressRaising`), with prospective SC063/SC065/SC066
  implications. This is a separate research memorandum, not a replacement
  registered adjudication.
- Branch: `research/soul-fulk-oblique`; scientific reference:
  `637b30dbfa2455f57f3f467088743d73f8b536b9`, the approved earthly/SC040
  integration. That commit was not an ancestor of `origin/update` when
  the isolated worktree was created.
- Research only. No corpus, registered rule, published lexical selection,
  protected baseline or accepted world/rainbow/earthly history is adopted here.

## Question

Can inherited feminine accusative singular *sáiwalǭ regularly yield
*sāwle*, without a soul-specific medial-vowel change?

Confirmation requires independent ending reconstruction, an actual accusative
attestation, deletion in an open medial syllable under independently
supported prosodic conditions, and complete ending development. It also
requires retaining vowels in independently attested conservative H–L–L
forms. Producing the selected nominative by another convenient rewrite
would not confirm the hypothesis.

The frozen experiment hypotheses are intentionally separable:

1. A: after a heavy initial syllable, a short unstressed medial vowel
   syncopates in an open syllable before a heavy following syllable, not
   before light final *-u*. Apocope does not destroy original H–L–L.
2. B: nonhigh open-medial syncope followed by apocope, then sonorant-adjacent
   insertion. Compare existing insertion with a general, explicitly
   experimental extension to final *l*, never a *wl*-only rule.
3. C: remove the soul proxy alone; then add only the nonhigh heavy-following
   fragment while leaving current apocope and other machinery intact.

The experimental A formulation tests the heavy-initial fragment, not a
claim to implement the entire Old English syncope system. Accent, vowel
length, syllable closure and following weight are phonological conditions;
case and inflection-class labels never occur in its Foma definitions.

## Current state (before any edits)

The live SC036 registry characterization remains Old English,
English-specific, confidence C, `REFORMULATE/REORDER`. The adopted world
component `OELHWeakRaising` and the technical `OESoulProxy` are composed
in `OEInterStressRaising`. The latter changes medial *a* to *u* before
consonants plus *u/ū*, after an earlier vowel; it is not inherited-vowel
retention or syncope.

Selected row2201 is nominative `*sáiwalō`, comparative `PROTO=*sáiwalō`,
target `sāwol`, `DERIVATION_CLASS=regular`. Its documentary classification
does not certify every operation in its history as historical phonology.
It has no pilot/full entry in `report_manifest.tsv`, no row in the scoped
`pgmc_integration/editorial_cases.tsv`, and no mature soul `.model.md`.
The archived dev-note slice is source material, not a published mature
article to overwrite.

Consulted authorities: CURRENT_STATE; the research protocol and companion
template; CONTROL_PLANE; CI_VALIDATION; registered SC036 and SC040 memos
and reader discussion; SC065 and SC066 memos; report schema, reconstruction
README and lexical-integration README. The earlier syncope decisions are
evidence to explain, not permission to silently enlarge those laws.

## Diagnosis

The genuine baseline SC036 evidence command rebuilt the stage bins and
verified all 391 production/sandbox outputs. Exactly two live applications:

| Witness | Before SC036 | After SC036 | Classification |
|---|---|---|---|
| soul2201 | *sāwalu | *sāwulu | Technical proxy; not demonstrated inherited phonology |
| world2302 | *werald | *weruld | Adopted weak initial-LH development; retained |

Soul has technical feeding dependencies on the earlier final-*ō* raising
and *ai* monophthongization, and feeds late SC040. Those dependencies do
not demonstrate an ancient *a > u* law. World requires ordinary grave
removal before its weak-vowel operation. Its accepted *wír-àldiz input
and treatment are not reopened.

Baseline: 391 selected, 383 matching, eight mismatches
(1973, 2013, 2030, 2162, 2224, 2240, 2298, 2300), no ambiguity.
Protected observations:

| Object | SHA256 |
|---|---|
| FST SOURCE | `0d79aeeed03638dbdda051e48bb8b6191ad2f5c395cf4287041f3b01c4216705` |
| Corpus SOURCE | `646de04cec66c13ff00e1d4b8e4d87911a66f92c082496ca86ba95e42b9302b1` |
| Active391 evaluator projection | `efabc1f0512a862f601b651e6409b4e3265a5911b55ce9624b5661e297b8828e` |
| Active original380 projection | `9fb5d393e2f91ad077115593034099851c2d067f5dfefec5859f516a93783597` |
| Immutable380 archive bytes | `fae656520e9ebf446854643907a1ba48a511877fc25b1fae39649d5b97e9a6cf` |

Two preliminary evidence attempts failed honestly on out-of-library
symlinked holdings (first the Colman PDF, then its local extraction).
Read-only hardlinks in real directories remedied containment; the complete
holding-integrity survey then passed and the third evidence command
succeeded. Failed receipts are retained, not relabelled as successful.

### Executable machinery

The physical order, not a historical staging inference from names, is:
early ending changes and diphthong changes; compound linking syncope;
grave removal; SC036; early low-vowel changes; umlaut/back mutation;
SC063 apocope; SC065 narrowly predental *i*-syncope; SC066 *i*-syncope
next to *l*; late long-vowel shortening and unstressed fronting/merger;
SC040; contraction; epenthesis; surface.

SC063 explicitly deletes final high vowels in H–L–L configurations.
That is incompatible with Fulk's early retained *hēafudu* type, even if
it models a later levelled output. SC065 neither targets *a/æ* nor reads
the lost open-medial structure before apocope. SC066 also has a documented
latent problem with heavy originally disyllabic closed nominatives.
The experimental A replacement removes those overlapping post-apocope
*i* operations; that is a diagnostic intervention, not an approved merger.

`OEEpentheticVowel` inserts before final *r* and in final *gl*, not *wl*.
Its back-shift clause mentioning *l* does not itself insert anything.
SC040 lowers *u*, not *a*: it cannot supply the missing justification for
turning retained inherited medial *a* into *u*.

## Literature

### Reading and verification status

The held original PDFs, not only earlier dossiers, were read for Fulk
2010 pp.126–144, Fulk 2022 pp.13–17, Fulk 2018 §§5.4, 5.6, 7.14–15,
Ringe 2017 pp.91–92 and 312, and Ringe–Taylor 2014 pp.55–59, 264–65,
284–89, 299–300 and 330. Handbook OCR was checked against original page
images for Campbell §§341, 353, 363, Brunner §159 and Hogg §6.22.
Luick §§309 and 317 were read in the held text and their original page
images. Fulk's original p.134 and comparative grammar p.155, and Ringe's
original p.312 paradigm were inspected directly: this matters especially
for length and nasalization, which OCR can corrupt. No new autograph
collation or complete concordance is claimed.

Fulk 2022 pp.14–15 rejects obligatory metrical emendation of Exeter
*sawl* to accusative *sawle*. Orthographic *sawl* can represent a
disyllable. His Beowulf four-of-four count includes compound instances
(1406b *sāwollēasne*, 2693a *sāwuldriore*), not four independently
attested nominative tokens; 2820a and 3033b supply simplex instances.
This distinction must survive citation of his aggregate count.
He contrasts 22 secure nonparasiting examples with five parasiting ones
in Beowulf, and absence of parasiting of etymologically nonsyllabic *l*
in the relevant poetic environment. Together with Anglian spellings,
that is positive evidence against a uniformly early monosyllabic
nominative followed by ordinary epenthesis.

Fulk 2010 pp.133–35 shows that syncope is absent before light final
*-u*, not before all *u*: *hālgum* has syncope. Most other inflections
are consonant-closed; surviving vocalic inflections were still heavy.
His p.134 n.15 describes them as trimoric. Fulk 2018 p.87 n.6 makes
the important refinement that ō-stem accusative *-ōn* also blocks
resolution although usually reconstructed bimoric: long unshortened
and trimoric vowels need not be distinguishable in this evidence.
Therefore the present accusative is not silently made trimoric to
fit the analysis. It is nasalized bimoric *-ǭ*, still long at syncope.

Fulk 2022 pp.16–17 applies that prosodic contrast to soul: retained
medial vowel before light nominative *-u*; syncope in obliques. He posits
subsequent extension of the oblique stem into the nominative. His
separate explanation for lost final *-u* in disyllabic *sāwul* is
probable analogy to the other disyllabic feminine nouns, not a new
phonological apocope. He does not demonstrate every intermediate
vowel-quality change in his compressed *saiwalō > sāwulu* statement.

Ringe–Taylor 2014 p.265 explicitly gives the *sāwælu / sāwælǣ*
contrast, syncope, apocope, then epenthesis. Their p.56 already
requires restoration of nominative *-u* after its hypothesized earlier
West Germanic loss. Accordingly their complete nominative account
is not purely phonological either. Page330's independent *fugol*,
*tungol* and *cumbol* establish an insertion phenomenon but not
unrestricted early insertion between *w* and *l*. Their *sēola*
comparison there is explicitly an accusative.

Campbell §§341, 363 and 589.5 and Brunner §159 represent the traditional
syncope–parasiting analysis. Campbell §353 calls retained *hēafodu*
analogical, the opposite evaluation from Fulk 2010's conservative
Mercian evidence. Luick §309's nonhigh-syncope-before-high-loss
argument uses soul itself; §317 describes subsequent sonorant
vocalization. Hogg §6.22 likewise uses the assumed monosyllabic soul
history to establish nonhigh syncope < apocope < high syncope.
That edge cannot independently adjudicate the premise that Fulk
disputes. Fulk's distribution permits HVS/HVA to be considered together
without forcing feeding loss in H–L–L; the present serialization tests
operations, not a new universally established historical ordering.

### Inherited paradigm

These are CAPR combinations of the independently sourced stem and endings,
not quotations of whole accented words printed in the grammars.

| Cell | Inherited form | Regular prediction | Attested outcome | Status |
|---|---|---|---|---|
| Nom.sg. | *sáiwalō | Medial vowel and final *-u* retained in early H–L–L; exact medial quality still requires explanation | *sāwul, sāwol, sāwel, sāwl* | No fully regular route to all nominative variants established |
| Acc.sg. | *sáiwalǭ* (Fulk's *-ōn* notation before final-n loss) | Syncopated stem plus regular *-e*: *sāwle* | *sāwle* | Preferred cell; computational assessment below |
| Gen.sg., Fulk | *sáiwalôz* | Syncopated stem plus *-a*: *sāwla* | *sāwle* | Ending *-e* analogical in Fulk 2018 p.155 |
| Gen.sg., Ringe | *sáiwalōz* | *sāwle* | *sāwle* | Regular only under the alternative bimoric reconstruction |
| Dat.sg. | *sáiwalôi* (trimoric diphthong; Ringe marks its reconstruction uncertain) | *sāwle* through *ē > ǣ > æ > e* | *sāwle* | Independent ending; not the accusative ending |

Ringe 2017 p.312 prints *gebō / gebǭ / gebōz / gebôi (?)*; pp.91–92
distinguish bimoric nasalized *-ǭ* from trimoric nasalized *-ǭ̄*.
Fulk 2018 p.155 independently derives accusative *-ōn* from PIE
*-ām* and explicitly calls its OE *-e* regular. His genitive *-ôz*
and dative *-ôi* are not the same ending. The trimoric circumflex
is quantity notation, not lexical stress. Ordinary CAPR symbols must
not be assumed to implement it faithfully merely because they parse.
The accusative's nominal class is feminine ō-stem; sharing an ending
reflex with a weak n-stem nominative does not make soul an n-stem.

### Independent controls and excluded analogies

Fulk 2010 pp.133–39 and Fulk 2018 pp.92–93 independently establish
retained *hēafudu*, *īdelu*, *eādigu*, *nētenu* versus syncopated
*hēafdes*, *īdlan*, *eādge* and *nētna/nētnum*. Fulk 2018 expressly
prints *īðalō*, *auðagō* and *nautīnō*. The latter's medial long
vowel must be shortened before syncope; a staged *nēatinu* probe
cannot certify that complete inherited derivation. Head has competing
medial-vowel variants already in the comparative evidence; its full
experimental input is a labelled reconstruction, not another corpus row.

The controls test independently sourced phonological states; additional
unattested near-neighbours are explicitly formal negatives, not new
attestations. Closed medial syllables, accented medial vowels and long
medial vowels must be retained. Final *-um* is a positive heavy control,
not a blanket *u*-blocking rule. A separate light-initial *werudu*
probe tests the apocope contrast.

*Calferu/lomberu* have suffix/reconstruction complications; they are
corroborating distributional evidence, not the sole positive control.
West Saxon *hēafdu/īdlu* and retained-medial *nīetenum* cannot all be
treated as conservative regular outputs of one early law. Fulk identifies
opposite analogical levellings and independent changed endings. Feminine
*-iþō* abstracts are also explicitly treated as early stem levelling
by Fulk 2010 pp.140–41 and 2022 p.17 n.18; this research does not
pretend that protecting the current filth output proves its nominative
regular under his analysis.

## Historical analysis

Historical locus: preliterary Old English, with conservative early Mercian
evidence for the retention distribution. Fulk argues for a shared earlier
OE pattern; the directly observed conservative forms are not a licence
to equate late West Saxon outputs with that stage.

There is positive distributional evidence for nominative stem levelling:
early disyllabic behaviour, later securely monosyllabic nominatives,
and an independently syncopated oblique stem. Loss of final *-u* by
analogy is plausible because the retained H–L common-noun feminine was
isolated; this is Fulk's probable explanation, not a documented event
with a datable manuscript innovation. Its evidential strength is lower
than the basic retained-versus-syncopated stem contrast.

Ringe–Taylor's account is inadequate as a uniform explanation of the
early nominative evidence. Later or dialectally different epenthetic
tokens remain possible; the spellings alone cannot distinguish
inherited vowel, syllabic sonorant or insertion. The competing accounts
need not make every individual late *sāwol* token identical in history.

Chronology:

- Umlaut before relevant high-vowel loss: independently demonstrated
  by comparative mutated reflexes (Fulk 2018 §5.6, Hogg §6.23).
- Syncope while the following inherited vocalic inflection remains
  heavy, before its final shortening: independent prosodic requirement,
  supported by Fulk 2010 p.134 and Fulk 2018 p.87; the exact ordering
  of every shortening subprocess remains separate.
- Nonhigh syncope before apocope in the traditional soul account:
  model-local feeding, not independent proof that its nominative passed
  through *sāwlu*. No new canonical edge is adopted.
- Epenthesis after cluster creation: feeding requirement for B; general
  sonorant evidence does not establish early *wl* insertion.
- SC040 lowering after an actual *u*: retained late law, not evidence
  for generating the soul proxy's input vowel.
- No late SC040 foot annotation or temporary prominence computation is
  reused at early syncope. World and earthly are comparisons, not a
  prosodic oracle imported into a different historical stage.

## Verdict

Registry-verdict: SC036=REFORMULATE/REORDER

That line records the unchanged registered verdict. This research's
adoption decision, experiments and residual limitations are reported in
`results.md`; no registry pointer is redirected to this memorandum.

## Propagation (only after verdict)

None authorized. The exact conditional implementation/publication plan
is in `adoption-plan.md`. Research code, source-critical evidence and
experimental receipts alone are committed here. No new SC identity,
selected-input approval or baseline migration is enacted.

## Residue

See the experimental verdict and adoption gates in the companion files.
In particular, retained medial syllabicity is not itself a demonstration
of *a > u*, and a successfully parsed dative spelling is not proof that
the trimoric diphthong has been interpreted correctly.
