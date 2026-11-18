# SC047: early low-vowel apocope and its late nasal fragment

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
