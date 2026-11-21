# SC047 comparative recommendation — retain production, keep open

**Provisionally prefer early loss of both endings for the comparative
history, but retain the production order.** The important positive
evidence is the Continental bed-type singleton **with** its high
ending, not a short spelling in isolation. Early loss derives both
properties by stranding *j*; it also predicts the contrast with
vowel-protected doubling. English directly favours split loss *if*
the doubled direct forms are inherited. The real English obliques
make a common stem extension viable, and the attested direct cells
do not independently establish its direction. *Weti/wetti* gives a
second nonlabial comparison provisionally, not a second confirmed
early singleton until its edition locus and cell are secured. See
the [source audit](../source_integration/source_audit.md) and [cells
and witnesses](paradigms.md).

## Hypotheses at the historical decision

| Proposal | Positive evidence | Contrary evidence or cost | What could decide |
|---|---|---|---|
| **A**: oral and nasal loss, then vocalization and SC010 (Ringe–Taylor pp. 44–47; Campbell §576) | Inherited singleton-plus-high-vowel accounts for OHG *peti*; compare *weti*, the *mene* type and the labially more complex *hewi*. Protected cells readily retain adjacent *j* long enough to double. | Regular English direct *nete, bede, cyne, wede* are not the ordinary attested headwords. Requires class-wide stem extension with real English donors, but no documented transition in those individual direct cells. | Confirm early, independently parsed singleton direct cells contrasting with protected doubled cells in another nonlabial paradigm; or disprove inheritance of the Continental singletons. |
| **B**: oral loss, SC010, nasal loss (Hogg–Fulk §2.23) | English *nett, bedd, wedd* are regular; *cynn* doubles before final simplification. The masculine oral nom. and nasal acc. differ, and direct-case syncretism offers the accusative as donor for *seċġ*. | Needs a distinct regional or independently secondary account of OHG *peti*; no dated English accusative shows the assumed precedence over the remodelled nominative. | An early paradigm with clearly inherited doubled nasal direct and clearly inherited singleton oral direct, in which the doubled form cannot already be explained by transfer. |
| **C**: SC010 before either loss (Boutkan pp. 209–213, 435–436) | Northern *seċġ* and the English doubled neuter direct forms can all be inherited. The Weser *kunni* is evidence for early regional doubling, without a secure direct-cell reading. | Southern `-CC > -Ci`, or replacement by *-i* from heavy stems, needs independent conditioning and timing; Fulk §7.11 n. 5 challenges the linkage to later high apocope. Doubled southern direct forms then need restored stems. The executed C is **only** the northern order proxy. | Independently demonstrate the southern phonological operation or ending transfer, and secure an inherited geminate even in the oral direct cell, before possible transfer. |
| **D**: early denasalization and later deletion | Hollifield II pp. 168–172 supports distinguishing the loss of original nasality, later nasalization in some endings, and actual vowel loss. | Early oralization alone predicts no different response once both endings are short oral *a*. An otherwise identical surviving vowel is not an independent hypothesis. | Show a surviving quality/quantity/prosodic distinction or establish denasalization *after* oral apocope but *before* gemination. No D arm was run. |

The pattern documented for ordinary direct-case syncretism does not
prove the direction of transfer in *seċġ*. Extension of an oblique
stem has positive support as a class pattern and a source of the
forms, not a separate historical event proved for each noun.
Likewise, i-stem reclassification is credible for *mene* and
partial reanalysis for *mettas*, but the specific doubled ancestral
cell remains conjectural. Erdmann's `*-ij-` genitives exclude a
universal geminating donor. *Rīċe* controls vocalization of heavy
`*-ij`, not a light stem eligible for gemination. *Searu–searwes*
supplies a protected alternant for the stranded-*w* comparison,
but does not identify which direct allomorph was inherited or date
nasal loss. No new lexeme or cell is admitted for scoring.

## Reproducible experiment and first divergences

`sc047-followup-9507ce18` pins input identities and the exact
[archive hashes](provenance.json); see the preceding
[source-integration batch](../source_integration/README.md) for full
changed-output stage traces and firing identities. The new round
uses the identical four orders and reproduces every corpus row
and its target, with no rejected or ambiguous rows. Only nine
unscored cells and five local network comparisons were added. One
shared compiler pass dominated the 320-second run (peak 2,243,600
KiB); no routine test compiles this research batch.
`make_plan.py OUTPUT --morphology` emits the user plan
(SHA-256 `ed3f183b2ef4114c4385b45a52e726b1d69a1a53ddd6e2ef4b19f506c8c6f6cf`).
The archived worker adds the helper hashes before pinning that
plan; `export_morphology.py SNAPSHOT` verifies the receipt,
complete archive, and per-arm corpus equality before writing the
diagnostic tables.

| Arm | Complete differences from production |
|---|---|
| Identity | None; all 394 accepted, 386 matches, eight inherited mismatches. |
| A | hay *hēa*, hedge *heġe*, net *nete*, rest *rast*, hue *hii*. |
| B | hay *hewe*, hedge *heġe*, rest *rast*, hue *hiewe*. |
| C, northern order only | hay *hewe*, rest *rast*, hue *hiewe*. |

For the [new cells](diagnostics.tsv), A's first difference is SC047
removing `*-ą` before SC010; SC010 then sees exposed *Cj* and does
not double it. Nuclearization gives *Ci*. B/C show `*nnj/*ddj/*bbj`
at SC010, keep the doubled root through final vocalization, then
delete high *i*. The final simplifier changes *fenn* to *fen*;
singleton *b* in A instead contributes to the later *wefe* outcome.
Genitives/dat. maintain the following vowel and keep the doubles.
The preceding archive includes SC017's same 40 firing IDs, SC112's
same two IDs and input `*dorą` for *door*, and SC111's *strau*
intermediate. *There, where, deer, strew, believe, straw* remain
invariant. Loss in *hedge* first strands oral *j*; *rest* changes
because of final *z* relative to long-ending raising, not nasal
apocope. The *door* result constrains placement of the proxy, not
the historical date of SC112. SC048 and SC059 remain unchanged.

## Hue: fusion is possible, not independently established

In A, `*xíwją > *xíwj > *xíwi > *çíwi > *çíi`; CAPR writes
`hii`. Its late `OEContraction` covers unstressed `*i*i`, not the
short **stressed–unstressed** pair. The archived FII trials give
*hī, glī, nī-* at all three slots: after SC054, after
`OEWeakTailNasalLoss` before late high deletion, and after existing
`OEContraction`. All three could exemplify the same history; their
agreement does not date it more narrowly or license an unrestricted
normalization.

| Mechanism | Local prediction and evidence needed |
|---|---|
| **W-loss, then fusion** | `*íwi > *íi > *ḯ`; a separately established short *í.i* with no *w* also fuses. There is no independent matched native positive in the present record. Stress, length and adjacent segments matter: long/stressed second *i* or intervening *j* does not feed FII. Provisional limit: within the same word, after SC054 produces the short hiatus, before a subsequent operation can remove a member; no evidence for arbitrary boundaries or nonfinal positions. |
| **Length compensation at W-loss** | The broad executable countermodel leaves `*ḯi` at w-loss and would likewise lengthen short *e* before lost *w* in *streide*. Pure one-step compensation that accounts for a monosyllable must also explain disappearance of the following short vowel at that step. Silent final *i* must not be inferred from a spelling alone. |
| **Lengthening and then high-vowel loss** | The same broad model, plus existing high-vowel deletion in a heavy environment, makes `*ḯi > *ḯ` and agrees with fusion for all three positive cases. If lengthening were restricted to homorganic short vowels, the current endpoints would not separate it from fusion. This account requires independently motivated root lengthening before the deletion step, not merely evidence that the deletion can work. |

[Local results](hiatus.tsv) separate the mechanisms formally:
synthetic `*píi` fuses without w-loss; `*píwī` lengthens the root
only under broad compensation and retains its long second vowel;
staged short `*stréwidē` gives `*stréidē` after plain loss versus
`*strḗidē` before deletion and `*strḗdē` after deletion under broad
compensation. The edited Mercian *streide* (Ringe–Taylor
pp. 257–261) positively supports persistence of both vowel qualities
at that point; spelling is not itself a measure of first-vowel
quantity. The *Beowulf* 2436 *strēd* form, with metrical evidence
discussed there, is not the same dated dialect cell. *Pyle* tests
loss of *w* after a consonant without a short stressed adjacent
two-vowel environment, and *sǣ/ǣ* support deletion after an already
long vowel (Campbell §406; Ringe–Taylor p. 259). The local
`*gerwiþi` representation was rejected and is **not** a negative
result; the historical *gierwan–giereþ/gierede* comparison is
source evidence, not a validated local serialization. An
independently dated short-vowel *i.i* precursor, or a recoverable
intermediate with long root and still-present unstressed *i*,
would make the next experiment informative. No new rule is ready.

## Hay: stop at the divergence, not the headword

In the narrow archived A/FWA trial, immediate vocalization gives
`*xáwi`. Blocking premature long-diphthong formation at SC034
recovers Ringe–Taylor's `*hæwi`, followed by mutation `*çewi` and
SC054 `*çei`. CAPR has no later rule that turns short *e.i* into the
long diphthong plus final palatal of *hīeġ*. This locates the
computational gap; it does **not** show that such a rule ever ran.
The separate protected geminate route supplies modelled
*hīeġes/hīeġ*; attested *mid híg* establishes use of the long stem
in an oblique but not a diagnostic overt donor ending or the
direction of transfer. The Notker spellings mix stems across cells.
Inherited *au* (Fulk §§4.10, 6.15) and early stem transfer
(Ringe–Taylor; Campbell §579) therefore remain distinct
possibilities. *Hei* cannot be forced to *hīeġ* by declaring one
of them wrong.

The narrow FWA runs change staged ‘flock’ and preterites of ‘strew’
and ‘call’, leave non-i ‘show’ unchanged, and hold the scored
*hue, strew, believe* and *straw* controls fixed when varied on
their own. This is not authority to move the labial block. FNS
protects **singleton** `Vwj` and `wwj`, so early/FNS is not
immediate vocalization. FNG leaves only the geminated cluster
protected and lets the singleton vocalize. Delaying singleton
vocalization is an additional hypothesis even if endpoints
converge. A narrower SC034 candidate remains experimental: its
feeding environment here was created by the early-loss arm and
its full historical scope is unresolved.

**Disposition:** No changes to SC047, registry, assembly, selected
forms, or canonical sound-change order. Deer remains
`*déuzô → dēora`, with `*déuzą` unscored. The most valuable next
evidence is Dal's original Continental paradigm record, Dahl's
original English cell distribution, and a primary nonlabial
singleton/doublet with independently recoverable quantity and
transfer direction. Prefer B or C over A if those show truly
inherited early doubling in a nasal direct cell (and, for C,
in an eligible oral direct cell) or establish a regular secondary
source of Continental singleton-plus-*i*. Neither the differences
among the match totals nor this research receipt justify a
production change or a new production certificate.
