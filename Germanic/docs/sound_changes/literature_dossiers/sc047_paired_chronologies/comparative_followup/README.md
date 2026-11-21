# SC047: comparative chronology and independent labial questions

## Identity and question

SC047 (`OEHeavySyllableNasalApocope`), interacting with SC041 and
SC010; SC048 and the corrected SC059 remain fixed. Follow-up dated
21 November 2026, based on `489f7d424942cea22844925f599b95c120f4a079`.
The review PR remains open at `1468c4ac0a6b4d4ca4997a28f82e88353f33c7a0`.

If oral and nasal low vowels disappeared early, a light direct `*-Cją`
should give `*-Ci` while an oblique with protected `*-CjV-` should
geminate. If the nasal vowel survived, the same nasal cell should
geminate directly. If both vowels survived, even an oral direct
masculine cell should geminate. A securely inherited direct
singleton plus vowel in a nasal cell would favour early loss; an
inherited direct geminate without an independently supported donor
would favour nasal survival. Separate from this, inherited unstressed
high-front `i` should not cause the same singleton-aw development as
protected `wwj`; and short stressed i plus newly adjacent unstressed
i may resolve to a long stressed nucleus, not a changed spelling.

## Current state

SC047 is historically mapped to Proto-West Germanic in the registry,
with weight-independent final short nasal low-vowel loss; its late
execution slot is not a dating claim. SC041 removes short final oral
`a`; SC048 supplies a different, secondary nasalization pathway.
See the [baseline dossier](../README.md), [labial crossing](../labial_review/README.md),
and [source appendix](sources.md). The 394 fixed selections include
only the approved deer migration; the direct singular of deer is
unscored. No additional diagnostic was admitted.

## Design and diagnosis

The plan uses the archived backend worker. A and B repeat the
earlier experiment exactly. All non-live arms with chronology moves
share the earlier SC017/SC112 serialization and the SC111 companion
for newly endingless `aw`. A and B move ordinary final z loss
(SC020's executable `EAFFinalZDeletion`) before SC041; C performs
that same proxy **after SC010 but before SC041**. Monosyllabic final
z loss and rhotacism are not rewritten. This encodes Boutkan's
northern ordering contrast; it is not a simulation of his entire
absolute chronology, low loss with z still present, southern
`-CC > -Ci`, or final degemination as a new rule.

The additional arms (1) look for stressed i hiatus at two positions,
(2) exclude pre-unstressed-high-front singleton `aw` from the SC034
proxy and check its effect on live production data, and (3) move the
existing labial consumer block as a unit ahead of nasal loss, without
changing its clauses or introducing a terminal-j exception. In the
placement arm, the relevant block starts at SC029 and ends at SC032.
Its component order is preserved, including SC033 and SC110. This is
the published phonological dependency of a geminated input on
subsequent labial processing, tested at an earlier executable
placement; no author is claimed to date the whole executable block
there. Ordinary immediate vocalization and the earlier geminate-only
exception remain separate controls.

### Prospective operation: high-front hiatus resolution

**Experimental identifier:** `FII`, not a registry number.
**Input/output:** short stressed i plus adjacent short unstressed i
within the word gives long stressed ī. CAPR encodes this as
`{*í} {*i} -> {*ḯ}`. There is no lexical condition. No double-stressed,
already-long, nonhomorganic or w-separated input is changed directly.
No new word-internal boundary representation is inferred. The early
test is after i-mutation and SC054's w-loss, before later high-vowel
loss and syncope; the late control is after the existing h-loss
contraction. These placements test ordering consequences, not a
claimed narrow date. Ringe and Taylor §6.7.1 distinguish pre-syncope
w-loss from distinctly later intervocalic h-loss; Hogg §§5.131–134,
pp. 172–175, allows hiatus from either source and analyzes the
lengthening and loss of the unstressed vowel separately. His early
gloss evidence also allows some hiatus to persist. Campbell §406
explicitly distinguishes losing w and later losing i in *sǣ*.
Fulk §4.15 independently discusses contraction following w-loss in
Old Saxon, where the distribution differs by type and poetic usage;
this is comparative support for the mechanism, not a date for the
English change.

Direct hue's `*hī` is reconstructed; *glī* and the combining form
*nī-* are independent continuations with different functions but the
same proposed `*íwi`. Ringe and Taylor pp. 250, 259 give all three.
*Sǣ* is not a second short `ii` case: its long root and heterogeneous
hiatus are useful negative controls. Protected labial *hīew-*, a long
root and a stressed second vowel must not be levelled to *hī* by
the rule. The older h-loss `OEContraction` already contracts
unstressed-token `*i*i`, but not the explicit stressed-root sequence.
That mechanical overlap does not make the two chronology arguments
identical.

**Review wording (not published chapter):** After noninitial w was
lost before unstressed i, a stressed short i could stand directly
before it. West Saxon *glī* ‘joy’ and *nī-* ‘new-’ are consistent with
resolution as long ī; the corresponding direct outcome for ‘hue’ is
reconstructed, not the attested *hīew*. These forms constrain the
result more securely than the date or whether lengthening and loss
were separate operations. The evidence describes a phonological
class, but does not show independently that this particular early
serialization is necessary or that all other comparable hiatus
sequences resolved at that point.

### Singleton aw

In the early direct hay route, SC010 correctly finds no `j` after
nuclearization, and SC029 correctly finds no geminate. The first
incompatible rule is the provisional SC034 singleton-aw proxy:
`*xáwi > *xḗawi`, before ordinary fronting could yield the source's
`*xæwi`. The exclusion test is a narrow negative restriction on
that proxy, not a newly claimed fronting rule and not a rescue of
*hīeġ*. Ringe and Taylor's *awidi*, strew preterite *strawidē*, and
call *gakawidē* histories (§6.7.1 pp. 259–260) provide independent
positive domains for aw before unstressed i without a long initial
`ēa`; *sċēawian* before a non-i suffix is the existing proxy's
independent selected negative control for the exclusion. The
geminate/inherited-au present of *strew* is a different route from
its preterite; its present j remains prevocalic in all arms.

## Executed comparisons

All eleven arms returned one output for each of the same 394 selected
inputs. `identity`, A, B and B with geminate-only protection reproduced
the previous archive row for row. Below, outputs are literal CAPR
orthography; the [full matrix](outputs.tsv) gives each selected input,
target and output, including unchanged mismatches. The
[factor differences](factor-differences.tsv) compare each intervention
with its own control, not just with the live stack.

| Arm | Matches | All changes from the live output |
|---|---:|---|
| Live identity | 386 | None |
| A: both low losses early | 381 | hay `hēa`, hedge `heġe`, net `nete`, rest `rast`, hue `hii` |
| B: oral early, nasal after gemination | 382 | hay `hewe`, hedge `heġe`, rest `rast`, hue `hiewe` |
| C: northern gemination-first proxy | 383 | hay `hewe`, rest `rast`, hue `hiewe` |
| A + contraction directly after w-loss | 381 | A except hue `hī` |
| A + contraction after existing late contraction | 381 | A except hue `hī` |
| A + singleton-aw restriction | 381 | A except hay `hei` |
| Live + singleton-aw restriction | 386 | None |
| B + geminate-only protection | 384 | hedge `heġe`, rest `rast` |
| B + early labial consumers | 382 | believe `ġealīefan`, hedge `heġe`, rest `rast`, straw `strau`, hue `hīe` |
| C + early labial consumers | 383 | believe `ġealīefan`, rest `rast`, straw `strau`, hue `hīe` |

Straw was already an inherited mismatch (`strēa` vs. target
`strēaw`); changing it to `strau` does not cost another point. A
different mismatch is not an equivalence. The other inherited
mismatches, *buck, fire, fowl, rust, tap, wolf,* and *wool*, did
not change. `bed` in the tables below is an unscored diagnostic.

### Apocope and gemination

| Same proto-cell or diagnostic | A | B | C | First meaningful difference and historical interpretation |
|---|---|---|---|---|
| Net and bed, nasal direct `*-Cją` | `nete`, `bede` | `nett`, `bedd` | `nett`, `bedd` | A takes off `ą` and vocalizes `j` before SC010; B/C geminate with `ą` present, then lose `ą`, vocalize terminal `j`, and lose resulting `i` after the heavy syllable. This supports regular direct geminates under B/C. A needs transfer in English, with independently established donors. |
| Protected net and bed forms | `nettes`, `nette`, `nettum`; `beddes`, `bedde` | Same | Same | A also geminates when an ending still protects `j`. `nette`, `beddes`, `bedde` support the donor stem; predicted cells without an edition witness are not new attestations. |
| Man, oral nom. `*ságjaz`; nasal acc. `*ságją`; protected gen. `*ságjas` | `seġe`, `seġe`, `seġġes` | `seġe`, `seġġ`, `seġġes` | `seġġ`, `seġġ`, `seġġes` | In A/B oral loss and nuclearization precede SC010, but C doubles `g` before it loses `z` and `a`. B alone has the nasal accusative as a regular donor for an ungeminated nominative; A needs a protected oblique, C neither. This is an oral control, with a separate nasal comparison. |
| Necklace, proposed nasal `*mánją`; protected `*mánjas` | `mene`, `mennes` | `men`, `mennes` | `men`, `mennes` | A retains singleton plus vowel. Under B/C, SC010 creates `nn`, then high apocope removes `i`; surface spelling gives `men`. A accounts for *mene* without adding a vowel, if the neuter cell is inherited. Neither B nor this limited C arm implements Boutkan’s class transfer. |
| Food, inherited i-stem `*mátiz`; artificial light `*-ją` control | `mete`, `mete` | `mete`, `mett` | `mete`, `mett` | The real i-stem misses SC010 under every chronology. The artificial nasal probe diverges at the same point as net, but does not derive the attested plural *mettas* or establish its source. |
| Heavy `*rīkiją`; `*sárwą` vs. protected searu genitive | `rīċe`; `saru`, `searwes` | Same | Same | None is eligible for light j-gemination. Shared nuclearization gives `*rīkī` and `*saru`; the latter is early enough to miss the model's breaking environment and does not yet give *searu*. The oblique has the independently attested stem vowel. This is a downstream development/levelling question, not a discriminator between A, B and C. |

The [diagnostic appendix](diagnostics.tsv) records all 41 unscored
probes, including the four consistent proto-gate rejections (the
retained-o net dative-plural spelling, *here*, and both *yellow*
probes). No conclusion is drawn from those rejections. *Ende* is
an additional oral control: the arms yield `ende` where live gives
`end`. Neither it nor the nonlabial donors depend on the special
labial factors.

### Final consonants and vowel controls

Each arm retained the same 40 SC017 lowering witnesses and the
same SC112 firings. In A the SC112 input for door is `*dorą`,
not `*dor`; SC047 follows and yields `dor`, while *þǣr* and
*hwǣr* retain lengthening. The archived late-SC112 counter-run
gave `dōr`. These constrain the implementation, not the historical
date of SC112. All chronology arms give unscored singular `dēo`:
SC047 exposes final `z`, which does not rhotacize; selected
`*déuzô → dēora` still has medial `z` at rhotacism. SC111 still
fires on the same corpus row, straw, including in the moved-block
arms; its downstream effect is not invariant.

For hedge, A/B already have `*xágj > *xági` when SC010 arrives;
C doubles before oral loss, then retains the doubled output
`heġġ`. This is the same oral contrast as *secg*, not an extra
nasal-loss witness. For rest, early ordinary final-z loss exposes
`*rástō` to `PNWGmcFinalLongORaising`, giving `*rástu`; live
still has `*rástōz` at that rule and eventually unrounds to
`*rástā`. Restoration and high apocope yield experimental `rast`
instead of live `ræste`. C does not repair that final-z/long-vowel
ordering. Neither defect is repaired by changing the chosen cell.

### Labial results and what they test

**Hay.** A has `*xáwją > *xáwj > *xáwi`, with no geminate.
SC034 first departs from Ringe and Taylor, giving `*xḗawi`
where their account allows `*hæwi`. With the restriction, the
model retains `*xáwi` through SC034, then fronts to `*xæwi`;
mutation and w-loss give `*çewi > *çei > hei`. This recovers a
source-backed **intermediate**, not the selected West Saxon
*hīeġ*, nor an independently attested direct Old English *hei*.
Locally the same restriction suppresses premature long ēa in
staged ‘flock’, ‘strew’ preterite and ‘call’ preterite inputs,
but does not suppress it in the ‘show’ control. Their terminal
outputs are not all attested forms; independent suffix histories
are not being repaired here. In the live comparison SC034
still fires only on the same three ‘show’ rows; no selected
output changes. This is evidence about singleton aw, not a vote
for early nasal loss.

With B, SC010 instead gives `*xáwwją`. Immediate nuclearization
after apocope changes `*xáwwj` to `*xáwwi`, too late to undo
gemination but early enough to block labial resolution; `hewe`
is not the source's singleton route to OHG *hewi*. With
geminate-only protection the first difference is retention of
`j` at that same checkpoint. Resolution, brightening and
levelling give `*xáuj > *xáeuj > *xēaj`; i-mutation gives
`*çīej > hīeġ`. With the consumers moved earlier the same
resolved `*xēaj` is in place by apocope, and FNU does not
vocalize its diphthong-adjacent `j`. The genitive and direct
plural probes already give the geminate-derived stem even in
A. OHG *hewi/houwi* therefore weigh on whether a singleton and a
distinct protected stem were inherited, not on whether OE
*hīeġ* itself must descend from an inherited direct geminate.
The earlier crossed run also showed why delaying singleton `wj`
is a separate hypothesis: geminate-only protection had no effect
under A, whereas delaying nuclearization let A geminate a newly
endingless singleton. The latter cannot be credited to Ringe and
Taylor's immediate-vocalization account.

**Hue.** A gives `*xíwją > *xíwi > *çíwi > *çíi > hii`.
Adding FII is the first difference: `*çíi > *çḯ`, hence `hī`,
at either placement. Both also change direct ‘glee’ and the
‘new’ oral probe from `glii, nii` to `glī, nī`, without changing
protected `glīewes, nīewes`, or `sǣ`. Isolated FII leaves
two stressed vowels, two unstressed vowels, an already-long vowel
and a long second vowel unchanged; after w-loss nonhomorganic
`*éi` is untouched. The double-unstressed pair is handled by a
different existing contraction. The late arm's equal outputs do
not establish historical simultaneity. These are positive
phonological class tests, not grounds to replace *hīew*.

B and C form `*xíwwją`, then FNU feeds `*xíwwi` rather than
the long-diphthong route and the model gives `hiewe`.
Geminate-only protection keeps `j` through labial processing
(`*xíuwj > *xīowj`) and mutation (`*çīewj`), yielding
*hīew*. Early labial placement also gives `*xīowj`, but
apocope then exposes **singleton w plus j**; FNU yields
`*xīowi`, mutation yields `*çīewi`, and SC054 plus high
apocope gives `*çīei > *çīe > hīe`. Moving the block therefore
does not replace protection for hue. Independently supported
protected hue `*xíwjas` yields *hīewes* throughout, showing
the source of a possible transfer without implementing one.

**Strew.** SC010 doubles w in `*stráwjaną` while root j is
prevocalic. The ordinary consumer gives `*stráujan(ą)`;
the Fulk input enters with inherited `au`. Final `ą` can
disappear before or after gemination without stranding that j.
The routes converge by labial resolution and give model
`strīeġan` in every arm, not a newly attested West Saxon
spelling. The Anglian evidence and Fulk's argument against
residual w distinguish hypotheses about the *origin of the
diphthong*, not the date of nasal apocope.

An earlier placement of the entire block cannot be recommended as
a general substitute for geminate protection. The
[companion traces](placement-traces.json.gz) locate two unrelated
changes in both B and C:

- **Believe:** the first changed segmental step is early
  `OEAuBrightening`, followed by `OEDiphthongLeveling`, before
  `OEStressFootContext` can see `*galáubijan`. In the control,
  the foot marker survives root labial processing and permits
  prefix reduction. The moved block presents `*galēabijan` to
  the stress-foot rule; it no longer marks the form. The
  unreduced prefix instead undergoes West Saxon palatal
  diphthongization, giving `ġealīefan` instead of `ġelīefan`.
  This is a prosodic dependency of the implementation, not a
  newly supported date for prefix reduction.
- **Straw:** SC111's companion FW still gives `*stráu` after
  loss. The first missed transformation is SC030's `*stráu >
  *stráeu` because it has already run. SC032 then has nothing
  to level, so the result is `strau` instead of the inherited
  model mismatch `strēa`. No missing geminate or j is involved.

No proposed placement was applied to the live stack.

## Historical assessment and verdict

The comparatively best working hypothesis is early oral **and**
nasal loss with vocalization. Its advantage is the comparative
distribution of simplex-plus-vowel relics, above all OHG *beti*
and the corresponding *hewi* evidence, and Stiles's necklace
comparison, not the selected-citation score. It explains those
shapes without separately requiring southern degemination or an
added i-stem vowel in every singleton. This is a qualified
preference: actual gender/class evidence supports reclassification
in *mene*, and Boutkan's southern treatment is coherent enough
that neither *beti* nor *hewi* can exclude it alone.

For Old English direct cells considered on their own, split loss is
more regular for *nett*, *bedd* and *cynn*: gemination requires
neither an additional chronology assumption nor transfer from the
genitive or dative. These are genuine advantages. Early loss
requires transfer but not an invented donor: *nette* and the
comparative *beddie* are independent evidence of protected stems.
Gemination-first is still more directly regular for *secg*, but
the oral versus nasal ending contrasts of its
paradigm do not prove which stem occupied the prehistoric
nominative. *Mete/mettas* primarily tests whether a model provides
a plausible i-stem reanalysis; because its cells are not all
inherited ja-stems, it cannot outweigh these direct-cell tests.

**RETAIN** the control serialization, **DEFER** an adoption decision
on the apocope–gemination edge, and **DEFER** a new registry identity
for the hiatus operation. The stress-preserving contraction is a
plausible regular process, but the evidence does not yet establish
the distinct early operation's chronology and scope independently
of general hiatus resolution. The SC034 restriction merits a
separate source-led review; the current assay is not that
adjudication. No edge or historical domain is inferred from an
executable identifier or from a rerendered endpoint.

Registry-verdict: SC047=REFORMULATE/RETAIN

**Proposed reader clarification, not applied to the book:** The
light neuters *nett* and *bedd* require no transfer if the nasal
vowel was still present during doubling. Their protected stems
are independently attested, so early loss does not require an
invented source for the same geminates. Comparative Old High
German *beti* and *hewi* strengthen the early-loss interpretation
if their singleton plus vowel is inherited; secondary loss of
doubling or reclassification must be ruled out independently.
Putting oral loss after doubling additionally derives masculine
*seċġ* without transfer, but that form cannot identify the
ancestral nominative stem on its own. The subsequent labial
histories of *hīeġ* and *hīew* do not settle the order, and
contraction in the separate singleton path to reconstructed
*hī* is not the source of attested *hīew*.

## Propagation and residue

Only unscored research evidence and an opt-in harness were added.
No changes to the FST, lexical selections, registry, reader
chapter, book, recurring fixtures or validation execution. No
new exact-commit strict certificate is claimed for this appendix.
The decisive next evidence would be early, dialect- and
cell-specific singleton reflexes with an independently inherited
vowel, geminated English direct cells shown not to have a protected
donor, or a hiatus continuation whose vowel quantity and timing
can be dated independently. Obtain the original Dal/Dahl passages
and check the earliest OHG edition witnesses against their spelling
practices before strengthening the verdict. Sievers's account of
phonological doubling is directly checked but does not supply this
relative date.

## Reproduction and validation cost

On the unchanged Germanic runtime, generate the plan with `make_plan.py`
and pass its output to the `--capture` argument of the [archived
worker](../../sc047_three_decisions/README.md#reproducible-evidence)
with `PYTHONPATH=Germanic/tools`. Place the extracted worker and plan
in the local `.capr-work/sc047-followup/` directory expected by that
worker. No untrusted input is executed; variants are source in the
review plan. Foma runs only in the backend container. Use
`make_plan.py PLAN --placement-trace` for the narrow companion
capture. Use `export_observations.py SNAPSHOT PLACEMENT_SNAPSHOT`
to authenticate the earlier per-row results against the new run
and project the complete corpus and probe outputs. The companion
capture must agree with the primary results row for row before its
straw and believe traces are accepted.

The full compressed observations contain every selected output set,
the named checkpoint traces and full-corpus firing queries. This is
an opt-in snapshot assay, not an added test-suite compile, fixture
extension, sweep or concurrency requirement.

The primary receipt records 1,571 networks in 11 arms, 357 seconds
wall time, of which 333 seconds were common-definition compilation
and 21 seconds the query batch; peak compiler RSS was 2,243,544
KiB. The companion run used 447 networks in five arms, 329
seconds wall time (323 seconds common definitions and 5 seconds
query batch), with peak RSS of 2,247,776 KiB. The primary run
supersedes a missing-alias trial and a trial that defined `FON`
before `FNU`. The companion supersedes a trial that omitted the
worker's required `identity` arm. These are harness errors, not
scientific results. [Provenance](provenance.json) pins the input
and output digests and the runtime completion receipts. Some
research-only files changed in the checkout during execution;
the pinned input hashes identify what was actually run, not a
clean exact-commit production certificate.
