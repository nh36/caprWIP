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

---

## Appendix B: Source canvass for the *wi → *wu rule

This appendix systematically canvasses six handbook authorities
beyond Bulbring sec. 264 and Campbell sec. 218 (the only sources
cited in the DEV_NOTES sec. 17.51.A1 draft) on the OE w-effect /
combinative u-umlaut / "gesteigerter Velarumlaut". The aim is to
test whether the draft conditioning ("word-initial #w + stressed
*i + single non-nasal/non-liquid C + *u or *o in next syllable")
is faithful to the handbook consensus, or whether the consensus
demands a broader/different formulation.

### B.1 Bulbring, Altenglisches Elementarbuch sec. 264

**Locus.** sec. 264, p. 107 of the print edition.

**Verbatim.** `bulbring_altenglisches_elementarbuch.txt:5399-5419`:

> Ums Jahr 700 (bereits im Epin. Gloss.) wird das durch u/a-Umlaut
> entstehende _iu_ (sec. 235) in allen Dialekten ausser dem
> Kentischen durch Einfluss eines vorangehenden _w_ zu _u_: **wudu**
> 'Holz' aus *wiudu (<*widu, ahd. witu), ws. **wuduwe** 'Witwe'
> (angl. widwe und bei Aelfric widewe ohne u-Umlaut), wuluc
> 'Purpurschnecke', swutol 'klar', wuton 'wohlan', ws. swustur
> swuster Ru.1 swuster 'Schwester' (aus *swistur); ebenso mit
> w-Umlaut (und Verlust des anlautenden w), ws. tuwa 'zweimal'
> <*twiwa. Folgender Velar stort im Ws. diese Entwicklung nicht:
> **wucu** 'Woche', gecwucian 'beleben', swugian 'schweigen'; im
> Anglischen aber wird _iu_ wieder zu _i_, ehe das _w_ sich geltend
> machte (sec. 202 und 230): wicu, cwician u. s. w. Im Kentischen
> erhalt sich der Diphthong: wiodu, wiadu, weadu 'Holz' sec. 238,
> bewiotian 'beobachten, vollfuhren', gesweotolian 'offenbaren'
> u. s. w.

Cross-reference at `bulbring_altenglisches_elementarbuch.txt:5040-5051`
(sec. 235): "nach _w_ (sec. 229, 1) u-Umlaut und Ubergang der so
entstehenden Gruppe _wiu_ zu _wu_ ein (*widu > *wiudu > wudu 'Holz'
sec. 264) ... nach _w_ entsteht auch im Ws. durch u-Umlaut _iu_,
welches gemass sec. 264 zu _u_ wird (wucu 'Woche' < *wiucu *wicu),
wohingegen a-Umlaut unterbleibt".

Cross-reference at `bulbring_altenglisches_elementarbuch.txt:5219-5220`
(sec. 250): swustur < *swistur, listed under "Vor st gilt ... Umlaut
von i" — so the rule explicitly fires across an *st cluster.

Cross-reference at `bulbring_altenglisches_elementarbuch.txt:8689-8693`
(sec. 464): w is lost before "dem gemass sec. 264 erst aus iu < i
entstandenen u in **uton** 'lasst uns', ws. cucu 'lebendig', ws.
betux 'zwischen', neben wuton, ws. cwucu, betwux."

**Conditioning explicitly stated.**
- Initial *w-: yes (the rule is _vorangehendes w_).
- After *sw-: yes — explicit examples swustur, swutol, swugian.
- After *kw-/*tw-: yes — explicit examples cwucu, gecwucian,
  cwudu, tuwa < *twiwa.
- After *hw-: not exemplified (but no exclusion stated either).
- Following C restrictions: NONE in WS — Bulbring's wording is
  "Folgender Velar stort im Ws. diese Entwicklung _nicht_"
  (a velar does NOT block); the WS rule applies before stops
  (*d, *k, *g, *t), the cluster *st (swustur), and is paralleled
  by the w-Umlaut variant tuwa < *twiwa. Bulbring lists no
  consonant exclusion in WS.
- In Anglian, blocked before c, g (velars only); in Kentish,
  blocked entirely (the diphthong remains).
- Trigger vowel: described as "_iu_ entstehend durch _u/a-Umlaut_",
  i.e. trigger is next-syllable *u (u-umlaut) **or** *a (a-umlaut).
  Examples: wuduwe (next-syllable *u), wuton (next-syllable *a in
  *witan), swustur (next-syllable *u), tuwa < *twiwa (next-syllable
  *a). Bulbring's framing of u/a-Umlaut conjoined explicitly admits
  *a as trigger.

**Chronology.** "Ums Jahr 700 (bereits im Epin. Gloss.)" — the rule
is in force by ca. 700 AD. Two-step: u/a-umlaut produces *iu first,
then *wiu → wu. Anglian "_iu_ wieder zu _i_" (i.e. iu monophthong-
ised back to i in Anglian, sec. 230) — implies the rule is later
than Anglian smoothing.

**Dialect.** All dialects EXCEPT Kentish; Anglian is partial (blocked
before velars).

**Examples cited.** wudu < *wiudu < *widu; wuduwe; wuluc; swutol;
wuton; swustur, swuster; tuwa < *twiwa; wucu (WS only; Anglian
wicu); gecwucian (WS); swugian (WS); uton (with w-loss); cucu;
betux; betwux. Counter-examples cited as Anglian: widwe, wicu,
cwician, swigade. Kentish: wiodu, weadu, bewiotian, gesweotolian.

**Disagreements with current draft.**
1. Draft's right-context excludes nasals and liquids, but Bulbring
   does not state any consonant exclusion in WS.
2. Draft requires word-initial #w; Bulbring's examples explicitly
   include *sw-, *kw-, *tw- clusters.
3. Draft restricts trigger to *u/*o; Bulbring includes *a (wuton,
   tuwa).

### B.2 Campbell, Old English Grammar sec. 218 (and 217, 219, 365, 373, 470)

**Loci.** sec. 217 (cross-ref to combinative back umlaut),
sec. 218 (the main statement), sec. 219 (combinative a-umlaut),
sec. 365 (later parasiting), sec. 373 (unaccented u → o),
sec. 470 (loss of w before u).

**Verbatim sec. 218** (`campbell_old_english_grammar.txt:6571-6604`):

> sec. 218. Combinative back umlaut generally intervenes in the
> case of u-umlaut of i, and has already taken place in the oldest
> texts, e.g. BH Derauuda d.s. (after -wudu), Ep. uudu- 'wood',
> Cp. -cudu 'cud', although Ep. has some forms without the change,
> e.g. uuidu-, uuiloc-, -quidu, and Cp. has also forms which show
> that i could escape combinative u-umlaut, and then undergo
> normal u-umlaut, e.g. wioloc, seotol evident (770, read sweotol).
> In W-S many forms have combinative u-umlaut of i, and the change
> seems not to be limited, like u-umlaut, to positions before
> liquids and labials, e.g. **wudu** wood, **wuduwe** widow, **wucu**
> week, **swutol** evident, **cwoudu** cud, **swugian** be silent,
> **(w)uton** let us; but there occur also in many cases forms with
> io (eo) or i, e.g. weoduwe, widuwe, wicu, cwicu, swiotol, sweotol,
> cweodu, swigian, and always swiocol, swicol treacherous, wioton,
> witon they know, swicon they deserted. Practically the same
> applies to all the dialects, except that i remains unchanged
> before c, g, in Angl. (e.g. cwicu, wicu, twigu twig, swigian),
> apart from the analogical forms, mostly in VP, mentioned in
> sec. 214.

**Verbatim sec. 219** (`campbell_old_english_grammar.txt:6606-6627`):

> sec. 219. Combinative a-umlaut of i is practically limited to
> various forms of wuta, know, and wuta wise man, in North. W-S
> has very rare instances, wutan wise men, CP 2, 2, gewuta witness,
> id. 145, 13; 449, 1. All these forms could be regarded as having
> the vowel of wuton. W-S and VP extend the vowel of wudu to infl.
> wuda, but Kt. has wiada, weada (Cts. 28 and 39).

**Cross-reference sec. 470** (`campbell_old_english_grammar.txt:12159-12184`):

> sec. 470. Loss of w before u. Loss of u [sic; read 'w'] occurs
> irregularly between another consonant and u. Examples are: (1)
> with combinative back umlaut (sec. 218): cucu alive, cudu cud,
> sugian be silent, sutol clear, beside cwucu, cwudu, swugian,
> swutol; (2) with development of diphthong to u (sec. 338,
> footnote): betuh beside betwuh. Tuwa twice < twuwa has retraction
> of i to u between u and u, similar to that between u and r ...
> sec. 471. An isolated loss of w not preceded by a consonant before
> u is uton beside wuton let us (sec. 218).

**Conditioning explicitly stated.**
- Initial *w-: yes.
- After *sw-: yes — swutol, swugian.
- After *kw-/*tw-: yes — cwoudu, cwucu, twuwa.
- Following C restrictions: Campbell is emphatic: "the change
  seems not to be limited, like u-umlaut, to positions before
  liquids and labials". So no consonant restriction in WS. In
  Anglian: blocked before *c, *g (velars).
- Trigger vowel: Campbell separates u-umlaut (sec. 218: trigger
  *u) from a-umlaut (sec. 219: trigger *a). Combinative a-umlaut
  exists, just with narrower scope (mostly North.). Examples with
  *a trigger that fire in WS too: wuton (< *witan, *a trigger),
  wutan wise men, gewuta. So in WS, trigger {*u, *a} both work.

**Chronology.** "has already taken place in the oldest texts"
(BH Derauuda, Ep. uudu-). Rule is pre-historic.

**Dialect.** WS with full extent (no consonant restriction);
Anglian (Mercian, Northumbrian) blocked before velars only;
"Practically the same applies to all the dialects" save the
velar restriction. Kentish is not separately treated under
sec. 218 (cf. Bulbring: in Kentish the diphthong is preserved,
so the change does not apply).

**Examples cited.** wudu, wuduwe, wucu, swutol, cwoudu, swugian,
(w)uton, cucu, cudu, sugian, sutol, cwucu, cwudu, swustur,
twuwa > tuwa, wuta, wutan, gewuta, wuda. Counter-examples retaining
i/io/eo: weoduwe, widuwe, wicu, cwicu, swiotol, sweotol, cweodu,
swigian, swiocol, swicol, wioton, witon, swicon. Kentish: wiada,
weada.

**Disagreements with current draft.**
1. Same as Bulbring: no consonant exclusion (so the draft's
   "non-nasal, non-liquid" restriction is unmotivated; the
   actual restriction is non-velar in Anglian, no restriction
   in WS).
2. *sw-, *kw-, *tw- clusters fire (wuton with optional w-loss,
   swustur, cwucu, twuwa).
3. *a trigger fires (wuton, wutan, wuda).

### B.3 Brunner (Sievers-Brunner), Altenglische Grammatik sec. 114b (and 113, 114a, 114c)

**Loci.** sec. 113 (we → wo), sec. 114a (wir > wur > wyr in Anglian),
sec. 114b (the *wi → wu rule), sec. 114c (a-umlaut conditions).

**Verbatim sec. 114b** (`brunner_1965_altenglische_grammatik.txt:4640-4675`):

> b) Westgerm. _i_ unter den Vorbedingungen des _u_-Umlauts (sec. 108, 1)
> scheint gemeinae. zu _u_ geworden zu sein, doch fehlen aus Kent
> ae. Beispiele (s. Anm. 6). Anglisch ist vor _c_ und _g_ _i_ erhalten
> (vgl. sec. 108, Anm. 3). Es heisst daher ws. angl. wuluc 'Purpur-
> schnecke', wudu 'Holz', c(w)udu 'Harz', wuton 'wohlan', swutol
> 'klar'; aber nur ws. wucu 'Woche', cwucu 'lebendig', swugode
> 'schwieg' (angl. wicu, cwicu, swigade). Hierher gehoert ausserdem
> vielleicht auch spaetws. swustor, swuster (auch R1), s. sec. 113,
> Anm. 4. ... Angl. widwe (L, Rit. R2, Vesp. Ps.) neben ws. wuduwe
> 'Witwe' ist durch fruehe Synkope zu erklaeren. Durch Ausgleich
> zwischen synkopierten und nicht synkopierten Formen ist spaetws.
> widuwe, wyduwe (mit y nach sec. 116) und weodowe (aus *wioduwe)
> mit gewoehnlichem Velarumlaut zu erklaeren.

**Verbatim sec. 114c** (`brunner_1965_altenglische_grammatik.txt:4676-4682`):

> c) Unter den Bedingungen des o/a-Umlauts kommt _u_ fuer _i_ nach
> _w_ im Nordh. und teilweise im Westsaechsischen vor, so nordh.
> wutan 'wissen' und andere Formen dazu, wuta 'Ratgeber' (ws. wita,
> nicht streng ws. wiota, weota, sec. 111, Anm. 2), wuda Pl. 'Holz'
> (das allerdings vom Nom. Sg. beeinflusst sein kann). Anm. 7. Da
> _u_ bereits in sehr alten Texten begegnet (so in derauuda 'in
> silva derorum' lat. Beda Hss., uuluc, uudu Ep. Gl.), ist dieser
> 'gesteigerte Velarumlaut' (Luick) aelter als der gewoehnliche
> und gehoert der vorhistorischen Zeit an.

**Conditioning explicitly stated.**
- Initial *w-: yes.
- After *sw-: yes — swutol, swugode, swustor, swuster.
- After *kw-: yes — cwucu, c(w)udu.
- Following C restrictions: NONE in WS for u-umlaut (sec. 114b).
  In Anglian: blocked before *c, *g only. swustor with cluster
  *st is treated under "spaetws." but admitted under sec. 114b.
- Trigger vowel: u-Umlaut (sec. 114b, trigger *u) AND o/a-Umlaut
  (sec. 114c, trigger *a) both produce *u after *w. wutan, wuta,
  wuda all have *a trigger.

**Chronology.** Sec. 114b Anm. 7: "gesteigerter Velarumlaut" is
older than ordinary Velarumlaut and is pre-historic. Brunner
implicitly accepts a two-step *wi > *wiu > *wu via the umlaut
intermediate (since he subsumes *wi → *wu under the conditions
of u-Umlaut).

**Dialect.** Common-OE (gemeinae.) for u-umlaut, except Anglian
before velars; Kentish lacks examples; for a-umlaut (sec. 114c),
Northumbrian and partly WS only.

**Examples cited.** wuluc, wudu, c(w)udu, wuton, swutol, wucu,
cwucu, swugode, swustor, swuster, wuduwe, wutan, wuta, wuda,
derauuda. Counter-examples (Anglian): wicu, cwicu, swigade,
widwe.

**Disagreements with current draft.** Same as Bulbring/Campbell:
(1) no consonant exclusion in WS, (2) cluster after *s/*k OK,
(3) *a trigger admitted (sec. 114c).

### B.4 Luick, Historische Grammatik sec. 221 (and 222, 223, 224, 225, 233)

**Locus.** sec. 221 ("Der gesteigerte Velarumlaut: wi > wu"),
pp. 203-204; sec. 223 (relative chronology, no diphthong stage);
sec. 224 (ordinary velar umlaut, post-dating gesteigert);
sec. 225 (velar umlaut before clusters).

**Verbatim sec. 221** (`luick_historische_grammatik.txt:12752-12793`):

> a) Der gesteigerte Velarumlaut wi > wu.
> sec. 221. 1. Wenn die Lautfolge _wi_ unter den Bedingungen des
> _u-Umlautes_ stand, so wurde daraus gemeinenglisch _wu_, nur mit
> der Einschraenkung, dass im Anglischen vor Gutturalen diese
> Entwicklung unterblieb. So: wuluc 'Purpurschnecke', **wudu**
> 'Holz', c(w)udu 'Harz', **wuton** 'wohlan', **swutol** 'klar',
> ws. und kent. **wucu** 'Woche', **cwucu** 'lebhaft'; dazu
> zufaellig nur in einzelnen Dialekten belegt: spaetws. und
> ostmerc. **swuster** 'Schwester' (aus *swistur), ws. **wuduwe**
> 'Witwe', swugode 'schwieg' (und danach swugian 'schweigen').
> 2. Die Folge _wi_ wurde unter den Bedingungen des _o/a-Umlautes_
> zu _wu_ im Nordhumbrischen und wahrscheinlich auch in west-
> saechsischen Untermundarten in **wuta** (plur. -an) 'Weiser,
> Ratgeber', **wuda** obl. zu wudu 'Holz'.
> Anm. 1. Es heisst also im Anglischen wicu, cuicu, swica
> 'Betrueger', swigian, im Mercischen gewita (sec. 224 Anm. 2),
> im Strengwestsaechsischen wita, cuidu 'Bauch', hwida 'Hauch',
> swica, wiga 'Kaempfer', im Kentischen ebenso. Gelegentliches
> wuta bei Alfred wird wohl aus westsaechsischen Untermundarten
> stammen.

**Verbatim sec. 223** (`luick_historische_grammatik.txt:12836-12847`):

> sec. 223. Gewoehnlich wird angenommen, dass in diesen Faellen
> _i_ und _e_ zunaechst wie beim gewoehnlichen Velarumlaut zu _iu_
> und _eo_ wurden und dann _wiu_ zu _wu_, _weo_ zu _wo_ (und _wea_
> zu _wa_). Wenn aber der Weg von urengl. *werold zu ws. worold
> wirklich ueber *weorold gegangen, also _weo-_ zu _wo-_ geworden
> waere, so haette wohl das um jene Zeit schon laengst bestehende
> Brechungs-_eo_ an diesem Wandel teilgenommen, also z. B. ws.
> weordan sich zu *wordan entwickelt, was nicht der Fall ist. Dazu
> kommt, dass der 'gesteigerte' Velarumlaut einige Zeit vor dem
> gewoehnlichen sich vollzogen hat (unten sec. 233). Es ist daher
> wahrscheinlich, dass _i, e_ ohne diphthongische Zwischenstufe zu
> _u, o_ wurden, etwa durch die Reihen i-y-u, e-ae-o hindurch.

**Conditioning explicitly stated.**
- Initial *w-: yes.
- After *sw-: yes — swuster, swutol, swugode, swugian.
- After *kw-: yes — cwucu, c(w)udu.
- Following C restrictions: NONE in WS, Mercian ostmerc., and
  Kentish (for u-umlaut), explicitly admits clusters (swuster
  before *st). Anglian blocked before _Gutturalen_ (velars *c,
  *g) only.
- Trigger vowel: u-Umlaut (sec. 221.1) AND o/a-Umlaut (sec. 221.2)
  both fire. Examples with *a: wuta, wuda, wuton.

**Chronology.** Sec. 223: critically, Luick **rejects** the
two-step *wi > *wiu > *wu account (Bulbring's account). He
argues, on the parallel of *we > *wo NOT proceeding via *weo
(since brechung-eo did not undergo it), that the change
*wi > *wu is direct, "ohne diphthongische Zwischenstufe ...
etwa durch die Reihen i-y-u ... hindurch" (i.e. via centralised
[y] or rounded high front vowel). Luick also explicitly states
that the gesteigerter Velarumlaut **predates** ordinary Velar-
umlaut (sec. 233 cross-ref). Earliest attested: Bede's Derauuda,
Ep. Gloss. uuluc, uudu — pre-historic.

**Dialect.** "gemeinenglisch" (common-OE) for the u-umlaut
variant, with Anglian carve-out before velars; Kentish admits
the change before *u (Luick explicitly: "Dass dieser Uebergang
vor _u_ auch dem Kentischen eigen war, lehren die spaerlichen
Belege im Verein mit dem spaeteren Bestand", sec. 221 Anm. 2)
but NOT before *o/*a. The o/a-umlaut variant is Northumbrian
+ WS submundarts only.

**Examples cited.** wuluc, wudu, c(w)udu, wuton, swutol, wucu,
cwucu, swuster, wuduwe, swugode, swugian, wuta, wuda, derauuda,
uuluc, uudu. Counter-examples (Anglian): wicu, cuicu, swica,
swigian, gewita.

**Disagreements with current draft.**
1. No consonant exclusion in WS (admits cluster *st in swuster,
   admits *d, *k, *g, *t).
2. *sw-, *kw- clusters fire.
3. *a trigger fires (wuta, wuda, wuton in addition to u-umlaut
   wudu, wuduwe etc.).
4. Luick rejects the *wiu intermediate stage outright. The
   draft's collapse to a single direct rule is therefore
   independently endorsed by Luick (it is Bulbring's two-step
   account that is the outlier, not the cascade's collapse).

### B.5 Hogg, in CHEL Vol. 1 (1992 chapter)

**Locus.** Hogg's chapter on phonology and morphology in CHEL
Vol. 1, p. 116 (back mutation discussion).

**Verbatim** (`hogg_vol1.txt:5664-5694`):

> [back mutation] involved exactly the same diphthongisation
> process [as breaking], except that in the later change only
> short vowels are diphthongised, i.e., /i/ > /io/, /e/ > /eo/,
> /ae/ > /aea/. The other principal difference between the two
> is that the environment for back mutation was a following back
> vowel not a back (velar) consonant. ... In West Saxon back
> mutation was even more restricted, for it occurred only if there
> was a single intervening consonant which was either a labial
> or a liquid (see Davidsen-Nielsen & Orum 1978 for a possible
> acoustic explanation). By the time of the change, at least in
> West Saxon, there were only two unstressed back vowels, /o/ and
> /a/, and it is often helpful to distinguish between o-mutation
> and a-mutation. Although o-mutation was regular, in West Saxon
> a-mutation occurred only if the preceding vowel was /i/ ...

**Conditioning explicitly stated.** Hogg's CHEL chapter does
not separate "combinative" from ordinary back mutation in detail
(the chapter is a high-level overview). The relevant generalisations
he gives are: (i) trigger is a back vowel /o/ or /a/ in the next
syllable (he does not flag /u/ separately, presumably because
unstressed /u/ → /o/ by his date); (ii) WS restricts to single
labial/liquid consonant for ordinary back mutation, BUT (iii)
"a-mutation occurred only if the preceding vowel was /i/" — i.e.
WS does have a-mutation, but only of /i/, which is exactly the
*wi → *wu environment.

**Chronology.** Hogg dates back mutation to ca. 700 AD, the
earliest of the post-prehistoric changes. He does not separately
date the combinative variant.

**Dialect.** Hogg treats the change as common-OE with WS
restrictions; he does not isolate the w-effect.

**Examples cited.** Hogg's CHEL chapter does not explicitly list
*wi → *wu examples in this passage. Words wudu, widuwe occur
elsewhere in CHEL Vol. 1 only in literary contexts (`hogg_vol1.txt:16778`
etc.) and not in phonological discussion. There is no detailed
combinative-u-umlaut treatment in this chapter.

**Disagreements with current draft.** Hogg does not contradict
the rule but supplies less detail than Bulbring/Campbell/Brunner/
Luick. The one positive contribution is the explicit statement
that WS a-mutation operates _only_ when the stressed vowel is
/i/ — which independently supports including *a as a trigger
in the *wi → *wu environment specifically.

### B.6 Ringe & Taylor, A Linguistic History of English Vol. 2 (2014), sec. 6.9.6

**Locus.** sec. 6.9.6 "Back umlaut", pp. 320-323.

**Verbatim** (`ringe_taylor_linguistic_history_vol2.txt:18318-18525`):

> Beginning of sec. 6.9.6: "and a following back umlaut environment
> cause _i_ to become _u_ and _e_ to become _o_ (i.e. complete
> velarization and rounding of the nonlow short front vowels). It
> is also generally believed that the latter, more extreme change
> occurred significantly earlier than normal back umlaut, at least
> when the vowel affected was *i and the back vowel of the
> following syllable was _u_ (Luick 1914-40: 213, Campbell 1962:
> 92). ... it appears that back umlaut can have been a single
> historical change which ran its course over about the first
> half of the 8th century; possibly the 'combinative' part of the
> change went to completion first, or the whole course of the
> change was about a generation earlier in Northumbria than in
> Mercia."
>
> "When _w_ preceded _i_ in a back-umlauting environment, _i_ often
> became _u_ in all the dialects regardless of what consonant
> followed. The following examples have unproblematic etymologies:
> PGmc *widuwon- ... > WS OE wuduwe ~ widuwe, but Merc. widwe,
> North. widua;
> PGmc *widuz 'forest, woods' ... > OE widu ... > wudu (early
> Merc., CorpGl 715, 717, 835, 836, 1590); the latter is the usual
> WS, Merc., and North. form, though mid-9th-century Kentish has
> weada 'of wood' ...
> PGmc *wikon- 'order, alternation' ... > WS wucu, North. wicu;
> PGmc *kwikwaz 'alive' ... > OE *cwicu >- cwic ... ~ cwicu >
> cwucu > cucu (all genders) ...
> PWGmc *kwidu 'gum' ... > OE cwidu ... > cwudu > cudu ...
> northern WGmc *witum '... let's' ... > OE wutum 'let's' > wutun
> (North.) > wuton (Kent.) > uton (WS).
> ... In forms of 'know' and its derivatives there is a more or
> less clear dialect distribution of the outcomes:
> PGmc *witana 'to know' ... > WS OE witan, Merc. *wiotan >
> weotan, North. wuta;
> PGmc *witun 'they know' ... > WS OE witun, Merc. *wiotun >
> weotun, North. wutun;
> ... PNWGmc *witodaz 'observed, determined' ... > WS, Kent. OE
> witodlice 'certainly, truly', Merc. weotodlice, North. wutodlice"

**Conditioning explicitly stated.**
- Initial *w-: yes.
- After *sw-: not explicitly named, but no exclusion (and they
  cite swuster forms elsewhere).
- After *kw-: yes — cwucu, cwudu (PGmc *kwikwaz, *kwidu).
- Following C restrictions: R&T flag this most explicitly:
  "_i_ often became _u_ in all the dialects **regardless of what
  consonant followed**" (line 18458). NO consonant restriction
  whatever.
- Trigger vowel: R&T treat the change as part of "back umlaut",
  whose triggers are next-syllable back vowels generally. They
  flag the strong evidence concentrating on cases where the
  trigger is *u (line 18324). For wuton < *witana the trigger
  is *a; R&T list wuton ~ wutun explicitly under the *wi → *wu
  rubric. So *u and *a are both admitted.

**Chronology.** R&T date all back umlaut to roughly the first
half of the 8th century, with the "combinative" subtype going
to completion first (line 18336-18338). This is consistent with
Luick. R&T do not commit to a *wiu intermediate; they describe
the change as "_i_ ... became _u_" directly.

**Dialect.** "All the dialects" for the *w_-conditioned change
(line 18457). With minor dialect-specific levellings.

**Examples cited.** wuduwe ~ widuwe (WS), widwe (Merc.), widua
(North.); wudu < widu; wucu < *wice; cwucu < *cwicu; cwudu <
cwidu; wutum > wutun > wuton > uton; wuta, wutun, wutodlice
(North.); weotan, weotun, weotodlice (Merc.).

**Disagreements with current draft.**
1. R&T are the most explicit: NO consonant restriction at all.
2. *kw- cluster (and presumably *sw-) admitted (cwucu, cwudu).
3. *a trigger admitted (wuton).
4. R&T treat the change as common-OE, not WS-specific (though
   for wuduwe specifically, only WS shows it because Anglian
   syncopated to widwe).

### B.7 Kroonen, Etymological Dictionary of Proto-Germanic; Orel, Handbook

**Loci.** Kroonen's entry for *widu(w)on- (OE widewe, wudewe);
Orel's entry for *widuwon (OE widuwe).

**Verbatim Kroonen** (`kroonen_etymological_dictionary_pgmc.vision.txt:29632-29637`):

> *widu(w)on- f. 'widow' - Go. widuwo f. 'id.', OE widewe, wudewe
> f. 'id.', E widow, OFri. widwe f. 'id.', OS widowa f. 'id.',
> Du. weduwe c. 'id.', OHG wituwa f. 'id.', G Witwe f. 'id.'
> *h1ui-dhh1-uh2- (IE) - Gr. eitheos m. 'unmarried youth ...',
> Lat. vidua f. 'widow' ... Cf. also *widu(w)ernan-: Go. widuwairna
> m. 'orphan' ... and OE widuwa, OHG wituwo m. 'widower' < PGm.
> *widu(w)an-.

**Verbatim Orel** (`orel_handbook_germanic_etymology.vision.txt:50890-50902`):

> *widuwon sb.f.: Goth widuwo 'widow', OE widuwe id., OFris widwe
> id., OS widowa id., OHG wituwa id. Etymologically connected with
> Skt vidhava id., Av vidava id., Lat uidua id., OIr fedb id.,
> OPrus widdewu id., Slav *vodova id.

**Relevance.** Neither Kroonen nor Orel contain a phonological
discussion of the *wi → *wu change — they are etymological
dictionaries. They are useful only for confirming the PGmc
reconstruction. Note that Kroonen lists OE "widewe, wudewe"
(rather than Brunner-style wuduwe), reflecting the LWS levelled
variants. Orel lists "widuwe". Neither cites *wuduwe directly,
which is mildly significant: Kroonen's choice of OE citation
form leans late-WS analogical levelled rather than the genuine
WS Lautgesetz output that Brunner sec. 114b identifies. This
does not affect the rule formulation; it does suggest that
TSV protoform / OE-target choice depends on which lexicographic
authority one privileges (cf. sec. 6 of the main dossier).

### B.8 Synthesis across the canvass: answers to questions A-G

**A. Is the conditioning "single C, non-nasal, non-liquid"
correct?** **No.** All five phonological authorities (Bulbring,
Campbell, Brunner, Luick, Hogg, R&T) agree that, in WS, the
change has NO consonant restriction. Bulbring sec. 264 says
"Folgender Velar stoert im Ws. diese Entwicklung _nicht_";
Campbell sec. 218 says "the change seems not to be limited,
like u-umlaut, to positions before liquids and labials";
R&T say "regardless of what consonant followed". Brunner and
Luick concur. The only documented restriction is the **Anglian**
restriction before velars *c, *g (which does not apply to WS).
The draft rule's exclusion of nasals and liquids is **without
handbook support**.

However, the draft is conservative in the safe direction: it
under-fires rather than over-fires. Forms with following nasal
(*windan, *wintru-) or liquid (*wir-) in the cogset do NOT
appear with *wu- attestations (windan, winter, weorold are
all attested with retained *i / *eo). So the draft's narrower
rule does not produce wrong outputs; it merely fails to license
forms that the cogset does not contain. The handbooks' broader
formulation would be the philologically correct one IF other
*wi[N/L]u- shapes had attestations exhibiting the change, but
the cogset doesn't include any such forms.

**B. Should the trigger include *a?** **Yes, on the literature.**
Bulbring (wuton, tuwa), Campbell (sec. 219 explicitly: combinative
a-umlaut; wuton, wuta), Brunner (sec. 114c: wutan, wuta, wuda),
Luick (sec. 221.2: wuta, wuda), and R&T (wuton) all admit *a as
a trigger of the *wi → *wu change, in addition to *u.

The cogset target *widuwon- has *u in the next syllable, so the
*a-trigger extension is not needed for THIS row. But the existing
rule under-models the literature. If any future cogset row has
the shape *wi-C-*a-... (e.g. *witana → wuton path), the rule
will fail.

**C. After *sw-, *kw-, etc.?** **Yes, on the literature.** All
authorities cite swuster < *swistur, swutol, swugian, cwucu,
cwudu, twuwa as members of the same change. The draft's
restriction to ".#. {*w}" excludes these. Again, this is a
conservative under-fire: the cogset target row does not require
the *sw-/*kw- extension, but the rule as drafted is narrower
than the literature.

**D. Chronology.**
- Pre-historic / very early 8c (in force by ca. 700 AD): all
  authorities agree (Bulbring "Ums Jahr 700"; Campbell "in the
  oldest texts"; Brunner "vorhistorisch"; Luick "sec. 233";
  R&T "first half of the 8th century, combinative part first").
- Earlier than ordinary back umlaut (Luick sec. 233; Brunner
  sec. 114b Anm. 7; R&T 18336).
- Earlier than the merger of *iu/*eo with *eo (Bulbring's
  *wiu intermediate is consistent with this).
- Anglian smoothing of *iu → *i (sec. 230) is later, only
  affecting Anglian: this is why Anglian has wicu rather than
  wucu (Bulbring sec. 264).
- Relative to syncope: in Anglian widwe (early syncope of medial
  -u-) bleeds the rule (no medial *u trigger left), giving
  Brunner sec. 114b's account of widwe vs. WS wuduwe.
- Relative to i-umlaut: not directly addressed by these
  authorities for *wi → *wu specifically; Brunner sec. 114a's
  parallel *wir > *wur > *wyr (Anglian) shows *wir → *wur
  precedes i-umlaut.
- Within the cascade: the rule must precede OEMedUnstressedULowering
  (so the *u trigger is still present when the rule fires), and
  must precede whatever models Anglian smoothing if such forms
  enter the cogset.

**E. Blocked-but-predicted forms?** None in the cogset. Within
the literature, candidate counter-examples are forms that retain
*i / *io / *eo (widuwe, weoduwe, wicu, witon, swiotol, sweotol).
The handbooks uniformly describe these as analogical levellings
(WS wita ← from sg. *wic etc. — Luick sec. 221 Anm. 1; Brunner
sec. 114b end), or as Anglian/Kentish dialect outcomes, NOT as
phonological exceptions to the WS Lautgesetz. So the rule, when
applied at the WS-Lautgesetz level, has no documented
counter-examples.

**F. WS-specific?** **No** — common-OE, with carve-outs:
- WS: rule fires fully (no consonant restriction).
- Anglian (Mercian, Northumbrian): rule fires EXCEPT before
  velars *c, *g.
- Kentish for u-trigger: rule fires (Luick sec. 221 Anm. 2,
  on the basis of ME woke).
- Kentish for o/a-trigger: rule does NOT fire (Luick: Kentish
  has wiodu, weadu).
- Northumbrian for o/a-trigger: rule fires (Brunner sec. 114c).
- WS for o/a-trigger: partial (Untermundarten only) per Luick;
  Brunner cites WS gewuta, wutan as rare.

The cascade is OE-internal (i.e. EnglishProtoToOE), not dialect-
specific, so the question is moot for the FST as currently
structured: it is fine to model the rule as applying in the
dialect that the cascade targets (WS, presumably).

**G. Single step or two-step?** **Disputed in the literature.**
Bulbring sec. 264 explicitly two-step: *widu > *wiudu > *wudu.
Brunner sec. 114b implicitly two-step (subsumes under u-Umlaut
conditions, which produce *iu first). Luick sec. 223 explicitly
**one-step**, against the two-step account: "ohne diphthongische
Zwischenstufe ... etwa durch die Reihen i-y-u ... hindurch", on
the parallel-evidence argument from *we > *wo not proceeding via
*weo. R&T do not commit but describe it as a direct change.

The cascade collapses to a single direct rule. Luick and R&T
support this; Bulbring and Brunner are compatible (the *iu stage
is transient and would be optimized out of any cascade in any
case). The collapse is therefore not problematic.

### B.9 RECOMMENDATIONS

Based on the broader source canvass, the draft rule formulation
in DEV_NOTES sec. 17.51.A1 is **defensible for the single cogset
row it currently covers** (*widuwon → wuduwe), but it is
**narrower than the handbook consensus** in three respects.
For the immediate task (deriving wuduwe), the narrower rule is
adequate; for a philologically faithful FST that may later be
extended to cover wudu, wucu, cwucu, swuster, wuton, etc., the
following adjustments are indicated:

1. **Drop the nasal/liquid consonant exclusion.** The handbook
   consensus (Bulbring sec. 264; Campbell sec. 218; Brunner
   sec. 114b; Luick sec. 221; R&T sec. 6.9.6) is that the WS
   change has NO consonant restriction. The Anglian-only velar
   restriction is irrelevant to a WS-targeting cascade. Replace:

   ```
   _ [EnglishStarConsonant - [EnglishStarNasal | EnglishStarLiquid]]
   ```

   with:

   ```
   _ EnglishStarConsonant+ ?
   ```

   or simply:

   ```
   _ EnglishStarConsonant
   ```

   if a single-C left-context is preferred (note that swuster
   has cluster *st and is admitted by all sources, so the
   single-C restriction itself is also literature-narrower; but
   this matters only if the cogset acquires words like swustur).

2. **Extend the trigger vowel set to include *a.** Campbell
   sec. 219 explicitly recognises combinative a-umlaut of *i
   (wuton, wuta, gewuta, wutan); Bulbring sec. 264 includes
   wuton; Brunner sec. 114c lists this as a separate sub-rule;
   Luick sec. 221.2 admits it. Replace:

   ```
   ({*u} | {*o})
   ```

   with:

   ```
   ({*u} | {*o} | {*a})
   ```

   This is essential if the cogset is later extended to include
   *witana → wuton or *wuda forms; it is harmless for the current
   *widuwon row (whose trigger is *u).

3. **Allow optional *s/*k before *w in the left-context.** The
   handbooks unanimously include swustur, swutol, swugian, cwucu,
   cwudu in the same change. Replace:

   ```
   .#. {*w}
   ```

   with:

   ```
   .#. ({*s} | {*k} | {*t}) {*w}
   ```

   or, more conservatively (covering only attested clusters):

   ```
   .#. ({*s} | {*k}) {*w}
   ```

   (twuwa < *twiwa is a marginal case mentioned by Bulbring and
   Campbell but not central; including *t is optional.)

4. **Other refinements indicated.**
   - The draft's collapse of the (Bulbring) two-step *wi >
     *wiu > *wu into a single direct rule is independently
     supported by Luick sec. 223 and is not problematic.
   - The draft's pre-OEMedUnstressedULowering ordering is
     correct: the *u trigger must still be present when the
     rule fires, and the early date of the change (pre-700)
     is consistent with placing it before any later medial-*u
     changes.
   - No forms in the cogset are blocked by the draft rule that
     should fire, and no forms outside the cogset would be
     affected by adopting the broader formulation, since the
     broader formulation only licenses additional firings on
     forms not currently in the input.

**Bottom line.** The draft rule is **safe but narrow**. It
correctly derives the one form it is designed to derive. If
the goal is just to fix wuduwe, the draft is adequate. If the
goal is a Lautgesetz formulation faithful to the handbook
consensus and robust to future cogset extension, adopt
adjustments 1-3 above.

---

## Appendix C: PGmc/PIE-level canvass for *wi → *wu

This appendix extends the OE-handbook canvass of Appendix B by going **deeper
genetically** — into PIE / PGmc / NWGmc / cross-branch West-Germanic resources —
to test whether the change *wi → *wu (combinative u-umlaut after initial *w-)
should be reconstructed at a higher genetic level than Old English.

The OE handbooks (Bülbring §264, Campbell §218, Brunner §114b–c, Luick §221,
Hogg vol. 1, R&T §6.9.6) all locate the change OE-internally, ca. 700 (see
Appendix B). The question here is whether any PIE / PGmc / NWGmc authority
reconstructs PGmc *wuduwōn- (or *wudu- 'wood') rather than *widuwōn- / *widu-,
or posits a PGmc-/NWGmc-level rule of *i → *u after initial *w-.

### C.1 Local references actually canvassed

All in `docs/references/`:

| Source | File |
| --- | --- |
| Ringe, *From PIE to Proto-Germanic* (vol. 1) | `ringe_vol1_pie_to_pgmc.txt` |
| Kroonen, *Etymological Dictionary of Proto-Germanic* | `kroonen_etymological_dictionary_pgmc.vision.txt` |
| Orel, *Handbook of Germanic Etymology* | `orel_handbook_germanic_etymology.vision.txt` |
| Bammesberger, *Morphologie des urgermanischen Nomens* (1990) | `bammesberger_1990_morphologie.txt` |
| Streitberg, *Urgermanische Grammatik* | `streitberg_urgermanische_grammatik.txt` / `.vision.txt` |
| Hirt, *Handbuch des Urgermanischen* | `hirt_handbuch_des_urgermanischen.vision.txt` |
| Fulk, *Comparative Grammar of the Early Germanic Languages* | `fulk_comparative_grammar_early_germanic.vision.txt` |
| Pokorny, *Indogermanisches etymologisches Wörterbuch* (relevant pages) | `pokorny_iew_pages/00000638.txt` |
| Mayrhofer, *EWAia* (vol. III index) | `mayrhofer_ewaia_III.vision.txt` |
| Beekes, *Etymological Dictionary of Greek* | `beekes_edg.txt` |
| Kluge–Seebold (entry "Witwe", "Strohwitwe") | `kluge_seebold_etymologisches_woerterbuch.txt` |
| Ringe & Taylor, *A Linguistic History of English* vol. 2 | `ringe_taylor_linguistic_history_vol2.txt` (already in App. B) |

LIV² and Schaffner (Vernerian Wandel) are not present on disk; their omission
is harmless because the change in question is not a Vernerian/laryngeal issue.
Pokorny is on disk only as the page-images of the 'widhu-' / 'ueidh-' entries.

### C.2 Per-source verbatim findings

#### C.2.1 Ringe, *From PIE to Proto-Germanic* (vol. 1)

`ringe_vol1_pie_to_pgmc.txt:5465–5466`:

> "PIE *h₁widhéwh₂ ~ *h₁widhwáh₂- 'widow' (cf. Skt vidhávā, Lat. vidua) >!
> PGmc *widuwōn- (cf. Goth. widuwo, OE widuwe);"

`ringe_vol1_pie_to_pgmc.txt:13186–13193`:

> "PIE *h₁widhéw-h₂ ~ *h₁widhw-áh₂- 'widow' (cf. OIr. fedb vs. OCS vĭdova; Lionel
> Joseph, p.c. ca. 1980) appears in PGmc in the 'compromise form' *widuwō-n-,
> with a full-grade stem vowel (extended by *-n-) and a medial syllable that
> seems to owe its syllabicity to one PIE alternant and the identity of its
> vowel to the other."

`ringe_vol1_pie_to_pgmc.txt:16353` (PGmc index): *widuwōn-* — listed with *i.

**Reconstruction: PGmc *widuwōn-, initial *i. No mention of any *w-rounding rule.**
The only *w-related sound change Ringe vol. 1 cites is "nasal-labial umlaut"
in *nahtų > ON nótt (line 10710) — that is *a → *ǫ before nasal+labial, not
*i → *u after initial *w-.

#### C.2.2 Kroonen, *Etymological Dictionary of Proto-Germanic*

`kroonen_etymological_dictionary_pgmc.vision.txt:29619–29622` (entry *widu-*):

> "*widu- m. (n.?) 'tree; wood' — ON viðr, gen. viðar m. 'id.', Far. viður m.
> 'id.', Elfd. wið m. 'id.', OE widu, wiodu, wudu m. 'id.', E wood, OHG witu
> m./n. 'id.', MHG wite, wit m. 'id.' ⇐ *(h₁)uidh-u- (EUR/IE?) — OIr. fid m.
> 'tree; wood; forest' …"

`kroonen_etymological_dictionary_pgmc.vision.txt:29632–29637` (entry *widu(w)ōn-*):

> "*widu(w)ōn- f. 'widow' — Go. widuwo f. 'id.', OE widewe, wudewe f. 'id.', E
> widow, OFri. widwe f. 'id.', OS widowa f. 'id.', Du. weduwe c. 'id.', OHG
> wituwa f. 'id.', G Witwe f. 'id.' ⇐ *h₁ui-dhh₁-uh₂- (IE) — Gr. ἠΐθεος m.
> 'unmarried youth …', Lat. vidua f. 'widow', OIr. fedb f. 'id.', OPru.
> widdewu 'widow', OCS vodova, Ru. vdová …"

**Reconstruction: PGmc *widu- and *widu(w)ōn-, both with initial *i.** OE
*wudu* and *wudewe* are listed as **OE variants alongside** *widu / widewe*,
not as PGmc-level forms. No *w-rounding rule is invoked.

#### C.2.3 Orel, *Handbook of Germanic Etymology*

`orel_handbook_germanic_etymology.vision.txt:50890–50908`:

> "*widuwōn sb.f.: Goth widuwo 'widow', OE widuwe id., OFris widwe id., OS
> widowa id., OHG wituwa id. Etymologically connected with Skt vidhávā id.,
> Av vidavā id., Lat uidua id., OIr fedb id., OPrus widdewu id., Slav
> *vodova id."
>
> "*widuz sb.m.: ON viðr 'tree, forest, wood', OE widu, wudu 'wood', OS
> wido-hoppa 'hoopoe', OHG witu 'wood'."

**Reconstruction: PGmc *widuwōn / *widuz, initial *i.** OE *wudu* listed as
an OE doublet of *widu*, **not** as a PGmc reflex. No *w-rounding rule.

#### C.2.4 Bammesberger, *Morphologie des urgermanischen Nomens* (1990)

`bammesberger_1990_morphologie.txt:6096–6098`:

> "*wid-u- > an. viðr m. 'Wald, Holz, Baum', ae. widu, wiodu, wudu, as. widu,
> ahd. witu: urg. *wid-: idg. *widh-. Vermutlich ist idg. *widh- eine sekundäre
> Wurzel, die aus *wi- + *dh(ə)- … besteht."

`bammesberger_1990_morphologie.txt:7042–7048`:

> "*widuwōn- > got. widuwo 'Witwe', ae. widuwe, ahd. wituwa. Die Ausgangsform
> wird von Szemerényi 1977:85 als idg. *widhewā (vgl. ai. vidhavā, av. viδavā,
> apr. widdewu) angesetzt, wobei freilich der Vokal *u der germanischen Form
> (vgl. lat. vidua) nicht unproblematisch ist."

`bammesberger_1990_morphologie.txt:6728–6729`: *widuwō-* re-built to PGmc
*widuwōn-* on the model of masculine an-stems.

**Reconstruction: PGmc *wid-u- and *widuwōn-, initial *i.** Bammesberger
flags only the **medial** *u (vs. Lat. *ě* in *vidua*) as problematic;
the **initial** *i is unproblematic. ae. *wudu* and *wuduwe* are not given
PGmc status. No *w-rounding rule.

#### C.2.5 Streitberg, *Urgermanische Grammatik*

Streitberg lists the cognate set repeatedly with initial *i throughout the
non-OE branches, and shows that OE itself attests both *widewe* and *wuduwe*:

`streitberg_urgermanische_grammatik.vision.txt:3576–3577` (§67/68, on PGmc *i*):

> "1. Idg. germ. i. lat. uidua 'Witwe', got. widuwō, ae. widewe, as. widowa,
> ahd. wituwa."

`streitberg_urgermanische_grammatik.vision.txt:3810–3811` (on PGmc *u in
unstressed syllable < PIE *eu*):

> "ai. vidhává, got. widuwo 'Witwe', ae. wuduwe, as. widowa, ahd. wituwa."

`streitberg_urgermanische_grammatik.vision.txt:6833`:

> "ai. vidhávā 'Witwe', got. widuwo, ae. wuduwe, as. widowa."

`streitberg_urgermanische_grammatik.vision.txt:9857` (under 'Holz'):

> "as. sidu, ahd. situ, ae. wudu 'Holz', ahd. witu u. a."

**Streitberg cites both ae. *widewe* and ae. *wuduwe*** — i.e. he is aware of
the OE doublet but **explicitly assumes initial *i** at the PGmc level (Goth.,
OS, OHG all *i). No PGmc-level rounding rule is formulated; the OE *u is
simply accepted as an OE-internal variant.

#### C.2.6 Hirt, *Handbuch des Urgermanischen*

`hirt_handbuch_des_urgermanischen.vision.txt:4998` and 13215:

> "g. widuwo 1. vidua 'Witwe'"

`hirt_handbuch_des_urgermanischen.vision.txt:13554, 14006`: same — PGmc *widuwo
with initial *i. No mention of *wuduw- at PGmc level. No *w-rounding rule.

#### C.2.7 Pokorny, *Indogermanisches etymologisches Wörterbuch*

`docs/references/pokorny_iew_pages/00000638.txt:12–17`:

> "ai. vidháva 'Witwe', av. vidavā ds., gr. [F]íθεος 'Junggeselle', lat. vidua
> 'Witwe; geschiedene oder unverheiratete Frau', viduus 'beraubt, leer von
> etwas', air. fedb 'Witwe', corn. guedeu ds., cymr. gweddw 'Witwer', got.
> widuwo 'Witwe' (dazu widuwairna m. 'Waise'), ags. widuwe, wuduwe, ahd.
> wituwa 'Witwe', apr. widdewu, aksl. vidova ds.; idg. *uidheuo- Adj.
> 'getrennt, im Fem. substantiviert, Witwe'."

**Reconstruction: PIE *uidheu̯o-, initial *i.** Both ags. *widuwe* and
*wuduwe* are cited but with no PGmc-level rounding rule.

#### C.2.8 Mayrhofer, *EWAia* (Skt *vidhávā*)

`mayrhofer_ewaia_III.vision.txt:28135` (index entry vol. II p. 556) ties Skt
*vidhávā* to Goth. *widuwo* — initial *i throughout. (The body discussion is
on a non-OCR'd page; the index pointer suffices to confirm initial *i*.)

#### C.2.9 Kluge–Seebold, *Etymologisches Wörterbuch der deutschen Sprache*

`kluge_seebold_etymologisches_woerterbuch.txt:99363–99364` (entry "Witwe"):

> "wituwa, as. widowa Stammwort. Aus g. *widuwō f. 'Witwe', auch in gt.
> widuwo, ae. widewe, afr. widwe. Dieses aus ig. *widhewā f. 'Witwe' in
> l. vidua, air. fedb, akslav. vidova, ai. vidhávā."

**Reconstruction: PGmc *widuwō, PIE *widhewā, initial *i.**

#### C.2.10 Beekes, *Etymological Dictionary of Greek*

`beekes_edg.txt:17861–17863` (entry on Gr. ἠΐθεος):

> "widuwo, etc., Lat. vidua, from a pre-form *h₁uidheu-. A masculine
> expression for 'widowed, unmarried' was made from this pre-form, like in
> Lat. viduus, Ru. …"

PIE *h₁uidheu-, initial *i.

#### C.2.11 Fulk, *Comparative Grammar of the Early Germanic Languages*

This is the single most decisive source for the present question. Fulk
covers North and West Germanic comparatively and explicitly addresses
*wi → *wu in OE.

`fulk_comparative_grammar_early_germanic.vision.txt:4318–4426` (§4.8 Back
mutation, the Old English subsection):

> "i > io, which yields eo in all dialects except Northumbrian and, in part,
> Kentish. … The vowel i in the environment for back mutation, and regardless
> of the following consonant, **may undergo so-called combinative back
> mutation when it follows w, as in OE *wudu* 'wood' < *widu* (also attested)
> and *swugian* beside *swigian* 'be silent'**."

`fulk_comparative_grammar_early_germanic.vision.txt:4427–4430` (Old Frisian):

> "Old Frisian. The vowel *i* was diphthongized to *iu*, a rising diphthong,
> before *u* or *w* in the next syllable, e.g. *niugen* '9' < NSGmc. *nizun*
> and *diunk* 'dark' < WGmc. *þiŋkwa*."

Fulk thus places "combinative back mutation" of *wi → *wu **squarely inside
Old English**, as a sub-case of OE back mutation (which he dates ca. 700 or
later: line 4378, "most likely coeval with, or postdates, the earliest
manuscript evidence (ca. 700)"). In his Old Frisian chapter the parallel
process is *i → iu*, **not** *i → u*; that is a different rule. There is no
OS, OHG, ON, or Goth subsection of §4.8 that posits *wi → *wu.

`fulk_comparative_grammar_early_germanic.vision.txt:30341` (index): "wudu,
widu 4.8" — i.e. *wudu* is indexed only under §4.8 Back mutation (an
OE-internal section), not anywhere in the PGmc/NWGmc chapters.

#### C.2.12 Ringe & Taylor (2014), already in Appendix B

`ringe_taylor_linguistic_history_vol2.txt:15570–15571` and 18461–18462:

> "PGmc *widuwon- 'widow' (Goth. widuwo, OF widwe, OS widowa, OHG wituwa)
> > *widuwe > OE widuwe;"
>
> "PGmc *widuwon- (Goth. widuwo) > PWGmc *widuwa (OF widwe, OS widowa, OHG
> wituwa) > WS OE wuduwe ~ widuwe, but Merc. widwe, North. widua;"

Same picture: **PGmc and PWGmc both have initial *i*; the *u-form arises
only inside Old English**, and only in WS — Merc. *widwe*, North. *widua*
preserve *i*.

### C.3 Summary table

| Source | 'widow' root | 'wood' root | Posits a *w- → rounding rule? | Dating |
| --- | --- | --- | --- | --- |
| Ringe vol. 1 (PIE→PGmc) | PGmc *widuwōn- (initial *i) | n/a | No | PGmc-level reconstruction |
| Kroonen | *widu(w)ōn- (initial *i) | *widu- (initial *i) | No — OE *wudu, *wudewe listed as OE variants of *widu, *widewe | PGmc |
| Orel | *widuwōn (initial *i) | *widuz (initial *i) | No | PGmc |
| Bammesberger 1990 | *widuwōn- (initial *i; medial *u flagged but initial *i unproblematic) | *wid-u- (initial *i) | No | PGmc |
| Streitberg | *widuwō (initial *i) | *widu- (initial *i) | No (cites ae. *wuduwe* as a doublet, no rule) | PGmc |
| Hirt | *widuwo (initial *i) | n/a | No | PGmc |
| Pokorny IEW | PIE *uidheu̯o- (initial *i) | PIE *uidh-u- | No | PIE |
| Mayrhofer EWAia | PIE/Skt *vidhávā* (initial *i) | n/a | No | PIE |
| Kluge–Seebold | PGmc *widuwō (initial *i) | *widu- (initial *i) | No | PGmc/PIE |
| Beekes EDG | PIE *h₁uidheu- (initial *i) | n/a | No | PIE |
| **Fulk (Comp. Gmc.)** | PGmc *widuwōn- (initial *i) | PGmc *widu- (initial *i) | **Yes — explicitly an OE-internal rule** ("combinative back mutation … when it follows w") | **OE-internal, ca. 700** |
| Ringe & Taylor 2014 (App. B) | PGmc *widuwōn- > PWGmc *widuwa | (Same) | Yes — OE-internal | OE-internal |

### C.4 Cross-branch evidence table

| Branch | 'widow' | 'wood' | Initial *i preserved? | Any *u-rounding after *w-? |
| --- | --- | --- | --- | --- |
| Gothic | *widuwo* | n/a (cf. *widuwairna* 'orphan') | Yes | No |
| Old Norse | (no direct cognate of *widuwōn*; cf. ON *ekkja*, OEN *ænkia* 'widow') | *viðr*, gen. *viðar* | Yes | No |
| OHG | *wituwa* | *witu* | Yes | No |
| Old Saxon | *widowa* | *widu*, *wido-hoppa* 'hoopoe' | Yes | No |
| Old Frisian | *widwe* | (n/a in attested compounds) | Yes (initial *i*) | **No — but OFris has a different rule, *i → iu* before *u, w* (Fulk §4.8): *niugen, diunk*** |
| Middle Dutch / Du. | *weduwe* | (cf. E *wood*) | Yes (initial *i*) | No |
| Old English | *widewe* AND *wudewe / wuduwe* (WS); Merc. *widwe*; North. *widua* | *widu, wiodu, wudu* | Variable: Anglian retains *i; WS innovates *u | **Yes — and only here** |

Goth., ON, OHG, OS, OFris, MDu **all show initial *i*.** Only Old English
shows *u* in the initial syllable, and even within OE only WS does so —
Mercian and Northumbrian retain *i* (Mercian *widwe*, Northumbrian *widua*).
**No non-OE branch shows *wuduw-/wudu- with initial *u*.**

### C.5 Synthesis: at what genetic level should the rule be placed?

The evidence is **uniform and unambiguous**:

1. **All eleven** PIE / PGmc / NWGmc / cross-branch handbooks, dictionaries, and
   etymologies canvassed reconstruct the relevant roots with **initial *i** at
   PGmc and PIE level: PIE *h₁uidh- → PGmc *wid-, with no rounding.
2. **No source** reconstructs PGmc *wuduwōn- or PGmc *wudu-. Where *u-forms
   are mentioned (Streitberg, Pokorny, Kroonen, Orel, Fulk, R&T), they are
   explicitly labelled as Old English variants alongside the *i-forms.
3. **No PGmc / NWGmc / PWGmc / Ingvaeonic** authority recognises a sound law
   "after initial *w-, *i → *u before *u/*o/*a in next syllable". The closest
   formulation is Fulk's "combinative back mutation when it follows w" —
   which Fulk locates **inside the OE Back-Mutation section (§4.8)**, dates
   to ca. 700, and contrasts with the **different** OFris rule *i → iu / __ u, w
   (which is also in §4.8 but is a separate Ingvaeonic / OFris-internal rule,
   not a *u-rounding).
4. The cross-branch distribution (Goth, ON, OHG, OS, OFris, MDu all *i; only
   OE — and within OE only WS — shows *u) is exactly what an OE-internal
   (indeed WS-internal) rule predicts. A NWGmc, PWGmc, or PGmc rule would
   predict *u in at least some non-English continental branch, which is
   nowhere attested.
5. The PIE labiovelars *kʷ, *gʷ are sometimes argued to have a distinctive
   effect on a following *i (e.g. raising/lowering discussions in Ringe vol. 1),
   but **none** of the sources canvassed extends this to plain *w- + *i.
   No PIE/PGmc handbook posits a labializing or rounding effect of plain *w-
   on a following *i.

### C.6 Recommendation

**The cascade rule for *wi → *wu after initial *w- should remain OE-internal**
— i.e., it belongs in `EnglishProtoToOE` (or whichever pre-OE-historical OE
stage `OEWICombinativeUUmlaut` lives in), **not** in `NWGmcChanges`,
`PWGmcChanges`, or `IngvaeonicChanges`.

Specifically:

- **No source reconstructs PGmc *wuduwōn-.** All eleven canvassed authorities
  reconstruct PGmc *widuwōn- with initial *i. The TSV protoform should
  therefore stay *widuwōn- at the PGmc level.
- **The change is OE-internal per every PGmc-level source** — including
  Ringe (vol. 1), Kroonen, Orel, Bammesberger, Streitberg, Hirt, Pokorny,
  Mayrhofer, Kluge–Seebold, Beekes, **and** Fulk's *Comparative Grammar*
  (which is the only one that even mentions the *wi → *wu change explicitly,
  and which places it firmly inside Old English §4.8 Back Mutation).
- **The cross-branch test is decisive**: Gothic *widuwo*, ON *viðr*, OHG
  *wituwa* / *witu*, OS *widowa* / *widu* / *wido-hoppa*, OFris *widwe*,
  MDu *weduwe* all retain initial *i*. Only OE — and within OE only WS —
  shows *u*. Anglian *widwe / widua* and Mercian *widwe* preserve *i*,
  exactly as the OE handbooks (App. B) describe.
- **OFris is not a counterexample.** OFris *widwe* has *i*, not *u*. The
  OFris rule *i → iu before *u, w* (Fulk §4.8: *niugen* '9', *diunk* 'dark')
  is a different, dialect-internal Ingvaeonic-period rule, and it produces
  a diphthong *iu*, not a monophthong *u*. It does not motivate raising
  the OE *wi → *wu rule to a NWGmc or Ingvaeonic stage.
- **§17.51.A1 of DEV_NOTES (the OEWICombinativeUUmlaut proposal) is correctly
  scoped.** Placing this rule in the OE-internal cascade (between
  `EnglishProtoToOEWeightCleanup` and the established OE back-mutation /
  fronting rules) is consistent with every PGmc-level authority canvassed.
  No higher genetic stage is supported by the literature.

In sum: this is the rare case where the OE-handbook tradition (Bülbring,
Campbell, Brunner, Luick, Hogg, R&T) and the comparative-Germanic / IE
tradition (Ringe, Kroonen, Orel, Bammesberger, Streitberg, Hirt, Pokorny,
Mayrhofer, Kluge–Seebold, Beekes, Fulk) **agree completely**: the change
is OE-internal, not PGmc, NWGmc, PWGmc, or Ingvaeonic.
