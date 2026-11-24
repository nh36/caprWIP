# Competing derivations of OE 'hay' (artifact E)

> **Cycle 10:** Early apocope regularly gives \*hawi → \*hæwi →
> \*hewi → \*he.i. The recorded \*hē is conditional on contraction;
> its date is not established in final position. The alternative
> \*he.i → \*hej has no independent historical control, and ⟨eg⟩ as
> hiatus is not established. Contraction followed by restoration of /j/
> remains a defensible Anglian account, not an identified historical
> event. See `RESEARCH_MEMO_CYCLE10.md`.

> **Cycle-9 correction (supersedes the cycle-8 section below and the
> cycle-8 supersession notes above it).** Cycle 8's premise that loss of
> \*w before unstressed \*i has no historical support was a
> source-critical error: Ringe & Taylor 2014: 257–61 (§6.7.1) establish
> the change (post-i-umlaut, pre-syncope; positive examples sǣ, ǣ, glī,
> nī-, ēde, pyle, strēn, streide/strēdun, gecnēþ, crēd, gecēd, the
> gierwan-class), with Campbell §§237.1.b, 406, pp. 327–8 and Hogg §5.133
> in agreement; eowu is saved by ō-stem transfer *before* w-loss (R&T
> p. 259) and cleweþa is R&T's own flagged lexical exception (pp. 260–1).
> The recommendation to withdraw the frozen `OEWLossBeforeI` is itself
> withdrawn. The regular early-apocope outcome is **\*hē** (via hiatus
> \*he.i and contraction, R&T 6.9.3 p. 318), not \*\*hewe; Anglian hēġ
> may continue it with only glīg-style -ġ restoration, while WS hīeġ
> requires the oblique vocalism. See `RESEARCH_MEMO_CYCLE9.md` and the
> cycle-9 experiments (14/14 PASS).


All CAPR stage traces below are quoted verbatim from the frozen PR #21
capture `Germanic/docs/models/sc047/captures/sc047-adoption-v1.json.gz`
(commit 113101ac5f169b589e1a9647cdf24d32cdd4d919, read-only worktree
`.capr-work/worktrees/sc047-model-adoption`). Nothing here modifies the
production models. A missing stage in a trace means identity at that stage.

## Shared frozen facts

- Input (both models, all cells): neuter ja-stem \*xáwją; protected cells
  \*xáwjas (gen.), \*xáwjai (dat.), \*xáwjō (nom.acc.pl).
- **Both models derive identical protected forms**: *hīeġes*, *hīeġe*,
  *hīeġ* (pl.) via gemination → \*wwj resolution → \*auj > \*ēaj → i-umlaut
  → īej, with ġ from j-strengthening after the front diphthong.
- The models differ only in when nasal \*-ą is lost relative to gemination.
- Scores (active corpus): A 387/396, B2 388/396 — shared inputs and other
  decisions; **not evidence about this word's history**.
- *Hay* has no verified protected-cell target; its frozen direct comparison
  in A is a visible unresolved mismatch, deliberately not certified
  (PR README).

## A0 — Early apocope, no additional changes (frozen Model A trace)

> **Cycle-8 adjudication: the `OEWLossBeforeI` step is refuted as
> history.** See "Cycle 8 — the regular direct cell established" below.
> The frozen trace remains the accurate record of what the experimental
> Model A computes; its historical interpretation is superseded.

```
SC047ProtoInput                *xáwją
OEHeavySyllableNasalApocope    *xáwj
FNG (stranded-glide vocaliz.)  *xáwi
EAFBrightening                 *xæwi
OEVelarFricativePalatalization *çæwi
OEIUmlaut                      *çewi
OEWLossBeforeI                 *çei
OldEnglishOrthography          hei
```

- Output: /he.i/ — short stressed /e/ + final /i/ (vocalic).
- Chronology: apocope precedes gemination (R&T pp. 44–47); umlaut operates
  on \*hæwi (Ingvaeonic umlaut by lost/retained -i; cf. Stiles 1995 on
  umlaut even by "lost \*-i"); w-loss before unstressed i precedes or feeds
  the final sequence.
- \*çewi matches Campbell's "undisturbed" \*hewi (§579(4)) and R&T's \*hǣwi
  (pre-umlaut æ) exactly; the model simply continues where they stop.
- Predicted spelling: ⟨hei⟩ or ⟨heg⟩ (if final /i~j/ written ⟨g⟩, Hogg
  §2.76 makes ⟨g⟩ for /j/ normal but final ⟨i⟩ possible early).
- Predicted quantity: short e. Predicted inflection: direct cell invariant;
  obliques *hīeġes* etc. — i.e. a **suppletive-looking paradigm**
  hei ~ hīeġes.
- Dialect prediction: identical everywhere (no ēa/īe in the direct cell →
  no WS/Anglian vocalism split).
- **Where it fails**: WS ⟨hieg/hig/hyg⟩ requires īe < \*ēa+umlaut, which
  this derivation never creates in the direct cell; it also predicts
  persistent e-vocalism in WS, against the record. Compatible only with
  Anglian ⟨heg⟩ and Kentish ⟨hei-⟩, which are equally derivable from the
  geminate stem.
- Falsifier (satisfied): any WS direct token with ie/i/y vocalism.
- **Cycle-4 manuscript grounding, qualified in cycle 5**
  (`RESEARCH_MEMO_CYCLE5.md`): S 1196 (conventionally dated 859; Lowe
  gives ?859) carries *cyniges heiweg* on a surviving single sheet,
  Cotton Augustus ii.16, s. ix med. The broader ninth-century Kentish
  charters write *dæġ* as **dei** (OET Ct. 39, 42), and the scribe-7
  corpus has *dei* in S 1195. The S 1196 witness-list form **Deimund**
  is not a secure same-hand control because the list may be a separate
  addition. The corpus lacks a same-scribe long-vowel + palatal-glide
  comparator; ⟨hei⟩ therefore cannot establish quantity or stem identity.
  (ii) The WS failure
  is likewise manuscript-grounded: in Skeat's gospel witnesses *weġ*
  (certified short e + /j/) is written ⟨weg(e)(s)⟩ 31× and never
  ⟨wig/wyg/wieg⟩, while Royal 1 A.xiv's inorganic-⟨g⟩ convention (*hig*
  'they' = hī, *hwig/hwyg* = hwī) attaches to /iː/ — so ⟨hig/hyg/hieg⟩
  'hay' presupposes high front vocalism that /he(.)i~hej/ cannot supply.
  (iii) The "c. 1150 ⟨hei⟩" (WW I.547) is withdrawn as even ambiguous
  support: Worcester F.174 (Tremulous Hand, s. xiii) respells exemplar
  ⟨hig⟩ (WW no. X *Foenum, hig, oðde gærs*) with the same ⟨ei⟩ it uses
  in *Uia, wei* for short *weġ*.

## A1 — Early apocope + independently motivated further changes

> **Cycle-8 adjudication: moot.** Every A1 candidate operates on \*çe.i
> or /hej/, i.e. on the output of `OEWLossBeforeI`. Since that input
> never arises by regular change (see cycle-8 section), the hiatus and
> resyllabification routes have nothing to apply to. The analyses below
> are retained as the record of why they were once live.

Candidate processes examined (each must be independently supported, apply
to /çewi/ or /çei/, and be chronologically possible):

### A1-i. Hogg's hiatus resolution (§§5.129–134)

- Mechanism: after w-loss, \*çe.i is a hiatus sequence; the stressed vowel
  "would be already long, since it occurred finally in a syllable"
  (automatic positional lengthening, §5.129–130) → \*çē.i; resolution of
  long V + **front** V is **loss of the unstressed vowel** (ābst, scōs
  type; diphthongization is confined to back second vowels) → \*çē = *hē*.
- Chronology: possible — hiatus resolution postdates i-umlaut; early
  Mercian glossaries still show unresolved hiatus (CorpGl *strēidæ*).
- Output: *hē*, long vowel, **no final consonant**. To reach attested
  ⟨heg⟩/⟨hēġ⟩ the -ġ must still be imported from the inflected forms —
  precisely Dahl's ending-reintroduction, converging with his \*hē → *heg*.
- Controls: predicts *hē* like *scōs*-type contractions; does not
  overgenerate (w-loss inputs of this shape are rare); but it yields
  nWS-type ē-vocalism only — WS īe remains out of reach.
- Verdict: **chronologically possible, independently motivated, but
  insufficient**: it supplies length, destroys the final segment, cannot
  produce WS īe, and still needs paradigm influence for -ġ.

### A1-ii. Resyllabification /e.i/ > /ei̯/ or /ej/

- OE had no native /ei̯/ diphthong phoneme; a marginal [ej] coda exists in
  *weġ*, *dæġ*. Reinterpreting final /i/ as /j/ (*hej*) is phonetically
  trivial and matches Jones's [hej] for the LOE alternants and the
  ⟨heg⟩/⟨heig⟩ spellings directly.
- But no independent OE change converts the result into /heːj/ or WS
  /hiej/: Minkova's ME merger shows length was neutralized in this
  position, i.e. there was no later lengthening that would be recoverable.
- Verdict: plausible as a low-level reinterpretation; makes A0's output
  compatible with **non-WS** ⟨heg⟩/⟨heig⟩; does nothing for WS īe.

### A1-iii. The *glīg* parallel

- \*gliwą/\*gliwi direct > *glīg* would, if regular, show exactly the
  needed change (w-loss + lengthening + -g). But Campbell calls *glīg* a
  re-formation (§411), and *glēo* (w retained, back reflex) is the
  alternative outcome; the parallel is itself contested and cannot anchor
  an independent rule.

### A1 conclusion — conditional, not a current adjudication

Under the assumptions previously used, the modeled A0/A1 chains do not
produce the normalized West Saxon *hīeġ*: their endpoints are *hē* or
*hei/hej*, and the final -ġ remains unexplained. This does not now
categorically exclude Model A from the attested record. The two
manuscript ⟨hieg⟩ readings are in Eadwine, whose dialect and exemplar
language are unassigned, and the applicability of the several documented
West Saxon ⟨ie⟩ developments to this lexeme has not been established.
The regular development and quantity of the inherited direct form, and
whether hiatus resolution applies, remain for historical adjudication.

## A2 — Early apocope + paradigmatic levelling (Ringe–Taylor's actual account)

- Inherited \*hǣwi (= frozen \*hæwi stage) replaced by the protected stem
  \*hēaj- before i-umlaut; thereafter identical to B2: umlaut > \*hīej →
  *hīeġ*, Anglian smoothing > *hēġ*.
- Chronology: replacement must precede i-umlaut to feed WS īe; R&T's ">—"
  sits exactly there (pp. 173, 246).
- Donor status: gen./dat./pl. *hīeġes/hīeġe/hīeġ* are regular **in the
  model**. OHG *hewi/houwi* is an attested doublet, but the identification
  of *houwi* as a levelled geminate stem beside inherited *hewi* is
  chronology-dependent. **Cycle-3 revision: the dative cell is now attested** —
  Paris Psalter *hege* ×3 (101.4, 101.9, 102.14; ids 33–35,
  manuscript-verified) shows stem + -e, exactly the oblique shape the
  levelled paradigm predicts. But the attestation is eleventh-century,
  in one Saxonized-Anglian poetic tradition, centuries after i-umlaut:
  it confirms that the uniform paradigm existed in historical OE (which
  every account predicts), not that the protected stem was available as
  a donor **before umlaut**, which is when A2's replacement must occur.
  The donor at the required date remains reconstructed; the genitive
  remains unattested at any date.
- Typological support: Hogg 1979's hyll/hyse evidence shows such mixed
  paradigms existed and levelled in both directions; Adamczyk 2018's
  *mete/mette* alternations likewise. Middle Dutch **hoye/houwe** and
  OHG *hewi/houwi* are attested doublets. Boutkan assigns the Middle
  Dutch forms to oblique and old nominative stems (1995: 212–213, after
  van Loon 1986: 48 and Braune–Eggers), but those stem identities and
  directions of levelling are historical analyses, not entailed by the
  forms. The doublets establish comparative variation; they do not
  independently prove levelling in either direction. Levelling is
  typologically possible, not obligatory. The former claim that WS
  ⟨ie⟩ itself demonstrates pre-umlaut levelling is superseded; its
  application depends on the still-unresolved dialect and source of the
  Eadwine readings.
- Predictions: after levelling, identical to B2 in every dialect and cell —
  **A2 and B2 are empirically indistinguishable for this word** except for
  the possibility of unlevelled relic spellings (heg/hei-?) which are
  ambiguous (QUANTITY_EVIDENCE.md §7).
- Falsifier: none available within OE for this word; only comparative
  evidence (OHG *hewi* type) bears on whether the ungeminated cell ever
  existed in English.

## B2 — Later nasal apocope (frozen Model B2 trace)

```
SC047ProtoInput                *xáwją
PWGmcJGemination               *xáwwją
OEHeavySyllableNasalApocope    *xáwwj
OEAwwjResolution               *xáuj
OEAuBrightening                *xáeuj
OEDiphthongLeveling            *xēaj
OEVelarFricativePalatalization *çēaj
OEIUmlaut                      *çīej
OldEnglishOrthography          hīeġ
```

- Output: *hīeġ* — the conventional WS comparison, regular in the direct
  cell with no analogy.
- Chronology: nasal \*-ą survives gemination (Dahl 1938: 81–6; Hogg–Fulk
  §2.23; Boutkan); i-umlaut here is triggered within \*īej by the glide.
- Predictions: WS *hīeġ*, Anglian (smoothed) *hēġ*, uniform stem across the
  paradigm — matches the attested WS and Anglian record without remainder.
- Carrier caveat (PR README): both models share the post-nasal-loss labial
  carrier that preserves only stranded geminated \*wwj; this is a bounded
  implementation, "not a published Hogg–Fulk derivation of those two
  words".
- Falsifier: a secure OE direct-cell token requiring e-vocalism that cannot
  be smoothing (none exists); comparatively, inherited OHG *hewi* if its
  transmission is inherited rather than remodelled (R&T's strongest card).

## Dahl's third route (no gemination in -awj-), for completeness

\*hauja̯ > \*hǣoi(ə) > \*hǣoi > \*hīe/\*hē → *hī(e)g*/*heg* with -g from
\*hī(e)ges. Derives **both** WS and Anglian vocalism without gemination in
this word, at the cost of (i) a special diphthong-differentiation path and
(ii) the same paradigm-imported -g. Note that under this route the A/B2
chronological contrast is moot **for this lexeme**: 'hay' ceases to be a
gemination diagnostic at all.

**Cycle-2 reassessment** (full analysis in DAHL_REASSESSMENT.md): the
differentiation path is not in fact special — granted Dahl's diphthongal
syllabification \*-au̯.ja-, the vocalism uses only the regular \*au > ēa
change and i-umlaut, and from pre-OE \*auj onward his derivation is
segment-for-segment identical with B2's post-resolution stages (and with
R&T's "reversible gemination" \*awj > [aww'] > [auj], p. 53). The route
is conditionally defensible for the vocalism, analogical for the final
consonant by his own statement, compatible with either apocope
chronology, and observationally near-equivalent to B2 within English.

## Cycle-3 comparison of the surviving accounts (deliverable D)

The enlarged record (dative *hege* ×3 manuscript-verified; verse tokens
identified; Farman's acutes calibrated; ⟨hehg⟩ resolved as a corrected
scribal spelling) changes the evidential bookkeeping but not the
standings. What each surviving account predicts, explains, and borrows:

| | A2 (early apocope + levelling) | B2 (late apocope, geminate route) | Dahl (never geminated) |
|---|---|---|---|
| WS *hīeġ*, Anglian *hēġ* | regular **after** the pre-umlaut stem replacement | regular throughout | regular granted the diphthongal parse of \*-awj- |
| Dative *hege* (PPs ×3, new) | regular (the donor cell itself) | regular | regular for the vocalism; final -g analogical by Dahl's own statement |
| Long nucleus (Farman's acute, probabilistic) | predicted | predicted | predicted |
| Analogical step required | whole direct-cell stem, dated before i-umlaut | none for this word | final consonant of the direct cell (any date) |
| Attested support for that step | mixed-paradigm levelling typologically real (Hogg 1979); donor cell now attested, but only centuries post-umlaut | — | final -g restoration repeated in this class (glīg etc.) |
| What would falsify it within OE | nothing identified | a secure direct-cell token requiring non-smoothing e-vocalism (none) | a secure w-form of an OE \*-awj- noun (none found) |

The new dative tokens are compatible with all three accounts and are
therefore **non-discriminating**: every account predicts *hēġe/hege* as
the historical dative. Their real contribution is negative-critical —
they retire the cycle-1/2 claim that the analogical donor was a
paradigm cell never observed in any Old English text, while leaving
intact the sharper point that no attestation dates the levelled oblique
stem early enough to serve A2's pre-umlaut replacement. The word
remains, as cycle 2 concluded, a dependent of the chronology debate and
not a witness in it; the scores of the frozen models (387/396 vs
388/396) remain formal controls, not historical evidence.

## Control words (frozen capture, direct cells)

| Lexeme | Input | A output | B2 output | Attested | Favors |
|---|---|---|---|---|---|
| net | \*nátją | *nete* | *nett* | *nett* (Li Lk 5.6 nom.) | B2 |
| bed | \*bádją | *bede* | *bedd* | *bedd* | B2 |
| kin | \*kúnją | *cyne* | *cyn* | *cynn* | B2 |
| hue | \*xíwją | *hī* | *hīew* | *hīew/hīw* | B2 |
| end (heavy control) | \*ándijaz | *ende* | *ende* | *ende* | both |

(*Hedge* was tested only in the earlier dossier arms, where the added
early-**oral** component gives model *heġe* against production *heġġ* —
an oral \*-az effect shared by both adopted models, not a nasal-order
diagnostic.)

The light neuter direct cells (*nett*, *bedd*, *cynn*) are regular only
under B2; under A they require the same levelling story as 'hay'
(dossier disposition: "*Nett* and *bedd* favour the split account").
Comparative ungeminated relics (OHG *hewi*, *beti*; OE *mene*, OS
*(hals-)meni* — Stiles 2013) support early loss **if inherited**.

## Cycle 8 — the regular direct cell established (first-principles reconstruction)

Cycle 8 re-derived the direct cell from the grammars without assuming any
prior CAPR adjudication. The result is a positive finding: under early
nasal apocope the regular Old English continuation of the direct cell is
the disyllabic, w-retaining form **\*\*hewe**, secured segment by segment
by independently attested minimal-pair controls. Neither \*hei nor any
monosyllabic form can be reached by regular change from \*hawi.

### Stage-by-stage, with controls

Starting point: PWGmc nom.acc.sg. \*hawi. This stage is not reconstructed
from theory alone — it is **attested as OHG hewi** (R&T p. 53 and p. 173:
"OHG hewi — the inherited nom.-acc. sg. — and houwi, with gemination
levelled in from the oblique forms"), and Gothic *hawi* shows the same
consonantal parse. Under early apocope the pre-OE direct cell is this
form.

| Stage | Form | Control securing the step |
|---|---|---|
| PWGmc after apocope | \*hawi | OHG *hewi*, Goth. *hawi* (consonantal w, syllabic -i) |
| Anglo-Frisian fronting before \*wi | \*hǣwi | R&T 5.1.2: "fronting occurred before \*w which was followed by \*i": \*awi > \*ǣwi ('ewe'), \*klawiþō > \*klǣwiþa ('itch') |
| i-umlaut (æ > e), **w retained** | \*hewi | R&T 6.6.2: \*ǣwi > OE \*ewi → *eowu*; \*klǣwiþa > OE \*klewiþa > **cleweþa** 'itch' (attested) |
| No diphthongization before \*wi | \*hewi | R&T p. 203 (6.2.4): "this diphthongization did not occur by regular sound change before the sequences \*wi and \*wī" |
| Final \*-i after a light syllable retained, weakened to -e | **\*\*hewe** | *mete* < \*mati, *stede* < \*stadi, *hete* < \*hati, *ege*, *slege*, *here* (R&T 6.6.2); crucially **mene** < \*mani < \*manją — the same early-apocope relic class (Stiles 2013) |

### Why `OEWLossBeforeI` is refuted

The frozen Model A step deletes /w/ before unstressed /i/. No such change
exists in the handbooks, and two words directly contradict it:

1. **eowu 'ewe'** < PGmc \*awiz: R&T carry \*awi > \*ǣwi > OE \*ewi with
   w retained at every stage (5.1.2, 6.6.2, 6.9.4); the attested back
   vocalism comes from the later morphological shift into the ō-stems
   (\*ewi → \*ewu > eowu). Pre-OE \*awi is the **exact minimal pair** for
   \*hawi — identical string but for the initial consonant.
2. **cleweþa 'itch'** < PNWGmc \*klawiþō (ON kláði): an *attested* OE
   word in which \*-awi- survives as -ewe- with the w intact (R&T 5.1.2).

Supporting evidence: documented w-loss environments are confined to
w before \*u/\*ō (Campbell §405; Hogg–Fulk §3.19: clēa, cnēo, þrēa) and
to absolute final position after a vowel (Hogg–Fulk §§3.17, 4.9, 7.72);
WS verb alternations *crāwan* : *crǣwþ*, *oncnāwan* : *oncnǣwst* show
w intact before umlaut-triggering \*i in exactly the relevant position
(R&T 6.6.3). There is no OE rule deleting intervocalic w before i.

Additionally, Hogg–Fulk §7.69 (following Colman) deny that any new /ei̯/
diphthong ever arose in OE: ⟨dei⟩-type spellings are "merely orthographic
variants of deġ", and vocalization of /j/ is real only after /i(ː)/
(§7.70). The A0 output /he.i/~/hei̯/ is thus not even an available OE
phonological object.

### Why the diphthongal rescue is unavailable under early apocope

Dahl's route (and R&T's "reversible gemination" \*[aww'] > \*[auj], p. 53)
nuclearizes the w — but only in cells where \*j follows (\*hawj-V, the
oblique cells). Under early apocope the direct cell has already become
\*hawi (onset w before syllabic i) **before** gemination, as R&T's own
ordering requires; OHG *hewi* attests exactly that shape, and *eowu*/
*cleweþa* fix its pre-OE development. The diphthongal parse therefore
rescues the direct cell only if the final vowel survives long enough for
the \*-awj- > \*-auj- nucleus to arise there too — i.e. only under late
apocope, where it converges with B2 (DAHL_REASSESSMENT.md §4).

### Consequences

1. **Regular early-apocope outcome: \*\*hewe** — disyllabic, short e,
   w retained; the exact structural twin of attested *mene* and of OHG
   *hewi*. It is unattested in Old English and cannot underlie any
   attested spelling of 'hay' (all are monosyllabic and w-less).
2. **Therefore, under early apocope, analogy is required** — and not the
   one-segment -ġ restoration, but replacement of the whole direct-cell
   stem by the oblique \*hēaj-/hīeġ- stem, in every dialect (WS, Anglian,
   Kentish alike show the oblique-stem vocalism). This is exactly R&T's
   ">—" (pp. 173, 246); cycle 8 shows the replacement is forced, not
   optional.
3. **Under late apocope (B2) the attested paradigm is regular without
   analogy**; Dahl's variant is a late-apocope route differing only in
   denying gemination and borrowing final -ġ.
4. **'Hay' therefore patterns with *nett*, *bedd*, *cynn***: regular only
   under late apocope, an analogical liability under early apocope. It
   is no longer a neutral "dependent of the chronology debate" (cycle-3
   formulation, now superseded): it adds one more whole-stem levelling,
   in all dialects, to the cost of the early chronology — while remaining
   compatible with early apocope *plus* levelling, as 'bed' is.
5. **Quantity resolved at the level of viable derivations**: the only
   regular short-vowel candidate, \*\*hewe, is excluded by every attested
   spelling. Every derivation consistent with the record (B2, Dahl, A2
   levelling) yields a long umlauted nucleus (WS īe, Angl. ē). The
   cycle-6 withdrawal of "all viable routes predict length" is itself
   superseded in this sharpened, argued form.
6. **Production recommendation (separate from this research)**: the
   experimental Model A rule `OEWLossBeforeI` should not be promoted in
   any form; it is contradicted by *eowu* and *cleweþa* and unsupported
   in the literature. No production change is made in this cycle.

Formal verification of these chains against the controls is in
`experiments/` (research-only cascade; see experiments/README.md).
