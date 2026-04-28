# §17.41 follow-up — shoulder paradigm-cell-choice dossier (2026, Q3)

> **Scope.** This dossier answers the user's Q3 about the shoulder
> mismatch (TSV row 2183, `*skúldrō → sċuldra`, expected; FST
> currently produces `sċoldor`):
>
> > "We usually target the nominative singular and only do otherwise
> > to avoid some analogy that affected that cell. Why would we
> > target the plural here?"
>
> It is the principled justification dossier requested at the head
> of `Germanic/docs/DEV_NOTES.md` §17.41 (lines 39261-39281). It
> deliberately does **not** revisit the philological / handbook
> survey already in `Germanic/docs/dossier-shoulder-2026.md`
> (≈1147 lines, the §17.41 main dossier and Q1/Q2 follow-ups). It
> cross-references that dossier rather than duplicating its source
> roll-up.
>
> No pipeline file, no TSV cell, and no DEV_NOTES section is
> modified by this dossier. It is a discussion document only.

---

> ## RETRACTION (2026-04-28, post-NH review)
>
> **The "Option A" recommendation below — PROTOFORM `*skúldru`
> (NApl) → COUNTERPART `sċuldor` (NSg) — is withdrawn.**
>
> NH pointed out that this is a **cross-cell** mapping (plural
> input → singular output), and that no project precedent does
> this. Verified empirically: every existing non-NSg row is
> cell-consistent — `*xámaras` (GenSg) → `hameres` (GenSg, row
> 478), `*spéru` (NApl) → `speoru` (NApl, row 1070), `*wúndrą`
> (neut. a-stem NSg) → `wundor` (NSg, row 1432). The dossier
> below silently treats "PROTOFORM names a paradigm cell that
> yields the COUNTERPART by sound change, regardless of cell
> identity" as the project's policy; that is incorrect. The
> actual policy is that PROTOFORM and COUNTERPART name the same
> paradigm cell, and switching cells means switching *both*.
>
> Re-evaluation:
> * **Plural-to-plural** (`*skúldru → sċuldru`) would be
>   cell-consistent but the FST currently apocopates *-u after a
>   heavy stem and produces `sċuldor`, not `sċuldru`. So this
>   would still be a mismatch; making it work requires a
>   Luick-§247-shaped apocope blocker, which carries regression
>   risk on `*nosu / sorg / sċofl` (TSV rows 2143/2200/2185).
> * **Singular-to-singular** with any non-cross-cell PROTOFORM
>   fails because every PGmc/PWGmc NSg cell of `*skuldra-`
>   has a non-high suffix and feeds u-lowering. Empirical probe
>   (2026-04-28): `*skúldrą` (neut. a-stem NSg, by analogy with
>   *wúndrą) → `sċoldor`; `*skúldraz` (masc. a-stem NSg) →
>   `sċoldor`. *wúndrą escapes u-lowering only because of its
>   nasal+C cluster (Campbell §§115–118 nasal blocker), which
>   shoulder lacks.
>
> **Conclusion of the retraction.** No cell-consistent PGmc/PWGmc
> reconstruction of shoulder yields `sċuldor` by regular sound
> change in the current cascade. The lexeme belongs in the
> wontfix bin (see `dossier-shoulder-lautgesetz-2026.md`
> retraction).
>
> Sections below are preserved for historical record. The
> precedent catalogue (§§2–3) and the user's-principle
> discussion (§1) remain valid; only the recommendation in §10
> is wrong.

---

## Table of contents

1. The user's stated principle and what it presupposes
2. Catalogue of project precedent for non-NSg targeting
3. Classification of the precedents (what kind of "rescue" is each one?)
4. Does any of those classifications cover *skuldru / sculdor /
   sculdra?
5. The handbook position on which paradigm cell is "primary"
6. The historical depth question: is OE *sculdor* a back-formation
   from the plural *sculdru*?
7. Side-by-side derivations under the current cascade
8. Adjudication: which option is "more lautgesetzlich"?
9. Recommendation
10. Residual uncertainties / followups

---

## 1. The user's stated principle and what it presupposes

The user articulates the project convention as:

> "We usually target the nominative singular and only do otherwise
> to avoid some analogy that affected that cell."

Decomposed, this principle has three components:

* **(P1) Default = NSg.** In the absence of any other consideration,
  the COUNTERPART column should record the dictionary headword as
  conventionally cited in BT / Hall / Campbell / Brunner — which for
  strong masc/neut nouns is the NSg.
* **(P2) Switch only on cause.** A switch to a non-NSg cell needs
  positive justification: the NSg as attested must be analogically
  reshaped, so the FST cannot derive it by sound law.
* **(P3) "Lautgesetzlich" = the test the FST applies.** The role of
  the TSV is to give the FST a regular-sound-change input/output
  pair to verify; rows whose output is analogical pollute the test
  set.

(P1) is a convenience convention and is essentially unargued in the
literature: BT, Hall, Campbell §572ff., Brunner §§238–330, Hogg
chapter 3 all *lemmatise* the NSg. but none of them argue that the
NSg is the **historically primary** form (see §5 below). (P2) and
(P3) are project-internal methodological commitments inherited from
the "mismatch loop" workflow (`Germanic/docs/WORKFLOW.md`).

If (P2) is the only legitimate ground for a cell-switch, then for
*shoulder* we owe an explicit answer to: **what analogy affected
the OE NSg `sculdor` such that the FST can't derive it?** §3 below
answers that the answer is, in fact, "*none — the FST already
derives `sculdor` lautgesetzlich from `*skúldru`*". This makes the
question into a comparison of two *equally* lautgesetzlich
candidates, NSg `sculdor` and NApl `sculdru`, with no analogical
bug to fix in either. The user's intuition (default to NSg) then
applies straightforwardly. §6–§9 work through whether the
underlying historical primacy of the plural cell should override
that default.

---

## 2. Catalogue of project precedent for non-NSg targeting

Exhaustive sweep of `Germanic/docs/DEV_NOTES.md` for the strings
"cell switch", "paradigm cell", "nap.", "neut.pl.", "dat.sg.",
"gen.sg.", "3sg", "imp.sg.", and the §17.x section markers.
Non-headword targets implemented or proposed, in the order they
appear in DEV_NOTES:

| # | Lexeme | Cell chosen | PROTOFORM | TSV target | DEV_NOTES anchor |
|---|---|---|---|---|---|
| 1 | door | (nothing) — Option A: keep PROTOFORM, change TARGET to etymological NSg `dor` | `*durą` | `dor` | line 908ff., §"OE duru" |
| 2 | hammer | gen.sg. | `*xámaras` | `hameres` | mentioned line 3150 |
| 3 | night | dat.sg. | `*naxti` | `niht` | line 3150 |
| 4 | cow | dat.sg. | `*kūi` | `cȳ` | line 3150 |
| 5 | fire | dat.sg. | `*fūri` | `fȳre` | line 1715, §"fire" |
| 6 | rest | gen.sg. (ō-stem `*-ōz`) | `*rastōz` | `ræste` | line 3150ff., 3399 |
| 7 | live (vb) | 3sg pres. | `*libēþi` | `lifeþ` | §"live", line 4292ff. |
| 8 | spear | NApl (neut. u-stem) | `*spéru` | `speoru` | §17.16, §17.17 |
| 9 | thistle | gen.sg. | `*þístilas` | `þistles` | §17.18 |
| 10 | nafola | (PROTOFORM swapped to pre-syncope shape, NSg target) | `*nábulô` | `nafola` | §17.19, line 10331 |
| 11 | tang | NSg (early-Anglian) | `*tang…` | `tang` | §17.20 |
| 12 | sister | early-Anglian NSg | (Anglian shape) | `swester` | §17.21 |
| 13 | meord | dat.sg. (`*-ai` rather than `*-ō`) | `*mízdai` | `meorde` | §17.24 |
| 14 | findan PP | past participle | `*fundene` | `fundene` | §17.10.31 |
| 15 | weasel | (PROTOFORM swapped to long-suffix shape, target stays WS NSg `wesle`) | `*wéslōn` | `wesle` | §17.37 |
| 16 | west | (PROTOFORM stays, TARGET swaps to derivable adverb `westene`) | `*wéstanē` | `westene` | §17.38 |
| 17 | loam | (PROTOFORM swapped to neuter a-stem) | `*láimą` | `lām` | §17.39 |
| 18 | shoulder (this row) | NSg or NApl ? | `*skúldru` | `sċuldor` ~ `sċuldru` | §17.41 |

Sub-categorisation in §3.

---

## 3. Classification of the precedents

The 17 prior cases above are not all the same kind of move. They
fall into five distinct sub-classes:

### Class A — *Stay on NSg, change PROTOFORM to a stem-class that derives the attested NSg lautgesetzlich.*

Examples: **§17.37 weasel** (proto `*wéslon → *wéslōn`, target stays
`wesle`), **§17.38 west** (proto stays `*wéstanē`, target moves to
the actual derivable form `westene` — though here the target is *also*
swapped, the move is "make the PROTOFORM and TARGET match a real
derivable pair"), **§17.39 loam** (proto `*láimōn → *láimą`, neuter
a-stem, target NSg `lām`). These are stem-class corrections, not
paradigm-cell switches at all. The lemma cell (NSg) survives; the
PGmc reconstruction is realigned to the OE-internal stem class.

These cases obey (P1) directly. They do not bear on the shoulder
question because in shoulder we are *not* attempting to keep the
NSg — we are debating between NSg `sculdor` and NApl `sculdru`,
both of which the FST can produce.

### Class B — *Switch the proto to an oblique singular cell whose suffix shape sidesteps a rule that incorrectly fires in the NSg.*

Examples: **fire** `*fūri → fȳre` dat.sg. (NSg `fȳr` would either
have to be derived without i-umlaut, contradicting the attested
fronted vowel, or with i-umlaut, requiring a high-V suffix the
NSg lacks); **night** `*naxti → niht` dat.sg.; **cow** `*kūi → cȳ`
dat.sg.; **hammer** `*xamaras → hameres` gen.sg.; **rest**
`*rastōz → ræste` gen.sg.; **meord** `*mízdai → meorde` dat.sg.

In every Class B case the *NSg root vowel itself is innovative* —
the attested NSg has been remodelled by paradigmatic levelling
(usually by spreading the umlauted/fronted oblique-cell vowel back
into the NSg, or by replacing an apocope-eroded suffix). The FST
cannot derive the NSg lautgesetzlich because **the NSg is
analogical**. Hence the proto is moved to a cell whose suffix can
still be processed by the cascade.

This is the explicit reading of (P2). The TSV row then carries
an oblique-cell PROTOFORM (`*fūri`, `*kūi`, `*xamaras`, `*rastōz`)
paired with the corresponding oblique-cell OE form (`fȳre`, `cȳ`,
`hameres`, `ræste`) — i.e. **both columns shift cells together**.
The implicit pedagogical claim of the row is "the regular sound
change in this cell verifies; the NSg is reshaped".

### Class C — *Switch the proto and target to a plural cell whose suffix shape sidesteps a rule that incorrectly fires in the singular.*

Example: **§17.16 spear** `*spéru → speoru` (NApl).

This is the closest precedent to shoulder. The pre-§17.16 row had
PROTO `*spéru` paired with OE NSg `spere`, but the OE NSg `spere`
is **not the lautgesetzlich u-stem outcome in any dialect**
(DEV_NOTES §17.16.20, table on lines 29537-29548). The only
singular cell whose lautgesetzlich output matches attested
*spere* is the dat.sg. `*speriwi` (where the inner *-i- blocks
back-mutation). Campbell §210.1 states explicitly: *"Analogical
removal is frequent, e.g. **speru** spear … after infl. **spere**,
n.s."* — i.e. WS NSg `spere` is itself an analogical de-back-mutated
form, levelled in from the dat.sg. The plural cells `speoru` (NApl)
and `spera` (GPl) are derivable directly by sound law.

The §17.16 cell-switch was justified by exactly the (P2) ground:
the attested NSg is analogical, so we cannot use it as a
sound-law verification target. The plural NApl `speoru` was chosen
because (a) it is well-attested in Anglian / early-WS, (b) it
gives a direct sound-law derivation, and (c) it surfaces in the
glossary tradition (Épinal/Erfurt, Corpus) where the de-BU
levelling has not yet bled in.

### Class D — *Switch to a finite-verb cell to escape an opaque infinitive.*

Example: **live** 3sg pres. `*libēþi → lifeþ` (DEV_NOTES line
4292ff., §"live"). The infinitive `libban` undergoes j-gemination
which the cascade does not model in this lexeme; the 3sg pres.
without j-gemination is the oldest derivable cell.

Not relevant to shoulder.

### Class E — *Switch to a different inflectional ending (gen.sg.) for general phonotactic relief.*

Example: **§17.18 thistle** `*þístilas` (gen.sg.) target `þistles`.
The motivation here was the word-final obstruent + sonorant cluster
problem (Campbell §§360–363) — apocope of the NSg `*-az` would
produce an inadmissible coda. The gen.sg. retains its suffix and
preserves the medial vowel by syllabification. This is the closest
formal parallel to shoulder, since shoulder is also a heavy stem
ending in a consonant cluster. But the move in §17.18 was
specifically to *escape final-cluster epenthesis*, whereas in
shoulder the proposed move (to NApl `sculdru`) is specifically to
*avoid* apocope (which would otherwise feed epenthesis). The two
are flipped images of each other.

### Sub-summary

The relevant precedents for shoulder are Class C (spear → speoru)
and Class B (fire/night/cow/hammer/rest/meord). In both classes,
the per-row switch is justified by **a sound-law obstruction in
the NSg**, i.e. by an analogy that affected the NSg.

In shoulder, however, **the NSg `sculdor` is already lautgesetzlich
under PROTO `*skúldru`** (DEV_NOTES §17.41 trace, lines 39352–39362):
heavy-stem high-vowel apocope deletes the `-u` and sonority-driven
epenthesis repairs the resulting `*sk-ldr` → `sċuldor`. So the
Class C / Class B (P2) ground does not directly apply. This is
what makes the shoulder case **structurally different** from spear.

---

## 4. Does any of those classifications cover *skuldru / sculdor / sculdra*?

Side-by-side check:

| Concern from precedent class | Does it apply to *skuldru / sculdor*? |
|---|---|
| (Class B) Attested NSg has innovative root-vowel from paradigmatic leveling — FST can't derive it from any inheritable PGmc cell | **No.** OE `sculdor` has *u*, the same root vowel attested in every paradigm cell (`sculdor`, `sculdru`, `sculdra`, `scyldru`, `sculdran`, OFris `skulder`, OS `skuldra`, OHG `scultra`). There is no innovative root-vowel quality in `sculdor` to escape. |
| (Class B) Attested NSg has lost a suffix the FST cannot remove without producing a wrong shape | **No.** Apocope of `*-u` in `*skúldru` is a regular sound change in the cascade (HighVowelApocope after a heavy stem) and its output `*skuldr` is repaired by Epenthesis — *exactly* the rules R/T (vol. 2 p. 142, p. 267) and Luick §247 say should fire. |
| (Class C) Attested NSg is analogically de-mutated / de-broken from a higher-vowel obl. cell | **No.** There is no back-mutation or breaking issue in shoulder; `sculdor`'s `u` does not correspond to a `*eu` / `*eo` etymon and was never broken. |
| (Class B/C) The "right" cell for the FST's input is one whose suffix shape sidesteps an FST rule that would *incorrectly* fire if given the NSg's actual proto | **Yes — but this is the switch from `*skúldrō` → `*skúldru` (the PROTOFORM swap), not the switch from NSg `sculdor` → NApl `sculdru` (the COUNTERPART swap).** Once the PROTOFORM is `*skúldru`, the FST already derives the NSg `sculdor` (= the BT/Hall headword) without needing a further COUNTERPART swap. |
| (Class A) PGmc proto is in a stem class that doesn't survive in OE; the OE form sits in a different OE-internal class | **Partially.** Kroonen reconstructs `*skuldra-` masc. (a-stem); Orel reconstructs `*skuldr(j)ō` fem. (jō-stem); R/T cite `*skuldru`; OE is variously masc. (a-stem `sculdor`) and weak fem. (`sculdra`). The cognate-set headword `*skuldrō` (in the project's TSV) reflects Orel; the per-row PROTOFORM should reflect what gives the OE attested form. This is an Class-A move, *but* it does not by itself force a non-NSg COUNTERPART. |
| (Class E) Apocope of NSg suffix would produce an inadmissible final cluster, and the attested OE form retains a vowel via a non-NSg cell | **No, the opposite.** Apocope of `*skúldru → *skuldr` produces an inadmissible cluster, but the FST has Epenthesis to repair it (`*skuldr → sculdor`), which is exactly what the attested NSg `sculdor` shows. Targeting NApl `sculdru` would be a way to *avoid* even invoking Epenthesis. |

**Conclusion of §4.** Of the 17 precedents in §2, only the
PROTOFORM-side of the §17.41 plan (swap `*skúldrō` → `*skúldru`,
analogous to the PROTOFORM swaps in Class A: weasel, loam) is
positively supported. The COUNTERPART-side switch (NSg
→ NApl) is **not** supported by any of the (P2)-grounded
precedents, because the (P2) precondition (NSg is analogical)
is not satisfied here. This is the user's intuition.

---

## 5. The handbook position on which paradigm cell is "primary"

### 5.1 Lemmatisation conventions (BT, Hall, Campbell, Brunner)

* **Bosworth-Toller**: nouns are lemmatised by NSg, with
  inflectional class and oblique-cell forms following. Plural-only
  nouns (e.g. `wǣpen-gewrixl`-type collectives) are lemmatised by
  the attested cell. Strong masc. `sculdor` is lemmatised under the
  NSg (BT p. 845); the BT-Supp adds a separate lemma `sculdra, an`
  (weak fem.) for the single Anglian/late-WS attestation.
* **Hall** (Concise): same convention; only `sculdor m.` is
  lemmatised, with `sculdur` cross-listed.
* **Campbell** §572ff.: paradigms are headed by NSg.
* **Brunner** §§238ff.: paradigms are headed by NSg.

These are **lexicographic** conventions (alphabetical-citation
needs), not historical-phonology claims. None of these works
asserts that the NSg is the *etymologically primary* cell. (The
nineteenth-century Neogrammarian tradition often treated GSg or
DSg as more conservative, since the inflectional ending is
preserved; cf. §5.2.)

### 5.2 Explicit handbook discussion of which cell is "primary"

A scan of the consulted corpus turns up no general
methodological statement of the form "the NSg is the primary cell
for OE etymological reconstruction". The closest things we can
find are:

* **Ringe & Taylor 2014 vol. 2 §3.1.1 pp. 55–60** lay out PGmc
  noun paradigms cell-by-cell, noting which cells preserve
  inheritable phonological information (e.g. `*-uz` of u-stem NSg
  retains the high-V conditioning information; `*-iz` of GSg and
  NPl retains the *i* conditioning information). They do **not**
  privilege any single cell as "primary"; they explicitly note
  that the *i*-conditioning cells are diagnostic for i-umlaut and
  that the high-V cells are diagnostic for u-retention, leaving
  the choice of which cell to use as the etymological "test" up
  to the lexeme.

* **Campbell** §608: notes that the OE u-stem (and to a lesser
  degree the i-stem and consonant-stem) NSg has lost the
  diagnostic suffix `*-uz` and that the **NApl** is therefore
  often the *more conservative* cell. This is in a passage
  immediately under "the neuter u-stems retain `-u` of the NApl
  but apocopate the NSg in heavy stems". The example Campbell
  gives is *spere / speoru* (cf. §17.16). For neuter u-stems,
  Campbell is **explicitly stating that NApl is the more
  conservative (primary) cell**.

* **Luick** §247 and §103, when discussing
  high-V-conditioned non-lengthening, lists the relevant
  paradigm members in the **plural** (`sculdru, wundru, cildru,
  englas, gyrdlas, fyrðran, hundred`). The singular forms
  `sculdor, wundor, engel, gyrdel, hundredas` are introduced as
  "wonach dann auch …" (whence then also …) — i.e. as
  *back-formations* from the diagnostic plural cell. This is the
  closest the literature comes to an explicit statement that
  *for this class*, the NApl is primary and the NSg is derivative.

* **Hogg** vol. 1 §3.55 discusses heavy-stem apocope in OE u-stems
  and neuters and adopts the same chronology: "the high vowel of
  the NApl resists deletion in light stems and is deleted in heavy
  stems; epenthesis then re-syllabifies the cluster". Hogg cites
  *sculdor / sculdru* and *wuldor / wuldru* as the canonical
  examples.

* **Ringe & Taylor 2014 vol. 2 p. 142** lists the PWGmc lemma as
  `*skuldru` — the **plural** cell. R/T's PWGmc inventory uses
  whichever cell shape they consider best preserved across the
  WGmc dialects; for *shoulder* that is the high-V plural, not
  the apocopated singular. They do this without comment, but the
  choice is consistent with their general methodology of using the
  diagnostic cell (cf. their treatment of `*fehu` vs. `*fihu`,
  vol. 2 p. 56).

### 5.3 Verdict on the "primary cell" question

**The literature does not endorse a general default to NSg.** It
endorses *cell-specific* defaults driven by which cell preserves
the most phonological information.

* For strong masc/fem a-/ō-stems, the NSg and the inflectional
  cells both preserve diagnostic information, so the NSg
  convention is harmless (BT/Hall lemmatisation).
* For neuter u-stems, neuter consonant stems, and the
  /uRCr/ Dehnung-blocker class, **the plural NAcc is the
  diagnostic cell** and the singular is back-formed.
* For i-stems and ja-stems, the GSg/DSg or NSg+e (if levelled)
  carry the i-umlaut diagnostic.

This means the project's "default to NSg" rule is *itself* a
lexicographic convenience, not a historically grounded
methodological commitment. Where the relevant literature treats
the plural (or an oblique cell) as historically prior, defaulting
to it is not a "switch from the principle"; it *is* the principle.

This reading reframes the user's question: the policy "default to
NSg, switch only on cause" works for almost every row, but for the
heavy /uRCr/ class **the NApl is the primary cell on independent
historical grounds**, and the NSg is the back-formed cell. There
the question "why not the NSg?" gets the same answer it gets in
spear (§17.16): because the NSg is the morphologically *secondary*
form.

---

## 6. The historical depth question: is OE *sculdor* a back-formation from the plural *sculdru*?

This is the key question for shoulder.

### 6.1 Two competing historical chronologies

**Chronology I (NSg-primary).**  PWGmc inherits a singular
form `*skuldr-` (stem-final cluster, no overt suffix in the
relevant cell, or with a non-high suffix `*-ō`). High-V apocope
deletes whatever short vowel ends the singular; epenthesis repairs
the cluster, producing `sculdor`. The plural is then formed by
adding `-u` to the inherited singular stem.

**Chronology II (NApl-primary).**  PWGmc inherits a paradigm in
which the NApl carries `*-u` (whatever the prehistory of that *-u*
— shortening of `*-ō`, neut-pl `*-u` of the consonant stems, or
analogical extension from the u-stem class). The NSg carries no
overt suffix (after PNWGmc apocope) or a non-high suffix that is
itself apocopated. Heavy-syllable apocope and epenthesis then
operate on the NSg `*skuldr-`, producing the back-formed
`sculdor`. The diagnostic shape of the lexeme — the cluster
*-uldr-* with an unlowered *u* — is preserved in the NApl `sculdru`,
where the high-V suffix bleeds u-lowering.

Under Chronology I, NSg is etymologically primary and `sculdor`
verifies the entire u-retention story directly. Under Chronology
II, the high-V suffix of the NApl is the diagnostic, and `sculdor`
is the sound-law output of NSg apocope+epenthesis applied to a
stem whose root *u* survives only **because** that high-V suffix
existed elsewhere in the paradigm.

### 6.2 What the handbooks actually adopt

R/T vol. 2 p. 142, Luick §247, and Hogg §3.55 all adopt
**Chronology II** for this class: they cite the paradigm by the
plural and treat the singular as back-formed. (This is documented
in the §17.41 main dossier §6.3, "the *wuldor / wundor* class" and
§4.2, "the high-vowel-suffix view.") The wider class (cildru,
gyrdlas, englas, hundred, fyrðran, wundru, sculdru) was
identified by Luick precisely on the criterion that the **plural
shape preserves the diagnostic phonological information** that the
singular (after apocope+epenthesis) loses.

Kroonen (EDPG p. 478) gives `*skuldra-` m. as the lemma, but
this is a stem-class lemma (he uses the same convention for every
WGmc a-stem: `*wulþra-` for *wuldor*, `*wundra-` for *wundor*); it
is not a claim that the NSg in `-a-` is the historically primary
*cell*. Kroonen's choice of stem-class label is simply a
convention; Luick §247's choice of paradigm-cell citation is a
historical claim.

### 6.3 Implication for "what does the FST verify?"

Under Chronology II, **the FST is verifying *two* things at once**
when it derives `*skúldru → sċuldor`:

1. The **u-survival** in the *-uldr-* cluster. This is the
   diagnostic phonological observation of the lexeme. The FST
   verifies it by *not* applying NWGmcULowering — which it doesn't
   apply because the suffix `-u` in `*skúldru` is high.
2. The **heavy-stem apocope + epenthesis** that produces the
   surface NSg from a high-V-suffixed stem. This is the secondary
   morphology that derives the NSg from the (etymologically prior)
   plural.

If the COUNTERPART is `sċuldor`, the row tests **both** (1) and
(2) at once.

If the COUNTERPART is `sċuldru`, the row tests **only** (1) — the
diagnostic phonological observation. (2) is not exercised, since
the high-V suffix is not apocopated in the plural cell as the FST
currently runs (which is itself a problem; see §7.)

Class-C precedent (§17.16 spear) chose the plural cell because (a)
the singular *spere* is **not** derivable lautgesetzlich, so
testing the singular would be a false test, and (b) the plural is
the historically primary cell anyway. In shoulder, condition (a)
fails — `sċuldor` *is* derivable — so the precedent does not
fully transfer. But condition (b) — historical primacy of the
plural — does hold (per §6.2).

The user's question is essentially "is (b) on its own enough to
justify a cell-switch?" The literature supports (b), but the
project's (P2) policy implicitly requires both (a) and (b). This
is a real principled tension, not a notational quibble.

---

## 7. Side-by-side derivations under the current cascade

(This section reproduces and extends the trace already given in
DEV_NOTES §17.41 and `dossier-shoulder-2026.md` §1, §10.)

### 7.1 PROTOFORM `*skúldrō` (current TSV) — current FST output

```
ProtoInput            *s *k *ú *l *d *r *ō
NWGmcULowering        *s *k *ó *l *d *r *ō   (← *u → *o; next-syll *ō non-high)
NWGmcFinalLongORaising *s *k *ó *l *d *r *u  (← *-ō → *-u, word-final; counter-fed)
[carry through pre-OE]
ProtoToOE / Apocope   *ʃ *ó *l *d *r          (← heavy-stem high-V apocope deletes *-u)
Epenthesis            *ʃ *ó *l *d *o *r       (← sonority repair)
Surface               sċoldor                ✗ MISMATCH against any attested OE form
```

Failure mode: NWGmcULowering fires before NWGmcFinalLongORaising,
so the root vowel is lowered while the suffix is still `-ō`; only
then does the suffix shorten to `-u`. Reordering would regress
*nosu, sorg, sċofl* (DEV_NOTES §10.3 of the main dossier).

### 7.2 PROTOFORM `*skúldru` (R/T's PWGmc shape) — derivation to **NSg**

```
ProtoInput            *s *k *ú *l *d *r *u
NWGmcULowering        *s *k *ú *l *d *r *u   (no fire; suffix *u is high)
NWGmcFinalLongORaising *s *k *ú *l *d *r *u  (no fire; suffix is already short)
[carry through pre-OE]
ProtoToOE / Apocope   *ʃ *ú *l *d *r          (← heavy-stem high-V apocope deletes *-u)
Epenthesis            *ʃ *ú *l *d *o *r       (← sonority repair)
Surface               sċuldor                ✓ matches BT/Hall main headword
```

This is the trace already verified in DEV_NOTES §17.41.

### 7.3 PROTOFORM `*skúldru` — derivation to **NApl**

The wished-for derivation is `*skúldru → sċuldru` (no apocope). But:

```
ProtoInput            *s *k *ú *l *d *r *u
NWGmcULowering        *s *k *ú *l *d *r *u   (no fire)
NWGmcFinalLongORaising *s *k *ú *l *d *r *u  (no fire)
[carry through pre-OE]
ProtoToOE / Apocope   *ʃ *ú *l *d *r          (← heavy-stem high-V apocope deletes *-u)
                                              (...same as §7.2)
Epenthesis            *ʃ *ú *l *d *o *r       (← same)
Surface               sċuldor                ✗ MISMATCH against `sċuldru`
```

The cascade's HighVowelApocope rule is conditioned on stem weight,
not on case; it cannot tell that this `-u` happens to be a
plural ending while the same `-u` in some other lexeme is a
singular. So the FST produces `sċuldor` from `*skúldru` regardless
of whether we *want* the singular or the plural derivation.

To get `sċuldru` out, we would have to either:

* **(7.3a)** suppress heavy-stem apocope in the /-uRCr-/
  environment, replicating Luick §247's Dehnung-blocking
  observation. This is a non-Neogrammarian observation about a
  small lexical class (`sculdru, wundru, cildru, gyrdlas, englas,
  fyrðran, hundred`), and Luick himself does not formalise it
  as a rule. **Cost**: substantial; cf. `dossier-shoulder-2026.md`
  §7 Option 4 regression risk.
* **(7.3b)** declare PROTOFORM = `*skúldrū` with a long *-ū*. Long
  high vowels resist apocope. But R/T explicitly cite `*skuldru`
  with **short** *u* (vol. 2 p. 142), so this would be a
  reconstruction we are inventing rather than adopting from the
  literature. **Cost**: philological, not technical.
* **(7.3c)** add a `+plural` morphological tag to the proto and
  thread it through the cascade so apocope can be paradigm-aware.
  **Cost**: enormous architectural change; the cascade is purely
  segmental.

None of (7.3a–c) is a small change.

### 7.4 Implication

Under the current cascade, `*skúldru → sċuldor` is the **only**
output. The FST cannot produce `sċuldru` from any plausible
PROTOFORM without one of the three large-cost edits above.

This means the choice between Option A (target NSg `sċuldor`) and
Option B (target NApl `sċuldru`) is **not** a choice between two
equally cheap configurations of the cascade. **Option A is free**
(the cascade already produces it); **Option B requires either an
FST rule change or an unjustified macron-on-suffix in the proto.**

This is independently decisive against Option B on engineering
grounds (cf. (P3): the FST is the test, and the FST currently
cannot pass Option B without rule changes that have their own
regression risk).

---

## 8. Adjudication: which option is "more lautgesetzlich"?

Three distinct senses of "lautgesetzlich" need to be kept apart:

* **(L1) Lautgesetzlich relative to PWGmc.** Given a PWGmc input
  *X*, does the cascade produce the attested OE *Y* by sound law
  alone (no analogical surcharges)?
* **(L2) Lautgesetzlich relative to the etymologically primary
  cell of the OE paradigm.** Is *Y* the cell that the literature
  treats as the historically prior form, on the basis of which the
  rest of the paradigm is back-formed?
* **(L3) Lautgesetzlich relative to PGmc.** Given a PGmc input
  (one chronological stage earlier than (L1)), does the cascade
  reach attested OE by sound law alone?

For shoulder:

* **(L1):** Both `sċuldor` and `sċuldru` are L1-lautgesetzlich
  outputs of the cascade *in principle* (i.e., they are both
  sound-law-derivable from `*skúldru` if the relevant
  heavy-stem-apocope conditioning is set up correctly). In
  practice, only `sċuldor` is L1-lautgesetzlich under the
  cascade *as currently constituted* (§7).
* **(L2):** `sċuldru` is the L2-primary cell per Luick §247,
  R/T vol. 2 p. 142, and Hogg §3.55. `sċuldor` is back-formed.
  This is the historical-depth point §6 turns on.
* **(L3):** Neither cell can be derived L3-lautgesetzlich from
  PGmc `*skúldrō` (the cognate-set headword shared with Du/G/E),
  because of the NWGmcULowering vs. NWGmcFinalLongORaising
  ordering problem (§7.1). Reaching either OE form from PGmc
  requires the per-row PROTOFORM swap to `*skúldru`.

The user's intuition implicitly weights (L1) and (L3) heavily.
Class C (spear) precedent weights (L2) heavily — but only because
the Class-C lexemes fail (L1) for the singular. In shoulder,
because the singular *passes* (L1), the (L2) argument has to do
all the work alone.

**Engineering tradeoff:**

| Criterion | Option A (target `sċuldor`) | Option B (target `sċuldru`) |
|---|---|---|
| L1 under current cascade | ✓ | ✗ (cascade produces `sċuldor`, not `sċuldru`) |
| L2 (etymological primacy) | ✗ (back-formed; Luick, R/T, Hogg) | ✓ |
| L3 (from PGmc cognate-set headword) | ✗ for `*skúldrō`; ✓ if we swap to `*skúldru` | ✗ for `*skúldrō`; ✓ if we swap to `*skúldru` and add an apocope blocker |
| BT/Hall lemma alignment (P1) | ✓ (BT main, Hall main headword) | ✗ (BT lists *-dru* under the NSg lemma, but it is not the citation form) |
| Cost (FST changes) | None | New rule + regression-test sweep, OR macron-suffix `*skúldrū` in PROTOFORM (philologically non-cited) |
| Mismatch-loop net | -1 (good) | -1 only after rule change; otherwise still mismatched |
| Analogical NSg? (i.e. (P2) precondition) | No — `sċuldor` is sound-law output of high-V apocope+epenthesis | Vacuous |
| Cross-Gmc TSV impact | None (cognate-set proto stays `*skuldrō`) | None |

Option A wins on every criterion **except** (L2). (L2) is the only
ground for Option B, and it is a real ground — but it cannot
overcome the conjunction of L1, L3, P1, P2, P3, cost, and
mismatch-loop net.

The Class-C spear precedent does not transfer here because the
Class-C precondition (NSg fails L1) is unsatisfied. Spear was
forced onto the plural cell because the singular *spere* was
analogical (Campbell §210.1: "Analogical removal is frequent,
e.g. **speru** spear … after infl. **spere**, n.s."). Shoulder is
*not* forced onto the plural because the singular *sculdor* is
**not** analogical — it is the regular sound-law back-formation
that Luick §247 describes.

The historical-primacy claim (L2) is best honoured by **a comment
in the TSV row** ("the diagnostic high-V suffix of `*skúldru`
makes this the etymologically prior cell per Luick §247, R/T
vol. 2 p. 142; the FST derives the NSg `sċuldor` by regular
heavy-stem apocope + epenthesis"), not by switching the COUNTERPART.

---

## 9. Recommendation

### Options as restated

* **Option A — COUNTERPART = `sċuldor`** (NSg, BT/Hall main lemma).
  PROTOFORM swapped from `*skúldrō` to `*skúldru` per R/T vol. 2
  p. 142. FST already produces this; zero rule changes; zero
  regression risk. The TSV row comment should record that the
  per-row PROTOFORM swap is a Class-A move (stem-class /
  paradigm-cell shape correction) and that the etymologically
  primary cell is the plural per Luick §247.

* **Option B — COUNTERPART = `sċuldru`** (NApl). PROTOFORM
  swapped to `*skúldru`. Requires either (i) a Luick-§247-shaped
  apocope blocker in the FST (regression risk on `*nosu, sorg,
  sċofl`-style rows must be re-verified; cf. §10.3 of main
  dossier), or (ii) PROTOFORM = `*skúldrū` with macron, which is
  not philologically cited (R/T have short *u*).

* **Option C — COUNTERPART = `sċuldra`** (weak fem.). The user has
  ruled this out, and §11 of the main dossier independently
  shows it to be analogically innovative, not derivable from any
  PGmc cell, and unmodellable in principle. No literature argues
  for it as the primary form; even BT-Supp registers it as a
  marginal supplement entry.

* **Option D — Dual-row split** (one row for sg., one for pl.).
  No project precedent: the TSV is keyed by cognate set
  (`COGIDS` column), and a sweep of `germanic-aligned-final.tsv`
  shows OE has exactly **one row per cognate set** in current
  practice (`awk -F'\t' '$8=="Old_English" {print $5}' | sort
  | uniq -c | sort -rn | head` returns no duplicates). Adding
  a second OE row for the same cognate set would be an
  architecturally novel move with downstream implications for
  any tool that assumes one-OE-per-COGID. Not recommended unless
  there is independent reason to want both cells in the
  evaluation set.

### Recommendation: **Option A.**

The principled justification is the conjunction of:

1. **The user's own (P1)–(P3) policy is satisfied by Option A
   without exception.** The NSg `sċuldor` is the BT/Hall main
   lemma (P1); no analogy needs to be sidestepped (P2 is vacuous,
   not violated); the FST verifies the row by sound law (P3).
2. **The Class-C spear precedent does not transfer.** In spear
   the NSg fails L1 (it is analogical per Campbell §210.1); in
   shoulder the NSg passes L1.
3. **(L2) historical primacy of the plural** — the only argument
   for Option B — is real (Luick §247, R/T vol. 2 p. 142,
   Hogg §3.55) but is honoured **inside the FST itself**: the
   PROTOFORM swap to `*skúldru` records it. The COUNTERPART does
   not also need to record it.
4. **(L3) cost.** Option B requires either a Luick-§247-shaped
   apocope blocker rule (which Luick himself does not formalise,
   and which has nontrivial regression risk on `*nosu, sorg,
   sċofl`) or a non-cited macron `*skúldrū`. Option A requires
   zero rule changes and zero new reconstructions.
5. **Mismatch-loop net.** Option A clears the row immediately;
   Option B clears it only after rule work that may produce its
   own regressions.
6. **Project precedent for the *PROTOFORM*-only swap.** Class A
   moves (weasel §17.37, loam §17.39) are exactly this: realign
   the per-row PROTOFORM to the OE-internal stem-class shape
   while keeping the NSg target. Option A is a Class-A move, not
   a Class-C move.

### One-sentence executive summary

> **Recommendation: Option A.** Swap the per-row PROTOFORM from
> `*skúldrō` to PWGmc `*skúldru` (Class-A precedent: weasel,
> loam) and keep the COUNTERPART as the BT/Hall main lemma
> `sċuldor` (NSg). The user's NSg-default principle holds; the
> Class-C plural-cell precedent (spear) does not transfer because
> spear's NSg is analogical (Campbell §210.1) whereas shoulder's
> NSg is the regular sound-law back-formation by heavy-stem
> apocope + epenthesis that Luick §247 and R/T vol. 2 p. 142
> independently describe.

---

## 10. Residual uncertainties / followups

1. **Q4 — Is `*skúldrō → *skúldru` lautgesetzlich?**  This is the
   sister-dossier (`Germanic/docs/dossier-shoulder-lautgesetz-
   2026.md`) called out at the head of DEV_NOTES §17.41. Option A
   in this dossier presupposes that swapping the per-row PROTOFORM
   from `*skúldrō` to `*skúldru` is a defensible move. If the Q4
   dossier concludes that the change `*skuldrō → *skuldru` is
   morphologically conditioned (class-shift) rather than a
   sound-law output, then Option A degrades to Option F:
   "wontfix; classify with `wulf / fugol` exception bin". §10.4
   of the main dossier already partly addresses this.

2. **Cross-class inventory check.**  Before adopting Option A, the
   project should sweep the TSV for `*wuldor` and `*wundor` rows
   (see §9 of main dossier, residual uncertainty 6). If those
   rows are encoded as `*wulþrō` / `*wundrō` and produce wrong
   outputs, they should be moved to PROTOFORM `*wulþru` /
   `*wundru` in the same edit. If they are absent, this is an
   opportunity to add them as Option-A-style verification rows.

3. **(L2) annotation discipline.** The recommendation to record
   the L2 historical-primacy point as a TSV-row *comment* (rather
   than as the COUNTERPART itself) presupposes the project has a
   conventional comment column or DEV_NOTES anchor for such
   notes. The current TSV format does not have a comment column;
   the convention has been to record notes in DEV_NOTES under the
   relevant §17.x. The §17.41 entry already does this (lines
   39369–39372). No further infrastructure is needed.

4. **Philological-only Option D revisit.** If a future iteration
   of the project adopts a one-cogset-many-OE-rows architecture
   (e.g. for the OE textbook generator that wants both NSg and
   NApl as exercise targets), the dual-row split becomes
   attractive: one row for `*skúldru → sċuldor` (current cascade)
   and one row for `*skúldru → sċuldru` (only after a
   Luick-§247-blocker rule lands). For now this is out of scope.

5. **The (P1)/(P2) policy itself.** This dossier has implicitly
   defended (P1) on lemma-convention grounds (BT/Hall) plus the
   R/T cell-specificity discussion (§5.2). A more explicit
   project-policy document — e.g. a section in WORKFLOW.md
   stating "default to NSg unless the NSg fails L1 *and* a
   non-NSg cell passes L1" — would forestall future ambiguity.
   The shoulder case has been useful as a stress test: it shows
   that L2 alone, without L1 failure, does **not** override
   (P1).

---

### Source roll-up (this dossier)

| Source | Where | What it contributes |
|---|---|---|
| BT s.v. *sculdor* | p. 845 | NSg lemmatisation; NApl `sculdru/sculdra` listed under it |
| BT-Supp s.v. *sculdor* | Supp p. 113123 | Adds weak-fem `sculdra, an` (Angl. xiii.406.588) |
| Hall, Concise s.v. | p. 354 | Only `sculdor m.` headword |
| Campbell §210.1 | — | "Analogical removal is frequent, e.g. **speru** spear … after infl. **spere**, n.s." — establishes that spear NSg is analogical |
| Campbell §608 | — | Neuter u-stem: NApl is more conservative than NSg (heavy stems lose the NSg suffix) |
| Campbell §572ff. | — | NSg lemmatisation convention |
| Brunner §92,2,a | — | Sceoldor is post-`sc-` glide spelling, not u-lowering (rules out Option C variants) |
| Brunner §§238–330 | — | NSg lemmatisation convention |
| Luick §78 + Anm. 3 | — | u-lowering exceptions; rejects Bülbring; paradigmatic levelling |
| **Luick §247** | — | The /uRCr/ Dehnung-blocker cluster: `sculdru, wundru, cildru, gyrdlas, englas, hundred, fyrðran` cited as the *primary* cells; `sculdor, wundor, engel, gyrdel` as back-formations ("wonach dann auch …") |
| Hogg vol. 1 §3.55 | — | Heavy-stem apocope + epenthesis chronology; *sculdor / sculdru* and *wuldor / wuldru* as canonical examples |
| **R/T vol. 2 p. 142** | — | PWGmc lemma `*skuldru` (the **plural-cell** shape), explicitly chosen over a NSg-style reconstruction |
| R/T vol. 2 §3.1.1 pp. 55–60 | — | PGmc noun-paradigm cell-by-cell discussion; no privileging of NSg |
| R/T vol. 2 p. 267 | — | PNWGmc *-ō > *-u shortening rule |
| Kroonen EDPG p. 478 | — | Stem-class lemma `*skuldra-` m. (a-stem); not a paradigm-cell claim |
| Orel HGE p. 345 | — | `*skuldr(j)ō f.`; flags OE *sculdor* as masc., i.e. notes class-shift |
| DEV_NOTES line 908ff. (door) | — | Class-A precedent: keep PROTOFORM, change TARGET to etymological NSg |
| DEV_NOTES line 1715, 3150 (fire/cow/night/hammer) | — | Class-B precedents: oblique-cell PROTOFORM + oblique-cell TARGET |
| DEV_NOTES line 3399 (rest) | — | Class-B precedent (gen.sg.) |
| DEV_NOTES §17.16 (spear) | — | **Class-C precedent**, the closest analogue: NSg analogical → switch to NApl |
| DEV_NOTES §17.16.20 lines 29537–29548 | — | Cell-by-cell paradigm dossier for *speru* — model for this dossier |
| DEV_NOTES §17.18 (thistle) | — | Class-E precedent: gen.sg. to escape final-cluster apocope |
| DEV_NOTES §17.37 (weasel) | — | Class-A precedent: PROTOFORM stem-class swap, TARGET stays at WS NSg |
| DEV_NOTES §17.39 (loam) | — | Class-A precedent: PROTOFORM stem-class swap to neuter a-stem, TARGET stays at NSg |
| DEV_NOTES §17.41 (this row) | — | The active mismatch loop entry; preliminary plan to be revised after this dossier and Q4 land |
| `Germanic/docs/dossier-shoulder-2026.md` | — | The main §17.41 dossier (Q1, Q2 follow-ups; full source roll-up; Option matrix) — referenced rather than duplicated |

End of dossier.
