# OE medial unstressed `*u → *o`: what is the conditioning environment?

A research dossier for the FST cascade modelling PGmc → OE,
specifically targeting the rule we currently call
`OEMedUnstressedULowering` (Campbell §§373–374; Brunner §44;
Hogg 1992 §§3.3.1.3, 3.3.3.2). Companion to
`dossier-datpl-um-vs-om-2026.md`, which independently established
that early-OE DatPl `-um` is phonologically inert and that no
standard handbook posits a `*-um → *-om` stage.

The present dossier asks the **inverse, more general** question:
given that past-pl `-on` (lowered) and dat.pl. `-um` (preserved)
both descend from unstressed *u in apparently identical
phonotactic position, what is the right structural description of
the lowering rule? In particular, is "exclude `*m` from the
right-context consonant slot" the consensus statement, an
approximation, or a novel proposal?

**Bottom line up front:** the proposed *m*-exclusion is **not
novel** — Campbell §373 and Brunner §44 (Anm. 7) state it
explicitly, Hogg 1992 §3.3.1.3 cites it as an unexplained but
empirically robust generalisation, and Fulk treats raising/
preservation before *m* as a NWGmc-level isogloss (§1.8 (b);
§5.2). The rule's right context should be `[C - {*m}]`, possibly
also `[C - {*m, *ng}]` (Brunner). The cascade's current
unrestricted formulation is over-applying.

---

## §1. Question

The cascade currently lowers any medial unstressed `*u` to `*o`
between any non-`u` vocalic context and any consonantal context:

```
{*u} -> {*o} || [EnglishStarVocalic - [{*u}|{*ū}]]
                [EnglishStarConsonant | EnglishPalatalConsonant]+
                _
                [EnglishStarConsonant | EnglishPalatalConsonant]
```

Empirical pressure points:

| paradigm cell | PGmc | OE | suffix vowel |
|---|---|---|---|
| past-pl strong | `*búgun` | `búgon` | lowered |
| past-pl strong | `*skúbun` | `sċufon` | lowered |
| past-pl strong | `*budun` | `budon` | lowered |
| dat-pl masc.    | `*skúldrumiz` | `sċuldrum` | preserved |
| dat-pl a-stem   | `*dagamaz`  | `dagum` | preserved (via raising) |
| dat-pl mixed    | `*xámarumiz` | `hamerum` | preserved |
| acc.sg. r-stem | `*brṓþurun` | `brōðor` | preserved as `u` then late lowered to `o` |

Both -on and -um are post-stress, pre-single-nasal, word-final
after PWGmc apocope. The only segmental difference in the right
context is **/n/ vs /m/**.

The user's working hypothesis: narrow OEMedUnstressedULowering
by **excluding `*m` from the right-context consonant slot**.
Question: is this the consensus formulation in the historical
phonology literature, or a novel generalisation?

---

## §2. The rule as stated in the standard sources

### 2.1. Campbell, *Old English Grammar* (1959), §§373–374, §378

Campbell's §373 is the foundational locus. The rule, *verbatim*,
runs (I quote from `docs/references/campbell_old_english_grammar.txt`,
lines 10189–10215):

> § 373. Unaccented *u* is preserved in all instances in the early
> North. short texts, BH and LV. … In later sources *u* has an
> increasing tendency to change to *o*, but it was far more stable
> in absolute finality than when protected. … Ordinary OE forms
> are, however, e.g. *hēafod* head, *heofon* heaven, *tungol* star,
> past indic. pl. -*on*, weak past of Class II -*ode*, superl. -*ost*,
> but n.s. of *wa*-, *ō*- and *u*-stems -*u* (*bearu*, *giefu*, *sidu*),
> n.p.n. of *a*-stems -*u* (*scipu*), nW-S 1st sg. pres. indic. -*u*
> (VP *fearu*). *o* for unprotected *u* is increasingly common in
> late texts.
>
> ***u* is always well preserved after accented *u*, e.g. *sunu*,
> *wudu*, *duguþ*; before *m*, e.g. *māþum*, d.p. -*um*, -*sum* as
> suffix; in the suffix -*ung*; in the suffix -*uc* of whatever
> origin, e.g. *beallucas*, *bulluc*, *gafeluc*, *hassuc*, *mattuc*,
> *munuc*.**

This is unambiguous. Campbell gives **four** preserving
environments, of which one is **"before *m*"** explicitly, with
the canonical examples `māþum` (n. 'treasure', a-stem), DatPl
`-um`, and the suffix `-sum`. Past plural `-on` is on the *other*
side of the divide — Campbell lists it among the "ordinary OE
forms" that show lowering.

Campbell §378 (lines 10274–10279) provides the smoking gun for
the `*m`-conditioning:

> § 378. In lW-S -*um* of the d.p. of nouns and adjs., and dat. sg.
> masc. and neut. of adjs., appears very frequently as -*on*, -*an*.
> **Presumably -*m* > -*n*, and when no longer followed by *m*,
> unaccented *u* changed to *o* (§ 373) and *a* (§ 377).** Fairly
> frequent dat. pl. in -*un* in eW-S may show the first stage of
> the change.

This is the cleanest possible empirical demonstration that the
preservation is **caused by the right-context `*m`**, not by
morphological identity of the DatPl: when `*m` is replaced by `*n`
(by the late-OE *m* > *n* shift), the same `*u` *immediately*
becomes vulnerable to the very lowering rule we are trying to
formulate, and surfaces as `-on`/`-an`. The protection travels
with the segment, not with the morph.

### 2.2. Brunner, *Altenglische Grammatik* (3rd ed. 1965), §44

Brunner is even more explicit about the rule's *form*. §44 Anm. 7
(`docs/references/brunner_1965_altenglische_grammatik.txt`,
lines 1830–1845) states:

> Anm. 7. -*u* erhält sich in der Endung -*um* und der
> Ableitungssilbe -*ung* bis ans Ende der ae. Zeit; im
> unmittelbaren Auslaut kommt spätws. zwar -*o* und später auch
> -*a* vor, doch zeigt sich selbst noch spät Schwanken zwischen
> -*u* und -*o*; nach einem -*u* der Tonsilbe bleibt es überhaupt in
> der Regel bewahrt (z. B. *wudu* Holz, *sunu* Sohn, aber *g(i)efu,
> -o* Gabe, *hofu, -o* Pl. Höfe, *ricu, -o* Reiche). **Im Inlaut vor
> anderen Konsonanten außer -*m* und -*ng* ist -*o*- im Ws. schon
> früh durchwegs durchgeführt**, nur nach einem *u* der Stammsilbe
> steht vor einfachem Konsonanten -*u*-, daher *munuc* Mönch,
> *du3uð* Tugend, aber *hēafod* Haupt, *nacod* nackt, *tun3ol* Stern
> usw.

The key clause — *"In medial position before consonants other than
-m and -ng, -o- has been carried through generally early in West
Saxon"* — is *exactly* the user's proposed rule statement, with
the additional exclusion of `-ng`. Brunner adds that an
immediately preceding stem-syllable `*u` (vowel harmony) also
preserves: `munuc`, `duguð`. These are the same four exceptions
Campbell gives.

Brunner §44 Anm. 3 (lines 1786–1801) goes further and inverts the
direction for the prehistoric stage: even PGmc `*ō` (and *o*)
became `*u` in medial syllables before `*m`, citing dative plural
`-um` from PIE `*-omis` and acc.sg. `brōðor` from urgerm.
`*brōþurun`. So `*m` is not merely a *u*-preserving environment;
it is a positively *u*-favouring environment in the broader
NWGmc/pre-OE history, with raising as well as preservation
operating in this same labial-nasal context.

### 2.3. Hogg, *A Grammar of Old English* vol. 1 (1992), §§3.3.1.3, 3.3.3.2

Hogg's §3.3.1.3 (lines 4413–4423 in the OCR) gives the principle
in a single paragraph:

> A further exception concerns the back high vowel /u/. As
> indicated above, the spelling evidence suggests that unstressed
> /u/ was normally lowered and centralised. However, **word-finally
> after another /u/, as in *sunu* 'son', or before /m/, as in the
> dative plural inflexion -um, and also in the suffix -uc, -ung,
> e.g. *munuc* 'monk', *costung* 'temptation', the <u> was normally
> preserved.** The circumstances which combined to thus protect
> the high vowel and the phonemic status of unstressed [u] are
> equally obscure, see §3.3.3.2 for further discussion.

Hogg's wording is essentially identical to Campbell §373. He
flags the *protective* environments (after stem `*u`, before `*m`,
in -uc, -ung) and characterises the phonetic/structural rationale
as **"equally obscure"** — i.e., he accepts the empirical
generalisation without committing to a specific phonetic
explanation.

§3.3.3.2 (lines 5862ff.) restates the lowering side of the rule:

> /u/ had a strong tendency to lower, especially when a consonant
> followed, so we find, for example, *heofon* 'heaven' in Early
> West Saxon rather than *heofun*, although if /u/ is in absolute
> finality, as in the nominative plural inflexion of a-declension
> neuter nouns, e.g. *scipu* 'ships', it more usually remained.
> The general rule when /u/ was followed by a consonant is that
> the later the text the more likely it is that *o*-spellings would
> prevail.

Hogg's `heofon` example is informative: the right context is
`*-an` (from PGmc `*hibanaz`, with the `*a` of the second syllable
raised before the nasal — but here the relevant `*u` is not
present, so the example is about a different vowel). The
generalisation Hogg is making, however, is "before consonants
generally", with the qualifications listed in §3.3.1.3.

⚠ §6.42–§6.45 in the user's prompt refers to the section
numbering of the *intended* manuscript (as preserved in the
typescript / second-edition pagination); in the published 1992
Cambridge volume the relevant material is at **§§3.3.1.3 and
3.3.3.2** of vol. 1 (the chapter renumbered in publication). The
substantive content is the same. Future dossier work should cite
the published §§ to avoid confusion.

### 2.4. Ringe & Taylor, *The Development of Old English* (2014), §6.9.6

Ringe & Taylor's §6.9.6 ('Mergers of unstressed vowels',
`docs/references/ringe_taylor_linguistic_history_vol2.txt`,
lines 19031ff.) is more circumspect than Campbell/Brunner/Hogg.
R&T treat the unstressed-back-vowel situation as principally one
of *mergers* (across the late 8th-10th c.), not of phonetic
*lowering* per se:

> For the most part unstressed *a* and *u* remained distinct in
> early OE (the latter often written *o*). However, they are
> beginning to be confused in 9th-century Kentish charters … and
> there are a few early WS examples of -*a* for expected -*u*. …
> By 900 the contrast between the unstressed back vowels was
> breaking down in closed final syllables in Kentish and in all
> positions, except word-finally, in WS …

In §3.1.5 (lines 4280ff.) R&T explicitly *reject* the view that
there was a regular sound change `*o → *u` before nasal
inflectional endings (their target is the *raising* direction; cf.
Brunner §44 Anm. 3). The OE distribution of `-um` vs. `-on` and
the messy class-II weak verb `-od-` ~ `-ad-` ~ `-ud-` data leads
them to favour inheritance + paradigm-internal levelling over a
clean phonetic rule:

> we have already seen that the distribution of forms does not
> support the hypothesis of an early change of *ō* to *ū* before
> indic. pl. -*un*, dat. sg. and pl. -*um* (see 3.1.5).

R&T's position is therefore an honest agnosticism about the
*phonetic* status of unstressed-vowel changes in this region —
they neither confirm nor deny a `*m`-specific protection rule, and
indeed they are skeptical that any clean phonetic rule
characterises the whole space. The empirical generalisation
(`-um` preserved, `-on` lowered) they accept; the structural
description as a phonetic conditioning is what they hesitate over.

### 2.5. Fulk, *Comparative Grammar of the Early Germanic Languages*

Fulk (vision-OCR text) treats raising/preservation before `*m` as
a NWGmc-level isogloss and a defining innovation:

> §1.8 (b) development of early PGmc. unstressed *o* to *u* before
> *m*, as in the dat. pl. inflection -*um* (Go. -*am*; §5.2)

(line 1661). And in his discussion of Old Saxon (line 5941):

> When a postconsonantal final sonorant is nuclearized, usually
> *a* is written before it, occasionally *e*, as in *wintar*
> 'winter' … *hunger* 'hunger'. **But before *m* usually *o* is
> written, occasionally *u*, as in *wastom*, -*um* 'growth'.**

— and similarly for OHG (line 5957): "a syllabified sonorant has
usually *a* written before it, but often *u* in a labial
environment, especially before *m*."

So the *m*-specific behaviour of preceding unstressed back vowels
is not just an OE oddity — it is a stable feature across the
NWGmc subgroup. This is independent corroboration that the rule
should single out `*m`.

### 2.6. Synthesis

| author | states *m*-protection? | states it as the only protector? | sharp rule? |
|---|---|---|---|
| Campbell §§373, 378 | **explicitly, twice** | one of four (after stem *u*, before *m*, -ung, -uc) | yes (§378 mechanistic) |
| Brunner §44 Anm. 7 | **explicitly** | exclusion list: *m*, *ng*, post-stem-*u* | **yes — exact rule form** |
| Hogg §3.3.1.3 | **explicitly** | one of four (after *u*, before *m*, -ung, -uc) | semi-sharp; "obscure" |
| Fulk §§1.8, §5.2 | **explicitly** for NWGmc | yes (raising/preservation context) | sharp at NWGmc level |
| R&T §6.9.6, §3.1.5 | implicit (accepts data) | agnostic | declines to formulate |

**Verdict on §2:** four of five authorities give the
*m*-conditioning explicitly, with Brunner formulating it in
essentially the same form the user proposes. R&T are the
holdout, and even they accept the empirical distribution; their
reservation is meta-theoretical (skepticism of clean phonetic
rules in this region) rather than substantive.

The user's proposal **replicates an established generalisation**.
It is not novel.

---

## §3. The DatPl `-um` problem in detail

The companion dossier `dossier-datpl-um-vs-om-2026.md`
established that:

1. PGmc DatPl is stem-specific: `*-amaz` (a-stem), `*-ōmaz`
   (ō-stem), `*-umiz`/`*-umaz` (u-stem, weak n-stem,
   consonant-stem).
2. For a-/ō-stem cases the suffix `*a`/`*ō` is **raised** to `*u`
   before tautosyllabic nasal in pre-OE — the well-known
   `*-am > *-um` raising (Campbell §378, §472; Hogg §6.58;
   Brunner §44 Anm. 3).
3. The result is uniform OE `-um` across all stem classes.

The further evidence assembled in §2 above answers the question
left open in the companion dossier — *why* the inherited
u-stem-type `*-um` resists lowering. **It resists because `*m`
is itself the protective factor.** Campbell §378 makes this
explicit with the *m* > *n* > lowering chain in late West Saxon.
The DatPl is not "morphologically protected" — it is
*phonetically* protected by the labial nasal, and the moment that
nasal is replaced (whether by *m* > *n* in lW-S or by the general
late-OE collapse), the protection vanishes and `-on`/`-an`
spellings appear.

This is a clean diagnostic: if DatPl `-um` were morphologically
restored from earlier `-om`, we would expect the late-OE
spellings to *retain* `-um` (paradigm uniformity), not to
collapse to `-on`/`-an`. Their collapse, *coincident with the
loss of `*m`*, confirms the phonetic-conditioning analysis.

---

## §4. Past plural `-on` for contrast

PGmc strong-verb 3pl preterite `*-un`. OE outcome uniformly `-on`
in classical/late texts; `-un` preserved in early Northumbrian
(Campbell §373: "very rarely -*on*" in early texts; "ordinary OE
forms are … past indic. pl. -*on*").

Campbell §373 places past-pl `-on < *-un` squarely on the
*lowering* side of the rule, alongside `hēafod`, `heofon`,
`tungol`, weak past `-ode`, and superl. `-ost`. The right
context in `-un` is `*n`, which Campbell does *not* list among the
protective environments. Brunner §44 Anm. 7 likewise has `*n`
implicitly in the lowering set ("vor anderen Konsonanten außer
-*m* und -*ng*").

So the *m*/*n* asymmetry is **explicitly drawn by both Campbell
and Brunner** in their statements of the rule. There is no
controversy here in the standard sources.

### 4.1. Counterexamples to lowering before `*n`?

The user asks whether there are forms where unstressed `*u`
before `*n` is *preserved*. The candidates worth considering:

* `duguþ`, `iuguþ`/`ġeoguþ` — these have **lengthened** root
  vowels (NSL or compensatory; Campbell §282) and the `*u` is
  long, hence outside the rule's scope. Already commented in our
  cascade.
* `tācn`, `wǣpn`, `bēacn` — `n` here is post-syncope syllabic,
  not the right-context consonant of an `*u + n` sequence. Not
  diagnostic.
* `cyning`, `helming`, `þēoden` — here too the vowel is `*i`/`*e`,
  not `*u`.

There are no clean counterexamples; the rule "lower `*u` before
`*n`" is empirically robust.

### 4.2. The `*-und` cluster reconstruction

The user asks about an alternative reconstruction in which the
3pl preterite was `*-und` (retaining the PIE/PGmc `*-nt`),
yielding a closed-syllable conditioning rather than an `*m`/`*n`
asymmetry. The mainstream view (Ringe 2017: 264; R&T 2014 ch. 4;
Fulk passim) reconstructs `*-un`. The `*-und` view does not
appear in any of the OE-grammar sources surveyed in §2 and is not
needed to explain the data. We **do not endorse** the cluster
reanalysis as a substitute for the *m*/*n* asymmetry.

---

## §5. Other -m forms in OE

To test whether the *m*-protection generalises beyond DatPl `-um`:

### 5.1. The handbooks' own example list

Campbell §373 explicitly lists **three** unstressed-*u*-before-*m*
environments as protective:

* DatPl inflection `-um`
* the noun `māþum` 'treasure' (lit. 'gift'; cf. Goth `maiþms`,
  with epenthetic vowel — see §5.4 below)
* the suffix `-sum` (e.g. `wynsum` 'pleasant', `lufsum` 'lovely',
  `ealdorsum`)

Hogg §3.3.1.3 lists DatPl `-um` only (combined with -uc, -ung).

Brunner §44 Anm. 7 lists `-um` and `-ung`; in §44 Anm. 3 he adds
`brōðor` (acc.sg.) from urgerm. `*brōþurun` as evidence for the
broader *m*-favouring history.

Fulk §1.8, §5.2 generalises across NWGmc, citing OS *wastom*,
OHG *-um* parallels.

### 5.2. The superlative ending `-uma`

PGmc `*-umô`/`*-umaz` (cf. Goth `auhumists`, OHG *obaro*). OE
`-uma` (`forma`, `hindema`, `medema`, `nēahuma`). In classical
OE the `*u` before `*m` is preserved as `u`, consistent with the
rule. ✓

(Campbell §659 covers the superlative; Brunner §319 ff.)

### 5.3. The `-sum` suffix

Campbell §373 gives this as a clean preservation case:
`hwitsum`, `lēofsum`, `wynsum`, `lufsum`, `langsum`. ✓

### 5.4. Epenthetic-vowel cases (`māþum`, `bōsm`, `wæstm`, `botm`)

* `māþum` / `māððum` (PGmc `*maiþmaz`, Goth `maiþms`): the medial
  vowel between `*þ` and `*m` is epenthetic, inserted to break
  the cluster. The vowel is consistently `u` (and sometimes `o`
  in late texts): Campbell §373 cites it as a clean
  *m*-preservation case, treating the epenthetic vowel itself as
  inserted with high quality. Fulk (line 7644) notes
  "Gemination before *m* occurs in lW-S *māþþm* beside *māþm*
  'treasure'" — confirming that *m* is the conditioning segment.
* `bōsm` (PGmc `*bōsmaz`): root vowel is long `ō`; the
  consonantal cluster is broken by an epenthetic vowel late, and
  this surfaces variably as `o` or `u`. Not diagnostic for the
  short-`*u` rule.
* `wæstm`, `botm`: same epenthetic-vowel situation. Not directly
  diagnostic.

These epenthetic cases do **not** undermine the *m*-protection
rule (the epenthetic vowel is a *consequence* of stem-final *m*
needing nuclearization, not an instance of inherited unstressed
`*u`). But they do show that the *m* environment is consistently
associated with `u` quality of the inserted vowel — which is
again consistent with §2.5's NWGmc generalisation.

### 5.5. The 1Sg pres. and 1Pl pres. endings

The 1Sg pres. ind. of strong verbs derives from PGmc `*-ō` (with
`*-am(i)` only in some weak classes, replaced in OE). The 1Pl
pres. ind. ending in OE is `-aþ` (innovative, from earlier 3pl).
Pre-OE 1Pl `*-um(i)` (cf. Goth `-am`, OHG `-em`/`-um`) was
**replaced analogically** by `-aþ`. So neither is a synchronic
test in OE, though pre-OE `*-um(i)` would have shown preservation
of `*u` before `*m` by the proposed rule.

### 5.6. Acc.sg. of consonant stems: `brōðor`

Brunner §44 Anm. 3 cites: urgerm. `*brōþurun` > acc.sg.
`brōðor` (with `-or` < `-ur` and ultimately *m*-favoured `*u`
quality at the relevant stage). The example is somewhat
indirect, but it falls in line.

### 5.7. Summary of -m forms

| form | source | medial *u + *m? | preserved? | clean test? |
|---|---|---|---|---|
| DatPl `-um` | PGmc `*-um(iz)` / `*-am(iz)` raised | yes | yes | ✓ canonical (Campbell §373) |
| superlative `-uma` | PGmc `*-umô` | yes | yes | ✓ |
| `-sum` suffix | PGmc `*sumaz`/agreement | yes | yes | ✓ (Campbell §373) |
| `māþum` | epenthetic between `*þ`/`*m` | quasi (epenthetic) | yes (consistently `u`) | ✓ (Campbell §373) |
| `bōsm`, `wæstm`, `botm` | epenthetic | epenthetic | yes (variable `u/o`) | partial |
| pre-OE 1Pl `*-um(i)` | PGmc `*-amaz` raised | yes | yes (then replaced analogically) | ✓ pre-OE only |
| acc.sg. `brōðor` | urgerm. `*brōþurun` | yes | yes (`u` then late `o`) | ✓ |

**Every diagnostic case shows preservation.** No early-OE form
of medial unstressed `*u` before `*m` lowers to `*o` until the
late-OE collapse (Campbell §378) when `*m` itself is replaced by
`*n`.

---

## §6. Alternative analyses considered

### 6.1. Phonetic conditioning by `*m` (the proposal)

**"Unstressed `*u` lowers to `*o` before consonants, except
before `*m`."**

* Empirical fit: ✓ DatPl `-um`, superlative `-uma`, `-sum`,
  `māþum`, past-pl `-on`, weak past `-ode`, `hēafod`, `heofon`,
  `tungol` all fit.
* Author support: Campbell §§373, 378 (explicit and mechanistic);
  Brunner §44 Anm. 7 (explicit, in the user's exact form);
  Hogg §3.3.1.3 (explicit, "obscure" rationale); Fulk §§1.8,
  §5.2 (NWGmc-level).
* Phonetic rationale: labial-nasal articulation favours retention
  of preceding high-back vowel. Hogg calls this "obscure"; Fulk
  treats it as a stable NWGmc isogloss; Brunner offers no
  rationale. The phonetics is empirically robust, not
  theoretically forced.

### 6.2. Morphological protection (paradigm uniformity)

**"Lowering applies generally; DatPl `-um` is analogically
restored from `*-om` under paradigm-uniformity pressure."**

* Empirical fit: requires positing an unattested `*-om` stage.
* The decisive disconfirmation is **Campbell §378**: when `*m`
  becomes `*n` in lW-S (a phonetic change unrelated to the DatPl
  morphological cell), the DatPl *immediately* shows lowering to
  `-on`/`-an`. Paradigm-uniformity protection should hold across
  this change; it does not. Hence the protection is segmental,
  not morphological.
* No author surveyed posits the morphological-restoration
  account.

### 6.3. Chronological / cluster-based reconstruction

**"Past-pl `*-un` was originally `*-und`; cluster context
triggered lowering before cluster simplification."**

* Author support: not in any of Campbell, Brunner, Hogg, R&T,
  Fulk for OE. (R&T 2014 §3.1.5 explicitly works with `*-un`,
  not `*-und`.)
* Cannot extend to `māþum`, `-uma`, `-sum`.
* **Rejected.**

### 6.4. Vowel harmony / preceding-syllable conditioning

The cascade's current rule already excludes preceding `*u`/`*ū`
from the trigger context (vowel harmony: `munuc`, `wudu`,
`duguþ`). This is real (Campbell §373 second clause; Brunner §44
Anm. 7 last clause; Hogg §3.3.1.3 first clause). But the
*m*/*n* asymmetry is **independent** of the preceding-vowel
effect: `dagum` has preceding `*a` and `-um` is preserved;
`bugon` has preceding long `*ū` and `-on` is lowered. So vowel
harmony does *not* substitute for the *m*-exclusion; both
conditions must be encoded.

### 6.5. Stress / next-syllable conditioning

In all the relevant forms there is no following syllable
(post-apocope, post-loss-of-`*-iz`/`*-az`); the rule fires
word-finally. Stress of the next syllable is not a live
parameter for these forms.

For non-final cases (e.g. `heofon` < `*hibanaz`, `tungol` <
`*tunglaz`), Campbell §373 lists them on the *lowering* side, with
right context `*n`/`*l` respectively. Medial `*u` before `*m`
non-finally (e.g. `māþum` with `m` not strictly final but in a
mono-suffix word) is preserved. The asymmetry holds.

---

## §7. Verdict on the *m exclusion proposal

**The proposal — "narrow OEMedUnstressedULowering to exclude `*m`
from the right-context consonant slot" — is the explicit
formulation in Brunner §44 Anm. 7, and is consistent with
Campbell §§373, 378, Hogg §3.3.1.3, and Fulk §§1.8, §5.2. It is
NOT novel.**

The narrower verdict on the *form* of the rule:

* **Brunner §44 Anm. 7** writes the rule as: lowering applies
  before all consonants **except `-m` and `-ng`** (and is blocked
  if the preceding stem syllable contains `*u`).
* **Campbell §373** writes it as a positive list of preserving
  environments: after stem `*u`; before `*m`; in `-uc`; in `-ung`.
  The lowering side is the complement.
* **Hogg §3.3.1.3** is in essential agreement with Campbell, with
  no specific phonetic rationale offered.
* **Campbell §378** provides the diagnostic mechanism: when `*m`
  is segmentally lost (lW-S `*m` > `*n`), the *u*-preservation
  vanishes.
* **R&T §6.9.6** are agnostic on the rule's *form* but accept the
  data.
* **Fulk §§1.8, §5.2** confirms `*m` as a *u*-favouring
  environment at the NWGmc level.

### 7.1. Recommended cascade implementation

The `OEMedUnstressedULowering` rule should be narrowed to:

```
{*u} -> {*o} || [EnglishStarVocalic - [{*u}|{*ū}]]
                [EnglishStarConsonant | EnglishPalatalConsonant]+
                _
                [EnglishStarConsonant - {*m} | EnglishPalatalConsonant]
```

i.e., exclude `*m` from the right-context consonant set (and keep
the existing exclusion of preceding stem `*u`/`*ū`). Optionally,
following Brunner §44 Anm. 7, also exclude `*ng` — this would
correctly preserve the `-ung` suffix (Campbell §373: `costung`).
The `-uc` suffix preservation (Campbell §373: `munuc`,
`gafeluc`, `mattuc`) is independent: it follows from a preceding
stem `*u` (vowel-harmony exclusion already encoded) in `munuc`,
`bulluc`; for `mattuc`, `gafeluc`, `hassuc`, `beallucas`, the
preservation of `*u` before `*c` is an additional fact that
Campbell calls out without explanation, and may need a separate
narrow-context exclusion if the cascade lexicon includes such
forms.

### 7.2. Recommended documentation comment for the rule

```
# OEMedUnstressedULowering (Campbell §§373-374, §378;
# Brunner §44 Anm. 7; Hogg 1992 §3.3.1.3, §3.3.3.2;
# Fulk §§1.8, §5.2 for the NWGmc background).
#
# Medial unstressed *u lowers to *o before any consonant other
# than *m. This encodes the well-attested asymmetry between
# preserved DatPl -um, superlative -uma, suffix -sum, mā}um
# (all with *m in right context) on the one hand, and lowered
# past-pl -on, weak past -ode, hēafod, heofon, tungol (all with
# non-*m right context) on the other.
#
# The *m exclusion is segmental, not morphological: cf. Campbell
# §378, who shows that when *m > *n in lW-S the protection of
# *u disappears and -um surfaces as -on/-an. The rule therefore
# fires on segmental conditions, not paradigm cells.
#
# Vowel harmony: lowering is also blocked when the preceding
# stem syllable contains *u or *ū (munuc, wudu, du3uð). This
# is independent of the *m exclusion and is encoded in the
# left context.
#
# Optional: Brunner §44 Anm. 7 also excludes *ng (suffix -ung;
# Campbell §373 cites costung as preserved). If the lexicon
# contains -ung-suffixed forms, add *ng to the excluded right
# context.
```

### 7.3. What the proposal does *not* claim

The proposal should **not** be characterised as:

* A discovery; it is a re-statement of Brunner §44 Anm. 7.
* A complete account of OE unstressed-vowel reduction; the
  late-OE collapse (Campbell §378–§379, Hogg §3.3.3.2 final
  paragraphs, R&T §6.9.6) is post-classical and orthogonal.
* A claim about typological universality; some Germanic
  varieties (Old Saxon -un past-pl, OHG variation) show
  different surface patterns, but these are addressed at the
  language-specific level (Fulk).

### 7.4. Caveats

* Hogg's section reference in the user's prompt (§§6.42–6.45)
  appears to be from an alternate / draft numbering; the
  published 1992 *Grammar of Old English* vol. 1 places this
  material at §§3.3.1.3 and 3.3.3.2. Cite §§3.3.1.3, 3.3.3.2
  in our documentation.
* Brunner §44 Anm. 7 also excludes `-ng`; whether to encode this
  in the cascade depends on whether the lexicon contains
  `*-ung`-suffixed forms with medial unstressed `*u` in the
  relevant configuration. The user should audit.
* R&T's skepticism about clean phonetic rules in the
  unstressed-vowel region (§6.9.6) is a methodological caveat,
  not a substantive disagreement with the *m*/*n* data. It does
  not undermine the proposed rule.

---

## §8. Bibliography (with primary-source citations used)

* **Campbell, Alistair** (1959). *Old English Grammar.* Oxford:
  Clarendon. — **§ 373** (preservation of unaccented `*u` after
  stem `*u`, before `*m`, in -uc, -ung; with the lists `māþum`,
  d.p. -um, -sum, *beallucas*, *bulluc*, *gafeluc*, *hassuc*,
  *mattuc*, *munuc*); **§ 374** (same change `*u > *o` in
  obscured compounds); **§ 378** (lW-S -*um* > -*on*/-*an* via
  `*m > *n` and consequent loss of *u*-protection — the
  mechanistic smoking gun); §§369–389 surrounding context;
  §§331–333 (early developments). Local copy:
  `docs/references/campbell_old_english_grammar.txt`.
* **Brunner, Karl** (1965). *Altenglische Grammatik nach der
  angelsächsischen Grammatik von Eduard Sievers.* 3rd ed.
  Tübingen: Niemeyer. — **§ 44 Anm. 7** ("Im Inlaut vor anderen
  Konsonanten außer -*m* und -*ng* ist -*o*- im Ws. schon früh
  durchwegs durchgeführt"); **§ 44 Anm. 3** (germ. `*ō > u`
  before `*m` in medial syllables; `*brōþurun > brōðor`); §§43,
  45 surrounding context. Local copy:
  `docs/references/brunner_1965_altenglische_grammatik.txt`.
* **Hogg, Richard M.** (1992). *A Grammar of Old English. Volume
  1: Phonology.* Oxford: Blackwell. — **§ 3.3.1.3** (preservation
  of unstressed `/u/` after another `/u/`, before `/m/`, and in
  -*uc*, -*ung*; rationale "obscure"); **§ 3.3.3.2** (general
  lowering of `/u/` before consonant; chronology and dialect
  geography of the late-OE collapse). Local copy:
  `docs/references/hogg_vol1.txt`.
  *(Note: the user's prompt references §§6.42–6.45; the
  published numbering is §§3.3.1.3, 3.3.3.2.)*
* **Ringe, Donald A. & Ann Taylor** (2014). *The Development of
  Old English.* Oxford: OUP (= *A Linguistic History of English*
  vol. 2). — **§ 6.9.6** (Mergers of unstressed vowels; accepts
  empirical distribution but is methodologically wary of clean
  phonetic rules); **§ 3.1.5** (rejects regular `*ō > *ū` raising
  before nasal as a sound change; favours inheritance + analogy).
  Local copy: `docs/references/ringe_taylor_linguistic_history_vol2.txt`.
* **Fulk, R. D.** (2018). *A Comparative Grammar of the Early
  Germanic Languages.* Amsterdam: Benjamins. — **§ 1.8 (b)**
  (NWGmc *o > u* before *m* as defining isogloss); **§ 5.2**
  (PGmc `*-omiz > *-umiz` in DatPl); §5.6 (broader unstressed-
  vowel typology). Local copy:
  `docs/references/fulk_comparative_grammar_early_germanic.vision.txt`.
* **Ringe, Donald A.** (2017). *From Proto-Indo-European to
  Proto-Germanic.* 2nd ed. Oxford: OUP. — pp. 264 (3pl preterite
  `*-un` reconstruction); paradigm tables. Local copy:
  `docs/references/ringe_vol1_pie_to_pgmc.txt`.

### Companion dossiers in this repo

* `Germanic/docs/dossier-datpl-um-vs-om-2026.md` — establishes
  that early-OE DatPl `-um` has no `*-om` stage; the cascade's
  `*-um → -om` output is a misapplication, not a defensible
  intermediate. The present dossier identifies the *fix*:
  exclude `*m` from the lowering rule's right context.
* `Germanic/docs/dossier-shoulder-paradigm-survey-2026.md` —
  selects the masc. a-stem DatPl `*skuldr-um(iz)` ↔ `sċuldrum`
  cell-pair as the only one preserving root /u/ lautgesetzlich.
* `Germanic/docs/dossier-shoulder-lautgesetz-2026.md` and
  `dossier-shoulder-cellchoice-2026.md` — broader paradigm
  context for the `shoulder` row that triggered this work.

---

## §9. Honest residual uncertainty

1. **Hogg section numbering.** The user's prompt cites
   §§6.42–6.45 of Hogg vol. 1; the published 1992 volume places
   the relevant material at §§3.3.1.3 and 3.3.3.2. The
   discrepancy is presumably a draft/edition issue. The
   substantive content is identical, and the citations in the
   recommended rule comment (§7.2) use the published numbering.
2. **`-ng` exclusion.** Brunner §44 Anm. 7 also excludes `-ng`
   (suffix -*ung*) from the lowering context. Whether to
   encode this in the cascade depends on the lexicon. If
   `-ung`-suffixed verbal abstracts are present, add `*ng` to
   the excluded right context. Campbell §373 lists -*ung* as
   preservative without further qualification.
3. **`-uc` suffix.** Campbell lists -*uc* (`mattuc`, `gafeluc`,
   `hassuc`, `beallucas`, `bulluc`, `munuc`) as preservative.
   For `munuc`, `bulluc` the preservation falls out of the
   preceding-stem-`*u` exclusion (vowel harmony, already
   encoded). For `mattuc`, `gafeluc`, `hassuc`, the preservation
   does not fall out and would require a further exclusion
   (`*c` from the right context, perhaps). This is a *separate*
   issue from the *m*-exclusion at hand and is flagged here for
   future dossier work.
4. **R&T's methodological reservation.** Ringe & Taylor §6.9.6
   are skeptical that clean phonetic rules can characterise the
   unstressed-vowel space. We accept their data and proceed with
   the rule as stated by Campbell/Brunner/Hogg, but the cascade
   should be aware that some surface forms (especially
   class-II weak past `-od-` ~ `-ad-` ~ `-ud-`) may need
   independent treatment beyond OEMedUnstressedULowering.
5. **Late-OE/Anglian data.** The proposed rule applies to
   classical/early OE. Late-OE (post-c. 950) and Northumbrian
   show interchangeable `-um`/`-on`/`-an`/`-em` spellings
   (Campbell §378–§379; Hogg §3.3.3.2 final paragraphs; R&T
   §6.9.6). If the cascade models a late-OE / pre-ME stage, the
   *m*-exclusion will need to be relaxed at that stage.
