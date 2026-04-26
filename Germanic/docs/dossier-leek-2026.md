# Dossier: OE *lēac/lēc* 'leek' — testing the *raukaz* model on *laukaz* (2026)

**Scope.** Companion to `dossier-reek-2026.md`. The user proposes that the OE
treatment of *laukaz* 'leek' parallels that of *raukaz* 'smoke': a-stem +
Anglian smoothing, with the smoothed Anglian form ultimately winning out into
ModE (*leek* /liːk/, like *reek* /riːk/, both monophthongal and velar).

Three open questions are addressed:
- §2 — Is *lēc* documented as an Anglian loan into late WS?
- §3 — Where does smoothing sit in the chronology relative to palatalisation
  and i-umlaut? (Quote-driven; this is the empirically critical section.)
- §4 — Does paradigm contamination supply or reinforce velar [k]?

§1 establishes the concrete TSV/FST status. §5 synthesises. §6 gives a
recommendation. §7 lists open questions.

---

## §1  Status of *lēac/lēc* in TSV and FST

### §1.1  TSV row

`Germanic/data/germanic-aligned-final.tsv` line 646 (concept ID 215, COGID 147):
`2097  l ē a c  *láukaz  l iː k (- -)  liːk  lēac  Old_English … *láukaz  147`.
PROTOFORM `*láukaz` (a-stem). Target token `l ē a c` = *lēac*. Counterpart
IPA `liːk` is the ModE pronunciation. Sibling rows in cog-set 147: 644 Du.
`l uː k`, 645 Eng. `l iː k`, 647 Ger. `l au x`, all on `*láukaz`. **Already
aligned on a-stem proto** — no `*laukiz` i-stem ambiguity. Contrast row 2151
for *rēc*, which had `*ráukiz` and required rewriting per dossier-reek-2026.

### §1.2  FST probe

```
$ docker compose exec -T backend bash -lc 'echo laukaz | flookup -i /usr/app/old_english.bin'
laukaz   lēac

$ … 'echo laukiz | …'      → līeċ
$ … 'echo lauk | …'        → lēac
```

**The FST already produces *lēac* from `*laukaz`** — agreeing exactly with
the TSV target. So at the surface-comparison level, **this row is not
currently a mismatch**.

### §1.3  Where the ModE constraint pinches

ModE row 645 has /liːk/ (velar monophthong); the OE row has *lēac* (diphthong).
Either (i) ModE *leek* continues Anglian-smoothed *lēc*, with WS *lēac* a
co-form, or (ii) ModE /iːk/ derives from WS *lēac* via early-ME ēa→ē
(Jordan §82). Both pathways are real (§2). *lēac* is securely attested in WS
(BT 97864, Clark Hall 25515); *léc* is also attested incl. in late-WS Ælfric
(BT 98090, Clark Hall 25647). Per project ethos, either OE form is defensible
as a target. See §6.

---

## §2  Anglian-loan-into-WS hypothesis (Q1)

### §2.1  Lexicographic distribution of *lēac* vs *lēc*

**Bosworth-Toller** has separate entries: `leác` (BT 97864) "Laec ambila…
Leác alium… He leác sette he planted vegetables, Shrn. 61, 20"; `léc` (BT
98090) "Hwæt secge ic be eágum mínum þá mê mid lêce forhwyrfdon… Hml. S. 31,
296" (Ælfric, late WS!). Compounds: `gar-leác` ~ `gârlęc, -lec` (BT 46532);
`brade-leúc` ~ `brade-, -leác, -léc` (BT 16889); `cipe-leác` (BT 20433);
`crop-lēac / -lēc` (Clark Hall 9719). Clark Hall 25515 records all three
shapes under one lemma: "**lẽac I. (æ, ē, ēo) n. 'leek'**". **Both forms are
attested pan-dialectally**; *lēc* is not exclusively Anglian in the surviving
record.

### §2.2  Campbell §225 — the canonical statement

> "The smoothing of éa has still not taken place in a number of forms preserved
> in Ep.: léag lye, fléah flea, géacaes- g.s. cuckoo, téac tye, and in the
> second element of compounds, **-béacn** beacon, -béag ring, **-léac leek**.
> Smoothing to æ appears in **æc** also, **-bæcon** beacon, **læc** leek, and
> the further stage é in **égan** eyes. **Cp. has smoothing always, except
> -léac, 965**, most forms having æ, but é also occurring in a few instances:
> **-léec, -bécn** (also -bénc), égan. … In VP and Ru.1, smoothing of éa is
> practically universal, appearing as é …"  — Campbell §225 (1959, p. 95)

Trajectory in the early-Anglian glossaries: *-léac* (Epinal, unsmoothed) →
*-læc* (Corpus, Erfurt; first-stage smoothing to æ) → *-léc* (Corpus
sporadically, VPs, Ru.1, BC, LR; final stage). The Anglian *lēc* propagates
pan-dialectally for high-frequency lexemes, paralleling *bēcen* in some WS
manuscripts. **Campbell does not flag *lēc* specifically as a "loan into
WS"** — he treats it as the natural Anglian form competing orthographically
with WS *lēac*. Late-WS *léc* in Ælfric (BT 98090) is straightforwardly the
pan-dialectal smoothed variant by late OE.

### §2.3  Toon (Cambridge History vol. 1, ch. 6)

Toon (in Hogg vol. 1, lines 19660–21240) treats smoothing as the most robust
diagnostic of Mercian/Northumbrian origin (table p. 416: smoothing `+` for
Anglian, `-` for WS) and traces its wave-like spread through the early
manuscripts (EpGl ca700 → ErfGl ca750 → CorpGl ca800 → VPs ca825). Toon does
not assert "*lēc* is an Anglian *loan* into WS" in the technical lexical-
borrowing sense; the accurate description is that **the Anglian smoothed form
*lēc* spread pan-dialectally** during the OE period, surviving alongside
*lēac* and ultimately out-competing it (giving ModE *leek* via ME *lek(e)*).

### §2.4  Bēacen vs. lēc — divergent outcomes

The cleanest internal control is *bēacen*:

| Lexeme   | WS form    | Anglian form | ModE      | Whose form won out?  |
|----------|-----------|--------------|-----------|----------------------|
| 'beacon' | bēacen    | bēcen        | beacon    | **WS** (literary survival) |
| 'leek'   | lēac      | lēc          | leek      | **Anglian** (everyday lexeme) |

The asymmetry is sociolinguistic: the everyday vegetable *lēc* survived as
the rural/Anglian form; the literary *bēacen* survived as the WS scribal
form. Both pathways are documented (Campbell §225, Hogg p. 416, Toon 1983).
**The ModE constraint that the etymon was velar [k] selects the smoothed-
Anglian-pathway form for the ModE-witnessed lexeme**; WS *lēac* is preserved
as a parallel co-form.

### §2.5  Verdict on Q1

The "*lēc* is an Anglian loan into WS" framing is **partially right but
needs sharpening**: *lēc* is not strictly a *borrowing* into WS in the sense
*cirice* is borrowed from Greek; it is the **Anglian form that diffused
pan-dialectally** during the OE period (Campbell §225), already attested in
late-WS Ælfric (BT 98090). The handbooks call it the "smoothed form" that
became increasingly the norm, not a "loan". For TSV/FST purposes, this is a
distinction without a difference: the OE form ancestral to ModE is *lēc*, and
the OE form preserved in WS is *lēac*. Both are real OE.

---

## §3  Smoothing chronology (Q2) — verbatim handbook evidence

The critical chronological question, restated: **does Anglian smoothing of ēa →
ē fire before or after palatalisation of *k**? If after, then we need to be
sure that palatalisation **did not apply** to the *k of *laukaz* in the first
place — otherwise we have *līeċ*-type palatal output, which is wrong.

### §3.1  Campbell §255 — the canonical chronological summary

> "From what has now been said, we can suggest the following chronological
> order as probable for the sound-changes discussed in the present chapter:
>   1. Anglo-Frisian development of nasal ā; and of ǣ/ē from West Gmc. ā.
>   2. West Gmc. ai > ā.  3. Fronting of West Gmc. a to æ.
>   4. Breaking and the related processes of retraction.
>   5. Restoration of ā before back vowels.
>   6. Second fronting (mainly VP). **Palatal diphthongization of front
>      vowels, and early diphthongizations of back vowels.**
>   7. **i-Mutation.**  8. Back Mutation.  9. **Smoothing.**
>   10. Contraction of vowels, compensatory lengthening."  — Campbell §255
>      (1959, p. 109)

Campbell ranks **smoothing as #9, AFTER both palatal influence (#6) and
i-mutation (#7)**. This is the opposite order from the one floated in
dossier-reek-2026 §3.ε. On Campbell's chronology, **smoothing cannot bleed
palatalisation**; palatalisation has already either fired or not by the time
smoothing runs.

### §3.2  Hogg vol. 1 §3.3.3.1 — i-mutation and palatalisation order

> "It is generally accepted that **palatalisation preceded i-mutation**, but
> the chronology is difficult to prove, see Hogg (1979b: §5) and also Colman
> (1986a)."  — Hogg vol. 1, lines 7988–7990

This confirms Campbell's #6 < #7. Smoothing is later than both. Hogg p. 446
reproduces and challenges Campbell's ordering with a finer-grained chart
(lines 21115–21127) placing various smoothings between Epinal (ca700) and VPs
(ca825) — confirming smoothing as **post-prehistoric and contemporaneous with
the early manuscript record**, well after palatalisation and i-mutation
(both prehistoric).

### §3.3  Brunner §119 Anm. 1 — what was the trigger consonant?

> "Die Bezeichnung 'Ebnung' für diese Erscheinung wurde als Übersetzung des
> von H. Sweet dafür gebrauchten engl. 'smoothing' … in die deutsche
> grammatische Literatur eingeführt … Die frühere Bezeichnung als
> 'Palatalumlaut' ist sachlich unrichtig, **weil c, 3, h in diesen Fällen
> velar und nicht palatal waren**."  — Brunner §119 Anm. 1

And Anm. 6: "**Anzeichen dafür, daß die Gaumenlaute bei 'Ebnung' im Laufe der
ae. Zeit nicht mehr rein velar gesprochen wurden, fehlen demnach.** Nur vor
hs (geschrieben x) scheint sich eine palatalere Aussprache durchgesetzt zu
haben…"

**Brunner's explicit position: the c/g/h that conditions smoothing was velar,
not palatal, throughout the OE period.** Decisive: **the trigger c was velar
all along, so palatalisation never had any reason to fire in the smoothing
environment**.

### §3.4  Fulk 2018 — disputed phonetics, but same chronology

Fulk takes the opposite phonetic view from Brunner:

> "At about the time of the earliest manuscript records, in a process referred
> to as smoothing, the diphthongs ĕa, ĕo, io were monophthongized to æ, ě, Ĭ
> in the Anglian dialects before c, g, h, **which were thus presumably
> palatal** (see Hogg 1992: §5.93 for discussion)."  — Fulk 2018, §4.13

But Fulk concurs that smoothing is **manuscript-period, not prehistoric** —
post-palatalisation, post-i-mutation in absolute chronology. The phonetic-
identity dispute does not move the relative ordering.

### §3.5  Resolving the chronology paradox for *laukaz → lēc*

The dossier-reek-2026 §3.ε formulation — "smoothing precedes palatalisation,
bleeding it" — is **chronologically incorrect** by Campbell §255 and Hogg
vol. 1 §3.3.3.1. Smoothing is #9, palatalisation is #6, i-mutation is #7.

The correct formulation is **simpler and does not require any unusual
ordering**:

1. PGmc *laukaz (a-stem; back-vowel ending throughout the paradigm).
2. Fronting and breaking deliver early-OE *lēac (with diphthong ēa from
   breaking-of-au, second element a back-vowel offglide -a).
3. Palatalisation Rule 2 (k → ċ before front vowel) fires only when *k is
   followed by a front vowel. In *lēac (NomSg), *c is word-final after the
   back-offglide -a; the rule does not target it. In oblique cases the *c
   is followed mostly by back vowels (-as, -a, -um); only Gen/DatSg `-e`
   could potentially condition palatalisation, and there the levelling
   pressure of the majority back-vowel cells (§4.1) blocks it.
4. i-Mutation has nothing to bite on (no *i in any cell of the a-stem
   paradigm; contrast i-stem *laukiz, FST `laukiz` → *līeċ*).
5. Smoothing (Anglian, late-prehistoric → early-historic) collapses ēa → ē
   before c/g/h. The *c is **already velar** at this point; smoothing does
   not change the consonant.
6. Outcome: *lēc* (Anglian, then pan-dialectal) with velar [k]. WS preserves
   *lēac* (also velar [k]) as the unsmoothed parallel.

**Crucial clarification.** The velar [k] in *lēc* / *lēac* is **not produced
by smoothing bleeding palatalisation**; it is produced by *palatalisation
simply not applying* in this paradigm at any point. **This is a cleaner
analysis than dossier-reek-2026 §3.ε**, and one that does not require
re-ordering the FST cascade.

---

## §4  Paradigm contamination (Q3)

### §4.1  The a-stem masc. paradigm of *laukaz

| Cell  | PGmc       | OE expected (pre-smoothing) | Following V | Palatalisation? |
|-------|------------|-----------------------------|-------------|-----------------|
| NomSg | *laukaz    | *lēac (after apocope of -az)| word-final after back-offglide -a | NO |
| AccSg | *laukam    | *lēac                        | word-final  | NO |
| GenSg | *laukas/-iz| *lēaces                      | -e (front)  | maybe — but not before back -a of root-final ēa (see below) |
| DatSg | *laukai    | *lēace                       | -e (front)  | maybe |
| NomPl | *laukōz    | *lēacas                      | -a (back)   | NO |
| AccPl | *laukans   | *lēacas                      | -a (back)   | NO |
| GenPl | *laukǭ     | *lēaca                       | -a (back)   | NO |
| DatPl | *laukamiz  | *lēacum                      | -u (back)   | NO |

**Six cells with back-vowel context** (NomSg, AccSg, NomPl, AccPl, GenPl,
DatPl) versus **two cells with potential front-vowel context** (GenSg, DatSg).
Even in those two cells, the immediately-preceding ēa diphthong terminates in
a back -a offglide, which on Brunner §119's analysis means the *c is already
velar in the surface phonetics; only on Fulk's view of late-OE smoothing-
trigger c as palatal would there be any pressure toward palatalisation here,
and that is well after the prehistoric palatalisation rule has stopped firing.

### §4.2  Campbell §437–438 — analogical levelling in OE c/ċ paradigms

> "§437. The distribution of velar and palatal or assibilated consonants
> outlined above is very prone to analogical disturbance, and ME and NE forms
> show that there was much variation in OE, e.g. ME *kerven, beginnen*, show
> the initial sound levelled out from *curfon, gunnon*; and many forms like
> NE *like, dike*, Scots *breeks*, beside *such, ditch, breeches* are
> explained from OE doublets like **ġelíc-ġelícum, díċ-dícas, brēċ-brēc**."
> — Campbell §437 (p. 177)
>
> "§438. … 'beside *þencan, þyncan, sécan, sengan* with assibilation, 3rd sg.
> pres. indic. would be *þencþ, þyncþ, sécþ, sengþ*, in which the palatal
> stops reverted to velars; from these velars could be transferred to the
> inf., hence NE *think, seek* (beside *beseech*), dial. *sing* (for *singe*),
> and so *reck, work* (OE *reccean, wyrcan*) … It is more difficult to
> explain similar alternative forms in nouns, e.g. dial. *brig, rig, steek,
> eg, seg, weg, birk*, ME *benk*, for *bridge, ridge, stitch, edge, sedge,
> wedge, birch, bench*. **Luick (Hist. Gramm., §690) would explain such
> forms by assuming that assibilation did not take place before a back vowel,
> and hence would derive them from inflected *brycgum, ecgas, sticas, bircan*,
> &c.** … It is, however, more likely that the explanation lies in complete
> failure to assibilate by Scandinavian settlers."  — Campbell §438 (p. 177)

Campbell endorses the **velar-from-back-vowel-cells** mechanism for verbs
(§438 first paragraph), and reports Luick §690's extension of it to nouns
(scepticism on Norse-contact grounds). For our purposes either explanation
gives the same outcome: **velar [k] is the predicted form in OE for an
a-stem masc. with majority back-vowel cells**.

### §4.3  Direction of analogical levelling — when does velar win?

The ModE doublets enumerated in §437 (NE *like, dike, breeks* vs. *such,
ditch, breeches*) show that **either direction is possible**, depending on
which paradigm cell happens to dominate. Velar wins when: (a) the most-cited
form has a back-vowel suffix; (b) verbs whose 3sg.pres has a syncopating
dental cluster (*sécan/sōhte*, *rēccan/rēhte*) level velar through the
paradigm; (c) nouns whose Sg ends in C-final after a diphthong with back-
offglide (*lēac, rēc, bēag, bēacen* — all velar through the paradigm).

**For *lēac/lēc* specifically.** The a-stem paradigm has six velar cells out
of eight; the NomSg has -c after back-offglide -a (not a front-vowel
context); palatalisation simply never fired anywhere in the paradigm.
Levelling pressure points squarely at velar [k]. **No exception is needed.**

### §4.4  Hogg vol. 1 on depalatalisation by analogy

Hogg vol. 1 (lines 5481–5486) notes that "after palatalisation the new palatal
consonants appear to have had an effect on" subsequent vowel changes; and
treats the c/ċ alternation as paradigm-bound at lines 14231 (i-umlaut /
palatalisation interaction in *cyre / ceosan*) and 17146 (paradigmatic c/ċ
in *ceosan/curon ~ cyre*).

There is no Hogg passage that flags *lēc* / *lēac* as exceptional; like
Campbell, Hogg simply lists it under the smoothing inventory.

### §4.5  Verdict on Q3

Paradigm contamination **reinforces** the velar [k] outcome but is not the
proximal cause: the proximal cause is that **palatalisation never fires in
the a-stem paradigm of *laukaz at all** (back-offglide in NomSg, back-vowel
suffixes in oblique cells, no *i-trigger). The Campbell §437–438 / Luick
§690 mechanism would matter only if there were a front-vowel cell that could
plausibly have palatalised; for the i-stem *laukiz it does, and Norse
*laukr* even shows i-stem confirmation. For OE, WGmc had already shifted to
a-stem (cf. OHG *louh* without umlaut), so the question is moot for the
OE-internal derivation.

---

## §5  Synthesis — does the *raukaz* model carry over?

### §5.1  The parallel summarised

| Feature                           | *raukaz* → rēc   | *laukaz* → lēc/lēac    |
|-----------------------------------|------------------|------------------------|
| PGmc proto (proposed)             | *raukaz a-stem   | *laukaz a-stem (**TSV already**) |
| OHG without umlaut                | *rouh*           | *louh*                 |
| ON                                | *reykr* i-stem   | *laukr* a-stem (no umlaut) |
| OE WS form                        | rēc only         | **lēac**               |
| OE Anglian/smoothed               | rēc              | **lēc**                |
| ModE                              | reek /iːk/       | leek /iːk/             |
| FST current behaviour from a-stem | (mismatch)       | **lēac (matches TSV!)**|

### §5.2  The critical difference

For *raukaz*, the OE attestation is universally *rēc*, never *rēac* — forcing
a target shift. For *laukaz*, **both *lēac* (WS) and *lēc* (Anglian, late-WS
Ælfric) are attested**. The TSV row 2097 already targets *lēac*, the FST
already produces *lēac*. The model is **not under empirical strain** here.

### §5.3  Where the *raukaz* model would extend identically

If the project chooses to align the OE row with the **ModE-witnessed form**
(retarget to *lēc*), then PROTOFORM `*láukaz` stays, and the smoothing rule
from dossier-reek-2026 §4.2 derives *lēc* from *laukaz* by exactly the same
mechanism as *rēc* from *raukaz* — parallel rows. If the project retains
*lēac* as the OE target (the WS-attested form, BT 97864), nothing changes
in FST or TSV; the OE→ME→ModE asymmetry runs through ordinary early-ME
ēa → ē monophthongisation (Jordan §82), outside FST scope.

---

## §6  Recommendation

### §6.1  Priority structure (mirroring dossier-reek-2026 §4.2)

**Priority 1 — leave the row as is (recommended).** Row 2097 PROTOFORM =
`*láukaz`, target = `lēac`, FST output = `lēac`. **Already correct.** OE
*lēac* is well-attested in BT (97864) and Clark Hall (25515). The OE→ME→ModE
transition `lēac` → `lēk` → `liːk` runs through ordinary early-ME
monophthongisation of ēa, outside FST scope. **No change to TSV. No change
to FST.** Verification: `echo laukaz | flookup -i /usr/app/old_english.bin →
lēac` (unchanged).

**Priority 2 — retarget to *lēc* for ModE-pathway consistency with the *rēc*
row.** Appropriate **only if** the project also adopts the Anglian smoothing
rule recommended in dossier-reek-2026 §4.2. Without smoothing in the FST,
retargeting `lēac` → `lēc` would create a new mismatch. If smoothing is
added: TOKENS field `l ē a c` → `l ē c`, PROTOFORM unchanged. The smoothing
rule then derives `lēc` from `*laukaz` via `lēac → lēc`, parallel to *rēc*.

**Priority 3 — add a NOTE.** Lighter touch: keep `lēac` as target, add to
NOTE: "Anglian smoothed *lēc* (Campbell §225) is ancestral to ModE *leek*;
WS *lēac* preserved. Both attested by late OE (BT 97864 vs. 98090)."

### §6.2  Why Priority 1 is the default

Unlike the *rēc* row, **the *lēac* row is not currently broken**. The FST
output matches the TSV target. The ModE asymmetry is downstream OE→ME. Per
the project ethos ("actually attested OE form"), *lēac* is unimpeachably
attested in WS, so targeting it is correct. Priority 2 only kicks in if the
project adopts smoothing from the *rēc* recommendation and chooses to apply
it uniformly.

### §6.3  What this dossier does **not** recommend

- Not changing PROTOFORM. `*láukaz` is exactly right (matches OHG *louh*, ON
  *laukr* without umlaut).
- Not adding a paradigm-contamination FST mechanism (Q3 is not load-bearing
  here; palatalisation simply never fires in the a-stem paradigm).
- Not endorsing dossier-reek §3.ε's "smoothing bleeds palatalisation"
  framing. By Campbell §255 / Hogg, smoothing is #9 and palatalisation is
  #6, so smoothing cannot bleed palatalisation. The correct framing is
  **palatalisation never had reason to apply** in the a-stem paradigm of
  *laukaz / *raukaz, irrespective of smoothing — see §3.5.

This last point is a **substantive correction to dossier-reek-2026 §3.ε**
that should be carried back when revised. It does not change the
*recommendation* of dossier-reek-2026 (add smoothing rule, target *rēc*),
only the chronological *justification* for it.

---

## §7  Open questions

1. **Should dossier-reek-2026 §3.ε be revised?** Yes. The "smoothing bleeds
   palatalisation" formulation is wrong by Campbell §255; the cleaner
   formulation is "palatalisation never targeted *k in the a-stem paradigm;
   smoothing then runs late, harmlessly, on the vowel only". Same
   recommendation, tighter argument.

2. **Was the smoothing trigger c velar (Brunner) or palatal-by-then (Fulk)?**
   The ModE outcome (*leek*/*reek* /iːk/, no affricate reflexes) decisively
   supports Brunner. **Brunner's view is the safer one for the FST**: model
   the smoothing-trigger c as velar.

3. **DOEC corpus search.** Not directly accessible here. Would confirm:
   proportion of *lēc* in late-WS prose; any pre-Alfredian WS *lēac*;
   compound frequencies of *gar-/brade-/crop-* with -lēc vs. -lēac.

4. **Bēacen control.** Parallel mini-dossier on *bēacen / bēcen* would
   sharpen the propagation account in §2.4 — there ModE *beacon* /ˈbiːkən/
   is also monophthongal but reflects ME *beken*, so the propagation story
   is not WS-vs-Anglian but generic ME-monophthongisation.

5. **Toon 1983.** Not in our corpus; only via Hogg ch. 6. Would tighten §2.5
   beyond handbook level.

---

*End of dossier-leek-2026.md. Companion to dossier-reek-2026.md. Conclusion:
row 2097 (*laukaz → lēac*) is currently consistent and requires no change;
the ModE asymmetry pathway runs through Anglian smoothing identically to
*rēc*, and a uniform retargeting to *lēc* is available only if the smoothing
rule from the *rēc* recommendation is adopted. Side-finding: dossier-reek-
2026 §3.ε's "smoothing bleeds palatalisation" framing should be replaced
with "palatalisation never applies in the a-stem paradigm; smoothing runs
late on the vowel only" — same recommendation, cleaner justification,
consistent with Campbell §255 and Hogg vol. 1 §3.3.3.1.*
