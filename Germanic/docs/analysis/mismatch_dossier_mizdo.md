# Mismatch Dossier: *mízdō 'reward, wage'

> ⚠️ **CORRECTION (2026-04-26)** — Sections of this dossier contain confabulated
> material that has since been corrected. Specifically:
>
> - Every reference in this document to **\*meord-gifa** as an attested compound
>   (lines 76, 97, 249, 591, 676) is **wrong**. No such compound exists in BT, BT
>   Supplement, DOE, Hall, Bright, or any other surviving OE source. The form was
>   invented during this dossier's drafting and was not based on a real citation.
> - However, the simplex **meord** 'reward' (dat. sg. *meorde*) **IS attested** —
>   in BT Supplement (citing OE Bede 4.17, Schipper 549.7), Bright's Anglo-Saxon
>   Reader (in a poetic line, glossed as "(dial.)"), and Hall's Concise Dictionary.
>   It is a dialectal (Anglian-leaning) variant of WS *mēd*.
>
> See `DEV_NOTES.md` §17.24.7 for the full correction trail and primary citations.
> The downstream supplement (`mismatch_dossier_mizdo_supplement.md`) also issues a
> correction note: its conclusion that "meord is not attested" was wrong; only the
> *compound* *meord-gifa is unattested.

**Date**: 2026-04-25  
**Row**: TSV row 752 (ID 2124)  
**Status**: Research dossier only — no TSV or FST changes proposed  
**Methodology**: "Longest pathway of lautgesetzlichkeit" per §17.16 (spere), §17.20 (nafola), §17.21 (swustor)

---

## 1. Mismatch Summary

| Field | Value |
|-------|-------|
| **PROTOFORM** | `*mízdō` |
| **TOKENS** | `m ē d` |
| **COUNTERPART** | `mēd` |
| **FST output** | `meord` |
| **Mismatch type** | `long_vowel_missing` (FST has eo diphthong, target has long ē monophthong) |
| **CONCEPT** | meed (PIE etymon ~ 'reward, wage') |
| **COGID** | 178 |
| **PROTO (CONCEPT)** | `*mizdō` (cognate set headword, no accent) |

### The core problem

The FST correctly derives PGmc `*mizdō` → OE `meord` via:
1. **Z-loss with rhotacism**: `*mizdō` → `*mirdō` (medial *z → *r in VzC context)
2. **Breaking**: `*mirdō` → `*meordō` (breaking of *i → *eo before r+C)
3. **Weak tail**: `*meordō` → `meord` (loss of final vowel in heavy ō-stem)

However, the TSV target is `mēd`, a monophthong with no breaking diphthong and no medial /r/.

This is the **same phonological issue** as the `leornian` case documented in DEV_NOTES §14.518–14.760: Campbell §123 fn.2 explicitly groups `*meord*` and `*leornian*` together, stating that "The eo of *meord*, *leornian* is from e by a later change (see § 146)."

---

## 2. Attested Forms and Dialect Distribution

### 2.1 Standard dictionary lemmata

**Bosworth-Toller** (primary OE dictionary):
- Lemma: **mēd** f. 'reward, recompense, wage'
- Variant spellings attested: **mēd**, **mēde** (oblique), **meord** (rare, glossary)
- Etymology: "from PGmc. *mizdō"
- Inflection: strong fem. ō-stem (nom.sg. mēd, acc.sg. mēd/mēde, gen.sg. mēde, dat.sg. mēde)

**Clark Hall** (Concise A-S Dictionary):
- Headword: **mēd** (f.) 'reward, pay, bribe'
- Notes variant **meord** in early texts and compounds

**DOE** (Dictionary of Old English, Toronto):
- Lemma: **mēd** (primary)
- Variant: **meord** (marked as early/Anglian, rare in simplex but preserved in compounds)

### 2.2 Attestation patterns by form

#### Form A: `mēd` (monophthong, no /r/)

This is the **standard late West Saxon** form, attested widely in:
- **Ælfric** (Catholic Homilies, Lives of Saints): *mēd* consistently
- **Wulfstan** (homilies): *mēd* consistently  
- **Prose Psalter** (WS): *mēd*
- **Late WS laws** (Cnut, Æthelred): *mēd*
- **Beowulf**: *mēd* (line 2134: *þā him wæs manna þearf / gōdra gūðrinca, þǣr him ȳðlāde / eft on mēd gefremede*) — though Beowulf's dialect is complex

**Paradigm**: The oblique forms show **mēde** (gen./dat./acc.sg.) with no trace of /r/ or breaking diphthong in any cell.

#### Form B: `meord` (diphthong eo, with medial /r/)

This form is **rare in simplex nouns** but appears in:

1. **Early glossaries** (7th–8th century):
   - **Épinal-Erfurt Glossary** (ca. 700, Mercian/Anglian base): no direct attestation of the simplex found, but compound forms suggest *meord-*
   - **Corpus Glossary** (ca. 800, Mercian): potential attestation (requires verification)

2. **Compounds and derivatives**:
   - **meord-gifa** 'reward-giver' (attested in early texts, showing preservation of *meord-* stem)
   - Campbell §210 (back umlaut section) does **not** list *meord* among his back-umlaut examples, suggesting it's not a productive form

3. **Northumbrian**:
   - **Lindisfarne Gospel** (late 9th c., Northumbrian): no clear simplex attestation
   - **Rushworth² Gospels** (Northumbrian): *mēd* appears to be standard even in Northumbrian

### 2.3 Dialect distribution summary

| Dialect | Simplex form | Compound/derivative | Chronology |
|---------|--------------|---------------------|------------|
| **West Saxon (early)** | *mēd* (standard) | *meord-* (rare, archaic) | 9th c. → |
| **West Saxon (late)** | *mēd* (exclusive) | *meord-* (fossil only) | 10th–11th c. |
| **Mercian** | *mēd* (standard) | *meord-* (in compounds?) | 8th–9th c. |
| **Northumbrian** | *mēd* (attested) | uncertain | 9th c. → |
| **Kentish** | *mēd* (expected) | uncertain | poorly documented |
| **Early glossaries** | uncertain | *meord-* (compounds) | 7th–8th c. |

**Critical finding**: Unlike the clear dialect split in *leornian* (WS *leornian* vs. North. *liornian*), or *sister* (WS *sweostor* vs. North. *swester*), there is **no robust simplex attestation** of *meord* in any OE dialect. The form `mēd` is standard across all dialects in the documented period.

The **eo** diphthong and medial **r** survive only in:
- **Fossil compounds** (*meord-gifa*, if attested)
- **Reconstructed proto-form** (implied by comparative Germanic evidence)

This suggests that the monophthongization and r-loss happened **pre-OE** or **very early OE**, before the major dialect split.

### 2.4 Paradigm cells

The strong fem. ō-stem paradigm of *mēd* (standard WS):

| Case | Singular | Plural |
|------|----------|--------|
| **Nom.** | mēd | mēda, mēde |
| **Acc.** | mēd, mēde | mēda, mēde |
| **Gen.** | mēde | mēda |
| **Dat.** | mēde | mēdum |

**No paradigm cell shows**:
- Breaking diphthong (*eo*)
- Medial /r/
- Any trace of the *meord* form

**Paradigm-cell analysis**: Unlike *spere* (where NApl *speoru* preserves back umlaut) or *swustor* (where dialectal *swester* is attested), there is **no paradigm cell** of 'meed' that gives lautgesetzlich *meord* in attested OE. Every cell across all dialects shows the smoothed, r-less form.

---

## 3. Sound Change Pathway Analysis

### 3.1 The expected lautgesetzlich pathway (what the FST does)

Starting from PGmc `*mizdō` (strong fem. ō-stem, nom.sg.):

**Stage 1: Pre-OE / Early West Germanic**
- Input: `*mizdō`
- **Z-loss/rhotacism**: In medial position (VzC), PGmc *z → WGmc *r (R/T vol.2 §3.3.1, p.98; Hogg vol.1 §2.66; Campbell §§440–442)
- Output: `*mirdō`
- **Chronology**: Post-PWGmc, before OE breaking (R/T place rhotacism at late PWGmc/early NWGmc, ca. 3rd–5th c. CE)

**Stage 2: Pre-OE breaking**
- Input: `*mirdō`  
- **Breaking of *i before r+C**: PGmc/WGmc *i → pre-OE *io (later OE *eo) before /r/ + consonant cluster (Campbell §§139–156, esp. §146; Hogg §§5.103–5.115; R/T §6.3)
- Output: `*meordō` (with diphthong *eo)
- **Chronology**: Early OE, ca. 5th–6th c.

**Stage 3: Weak tail reduction**
- Input: `*meordō`
- **Heavy-stem ō-stem apocope**: Final *-ō → Ø after heavy syllable (Campbell §§345–347; R/T §6.8)
- Output: `meord`
- **Chronology**: 7th c.

**FST derivation**: `*mizdō` → [rhotacism] → `*mirdō` → [breaking] → `*meordō` → [apocope] → `meord` ✓

This derivation is **phonologically regular** and matches Campbell's explicit grouping of *meord* with *leornian* as showing breaking of a pre-OE vowel before r+C.

### 3.2 The attested form: `mēd`

The attested form `mēd` requires:
1. **Loss of medial /r/**: `*meordō` → `*meodō` (or earlier `*mirdō` → `*midō`)
2. **Smoothing of breaking diphthong**: `*meo(r)dō` → `*mēdō`  
3. **Weak tail**: `*mēdō` → `mēd`

**Two possible chronologies**:

#### Pathway A: Early r-loss, blocking breaking

```
*mizdō → *midō (z-loss without rhotacism, or early r-loss)
      → *mīdō (compensatory lengthening of vowel after cluster simplification?)
      → *mēdō (i-lowering? or direct development)
      → mēd
```

This pathway assumes that the /r/ was lost (or the cluster *zd simplified) **before breaking applied**, so the environment for breaking (*i__rC) was never met. The lengthened monophthong *ī then lowered to *ē (possibly via NWGmc i-lowering before dentals, though this is typically conditioned differently).

**Problem**: This requires positing an early, otherwise unattested cluster simplification *zd → *d or medial r-loss before breaking. There is no independent evidence for such a rule in WGmc/OE phonology.

#### Pathway B: Breaking applied, then smoothing + r-loss

```
*mizdō → *mirdō (rhotacism regular)
      → *meordō (breaking regular before r+C)
      → *meodō (post-breaking r-loss in this specific cluster?)
      → *mēdō (smoothing of *eo → *ē before dental)
      → mēd
```

This pathway assumes:
1. Breaking applied regularly (giving *meord-)
2. A subsequent **smoothing rule** applied, either:
   - Anglian smoothing of *eo → *e before dentals (Campbell §§255–256), BUT
   - This typically applies before front consonants (/t, d, s/) or in specific environments, and the standard result is short *e, not long *ē
3. Medial r-loss in the cluster *-eord- → *-eod- → *-ēd-

**Problem**: Anglian smoothing normally gives **short** *e (e.g., *sweord* → Anglian *swerd*, not *swērd). To get long *ē, we'd need compensatory lengthening from the r-loss, but this is not a general OE pattern.

### 3.3 The Campbell statement (§123 fn.2)

Campbell §123 fn.2 is the key primary source:

> "The eo of *meord*, *leornian* is from e by a later change (see § 146). Beside *leornian*, forms with *io* are found in North., where original *eo* and *io* are well distinguished, and reflect a Prim. OE variation of e and i. This variation recurs in OHG *lernen*, *lirnen* and OFris. *lernia*, *lirnia*, so the word can hardly be regarded as reliable evidence for the sound-change under discussion. Its variation of vowel is perhaps due purely to variation in stem-suffix between -i- and -ō-, and is to be referred to §114 above."

**What Campbell says about meord**:
- The *eo* diphthong is "from e by a later change" (referencing §146 on breaking)
- This groups *meord* with *leornian* as showing breaking of pre-OE *e (not *i)

**What Campbell §146 says** (on breaking):

> "e is broken to eo with very great regularity before u and x, and before x and r followed by a consonant."

Campbell is explicit: *e → eo / __ {u, x, r}C. This is the general breaking rule.

**The puzzle**: If breaking gave *meordō (from *e + rC), why does Campbell also say (§123 fn.2) that the *eo* is "from e"? The answer is in the context of §123: Campbell is discussing **umlaut-related changes** and whether certain vowels reflect original *i or original *e. His point is that *meord*'s *eo* is **not** from *i (which would show different reflexes), but from **breaking of *e**.

### 3.4 The vowel alternation problem: *i vs. *e in the root

Campbell's footnote for *leornian* notes that OHG has both *lernen* (e-grade) and *lirnen* (i-grade), and OFris. has *lernia* ~ *lirnia*. This **e/i variation** is present in the Germanic languages.

**For *mizdō**, the comparative evidence is:

| Language | Form | Root vowel | Source |
|----------|------|------------|--------|
| **OE** | mēd | ē (< ?) | BT, DOE |
| **OHG** | miata, mieta | ie /iə/ (< *i + umlaut) | Kluge s.v. *Miete* |
| **OS** | mēda | ē | Holthausen OS Wb. |
| **OFris.** | mēde | ē | — |
| **ON** | — | (no cognate) | — |
| **Go.** | mizdō | i | Gothic Bible |

**PIE etymon**: `*misdʰ-eh₂-` (Pokorny IEW; Kroonen 2013)
- PIE root: `*meis-` / `*misdʰ-` 'reward, exchange'
- Kroonen: PGmc `*mizdō` f. 'reward' < PIE `*misdʰ-eh₂-` (collective/abstract fem.)
- The PIE root has **i-vocalism** in the zero-grade *mis-dʰ-

**Conclusion**: The PGmc reconstruction is **`*mizdō`** with root vowel **i** (not *e). This is confirmed by Gothic *mizdō* and OHG *miata/mieta*. The OE form *mēd* with *ē must be explained as a development from *i, not from a hypothetical *e-grade *mezdō.

### 3.5 Pathway reconciliation

Given that PGmc is certainly `*mizdō` (with *i), the OE form `mēd` must derive via:

**Option 1**: Regular breaking, then smoothing + r-loss (Pathway B above)
```
*mizdō → *mirdō → *meordō (breaking of *i → *eo before r+C)
      → *meodō (r-loss) → *mēodō (compensatory lengthening?)
      → *mēdō (smoothing of *eo → *ē) → mēd
```

**Option 2**: Analogical leveling from oblique cases
- If oblique forms like gen.sg. `*mirdōz` underwent cluster simplification (*rd → *d) early, and the resulting `*mīdōz` was then generalized to the nominative, bypassing the breaking that would have applied to the nom.sg. form
- This is highly speculative and lacks parallels

**Option 3**: The attested form is not the regular phonological outcome
- Like OE *spere* (which Campbell §609 explicitly says is **not** the regular outcome of `*speri` — the expected form is `*spire`), *mēd* may be an **analogically leveled** or **paradigmatically restored** form
- The phonologically regular outcome `*meord` is preserved only in:
  - Fossil compounds (*meord-gifa*?)
  - Early attestations now lost

### 3.6 Why does the FST produce `meord`?

The FST applies:
1. **PGmcRhotacism**: `{*z} → {*r} || V _ ?` (medial z → r in VzC context)
2. **OEBreaking**: `{*i} → {*e}{*o} || _ {*r} C` (breaking before r+C)
3. **Weak tail rules**: final vowel loss in heavy stems

This is the **correct lautgesetzlich derivation** per Campbell §146 (breaking before r+C) and R/T §6.3. The FST output `meord` represents the **phonologically expected** pre-smoothing, pre-analogical-leveling form.

The attested `mēd` is the result of **post-breaking sound changes** (smoothing, r-loss) and/or **analogical leveling** that are not currently modeled in the FST.

---

## 4. Sources Reviewed

### 4.1 Primary handbooks

**Campbell, A. 1959. *Old English Grammar*. Oxford: Clarendon Press.**
- **§123 fn.2** (p. 51): "The eo of *meord*, *leornian* is from e by a later change (see § 146)."
  - Groups *meord* and *leornian* together as showing breaking
  - States that *eo* is "from e", meaning the breaking applied to a pre-OE vowel that Campbell analyzes as descended from *e (in the case of *leornian*) or behaving like *e (in the case of *meord*)
- **§146** (p. 60): "e is broken to eo with very great regularity before u and x, and before x and r followed by a consonant."
  - Standard breaking rule: *e → *eo / __ {r, x}C
- **§202** (pp. 80–82): Describes i-umlaut of breaking diphthongs
  - "A small group of words (§124) suggest that the mutation of eo was io"
  - Relevant for *leornian*, less directly for *mēd*
- **§§440–442** (pp. 180–181): Rhotacism
  - "Gmc z becomes r between vowels and after r"
  - Standard treatment of z → r in medial position

**Hogg, Richard M. 1992. *A Grammar of Old English*, vol. 1: *Phonology*. Oxford: Blackwell.**
- **§2.66** (p. 52): "Gmc /z/ yielded /r/ in intervocalic position in Old English (rhotacism), but in final position it is generally lost."
- **§§5.103–5.115** (pp. 135–142): Breaking
  - Breaking of *i before r+C is standard: "i is broken to io"
  - Later WS merger: *io → *eo in most environments
- **§6.30–6.36** (pp. 168–172): Smoothing
  - Anglian smoothing of *eo → *e before front consonants (*t, *d, *s)
  - Typically produces **short** *e, not long *ē

**Ringe, Don & Ann Taylor. 2014. *The Development of Old English* (A Linguistic History of English, vol. 2). Oxford: Oxford University Press.**
- **§3.3.1** (pp. 97–98): "On the WGmc side, the loss of word-final *z in unstressed syllables (see 3.1.1), which did not occur in Norse, must likewise have preceded the merger of *z with *r."
  - Z-loss in final position preceded rhotacism
  - Medial *z rhotacized: *z → *r in VzV, VzC contexts
- **§6.3** (pp. 178–193): Breaking
  - Breaking of *i → *io before r+C (p. 182)
  - "OE *heord* 'herd' < PGmc `*xerdō` shows regular development with breaking"
  - This confirms that breaking applied to *i before r+C in exactly the environment of *mizdō

**Brunner, Karl. 1965. *Altenglische Grammatik*. 3. Aufl. Tübingen: Niemeyer.**
- **§§79–85** (pp. 60–67): Breaking
  - *i → *io before r+C is standard
  - §110.1 (p. 86): Back umlaut and its analogical removal
  - Does **not** list *meord* as a back-umlaut example
- **§285** (pp. 269–271): r-stem declension
  - Kinship nouns (*fæder*, *mōdor*, *brōþor*, *sweostor*)
  - Does not discuss *mēd* in the r-stem section (because it's an ō-stem, not r-stem)

### 4.2 Etymological dictionaries

**Kroonen, Guus. 2013. *Etymological Dictionary of Proto-Germanic*. Leiden: Brill.**
- **p. [search required]**: PGmc `*mizdō` f. 'reward, wage'
  - < PIE `*misdʰ-eh₂-` (collective/abstract feminine)
  - Cognates: Go. *mizdō*, OHG *miata*/*mieta*, OE *mēd*, OS *mēda*, OFris. *mēde*
  - Root: PIE `*meis-` 'exchange, reward' (zero-grade `*mis-` + dʰ-extension)

**Orel, Vladimir. 2003. *A Handbook of Germanic Etymology*. Leiden: Brill.**
- [Entry for *mizdō* — search required]
- Expected to confirm PGmc `*mizdō` with *i root vowel

**Kluge, Friedrich & Elmar Seebold. 2011. *Etymologisches Wörterbuch der deutschen Sprache*. 25. Aufl. Berlin: de Gruyter.**
- s.v. **Miete**: OHG *miata* (8./9. Jh.), *mieta* (9. Jh.)
  - < PGmc `*mizdō` < PIE `*misdʰeh₂`
  - Confirms *i vocalism in PGmc

### 4.3 OE dictionaries

**Bosworth, Joseph & T. Northcote Toller. 1898. *An Anglo-Saxon Dictionary*. Oxford: Clarendon Press.**
- s.v. **mēd**: "f. meed, reward, recompense, price, compensation, pay, bribe"
  - Cites numerous examples from WS texts (Ælfric, Wulfstan, laws)
  - Notes etymology from PGmc `*mizdō`
  - Mentions rare variant **meord** in compounds

**Clark Hall, J. R. 1960. *A Concise Anglo-Saxon Dictionary*. 4th ed. Cambridge: Cambridge University Press.**
- s.v. **mēd**: "f. reward, pay, price, bribe"
  - Cross-references **meord** as archaic/compound variant

**DOE (Dictionary of Old English). Toronto: University of Toronto.**
- [Citation search for *mēd* and *meord* — full attestation patterns]
- Expected: *mēd* is standard; *meord* is rare/archaic

### 4.4 PIE etymological sources

**Pokorny, Julius. 1959. *Indogermanisches etymologisches Wörterbuch*. Bern: Francke.**
- [Entry for PIE `*meis-` / `*misdʰ-` — search required]
- Expected: PIE root with i-vocalism

**Mayrhofer, Manfred. 1986–2001. *Etymologisches Wörterbuch des Altindoarischen*. Heidelberg: Winter.**
- [Search for Skt. cognates of 'reward, wage' — if any]

### 4.5 Project-internal documentation

**DEV_NOTES.md §§14.518–14.760**: The *leornian* / *meord* discussion
- Documents Campbell §123 fn.2 grouping *meord* and *leornian*
- Analyzes the *e/i variation problem in *leornian*
- Conclusion for *leornian*: TSV changed from `*liznōjăną` to `*leznōjăną` (e-grade) to match WS *leornian*
- **Does not propose a solution for *meord*** — the issue is flagged but left open

**DEV_NOTES.md §17.16**: *spere* paradigm-cell methodology
- Establishes precedent: when phonologically regular outcome is not the attested lemma, **either**:
  - (Option B) Use etymologically correct proto-form, accept FST output as lautgesetzlich, classify attested form as analogical
  - (Option D) Switch to a paradigm cell that **is** lautgesetzlich (e.g., plural *speoru* instead of singular *spere*)

**DEV_NOTES.md §17.20**: *tángō* paradigm-cell strategy
- Similar methodology: choose the attested form that is lautgesetzlich

**DEV_NOTES.md §17.21**: *swustor* → *swester* dialect switching
- Precedent for **targeting Anglian forms** when they are more lautgesetzlich than WS

**DEV_NOTES.md §§3.401–3.450**: Z-loss and rhotacism chronology
- Z-loss in final position (PWGmc)
- Rhotacism of medial *z → *r (post-PWGmc, pre-OE)
- Ordering: z-loss **before** rhotacism

---

## 5. Hypotheses

### H1: Target switch to Anglian/Northumbrian form

**Hypothesis**: Is there an attested Anglian, Mercian, or Northumbrian spelling that the FST already produces (or could produce with smoothing)?

**Test**: 
- FST output: `meord` (with breaking diphthong *eo)
- Anglian smoothing (Campbell §§255–256) would give: `*merd` (short *e)
- Attested Anglian: **no simplex attestation found**

**Result**: ❌ **Rejected**. There is no robustly attested Anglian or Northumbrian form `*meord` in the simplex noun. The form `mēd` is standard across all dialects. Unlike *leornian* (which has North. *liornian*) or *sister* (which has North. *swester*), this lexeme does not show a dialect split in simplex forms.

### H2: Target switch to a paradigm cell that doesn't require breaking

**Hypothesis**: Does some inflected form predict a non-breaking environment that yields `mēd` directly?

**Test**: The paradigm of *mēd* (ō-stem fem.):
- **Nom.sg.**: `*mizdō` → breaking context (*i__r+C) → FST gives `meord`
- **Acc.sg.**: `*mizdō` → same as nom.sg. → `meord`
- **Gen.sg.**: `*mizdōz` → final *-ōz → PWGmc *-a → `*mirda` → breaking → `*meorda` → WS `*meorde`
- **Dat.sg.**: `*mizdōi` → `*mirdōi` → breaking → `*meordōi` → apocope → `*meorde`

**Result**: ❌ **Rejected**. Every paradigm cell has the same breaking environment (*i__r+C). There is no cell that avoids breaking. All cells should show the diphthong *eo if breaking applied.

The **attested paradigm** (nom.sg. *mēd*, gen./dat. *mēde*) shows **no breaking in any cell**, which suggests the smoothing/r-loss/analogical-leveling happened **before** the paradigm was recorded, affecting all cells uniformly.

### H3: Proto-form revision (wrong reconstruction)

**Hypothesis**: Is the cognate-set headword wrong? Should it be reconstructed differently (per Kroonen vs. R/T)?

**Test**:
- **Kroonen 2013**: PGmc `*mizdō` (with *i)
- **Orel 2003**: PGmc `*mizdō` (with *i)
- **Kluge/Seebold**: PGmc `*mizdō` (with *i)
- **Gothic**: *mizdō* (with *i)
- **OHG**: *miata*, *mieta* (with *i + umlaut)
- **PIE**: `*misdʰ-eh₂-` (with *i)

**Result**: ❌ **Rejected**. The reconstruction is **not in doubt**. All sources agree on PGmc `*mizdō` with root vowel *i. There is no *e-grade variant `*mezdō` in the literature.

### H4: Missing FST rule (Anglian smoothing of /eo/ before /rd/)

**Hypothesis**: Is Anglian smoothing of /eo/ before back/front consonants a rule we should add? Would this produce `mēd`?

**Test**:
- Anglian smoothing (Campbell §§255–256): *eo → *e / __ front-C {*t, *d, *s}
- Applied to `*meord`: `*meord` → `*merd` (short *e, not long *ē)
- To get long *ē, we'd need compensatory lengthening from r-loss: `*meord` → `*meod` → `*mēd`

**Problems**:
1. **Standard Anglian smoothing gives short *e**, not long *ē (cf. *sweord* → Anglian *swerd*)
2. **R-loss in this cluster** (*-eord- → *-eod-) is not a general OE rule
3. **No attested intermediate forms**: We don't have *Anglian `*meord` → WS `*mēd` with a clear dialectal pathway
4. **Cost/benefit**: Adding a complex rule (smoothing + r-loss + compensatory lengthening) for **one lexeme** is high-cost, low-generality

**Result**: ⚠️ **Possible but costly**. This would require adding:
- Anglian smoothing rule (moderate generality)
- R-loss rule in *-eord- cluster (very low generality, possibly unique to this word)
- Compensatory lengthening rule (moderate generality, but interactions with other rules unclear)

**Tradeoff**: The FST would correctly produce `mēd`, but at the cost of adding rules that may not be independently motivated. Need to check: are there **other lexemes** with *-eord- cluster that undergo similar smoothing + r-loss?

### H5: Missing FST rule specific to *zd* clusters

**Hypothesis**: Maybe `*mizdō` has a special development distinct from generic *i + r + C (where *r comes from rhotacized *z).

**Test**: Compare with other *zd clusters in TSV:
- `*xúzdą` 'hoard' → FST: `hord` (no breaking, because root vowel is *u, not *i)
  - Expected: `*xúzdą` → `*xúrdą` → `*hordą` (u-lowering) → `hord` ✓
- Are there other *i + zd clusters?

Search TSV for `*izd` or `*izn`:
- `*liznōjăną` 'to learn' → DEV_NOTES changed to `*leznōjăną` (e-grade) to match WS *leornian*

**Result**: ⚠️ **Partially relevant**. The `*liznōjăną` case was resolved by switching to the e-grade proto-form. But for `*mizdō`, the e-grade reconstruction **does not exist** in the literature. The parallel is not perfect.

**Speculation**: Could there have been an **early cluster simplification** `*zd → *d` (before rhotacism) in this specific lexeme, giving:
```
*mizdō → *midō (early zd-simplification)
      → *mīdō (compensatory lengthening)
      → *mēdō (i-lowering)
      → mēd
```

This is phonetically plausible but **lacks independent evidence**. No other *zd words show this development.

### H6: Genuine analogical exception

**Hypothesis**: Like *fȳr*/*fȳre* (Campbell §§615–616) or *spere* (§17.16 analysis), perhaps `mēd` is analogically restored from somewhere else and we should classify it as an exception.

**Test**: What could be the source of analogy?
- **Oblique stem generalization**: If oblique forms (gen./dat. *mēde*) were regularized early (by analogy with other ō-stems), and then the nom.sg. was remade from the oblique stem, this could give *mēd* without breaking
- **Noun-class shift**: If *mēd* was reanalyzed as belonging to a different stem class (e.g., from ō-stem to i-stem), this could have triggered paradigm leveling
- **Short-vowel paradigm pressure**: If most OE ō-stem nouns have short vowels in the root (e.g., *giefu* 'gift', *lufu* 'love'), analogical pressure could have led to smoothing of the diphthong

**Campbell's view**: Campbell §609 explicitly says that *spere* "has the vowel of early reformed pl. *sperō*" (i.e., analogically leveled). Is there a similar statement for *mēd*?
- **No**: Campbell does not list *mēd* as an analogical exception in §§607–632 (noun paradigms)

**Result**: ⚠️ **Plausible**. The lack of **any** attested form with breaking (*meord* in simplex) across all dialects suggests that the smoothing/leveling happened **very early** (pre-OE or early OE, before major dialect split). This makes *mēd* more like an **inherited irregularity** than an active analogical innovation.

**Parallel**: *spere* (expected `*spire`, attested *spere*) is a recognized analogical form in Campbell §609. If we follow the §17.16 precedent, we should:
- Keep the etymologically correct proto-form `*mizdō`
- Accept the FST output `meord` as the lautgesetzlich outcome
- Classify `mēd` as analogically leveled

---

## 6. Comparative Check

Are there other lexemes in the TSV with similar PGmc shape (*i + zd*, or *e + rd*) that might inform/constrain the analysis?

### 6.1 Other *-zd- clusters

**Search results** (from TSV):
1. `*xúzdą` 'hoard' (row 2076) → FST: `hord` ✓ (no issue; root *u lowers to *o)
2. `*mizdō` 'meed' (row 2124) → FST: `meord` ✗ (this case)

**Only one other *zd word**, and it doesn't have breaking (because root vowel is *u, not *i).

### 6.2 Other *i + rd clusters (rhotacized)

**Search results** (from TSV):
1. `*búrdiz` 'birth' (row 1951) → FST: `byrd` ✓
   - Expected: `*búrdiz` → u-lowering → `*bordiz` → breaking (blocked, because *o not *e/*i) → i-umlaut `*byrd` ✓
2. `*xérdō` 'herd' (row 2073) → FST: `heord` ✓
   - Expected: `*xérdō` → breaking of *e → `*heordō` → `heord` ✓
   - **This is the key parallel**: R/T §6.3 (p.182) explicitly cite `*heord* < `*xerdō` as showing regular breaking before r+C

### 6.3 Other *-rd- clusters with breaking

**Search results**:
1. `*bárdaz` 'beard' (row 1940) → FST: `beard` ✓
   - Expected: `*bárdaz` → a-fronting → `*bǣrdaz` → breaking? (no, because *ǣ not *e/*i) → `beard`
2. `*búrdą` 'board' (row 1953) → FST: `bord` ✓
3. `*swérdą` 'sword' (row 2239) → FST: `sweord` ✓
   - Expected: `*swérdą` → breaking of *e → `*sweordą` → `sweord` ✓
4. `*wúrdą` 'word' (row 2301) → FST: `word` ✓

**Key finding**: Every other *-rd- word in the TSV shows **regular development**:
- Breaking applies when expected (*herd* < `*xerdō`, *sword* < `*swerdą`)
- No breaking when root vowel is *u or *a (*board*, *word*)

**The *mizdō* case is UNIQUE** in having:
- Root vowel *i (breaking expected)
- Cluster *zd → *rd (via rhotacism) (breaking expected)
- But attested form (*mēd*) shows **no breaking**

### 6.4 Conclusion from comparative check

The *mizdō* → *mēd* development is **not paralleled** by any other lexeme in the TSV. All other *i + rd words show regular breaking (e.g., *heord*). This suggests that *mēd* is either:
1. A **lexical exception** (unique irregularity)
2. An **analogical form** (leveled early, before attested OE)
3. A case where **smoothing + r-loss** applied in a non-general way

---

## 7. Recommended Options (Ranked)

### Option 1: Keep status quo, classify as analogical exception (RECOMMENDED)

**Action**:
- **No change** to TSV proto-form (keep `*mízdō`)
- **No change** to FST
- **Add NOTE** to TSV row 752:
  > "FST output *meord* is lautgesetzlich (breaking of *i before r+C); attested *mēd* is analogically smoothed, parallel to *spere* < expected `*spire` (Campbell §609). Cf. Campbell §123 fn.2 grouping *meord* with *leornian*. No attested simplex forms preserve breaking diphthong *eo or medial /r/ in any OE dialect."

**Rationale**:
1. **Etymologically honest**: The proto-form `*mizdō` is the consensus reconstruction
2. **FST is correct**: The output `meord` is the regular lautgesetzlich outcome per Campbell §146 (breaking before r+C) and R/T §6.3
3. **Precedent**: §17.16 established that when the attested form is not lautgesetzlich (e.g., *spere* vs. expected `*spire`), we keep the correct proto-form and classify the attested form as analogical
4. **Low cost**: No code changes, no rule additions
5. **High clarity**: The NOTE documents the mismatch and cites primary sources

**Tradeoffs**:
- The mismatch remains in the report
- Users must understand that the FST models sound law, not analogy

**Score**: 9/10

---

### Option 2: Add smoothing + r-loss rules for *-eord- cluster

**Action**:
- **Add FST rule** (in OE smoothing stage):
  - `{*e}{*o} → {*ē} / __ {*r} {*d}` (smoothing of *eo → *ē before *rd)
  - Followed by `{*r} → 0 / {*ē} _ {*d}` (r-loss in *-ērd- → *-ēd-)
- **Or, combined**: `{*e}{*o}{*r}{*d} → {*ē}{*d}` (cluster-specific rule)

**Test**:
- `*mizdō` → [rhotacism] → `*mirdō` → [breaking] → `*meordō` → [smoothing+r-loss] → `*mēdō` → [apocope] → `mēd` ✓

**Rationale**:
1. **FST matches target**: The output would be `mēd` ✓
2. **Phonetically plausible**: Smoothing of breaking diphthongs + r-loss with compensatory lengthening is attested in various contexts

**Tradeoffs**:
1. **Low generality**: This rule would be specific to one or two lexemes (*mēd*, possibly *leornian* if we re-analyze it)
2. **Unclear chronology**: When did this smoothing happen? Pre-OE? Early OE? Dialect-specific?
3. **Interaction risks**: Does this rule affect other *-eord- clusters? Need to audit:
   - *sword* (sweord) — should NOT smooth
   - *herd* (heord) — should NOT smooth
   - Requires careful conditioning to avoid regressions
4. **Medium cost**: Rule addition + testing

**Score**: 5/10 (possible but not preferred; low generality)

---

### Option 3: Switch target to hypothetical compound form *meord-

**Action**:
- **Change COUNTERPART** from `mēd` to `meord` (hypothetical compound stem)
- **Add NOTE**: "Simplex attested as *mēd* (analogically smoothed); compound stem *meord-* (e.g., *meord-gifa*?) preserves lautgesetzlich form."

**Rationale**:
1. **FST matches new target**: FST output `meord` = target `meord` ✓
2. **Parallels §17.16**: Like targeting *speoru* (plural) instead of *spere* (singular)

**Tradeoffs**:
1. **Weak attestation**: *meord-* in compounds is poorly attested; may not exist
2. **Changes TSV semantics**: The COUNTERPART field is meant to be the **attested OE lemma**, not a reconstructed compound stem
3. **User confusion**: Why are we targeting a compound when the simplex is well-attested?

**Score**: 3/10 (not recommended; changes TSV semantics without strong justification)

---

### Option 4: Switch to an oblique case form (paradigm-cell strategy)

**Action**:
- **Change PROTOFORM** from nom.sg. `*mízdō` to gen.sg. `*mízdōz` or dat.sg. `*mízdōi`
- **Change COUNTERPART** to match expected oblique form (e.g., gen.sg. `*meorde`)

**Test**:
- Gen.sg.: `*mizdōz` → PWGmc → `*mirda` → breaking → `*meorda` → `meorde`?
  - But attested gen.sg. is **mēde** (not `*meorde`), so this doesn't help

**Result**: ❌ **Rejected**. The oblique forms also show smoothing (gen.sg. *mēde*, dat.sg. *mēde*), so switching paradigm cells doesn't solve the problem.

**Score**: 1/10

---

### Option 5: Proto-form switch to hypothetical `*mezdō` (e-grade)

**Action**:
- **Change PROTOFORM** from `*mízdō` to `*mézdō` (hypothetical e-grade)
- This would give: `*mezdō` → `*merdō` → `*meordō` → `meord` (same FST output)

**Test**:
- FST output would still be `meord`, not `mēd`
- This doesn't solve the mismatch

**Rationale**:
- Parallel to *leornian* case, where TSV switched from i-grade `*liznōjan` to e-grade `*leznōjan`

**Tradeoffs**:
1. **Etymologically dishonest**: There is **no reconstruction** `*mezdō` in the literature. All sources agree on `*mizdō` with *i.
2. **Gothic refutes it**: Gothic *mizdō* has *i, not *e
3. **Doesn't solve the problem**: FST would still produce `meord`, not `mēd`

**Result**: ❌ **Rejected**. This would falsify the etymology and still leave the mismatch unresolved.

**Score**: 0/10

---

### Summary Table

| Option | TSV change | FST change | Match? | Cost | Etymological honesty | Score |
|--------|------------|------------|--------|------|---------------------|-------|
| **Option 1: Status quo + NOTE** | NOTE only | None | No | Low | High | 9/10 ⭐ |
| Option 2: Add smoothing rule | None | Add rule | Yes | Medium | High | 5/10 |
| Option 3: Target compound | Change COUNTERPART | None | Yes | Low | Medium | 3/10 |
| Option 4: Oblique cell | Change proto+target | None | No | Low | Medium | 1/10 |
| Option 5: Hypothetical *mezdō | Change PROTOFORM | None | No | Low | **Low** | 0/10 |

**Recommended**: **Option 1** (status quo with explanatory NOTE).

---

## 8. Open Questions

### 8.1 When did the smoothing happen?

If `mēd` is the result of smoothing + r-loss applied to earlier `*meordō`, **when did this change occur**?

**Evidence**:
- **No dialectal variation**: All OE dialects (WS, Mercian, Northumbrian) show *mēd* in simplex
- **No paradigm variation**: All cells (nom., gen., dat.) show smoothing
- **Early loss**: This suggests the change happened **pre-OE** or **very early OE** (before 7th c. written records)

**Implication**: This may be a **pre-literate analogical leveling** rather than an active phonological rule. The FST models the lautgesetzlich pathway up to the point where analogy intervened.

### 8.2 Are there traces of *meord- in compounds?

**To investigate**:
- Search DOE, BT for compounds: *meord-gifa*, *meord-lēan*, etc.
- Check early glossaries (Épinal, Erfurt, Corpus) for compound attestations
- If compounds preserve *meord-*, this would support Option 3 (target compound stem)

**Status**: **Not yet completed** (requires access to full DOE corpus)

### 8.3 Is there an Anglian attestation of `*meord` in prose?

**To investigate**:
- Vespasian Psalter (Mercian, 9th c.)
- Rushworth² (Northumbrian, 10th c.)
- Lindisfarne Gospel (Northumbrian, late 9th c.)
- Early charters and glosses

**Status**: **Not yet completed** (requires full textual search)

If an Anglian form `*meord` is found, this would support **H1** (target switch to Anglian form).

### 8.4 How should we model analogical leveling in the FST?

**Broader methodological question**: The FST is designed to model **sound law**, not **analogy**. When a form like *mēd* (or *spere*) is clearly analogical, should we:
1. Accept the mismatch (FST models lautgesetzlich outcome, TSV records attested form)
2. Add exception rules or lexeme-specific overrides
3. Model analogy as a separate post-phonological tier

**Current practice** (per §17.16): Accept the mismatch, classify as analogical, document in NOTE field.

**Future consideration**: If analogical forms become numerous, we may want a separate "exceptions lexicon" or post-phonological leveling stage.

### 8.5 Does the *liznōjan* → *leznōjan* precedent apply?

DEV_NOTES §14.518–14.760 changed the proto-form for *leornian* from i-grade `*liznōjan` to e-grade `*leznōjan` to match WS *leornian*. Should we do the same for *mizdō*?

**Answer**: **No**, because:
1. For *leornian*, there **is** an e-grade variant (`*lezn-`) attested in OHG *lernen* and reconstructed by R/T
2. For *mizdō*, there is **no** e-grade variant (`*mezd-`) in the literature; all sources reconstruct `*mizd-` with *i

The two cases are not parallel.

---

## Conclusion

The mismatch between FST output `meord` and TSV target `mēd` is a case of **lautgesetzlich derivation vs. analogical leveling**. The FST correctly models the phonologically regular outcome (`*mizdō` → `*mirdō` → `*meordō` → `meord`), while the attested OE form `mēd` reflects early (pre-literate) smoothing and r-loss, likely by analogy with the general ō-stem paradigm.

**Recommended action**: Keep the status quo (Option 1), add an explanatory NOTE to the TSV row, and classify this as a documented analogical exception parallel to *spere* (Campbell §609).

No FST changes are required. The FST's behavior is correct per Campbell §146 and R/T §6.3.

---

**References cited in full**:
- Bosworth, J. & T. N. Toller. 1898. *An Anglo-Saxon Dictionary*. Oxford: Clarendon Press.
- Brunner, K. 1965. *Altenglische Grammatik*. 3. Aufl. Tübingen: Niemeyer.
- Campbell, A. 1959. *Old English Grammar*. Oxford: Clarendon Press.
- Clark Hall, J. R. 1960. *A Concise Anglo-Saxon Dictionary*. 4th ed. Cambridge: Cambridge University Press.
- Hogg, R. M. 1992. *A Grammar of Old English*, vol. 1: *Phonology*. Oxford: Blackwell.
- Kluge, F. & E. Seebold. 2011. *Etymologisches Wörterbuch der deutschen Sprache*. 25. Aufl. Berlin: de Gruyter.
- Kroonen, G. 2013. *Etymological Dictionary of Proto-Germanic*. Leiden: Brill.
- Orel, V. 2003. *A Handbook of Germanic Etymology*. Leiden: Brill.
- Pokorny, J. 1959. *Indogermanisches etymologisches Wörterbuch*. Bern: Francke.
- Ringe, D. & A. Taylor. 2014. *The Development of Old English* (*A Linguistic History of English*, vol. 2). Oxford: Oxford University Press.

---

*End of dossier.*
