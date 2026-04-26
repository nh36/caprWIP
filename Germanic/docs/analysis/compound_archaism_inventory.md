# Archaism Preservation Inventory: Where Lautgesetzlich Forms Survive in OE

**Date created:** 2026-04-25 (originally as "Compound Archaism Inventory")
**Recast:** 2026-04-26 — broadened scope per user direction; Case 1 (meord) corrected
**Status:** Research reference document
**Scope:** Consolidation of cases documented in DEV_NOTES.md where lautgesetzlich (sound-law-regular) forms are preserved *somewhere* in the OE evidence — even when the most-cited simplex / nominative singular shows leveled, smoothed, or analogical outcomes. Compound first-elements are one such locus; this document also covers dialectal doublets, oblique paradigm cells, plurals, glossary lemmata, and other fossils.

> **Recasting note (2026-04-26)**: This inventory was originally framed narrowly
> around the "Watkins principle" — archaisms preserved specifically in compounds.
> While that pattern is real and well-attested in the literature, the *mizdō*
> investigation (DEV_NOTES.md §17.24) showed that it can lead to over-readings:
> Case 1 of the original document claimed *\*meord-gifa* as a compound preservation,
> but no such compound is attested. The actual preservation locus for *meord* is
> a **dialectal doublet** (Anglian *meord* vs. WS *mēd*), not a compound.
>
> The general methodological point — that the FST's lautgesetzlich output should
> be checked against *all* OE evidence, not just the dominant nom.sg. simplex —
> remains valid and important. We just need to recognise multiple preservation
> loci. The cases below are now indexed by **preservation locus**, not assumed
> to be compound-based.

---

## Introduction

When a sound change has occurred and been analogically leveled away in the most frequent or most-cited form (typically the nom.sg. simplex), the lautgesetzlich form may nevertheless be preserved elsewhere. Loci where archaisms are commonly preserved include:

- **Compound first-elements** (especially as the first member of nominal compounds, where stem form is preserved and analogical pressure from inflectional paradigms is reduced) — this is the classical "Watkins principle" locus.
- **Dialectal doublets** — one OE dialect retains the lautgesetzlich form while another shows analogical leveling. Anglian forms are particularly prone to this because of conservative scribal traditions in Bede glosses, the Vespasian Psalter, and parts of the poetic corpus.
- **Oblique paradigm cells** — non-nominative cases (gen.sg., dat.sg., pl.) sometimes retain forms that the nom.sg. has lost.
- **Plurals** that resisted paradigmatic regularization.
- **Glossary lemmata and fossils** — early glossaries (Épinal, Erfurt, Corpus) sometimes preserve forms that died out before the main MS tradition.
- **Compound second elements and bound forms** that fossilized at a stage prior to subsequent simplex changes.

This pattern is phonologically regular and historically authentic — the preserved form represents what the sound changes *should* have produced, while the leveled form often reflects later analogical, paradigmatic, or dialectal pressure.

### Why This Matters for CAPR

1. **Validation of FST output**: If the FST produces a form matching an attested form *somewhere* in OE — be it a compound, an oblique cell, a dialectal variant, or a glossary lemma — that validates the FST's phonological derivation, even if the output does not match the nominative simplex of the dominant dialect.

2. **Paradigm-cell / preservation-locus targeting** (§17.16, §17.20, §17.21 precedent): Rather than forcing all entries to target the most common nominative form, we may explicitly choose paradigm cells, dialect variants, or fossil forms whose lautgesetzlich outcome can be derived by regular sound changes. This is methodologically cleaner than adding lexically-specific FST rules or skip-lists.

3. **Distinction between lautgesetzlich and analogical**: Documenting these cases makes it explicit that certain forms are *not* phonologically regular outcomes but analogical innovations — and therefore should be marked accordingly in notes or skip-lists rather than targeted as if they were regular.

4. **Disciplined verification**: The original Case 1 (mizdō) was an over-reading. To prevent recurrence, every entry below must list the **specific primary witness** (BT lemma + cited text passage, glossary citation, attested compound + source, etc.) rather than a hypothetical or handbook-only reference.

---

## Inventory

### Case 1: *mízdō (reward, wage) — meord (dialectal doublet, NOT compound)

| Field | Value |
|-------|-------|
| **PROTO** | `*mizdō` (f., strong ō-stem; PIE *misdʰ-o/eh₂-) |
| **OE FORMS** | WS **mēd** ; Anglian-leaning **meord** (dialectal doublet) |
| **Preservation locus** | **Dialectal doublet** — not a compound. The lautgesetzlich post-rhotacism + breaking output (*z → r*; *i → eo / _r+C*) is preserved as the Anglian-leaning simplex *meord*, while WS shows the post-z-loss outcome *mēd* (z-loss + comp. lengthening + lowering of long *ī to ē). |
| **Primary witnesses for meord** | (i) **BT Supplement** s.v. *meord*: OE Bede 4.17, Schipper 549.7 (form *meorde*, dat.sg.); (ii) **Bright's Anglo-Saxon Reader**, line 12498 of repo OCR — *"þæs him meorde wile ... eadge forgyldan"* (likely *Phoenix*); glossary marks "(dial.)"; (iii) **Hall's Concise** s.v. *meard*: lists *meord* as a real headword. |
| **Lautgesetzlich output** | **meord** ✓ (FST currently produces this from `*mizdō`). |
| **Sound changes** | Pathway A (rhotacism + breaking): *mizdō → *mizd > *mird > *mird+ breaking → *meord. (Plus apocope.) The WS form *mēd* arises by a different pathway: sporadic z-loss before dentals (Kroonen EDPG p. 376) with compensatory lengthening, *mizd > *mīd > *mēd. |
| **DEV_NOTES reference** | §14.518–14.760 (leornian section); §17.24 (full investigation); §17.24.7 (correction trail). Dossiers: `mismatch_dossier_mizdo.md` (with correction banner) and `mismatch_dossier_mizdo_supplement.md` (with correction banner). |
| **What was previously claimed (and is wrong)** | The original Case 1 (2026-04-25) claimed *meord* was preserved in a compound *\*meord-gifa*. **No such compound is attested anywhere in BT, BT Supplement, DOE, Hall, Bright, or any other source.** All compounds are uniformly *mēd-* (e.g. *mēd-gyfa*, *mēd-sceatt*). The compound was an agent confabulation. |
| **Methodological use** | A textbook case of dialectal-doublet preservation: WS shows the analogical/innovative outcome (or a different sound-change pathway), Anglian-leaning sources preserve the form expected from the regular sequence rhotacism + breaking. Parallel to §17.21 (swustor/swester). The TSV target may legitimately be *meord* if we adopt the dialect-relic-targeting pattern. |
| **Precedent / parallels** | §17.21 (swustor → swester, Anglian-relic target adopted); §17.20 (nafola, Anglian glossary witness); §17.16 (spere/speoru paradigm cell). Methodologically equivalent to those — but operating on **dialect** rather than **paradigm cell** or **compound** as the preservation locus. |
| **Cross-reference to Watkins-principle (compound) cases** | The mizdō case is *not* an instance of the Watkins principle as conventionally stated, because the preservation locus is not a compound. It belongs to the broader umbrella of "archaism preservation" but is methodologically distinct. |

---

### Case 2: *spéru (spear) — speoru

| Field | Value |
|-------|-------|
| **PROTO** | `*spéru` (m./n., light u-stem or reformed i-stem; PIE *sperH-) |
| **OE SIMPLEX** | `spere` (nom.sg., attested widely: Maldon, Beowulf, Ælfric; non-umlauted) |
| **OE PLURAL** | `speru` (nominative/accusative plural, common; reformed form, analogically leveled away back umlaut) |
| **OE LAUTGESETZLICH PLURAL** | `speoru` (back-umlauted plural, expected from light u-stem, attested in **Corpus Glossary** #528 *contos : speoru*, Cleopatra Glossary; Leiden compound; **Mercian, ca. 800**) |
| **OE COMPOUND STEM** | `speoru-` (Leiden Glossary *speoruliran* 'spear-muscles', Campbell §276; preserves u-stem composition form) |
| **Sound changes** | Back umlaut (*e → eo* before back vowel) in plural cell only |
| **Lautgesetzlich output** | `speoru` (FST plural form; reflects NAPl back umlaut per Brunner §139: WS analogically leveled `speoru` → `speru` under pressure from singular `spere`) |
| **Attested simplex** | `spere` (singular nominative; already leveled in pre-OE, resists umlaut analogy) |
| **DEV_NOTES reference** | §17.16 (PROTOFORM research), §17.16.12–.20 (cell-by-cell paradigm dossier: *spere/speoru*); lines 28525–30200+ |
| **Attestation status** | **Simplex universal across OE dialects; plural lautgesetzlich form attested in early glossaries (7th–8th c., Mercian); compound form attested (Leiden).** |
| **Classification** | Back umlaut preserved in plural cell and compound stem; simplex singular shows no umlaut (either pre-OE leveling or original light i-stem). |
| **Methodological use** | **PRECEDENT-SETTING CASE** (§17.16 decision): The TSV now targets the **NApl form *speoru** as a legitimate paradigm-cell choice. The FST correctly produces `speoru` via back umlaut. The case justifies the "paradigm-cell targeting" methodology: we accept `speoru` as a valid target even though the common nominative singular is `spere`. |
| **Implementation** | Row 1070 changed to target `speoru` (plural cell). This established the precedent for later cases (§17.20 *tang*, §17.21 *swester*). |

---

### Case 3: *swéstēr (sister) — swester (lautgesetzlich) vs. swustor (late-WS innovation)

| Field | Value |
|-------|-------|
| **PROTO** | `*swéstēr` (f., consonant stem, r-stem; PIE *swesor-) |
| **OE SIMPLEX (Anglian)** | `swester` (lautgesetzlich, attested in Northumbrian Ru², Ru¹, Mercian Ru¹; 9th–10th c.; nom.sg.) |
| **OE SIMPLEX (WS)** | `sweostor` (early WS, showing breaking *e → eo*); `swostor` (later leveling); **`swustor`** (late WS, **10th–11th c. only**, showing labio-velar rounding e → u after labial+velar; innovation, not lautgesetzlich) |
| **Sound changes** | Breaking (*e → eo* before labial+velar) in WS; Anglian smoothing (*eo → e* before dental t) gives *swester* |
| **Lautgesetzlich output** | `swester` (Anglian, FST: ✓ correct; no eo-umlaut in Anglian) |
| **Attested simplex** | `swuster` (late WS, post-950; Campbell §210.2n, Brunner §113 Anm. 4) — a **late-WS innovation via labio-velar rounding**, NOT lautgesetzlich |
| **DEV_NOTES reference** | §17.21 (sister PROTOFORM research, §17.21.1–.11); lines 32925–34098 |
| **Attestation status** | **Anglian swester attested 9th–10th c.; late-WS swustor attested 10th–11th c. only; WS sweostor/swostor also attested. No early/Anglian form attests swustor.** |
| **Classification** | Lautgesetzlich form *swester* (Anglian) is the regular outcome. Late-WS *swustor* is an analogical/phonological innovation (labio-velar rounding), not part of the inherited sound-change chain. |
| **Methodological use** | **ACCEPTED PRECEDENT** (§17.21.7.1, Option A). The TSV target was changed from the conventional dictionary lemma `swustor` to the lautgesetzlich Anglian form `swester`. The decision applies the **§17.16/§17.20 precedent**: when an early Anglian lautgesetzlich form is attested and the FST can produce it via regular sound changes, we target the Anglian form, not the late-WS innovation. |
| **Implementation** | Row 2192 changed from `swustor` to `swester` (nom.sg.). The FST output matches. |

---

### Case 4: *tángō (tongs) — tang (lautgesetzlich Anglian) vs. tange (analogical late)

| Field | Value |
|-------|-------|
| **PROTO** | `*tángō` (f., strong ō-stem, fem.; cognates OHG zanga, ON tǫng) |
| **OE EARLY ANGLIAN** | `tang` (nom.sg., attested in Épinal-Erfurt Glossary ca. 700, Mercian/Anglian base, as gloss for *forceps*; **lautgesetzlich apocope of trimoric -ō after heavy stem, Campbell §585**) |
| **OE LATER/WS** | `tange` (analogical restoration of nominative from accusative singular, or paradigmatic analogy; dominant in later texts; 9th c. onward) |
| **Sound changes** | Apocope (*-ō → Ø* after heavy syllable, no final vowel) in early Anglian; Analogical restoration in later WS (*-e* reintroduced) |
| **Lautgesetzlich output** | `tang` (FST: ✓ correct; no final vowel) |
| **Attested simplex** | `tange` (post-Anglian, analogical generalization; conventional dictionary lemma; most frequent form in surviving OE texts) |
| **DEV_NOTES reference** | §17.20 (paradigm cell or stem-class question; *tángō → tange*); lines 32121–32924 |
| **Attestation status** | **Early Anglian `tang` attested only in Épinal-Erfurt ca. 700; later `tange` becomes standard and dominant in later WS (9th c. onward).** |
| **Classification** | The lautgesetzlich form `tang` (early, Anglian) shows regular apocope after heavy stem. The later form `tange` is analogical (restoration of nominative vowel from weak-stem patterns). |
| **Methodological use** | **ACCEPTED PRECEDENT** (§17.20.8, Option C, Implementation §17.20.10). Like *spere/speoru* (§17.16), we target the **early Anglian lautgesetzlich form `tang`** in preference to the later-WS analogical form `tange`. This established the methodological principle: "When an early Anglian lautgesetzlich form is attested and the FST can produce it via regular sound changes, target the Anglian form." |
| **Implementation** | TSV now targets `tang` (nom.sg., early Anglian). The FST output matches. |
| **Note** | This case is the **mirror image** of §17.16: in §17.16 (*spere*), the simplex nominative is lautgesetzlich and the plural/compound show back umlaut; in §17.20 (*tang*), the simplex nominative is lautgesetzlich and later forms show analogical restoration. Both demonstrate that paradigm-cell targeting (choosing oblique/plural/early forms) is methodologically sound. |

---

### Case 5: *nábulō (navel) — nafola / nafela

| Field | Value |
|-------|-------|
| **PROTO** | `*nábulō` (f., strong ō-stem; parallel forms in Germanic: OHG *nabalo*, OS *nafla*) |
| **OE ATTESTED** | `nafola` (early, preserving medial *u → *o vowel-harmony stage); `nafela` (later WS majority, showing vowel-harmony *o → *e*) |
| **OE OBLIQUE** | `nafolan` (nom.sg./gen.sg./dat.sg./acc.sg. oblique, all showing *a*; preserved in strong n-stem declension) |
| **Sound changes** | Vowel harmony: *u → *o (medial reduction), then *o → *e (harmony with front root vowel) |
| **Lautgesetzlich output** | `nafola` (preserves the medial *u → *o stage; nom.sg. of strong n-stem shows medial-vowel preservation per §17.19) |
| **Attested simplex** | `nafela` (late WS majority, showing both vowel-harmony stages: *u → *o → *e*); `nafola` (early/rare, preserves intermediate stage) |
| **DEV_NOTES reference** | §17.19 (PROTOFORM choice *nablô* vs *nabulō*); lines c. 10800–11700 |
| **Attestation status** | **Both forms attested in OE: `nafola` earlier/rarer, `nafela` later/majority in WS.** The choice represents two stages of vowel harmony, not two different proto-forms. |
| **Classification** | Unlike *meord*, *spere*, *tangle*, this case involves **oblique paradigm cells**: the oblique forms of the n-stem all show *a (e.g., *nafolan*), which preserves the *u of the root indirectly. The nominative singular `nafola` vs. `nafela` represents two diachronic stages of vowel harmony within OE, not a pre-OE phenomenon. |
| **Methodological use** | The TSV targets `nafola` (nom.sg., early form). The decision illustrates that when vowel-harmony changes occur *within* OE (rather than as inherited pre-OE changes), targeting the earlier stage may be appropriate if it represents the lautgesetzlich pathway before analogical smoothing. Parallel to the "vowel-harmony reduction" precedents in §17.10–17.13 (breve elimination research). |
| **Implementation** | Row 2133 targets `nafola`. The FST correctly produces it from `*nabulō` via vowel harmony. |

---

### Case 6: *líznōn- (learn) — leornian

| Field | Value |
|-------|-------|
| **PROTO** | `*leznōn-` (weak class II verb; class II weak = infinitive *-ōną*, not *-ōjăną*; root *e-grade not *i-grade) |
| **OE SIMPLEX** | `leornian` (standard WS and Mercian; nom.inf.; shows breaking *e → eo* before r+C) |
| **OE DIALECT VARIANT** | North. `liornian` ~ `leornian` (variation of root vowel, pre-OE) |
| **Comparative evidence** | OHG *lernēn* ~ *lirnēn* (both e-grade and i-grade attested in OHG; variation is pre-Germanic per Campbell §123 fn.2); OFris. *lirnia* ~ *lernia* (same) |
| **Sound changes** | Z-loss/Rhotacism (*z → r*) + Breaking (*e → eo* before r+C) |
| **Lautgesetzlich output** | `leornian` (from *e-grade root `*leznōn-`) (FST: ✓ correct with corrected proto) |
| **Previous FST output** | `liernian` (from incorrect *i-grade root `*liznōn-` + i-umlaut *eo → ie*) |
| **DEV_NOTES reference** | §14.518–14.760 (OE leornian 'to learn' — ie vs eo diphthong problem); major cross-reference in mismatch_dossier_mizdo.md (Campbell §123 fn.2 citation) |
| **Attestation status** | **`leornian` standard in WS and Mercian; North. shows both *liornian* and *leornian* (pre-OE variation of ablaut grade).** |
| **Classification** | NOT a compound-archaism case, but a **proto-form correction case**: the root vowel grade is variable at the PGmc stage (attested in OHG and OFris.). WS uses the *e-grade, North. uses both. The breaking is lautgesetzlich once the correct proto-form is chosen. |
| **Methodological use** | Demonstrates that **dialectal and ablaut-grade variation in the proto-form must be resolved before sound-change derivation** (different from the *speoru* case, where both forms are derived from one proto-form via sound changes). Campbell §123 fn.2 groups *meord* with *leornian* as showing breaking—but for *leornian* to match WS, the *e-grade must be chosen at the proto stage. |
| **Implementation** | TSV now targets proto `*leznōn-` (or with class II weak morphology, infinitive `*leznōną`). FST produces `leornian` ✓. |

---

### Case 7: *fúwerō / *fūri (fire) — fȳre (dat.sg.) vs. fȳr (nom.sg.)

| Field | Value |
|-------|-------|
| **PROTO** | `*fūri` (dat.sg., locative singular; singular = u-stem or ī-stem, feminine) |
| **OE SIMPLEX (NOM.SG.)** | `fȳr` (nom.sg., attested, showing i-umlaut of *ū → *ȳ*) |
| **OE SIMPLEX (DAT.SG.)** | `fȳre` (dat.sg., showing i-umlaut plus **analogically restored** final *-e*) |
| **Sound changes** | I-umlaut (*ū → ȳ* before *i) + Apocope (final *-i → Ø* after heavy syllable) + Analogical restoration (*-e added*) |
| **Lautgesetzlich output** | `fȳr` (nom.sg., from apocope of *fȳri*) (FST: ✓ correct) |
| **Attested simplex** | `fȳre` (dat.sg., with **analogically restored** *-e*) |
| **DEV_NOTES reference** | §6.084–6.168 (OE fȳr/fȳre 'fire': Paradigm and umlaut problem); lines c. 6084–6200 |
| **Attestation status** | **`fȳr` attested (nom.sg.); `fȳre` attested (dat.sg., post-apocope restoration); both valid OE forms from different paradigm cells.** |
| **Classification** | **Paradigm-cell case**: The dat.sg. `*fūri` → `fȳre` shows a **post-apocope analogical restoration** of the dative ending *-e (generalized from other weak stems). The nom.sg. `fȳr` is the pure lautgesetzlich product. The TSV targets the dat.sg. cell (`*fūri → fȳre`) because it preserves the original singular form; it is not a compound/fossil case but a **methodological choice to target oblique cells over analogically-restored nominatives**. |
| **Methodological use** | Parallel to cow (*kūi → cȳ*), night (*naxti → niht*), hammer (*xamaras → hameres*): when the lautgesetzlich nominative singular has been analogically restored with extraneous endings, the TSV explicitly targets the oblique paradigm cell (dat.sg., gen.sg., etc.) whose lautgesetzlich outcome is derivable. |
| **Implementation** | TSV targets proto `*fūri` (dat.sg.) with target `fȳre`. The FST produces `fȳr` (nom.sg.), which is actually lautgesetzlich; the mismatch is resolved by understanding that `fȳre` is the attested dat.sg. form (post-apocope restoration). |

---

### Case 8: *rastō (rest) — ræst / ræste

| Field | Value |
|-------|-------|
| **PROTO** | `*rastōz` (gen.sg. of strong ō-stem fem.; nom.sg. is `*rastō`) |
| **OE NOM.SG.** | `rast` (expected lautgesetzlich output; but rarely attested) |
| **OE NOM.SG. (STANDARD)** | `ræst` (attested as dictionary headword; shows **paradigmatic leveling** from oblique *-æ-* stem) |
| **OE OBLIQUE (GEN.SG./ACC.SG./DAT.SG.)** | `ræste` (front vowel throughout, no A-restoration) |
| **Sound changes** | AFB (A-restoration trigger = back vowel in suffix *-u*; fires in nom.sg., blocked in obliques with front *-æ*, *-e*) |
| **Lautgesetzlich output** | `rast` (nom.sg., from A-restoration + apocope) BUT oblique cells show `ræste` (front *æ* from AFB, no restoration) |
| **Attested simplex** | `ræst` (standard headword, showing paradigmatic leveling of oblique *-æ-* back to nom.sg.) |
| **DEV_NOTES reference** | §3.097–3.399 (A-restoration in ō-stems and n-stems: ræst, tæppa, stemn); lines c. 3097–3476 |
| **Attestation status** | **`ræst` standard in OE dictionaries (BT headword); oblique forms `ræste` (gen./dat.sg.) well-attested.** The nom.sg. `rast` is lautgesetzlich but rare; `ræst` is the conventional form showing paradigmatic generalization of the oblique stem. |
| **Classification** | **Paradigm-cell case via oblique**: The oblique gen.sg. `*rastōz` → `ræste` is the lautgesetzlich output. The nom.sg. `ræst` shows **analogical leveling** from the oblique stem. This is the reverse of the *spere* case: here the oblique is lautgesetzlich and the nom.sg. is leveled, rather than the other way around. |
| **Methodological use** | Per the precedent of fire/cow/night/hammer (§3.150), the TSV can target either (a) the oblique form `*rastōz → ræste` (changing both proto and target), or (b) document `ræst` as a paradigmatic-leveling exception with an ALIGNMENT note. The decision depends on whether we prefer "pure lautgesetzlich" or "conventional attested form." |
| **Implementation** | TSV now uses gen.sg. `*rastōz`, target `ræste` (following the precedent of paradigm-cell targeting; see §3.399: "RST row 2152 (ræst) now uses genuine PGmc gen.sg. *rastōz, target ræste..."). |

---

### Case 9: *héfanaz (heaven) — heofon (lautgesetzlich WS) vs. hefēn/hefen (Anglian)

| Field | Value |
|-------|-------|
| **PROTO** | `*héβan` / `*hemĭn` (m., stem class varies by source; root *hem-*, suffix *-an* or *-in*) |
| **OE WS** | `heofon` (nom.sg., showing back umlaut *e → eo* before labial+back vowel in suffix *-on*) |
| **OE ANGLIAN** | `hefen` (showing front vowel in suffix *-en*, no back umlaut trigger) |
| **Sound changes** | Back umlaut (*e → eo* before labial+back vowel) in WS; no umlaut in Anglian (suffix has front vowel) |
| **Lautgesetzlich output** | `heofon` (WS, from back umlaut); `hefen` (Anglian, from front suffix *-en* = no umlaut) (FST WS path: ✓ correct) |
| **Attested simplex** | Both `heofon` (WS) and `hefen` (Anglian); forms represent **different suffix vowels in the paradigm**. Per Campbell §210.1, WS generalized the oblique *-un-* to the nom.sg., giving `heofon` with back umlaut. |
| **DEV_NOTES reference** | OE heofon 'heaven': Back Umlaut and Nasal Dissimilation (2026-03-20); lines 12692–13050+ |
| **Attestation status** | **Both `heofon` and `hefen` attested (dialectal); `heofon` standard in WS.** The back umlaut is **paradigmatic leveling** (oblique nominatives had *-un-*; WS generalized the back vowel to the nom.sg.). |
| **Classification** | This is primarily a **dialectal variation case**, not a compound-archaism case. However, it demonstrates the same principle: when one dialect (WS) shows back-umlauted forms and another (Anglian) shows non-umlauted forms from the same paradigm, the umlauted form is the result of paradigmatic leveling, not a simple inherited phonological change. Both forms are lautgesetzlich *given their inflectional cell and dialect*. |
| **Methodological use** | Illustrates that back umlaut (like breaking) can appear in oblique cells and later be generalized to the nominative via paradigmatic analogy. The attested result (`heofon`) is lautgesetzlich *for WS* but reflects a secondary paradigmatic process. |

---

## Pattern Analysis

### Conditioning Environments

The cases in this inventory fall into a few overlapping categories:

1. **Plural / oblique preservation** (*speoru*, *nafola* obliques)
   - Back umlaut, vowel harmony, and other changes are more conservative in plural or oblique cells.
   - Nominative singulars are more prone to analogical leveling (paradigm collapse, generalization of majority patterns).

2. **Compound stem preservation** (*speoru-*, potentially *meord-*)
   - Compounds freeze the stem in its "raw" form before final-vowel loss or syncope.
   - The first element of a compound is less influenced by morphological pressures affecting the inflected simplex.

3. **Early dialectal attestation** (*speoru* Mercian, *tang* Épinal-Erfurt, *swester* Anglian)
   - Early glossaries (7th–8th c.) preserve forms before WS dominance and leveling.
   - Anglian forms often show lautgesetzlich outcomes that WS later smoothed or reformed.

4. **Paradigm-cell selection** (*fȳre* dat.sg., *ræste* gen.sg., *nafola* n-stem nom.sg.)
   - Rather than all paradigm cells being equally leveled, some cells resist analogy.
   - Oblique cases with different suffix vowels (e.g., *-i, -æ, -ē*) trigger different sound rules and may avoid leveling.

5. **Intermediate diachronic stages** (*nafola* vs. *nafela*; *sweostor* vs. *swostor* vs. *swustor*)
   - Multiple lautgesetzlich stages occur as sound changes apply in sequence (*u → *o → *e* in vowel harmony).
   - Different OE manuscripts may preserve different stages.

### How Often Compound vs. Simplex Is Targeted

From the inventory:

| Case | Simplex targeted | Compound/oblique/plural targeted | Outcome |
|------|-----|-----|-----|
| *meord* | `mēd` (smoothed) | `meord` (fossil, weakly attested) | **Simplex targeted; compound noted but not yet verified** |
| *speoru* | `spere` (singular) | `speoru` (plural, compound) | **Plural/compound targeted** (precedent-setting) |
| *swester* | `swustor` (late WS, analogical) | `swester` (Anglian, lautgesetzlich) | **Anglian lautgesetzlich targeted** |
| *tang* | `tange` (analogical) | `tang` (early Anglian, apocope) | **Early form targeted** |
| *nafola* | `nafela` (late, vowel harmony) | `nafola` (early, intermediate stage) | **Early stage targeted** |
| *leornian* | `leornian` (WS, *e-grade) | — | **Correct proto (*e-grade) targeted; derivation is lautgesetzlich** |
| *fȳre* | `fȳr` (nom.sg., lautgesetzlich) | `fȳre` (dat.sg., post-apocope restoration) | **Oblique cell targeted** |
| *ræst* | `rast` (lautgesetzlich nom.sg.) | `ræste` (oblique, lautgesetzlich) | **Oblique cell targeted** |
| *heofon* | `heofon` (WS, back umlaut) | — | **WS form targeted; paradigmatic leveling origin acknowledged** |

**Pattern**: When we follow the **§17.16/§17.20/§17.21 precedent**, we increasingly target compounds, plurals, and oblique cells that are lautgesetzlich, rather than forcing all entries to match the most frequent nominative singular. This reflects a deeper principle: **the FST should be allowed to produce forms that match attested cells within the paradigm**, even if not the most common cell.

### Consistency of Approach

**Precedent established by §17.16, §17.20, §17.21:**

- **§17.16** (*spere/speoru*): Accept plural `speoru` as a valid target when it is lautgesetzlich.
- **§17.20** (*tángō*): Target early-Anglian lautgesetzlich `tang` (apocope), not later-WS analogical `tange`.
- **§17.21** (*swester*): Target lautgesetzlich Anglian `swester`, not late-WS innovation `swustor`.

These three cases establish a **methodological precedent** that should be applied consistently:

1. **If a form is lautgesetzlich and attested (in any paradigm cell, dialect, or period), it deserves consideration as a target.**
2. **If a form is analogical or post-OE innovation, it should be marked as such and may be skipped or documented as an exception.**
3. **Paradigm-cell targeting is legitimate**: rather than forcing all entries to match the nominative singular, we may deliberately choose oblique cells (gen.sg., dat.sg.), plural forms, or early-dialectal attestations when they represent unbroken chains of lautgesetzlich sound changes.

---

## Methodological Implications for *meord / mēd*

> ⚠️ **Correction (2026-04-26)** — This entire section was written under the
> incorrect assumption that the preservation locus for *meord* might be a
> compound (*\*meord-gifa*). The compound is unattested. The simplex *meord*
> however **is** attested as a dialectal doublet (see Case 1 above for primary
> witnesses). Specific corrections to claims in the discussion below:
>
> - Line 293: "*meord* is rare in the simplex but preserved in compounds" — wrong.
>   *meord* is preserved as a dialectal-doublet simplex (Anglian-leaning sources),
>   not in compounds. No compounds of *meord-* exist.
> - Line 295: "*meord-* fossil compounds … structure identical to *speoru-*" — false.
>   No such compounds exist.
> - Line 299–301: "no clear attested plural/compound form" / "no dialectal split
>   (Anglian *meord*, WS *mēd*)" — second clause contradicts first; the truth is
>   that there *is* a dialectal split, with *meord* preserved in Anglian-leaning
>   simplex attestation (BT Suppl., Bright). Lines 299 and 301 are wrong.
> - Line 313: framing the mismatch as evidence of "paradigmatic and analogical
>   leveling" — partially correct, but the cleaner framing is that two sound-change
>   pathways operated (Pathway A rhotacism+breaking → meord; Pathway B z-loss+
>   comp.lengthening+lowering → mēd), each preserved in different dialects.
> - Decision matrix (line 326): "Attested (any form)? — Uncertain" should be
>   **Yes** (Anglian-leaning simplex; primary witnesses listed in Case 1).
> - Decision matrix (line 330): "Target simplex `mēd` (for now)" — the *meord*
>   case now has the same evidentiary standing as *swester* (§17.21). The TSV
>   target may legitimately be switched to *meord*.
>
> The paragraphs below are kept verbatim as a record of the original (flawed)
> reasoning. The substantive analysis is now in DEV_NOTES.md §17.24.7 and in
> the revised Case 1 above.

The *meord* case is currently **under active research** (mismatch_dossier_mizdo.md) and illustrates the decision criteria for the Watkins principle in CAPR.

### The Central Question

Is *meord* (lautgesetzlich outcome of breaking *i before r+C) attested in fossil compounds (e.g., *meord-gifa* 'reward-giver')? If so, should we:

1. **Accept *meord* as evidence for the lautgesetzlich derivation**, even though the simplex is always `mēd`?
2. **Keep the target as `mēd`** (smoothed form) and document the mismatch?
3. **Switch to a compound/fossil form** as the explicit target (unlikely, but theoretically possible)?

### Analysis

**Similarities to precedent cases:**

- Like *speoru* (plural form): *meord* is rare in the simplex but preserved in compounds.
- Like *leornian*: Campbell §123 fn.2 explicitly groups *meord* with *leornian*, both showing breaking of *e before r+C.
- Like *meord-* fossil compounds: the structure (compound stem preserving archaic form) is identical to *speoru-* in *speoruliran*.

**Differences from precedent cases:**

- Unlike *speoru*, we have **no clear attested plural/compound form**—*meord-gifa* is hypothetical and requires DOE/BT verification.
- Unlike *leornian*, the simplex `mēd` is **universally attested** across all OE dialects with no dialectal split (Anglian *meord*, WS *mēd*).
- Unlike *tang*/*tange*, the analogical smoothing happened **pre-OE or very early OE** (before the major dialect split), so all documented OE shows `mēd`, not `meord`.

### Recommended Approach

**Pending verification of fossil compounds:**

1. **Execute a targeted search** in DOE and Bosworth-Toller for compounds like *meord-gifa*, *meord-lēan*, *meord-* (any construction).
   - If fossil compounds are verified, *meord* becomes as legitimate as *speoru* (even if rare).
   - If not found, the case remains a **hypothetical lautgesetzlich form** preserved only in the simplex's indirect phonological evidence.

2. **Acknowledge the mismatch explicitly:**
   - The TSV note should state: "Simplex `mēd` shows post-breaking smoothing and r-loss; lautgesetzlich form `meord` (from breaking of *i before r+C, per Campbell §123 fn.2) is attested in fossil compounds (verify in DOE) or inferred from comparative evidence."
   - This frames the mismatch not as a failure, but as evidence of **paradigmatic and analogical leveling** within OE.

3. **Consider the precedent pathway:**
   - If §17.16/§17.20/§17.21 are to be **consistently applied**, a strong argument can be made that *meord* (if verified in compounds) deserves the same treatment as *speoru*: accept it as a valid paradigm-cell output.
   - However, without clear compound attestation, the case remains **analogous but not identical** to the precedent cases.

### Decision Framework

Use this **decision matrix** for similar cases:

| Criterion | *speoru* | *tang* | *swester* | *meord* |
|-----------|----------|--------|-----------|---------|
| **Lautgesetzlich?** | Yes (back umlaut) | Yes (apocope) | Yes (breaking + Anglian smoothing) | Yes (breaking) |
| **Attested (any form)?** | Yes (plural, Corpus Glossary; compound, Leiden) | Yes (early Anglian, Épinal-Erfurt) | Yes (Anglian, early OE) | Uncertain (simplex yes; compounds unverified) |
| **Early/Anglian?** | Yes (Mercian, ca. 800) | Yes (ca. 700) | Yes (ca. 9th c.) | Possibly (glossaries, if compounds exist) |
| **Simplex shows leveling?** | Yes (from *speoru* → *speru*) | Yes (from *tang* → *tange*) | Yes (from *swester* → *swustor*) | Yes (from `meord` → `mēd` via smoothing) |
| **Precedent applied?** | ✓ Yes (§17.16) | ✓ Yes (§17.20) | ✓ Yes (§17.21) | ? Pending verification |
| **TSV target decision** | Target plural `speoru` | Target early `tang` | Target Anglian `swester` | Target simplex `mēd` (for now); flag for review if compounds verified |

---

## Summary and Conclusion

The **Watkins principle** is well-attested in the CAPR documentation and has become a precedent-setting part of our methodology in §17.16 (spere), §17.20 (tang), and §17.21 (swester).

**Key findings:**

1. **Multiple cases show lautgesetzlich forms preserved in compounds, plurals, obliques, or early attestations** while the simplex nominative is leveled or smoothed.

2. **This is not a defect in the FST**, but evidence that the FST is correctly applying sound changes to get the "expected" form—which then matches attested compounds or oblique cells.

3. **The methodology is consistent**: We apply a "2D search" (proto-form cell × attested OE form) to find the longest unbroken chain of lautgesetzlich sound changes, and target *that* combination, even if it is not the most frequent nominative singular.

4. **The *meord* case** is the live test case: if fossil compounds *meord-* can be verified, it becomes precedent-strength evidence for accepting lautgesetzlich forms in compounds. If not, it remains a **hypothetical reconstruction** that we can flag in notes without targeting it.

5. **The principle applies broadly**: Every word showing a discrepancy between FST output and TSV target should be examined for whether a lautgesetzlich form exists *somewhere* in the paradigm or compound morphology. If it does, the case is a feature, not a bug.

---

**References and Cross-links:**

- DEV_NOTES.md §17.16 (spere / speoru precedent)
- DEV_NOTES.md §17.20 (*tángō / tang precedent)
- DEV_NOTES.md §17.21 (swester / swustor precedent)
- analysis/mismatch_dossier_mizdo.md (meord research dossier)
- Campbell, A. 1959. *Old English Grammar*. §§123, 146, 210, 255–256, 584–592.
- Ringe, D. & Taylor, A. 2014. *The Development of Old English*. Vol. 2.
- Brunner, K. 1965. *Altenglische Grammatik*. 3. Aufl.

---

**Document status:** REFERENCE (No TSV/FST changes proposed by this inventory; it consolidates existing research for guidance on future decisions.)

