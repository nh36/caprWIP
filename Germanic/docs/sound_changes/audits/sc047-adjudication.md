# SC047: early low-vowel apocope and its late nasal fragment

The initial pass below remains dated evidence. The corrected-control
follow-up at the end records the disposition after the discrete SC059
adoption; it does not overwrite the original experiments or expectations.

## Identity

- SC047; `OEHeavySyllableNasalApocope` is a stable identifier, not a
  syllable-weight condition or a historical stage.
- 18 November2026; `research/sc047-low-vowel-apocope`; fetched
  `update`/PR18 base `3f2bbd90307e0b4157e8c544da55b1de8f759a93`.
- SC048 is the coordinated immediate interaction. SC045, SC046 and the
  adopted rainbow stress domains remain settled.

## Question

Does SC047 model an independent heavy-syllable OE event, or the nasal
part of the early West Germanic low-vowel loss already discussed under
SC041? Does the current late position follow from historical evidence,
or from the representations consumed by other operations?

Preregistered predictions and falsifiers, including two explicitly corrected
predictions, are in [the source assessment](sc047-sc048-evidence/source-assessment.md).
Output fit is not the historical selection criterion.

## Current state (before any edits)

The registry described an unadjudicated OE/English-specific/A historical
change, “OE Heavy Syllable Nasal Apocope”. Its unchanged operation is:

```foma
define OEHeavySyllableNasalApocope Ctx([
    {*ą} -> 0 || OEAnyConsonant _ .#.
]);
```

It deletes a short unaccented nasal low vowel after any member of the
operative consonant class; that class includes j and w. There is no
syllable-weight test, nor an upstream gate restricting the firings to
heavy stems. Light *þæc* and heavy *horn* both fire. Long, accented,
oral and consonant-protected vowels are distinct controls.

The selected input is PROTOFORM with the canonical sentence-context
sidecar, not necessarily one nominative or one historical stage. There
are394 records,386 matches and eight inherited mismatches. SC041,
SC023/069, SC034/111, SC043, the post-brightening dossier, the accepted
HVD dossier and the retained final-vowel research were consulted. None
of those completed decisions is replaced by an old research packet.

## Diagnosis

### Complete census and provenance

Canonical `SC047 --evidence` rebuilt the stage bins and verified394-row
production/sandbox equality. SC048's census used those same authenticated
fresh bins without a redundant rebuild. All159 SC047 firings have selected
inputs ending in short ą; the immediate result is exactly deletion of
that final symbol. All89 SC048 firings expose the short a of selected
-aną after removal of final ą. No selected secondary à fires there.

The [evidence record](sc047-sc048-evidence/README.md) contains every selected
input, row identifier, immediate before/after, vowel origin, stress/quantity,
downstream checkpoints and endpoint, not just this representative table.
The source assessment distinguishes the encoded stress from an independent
historical reconstruction. The baseline FST digest is
`db0058f211138238c703bfdb75b3e4a95c1d5bfd714e1412a149bbf5c7e8c6c9`;
corpus digest is
`31ef6a72f138a777fc682bfdab41b57ab36dfc3797d567e8e7eb2c3f61a438b1`.
All three immutable snapshots and receipts retain exact context/helper identities.

| Witness; role | Immediately before SC047 | After SC047 | After SC048 |
|---|---|---|---|
| bake1934; live, feeding | `*b*a*k*a*n*ą` | `*b*a*k*a*n` | `*b*a*k*ą*n` |
| bind1950; live, feeding | `*b*í*n*d*a*n*ą` | `*b*í*n*d*a*n` | `*b*í*n*d*ą*n` |
| bast1938; heavy live control | `*b*æ*s*t*ą` | `*b*æ*s*t` | unchanged |
| thatch2245; light live control | `*θ*æ*k*ą` | `*θ*æ*k` | unchanged |
| horn2082; live, earlier u-lowering | `*x*ó*r*n*ą` | `*x*ó*r*n` | unchanged |
| Flask2016; protected long-vowel negative | `*f*l*a*s*k*ō*n` | unchanged | unchanged |

Hay, net and hue reach SC047 with final ją: their current glide handling
is not excluded by the consonant class. The source's stranded-glide
consequences are not thereby implemented correctly: unselected *sarwą*
and *rīkiją* give searw and rīċ, not source searu and rīce, in both
the incumbent and simple moved-loss trials. The sources require glide
nuclearization and paradigm history, not a weight restriction invented
to protect these inputs.

### Counterfactual results

Every trial keeps the same394 selected inputs and unchanged production
targets. Complete output sets and row-level deltas, including rejections
and ambiguity, are archived; aggregate scores alone are insufficient.

- Moving SC047 directly after SC041 changes no selected endpoint.
  Its position after restoration is therefore **not required** by these
  selected traces. Moving SC048 there as well changes seven restoration
  roots because the trigger has become ą; this is a separate change.
- A pre-j-gemination placement changes14 endpoints:12 lose their
  earlier u-lowering trigger; deer exposes z to later final-z loss;
  straw crosses the accepted SC111 pathway. Coordinating the oral-a
  loss and z loss there changes29. These failures do not date the
  historical apocope after gemination.
- After the ordinary final-z-loss checkpoint, deer and door still
  differ: the separate monosyllabic-z operation and final-r lengthening
  remain ahead. The source's historical ordering cannot be read from
  a number attached to one serialized deletion.
  Moving SC047 after rhotacism instead preserves all394 endpoints.
- Before SC023, dōną loses ą while old final-n loss is still active:
  dōn is rejected. This is the established counterfeeding-negative
  relation, not evidence for an independent OE apocope.
- With SC047 between restoration and nasalization, reversing the outer
  operations gives bacen/waden: nasalization saw the still protected n.
  With SC047 before both, the reversed order instead gives bæcan/wædan:
  nasalization sees final n but hides the restoration trigger. The root
  and ending effects are distinct; SC047 itself need not follow SC046.
- A wider early coda-nasal formulation first adds lung's lungan failure.
  Giving nasal ą an ordinary i-mutation consumer recovers lungen.
  The separately tested nasal restoration trigger then recovers the seven
  roots. That coupled candidate equals the full selected baseline, but
  changes more than deletion alone and is not adopted.

The historical87 reversal failures are one reciprocal experiment:
75 plain an/en cases, eight weak ian/ien cases, two h-loss/contraction
interactions and two additional back-mutation interactions. Today's89
contain the same87 plus admitted sow and betray. The old learn spelling
and all original expectations remain intact; no archived result is
silently updated to the present cascade.

## Literature

The [source assessment](sc047-sc048-evidence/source-assessment.md) gives
consultation limits, forms, exact printed pages and source holdings.
Principal directly checked passages are Ringe--Taylor2014 pp.44--48,
152--154,189--194, selected relevant passages of222--252 and319--327;
Fulk2018 pp.79--81,91--92,103,168--172; Campbell1959 pp.85--86,
137--141 and166; and Hogg Phonology pp.62--64,149--157,214--217.
Ringe--Taylor printed153 and Campbell printed138 were image-checked.
Campbell138 is PDF sheet156, not the older assumed sheet154.

Ringe--Taylor44--47 treats oral and nasal short-final low-vowel loss as
West Germanic. Their horn, sarwą/rīkiją, mettas beside mete and OHG beti
arguments connect loss, glide nuclearization and gemination. Fulk91
explicitly makes low-vowel loss independent of preceding weight and
distinguishes subsequent quantitative high-vowel loss. Campbell§331 and
Hogg§§3.27--32 distinguish earlier unprotected loss and later exposed
vowels; neither establishes a new OE heavy-syllable rule.

The held Faulkner author preprint, §§2--3 pp.3--7, documents19,315
infinitives and96.1% written -an. Conservative spelling and manuscript/
editorial dating prevent treating a late -an/-en count as direct
measurement of the prehistoric nasal stage.

Fulk2010 and Goering2016/2023 are reused through the accepted HVD dossier,
not presented as newly read in full. Boutkan and Hollifield are followed
through directly checked handbooks; their originals were unavailable.
Hogg/Fulk Morphology was not obtained; the held misleadingly named volume
is Phonology. Ball/Stiles is indirect through Hogg/Ringe--Taylor; Stiles's
author-deposited abstract, not his full article, was checked. These are
explicit access limitations, not invented original verification.
Fulk25n1 was now checked directly: Frienstedt supplies local z-less,
a-retaining evidence on its interpretation, not a pan-WG completion date.
Runic quantity and inflectional reconstruction remain distinct questions.

## Historical analysis

- **Stage/scope:** the nasal fragment belongs with SC041's early West
  Germanic low-vowel apocope, shared across WGmc with the handbook's
  dialect-continuum qualification. The changed PWGmc/pan-WGmc metadata
  are source-led; confidence B is an independent assessment of chronology
  and representation, not a value derived from those labels.
- **Conditioning:** short unstressed final low vowel, oral or nasal in the
  broader phenomenon, with no preceding-weight condition. This executable
  fragment targets nasal ą after a consonantal symbol. Morphological
  class is not a sound-law condition.
- **Historical bounds:** inherited final-n loss precedes the secondary
  n exposed by apocope; u-lowering precedes the loss for the horn
  history; the source's stranded-glide and gemination evidence places
  the broader low-vowel loss before WG j-gemination. Economical
  z-first ordering is qualified by Ringe--Taylor46, not logically
  compulsory. No secure absolute pan-WG year is established.
- **Executable bounds:** SC023, u-lowering, the accepted straw branch,
  monosyllabic-z loss and final-r lengthening consume representations
  that simple early movement changes. These are not independent dates.
  SC047 must precede the retained final-n proxy if that proxy is to see
  the exposed n; the two87-row cards do not constitute two historical
  demonstrations. The original straw/SC034 bound is superseded by SC111.
- **Analogy:** source-supported ja-stem/i-stem levelling and the guma
  donor cells are recorded, not inserted as a rescue for individual
  trial deltas. There is no analogy needed to delete the159 local vowels.

## Verdict

**REFORMULATE historical identity, label, stage/scope and chronology
claims / RETAIN the deletion and its executable location.**

Registry-verdict: SC047=REFORMULATE/RETAIN

SC047 is not independently motivated as an OE heavy-syllable event.
It is the nasal fragment of the early low-vowel loss whose oral fragment
is SC041. The current location is retained for stability, not because
restoration requires it: the full comparison explicitly disproves that
requirement. A source-shaped earlier joint implementation is executable
but does not by itself resolve the wider glide/ending histories.

## Propagation (only after verdict)

SC047/048 registry rows, inventory notes, affected edge interpretations,
reader chapters, current-state routing and a dated dossier/card addendum
are reconciled. The earlier packet and measurement tables remain historical.
This initial pass left SC059 unchanged and added a bounded reader caveat:
its literal parallel clauses leak the a-trigger to e, so the stelan/wefan
dependency is not independent WS chronology. The joint rainbow restriction
and all secondary annotation companions are preserved.

The associated source-backed input-gate proposal admits genuine unselected
weak-noun cells productively, without admitting them to the lexicon or
changing a sound law. Source notation is not confused with the first
trial's miscoded gúmammiz or NWGmc gúmunų diagnostic. Its exact scope,
full selected comparison and current checks are recorded with the evidence.

Focused regressions cover the current census, light/heavy and protected
negatives, authenticated alternatives and source-backed gate inputs.
They do not launch the research matrix in routine pytest. No selected
input, endpoint, target, ambiguity, rejection or protected baseline changes;
no baseline is refrozen. Final validation receipts certify their actual
source identity separately from these archived experiments.

## Residue

The full source-shaped coda architecture remains a reviewable alternative.
The subsequent discrete SC059 follow-up adopts the previously experimental
strict WS clause separation; see sc059-adjudication.md and
sc059-clause-evidence/README.md. Directly blocked fronting can equal the selected
endpoints without a nasal intermediate. The two relations differ on a
constructed gumanô control, but ô is CAPR's protected-tail carrier,
not the source's literal PWGmc quantity; that difference is not independent
historical falsification of direct blocking. Genuine PGmc gumanǭ gives
gumne, and the newly admitted gumanų gives gumn: the wider cascade does
not yet implement every source paradigm. A successful selected score is
therefore not universal coverage. Full Hogg/Fulk Morphology, Boutkan, Hollifield
and Ball/Stiles originals remain access gaps. No next sound change is
started.

## Corrected-control follow-up: disposition for PR19

### Identity, question and sources

Control commit `d83324ce433f135d6ea58d307555768efe5b4a36` first adopts
SC059 clause separation in a discrete commit. Its FST digest is
`43188e9a8e5bcbd028043675586c6655f81394beba55f0a4bb4044792db4050f`.
The 29 initial trials and their original predictions remain unchanged.
The [follow-up evidence](sc047-sc048-followup-evidence/README.md) contains
the preregistrations, exact definitions/orders, every output set,
all changed records, complete witness prefixes and command receipts.

The falsifiable question was whether prior lowering explains the twelve
root-vowel deltas without late historical apocope, and whether adding
source-supported glide nuclearization makes a general early move adequate.
Sources were read before variants: Ringe--Taylor2014 pp.27--29
§2.3.1(i),44--47 §§3.1.2--3.1.3,152--154 §5.1.2,189--192
§6.3.1 and325--326 §6.9.4; Fulk2018 pp.55--57,91--92,169--171;
Hogg Phonology pp.156--157. Fulk's requested §4.2 (p.55) concerns
closed-syllable shortening; **u-lowering is §4.3**, including the
ordering argument on p.57 n.1. No missing original listed above has
silently become a directly consulted source.

Ringe--Taylor29 contrasts a-stems with root nouns to motivate lowering
before low-final loss;45 explicitly allows prior lowering within the
developing dialect continuum. Their46--47 connects low loss and
postconsonantal j/w/ij nuclearization to pre-gemination history. Their
economical final-z-first analysis is qualified, not a proof of an
absolute pan-WG date. Fulk91 denies a preceding-weight restriction on
this low loss and separates quantitative high-vowel deletion. These
arguments, not a winning endpoint count, establish the historical bounds.

### Actual execution order and all fourteen original deltas

The expanded `EarlyEnglishLineChanges` executes ai-monophthongization,
a-to-u-before-m, long-e lowering, SC023, early-i apocope, final-or
lowering, coronal-w assimilation, ww simplification, ij contraction,
j-gemination, syllabic-j handling, xsC simplification, lþ voicing,
dental hardening and SC111, in that order. Outside the bundle come
i-lowering, SC017, the o-raising rules, ordinary final-z deletion,
word-final-i loss, monosyllabic-z loss, final-r lengthening and
rhotacism. Numerical SC order is not execution order.

Moving SC017 directly after ij contraction crosses gemination,
syllabic-j handling, xsC simplification, lþ voicing, dental hardening,
SC111 and i-lowering. Moving SC047 there additionally crosses the
z/r operations and the intervening brightening, breaking and restoration
region. The archived full order lists identify every crossed operation.
The first representation change in the loss-only trial is deletion of
final short ą at the new SC047 site:

| Row; selected input | Live endpoint | Loss alone before gemination | SC017 then SC047 there |
|---|---|---|---|
|1953 board; búrdą|bord|burd|bord|
|1979 corn; kúrną|corn|curn|corn|
|1988 deer; déuzą|dēor|dēo|dēo|
|1992 door; dúrą|dor|dūr|dōr|
|2026 folk; fúlką|folc|fulc|folc|
|2035 frost; frústą|forst|frust|forst|
|2042 god; gúdą|god|gud|god|
|2043 gold; gúlθą|gold|guld|gold|
|2076 hoard; xúzdą|hord|hurd|hord|
|2082 horn; xúrną|horn|hurn|horn|
|2111 lock; lúką|loc|luc|loc|
|2224 straw; stráwą|strēa|stræw|stræw|
|2265 trough; trúgą|trog|trug|trog|
|2301 word; wúrdą|word|wurd|word|

Twelve changed root vowels lose SC017's nonhigh trigger.
In frost, lost lowering additionally prevents `OERMetathesis`:
live fróst > fórst gives forst, while frúst remains frust.
In deer,
exposed final z survives ordinary final-z deletion but is deleted by
`MonosyllabicFinalZLoss`; live z instead survives until rhotacism,
giving déurą, then dēorą. In door, early apocope separately exposes
stressed final r to `PNWGmcMonosyllabicFinalRLengthening`: dúr becomes
dūr, and recovered dór becomes dōr. The after-ordinary-z trial still
gives dōr for dor, so lowering is not its second dependency.
Live straw has SC111 stráwą > stráu, then `OEAuBrightening` stráeu
and `OEDiphthongLeveling` strēa. Early deletion removes the input
of that accepted route; it is not the obsolete SC034-only test.

There are **thirteen**, not twelve, lost SC017 firings in the loss-only
trial. Yoke2307 additionally loses júką > jóką, but the final
`OEWsPalatalGlide` maps both ġúk and ġók to ġéok, hiding its endpoint
effect. All forty original firings, including Rainbow's secondary
ù, are recovered by moving SC017 alone or before early SC047; there
are no new firings and no conditioning changes. Current acute roots
and the one secondary-stress target are separately identifiable in
the complete census. Gold's earlier consonant is θ rather than the
later d; that representational change does not alter lowering's domain.
Nasal, high-vowel, intervening-j and unmarked-medial controls remain
negative, including source-shaped synthetic knusjanan/trumjanan.

The four-way trial gives identity386/0 changes, loss-only373/14,
lowering-only386/0, and joint384/3. No narrower SC017 prerequisite
repair is called for. After ordinary final-z deletion there remain two
changes (deer/door); after rhotacism or SC041 there are none. Before
SC023 there are fifteen changes including rejection of dōn: the exposed
n is consumed by old final-n loss. This is the established
counterfeeding negative, not evidence for late historical apocope.

### Source-staged glides: gains and unresolved predictions

Ringe--Taylor46 has **rīkiją > rīkī**, with long final ī, not rīki.
The independently staged experiment deletes short ą then nuclearizes
postconsonantal ij > ī, j > i and w > u, in separately composed
clauses. It reaches saru and rīkī before gemination. Rīkī retains
its final long vowel through quantitative high-vowel deletion,
palatalizes k, then shortens and lowers the ending to give rīċe.
Genitive *sagjas (Ringe--Taylor47) retains its medial j and geminates
g > gg; the test does not abolish gemination generally.

The early saru path is **not solved**. Brightening gives særu, which
no longer has rw to trigger breaking; SC046 then restores saru, so
back mutation never sees æ and the endpoint is saru, not searu.
No settled SC046 domain is reopened to repair it. The oral parallel
gelwa > gelu works locally with SC041 plus nuclearization, but its
tested full continuation gives ġielu, not the source's ġeolu. This
is also an unresolved wider-cascade derivation, not an accepted witness.

The full nuclearization candidate has six changed selected endpoints:
deer1988 dēo, door1992 dōr, hay2061 hēa (hīeġ), net2138 nete
(nett), straw2224 stræw, hue2332 hii (hīew). For hay, net and hue,
the first additional divergence is stranded j > i before gemination;
current later syllabic-j handling no longer receives the same input.
Their complete downstream traces are preserved. The three older
dependencies remain: straw's w is postvocalic, outside this
postconsonantal nuclearization, and z/r rules are unchanged.
These changes do not refute early historical loss. The source's
paradigm-levelling argument remains relevant, but no particular
hay/net/hue donor is invented or silently applied to repair this trial.

### Verdict, propagation and residue

**REFORMULATE/RETAIN remains the SC047 verdict.** Retain the current
rule and executable position, with explicitly early historical low loss.
Earlier lowering explains the twelve root-vowel effects but does not
repair the independent final-consonant and SC111 dependencies.
Source-supported nuclearization improves rīkī/rīċe while leaving
searu unresolved and changing three further selected outputs. A general
reorder or glide adoption is therefore not ready; neither source evidence
nor this bounded pass authorizes a z/r or SC111 historical rewrite.

SC059 clause separation is the only adopted production rule change in
this follow-up. No corpus entry, selected cell, target, stress-domain
restriction or baseline is changed. Reader quantity, current prose,
registry notes and chronology qualifications are reconciled; original
measurements remain untouched. SC048's accompanying disposition records
the coda/direct comparison, source cells and analogy donors.

The new tests authenticate frozen compiled observations and complete
row-level delta sets; they add no compiler, fixture or routine sweep.
The opt-in matrices' actual variant/network/time/RSS costs are recorded
in the evidence. Focused A and canonical B precede the final strict C
and book certificate; earlier exact-commit certificates are historical.
Review-ready: SC059's condition correction and these qualified findings.
Experimental: early reordering, glide nuclearization and wider
nasalization/direct blocking. No next sound change is begun.

The first final book attempt found one gloss-gate false positive:
dotted rīċe in the nuclearization discussion repeated the already
glossed rīce 'kingdom'. The prose is unchanged. The existing contextual
shared-gloss table now recognizes only that spelling in that exact
discussion after its glossed lemma, with negative checks for missing
or later anchors, another context, Part II and different quantities.
The failed receipt and pre-repair journal are preserved. This adds
one inexpensive Pandoc regression, not another runtime compiler,
fixture or scientific experiment; a new publication attempt and
the final strict certificate cover the repaired checker.

## Third pass: three source-led decisions on the certified control

### Identity and question

19 November 2026; scientific control634a1335, PR #19, no merge.
The preceding experiments and their original expectations remain historical.
The complete new assessment and exact evidence are in
[three-decision evidence](../literature_dossiers/sc047_three_decisions/README.md).

### Current state and literature

Live SC047 remains159 applications, with no weight filter; SC112 has two.
The original Hogg–Fulk Morphology, Boutkan, Ball–Stiles, Stiles and
Versloot were read alongside the previously held handbooks. The assessment
records pages, notation, paradigm cells and the still-indirect originals.
Hogg–Fulk §2.23 and Boutkan retain a gemination-first nasal-loss alternative;
Ringe–Taylor's early-both-loss analysis is not the only published account.

### Historical analysis and diagnosis

The B–T dative citation resolves to Northumbrian deare in Matthew's
prefatory capitulum LXXIX, Kemble–Hardwick1858 p.19, not Matthew19:11
or a diplomatic WS dēore. A secure WS genitive plural is deora,
Orosius I.1§15, Bosworth1859 p.20.25–27. Propose assembled *déuzôⁿ,
serialized *déuzô, target dēora, headword dēor. It gives dēora in all
seven configurations; source nasality is not separately serialized by ô.
The selected row and frozen baseline are deliberately unchanged.
Internal-z obliques do not prove regular direct-case r retention: in
the early-loss account direct dēor receives r from those obliques.

The unchanged SC112-before-early-loss comparison removes the extra door
firing and restores dor; there/where and all40 lowering identities remain.
This is a demonstrated executable prerequisite, not a strict historical
edge from output agreement. Hill's broader argument and Ringe–Taylor's
deictic/reanalysis alternatives are separately assessed.

Searu now has positively documented analogy from searwes, not an
unexplained historical failure. Ball–Stiles similarly identifies the
geolw- breaking branch for yellow. The direct regular saru/ġielu
branches and their w-bearing donors must remain separate.
Rīkī→rīċe succeeds; sagjas retains medial-j gemination.
Calu succeeds directly; ċealwes is not certified as its correct oblique.
The same-site SC111 aw# companion restores modelled strēa after early
loss, without deriving attested analogical strēaw.

### Counterfactual results

All394 inputs remain accepted/unambiguous in each of seven variants.
Identity/after-SC041386 matches; joint early384; plus earlier SC112385;
plus glides382; SC112+early-loss+aw385; complete glides+aw382.
The exhaustive changed-row union is deer1988,door1992,hay2061,net2138,
straw2224,hue2332. First divergences and full downstream checkpoints
are archived. Early SC047 adds only straw to its159 live firings.
The review-only deer migration would make the complete early trial383,
not386; it is not evidence that the order was historically wrong.
The retained-o dative input-template rejection and invalid hay alias are
preserved separately from the successful selected-corpus comparisons.

### Verdict and propagation

Registry-verdict: SC047=REFORMULATE/RETAIN

Retain body/order and all selections. Propose the genitive-plural cell
for review; do not adopt it silently. Correct the account of the viable
SC112/SC111 components and the source-supported paradigm alternatives.
Update SC047/097/111/112 readers, current registry notes and chronology
interpretations; preserve every older measurement and expectation.
No new strict historical edge, global z/r order, analogy transducer,
SC041/045/046 change, or further SC048/059 change is adopted.

### Residue

Hay/net/hue still distinguish paradigm histories and the alternative
nasal-loss chronologies. Hue's direct contraction and calu's oblique/
dialect history remain incomplete. The retained-o gate gap and the
unheld originals are explicit. The archive's cost review records740
opt-in networks; no routine test cost is added. Final certification is
for the final tree, not inherited from control634a1335.

## Selected deer cell after PR19 (20 November 2026)

The landed comparison at `545ba40ab3fa363249562bc032f7df1c3923dc47`
is the pre-migration reference. Adopt the genitive plural for row 1988
alone; retain *dēor* as the headword and `*déuzą` as the comparative PROTO
and unscored direct-singular diagnostic. Ohthere's partitive *tamra
deora unbebohtra syx hund* in Orosius I.1 §15 (Bosworth 1859, p. 20,
lines 25–27; Cotton Tiberius B.I) attests the oblique. The whole-cell
reconstruction `*déuzôⁿ` combines the stem with Fulk's genitive-plural
ending (2018, pp. 148–149, §7.8); CAPR `*déuzô` represents its trimoric
quantity without separately marking nasality. See the [original
assessment](../literature_dossiers/sc047_three_decisions/source-assessment.md#historical-analysis-deer)
for the source distinctions and original paired traces.

The genitive ending keeps z internal through rhotacism. Early low-vowel
loss in the direct singular instead exposes final z to loss and gives
regular dēo; Ringe and Taylor (2014, pp. 86–87, 174) derive the r of
attested dēor by levelling from inflected forms. Selecting an attested
regular oblique avoids making that proposed levelling a sound change or
presupposing the disputed apocope order. No rule, cascade position, or
other scoreable selection changes. The exact transition preserves the
pre-migration baseline and the immutable original 380; only the active
fingerprints that hash the selected deer cell must change.

## Paired oral/nasal chronology follow-up (20 November 2026)

The [source and experiment matrix](../literature_dossiers/sc047_paired_chronologies/README.md)
compares Ringe–Taylor's early-both-loss order directly with Hogg–Fulk's
oral-first split at the same reconstructed cells. It preserves all
394 output sets per variant, complete SC017/047/112 censuses and
staged extra cells outside scoring. There are 158 live SC047
applications; the experimental placements add straw, not a second
deer entry. No inherited mismatch or production rule changes.

The split order regularly gives nett and bedd; early nasal loss gives
nete and bede but leaves geminated obliques that could supply levelling.
OHG beti and the other comparative relics positively favour early
loss under their inherited analyses, without establishing an OE
direct nete. The matched oral ending of secg predicts ungeminated
seġe in both orders; ende is an attested oral control. The narrow
split-labial test separates genuine gemination from the later need
for palatalized w in hay and hue. Rīċe and searu test vocalization
and independently documented oblique breaking, not the relative
order under dispute. The controls reproduce short dor with unchanged
SC112 early, the there/where applications, and all lowering identities;
they add no historical chronology edge.

**Disposition:** retain the executable position and conditioning.
Reformulate the reader and metadata to distinguish evidence for the
split regular direct cells from evidence for early loss in the
comparative record. Neither establishes a general nasal-loss order
relative to gemination for Old English. Record the competing
falsifiers and representation gaps rather than changing more scored
cells. The deer transition remains the only baseline change, in its
own preceding commit.

## Combined proposal: hedge and rest (21 November 2026)

Correct row 2069 from masculine `*xágjaz` to feminine `*xágjō`, retaining
the normalized target *heġġ* and the `regular` classification. The old
and new canonical derivations both give *heġġ*, but only the feminine
formation agrees with the target evidence. See Kroonen (2013:198), Orel
(2003:150), Kemble III 52.25 and 78.21, and the Bosworth–Toller Supplement
(p. 528). The masculine *hege/heges* obliques remain unexplained by
regular gemination in inherited `*-jai/-jas`; nominative levelling and
reclassification are distinct possibilities, not established events.

Correct row 2152 separately, from genitive `*rástōz` to accusative `*rástǭ`,
retaining *ræste* and comparative `*rastō*. Morris 101.26 attests the
accusative as the direct object of *geearnige*; the proposed genitive is less
secure. The retained `late_analogy` classification addresses possible transfer
to nominative *ræst*, not the regular derivation of the selected accusative.
The genitive remains a long-vowel diagnostic and `*rástōi` remains unadmitted.

The combined migration on the review branch preserves the outputs and
mismatch identities of all 394 rows and archives its common parent baseline.
Neither correction changes a rule or rewrites the frozen historical A/B
selection. No additional compiler call, corpus sweep, rebuilt fixture,
or runtime-concurrency change is added to routine validation.
