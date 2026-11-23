# Competing derivations of OE 'hay' (artifact E)

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
  Anglian ⟨heg⟩, Kentish ⟨hei-⟩, and the c. 1150 ⟨hei⟩, all of which are
  equally derivable from the geminate stem.
- Falsifier (satisfied): any WS direct token with ie/i/y vocalism.

## A1 — Early apocope + independently motivated further changes

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

### A1 conclusion

**No independently supported chain takes the early-apocope direct form to
the attested WS *hīeġ*.** The reachable regular endpoints are *hē* (A1-i)
or *hei/hej* (A0/A1-ii), both of which still require the inflected stem to
supply the written -ġ (and, for WS, the entire īe vocalism). A rule
inventing /e/ → /iːe/ lengthening before /j/ would be hay-only and is
rejected. This is a negative result, reported as such.

## A2 — Early apocope + paradigmatic levelling (Ringe–Taylor's actual account)

- Inherited \*hǣwi (= frozen \*hæwi stage) replaced by the protected stem
  \*hēaj- before i-umlaut; thereafter identical to B2: umlaut > \*hīej →
  *hīeġ*, Anglian smoothing > *hēġ*.
- Chronology: replacement must precede i-umlaut to feed WS īe; R&T's ">—"
  sits exactly there (pp. 173, 246).
- Donor status: gen./dat./pl. *hīeġes/hīeġe/hīeġ* are regular **in the
  model** and supported comparatively (OHG *houwi* with levelled geminate
  beside *hewi*). **Cycle-3 revision: the dative cell is now attested** —
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
  *mete/mette* alternations likewise.
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
