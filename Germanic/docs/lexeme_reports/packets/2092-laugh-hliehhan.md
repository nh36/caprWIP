# Evidence packet — 2092 laugh / hliehhan

> This packet is evidence for drafting. Do not treat all hits as equally authoritative; prefer high-confidence evidence.

## TSV row data

| ID | CONCEPT | COUNTERPART | PROTO | PROTOFORM | DERIVATION_CLASS | NOTE | HISTORY |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2092 | laugh | hliehhan | *lákaną | *xláxjaną | early_analogy | §17.40: target hlæhhan → hliehhan (WS form per Bright p.597, Brunner §392,4; Anglian hlæhhan attested as variant — cascade defaults to WS). Added *x to PWGmcJGemination per Fulk §6.15. \| R/T: PGmc *hlahjanan > OE hlæhhan/hliehhan | - |

## Manifest status

_No manifest entry._

## High-confidence evidence

### Compact derivation trace entry

```md
# laugh
PROTO: *xláxjaną
EXPECTED: hliehhan
OUTPUTS: hliehhan



### Proto-Germanic consonant inheritance

Proto Input: *xláxjaną

| Earlier Germanic developments | Old English developments |
|:---|:---|
| **Proto-West Germanic**<br>PWGmc J Gemination: *xláxxjaną<br><br>**Northwest Germanic**<br>[no change] | **Old English**<br>Anglo Frisian Brightening: *xlæxxjaną<br>OE Breaking: *xleaxxjaną<br>OE Velar Fricative Palatalization: *xleaxçjaną<br>OE Heavy Syllable Nasal Apocope: *xleaxçjan<br>OE Secondary Nasalization: *xleaxçjąn<br>OE I Umlaut: *xliexçjąn<br>OE Weak Tail Reduction: *xliexçjan<br>OE J Loss After Heavy: *xliexçan |



### Orthography & surface

Old English Orthography: h*liehhan
Outcome: hliehhan

NOTE: §17.40: target hlæhhan → hliehhan (WS form per Bright p.597, Brunner §392,4; Anglian hlæhhan attested as variant — cascade defaults to WS). Added *x to PWGmcJGemination per Fulk §6.15. | R/T: PGmc *hlahjanan > OE hlæhhan/hliehhan
```

### Matching oe_known_problems.tsv entries

_None_

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:38962 (exact pair)

- Nearby heading: ### FST probe matrix (current bins, before fix)

```text
38960: 
38961: ```
38962: *xláxjaną → hliehhan  ✓  (with *x gemination: breaking → hleahh,
38963:                           i-umlaut → hliehh, j-loss → hliehhan)
38964: ```
```

#### Germanic/docs/DEV_NOTES.md:38977 (row ID)

- Nearby heading: ### Plan

```text
38975:    comment citing Fulk §6.15.
38976: 
38977: 2. **TSV row 2092 (Old_English / laugh):** change COUNTERPART
38978:    `hlæhhan` → `hliehhan`. IPA segment column updated `h l æ h h a n`
38979:    → `h l i e h h a n`. Note: "§17.40 — WS form (Bright; Brunner
```

#### Germanic/docs/DEV_NOTES.md:39302 (exact pair)

- Nearby heading: #### 6. Corpus rows that depend on the current loss rule

```text
39300: 
39301: **`*xj` (the bug case):**
39302: - 2092 `*xláxjaną` → `hliehhan` (expected). After gemination →
39303:   `*xláxxjaną`; current rule deletes the first `*x` because the right
39304:   context `*x*j` matches `CC`. This is the only *xj row in the
```

#### Germanic/docs/DEV_NOTES.md:39310 (row ID)

- Nearby heading: #### 6. Corpus rows that depend on the current loss rule

```text
39308: options (a) and (c), if restricted carefully, leave row 2015
39309: (`*fúnxstiz → fȳst`) intact — that is the single row depending on
39310: the rule firing — while sparing row 2092.
39311: 
39312: #### 7. Recommendation summary
```

#### Germanic/docs/DEV_NOTES.md:39324 (exact pair)

- Nearby heading: #### 7. Recommendation summary

```text
39322: one row that requires the loss rule to fire (*fúnxstiz → fȳst*, an
39323: *xs+C case) and exactly one row where the rule mis-fires after the
39324: recent gemination fix (*xláxjaną → hliehhan*); all other *xC rows
39325: are inert with respect to this rule. Three fix options have been
39326: laid out without a recommendation: (a) narrow the right context to
```

#### Germanic/docs/DEV_NOTES.md:39368 (exact pair)

- Nearby heading: ### Iteration 2 — fix implemented

```text
39366: 
39367: Verification:
39368: - `*xláxjaną` → `hliehhan` ✓ (was: hliehan)
39369: - `*fúnxstiz` → `fȳst` ✓ (the only corpus row depending on the loss
39370:   rule firing; preserved because *s is the first non-*x consonant)
```

### Analysis and dossier hits

#### Germanic/docs/analysis/four_complex_tsv_items.md:19 (row ID)

- Nearby heading: ## 1. *xlaxjăną → hlæhhan "laugh" (ID 2092)

```text
18: 
19: ## 1. *xlaxjăną → hlæhhan "laugh" (ID 2092)
20: 
```

## Supporting/background evidence

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:342 (note keyword: Anglian)

- Nearby heading: # Block if stressed syllable (first syllable) contains *u

```text
340:    - `*wúduwōn` → `wuduwe` (medial `u` preserved, not lowered to `o`)
341: 
342: 3. **Syncopation** in Anglian:
343:    - `*wuduwā` → `widwe` (Mercian), `widua` (Northumbrian)
344: 
```

#### Germanic/docs/DEV_NOTES.md:415 (note keyword: Anglian)

- Nearby heading: ### Paradigm-cell analysis: Where does `widwe` come from? (2026-03-21)

```text
413: removing the triggering `*u`, so back mutation couldn't apply.
414: 
415: **Possible explanations for Mercian/Anglian `widwe`:**
416: 
417: 1. **Pre-OE dialectal syncopation**: Some Northwest Germanic dialects may have 
```

#### Germanic/docs/DEV_NOTES.md:464 (note keyword: Anglian)

- Nearby heading: ### Paradigm-cell analysis: Where does `widwe` come from? (2026-03-21)

```text
462: |------|------------------------|-------|
463: | `wuduwe` | *widuwō → back mutation → *wuduwō → wuduwe | **WS regular** |
464: | `widwe` | *widuwō → early syncopation → *widwō → widwe | **Anglian/Mercian** |
465: | `widuwe` | `widwe` + analogical vowel restoration → widuwe | **Analogical** (Luick) |
466: | `widua` | = `widuwa` → widua | **Northumbrian** (no syncopation, no BM) |
```

#### Germanic/docs/DEV_NOTES.md:477 (note keyword: Anglian)

- Nearby heading: ### Paradigm-cell analysis: Where does `widwe` come from? (2026-03-21)

```text
475: dialectal developments:
476: - WS: no early syncopation → back mutation applies → `wuduwe`
477: - Anglian: early syncopation → back mutation can't apply → `widwe`
478: 
479: The form `widuwe` is **analogical** — a compromise between the syncopated Anglian
```

#### Germanic/docs/DEV_NOTES.md:479 (note keyword: Anglian)

- Nearby heading: ### Paradigm-cell analysis: Where does `widwe` come from? (2026-03-21)

```text
477: - Anglian: early syncopation → back mutation can't apply → `widwe`
478: 
479: The form `widuwe` is **analogical** — a compromise between the syncopated Anglian
480: `widwe` and the full three-syllable structure expected from the etymology.
481: 
```

#### Germanic/docs/DEV_NOTES.md:483 (note keyword: Anglian)

- Nearby heading: ### Paradigm-cell analysis: Where does `widwe` come from? (2026-03-21)

```text
481: 
482: **For the FST:** Target `wuduwe` as the regular WS outcome. The FST cannot model
483: the early Anglian syncopation (which may be a dialectal retention from NWGmc or
484: a sequence-specific contraction), nor the subsequent analogical restoration to
485: `widuwe`.
```

#### Germanic/docs/DEV_NOTES.md:38878 (exact COUNTERPART)

- Nearby heading: ### Mismatch as observed

```text
38876: Two things are off:
38877: 
38878: 1. The medial /h/ is single (`hliehan`), not geminate (`hliehhan` /
38879:    `hlæhhan`). WGmc j-gemination did not fire on *x.
38880: 2. The vowel diphthong is `ie` (West Saxon i-umlaut of `ea` from
```

#### Germanic/docs/DEV_NOTES.md:38895 (exact PROTOFORM)

- Nearby heading: ### Trace (post-§17.39)

```text
38893: ```
38894: 
38895: The gap: between `*xláxjaną` and the first stage that shows it
38896: (FinalSchwaApocope), the cascade has applied breaking and
38897: x-palatalisation but **not** WGmc j-gemination. The geminate /xx/
```

#### Germanic/docs/DEV_NOTES.md:38898 (exact COUNTERPART)

- Nearby heading: ### Trace (post-§17.39)

```text
38896: (FinalSchwaApocope), the cascade has applied breaking and
38897: x-palatalisation but **not** WGmc j-gemination. The geminate /xx/
38898: required for both the WS `hliehhan` and the Anglian `hlæhhan` is
38899: missing.
38900: 
```

#### Germanic/docs/DEV_NOTES.md:38912 (exact COUNTERPART)

- Nearby heading: ### Source audit

```text
38910: **Brunner Altenglische Grammatik §392, 4** (and §95 Anm. 7):
38911: 
38912: > Urspr. hj erscheint so als hh in ws. hliehhan lachen … nordh.
38913: > hlæhha … angl. hlæhhan; ws. hliehhan, aber nordh. hlæhhan nach
38914: > dem Subst.
```

#### Germanic/docs/DEV_NOTES.md:38913 (exact COUNTERPART)

- Nearby heading: ### Source audit

```text
38911: 
38912: > Urspr. hj erscheint so als hh in ws. hliehhan lachen … nordh.
38913: > hlæhha … angl. hlæhhan; ws. hliehhan, aber nordh. hlæhhan nach
38914: > dem Subst.
38915: 
```

#### Germanic/docs/DEV_NOTES.md:38916 (exact COUNTERPART)

- Nearby heading: ### Source audit

```text
38914: > dem Subst.
38915: 
38916: (Original *hj appears as *hh in WS hliehhan; Anglian/Northumbrian
38917: hlæhhan; the dialect split is well-known.)
38918: 
```

#### Germanic/docs/DEV_NOTES.md:38919 (exact COUNTERPART)

- Nearby heading: ### Source audit

```text
38917: hlæhhan; the dialect split is well-known.)
38918: 
38919: **Brunner §391, 3 / §511** (paradigm) lists `hlæhhan stv. s. hliehhan`
38920: — the Anglian form is cross-referenced to the WS lemma `hliehhan`.
38921: 
```

#### Germanic/docs/DEV_NOTES.md:38955 (exact PROTOFORM)

- Nearby heading: ### FST probe matrix (current bins, before fix)

```text
38953: 
38954: ```
38955: *xláxjaną → hliehan   ✗  (current; missing *x gemination → single h;
38956:                           breaking + i-umlaut applied → ie)
38957: ```
```

### Analysis and dossier hits

#### Germanic/docs/analysis/compound_archaism_inventory.md:14 (note keyword: Anglian)

- Nearby heading: # Archaism Preservation Inventory: Where Lautgesetzlich Forms Survive in OE

```text
13: > but no such compound is attested. The actual preservation locus for *meord* is
14: > a **dialectal doublet** (Anglian *meord* vs. WS *mēd*), not a compound.
15: >
```

#### Germanic/docs/analysis/compound_archaism_inventory.md:29 (note keyword: Anglian)

- Nearby heading: ## Introduction

```text
28: - **Compound first-elements** (especially as the first member of nominal compounds, where stem form is preserved and analogical pressure from inflectional paradigms is reduced) — this is the classical "Watkins principle" locus.
29: - **Dialectal doublets** — one OE dialect retains the lautgesetzlich form while another shows analogical leveling. Anglian forms are particularly prone to this because of conservative scribal traditions in Bede glosses, the Vespasian Psalter, and parts of the poetic corpus.
30: - **Oblique paradigm cells** — non-nominative cases (gen.sg., dat.sg., pl.) sometimes retain forms that the nom.sg. has lost.
```

#### Germanic/docs/analysis/compound_archaism_inventory.md:56 (note keyword: Anglian)

- Nearby heading: ### Case 1: *mízdō (reward, wage) — meord (dialectal doublet, NOT compound)

```text
55: | **PROTO** | `*mizdō` (f., strong ō-stem; PIE *misdʰ-o/eh₂-) |
56: | **OE FORMS** | WS **mēd** ; Anglian-leaning **meord** (dialectal doublet) |
57: | **Preservation locus** | **Dialectal doublet** — not a compound. The lautgesetzlich post-rhotacism + breaking output (*z → r*; *i → eo / _r+C*) is preserved as the Anglian-leaning simplex *meord*, while WS shows the post-z-loss outcome *mēd* (z-loss + comp. lengthening + lowering of long *ī to ē). |
```

#### Germanic/docs/analysis/four_complex_tsv_items.md:35 (exact COUNTERPART)

- Nearby heading: ### OE target assessment

```text
34: 
35: The TSV has `hlæhhan`. R/T give the WS form as **hliehhan** (lines 3674, 10264,
36: 13896, 19594) and the Anglian poetic form as **hlehhan** (line 13897). The form
```

#### Germanic/docs/analysis/four_complex_tsv_items.md:40 (exact COUNTERPART)

- Nearby heading: ### OE target assessment

```text
39: R/T's derivation (line 10264):
40: > PGmc \*hlahjana > PWGmc \*hlahh'an > \*hlehh'an > \*hleahh'an > OE hliehhan
41: 
```

#### Germanic/docs/analysis/meord_med_chronological_review.md:133 (note keyword: Anglian)

- Nearby heading: ### 2.4 Brunner, *Altenglische Grammatik* (3rd ed. 1965, after Sievers)

```text
132: 
133: **Position.** Brunner explicitly characterises *meord* as **Anglian and
134: poetic**, with the diphthong *eo* arising from the breaking-style
```

#### Germanic/docs/analysis/meord_med_chronological_review.md:139 (note keyword: Anglian)

- Nearby heading: ### 2.4 Brunner, *Altenglische Grammatik* (3rd ed. 1965, after Sievers)

```text
138: uniformly under *mēd-*, consistent with Brunner treating *meord* as
139: the Anglian/poetic doublet member.
140: 
```

#### Germanic/docs/analysis/meord_med_chronological_review.md:546 (note keyword: Anglian)

- Nearby heading: ### 2.17 Kilday, "Crist's Law, Smith's Law, and English *wizen*" (2024 draft)

```text
545: this distribution claim; the cited primary attestations in §1 above
546: are all from Anglian-leaning texts (Bede translation, Phoenix,
547: Gregory's Dialogues), consistent with Kilday but not strictly proving
```

#### Germanic/docs/analysis/notable_findings.md:1470 (note keyword: Anglian)

- Nearby heading: ## 10. OE rēc 'smoke': the missing WS rīec problem

```text
1469: OS rōk, OHG rouh, OFris rēk). The OE outcome is universally `rēc`,
1470: attested across all dialects and all periods (Anglian glosses, early
1471: WS, late WS, Kentish; 8th–11th c.). The expected West Saxon i-umlaut
```

#### Germanic/docs/analysis/notable_findings.md:1544 (note keyword: Anglian)

- Nearby heading: ## 10. OE rēc 'smoke': the missing WS rīec problem

```text
1543:   multiple regular outcomes; back-formation from the verb;
1544:   early-monophthongization of WS īe in this lexeme; Anglian → WS
1545:   borrowing. None of these fit the evidence as cleanly as H1, H2,
```

#### Germanic/docs/analysis/notable_findings.md:1550 (note keyword: Anglian)

- Nearby heading: ## 10. OE rēc 'smoke': the missing WS rīec problem

```text
1549: `Germanic/data/oe_known_problems.tsv` (status `wontfix`, category
1550: `smoothing_anglian_relic`). The earlier H1 recommendation (*rōkiz) is
1551: **withdrawn**.
```

#### Germanic/docs/analysis/ws_vs_anglian_dialect_differences.md:1 (note keyword: Anglian)

- Nearby heading: # West Saxon vs. Anglian: dialect differences in Old English

```text
1: # West Saxon vs. Anglian: dialect differences in Old English
2: 
```

#### Germanic/docs/analysis/ws_vs_anglian_dialect_differences.md:31 (note keyword: Anglian)

- Nearby heading: ## 1. Smoothing (Anglian monophthongisation before velars)

```text
30: 
31: ## 1. Smoothing (Anglian monophthongisation before velars)
32: 
```

#### Germanic/docs/analysis/ws_vs_anglian_dialect_differences.md:37 (note keyword: Anglian)

- Nearby heading: ## 1. Smoothing (Anglian monophthongisation before velars)

```text
36: It does **not** apply before dental clusters or non-velar environments. It
37: is the diagnostic Anglian feature.
38: 
```

#### Germanic/docs/dossiers/bugan-scufan-paradigm-cell-review.md:156 (note keyword: Anglian)

- Nearby heading: ## §3. The fault-line: `-un > -on` for stem-`u` verbs is analogical

```text
155:   Brunner §364.2 Anm. 4). For the two specific verbs we care about
156:   here, the early Anglian/Mercian witnesses simply do not contain
157:   a finite 3 pl. pret. token — the verb is unattested in those
```

#### Germanic/docs/dossiers/bugun-scufun-attestation.md:117 (note keyword: Anglian)

- Nearby heading: ### Direct corpus attestations

```text
116: 
117: The early Anglian/Mercian texts that *would* show `-un` if they
118: preserved this verb in 3 pl. pret. — the Épinal, Erfurt, and Corpus
```

#### Germanic/docs/dossiers/bugun-scufun-attestation.md:125 (note keyword: Anglian)

- Nearby heading: ### Direct corpus attestations

```text
124: i.e. weak `bīegan` 'to bend (something)', not the strong intransitive
125: `būgan`.) The `-un` Anglian preterite-plurals well-attested for other
126: verbs (e.g. VP `forleortun`, `fornōmun`, `āwoestun`, `gnornadun`,
```

#### Germanic/docs/dossiers/bugun-scufun-attestation.md:178 (note keyword: Anglian)

- Nearby heading: ### Local handbook evidence

```text
177: **Bülbring §302** (`bulbring_altenglisches_elementarbuch.txt`, line
178: 6031–6033) gives the **only Anglian/Northumbrian** pret. pl.
179: attestation of this verb that I can locate in the handbook tradition:
```

#### Germanic/docs/dossiers/un-to-on-chronology.md:183 (note keyword: Anglian)

- Nearby heading: ### Luick §326

```text
182:    -on` is, on Luick's account, the **same Lautgesetz** as that which
183:    produces `heafod` from `*hēafud`. (Anglian `wērun`, `heafud`,
184:    `wuldur`, `leofuste` confirm the Anglian retention pattern.)
```

#### Germanic/docs/dossiers/un-to-on-chronology.md:184 (note keyword: Anglian)

- Nearby heading: ### Luick §326

```text
183:    produces `heafod` from `*hēafud`. (Anglian `wērun`, `heafud`,
184:    `wuldur`, `leofuste` confirm the Anglian retention pattern.)
185: 
```

#### Germanic/docs/dossiers/un-to-on-chronology.md:358 (note keyword: Anglian)

- Nearby heading: ## Chronology

```text
357: 
358: The dialect distribution is clear: Mercian (Anglian) preserves `-un`
359: robustly into the 10th c.; West Saxon shifts to `-on` by the early 9th
```

#### Germanic/docs/dossiers/widuwe-u-preservation.md:28 (note keyword: Anglian)

- Nearby heading: ## §1. TL;DR

```text
27:    outcomes from PGmc *widuwōn- are:
28:    * **Anglian:** `widwe` (regular early syncope of medial `*u`).
29:    * **West Saxon:** `wuduwe` (combinative u-umlaut / "verstärkter
```

#### Germanic/docs/dossiers/widuwe-u-preservation.md:130 (note keyword: Anglian)

- Nearby heading: #### §114b — explicit "widuwe is analogical"

```text
129: 
130: Translation: "Anglian **widwe** (L, Rit., R², Vesp. Ps.) beside WS
131: **wuduwe** 'widow' is to be explained by early syncope. By analogical
```

#### Germanic/docs/dossiers/widuwe-u-preservation.md:138 (note keyword: Anglian)

- Nearby heading: #### §114b — explicit "widuwe is analogical"

```text
137: **analogical / leveled** forms, not as direct Lautgesetz reflexes.
138: The two Lautgesetz outcomes are: Anglian `widwe` (with syncope) and
139: WS `wuduwe` (with combinative u-umlaut of root `wi → wu` and medial
```

### Local lexical-table hits

#### old_english_wiktionary.tsv

| ENGLISH | OE_FORM | SOURCE | DETAIL | PAGE |
| :--- | :--- | :--- | :--- | :--- |
| laugh | hlæhhan | inh | template:inh | laugh |

#### old_english_swadesh.tsv

| NUMBER | ENGLISH | OLD_ENGLISH | IPA_RAW |
| :--- | :--- | :--- | :--- |
| 100 | to laugh | hliehhan | /ˈhl̥iy̯ç.çɑn/ |

## Possibly stale or diagnostic evidence

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:38865 (exact PROTOFORM)

- Nearby heading: ## §17.40 *xláxjaną → hliehan (expected hlæhhan): missing *x gemination + WS/Anglian target choice

```text
38863: 
38864: 
38865: ## §17.40 *xláxjaną → hliehan (expected hlæhhan): missing *x gemination + WS/Anglian target choice
38866: 
38867: ### Mismatch as observed
```

#### Germanic/docs/DEV_NOTES.md:38872 (exact PROTOFORM)

- Nearby heading: ### Mismatch as observed

```text
38870: 
38871: ```
38872: *xláxjaną -> hliehan (expected hlæhhan)
38873: >> ISSUE: Breaking difference plus consonant skeleton mismatch
38874: ```
```

#### Germanic/docs/DEV_NOTES.md:38924 (concept name)

- Nearby heading: ### Source audit

```text
38922: **Bright Anglo-Saxon Reader p.597:**
38923: 
38924: > hliehhan (<*hleahjan, 9 <*hlæhjan; Goth. hlahjan), to laugh.
38925: 
38926: **Bosworth-Toller** s.v. *hlihhan*: "Take here hlehhan in Dict.,
```

#### Germanic/docs/DEV_NOTES.md:38927 (concept name)

- Nearby heading: ### Source audit

```text
38925: 
38926: **Bosworth-Toller** s.v. *hlihhan*: "Take here hlehhan in Dict.,
38927: and add: I. to laugh"; lists `hlehhan, hlihhan, hlæhhan, hlyhhan`
38928: as variants. WS lemma is `hliehhan`.
38929: 
```

#### Germanic/docs/DEV_NOTES.md:38946 (exact PROTOFORM)

- Nearby heading: ### Diagnosis

```text
38944: 2. **TSV target.** The cascade applies WS-style breaking and
38945:    i-umlaut by default (cf. §17.37 *wéslōn, §17.38 *wéstanē, etc.),
38946:    so the lawful surface output of `*xláxjaną` after the gemination
38947:    fix should be the WS form `hliehhan`, not the Anglian `hlæhhan`.
38948:    The TSV row has the Anglian target. Per project precedent
```

#### Germanic/docs/DEV_NOTES.md:39140 (concept name)

- Nearby heading: #### 2. Geminate *xx vs. heterorganic *xCC

```text
39138: - **Fulk §6.15** (the rule citation already in `germanic.txt:1539`)
39139:   covers the gemination side, with `Olcel. geyja 'bark'`-type examples
39140:   and explicit *x in `Go. hlahjan ‘laugh' (ON hlæja, OE hlihhan <
39141:   *hliehhan)` (`fulk_comparative_grammar_early_germanic.vision.txt:16597`).
39142: 
```

### Analysis and dossier hits

#### Germanic/docs/analysis/mismatch_dossier_mizdo.md:13 (note keyword: Anglian)

- Nearby heading: # Mismatch Dossier: *mízdō 'reward, wage'

```text
12: >   Reader (in a poetic line, glossed as "(dial.)"), and Hall's Concise Dictionary.
13: >   It is a dialectal (Anglian-leaning) variant of WS *mēd*.
14: >
```

#### Germanic/docs/analysis/mismatch_dossier_mizdo.md:69 (note keyword: Anglian)

- Nearby heading: ### 2.1 Standard dictionary lemmata

```text
68: - Lemma: **mēd** (primary)
69: - Variant: **meord** (marked as early/Anglian, rare in simplex but preserved in compounds)
70: 
```

#### Germanic/docs/analysis/mismatch_dossier_mizdo.md:89 (note keyword: Anglian)

- Nearby heading: #### Form B: `meord` (diphthong eo, with medial /r/)

```text
88: 1. **Early glossaries** (7th–8th century):
89:    - **Épinal-Erfurt Glossary** (ca. 700, Mercian/Anglian base): no direct attestation of the simplex found, but compound forms suggest *meord-*
90:    - **Corpus Glossary** (ca. 800, Mercian): potential attestation (requires verification)
```

#### Germanic/docs/analysis/mismatch_dossier_mizdo_supplement.md:22 (note keyword: Anglian)

- Nearby heading: # Supplement to Mismatch Dossier: *mízdō 'reward, wage'

```text
21: > **withdrawn**. Kroonen's "(dialectally dependent?) doublet *méd : meord*"
22: > (EDPG p. 376) reflects genuine primary attestation in Anglian-leaning sources.
23: > The handbook agreement reflects shared evidence, not lexicographic recycling.
```

#### Germanic/docs/analysis/mismatch_dossier_mizdo_supplement.md:524 (note keyword: Anglian)

- Nearby heading: ### 5.1 The *rēc case (notable_findings.md #10)

```text
523: - **Attested outcome**: **rēc** (long ē monophthong, **no diphthong**)
524: - **Distribution**: **Universal across all OE dialects** (Anglian, WS, Kentish, Northumbrian)
525: 
```

## Bibliography-key candidates

### Preferred candidates

| Key | Why it was selected |
| :--- | :--- |
| Luick1914 | single available key for Luick |
| BrightCassidyRingler1971 | single available key for Bright |
| Fulk2018 | single available key for Fulk |
| Kilday2024 | single available key for Kilday |

### Low-confidence candidates

_None_

