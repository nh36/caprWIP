# Does *w* block OE medial unstressed `*u → *o`? The `widuwe` problem

A focused source-canvassing dossier for the FST cascade modelling
PGmc → OE. Companion to `Germanic/docs/dossier-medial-u-lowering-conditioning-2026.md`,
which established the `*m` exclusion in `OEMedUnstressedULowering`.
This dossier asks whether the same exclusion should be extended to
`*w` (or to all labials) on the grounds that the OE attested
**`widuwe`** (PGmc *widuwōn-) preserves the medial `*u`, while the
cascade currently lowers it to `*o`, producing `*widowe`.

---

## §1. TL;DR

1. **`*w` does NOT block medial `*u`-lowering.** No handbook in the
   surveyed corpus (Campbell, Brunner, Hogg, Ringe & Taylor, Bülbring,
   Luick) lists `*w` as a preserving environment. Campbell §365 in fact
   provides direct *counter*-evidence: parasite `-uw-` sequences
   regularly lower per §373, so `beaduwe → beadowe`, `swaluwan →
   swalewan`. Extending the exclusion to `*w` (or to all labials)
   would be unsupported and would over-generate `-uw-` preservations
   that the handbooks explicitly say are lowered.

2. **`widuwe` is not the regular Lautgesetz outcome.** The handbook
   tradition (Brunner §114b, Bülbring §264, Luick §221 Anm. 1) treats
   `widuwe` as **analogically restored**. The phonetically expected
   outcomes from PGmc *widuwōn- are:
   * **Anglian:** `widwe` (regular early syncope of medial `*u`).
   * **West Saxon:** `wuduwe` (combinative u-umlaut / "verstärkter
     Velarumlaut" `wi` → `wu`, then medial `*u` preserved by the
     stressed-`*u` left-context exclusion that the cascade already
     encodes).
   * **Late WS:** `weodowe` (< *wioduwe; medial `*u` HAS lowered to
     `*o` here, exactly as the cascade rule predicts).
   * **Aelfric:** `widewe` (medial `*u` lowered/raised one step
     further, by Campbell §385).

   Late-WS `widuwe` (~ `wyduwe`) is, per Brunner and Luick, an
   analogical compromise between syncopated `widwe` and unsyncopated
   `wuduwe`: stressed-syllable `i` of `widwe` carries over and
   "restores" a medial `u` after `-d-`. R&T (2014: 270, 322) merely
   list `widuwe` alongside `wuduwe` as a WS variant without
   committing to a derivational explanation.

3. **The cascade rule is correctly stated.** The mismatch
   `*wíduwōn → *widowe` vs. attested `widuwe` is a TSV / lexical /
   analogical problem, not a rule problem. The cascade output
   `widowe` is essentially identical to attested late-WS `weodowe`
   modulo the realisation of the root vowel (which the cascade
   handles separately via combinative u-umlaut / back-mutation rules).

4. **Recommendation.** Do **not** extend `OEMedUnstressedULowering` to
   exclude `*w`. The fix belongs at the TSV layer:
   add `*wíduwōn` to `Germanic/data/oe_known_problems.tsv` as
   `analogical_paradigm_levelling` (Luick §221 Anm. 1: "widuwe nach
   widwe"), or switch the protoform to `*wúduwōn` so the existing
   stressed-`*u` left-context exclusion preserves the medial `u`
   regularly (yielding `wuduwe`, the genuinely Lautgesetz WS form).

---

## §2. Per-handbook verbatim quotations

### 2.1. Campbell, *Old English Grammar* (1959)

#### §218 — combinative u-umlaut (root-vowel realization)
`docs/references/campbell_old_english_grammar.txt:6580–6604`:

> In W-S many forms have combinative u-umlaut of *i*, and the change
> seems not to be limited, like u-umlaut, to positions before liquids
> and labials, e.g. **wudu** wood, **wuduwe** widow, **wucu** week …
> but there occur also in many cases forms with *io* (*eo*) or *i*,
> e.g. **weoduwe**, **widuwe**, *wicu*, *cwicu* … VP **widwe**,
> wuton (let us); … North. … but **widwe**, …

Campbell here treats `wuduwe ~ widuwe ~ weoduwe ~ widwe` as four
**variants of root-vowel realisation** under combinative u-umlaut.
He does *not* address the medial `-u-` directly here; the variants
all retain `-u-` in this passage simply because Campbell is
illustrating the root-vowel reflex.

#### §365 — parasite vowel `-uw-` lowers
`docs/references/campbell_old_english_grammar.txt:10014–10033` (decisive):

> Especially W-S, … is a tendency to develop *j* and *u* after a
> short syllable to *ij*, *uw*, e.g. *herigas* armies, *herigan*
> praise, … *gearuwe* n.p. ready, **beaduwe** d.s. battle,
> **seonuwa** n.p. sinews, *swaluwe* swallow. *ij* can be
> monophthongized to *i* … . **By §§ 373, 385, *u* often appears as
> *o* and *e*, e.g. *beadowe*, *swalewan*; less frequent is *e* for
> *i* …**

This is the smoking gun for `*w` *not* being a blocker:
Campbell explicitly says that the parasite `*u` in the `-uw-`
sequence undergoes the very `*u → *o` lowering of §373, with the
canonical examples `beadowe`, `swalewan` — both with `*w` as the
right-context consonant.

#### §373 — preservation list (no *w*)
`docs/references/campbell_old_english_grammar.txt:10223–10226`:

> *u* is always well preserved after accented *u*, e.g. *sunu*,
> *wudu*, *dugup*; **before *m***, e.g. *māþum*, d.p. -*um*, -*sum*
> as suffix; in the suffix -*ung*; in the suffix -*uc* of whatever
> origin …

Four protective environments. **`*w` is not among them.**

#### Index entries
`docs/references/campbell_old_english_grammar.txt:34211, 33934`:

> **wuduwe** see widuwe.
> g.p. **widuwana** 218.

i.e., Campbell's master entry is under `widuwe` but `wuduwe` is
treated as the cross-reference target — an editorial choice
consistent with Campbell's wording at §218 ("In W-S … wudu, wuduwe").

### 2.2. Brunner, *Altenglische Grammatik* (3rd ed. 1965)

#### §114b — explicit "widuwe is analogical"
`docs/references/brunner_1965_altenglische_grammatik.txt:4671–4675`:

> Angl. **widwe** (L, Rit. R 2 , Vesp. Ps.) neben ws. **wuduwe**
> Witwe ist durch frühe Synkope zu erklären. Durch Ausgleich
> zwischen synkopierten und nicht synkopierten Formen ist spätws.
> **widuwe**, **wyduwe** (mit y nach § 116) und **weodowe** (aus
> *wioduwe) mit gewöhnlichem Velarumlaut zu erklären.

Translation: "Anglian **widwe** (L, Rit., R², Vesp. Ps.) beside WS
**wuduwe** 'widow' is to be explained by early syncope. By analogical
levelling between syncopated and unsyncopated forms, late-WS
**widuwe**, **wyduwe** (with *y* per §116), and **weodowe** (from
*wioduwe with ordinary back-umlaut) are to be explained."

This is **explicit**: Brunner derives `widuwe` and `weodowe` as
**analogical / leveled** forms, not as direct Lautgesetz reflexes.
The two Lautgesetz outcomes are: Anglian `widwe` (with syncope) and
WS `wuduwe` (with combinative u-umlaut of root `wi → wu` and medial
`u` preserved by following stressed-`*u` left context — vowel
harmony).

#### §44 Anm. 7 — preservation list (no *w*)
`docs/references/brunner_1965_altenglische_grammatik.txt:1830ff`
(quoted in companion dossier `dossier-medial-u-lowering-conditioning-2026.md`
§2.2, lines 117–141):

> Im Inlaut vor anderen Konsonanten **außer -m und -ng** ist -o- im
> Ws. schon früh durchwegs durchgeführt …

Brunner's exclusion list is **`m`, `ng`, and post-stem-`u`**. *No
mention of `w` or labials as a class.*

### 2.3. Hogg, *A Grammar of Old English* vol. 1 (1992)

#### §3.3.1.3 — preservation list (no *w*)
`docs/references/hogg_vol1.txt:4413–4423`:

> However, word-finally after another /u/, as in **sunu** 'son', or
> **before /m/**, as in the dative plural inflexion -*um*, and also
> in the suffix -*uc*, -*ung*, e.g. **munuc** 'monk', **costung**
> 'temptation', the <u> was normally preserved.

Identical structural list to Campbell §373: `_u`, `_m`, `-uc`,
`-ung`. **No `*w`, no labials as a class.**

Hogg has no dedicated discussion of `widuwe`; the only occurrence
in vol. 1 is at line 24943 ("father to the widows") in a discussion
of poetics.

### 2.4. Ringe & Taylor, *The Development of Old English* (2014)

#### p. 270 — `widuwe` listed under "i, u, y not syncopated"
`docs/references/ringe_taylor_linguistic_history_vol2.txt:15565–15571`:

> A large number of examples show that *i, *u, and *y (the i-umlaut
> product of *u) were not syncopated after light syllables. They
> include isolated and opaquely derived words … e.g.:
>
> PGmc *widuwon- 'widow' (Goth. widuwo, OF widwe, OS widowa, OHG
> wituwa) > *widuwe > OE **widuwe**;

R&T treat `widuwe` here as the regular outcome of "non-syncope"
under their account — i.e., they posit no medial-`*u`-lowering rule
that would affect it. Their account is *agnostic* about whether the
medial `*u` is preserved by Lautgesetz or by analogy; they simply
list both outcomes.

#### p. 322 — explicit dialect distribution
`docs/references/ringe_taylor_linguistic_history_vol2.txt:18457–18467`:

> When *w* preceded *i* in a back-umlauting environment, *i* often
> became *u* in all the dialects regardless of what consonant
> followed. The following examples have unproblematic etymologies:
>
> PGmc *widuwon- (Goth. widuwo) > PWGmc *widuwa (OF widwe, OS
> widowa, OHG wituwa) > **WS OE wuduwe ~ widuwe, but Merc. widwe,
> North. widua**;

R&T's framing here is again about the **stressed-syllable** *i → u*
shift (combinative u-umlaut). They treat `wuduwe ~ widuwe` as
co-existent WS variants without explicitly endorsing or rejecting an
analogical account; cf. Brunner §114b for the analogical reading.

R&T's broader §6.9.6 (lines 19031ff, "Mergers of unstressed vowels")
is methodologically wary of clean phonetic rules in unstressed-vowel
space. They neither posit a rule that would lower the medial `*u` in
`*widuwe` nor one that would preserve it before `*w`.

### 2.5. Bülbring, *Altenglisches Elementarbuch* (1902) §264

`docs/references/bulbring_altenglisches_elementarbuch.txt:5407–5419`:

> wudu 'Holz' aus *wiudu (<*widu, ahd. witu), ws. **wuduwe** 'Witwe'
> (angl. **widwe** und bei Aelfric **widewe** ohne u-Umlaut), wuluc
> 'Purpurschnecke', swutol 'klar', wuton 'wohlan', ws. swustur
> swuster Ru.¹ swuster 'Schwester' (aus *swistur)…

Bülbring's three named OE forms are:
* WS **wuduwe** (the regular Lautgesetz outcome with combinative
  u-umlaut);
* Anglian **widwe** (regular with syncope);
* Aelfric **widewe** (with `i` preserved as in `widwe` and the
  medial `u` then **lowered to `e`** — exactly the §373/§385 cascade
  rule firing before `*w`!).

Bülbring's `widewe` confirms Campbell §365: the medial `*u` in `-uw-`
does lower in some texts. There is no `*w`-blocker.

### 2.6. Luick, *Historische Grammatik der englischen Sprache*

`docs/references/luick_historische_grammatik.txt:12779`:

> … durch Übertragungen wurde auch sonst manchmal i wieder
> hergestellt: … **widuwe nach widwe**; …

Luick §221 Anm. 1, the four-word version: **"widuwe nach widwe"** —
"`widuwe` (modelled) on `widwe`". This is the cleanest possible
statement: `widuwe` is analogically formed from `widwe`, not a direct
Lautgesetz outcome. He also lists (line 12886, 12976):

> kent. wiodu, Cp. wioluc, altws. swiotol (neben swutol), wioton
> (neben witon Anm. 3), ***wioduwe (woraus später weoduwe)**.

i.e., late-WS `weoduwe ~ weodowe` is reconstructed as deriving from
*wioduwe via the *ordinary* (gewöhnliche) back-umlaut. The medial
`*u` in `weodowe` has thus already lowered to `*o` — again
consistent with `*w` not being a blocker.

### 2.7. Sievers / Brunner (1965) §44

The companion dossier already canvasses §44 in full. There is no
clause about `*w` or labials as a class; the only excluded
right-context consonants in §44 Anm. 7 are `*m` and `*ng`.

### 2.8. Synthesis table

| author | lists `*w` as preserver? | analogy account for `widuwe`? | Lautgesetz outcome of *widuwōn |
|---|---|---|---|
| Campbell §218, §365, §373 | **no** (§373 list explicitly omits *w*; §365 shows `-uw- → -ow-` regularly) | implicit (lists wuduwe as headword) | `wuduwe` (WS), `widwe` (Angl.) |
| Brunner §44 Anm. 7, §114b | **no** | **explicit** (§114b: "Ausgleich zwischen synkopierten und nicht synkopierten Formen") | `wuduwe` (WS), `widwe` (Angl.) |
| Hogg §3.3.1.3 | **no** | not addressed | not specified |
| R&T 2014: 270, 322 | **no** (no rule posited) | not committed | `wuduwe ~ widuwe` (WS); `widwe` (Merc.); `widua` (North.) |
| Bülbring §264 | **no** | implicit (gives `widewe` with lowered medial *u*) | `wuduwe` (WS), `widwe` (Angl.) |
| Luick §221 Anm. 1 | **no** | **explicit** ("widuwe nach widwe") | `wuduwe` (WS), `widwe` (Angl.); `widuwe` analogical |

**Verdict:** zero of six authorities posit a `*w`-blocker. Two
(Brunner, Luick) explicitly state that `widuwe` is analogical.

---

## §3. Phonological vs. morphological/lexical analysis

### 3.1. The phonological null hypothesis

Apply `OEMedUnstressedULowering` (Campbell §373) as currently
formulated. From `*wíduwōn` (or `*widuwōn`):

* Step 1 (combinative u-umlaut, "verstärkter Velarumlaut"; Bülbring
  §264, Luick §221, Campbell §218): root `*wi-` → `*wu-` in WS, but
  not in Anglian or Mercian. The cascade does this in
  `OEBackMutation` family.
* Step 2 (medial unstressed `*u`-lowering, Campbell §373): in the
  resulting `*wuduwe` the left context contains stressed `*u`, so
  the existing **vowel-harmony left-context exclusion** of the rule
  blocks lowering. Output: `wuduwe`. ✓
* Step 2′ (alternative: if Step 1 doesn't apply, e.g. Anglian-style
  derivation): root remains `*wi-`, left context is stressed `*i`,
  vowel-harmony exclusion does **not** apply, medial `*u` lowers
  before `*w`. Output: `*widowe`.

The cascade currently runs on `*wíduwōn` (no combinative u-umlaut
applied to the stressed root) and produces `*widowe` — which is
phonetically the Anglian-derivation outcome with one further OE
lowering step. This is **a valid Lautgesetz reflex**, just not the
WS form selected by the TSV target.

### 3.2. The analogical / paradigm-uniformity hypothesis

Brunner §114b and Luick §221 Anm. 1 derive late-WS `widuwe` as a
paradigm-internal compromise:

* Mercian / Anglian inherits the syncopated form `widwe` (with
  preserved root `i` because no combinative u-umlaut applies).
* WS inherits the unsyncopated form `wuduwe`.
* Late WS, in contact with both forms, produces a hybrid: the root
  `i` of `widwe` is restored alongside the `-uwe` of `wuduwe`,
  yielding the analogical `widuwe`.

This account is the consensus in the German handbook tradition
(Brunner, Luick, Bülbring) and is consistent with the late-WS dating
of `widuwe` (Brunner: "spätws.").

R&T (2014) do not endorse the analogical account, but they also do
not posit a phonetic rule that would derive `widuwe` directly —
they simply list it. The methodological caution of R&T §6.9.6
toward clean phonetic rules in this region is consistent with
treating `widuwe` as a non-Lautgesetz form.

### 3.3. Why a `*w`-blocker rule is empirically wrong

If we extended `OEMedUnstressedULowering` to exclude `*w` from the
right context, we would over-generate **preservation** in the
following cases the handbooks explicitly list as **lowered**:

* `beaduwe → beadowe` (Campbell §365: "By §§ 373, 385, *u* often
  appears as *o* …, e.g. *beadowe*"). Parasite `-uw-` from PWGmc
  *badwō (R&T p. 16, 42).
* `swaluwan → swalewan` (Campbell §365). Parasite `-uw-` from PGmc
  *swalwōn-.
* `seonuwa → seonowa` (Campbell §218 lists `seonuwa`; §365 is the
  rule). Parasite `-uw-` from *sinwō / *senawō (R&T p. 322).
* `gearuwe → gearowe`. Parasite `-uw-` from *garwa-.
* Aelfric's `widewe` itself (Bülbring §264): the medial `*u` of
  `widuwe` has lowered/raised one further step, with `*w` as right
  context.

A `*w`-blocker rule would block all these — which the handbooks say
do lower. This refutes the rule.

---

## §4. Recommendation for the foma rule

**Do not extend the right-context exclusion to include `*w`.**

The cleanest options, in order of preference:

### Option A: TSV protoform change to `*wúduwōn`

Change the TSV `PROTOFORM` for English/OE `widow` row from
`*wíduwōn` to `*wúduwōn`. This treats the combinative u-umlaut
(`wi → wu`) as already accomplished in the proto-input — which is
defensible because:

1. The change is pre-historic for OE (Bülbring §264, Luick §221
   Anm. 3: "Der Lautwandel ist also sicher vorhistorisch", "uudu Ep.").
2. Other TSV rows already encode pre-historic shifts in their
   protoforms.
3. It puts the medial `*u` immediately under the existing
   stressed-`*u` left-context exclusion in `OEMedUnstressedULowering`
   — yielding `wuduwe`, the most widely attested WS form.

The TSV target `widuwe` would need to be updated to `wuduwe` (which
is in fact Campbell's index cross-reference target and Brunner's
"normal WS" form). The Wiktionary attestation `widuwe` is *one*
attested variant; `wuduwe` is equally attested and is the one the
handbooks consistently treat as Lautgesetz.

### Option B: Add to `oe_known_problems.tsv`

If the TSV target must remain `widuwe`, add a row to
`Germanic/data/oe_known_problems.tsv`:

```tsv
*wíduwōn	exception	analogical_paradigm_levelling	widuwe is analogical from widwe (Anglian, with early syncope) on the model of WS wuduwe; not a Lautgesetz outcome. Brunner §114b, Luick §221 Anm. 1 ("widuwe nach widwe"). Cascade output *widowe is the regular non-syncope, non-back-mutation outcome and matches attested late-WS weodowe modulo root-vowel realisation.	dossier-widuwe-u-preservation.md;DEV_NOTES.md §17.41	2026-XX-XX
```

This category aligns with existing `oe_known_problems.tsv` entries
(`*fūri` → `analogical_dat_e`; `*táppô` → `analogical_n_stem_levelling`).

### Option C: Combination

Switch protoform to `*wúduwōn`, target to `wuduwe`. Keep `widuwe`
(if desired) as a secondary attested-variant pointer, marked
`analogical`.

### What NOT to do

* **Do not** add `*w` to the excluded right-context set of
  `OEMedUnstressedULowering`. No source supports this; Campbell
  §365 directly contradicts it.
* **Do not** add "labials as a class" (`*w`, `*b`, `*f`, `*p`).
  DEV_NOTES already documents (line 81ff, citing Bülbring, Luick,
  Schuhmacher, R&T) that the labial-environment hypothesis cannot
  be formalised without massive over-/under-generation. The
  existing `u_lowering_near_labial` known-problems category exists
  precisely because the rule cannot be cleanly formulated.
* **Do not** rely on the Schuhmacher 2026-03-20 quote ("I do not
  see that the lowering affects unstressed vowels such as the
  middle vowel in the word for 'widow'") to argue against the rule
  itself. Schuhmacher there is talking about *A-Umlaut / stressed-
  `*u`-lowering*, not about Campbell §373; the latter is securely
  attested for unstressed `*u` in the relevant environment (cf.
  `heofon`, `tungol`, past-pl. `-on`, `beadowe`, `swalewan`).

---

## §5. Regression watchlist

Running the cascade after a hypothetical `*w`-exclusion change is
unnecessary because the change is rejected, but for completeness
the audit of TSV rows with the relevant `*-uw-` configuration is:

```
$ awk -F'\t' '$8=="Old_English"' Germanic/data/germanic-aligned-final.tsv | grep -E 'u w|uʋ'
2288  widuwe  *wíduwōn  ...  Old_English  widow
```

**Only one OE TSV row has the inherited `-uw-` configuration
relevant to this dossier**: row 2288 (`widow`). All other `-uw-`
sequences in the OE data are either:

* Absent from the current TSV (no `beaduwe`, `seonuwa`,
  `swaluwan`, `gearuwe` are present as OE entries — the TSV
  entries for `battle`, `sinew`, `swallow`, `ready` either don't
  exist or use different paradigm cells).
* Stressed-syllable diphthongal `-VVw-` sequences (`tréow`,
  `þéow`, `snáiwaz`-type), which are out of the rule's scope
  (rule requires medial *unstressed* `*u`, and the stressed
  vowel + glide cluster is structurally different).

So the regression risk of any rule-level change here is low *in this
TSV*, but the **handbook-level** counter-evidence (Campbell §365's
`beadowe`, `swalewan`) remains conclusive against the rule
extension.

If `*w` were added to the exclusion set, the rows that would
**incorrectly switch from lowering to preservation** in a fuller
lexicon (currently absent from the TSV, but likely to be added):

| proto-input | currently expected OE | with *w*-exclusion |
|---|---|---|
| oblique of *badwō ('battle') | beadowe ~ beaduwe | only beaduwe (Campbell §365 says beadowe is regular) |
| oblique of *swalwōn ('swallow') | swalewan ~ swaluwan | only swaluwan |
| oblique of *sinwō ('sinew') | seonowa ~ seonuwa | only seonuwa |
| Aelfric's widewe | widewe (Bülbring §264) | blocked, widuwe only |

Each of these is a documented attestation of medial `*u` lowering
before `*w`, and would be wrongly suppressed.

---

## §6. Sources actually opened vs. cited from secondary

### Opened and quoted directly (primary)

* `docs/references/campbell_old_english_grammar.txt` —
  §218 (lines 6580–6604), §365 (lines 10014–10033), §373
  (10189–10226), §374 (10228–10232), §378 (10274–10279), index
  (33934, 34211).
* `docs/references/brunner_1965_altenglische_grammatik.txt` —
  §114b (lines 4671–4675), §44 Anm. 7 (referenced via companion
  dossier), entries `weodowe`, `widwe`, `wuduwe` in word index
  (28128, 28243, 28535, 28592).
* `docs/references/hogg_vol1.txt` — §3.3.1.3 (lines 4413–4423),
  §6.481 region for `sinu`/`sinwa` (lines 6470–6520), labial-class
  searches (passim).
* `docs/references/ringe_taylor_linguistic_history_vol2.txt` —
  p. 270 (lines 15555–15600), p. 322 (lines 18430–18475),
  §6.9.6 (lines 19020–19100).
* `docs/references/bulbring_altenglisches_elementarbuch.txt` —
  §264 (lines 5407–5419), index entry `wuduwe 264`.
* `docs/references/luick_historische_grammatik.txt` —
  §221 (lines 12750–12810), §221 Anm. 1 (12779), §224 Anm. 2
  (12886, 12976).
* `Germanic/docs/dossier-medial-u-lowering-conditioning-2026.md`
  (companion dossier, 745 lines, fully read).
* `Germanic/docs/DEV_NOTES.md` (relevant section §17.41 / labial
  exceptions; lines 81, 83, 137, 139, 149, 151, 176, 195, 213,
  215, 225, 235, 261–392).
* `Germanic/data/germanic-aligned-final.tsv` (TSV audit for `-uw-`).
* `Germanic/data/oe_known_problems.tsv` (existing exception
  categories).
* `Germanic/fsts/germanic.txt` (lines 2290–2300, current rule
  formulation).

### Cited only via secondary / not directly opened in this round

* **Sievers 1898 (3rd ed.)** *Angelsächsische Grammatik* — cited
  through Brunner (the Brunner volume is "Altenglische Grammatik
  nach der angelsächsischen Grammatik von Eduard Sievers"). The
  relevant material is at Brunner §44, §114b, fully canvassed
  above; the original Sievers numbering is not separately consulted.
* **Campbell 1962** *Old English Grammar Index* (cited by R&T as
  "Campbell 1962: 153–7" for unstressed-vowel mergers). Not
  separately opened; the substantive content is in the 1959 main
  volume §§373–379 already canvassed.
* **Schuhmacher email (2026-03-20)** — quoted via DEV_NOTES; the
  primary email file (`docs/references/knob_email_2026-01-22.txt`)
  is on a different topic (Kroonen on `knob`). The Schuhmacher
  consultation appears not to have a corresponding `.txt` file in
  `docs/references/`; only DEV_NOTES carries the verbatim quote.
  The quote is informative but not load-bearing for this dossier:
  Schuhmacher is discussing A-Umlaut / stressed-`*u`-lowering, not
  Campbell §373 medial-unstressed lowering.
* **Kilday 2024** ("Crist's Law"; on file as
  `kilday_2024_crists_law_smiths_law_wizen.txt`) — not consulted;
  not relevant to medial unstressed `*u`-lowering.
* **Fulk** *Comparative Grammar* — companion dossier covers
  §§1.8, 5.2; not re-opened for `widuwe` because Fulk does not
  treat OE-internal analogy of this lexeme.

### Not consulted in this round (and not needed)

* Bosworth-Toller, Clark Hall, Bright, Sweet — lexicographical
  resources confirming the variant attestations `widuwe ~ wuduwe ~
  weoduwe ~ weodowe ~ widwe ~ widewe ~ wyduwe ~ widua` but adding
  no analytical content. The Campbell index entries already
  testify to the variation.
* Pokorny IEW, Mayrhofer EWAia, Beekes EDG — IE-level etymology of
  *widhewā- is not at issue.
* Kroonen EDPG, Orel — PGmc reconstruction
  *widuwō(n)- not in dispute.
* Stiles 2012, Howell & Salmons 1988, Cercignani — concern A-Umlaut
  / stressed lowering, not the medial-unstressed rule.
* Bammesberger, Erdmann, Adamczyk — concern morphological topics
  not at issue here.

### Web research

Not undertaken for this dossier. All claims are anchored to local
files. Archive.org material is not needed: the six handbooks named
in the prompt are all locally available and were directly consulted.

---

## §7. Honest residual uncertainty

1. **R&T's framing of `widuwe`.** R&T (270, 322) list `widuwe` as
   a regular non-syncope outcome, in apparent tension with Brunner
   §114b ("widuwe is analogical"). The disagreement is mild:
   R&T do not assert a Lautgesetz that *would* have lowered the
   medial `*u`, so they are not endorsing the `*w`-blocker
   hypothesis either; they are simply silent on the conditioning of
   medial-`*u`-lowering for the purposes of this lexeme. This
   silence does not undercut the present dossier's conclusion.

2. **Whether `wuduwe` or `widuwe` is "the" OE form.** The TSV row
   currently uses `widuwe` (per Wiktionary), but Campbell §218 lists
   `wudu, wuduwe` as the primary WS forms; Brunner identifies
   `wuduwe` as the WS norm and `widuwe` as a late-WS levelling.
   `wuduwe` is genuinely attested (Bosworth-Toller; cf. Campbell
   index line 34211 redirecting). Adopting `wuduwe` as the
   target would be more philologically defensible.

3. **The DEV_NOTES line 388–393 paraphrase of R&T §6.7.3.** That
   passage cites R&T's "*widuwe > OE widuwe" reading. Confirmed by
   direct reading at `ringe_taylor_linguistic_history_vol2.txt:15570–15571`.

4. **Cascade ordering.** This dossier does not re-audit the
   ordering of `OEMedUnstressedULowering` relative to combinative
   u-umlaut / "verstärkter Velarumlaut". Option A (changing the
   protoform to `*wúduwōn`) sidesteps the ordering question
   entirely. Option B (known-problems entry) accepts the current
   ordering.

5. **No evidence checked for `gearuwe`, `seonuwa`, `swaluwan`
   absent from the TSV.** Their citation here rests on Campbell §365
   alone. If the TSV is later expanded to include them, their
   handling will need to be re-audited (with the cascade rule
   *as currently stated*, they should lower regularly to `gearowe`,
   `seonowa`, `swalewan` — which is what Campbell says does happen).

---

## §8. Bottom line

The mismatch `*wíduwōn → *widowe` (cascade) vs. attested `widuwe`
(TSV target) is **not** a sound-law problem. The cascade rule
`OEMedUnstressedULowering` as currently formulated is correctly
stated; `*w` does not block medial unstressed `*u`-lowering, and
no handbook says it does. The OE form `widuwe` is, on the explicit
testimony of Brunner §114b and Luick §221 Anm. 1, an analogical
form derived from levelling between Anglian `widwe` (with early
syncope) and WS `wuduwe` (the genuinely Lautgesetz outcome). The
fix belongs at the TSV layer: either switch the protoform to
`*wúduwōn` (so the existing stressed-`*u` left-context exclusion
preserves the medial `u`, yielding the regularly attested WS
`wuduwe`), or mark `*wíduwōn` → `widuwe` as
`analogical_paradigm_levelling` in `oe_known_problems.tsv`.
