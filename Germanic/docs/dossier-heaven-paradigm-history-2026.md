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
