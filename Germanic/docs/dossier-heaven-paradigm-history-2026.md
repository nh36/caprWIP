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

**Bottom line:** *heaven* is **too remodeled to yield a long, clean,
uninterrupted Lautgesetzlich span from a citation-level input to an attested OE
form.** See §10 for the concrete CAPR recommendation (do not use the proxy; do
not use unattested `hefn`).

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

**Primary recommendation — classify row 2068 `known_unmodelled`.** *heaven* is
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

**Acceptable alternative (if a modelled datum is wanted), with full disclosure —
short back-mutation-only span:**
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
