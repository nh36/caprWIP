# SC047: a paired test of early and split low-vowel loss

The paired test starts from `a7099eb55b9ee88550f83b695989a8f688e05b5b`,
after adoption of the deer genitive plural. The selected corpus, target
spellings and contexts are identical in all arms. The extra forms are
research probes, not alternative scored entries.

## What the sources predict

| Published account and passage | Prediction and discriminating evidence |
|---|---|
| Ringe and Taylor (2014), pp. 44–47, §§3.1.2–3.1.3 | In the economical ordering, unstressed final z is lost before oral and nasal short low vowels. Both losses precede j-gemination: light direct `*-Cjaz` and `*-Cją` give `*-Ci` without doubling; protected medial `*-Cjas` keeps j and doubles C where eligible. Stranded postconsonantal `*w` becomes `*u`, and heavy `*-ij` gives `*-ī`. The ungeminated OHG direct *beti* beside *betti* and the OE *mete* : *mettas* contrast are evidence for their early chronology, not attestations of OE *nete*. |
| Hogg and Fulk (2011), pp. 19–22, §§2.20, 2.22–2.24, especially p. 20 §2.23 | Oral nominative `*-az` disappears before gemination; nasal accusative `*-ą` survives into it. They give masculine `*sagjaz > *sagi` against `*sagją > *saggją > *saggi`. On this account the neuter nominative and accusative share the nasal ending and geminate regularly; their light neuter list includes *nett* and *bedd*. Attested masculine nominative *seċġ* is remodelled on its accusative, not evidence that the nominative ending survived. Heavy `*-ij` stems are treated separately and do not diagnose light-stem doubling. |
| Campbell (1959), pp. 229–232, §§576–582 | Both endings disappear before gemination in his ja-stem account; *seċġ* and *cynn* require the geminate of other cells. His protected singular obliques and plurals supply testable donors, not evidence that levelling occurred in every individual word. For hay and hue (§579), he explicitly posits ungeminated direct developments beside the inflected stems and subsequent remodelling. |
| Boutkan (1995), pp. 209–213, 435–436 | He proposes gemination before low apocope, not Hogg and Fulk's oral-first split. His comparative interpretation invokes northern versus southern treatment of final j, likens some apparent ungeminated relics to later i-stem or ending remodelling, and finds the early-loss-plus-levelling analysis unnecessary. The dialect reconstruction and relative ordering are arguments, not directly dated inscriptions. |
| Stiles (2013), pp. 15–16; Versloot (2019), pp. 78–92, especially pp. 79, 86–87 | Stiles's early order uses comparative ungeminated relics such as OE *mene* and OS *(hals-)meni*, against OHG *menni*. Versloot argues for a late Frisian reflex of low endings, with written *-u* potentially representing a reduced vowel. The geographical assignment, reading and morphology of particular runes matter. Frisian reduction and continental z-less forms such as *kaba* qualify a uniform cutoff; neither dates OE nasal apocope against OE j-gemination. |

Original passages were consulted; access and folio identities are in
the [holding record](../../../../../docs/references/sc047_early_apocope/README.md).
The comparative OHG *beti* is a stronger challenge to general late
nasal loss if it is inherited from `*badją`, rather than the result of
subsequent remodelling. Stiles's *mene* has the same interpretive
qualification. Conversely, an early OE nasal direct cell with a geminate
and no independently plausible geminated donor would distinguish the
split chronology much more sharply than *nett* does.

## Implementation and controls

Both paired arms put ordinary final-z deletion and SC041 oral loss
before gemination, with immediate vocalization of oral-stranded glides.
They use the same SC017 lowering, the same SC112 before either loss,
the same stranded-glide relation after nasal loss, and the same SC111
companion for already-endingless *aw*. The only difference between
`early` and `split` is whether SC047 and its consequent glide stage
precede or follow j-gemination. Downstream rules are unchanged.
The early final-z placement is a shared implementation prerequisite
for oral `*-az`, not an adjudication of the whole z/r corridor.

In the matched runs lowering gives `*dorą`, which still has its ending
when SC112 applies. Short *dor* survives. Returning SC112 to its late
site exposes `*dor` and gives *dōr*. All forty SC017 firing identities,
including *horn*, *ġeoc* and the secondary lowering of *regnboga*,
survive. SC112 still lengthens only *there* and *where* (the late-site
negative adds *door*). This constrains the implementation, not the
historical date of SC112; Hill (2017), pp. 142–148, and Ringe and Taylor
(2014), p. 65, give distinct arguments for the two adverbs.

| Configuration | Matches / 394 | Changed outputs from production |
|---|---:|---|
| Production identity | 386 | none |
| Both oral and nasal loss early | 381 | hay, hedge, net, rest, hue |
| Oral early, nasal after gemination | 382 | hay, hedge, rest, hue |
| Split, preserving stranded `*wwj` | 384 | hedge, rest |
| Both early, SC112 left late | 380 | door, hay, hedge, net, rest, hue |
| Previous nasal-only early package, control | 383 | hay, net, hue |

All 394 are accepted with one output in every arm. Live SC047 deletes
158 final nasal vowels after the deer adoption; both prospective orders
add only *straw*, whose vowel otherwise goes at SC111. The added
early-oral component removes the gemination trigger of *hedge*
(`*xágjaz > *xágja > *xágj > *xági`, model *heġe* versus *heġġ*).
This is the same oral input class as *seċġ*, not a nasal-loss difference.
For *rest*, the shared advance of z-deletion exposes `*-ō` in
`*rástōz` before Final Long O Raising rather than after it. This feeds
the wrong ending route (*rast* versus *ræste*) before the two nasal
orders can differ. The selected rest genitive depends on that long
ending remaining protected through raising (Ringe and Taylor 2014,
pp. 299–300); the regression is not evidence that nasal low vowels
survived.

## Diagnostic cells and first divergences

- **Nett.** The first fork is `*natją > *natj > *nati` before gemination
  versus `*natją > *nattją > *nattj > *natti`. Umlaut and later loss of
  i after the now-heavy stem give *nett* in the split arm; the light
  early branch keeps the vowel as *nete*. Both arms give *nettes*,
  *nette*, *nett* (direct plural) and *nettum* under the tested
  ending reconstructions. Dative *nette* is independently attested
  (Bosworth–Toller, [s.v. net](https://bosworthtoller.com/23614),
  Ps. Th. 89.10 and Exod. 74); the other outputs in this matrix are
  not automatically primary attestations. In particular the direct
  plural is a possible identical donor, not a separately established
  transfer. The geminated obliques independently support a source for
  levelling but do not establish when it happened. The alternative
  retained-o `*nátjomiz` of the Hogg–Fulk ending type fails at the
  input gate, not at gemination.
- **Oral controls and bedd.** Both arms lose the oral ending of
  `*sagjaz` before SC010, giving reconstructed *seġe* (not attested
  as this masculine direct case); only the split arm gives geminated
  accusative *seġġ*. The protected `*sagjas` gives *seġġes* in both.
  The attested heavy oral control `*andijaz > *andī > ende` succeeds
  in both. The raw *here* and *yellow* probes fail at the input gate;
  no historical outcome is inferred from them. The earlier staged
  yellow test in the [preceding dossier](../sc047_three_decisions/source-assessment.md#historical-analysis-stranded-glides-and-sc111)
  remains distinct. Nasal `*badją` branches like *nett*, giving
  model *bede* versus *bedd*; `*badjas` gives *beddes* in both. OE
  *bedd* and OHG *beti* are distinct regional evidence, not one
  inconsistent OE target.
- **Hay and hue.** The early arm strips the nasal ending, then makes
  `*xawi` and `*xiwi` before gemination; the split arm first makes
  `*xawwją` and `*xiwwją`. But blindly vocalizing the latter stranded
  j eliminates the conditioning needed by CAPR's later `*wwj` rules,
  giving *hewe* and *hiewe*, not the West Saxon targets. Preserving
  stranded `*wwj` for the existing labial-cluster consumers recovers
  *hīeġ* and *hīew* without moving another sound law. This sensitivity
  arm is a downstream representation test, not a published
  Hogg–Fulk derivation of those two words. Both main arms geminate the
  protected genitives and direct plurals, yielding *hīeġes*, *hīewes*,
  *hīeġ* and *hīew*. Campbell (1959), pp. 46, 230–231, and Ringe and
  Taylor (2014), pp. 53, 173–174, 238, 250, independently supply
  distinct direct and inflected stems; compare OHG *hewi* beside
  *houwi*, and OE *hīwes* beside variant *hīewes*
  ([Bosworth–Toller Supplement, s.v. híw](https://bosworthtoller.com/52596),
  Past. 87.20). The early model outputs *hēa* and *hii* are not
  attested direct outcomes: *hii* stops at the contraction gap after
  w-loss, where Ringe and Taylor have *hī*. The genuine e-input
  alternatives and unresolved interpretation of palatalized w in
  [the hue source ledger](../../../lexeme_reports/model_entries/2332-hue-hīew.source_ledger.md)
  are independent of this ordering test.
- **Rīċe and searu.** Both arms give `*rīkiją > *rīkī > rīċe` and the
  protected genitive *rīċes*. Heavy-stem `*ij` is vocalized before
  later shortening, not doubled as light `*Cj`. Both arms also give
  `*sarwą > *saru` before breaking and reach model *saru*, versus
  *searwes* from protected `*sarwas`. The first within-paradigm
  difference is w-vocalization and hence the absence or presence of
  the breaking trigger. Campbell (1959), pp. 231–232, §§580–582,
  Hogg (2011), p. 92, §5.32(4), and Hogg and Fulk (2011), pp. 22–26,
  §§2.27–2.33, identify the oblique breaking donor and cite
  incompletely levelled relatives. The experimental plural `*sarwō`
  retains `*w` before the reflex `*u` and gives *searw*, whereas
  Campbell has `*sarwō > *sarwu > *saru` before diphthong levelling.
  That unimplemented w/u development is a separate gap shared by both
  arms. Neither *rīċe* nor the singular *searu* alternation requires
  nasal loss specifically before light-stem j-gemination.
- **Deer.** Both prospective orders expose z of `*déuzą` to final
  loss and give *dēo*, since both put SC047 before the later
  root-final-z operation, distinct from the ordinary ending-z loss
  above; neither result independently orders SC047 against SC010.
  The selected `*déuzô` keeps z medial and reaches *dēora* throughout.

## Disposition

*Nett* and *bedd* favour the split account as regular direct-cell
derivations in OE. The surviving geminated donors make early nasal
loss with levelling a historically supported alternative, not a
numerical repair. Comparative ungeminated direct relics support early
loss if their transmission is inherited. Hay and hue depend additionally
on the history of the labial cluster; *rīċe* and *searu* constrain
stranded glides without choosing between the tested orders. The
evidence does not settle a general OE oral/nasal sequence relative to
gemination. Retain the production order, do not add a historical
chronology edge, and do not change another scored cell.

The pinned [plan](plan.json), [complete observations](observations.json.gz)
and [execution provenance](observation-provenance.json) preserve every
selected output, all firing identities and the staged probes. The worker
is the same snapshot worker archived in the
[preceding experiment](../sc047_three_decisions/README.md#reproducible-evidence);
replay its `--capture` against the cited base with this plan and a fresh
backend build. The bounded follow-up compiled 166 finite relations in
310.45 s (maximum RSS 2,243,676 KiB), including one common-definition
image. No runtime compilation or enlarged fixture is added to routine
pytest.
