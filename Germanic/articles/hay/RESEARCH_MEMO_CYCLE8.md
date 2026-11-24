# Research memorandum — cycle 8 (Fable research cycle)

> **SUPERSEDED (cycle 9).** This memorandum's central negative claim —
> that no loss of \*w before unstressed \*i exists in the handbooks —
> is a source-critical error (R&T 2014: 257–61 §6.7.1 treats the change
> directly; the frozen `OEWLossBeforeI` cites it). The reconstruction
> \*\*hewe, the refutation of the frozen rule, the eowu/cleweþa
> "controls", the obligatory-whole-stem-levelling verdict, the quantity
> argument's basis, and the mene/hay minimal-pair claim are all corrected
> in `RESEARCH_MEMO_CYCLE9.md`. Retained for the research record only.


Scope: the first-principles historical investigation commissioned after
the seven source-preparation cycles. Central question: **did Old English
'hay' require analogy under early nasal apocope?** Answer: **yes — and
the regular alternative now has a definite, excludable shape.**

All page references are to sources held in the project reference
library; formal verification is in `experiments/` (10/10 checks pass).

## 1. Principal finding: the regular direct cell is \*\*hewe

Reconstructed independently from the grammars, with every step secured
by an attested control (full table in DERIVATIONS.md, cycle-8 section):

\*hawją > (early apocope + glide vocalization) \*hawi — this stage is
*attested*: OHG *hewi* is "the inherited nom.-acc. sg." (Ringe & Taylor
2014: 53, 173), beside Gothic *hawi* — > (Anglo-Frisian fronting, which
R&T 5.1.2 show operated before \*w + \*i: \*awi 'ewe', \*klawiþō 'itch')
\*hǣwi > (i-umlaut, w retained: R&T 6.6.2) \*hewi > (final \*-i after a
light syllable retained and weakened, as in *mete*, *stede*, *hete*,
*mene*) \*\*hewe.

The two decisive controls are:

- **eowu 'ewe'** < PGmc \*awiz: the exact minimal pair for \*hawi. R&T
  carry \*awi > \*ǣwi > OE \*ewi with w intact (5.1.2, 6.6.2, 6.9.4);
  Campbell §402 cites "\*aui > OE eowu" as an ungeminated regular form.
- **cleweþa 'itch'** < PNWGmc \*klawiþō (ON kláði): an *attested* OE
  word in which \*-awi- survives as -ewe- (R&T 5.1.2).

\*\*hewe is the structural twin of attested *mene* < \*manją and of OHG
*hewi*. It is unattested in Old English, and no attested spelling of
'hay' (all monosyllabic, all w-less) can continue it.

## 2. Refutation of `OEWLossBeforeI`

The frozen experimental Model A step deleting /w/ before unstressed /i/
has no support in Campbell, Hogg–Fulk or R&T — documented w-loss is
confined to position before \*u/\*ō (Campbell §405; Hogg–Fulk §3.19)
and absolute final position (§§3.17, 4.9, 7.72) — and is positively
contradicted by *eowu* and *cleweþa*. The formal cascade
`experiments/wloss_variant.bin` shows the rule overgenerates: it derives
\*\*ei for 'ewe' and \*\*cleiþa for 'itch'. In addition, Hogg–Fulk
§7.69 (following Colman 1983b) deny that any new /ei̯/ diphthong arose
in OE at all: ⟨dei⟩-type spellings are "merely orthographic variants of
*deġ*". Model A's output /he.i ~ hei̯/ is not an available OE
phonological object. The A1 rescue routes (hiatus resolution,
resyllabification) are thereby moot: their input never arises.

**Production recommendation (not implemented in this cycle):**
`OEWLossBeforeI` must not be promoted into any production cascade in
any form. The frozen SC047 captures, scores and PR #21 are untouched.

## 3. Consequences for the apocope chronology

- **Under early apocope, whole-stem levelling is required** in every
  dialect: the attested record shows only the oblique-stem vocalism
  (WS *hīeġ/hig/hyg*, Angl. *hēġ*, dative *hege*), and R&T's analogical
  replacement \*hǣwi >— \*hēaj- (pp. 173, 246) is forced, not optional.
- **Under late apocope the attested paradigm is regular without
  analogy** (B2), or regular in its vocalism with analogical final -ġ
  only (Dahl's ungeminated variant, which requires the final vowel to
  survive past differentiation and umlaut and is therefore itself a
  late-apocope route).
- 'Hay' therefore moves from "dependent of the debate" (cycle 2–3
  verdict, now superseded) into the same column as *nett*, *bedd*,
  *cynn*: regular only under late apocope.
- **The sharpest new comparative observation:** \*manją 'necklace' and
  \*hawją 'hay' are structurally parallel inputs, and under either
  chronology exactly one of them requires analogy — *mene* preserves
  the regular early-apocope shape (favouring early loss if inherited,
  Stiles 2013) while 'hay' preserves only the oblique shape (favouring
  late loss). The pair is the sharpest known minimal contrast in the
  debate; 'hay' adds genuine weight to the late side without tipping
  the scale alone.

## 4. Quantity resolved at the level of viable derivations

The only regular short-vowel candidate for the direct cell, \*\*hewe,
is excluded by every attested token on surface grounds. Every
derivation compatible with the record — B2, Dahl, early apocope +
levelling — yields a long umlauted nucleus (WS īe, Angl. ē). **The
attested word had a long vowel on all viable accounts.** This
supersedes, in argued form, both the cycle-4 categorical claim and its
cycle-6 withdrawal. Farman's two *hóeg* acutes and the calibration
retain their limited, now corroborative, force; no probability is
asserted.

## 5. West Saxon audit (Hogg's three sources of ⟨ie⟩)

Of the three documented sources of WS ⟨ie⟩ (Hogg 2006: 400; Hogg–Fulk
§§5.49–54, 5.82–84, 5.146–147), only **i-umlaut of a diphthong** is
reachable from the 'hay' etymon. Palatalization of /eː/ requires a
preceding palatal onset (ġ-, ċ-, sċ-), which 'hay' never had. Hiatus
resolution concerns \*ī-e sequences (*sīe*, *hīe* types, §5.146) and
would require a stem-final /iː/ that no viable derivation supplies
before the oblique stem is already in place. WS *hig/hyg* (Lambeth,
CCCC 140) are the regular LWS developments of īe and cannot continue
either \*\*hewe or the refuted \*hei. The Eadwine ⟨hieg⟩ readings
(PPs 71.16, 146.8; fols. 125r, 258r) remain dialect-unassigned; they
are consistent with an īe-tradition spelling but do not locate it.

## 6. Charter verdicts (required verdicts 1–2)

- **S 1196 *cyniges heiweg*** (conv. 859, Cotton Augustus ii.16, s. ix
  med.): **possible, not probable, witness for 'hay'.** Kentish ⟨ei⟩
  for /ej/ (*dei* = *dæġ*) makes ⟨hei⟩ orthographically compatible with
  long *hēġ* 'hay', with *heġe* 'hedge/enclosure' (in composition), and
  indirectly with *hēah* 'high' (though no independent *hēah* > ⟨hei-⟩
  development is demonstrated; the *-stræt* charters S 1338/1361/911
  spell the 'high' element ⟨heah/hæh/heh⟩). Cooper (2003: 61 nn. 151,
  155) suspected the document itself. Decisively for the present
  argument: after cycle 8 the form **cannot be a relic of a regular
  short direct form**, since no such form existed; if it is 'hay' at
  all, it is the ordinary long-vowel compound stem. Its earlier
  potential role as Model-A support is closed.
- **S 328 *Hegforde*** (858): **lexically indeterminate.** ⟨heg⟩ is
  compatible with *hēġ* 'hay' and with *heġ(e)* 'hedge, enclosure';
  nothing in the single attestation or context decides it. It is
  inadmissible as independent evidence for the stem history of 'hay'.

## 7. Eadwine, Farman, and the direct observations

Unchanged from cycle 7 and incorporated as qualifications: the two
Eadwine ⟨hieg⟩ tokens are the only manuscript ⟨hieg⟩ attestations;
normalized *hīeġ* is not a manuscript observation; Farman's calibrated
acutes on *hóeg* are suggestive of his own practice only; the
Lindisfarne readings (Mt 6:30 *heg*, Mt 14:19 *hehg* → *heg*, Jn 6:10
*heig*) and the Paris Psalter datives *hege* ×3 stand as verified.

## 8. The thirteen required verdicts

1. **S 1196 *heiweg***: possible witness for 'hay'; not secure, not
   probable; inadmissible as evidence for a short-vowel relic (§6).
2. **S 328 *Hegforde***: indeterminate between 'hay' and
   'hedge/enclosure'; no evidential weight for stem history (§6).
3. **Model A's \*hei**: not historically defensible. `OEWLossBeforeI`
   is unmotivated and contradicted by *eowu* and *cleweþa*; the regular
   early-apocope outcome is \*\*hewe (§§1–2).
4. **Survival of regular \*hei**: cannot be shown and is no longer even
   compatible with the evidence — the regular form was \*\*hewe, and no
   attested spelling continues it (§1).
5. **Quantity/syllabification**: the attested word had a long umlauted
   nucleus on all viable derivations (§4); direct quantity evidence
   remains probabilistic (Farman's acute) and the ⟨ei⟩ spellings carry
   no quantity information; syllabification of the early non-WS
   spellings (/heːj/ vs /heːi̯/) remains orthographically
   indistinguishable and historically inconsequential.
6. **WS *hig/hyg***: require īe (or ī) — i.e. the i-umlauted diphthongal
   stem of the oblique cells — via the regular LWS developments; they
   cannot continue \*\*hewe or \*hei (§5).
7. **Eadwine ⟨hieg⟩**: the only manuscript ⟨hieg⟩ tokens; consistent
   with an īe-tradition spelling but dialect- and exemplar-unassigned;
   they must not be upgraded into direct West Saxon evidence (§§5, 7).
8. **Mixed paradigm without levelling**: excluded as ancestor of the
   attested record. A mixed \*\*hewe ~ *hīeġes* paradigm, if it ever
   existed, left no trace; the attested paradigm is uniform (PARADIGM.md
   §6).
9. **Where/when/which dialects need analogy under early apocope**: in
   all three attested dialect areas (WS, Anglian, Kentish), replacement
   of the entire direct-cell stem by the oblique stem; datable only to
   before the earliest attestations (8th c.); if the replacement fed
   i-umlaut it predates umlaut, but a post-umlaut wholesale import of
   the umlauted oblique stem is equally sufficient (DERIVATIONS.md).
10. **Discrimination**: 'hay' now positively weighs for late apocope
    (joins *nett/bedd/cynn*) rather than being non-discriminating; it
    does not decide the chronology, because early apocope + levelling
    remains available and *mene* weighs on the other side (§3).
11. **'Bed' and the light neuter ja-stems**: 'hay' is now parallel to
    'bed' in evidential behaviour, with one structural difference —
    'hay''s glide class gives it a late-apocope derivation even without
    gemination (Dahl), whereas 'bed' has none. The \*manją/\*hawją
    minimal pair shows the analogical burden is non-zero under both
    chronologies (§3).
12. **New sound changes or refinements**: no new sound change is
    proposed. One negative refinement is established: no OE or pre-OE
    w-loss before \*i exists, and `OEWLossBeforeI` must be withdrawn
    from consideration (production recommendation, §2). The positive
    refinement is evidential: *eowu* and *cleweþa* are identified as
    the decisive controls for the \*-awi- direct cell.
13. **Central claim of the revised article**: Old English 'hay' had no
    regular monosyllabic direct form; the regular early-apocope outcome
    was disyllabic \*\*hewe (twin of OHG *hewi* and OE *mene*), which
    nothing attested continues. The attested paradigm is either
    original (late apocope) or the product of obligatory whole-stem
    levelling (early apocope); on all viable derivations the word's
    nucleus was long; and together with *mene* the word forms a minimal
    pair demonstrating that neither apocope chronology escapes analogy
    in this class.

## 9. Limitations and open questions

- The apocope chronology itself remains undecided; 'hay' constrains it.
- The Eadwine readings' provenance, the S 1196/S 328 lexical identities,
  and the direct quantity evidence retain the cycle-7 limitations.
- Dal (1934), Wallenberg (1931) and Brooks & Kelly (2013) remain
  outstanding (being acquired separately); Dal could bear on the
  ja-stem levelling typology, Wallenberg on the Kentish place-name
  readings, Brooks & Kelly on the S 1196 document.
- The claim that *mene* is an inherited relic (not remodelled) is
  adopted from Stiles 2013 with his own caution; Boutkan-type
  remodelling remains the standing counter.

## 10. Files, validation, reproduction

- New: `experiments/` (research-only foma cascades + runner + expected
  outcomes; run `bash Germanic/articles/hay/experiments/run_direct_cell.sh`
  with the docker stack up).
- Revised: DERIVATIONS.md (cycle-8 section + supersession notes),
  PARADIGM.md (§6, reconstruction table), QUANTITY_EVIDENCE.md
  (cycle-8 assessment), COMPARATIVE_CONTROLS.md (§4),
  ADVERSARIAL_REVIEW.md (cycle-8 review), UNRESOLVED.md (current
  status), DRAFT.md (substantive rewrite), README.md,
  SOURCE_PREPARATION_HANDOFF.md.
- Production cascades, SC047 captures, benchmark scores, corpus data
  and PR #21: untouched.
