# Dossier: the OE *heofon / hefen / heben* 'heaven' word — paradigm history and CAPR modelling (2026)

**Type:** first-principles research dossier. **No production change.**
**Branch:** `stem-row-2216-correction` · **HEAD at authoring:** `22d31464`.
Supersedes the piecemeal treatment in `audits/heaven-paradigm-cell-lautgesetzlich-probe.md`
(whose central proposal is here **corrected**) and complements
`dossier-sc022-mn-dissimilation-2026.md`,
`audits/sc022-heaven-allomorph-shadow-redesign.md`,
`audits/2216-stefn-shadow-rule-probe.md`.

Evidence levels are labelled throughout: **[MS]** manuscript, **[DIPL]**
diplomatic edition, **[NORM]** normalized corpus/edition, **[DICT]** dictionary
headword, **[RECON]** reconstruction. These are never silently conflated.

---

## 1. Executive conclusion

> **IMPLEMENTED DECISION (see §15, authoritative):** row 2068 = PROTO `*xémenaz`,
> PROTOFORM `*xébun`, COUNTERPART `heofon`, DERIVATION_CLASS **`early_analogy`**;
> SC022 becomes the literal adjacent `mn > βn`. Provisional `known_unmodelled`
> judgements in §10/§13.5/§14.8 are **superseded** by §15.

**Confident:**
- The Germanic labial (`f`/`b`/`β`) in this word originates in the **oblique
  `-mn-` cluster** of an old mn-stem and was **levelled** into the vowel-bearing
  cells. Every attested OE form combines the levelled labial **with** a medial
  vowel — an **analogical** combination, not a single-cell phonological reflex.
- The stressed `e : eo` split (`hefen`/`hefun` vs `heofon`) is OE **back
  mutation** conditioned by the medial vowel (Hogg: `*hefon > heofon`), partly
  continuing the inherited `*-en-/-on-` suffix ablaut; it is dialectally
  variable and, in the syncopated obliques, **levelled/pre-syncope** rather than
  regular before the `-fn-` cluster.
- **Bare OE `hefn` is not securely attested.** The earliest forms (Cædmon's
  Hymn) are `hefun`, `hefen`, and (Moore Bede) `heben` — **all with a medial
  vowel**. The earlier `hefn` recommendation rested on a normalized abstraction,
  not a manuscript witness, and is withdrawn.
- Computationally: a **genuine adjacent `mn > βn` rule** derives only
  `hefn`/`hefnes`/`hefnum` — **none attested**; the attested `heofon`/`hefen`
  arise only via the **ahistorical `mV…n` proxy** or from a **pre-labialized
  input** (`*héfon`).

**Uncertain:** the exact chronology/dialect ordering of leveling vs back
mutation; whether Northumbrian back mutation could reach a `-fn-` cluster; the
security of Kroonen's specific `*hemō/*hemnaz/*hemeni` remodelling.

**Bottom line (revised — see §13 addendum).** The 2026-08 research pass
sharpened this. The history is now describable as **two analogies bracketing a
real regular span**: an **early** analogy levels the oblique-cluster labial into
the vowel-bearing stem (giving Ringe–Taylor's northern-WGmc **`*hebun`**), then
**regular OE back mutation** derives `heofon` (exactly parallel to *seven*
`*sebun -> seofon`), then a **late** paradigm levelling + optional syncope give
the obliques. Crucially, a shadow probe now shows that CAPR's **real** cascade
(no proxy) derives attested `heofon` from a labial-bearing input `*hebun`
(`*xébun` ~ `*xéfun`) — the labial-levelling analogy simply lives *in the input*,
which is exactly what CAPR's `early_analogy` class is for. This **upgrades** the
old `*héfon` fallback of §10 into a genuine, better-motivated modelling option.

The revised recommendation (§10, §13.5) is therefore: **model heaven as
`early_analogy` from `*hebun -> heofon`** (regular back mutation, no proxy;
parallel to *seven*), **with `known_unmodelled` as a fully-legitimate
conservative fallback** (the correct tier — the history is *understood*, cf.
§13.1 — not `unexplained_unmodelled`). Either way the ahistorical `mV…n` proxy
is retired and SC022 becomes literal adjacent `mn > βn`, which also lets `stem`
derive `stefn`. The one thing still excluded is any *single-cell* span from a
**citation** input to an attested form: `heaven` remains "too remodeled" in that
narrow sense, but that is not the choice CAPR actually faces.

**Deepest-span finding (2026-08-14 — see §14).** A further pass stopped
privileging the nominative and asked how far the **labial itself** can be derived
by regular sound change. Answer: **very deep — to the inherited genitive.** In
the zero-grade oblique cells (gen. `*hemnaz` < PIE `*h₂k-mn-ós`, dat. `*hemni`,
dat.pl `*hemnum`) the change `mn > βn` is regular and mult-1 (shadow traces,
§14.2), so the `f/b` of OE `heofon` has continuous **regular** ancestry back to
PIE — a real advance on Ringe–Taylor, who merely posit the `b` of `*hebun`. But
the *clean* cluster outputs (`hefnes`, `hifn`, `hefnum`) are attested only in
**Norse** (ON `hifni`), **not** in Old English; the attested OE forms descend
from a **re-vowelled** `*hebun-` stem (labial already present, then regular back
umlaut/​syncope). The labial-deriving line and the attested-OE line are thus
**different cells**, joined only by one non-regular event (restoration of the
medial vowel). For this pass row 2068 is therefore held **provisionally
`known_unmodelled`** — not for want of history but because its regular history is
**split across paradigm cells** and cannot be one deterministic CAPR path. The
`early_analogy` `*hebun -> heofon` option above remains available if a modelled
datum is later wanted; §14 does not withdraw it, but shows why the honest
row-level label is `known_unmodelled`. The residue that stays genuinely
unrecoverable is the medial **`u`** (its ablaut source), never the `b`.

---

## 2. History of the CAPR problem

- **Current production (row 2068):** PROTO `*xémenaz`, PROTOFORM `*xémonų`
  (acc.sg., **intervocalic** m), COUNTERPART `heofon`, class `late_analogy`.
  It derives `heofon` **only** because live SC022 `PNWGmcMnDissimilation` uses a
  surface `m -> β / V _ V … N` **proxy** that labializes an intervocalic `m`.
- **`dossier-sc022-mn-dissimilation-2026.md`** established (sources) that the
  *real* historical change is the adjacent-cluster `-mn- > -bn-`, and that the
  `mV…n` environment is a segmental proxy for mn-stem allomorphy.
- **`sc022-heaven-allomorph-shadow-redesign.md`** showed that replacing the
  proxy with adjacent-mn **breaks** heaven if its target stays `heofon`
  (`*xémonų -> heomon`), and that no PGmc adjacent-`mn` allomorph yields `heofon`.
- **`heaven-paradigm-cell-lautgesetzlich-probe.md`** then proposed retargeting
  heaven to nom `hefn` (`*xémnaz -> hefn`) to get 380/373/7/0. **This dossier
  corrects that**: `hefn` is not securely attested; the attested nom is
  `hefen`/`hefun`/`heben` (medial vowel), which the clean adjacent-mn rule does
  **not** produce.
- **Sound lesson preserved:** a [NORM]/[RECON] form is not an [MS] attestation.

---

## 3. Etymology and reconstructed morphology

PIE **`*h₂ék-mōn`** 'stone; heavenly vault', gen. `*h₂k-mn-ós`, loc.
`*h₂k-mén-i` — a classic amphikinetic **mn-stem** (cf. Gr. ἄκμων 'anvil, sky',
Skt. áśman- 'stone', Lith. akmuõ) [RECON] (Kroonen EDPG p. 220,
`kroonen_etymological_dictionary_pgmc.vision.txt:12428`; Lühr 2000: 79).

Kroonen: since regular Gmc `*ahmōn/*humnaz/*meni` is impossible (`*hm-` banned),
the paradigm was **remodelled on the genitive** into nom. **`*hemō`**, gen.
**`*hemnaz`**, dat. **`*hemeni`** [RECON]. Two daughter stems split off: the
vowel-bearing **`*hemina-`** (→ Go `himins`, ON `himinn`) and the cluster
**`*hemna-`** (→ OE `heofon`, OS `heban`). Kroonen offers three framings (two
stems; syncope `*hemina- > *hemna-`; both from the oblique paradigm) and prefers
the last.

The medial-vowel suffix is the inherited n-stem **`*-en-/-on-`** ablaut (Fulk
`fulk_comparative_grammar_early_germanic.vision.txt:8239,10212,10263`: PIE
`*-en-/-on-`, loc. `*-en-i`/`*-on-i`). This is the ultimate source of the OE
`-en-` (front) vs `-on-` (back) medial-vowel variation.

| Cell | PGmc [RECON] | adjacent `mn`? | certainty | CAPR notation |
| :-- | :-- | :-: | :-- | :-- |
| nom.sg | `*hemō` / a-stem `*hemnaz` | (`*hemō` no; a-stem `*hemnaz` yes) | moderate | `*xémnaz` |
| gen.sg | `*hemnaz`/`*hemnas` | yes | moderate | `*xémnas` |
| dat.sg | `*hemeni` (full) / `*hemni` (sync.) | full: no; sync.: yes | low–moderate | `*xémeni`/`*xémni` |
| dat.pl | `*hemun-miz` → `*hemnum` | yes (syncopated) | low–moderate | `*xémnum` |
| vowel-stem | `*hemina-`/`*hemun-` | **no** (intervocalic m) | moderate | `*xémin-`/`*xémun-` |

**Key point:** the `f`-bearing OE forms cannot come from the vowel-stem cells
directly (their `m` is intervocalic and would survive); they require the labial
from the **cluster** cells, **levelled** into the vowel-bearing stem.

---

## 4. Comparative Germanic evidence

| Lang. | nom | oblique | labial | medial V | note |
| :-- | :-- | :-- | :-- | :-- | :-- |
| Gothic | `himins` | `himinis` | m | i | vowel-stem generalized; no labial |
| Old Norse | `himinn` | **dat. `hifni`** | m (nom) / **f (obl.)** | i (nom) / — (obl. syncope) | oblique `-mn- > -fn-` preserved (Kroonen 2011:1770) |
| Old English | `heofon`/`hefen`/`hefun` | gen. `heofnes`, dat.pl `heofnum` | **f/b** (all) | eo/e/u | labial levelled through paradigm |
| Old Saxon | **`heban`** | **gen. `hebenes`** | **b** (all) | e | labial levelled; medial vowel throughout (Fulk `:5946`) |
| OHG/G | `himil`/`Himmel` | — | m | i | heteroclitic `l`-stem |

**Reading:** ON is the crucial witness — it **keeps the paradigmatic
alternation** (nom `himinn` with `m`, oblique `hifni` with `f` from the
syncopated `-mn-` cluster). OE and OS, by contrast, **generalized the labial**
into every cell (incl. the vowel-bearing nom): OE `heofon`/`hefen`, OS
`heban`/`hebenes`. That generalization is the analogical event at the heart of
the problem.

---

## 5. Old English phonological problems

**(a) `mn > βn/fn`.** Real but a **cluster** change (Fulk §6.11 p. 121,
`:7365`, "changes common to Germanic"; Polomé pp. 818–819; K-S s.v. Himmel).
It applies to `-mn-` (adjacent), i.e. the **oblique/syncopated** cells, not to
intervocalic `-mVn-`. Hence the labial is regular only in the cluster cells and
**analogical** in the vowel-bearing cells.

**(b) Back mutation.** Hogg (`hogg_vol1.txt:5678-5694`): WS back mutation
`e -> eo` only before **a single** intervening labial/liquid + back vowel; his
paradigm example is **`*hefon > heofon`** (the `f` already present, back medial
`o`). Crucially, "morphological alternations could be caused by this change, but
in West Saxon the alternations were normally **levelled out**." So `heofon`
(back-vocalic cell) vs `hefen` (front-vocalic cell) is a **regular back-mutation
alternation** over an **already-labialized** stem. Campbell §210
(`campbell_old_english_grammar.txt:6318`) gives the same `hefen`/`heofon` split;
§381 (`:10332`) "**heofon is for older hefen**" with the `-in/-un/-an` suffix.

**(c) Medial-vowel variation.** The `-en-`/`-on-`/`-un-` medial vowels continue
the inherited `*-en-/-on-` ablaut (Fulk `:8239` etc.), later reduced (§d).
`hefen` ≠ `heofon` is **not** merely orthographic: the medial vowel conditions
back mutation.

**(d) Unstressed reduction.** `heofonas > heofenas`: reduction of the **medial**
back vowel to `/e/` (Hogg `:7617`, general reduction to `/e/`). This changes
`heo-fo-nas -> heo-fe-nas`; the **stressed `eo` is untouched**. Do not read
`heofenas` as `he-`-reversion.

**(e) Syncope.** Oblique cells lose the medial vowel: gen. `heofnes`, dat.
`heofne`, dat.pl `heofnum` (Hogg medial-vowel syncope `:5908-5950`; B-T
`:5170,:67495,:6389`). These expose `-fn-` directly — **but they carry `eo`**.
Since back mutation is not regular before the `-fn-` **cluster** (WS needs a
single consonant, §b), the `eo` of `heofnum` is either **levelled** from the
nom or **pre-syncope** (`*hefonum -> heofonum -> heofnum`). Either way it is
**not** a regular reflex of a syncopated `*hemnum` (which would give `hefnum`,
unattested).

**(f) Monophthongization / editorial normalization (§ below).** Later `eo > e`
and editorial normalization can erase the very `eo/e` contrast we depend on.

---

## 6. Dialect geography

- **West Saxon:** `heofon`; back mutation restricted (single labial/liquid +
  back vowel), so obliques' `-fn-` `eo` is levelled (Hogg §b).
- **Mercian:** Lord's Prayer `heofenum` (Hogg `:20445`) — `eo` + **reduced**
  medial `e`.
- **Northumbrian:** Lord's Prayer syncopated `heofnum`/`heofnas` (Hogg `:20445`);
  Cædmon's Hymn (earliest) `hefun`/`hefen`, Moore Bede `heben` — **pre-back-
  mutation** (Hogg: "Hefunricaes … lacking in back umlaut"), medial vowel + f/b.

No dialect provides a **bare `hefn`** or a **non-`eo` `hefnum`/`hefnes`** as a
secure surface form; the pre-back-mutation Northumbrian forms all retain the
medial vowel.

---

## 7. Old English attestation dossier (evidential status labelled)

| Form | cell | ms / source | dialect / date | labial | medial V | level |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| `hefun` | nom | Cædmon's Hymn, Rome ms (`Hefunricaes` 1b); also Moore | Nhb, ≤ c. 830 | f | u | **[MS]** (`caedmons…:769`) |
| `hefen` | nom | Cædmon's Hymn (6a); Di/Pa var. `efen` | Nhb | f | e | **[MS]** (`:627,:769`) |
| `heben` | nom | Moore Bede | Nhb, early | **b** (=/v/) | e | **[MS]** (`:775`) |
| `heofon` | nom | WS prose/verse passim | WS | f | o (→eo stressed) | [MS]/[NORM] |
| `heofnes` | gen.sg | Northumbrian; B-T `:5170` | Nhb/WS | f | ∅ (sync.) + eo | [MS]/[DIPL] |
| `heofnvm` | dat.pl | diplomatic Nhb | Nhb | f | ∅ + eo | **[DIPL]** |
| `heofnum` | dat.pl | Nhb Lord's Prayer (Hogg `:20445`); B-T `:6389` | Nhb/WS | f | ∅ + eo | [MS]/[NORM] |
| `heofenum` | dat.pl | Mercian Lord's Prayer (Hogg `:20445`) | Mer | f | e (reduced) + eo | [MS]/[NORM] |
| `heofones` | gen.sg | WS | WS | f | o + eo | [NORM] |
| **`hefn`** | — | **none secured** | — | f | ∅ | **[RECON]/[NORM] only — NOT [MS]** |
| `hefen` II = `heofon` | lemma | Clark Hall p. … `:21259` | — | — | — | **[DICT]** |

**Editorial caution (§5f):** several `heofon`/`heofnum` citations come through
[NORM]/[DICT]; the manuscript `eo` vs `e` and the `f` vs `b` must be checked per
witness. The Cædmon's Hymn `hefun`/`hefen`/`heben` are the securest early [MS]
data and are decisive: **the medial vowel is always present**.

---

## 8. Chronology (uncertainty marked)

1. PIE mn-stem `*h₂ék-mōn`, gen. `*h₂k-mn-ós` [RECON, secure].
2. PGmc remodelling → `*hemō/*hemnaz/*hemeni`, stems `*hemina-`/`*hemna-`
   [RECON, moderate].
3. NW/Common Gmc `-mn- > -bn-` in **cluster** cells (oblique) → `*hebn-`;
   vowel-cells keep `m` [RECON, moderate; Fulk/Polomé].
4. **Leveling** of the labial into vowel-bearing cells → `*hefun-/*hefin-`
   (OE/OS; ON does **not** level) [analogical, moderate].
5. OE **back mutation** `*hefon > heofon` in back-vocalic cells; `*hefen` stays
   `he-` [regular, dialectal; Hogg].
6. **Unstressed reduction** (`heofonas > heofenas`) [regular, late].
7. **Syncope** of medial vowel in obliques → `heofnes/heofnum` (carrying
   levelled/pre-syncope `eo`) [regular + analogy].
8. Later `eo` monophthongization; scribal/editorial normalization [late/graphic].

**Order that matters:** step 4 (leveling) precedes step 5 (back mutation) — the
back mutation operates on an already-labialized `*hefon`. This is why no clean
single-cell span reaches an attested form.

---

## 9. Competing historical analyses

- **A (back-vocalic regular):** `*hefon -> heofon` by regular back mutation, with
  later paradigm leveling. *Strength:* Hogg's own account; regular for the
  stressed vowel. *Weakness:* presupposes the labial already levelled in (step
  4); does not explain the `f` from a citation input.
- **B (adjacent-mn oblique + remodelling):** the `f` is regular in the oblique
  `-mn-` cluster (`*hemnaz -> *hefn`); `heofon` etc. are later remodelled.
  *Strength:* correct source of the labial (ON `hifni`; Fulk/Polomé).
  *Weakness:* the clean output is bare `hefn`/`hefnes` — **unattested**; every
  attested form has the medial vowel (leveling) and/or `eo`.
- **C (inherited paradigm allomorphy):** `he-` vs `heo-` partly continues the
  `*-en-/-on-` suffix ablaut + back mutation. *Strength:* Fulk on the suffix;
  explains the medial-vowel split. *Weakness:* still needs the labial leveled in;
  does not by itself yield a clean citation→attested span.
- **D (dialect/chronology):** `hefun/hefen/heben` (early Nhb, pre-back-mutation)
  vs `heofon` (later/WS). *Strength:* matches Cædmon's Hymn. *Weakness:* a
  descriptive layer, not a derivational span.
- **E (too remodeled):** no single reconstruction gives a **long** clean
  phonological derivation from a citation-level input to an **attested** OE
  form. *Strength:* matches every computational probe and the attestation record.
  **This dossier finds E the most accurate.**

**Predictions vs attestation (computational, this + prior probes):**
adjacent-mn `*hemnaz/*hemnas/*hemnum -> hefn/hefnes/hefnum` (**unattested**);
proxy `*xémenaz/*xémonų -> hefen/heofon` (**attested**, but via a pseudo-rule);
pre-labialized `*héfon -> heofon` (**attested**, real back mutation, but the
labial is pre-reconstructed). No probe yields an attested form by a long chain
of real changes from a citation input.

---

## 10. CAPR recommendation

**Primary recommendation — REVISED 2026-08 (see §13.5).** The prior draft of
this section made `known_unmodelled` the primary and `*héfon` a reluctant
"short-span" alternative. The new shadow probe (§13.4) and the classification
audit (§13.1) revise that ordering. **The recommended primary is now to model
heaven as `early_analogy` from Ringe–Taylor's `*hebun`** (`*xébun` ~ `*xéfun`)
`-> heofon`: a *regular* OE back-mutation span, shadow-verified with **no proxy**,
exactly parallel to the production-`regular` derivation *seven* `*sébun ->
seofon`. The early labial-levelling analogy is encoded **in the input** — which
is precisely the definition of CAPR's `early_analogy` class (Part III: "an
analogical change already separates the transducer input from the lexeme's
citation reconstruction before the specifically Old English changes apply").
**`known_unmodelled` remains a fully-legitimate conservative fallback** (§13.5);
it is the *correct tier* (history *understood*, unlike `unexplained_unmodelled`
— §13.1), appropriate if the project prefers not to compress the labial +
suffix-vowel remodelling into the input. Both retire the `mV…n` proxy.

The remainder of this section preserves the original (pre-revision) reasoning
for the record; read §13 for the superseding argument.

CAPR seeks the **longest defensible uninterrupted Lautgesetzlich span** and must
**not** invent a pseudo-sound-law to simulate analogy, choose an unattested
endpoint, or treat normalization as attestation.

**Findings that constrain the choice:**
- The current `mV…n` proxy **is** a pseudo-sound-law simulating the leveling —
  disallowed as a *sound change* (it survives only because heaven is its sole
  user).
- The clean adjacent-mn endpoints (`hefn`, `hefnes`, `hefnum`) are **unattested**
  — disallowed as endpoints.
- Every **attested** OE form is analogically leveled (labial + medial vowel;
  obliques' `eo` levelled/pre-syncope) — no long clean span exists.

**Primary recommendation (ORIGINAL — now the fallback; see §13.5) — classify row 2068 `known_unmodelled`.** *heaven* is
too remodeled to provide a clean CAPR datum. Concretely (future, do **not** edit
now):
- PROTO `*xémenaz` (citation) may remain.
- PROTOFORM: none that yields an attested form by real changes; mark the row
  `known_unmodelled` and record it as a documented exception alongside buck,
  fire, fowl, rust, tap, wolf, wool.
- Remove the `mV…n` proxy from SC022 and make SC022 the **literal adjacent
  `mn > βn`** (the proxy exists only for heaven; the sound change should be
  historically correct regardless of this lexeme). This **also** enables the
  independently-supported `stem` correction (§ below).
- Corpus effect (shadow-verified): adjacent-mn SC022 + `stem *stámniz` + heaven
  `known_unmodelled` → **380 / 372 / 8 / 0**, mismatch set {buck, fire, fowl,
  rust, tap, wolf, wool, **heaven**}.

**Acceptable alternative (ORIGINAL framing — now SUPERSEDED by the better-motivated
`*hebun` input of §13.4/§13.5), with full disclosure — short back-mutation-only span:**
- PROTOFORM `*héfon` (pre-OE English-branch, **post-leveling**: labial present,
  back medial vowel — Hogg's own `*hefon`), COUNTERPART `heofon` [attested WS
  nom], DERIVATION_CLASS `late_analogy` (the leveling is explicitly *outside*
  the span, encoded in the input).
- Trace: `*héfon -> OEBackMutation *héofon -> heofon` (regular; shadow-verified
  `*xéfon -> heofon` under both rule versions — no `mn` rule needed).
- **Analogy boundary:** everything up to and including the mn-dissimilation +
  labial leveling is pre-reconstructed in `*héfon`; only OE back mutation is
  modelled. *Confidence:* the span is real but **short**, and much history is
  baked into the input — hence this is an alternative, not the primary.
- Corpus effect: heaven matched (`heofon`), stem matched → **380 / 373 / 7 / 0**.

**Rejected:** (i) the current `mV…n` proxy as a *sound change*; (ii) retargeting
to bare `hefn` (unattested); (iii) targeting `hefnes`/`hefnum` (unattested,
non-`eo`); (iv) any choice made purely to raise the corpus score.

### Consequence for SC022
The heaven evidence **removes the last obstacle** to making SC022 the literal
adjacent `mn > βn`: heaven never needed a *sound change* for its labial (it needs
*analogy*, which CAPR encodes by input selection or by `known_unmodelled`), so
the `mV…n` proxy can be retired. This reconciles the earlier tension: **replace**
the proxy (not union), with heaven handled by data (exception or `*héfon`), and
stem gaining `stefn`.

### Consequence for row 2216 (stem)
Independently reconfirmed: `*stámniz -> stefn` (mult 1) under literal adjacent
`mn > βn`; `*stámnaz -> stæfn`. Unchanged by this dossier.

---

## 11. Shadow experiments (this dossier)

Adjacent-mn shadow SC022 (`{*m} -> {*β} || EnglishStarVocalic _ {*n}`),
ephemeral `/root`, production untouched:

| input | cell | prod (proxy) | shadow (adjacent-mn) | attested? |
| :-- | :-- | :-- | :-- | :-- |
| `*xémnaz` | nom cluster | `hemn` | `hefn` | **no** |
| `*xémnas` | gen cluster | `hemnes` | `hefnes` | **no** |
| `*xémnum` | dat.pl cluster | `hemnum` | `hefnum` | **no** |
| `*xémenaz` | nom vowel | **`hefen`** (proxy) | `hemen` | yes (via proxy only) |
| `*xémonų` | acc vowel (current) | **`heofon`** (proxy) | `heomon` | yes (via proxy only) |
| `*xéfon` | pre-labialized | **`heofon`** | **`heofon`** | yes (real back mutation) |

Corpus (adjacent-mn + `stem *stámniz`, heaven unchanged/exception): **380 / 372
/ 8 / 0**, mismatch {buck, fire, fowl, heaven, rust, tap, wolf, wool}. With the
`*héfon` alternative for heaven: **380 / 373 / 7 / 0**. Multiplicity 1
throughout; no ambiguity; no collateral beyond heaven and stem.

---

## 12. Production integrity

`germanic.txt` unchanged (sha256 `10c61d2c…`); `germanic-aligned-final.tsv`,
baselines, manifests, book/index, rows 2068 and 2216 unchanged. All shadow work
ran in the container's ephemeral `/root`. `git diff --check` clean.

## Bibliography (exact locators)

- Kroonen 2013, *EDPG* p. 220 (`kroonen_etymological_dictionary_pgmc.vision.txt:12428`);
  2011, *The PGmc n-stems* (`kroonen_2011_n_stems.vision.txt:1770`).
- Fulk 2018, *Comparative Grammar* §6.11 p. 121 (`:7365`); OS `heban/hebenes`
  (`:5946`); n-stem `*-en-/-on-` (`:8239, :10212, :10263`).
- Hogg 1992, *Grammar of OE I: Phonology*: back mutation `*hefon > heofon`
  (`hogg_vol1.txt:5678-5694`); Nhb/Mer Lord's Prayer `heofnum/heofnas/heofenum`
  (`:20445`); unstressed reduction to /e/ (`:7617`); syncope (`:5908-5950`).
- Campbell 1959, *OEG* §210 (`campbell_old_english_grammar.txt:6318`), §381
  (`:10332`).
- Cædmon's Hymn, Rome ms study: `hefun`/`hefen`/Moore `heben`
  (`caedmons_hymn_rome_ms_vitt_em_1452.vision.txt:627, :769, :775`).
- Clark Hall 1960: `hefen` II = `heofon` (`clark_hall…vision.txt:21259`).
- Bosworth–Toller: `heofnes` (`:5170`), `heofne` (`:67495`), `heofnum` (`:6389`).
- Polomé 1967 pp. 818–819 (`polome_1967_reflexes_ie_ms.txt:867`); Kluge–Seebold
  s.v. *Himmel* (`kluge_seebold…:42427`).

---

# 13. Addendum (2026-08-13): classification audit, Ringe–Taylor `*hebun`, and the two-analogy span

This addendum answers four loose ends left by §§1–12: (a) how CAPR's derivation
classes *actually* work; (b) what Ringe–Taylor's northern-WGmc **`*hebun`**
contributes, decomposing **`b`** vs **`u`**; (c) whether the "two analogies
bracketing a regular span" narrative survives; and (d) the resulting
classification. It **revises** the executive conclusion (§1) and the primary
recommendation (§10). No production file is touched.

## 13.1 CAPR classification system — what the categories actually permit

Inspected live: the book Parts and every current entry.

- **Part VI "Known but unmodelled developments"** (`known_unmodelled`,
  `lexical_volume_alpha_01.md:10829`): *"The historical development is
  sufficiently supported by comparative and philological evidence, but the
  current transducer cascade does not yet implement the phonological or
  morphological process required to derive the target."* Entries: **fire**
  (2013), **tap** (2240), **stem** (2216).
- **Part VII "Unexplained or deliberately unmodelled exceptions"**
  (`unexplained_unmodelled`, `:11140`): *"No sufficiently supported account yet
  reconciles the regular output with the Old English form."* Entries: **buck**
  (1973), **fowl** (2030), **rust** (2162), **wolf** (2298), **wool** (2300).

**Decisive point:** `known_unmodelled` ≠ "historically unexplained." It is the
tier for rows whose history *is* understood but whose deriving process the FST
does not implement. `unexplained_unmodelled` is the "we don't know" tier.
*heaven*, whose history this dossier reconstructs in detail, therefore belongs —
if unmodelled at all — to the **`known_unmodelled`** tier, never to
`unexplained_unmodelled`.

**Is there a precedent for *two* non-phonological interventions (early + late)
in one `known_unmodelled` row?** No. Surveying the three entries:

| entry | regular FST output | attested target | intervention(s) | where |
| :-- | :-- | :-- | :-- | :-- |
| **fire** | `fȳr` (regular, from selected oblique `*fūri`) | `fȳre` | one **late** analogy (`-e` restoration) + a paradigm-cell *selection* of the input | input selection + late |
| **tap** | `tappa` | `tæppa` | one analogy (`æ` levelled from j-stems) | surface |
| **stem** | `stamn` | `stefn` | none analogical — a **sound change** (`mn>fn`) not yet in the cascade | the rule itself |

So the closest precedent, **fire**, has a clean regular span **plus a single
late analogy** (and an input cell-selection). **No current `known_unmodelled`
entry brackets a regular span between an *early* and a *late* analogy.** If
heaven were classified `known_unmodelled`, it would be a **new but legitimate
sub-type** of that tier (double-analogy bracketing), not a category error.

**How the single-class system bears on heaven.** CAPR assigns **one** class per
row and models **one** cell's input→output. It has `early_analogy` (Part III:
analogy separates the *input* from citation before OE changes) and `late_analogy`
(Part IV: the OE form continues a later paradigm cell / remodelling), but **no
combined class**. Two honest readings follow, developed in §13.5.

## 13.2 Ringe–Taylor `*hebun`: decomposing `b` and `u`

Source used: `docs/references/ringe_taylor_linguistic_history_vol2.txt` (Ringe &
Taylor 2014, *The Development of Old English* = *A Linguistic History of English*
vol. 2). Three loci, all found and read:

1. **p. 272** (`:15697`), in the list of **non-syncopating heavy/‏light stems**
   (beside `*sikur -> sicor`, `*habukaz -> hafoc/hafoce`, `*stabulaz ->
   stapol/stapolas`): *"northern WGmc `*hebun`° 'sky, heaven', gen. `*hebunas`,
   etc. (OS heban, hebanas, etc.) > OE heofon, heofones."* — i.e. R&T derive
   `heofon, heofones` **regularly**, with the medial vowel **retained** (no early
   syncope). Footnote 20 (`:15711`): *"There is some sort of relationship between
   this word and PWGmc `*himil` (OF, OS, OHG himil), and between both and PGmc
   `*himinaz` (Goth. himins, ON himinn), but the details do not seem to be
   recoverable."*
2. **p. 324** (`:18570`), in the section on **WS back umlaut of `e`** (*"it
   occurred only when the following vowel was u and the intervening consonant was
   l, r, or a labial"*, `:18556`), listed **directly beside *seven***:
   `*sebun > WS/North. seofon, Merc. seofen`; then *"northern WGmc `*hebun` 'sky,
   heaven' (OS heban) > WS, North. OE heofon, Merc. heofen."*
3. **p. 387** (`:21859`): heaven cited as a **non-alternating** stem, *"heofon
   'sky, heaven', gen. sg. heofones < `*hebun-`."*

**What R&T regard as unrecoverable.** *Not* the internal `*hebun -> heofon`
derivation — that is one of their **regular** back-umlaut examples (locus 2),
strictly parallel to `*sebun -> seofon`. What is "not recoverable" (fn 20) is the
**morphological relationship among the three stem-shapes**: the labial `n`-stem
`*hebun`, the `l`-stem `*himil`, and the `m`-stem `*himinaz` (Goth. `himins`, ON
`himinn`). `*hebun` is thus, in R&T, a **northern-WGmc lexeme-level stem**
(nom. `*hebun`, gen. `*hebunas`), *not* an isolated case-cell, and its OE
outcome is regular.

Decomposition:

- **The `b`.** R&T **posit** it (from OS `heban`) but do **not** derive it; it is
  part of the "unrecoverable" relationship. **Our paradigm analysis explains it:**
  regular `mn > βn/bn` in the inherited oblique cluster (ON `himinn : hifni`
  preserves exactly this alternation; OS `heban/hebenes` generalizes it), then
  **early analogical levelling** of that labial into the vowel-bearing stem. So
  CAPR's account **explains the consonantism of R&T's `*hebun`** rather than
  accepting it as a black box — a genuine, if partial, advance on fn 20.
- **The `u`.** This is the separate, harder problem, and it must not be assumed
  merely because a back vowel is convenient for back umlaut. `*hebun` has the
  `n`-stem **suffixal vowel** `*-un-` (gen. `*-un-as`), the *same* element as in
  `*sebun` 'seven'; it is what **triggers** WS back umlaut (locus 2). Its *exact*
  morphological source — why the `-un-`/`-an-` grade generalized here whereas the
  cognate `m`-stem shows `-in-` (`himinn`, `himins`) — is precisely the
  suffix-ablaut / stem-relationship question R&T call unrecoverable. Kroonen's
  split `*hemina-` (i-vocalism → `himinn`, `himins`) vs `*hemna-`/oblique
  (→ OE/OS) frames the same uncertainty. So the **`u` remains partly opaque**:
  identifiable as the `n`-stem suffix vowel (parallel to *seven*), but its
  selected ablaut grade is not fully recoverable.

**Adjudication of §5's four options (task Part 5): B + D, shading to C.**
`*hebun` is best read as a **useful shorthand (B)** for the already-remodelled
vowel-bearing `b`-stem, whose **`b` our account explains** and whose **`u` is
partly opaque (D)**. It is **not a necessary intermediate (¬A)**: CAPR can derive
the OE forms directly from the remodelled stem without erecting `*hebun` as a
distinct node **(C)**. Net result — we explain **part** (the consonantism) of the
relationship R&T deemed unrecoverable, without claiming to have solved the `u`.

## 13.3 The two analogies — tested, and sharpened

The narrative survives falsification, but R&T force two refinements.

**Early analogy (labial levelling) — confirmed.** The `f`/`b`/`β` is regular only
in the oblique `-mn-` cluster; its presence in the vowel-bearing stem is
analogical (ON does **not** level: `himinn` keeps `m`; OE/OS do: `heofon`,
`heban`). This is the analogy that builds `*hebun-`. It explains R&T's `b`.

**Regular middle (back mutation) — sharpened to WS back umlaut of `e` before
`u`.** R&T (locus 2) make `*hebun -> heofon` a *textbook* WS/North. back-umlaut
example, conditioned by the **medial `u`** across the **labial**, and strictly
**parallel to *seven*** `*sebun -> seofon`. The labial is already present when
this fires. On heavy/non-alternating stems the medial vowel is **retained**
(locus 1, 3), so gen. `heofones`/dat.pl `heofonum` are **also regular** (back
umlaut applies; no early syncope).

**Late analogy — reframed as levelling + *late* syncope (the "before-syncope"
chronology wins).** §5e/§8.7 worried that `heofnum`'s `eo` cannot come from a
syncopated `*hemnum`. R&T resolve this cleanly: because `*hebun-` is
**non-alternating**, the regular obliques are `heofones`/`heofonum` (medial vowel
retained, `eo` already installed by back umlaut); the syncopated `heofnes`/
`heofnum` then arise by **later optional syncope** of *those* forms
(`heofonum > heofnum`). So the attested `eo` **is** regular (present **before**
syncope) — exactly the "levelling/back-umlaut before syncope" chronology the task
(Part 2) asked us to prefer over a fictitious back mutation across `-fn-`. The
residual genuinely-*analogical* late event is the **flattening of the
`he-`(front) : `heo-`(back) suffix-vowel alternation** across the paradigm (Hogg:
in WS such alternations "were normally levelled out"), which does **not** disturb
the modelled nominative `heofon`.

### Chronological schematic

```text
old amphikinetic mn-stem paradigm  (*hemō : gen *hemn-os …; ON himinn : hifni)
        |
        | REGULAR  mn > βn/bn  in the inherited cluster-bearing obliques
        v
paradigm with m : f/b alternation  (ON himinn : hifni type)
        |
        | EARLY ANALOGY: level the f/b labial into the vowel-bearing stem
        |                (+ generalize the n-stem suffix vowel *-un-)
        v
northern WGmc *hebun- / *hefun-   ============  Ringe–Taylor *hebun, gen *hebunas
   (b explained here; u = n-stem suffix vowel, exact grade partly opaque)
        |
        | REGULAR  WS back umlaut of e before medial u across the labial
        |          (exactly parallel to *sebun 'seven' > seofon)
        v
heofon (WS/North.) : Merc. heofen   +  regular obliques heofones/heofonum
        |
        | LATE: level residual he-/heo- alternation  +  optional late syncope
        |       (heofonum > heofnum; eo already present pre-syncope)
        v
attested  heofon : heofnes : heofnum : Merc. heofen : early Nhb hefun/hefen/heben
```

`*hebun` sits **on** the diagram (the remodelled `b`-stem node), not beside it as
a rival: our chain reaches the *same* node and additionally motivates its `b`.

## 13.4 New shadow probe (2026-08-13): does the *real* cascade reach `heofon`?

Method as §11 (ephemeral `/root`; production untouched). Two builds: **production**
(with the `mV…n` proxy) and **shadow** (SC022 = adjacent-`mn` only,
`{*m} -> {*β} || EnglishStarVocalic _ {*n}`). Inputs fed to `old_english.bin` via
`flookup -i` (normalized: strip `*`; `þ→θ`).

| input (CAPR notation) | reading | production (proxy) | **shadow (adjacent-mn, NO proxy)** | attested? |
| :-- | :-- | :-- | :-- | :-- |
| `*xéfon` | Hogg `*hefon` | `heofon` | **`heofon`** | yes (nom) |
| `*xéfun` | *seven*-parallel, medial u | `heofon` | **`heofon`** | yes (nom) |
| `*xébun` | **R&T `*hebun`** (b→β→f) | `heofon` | **`heofon`** | yes (nom) |
| `*xémun` | m, medial u (non-adjacent) | `heofon` (via proxy) | `heomon` | no |
| `*xémon` | m, medial o | `heofon` (via proxy) | `heomon` | no |
| `*xémonų` | **current row-2068 PROTOFORM** | `heofon` (via proxy) | `heomon` | no |
| `*xémenaz` | current row-2068 PROTO | `hefen` (via proxy) | `hemen` | no |
| `*xémnaz` | adjacent-mn nom cluster | `hemn` | `hefn` | no |
| `*xémnas` | adjacent-mn gen cluster | `hemnes` | `hefnes` | no |
| `*xémnum` | adjacent-mn dat.pl cluster | `hemnum` | `hefnum` | no |

**Reading.** (i) A **labial-bearing** input (`*xéfon` / `*xéfun` / **`*xébun`**)
derives attested `heofon` under the **real** cascade with **no proxy** — via
regular `PGmc B Allophony` (`b→β`) + `OE Back Mutation`, identical to the
production-`regular` derivation *seven* `*sébun -> *séβon -> séoβon -> seofon`.
(ii) An `m`-bearing input needs the **proxy** to reach `heofon`; without it,
`*xémonų` (current PROTOFORM) gives `heomon`. (iii) A genuine **adjacent-mn**
cluster input gives only **unattested** `hefn/hefnes/hefnum`. Multiplicity 1
throughout.

This is the crux: the **only** thing the proxy buys is fabricating the labial
from `m`. Once the labial is (correctly, analogically) in the input — as it is in
R&T's `*hebun` — the span to `heofon` is **ordinary, real OE phonology**.

## 13.5 Reassessed classification and final recommendation

Three levels, kept distinct per task Part 3 / Part 8:

1. **Lexeme history:** inherited mn-stem → *early* labial levelling → regular WS
   back umlaut → *late* alternation-levelling + syncope → attested paradigm
   (§13.3). Two analogies, real regular middle.
2. **Regular sub-spans:** (a) the **`*hebun -> heofon`** nominative span is real,
   regular, shadow-verified, *seven*-parallel; (b) the inherited-oblique line
   `*hemnum -> …-> *hefnum` is regular **but its endpoint is unattested** (attested
   `heofnum` descends from the vowel line, §13.3). Span (a) is the usable one.
2b. **Single CAPR row (the actual decision).** CAPR models **one** cell. For the
   **nominative**, the modelled derivation `*hebun -> heofon` contains **exactly
   one** intervention — the *early* labial levelling, encoded in the input — and
   is therefore a clean **`early_analogy`** row, structurally identical to
   `bottom` (`*búttmaz -> botm`). The *late* levelling/syncope belongs to **other
   cells** the row does not model (just as `fire` models only `fȳr` and lets the
   paradigm's `-e` restoration lie outside). The "two analogies" are a property of
   the **lexeme's paradigm**, not of the modelled nominative derivation.

**Recommendation.** Two honest, non-contradictory options; the project chooses:

- **PRIMARY — `early_analogy`, `*hebun -> heofon`.** PROTOFORM `*xébun`
  (≈ R&T `*hebun`; `*xéfun`/`*xéfon` are equivalent inputs), COUNTERPART `heofon`
  [attested WS/North. nom], DERIVATION_CLASS `early_analogy`. Trace (real cascade,
  no proxy; exactly the *seven* path): `*xébun -> [Med Unstressed U Lowering]
  *xébon -> [B Allophony] *xéβon -> [Back Mutation] *xéoβon -> heofon`.
  **Analogy boundary:** the mn-cluster labial levelling (and the
  suffix-vowel generalization) are pre-OE, *in the input*; only regular OE
  phonology is modelled. **Confidence:** high — `*hebun` is R&T's own
  reconstruction, the span is regular and *seven*-parallel, and the task (Part 2)
  explicitly licenses an analogical labial in the input. This **supersedes** the
  §10 `*héfon` alternative (same output, but `*hebun` is better motivated: real
  reconstruction, the `u` is the genuine back-umlaut trigger, `b→β→f` is regular).
- **FALLBACK — `known_unmodelled`.** If the project prefers not to compress the
  labial + suffix-vowel remodelling into `*hebun`, keep heaven as an explicit
  **understood** exception alongside fire/tap/stem. This is the **correct tier**
  (§13.1), *never* `unexplained_unmodelled`. Reader-facing wording:

  > *heaven* is `known_unmodelled` **not** because its development is inexplicable,
  > but because its Old English history brackets a real regular sound change (WS
  > back umlaut, `*hebun > heofon`, exactly as *seven* `*sebun > seofon`) between
  > an **earlier** analogy (levelling the oblique `-mn-` labial into the
  > vowel-bearing stem) and a **later** one (levelling the residual suffix-vowel
  > alternation, with optional syncope). CAPR assigns one derivation class per row
  > and does not model those analogical operations in the deterministic cascade.

- **REJECTED (unchanged):** the `mV…n` proxy *as a sound change*; retargeting to
  unattested `hefn`/`hefnes`/`hefnum`; any score-driven choice.

**Corpus consequence (shadow, unchanged from §11):** with SC022 = adjacent-`mn`
and `stem *stámniz -> stefn`, either heaven option gives a clean total — the
`early_analogy` primary matches `heofon` → **380 / 373 / 7 / 0**; the
`known_unmodelled` fallback lists heaven as the 8th mismatch → **380 / 372 / 8 /
0**. No collateral beyond heaven and stem.

## 13.6 Consequences (for the eventual implementation task — NOT executed here)

- **SC022:** the cell-to-cell evidence **supports retiring the `mV…n` proxy** and
  making SC022 literal adjacent `mn > βn`. Heaven never needed a *sound change*
  for its labial (it needs the *early analogy*, encoded by input choice or by the
  `known_unmodelled` label); the proxy's sole beneficiary was this one row.
- **Row 2068 (heaven):** implement as **`early_analogy`, PROTOFORM `*xébun`,
  COUNTERPART `heofon`** (primary), or **`known_unmodelled`** (fallback). Either
  removes the proxy dependency.
- **Row 2216 (stem):** `*stámniz -> stefn` (mult 1) remains independently
  supported under literal adjacent `mn > βn`; unaffected.

**Integrity (re-verified for this addendum):** all shadow builds ran in the
container's ephemeral `/root`; `germanic.txt` (`10c61d2c…`),
`germanic-aligned-final.tsv`, baselines, manifests, book/index, and rows
2068/2216 are untouched. This addendum is the only change.

### Bibliography additions

- Ringe & Taylor 2014, *A Linguistic History of English* vol. 2 (*The Development
  of Old English*): northern-WGmc `*hebun`, gen. `*hebunas` > OE heofon/heofones
  pp. 272 (`ringe_taylor_linguistic_history_vol2.txt:15697`, fn 20 `:15711`), 324
  (`:18570`; WS back umlaut of `e` before `u`, `:18556`; *seven* `*sebun >
  seofon` `:18565`), 387 (`:21859`).
- *seven* in CAPR: row 2174, PROTOFORM `*sébun`, `regular` match `seofon`
  (`germanic-aligned-final.tsv`; trace
  `debug_snapshots/oe_derivation_class_trace_report.compact.md:4624`).
- CAPR classes: Part VI `known_unmodelled` (`lexical_volume_alpha_01.md:10829`),
  Part VII `unexplained_unmodelled` (`:11140`), Part III `early_analogy`
  (`:4964`), Part IV `late_analogy` (`:8060`); `manifest_known_unmodelled.tsv`.

---

# 14. How far back can the regular history be recovered? Competing Lautgesetzlich spans

Row 2068 is treated here **provisionally as `known_unmodelled`** (§13.1). This
section does **not** try to rescue it as a match. Its purpose is the opposite of
§13's nominative focus: to find the **deepest and longest** stretches of the
history that proceed by *regular* sound change — and, above all, to test whether
the labial `b/f` can be **derived within a single paradigm cell** rather than
pre-supplied in the input. All experiments are shadow-only (adjacent-`mn` SC022,
ephemeral `/root`); production is untouched.

## 14.1 Where adjacent `mn` actually occurs in the paradigm

Kroonen (EDPG p. 220, `:12428`) reconstructs the remodelled PGmc paradigm on the
genitive: nom. **`*hemō`**, gen. **`*hemnaz`**, dat. **`*hemeni`**, continuing
PIE `*h₂ék-mōn`, gen. `*h₂k-mn-ós`, loc. `*h₂k-mén-i` (Lühr 2000: 79). Two stems
then generalize out of it: vowel-bearing **`*hemina-`** (→ Go. `himins`, ON
`himinn`) and cluster **`*hemna-`** (→ OE `heofon`, OS `heban`). The decisive
morphological fact:

| cell | PGmc | suffix grade | adjacent `mn`? | feeds the labial? |
| :-- | :-- | :-- | :-: | :-: |
| nom.sg | `*hemō` | — (no `n` cluster) | **no** | no |
| **gen.sg** | **`*hemnaz`** | **zero** (`*-n-`) | **YES** | **yes** |
| dat.sg | `*hemeni` | **full** (`*-en-`) | **no** (`hem-en-i`) | no |
| loc.sg (PIE) | `*h₂k-mén-i` | full (`*-én-`) | no | no |
| dat.pl (zero-grade) | `*hemn-um` | zero | **YES** | **yes** |
| gen.pl (zero-grade) | `*hemn-ō(n)` | zero | **YES** | **yes** |
| stem `*hemna-` | (generalized gen.) | zero | **YES** | **yes** |
| stem `*hemina-` | (generalized full) | full | no | no |

So the labial is fed **specifically by the zero-grade (genitive/oblique) cells**,
not by the nominative or the full-grade dative singular. This is the exact
morphological locus we must follow.

## 14.2 Three exact shadow traces (adjacent-`mn` cascade, mult 1 each)

Walked step-by-step through the sandbox's cumulative intermediate transducers
(`old_english_sandbox_after_*.bin`); only the steps that change the string are
shown.

**(a) Genitive cluster `*hemnas` (deep zero-grade) — the labial is derived:**
```
proto_input                     *x*e*m*n*a*s
pnwgmc_mn_dissimilation         *x*e*β*n*a*s   ← mn > βn  (SC022, REGULAR)
eaf_brightening                 *x*e*β*n*æ*s
oe_velar_fricative_palatal.     *ç*e*β*n*æ*s
oe_unstressed_ae_merger         *ç*e*β*n*e*s
old_english_orthography         h*e*β*n*e*s
old_english_remove_stars        hefnes          (β → f)
```

**(b) Dative-sg cluster `*hemni` (zero-grade, i-ending) — labial + i-umlaut:**
```
proto_input                     *x*e*m*n*i
pnwgmc_mn_dissimilation         *x*e*β*n*i     ← mn > βn  (SC022, REGULAR)
oe_velar_fricative_palatal.     *ç*e*β*n*i
oe_i_umlaut                     *ç*i*β*n*i     ← i-umlaut e > i  (from the ending)
oe_high_vowel_apocope           *ç*i*β*n
old_english_orthography         h*i*β*n
old_english_remove_stars        hifn
```
The outcome `hifn` converges in surface shape with **ON `hifni`** (dat.sg), the
attested North-Germanic form that carries the oblique labial from a syncopated
`-mn-` cluster — independent evidence that this cluster labialization is real.
(The two derivations are not claimed to be step-identical — ON `hifni` reaches
its root `i` through the `*hemina-` stem vowel + medial syncope, the OE probe
through i-umlaut — but both attest the same oblique `-mn- > -fn-`.)

**(c) Nominative remodelled stem `*hebun` (R&T) — the labial is pre-supplied:**
```
proto_input                     *x*e*b*u*n
oe_med_unstressed_u_lowering    *x*e*b*o*n     ← u > o (medial)
oe_velar_fricative_palatal.     *ç*e*b*o*n
pgmc_b_allophony                *ç*e*β*o*n     ← b > β
oe_back_mutation                *ç*eo*β*o*n    ← back mutation e > eo
old_english_orthography         h*eo*β*o*n
old_english_remove_stars        heofon
```
Here **no rule creates the labial** — it enters with the input `b`. Only vocalic
and surface changes are modelled.

Contrast in one line: cluster cells reach `hefnes`/`hifn`/`hefnum` **through a
regular `mn > β` step**; the vowel-line `*hebun/*hebunas` reaches attested
`heofon`/`heofones` **with the labial already present** and no such step.

## 14.3 The genitive `???` resolved: the `b` is regular, the `u` is secondary

The addendum (§13.2) asked whether R&T's gen. `*hebunas` can be reached from an
inherited cluster genitive. It can, in two regular consonantal moves plus one
**non-consonantal** interruption:

```
PIE  *h₂k-mn-ós            (gen., zero-grade suffix; secure — Kroonen/Lühr)
  →  PGmc *hemnaz          (remodelled on the gen.; adjacent mn)
  →  *heβnaz / *hebn-      REGULAR  mn > βn/bn   (SC022; trace §14.2a)
  →  *hebun-              ►►► medial vowel RESTORED/generalised  ◄◄◄  (not regular)
  →  R&T *hebunas
  →  heofones             REGULAR OE (u-lowering, back umlaut; R&T p. 272/387)
```

**The `b` is regular** within the genitive/oblique lineage: it is the ordinary
reflex of the inherited zero-grade cluster `-mn-`. This is a real gain over R&T,
who **posit** the `b` (from OS `heban`) without deriving it.

**The `u` is secondary, and demonstrably so.** The medial vowel of `heofon`
cannot be OE's regular parasite/​svarabhakti vowel in `-fn-` (the type
`efn ~ efen`, `hræfn ~ hræfen`), because that vowel is **late and optional** and
would post-date back mutation — yet `heofon`'s `eo` **requires** a medial vowel
to be present *before* back umlaut (§13.3, R&T p. 324). The vowel must therefore
be the **earlier restored/generalised suffix vowel**, installed *before* the OE
vocalic changes. That the vowel differs by dialect — OE `u/o` (`heofon`) vs OS
`a` (`heban`) — confirms it is a secondary resolution of the `*hebn-` cluster
stem, not an inherited constant. Its exact ablaut source (why `-u-` here, against
the `-i-` of the `*hemina-` stem, `himinn`/`himins`) is **not recoverable** — the
residue R&T flagged.

**Verdict.** The genitive is a *deeper* line than the nominative **for the
consonant** (it derives the `b`), but it offers **no advantage for reaching an
attested OE form**: exactly one non-regular event (the medial-vowel restoration)
sits between the regular cluster labialization and the attested `heofones`, and
it is the same event whichever oblique we choose.

## 14.4 Genuine ancestor, counterfactual, or dialectal? (per cell)

Applying the task's A/B/C test to each cluster output:

- **A (genuine pre-analogical ancestor):** holds for **ON**, not OE. ON
  `himinn : hifni` preserves the cluster line to an **attested** North-Germanic
  form. The `mn > fn` change has a real attested endpoint — in Norse.
- **B (counterfactual for OE):** the bare cluster outputs `hefnes`/`hefnum`/`hefn`
  are **not** the ancestors of attested OE `heofnes`/`heofnum`/`heofon`. The
  attested OE obliques carry `eo` (regular back umlaut on a *retained/restored*
  medial vowel, then optional late syncope: `heofonum > heofnum`, §13.3). A
  form that had stayed a bare `-fn-` cluster could not acquire that `eo`. So for
  OE, `*hemnum → hefnum` is what the **unrestructured** cell *would* have given —
  a counterfactual, not a derivation of the attested word.
- **C (dialectally split):** confirmed. North Germanic kept the cluster line
  longer (ON `hifni`); OE and OS generalised the labial into a **re-vowelled**
  stem (`*hebun-`, `*heban-`) before their attested paradigms. One West-Saxon
  chronology must **not** be imposed on ON.

**Consequence:** the labial of attested OE `heofon` **does** descend from the
regular cluster labialization (via the generalised `*hemna-/*hebn-` stem — the
*consonant's* ancestry is genuine, interpretation A for the segment); but the
**word-forms** with a bare cluster are counterfactual for OE (B), the cluster
line surviving attested only in Norse (C).

## 14.5 The longest-Lautgesetzlich-span table

Real forms; "regular endpoint" = output of the adjacent-`mn` cascade;
"first non-regular event" = where analogy/restructuring first becomes necessary
to reach the *attested* target of that cell.

| # | candidate line | start cell (chronological depth) | regular developments | regular endpoint | endpoint attested? | first non-regular event | actual ancestor of an attested form? |
| :- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| 1 | **gen.sg cluster** | PGmc `*hemnaz` < PIE `*h₂k-mn-ós` — **deepest** | **mn > βn**, brightening, palatal., æ-merger | `hefnes` | **no** (OE has `heofnes`) | medial-vowel restoration | **labial: yes**; OE word-form: no (→ B); cf. ON |
| 2 | **dat.sg cluster** (i-ending) | PGmc `*hemni` (zero-grade) — deep | **mn > βn**, **i-umlaut**, apocope | `hifn` | via **ON `hifni`** (not OE) | vowel restoration (for OE) | ON: **yes** (A/C); OE: no |
| 3 | **dat.pl cluster** | PGmc `*hemnum` < PIE zero-grade — deep | **mn > βn**, … | `hefnum` | **no** (OE has `heofnum`) | vowel restoration | labial: yes; OE word-form: no (→ B) |
| 4 | **gen.pl / a-stem cluster** | PGmc `*hemnō(n)` / `*hemnaz` — deep | **mn > βn**, ending loss | `hefn` | **no** | vowel restoration | labial: yes; OE word-form: no |
| 5 | **nom. remodelled stem** | northern WGmc `*hebun` — **shallow** | u-lowering, b-allophony, back mutation | `heofon` | **yes** (WS/North. nom) | *before* the input (labial + vowel levelled in) | **yes** (OE nom) |
| 6 | **gen.sg remodelled stem** | northern WGmc `*hebunas` (R&T) — shallow | u-lowering, b-allophony, back umlaut | `heofones` | **yes** (OE gen) | *before* the input | **yes** (OE gen) |
| 7 | **dat.pl remodelled stem** | northern WGmc `*hebunum` — shallow | back umlaut, **late syncope** | `heofonum > heofnum` | **yes** (OE dat.pl) | *before* the input | **yes** (OE dat.pl) |

Two independent measures, deliberately kept apart (task Part 6):

- **Chronological depth of the start:** lines 1–4 (cluster) are **deep** (secure
  to PIE zero-grade); lines 5–7 (remodelled `*hebun-`) are **shallow** (northern
  WGmc, post-levelling).
- **Regular-span length that reaches an *attested* endpoint:** lines 5–7 reach an
  attested OE form but derive **no** labial; lines 1–4 derive the labial by a
  long regular run but their **attested** endpoint is Norse (line 2) or nothing
  in OE (lines 1, 3, 4).

## 14.6 Ranking under CAPR's "longest defensible span" — and why they don't coincide

- **Deepest derivation of the labial itself:** the **genitive/oblique cluster**
  (lines 1–4). Here `mn > βn` is a real, regular, mult-1 step from a securely
  reconstructed PIE zero-grade cell. This is the historically most interesting
  span and the answer to "how far back can the labial be recovered": **to the
  inherited genitive `*h₂k-mn-ós`.**
- **Longest regular run to an *attested* endpoint — but in Norse:** the **dat.sg
  cluster** `*hemni → hifni` (line 2), whose attested witness is ON `hifni`.
- **Longest regular run to an attested *Old English* endpoint:** the **remodelled
  vowel line** `*hebun(as/um) → heofon(es/um)` (lines 5–7) — but it presupposes
  the labial and is *shallow*.

**They do not coincide, and that non-coincidence is the whole result.** No single
line is simultaneously (i) deep, (ii) labial-deriving, and (iii) terminating in
an attested **Old English** form: the one non-regular event — restoration of the
medial vowel into the labialised cluster stem — always intervenes between the
regular labialization and the attested OE paradigm. CAPR must therefore **not**
prefer a cluster oblique merely because it derives the `f` (its OE endpoint is
counterfactual, §14.4 B), nor claim the shallow nominative captures the labial's
history (it does not).

## 14.7 What we now explain of R&T's `*himinaz ~ *himil ~ *hebun`

- **The `b`: recovered further than R&T state.** Their northern-WGmc `*hebun` is
  posited from OS `heban`; we derive its labial regularly from the inherited
  oblique cluster `*hemn-` (`mn > βn/bn`, trace §14.2a) generalised out of the
  genitive-based `*hemna-` stem, with ON `himinn : hifni` and OS `heban/hebenes`
  as comparative anchors. The **consonantism** R&T left inside their
  "not recoverable" verdict is, in fact, largely recoverable.
- **The `u`: still opaque, and now precisely so.** It is the secondary resolution
  vowel of the `*hebn-` cluster stem (§14.3), the genuine trigger of WS back
  umlaut (parallel to *seven* `*sebun`), but its selected ablaut grade — `-u-`
  here vs `-i-` in the cognate `*hemina-` stem — is not derivable. This is the
  irreducible residue.
- **Net:** we convert R&T's single opaque `*hebun` into **`b` (explained) + `u`
  (residual)** — a real partial solution of a relationship they called
  unrecoverable, without overclaiming the vowel.

## 14.8 Consequence for the row and the executive conclusion

Nothing here makes row 2068 a clean single-path match, and it should **remain
`known_unmodelled`** for this pass. But the classification now rests on a sharp,
positive finding rather than a shrug:

> *heaven* is `known_unmodelled` because its regular history is **split across
> cells**: the labial `f/b` is regularly derivable, and *deeply* — back to the
> inherited genitive `*h₂k-mn-ós` (PGmc `*hemnaz`, `mn > βn`) — but only in the
> **oblique cluster** cells, whose clean outputs (`hefnes`, `hifn`, `hefnum`)
> are attested in Norse (ON `hifni`), **not** in Old English; while the
> **attested** OE forms (`heofon`, `heofones`, `heofnum`) descend from a
> **re-vowelled** `*hebun-` stem in which the labial is already present and only
> ordinary Old English changes (back umlaut, late syncope) apply. A single
> non-regular event — restoration of the medial vowel into the labialised
> cluster stem — separates the two, and no one CAPR input-to-attested-OE-target
> path spans it. CAPR can thus **describe** more regular history (the labial to
> PIE depth) than it can **model** in one deterministic derivation.

### Answers to the Part-10 questions

1. **Deepest regular source of the labial:** the inherited **genitive** cluster,
   PIE `*h₂k-mn-ós` → PGmc `*hemnaz` → regular `mn > βn` (§14.2a).
2. **Longest credible regular run:** for the labial, the oblique cluster lines
   (1–4); for an attested endpoint, the dat.sg `*hemni → hifni` (attested in ON)
   and the vowel-line `*hebun → heofon` (attested in OE).
3. **Actual ancestry vs counterfactual:** the cluster word-forms are
   **counterfactual for OE** (B) and **genuine for ON** (A/C); the *consonant* of
   OE `heofon` is nonetheless genuine cluster ancestry.
4. **Best actual path to an attested OE form:** the remodelled vowel line
   `*hebun(as/um) → heofon(es/um)` (lines 5–7).
5. **How much of R&T's relationship we explain:** the **`b`** (regular oblique
   `mn`), not the **`u`**.
6. **What remains unrecoverable:** the ablaut source of the medial **`u`** and
   the precise route/date of its restoration.
7. **Why the row stays `known_unmodelled`:** the labial-deriving line and the
   attested-OE line are **different cells**, joined only by a non-regular
   vowel restoration; one deterministic CAPR path cannot cover both.

### Shadow battery (this section; adjacent-`mn` SC022, production untouched)

| input | reading | output | mult | attested? | same-cell regular ancestry of the labial? |
| :-- | :-- | :-- | :-: | :-- | :-- |
| `*xemnas` | gen.sg cluster | `hefnes` | 1 | no (OE `heofnes`) | **yes** (mn>β) |
| `*xemni` | dat.sg cluster (i-end.) | `hifn` | 1 | via ON `hifni` | **yes** (mn>β + i-umlaut) |
| `*xemnum` | dat.pl cluster | `hefnum` | 1 | no (OE `heofnum`) | **yes** |
| `*xemnō` | gen.pl cluster | `hefn` | 1 | no | **yes** |
| `*xemnaz` | `*hemna-` a-stem nom | `hefn` | 1 | no (OE `heofon`) | **yes** |
| `*xebnas` | b-cluster gen (vowel not yet restored) | `hefnes` | 1 | no | (labial present) |
| `*xebun` | remodelled nom (R&T) | `heofon` | 1 | **yes** | no (labial pre-supplied) |
| `*xebunaz` | remodelled a-stem nom | `heofon` | 1 | **yes** | no |
| `*xefun` | remodelled nom (f) | `heofon` | 1 | **yes** | no |
| `*xemonų` | **current row-2068 PROTOFORM** | `heomon` | 1 | no | no (needs the proxy) |

(Vowel-line genitives `*xebunas`/`*xefones` return `+?`: the transducer's PGmc
**input** alphabet does not license those trisyllabic ending-shapes; R&T supply
the regular `*hebunas > heofones` documentarily, and `*xebun → heofon` confirms
the mechanism.)

### Bibliography additions (this section)

- Kroonen 2013, *EDPG* p. 220: paradigm nom. `*hemō`, gen. `*hemnaz`, dat.
  `*hemeni`; stems `*hemina- ~ *hemna-`; PIE `*h₂ék-mōn`, gen. `*h₂k-mn-ós`
  (`kroonen_etymological_dictionary_pgmc.vision.txt:12428`); Lühr 2000: 79.
- ON `himinn : hifni` (oblique cluster labial); OS `heban / hebenes`
  (Fulk `:5946`); OE parasite vowel `efn ~ efen` type (Campbell §363–§364;
  Hogg §6.36 syncope/parasiting) as the *late* svarabhakti excluded in §14.3.
- Shadow traces via `old_english_sandbox_after_*.bin` (adjacent-`mn` build,
  ephemeral `/root`); rule labels as in the sandbox cascade order.

---

# 15. Final CAPR implementation decision (2026-08-14)

The preceding sections (§§1–14) record the full research path, including two
**provisional** and now-**superseded** recommendations that a reader must not
mistake for the implemented judgement:

- §10 (original) and §13.5 (fallback) floated **`known_unmodelled`** as a
  conservative row-level label;
- §14.8 held the row **provisionally `known_unmodelled`** while the
  labial-derivation question was probed to PIE depth.

**Those provisional labels are hereby superseded for implementation.** After the
symmetrical §14 investigation, the implemented decision for **row 2068** is:

```text
PROTO             *xémenaz     (lexeme-level citation reconstruction — retained)
PROTOFORM         *xébun       (selected derivational input: northern WGmc / pre-OE *hebun)
COUNTERPART       heofon       (secure attested OE nominative — retained)
DERIVATION_CLASS  early_analogy
```

## 15.1 Why `early_analogy`, decided *after* §14

§14 established, and this decision rests on, four points that are **not** in
tension:

1. **The labial is historically regular and deep.** In the zero-grade oblique
   cells (gen. `*hemnaz` < PIE `*h₂k-mn-ós`, dat. `*hemni`, dat.pl `*hemnum`),
   `mn > βn` is a regular, mult-1 change (traces §14.2). The `f/b` of OE `heofon`
   therefore has recoverable regular ancestry — a real advance on Ringe–Taylor,
   who merely posit the `b` of `*hebun`.
2. **No oblique gives an uninterrupted *actual* OE line.** The clean cluster
   outputs (`hefnes`, `hifn`, `hefnum`) are attested only in **Norse**
   (ON `hifni`), not Old English; the attested OE forms descend from a
   **re-vowelled** `*hebun-` stem, so a single non-regular event (medial-vowel
   restoration) always intervenes before the attested OE paradigm (§14.3–§14.6).
3. **`*xébun → heofon` is the longest clean regular span that both begins *after*
   the necessary early restructuring and ends in a *secure attested OE* form**
   (§13.4, §14.2c), exactly parallel to the independently-regular *seven*
   `*sébun → seofon`.
4. **The selected `b` is analogical *within this nominative input*, but not
   historically unexplained** (its origin is the cluster-bearing oblique
   paradigm, point 1); the principal remaining opaque element is the medial
   **`u`**, not the labial.

This is the definition of CAPR's **`early_analogy`** class (Part III: "an
analogical change already separates the transducer input from the lexeme's
citation reconstruction *before* the specifically Old English changes apply").
The paradigm remodelling that installs the labial (and the medial vowel) is
encoded in the input `*xébun`; everything the FST models from there
(`u`-lowering, `b`-allophony, back mutation) is regular.

## 15.2 Why not the alternatives

- **Not `late_analogy`.** The selected row models one form, `*xébun → heofon`.
  The restructuring precedes the input; it is not a later paradigm-cell selection
  operating on an otherwise-citation input. The *later* history of *other*
  paradigm cells (oblique syncope, `heo-` levelling) does not touch the modelled
  nominative derivation.
- **Not `known_unmodelled` (for implementation).** That label is intellectually
  legitimate (§13.1 places heaven firmly in the *understood*, not *unexplained*,
  tier) and is **retained in this dossier as the rejected conservative
  alternative**. But it understates what CAPR can model: `*xébun → heofon` *is* a
  clean regular span to an attested target, so declaring the row unmodelled would
  discard a real, defensible derivation. The implementation therefore selects the
  modelled `early_analogy` reading; §14's provisional `known_unmodelled` was a
  research checkpoint, not the verdict.
- **Not the deep obliques as the selected input.** `*xémnas → hefnes`,
  `*xémni → hifn`, `*xémnum → hefnum` derive the labial themselves and are
  historically essential, but their unremodelled outputs are **not** the OE line
  that reaches the attested paradigm (§14.4 B). They stay in the dossier/model
  entry as the deep controls that *explain* the labial, not as the row datum.

## 15.3 SC022 consequence

The decision requires retiring the ahistorical `mV…n` proxy and making
`PNWGmcMnDissimilation` the **literal adjacent** `{*m} -> {*β} || EnglishStarVocalic _ {*n}`.
Heaven never needed a *sound change* for its labial (it needs the *early
analogy*, now encoded in `*xébun`); the proxy's sole beneficiary was this one
row. The literal rule also independently enables the *stem* correction
(`*stámniz → stefn`), gated separately.

## 15.4 Status of earlier sections

§§1–14 are preserved as the research trail. Where they present
`known_unmodelled` (§10 original block, §13.5 fallback, §14.8 provisional) or the
`*héfon` framing (§10) as a recommendation, **read them as superseded by this
§15**: the implemented row is `early_analogy` / `*xébun → heofon`. Nothing in the
evidence is withdrawn — only the row-level label is now fixed.

