# Evidence packet — 2310 make (3sg) / macaþ

> This packet is evidence for drafting. Do not treat all hits as equally authoritative; prefer high-confidence evidence.

## TSV row data

| ID | CONCEPT | COUNTERPART | PROTO | PROTOFORM | DERIVATION_CLASS | NOTE | HISTORY |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2310 | make (3sg) | macaþ | *makōną | *mákōθi | late_analogy | Class II weak 3sg pres. indic. Regular: *-ōθi → -aþ (Campbell §355.4, R/T vol.2 p.80). No i-umlaut: 3sg ending never had -j-. Forms with -eþ are dialectal (Campbell §757). | - |

## Manifest status

_No manifest entry._

## High-confidence evidence

### Compact derivation trace entry

```md
# make (3sg)
PROTO: *mákōθi
EXPECTED: macaþ
OUTPUTS: macaþ



### Proto-Germanic consonant inheritance

Proto Input: *mákōθi

| Earlier Germanic developments | Old English developments |
|:---|:---|
| **Proto-West Germanic**<br>PWGmc Early I Apocope: *mákōθ<br><br>**Northwest Germanic**<br>[no change] | **Old English**<br>Anglo Frisian Brightening: *mækōθ<br>OE A Restoration: *makōθ<br>OE Late O Shortening: *makaθ |



### Orthography & surface

Old English Orthography: *makaþ
Outcome: macaþ

NOTE: Class II weak 3sg pres. indic. Regular: *-ōθi → -aþ (Campbell §355.4, R/T vol.2 p.80). No i-umlaut: 3sg ending never had -j-. Forms with -eþ are dialectal (Campbell §757).
```

### Matching oe_known_problems.tsv entries

_None_

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:19598 (row ID)

- Nearby heading: ### TSV Corrections Needed

```text
19596: | Row | Current | Should be | Note correction |
19597: |-----|---------|-----------|-----------------|
19598: | 2310 | `maceþ` | `macaþ` | Regular *ōθi → -aþ. TSV note was wrong. |
19599: | 2312 | `boreþ` | `boraþ` | Regular *ōθi → -aþ. TSV note was wrong. |
19600: | 2314 | `liorneþ` | `liornaþ` | Regular *ōθi → -aþ. Forms with -eþ are dialectal. |
```

#### Germanic/docs/DEV_NOTES.md:19874 (exact PROTOFORM)

- Nearby heading: ### The Problem

```text
19872: ```
19873: --- make (3sg) ---
19874: PROTO: *mákōθi
19875: EXPECTED: macaþ
19876: OUTPUTS: maceþ
```

#### Germanic/docs/DEV_NOTES.md:19952 (exact pair)

- Nearby heading: ### Affected Forms

```text
19950: 
19951: This fix should resolve all 4 weak II 3sg regressions:
19952: 1. `*mákōθi → macaþ` (currently produces `maceþ`)
19953: 2. `*búrōθi → boraþ` (currently produces `boreþ`)
19954: 3. `*líkkōθi → liccaþ` (currently produces `licceþ`)
```

### Analysis and dossier hits

_None_

## Supporting/background evidence

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:19 (note keyword: i-umlaut)

- Nearby heading: ### Mismatch fixes (Mar 2026)

```text
17: - [Preconsonantal *x Loss: *xs > *s](#preconsonantal-x-loss-xs--s-before-consonant-clusters)
18: - [PGmc *d/*ð Representation Decision](#decision-2026-03-11-option-2a-confirmed)
19: - [OE þistel 'thistle': Scholarly Controversy](#oe-þistel-thistle-i-umlaut-not-preserved-2026-03-18)
20: - [OE huniġ 'honey': The -ag > -ig Sound Change](#oe-huniġ-honey-the--ag---ig-sound-change-2026-03-19)
21: - [OE wīþiġ 'withy': ja-stem vs Sievers' Law](#oe-wīþiġ-withy-ja-stem-adjective-vs-sievers-law-syncope-2026-03-19)
```

#### Germanic/docs/DEV_NOTES.md:116 (note keyword: i-umlaut)

- Nearby heading: ### Could we use paradigm forms? (Why we decided not to)

```text
114: - Root nouns are a small, archaic class (burg, brust, furh, hnut-); extending the analysis to common nouns like 'wolf' and 'fowl' would be speculative.
115: 
116: **Approach D: Use a derivational form with i-umlaut trigger.**
117: For some of the items, there are derivational forms with *j or *i that block lowering: *wulfi- (hypothetical i-stem variant?), or the derived verb *fullijaną 'to fill' → OE fyllan (where *-ij- blocks lowering of root *u).
118: 
```

#### Germanic/docs/DEV_NOTES.md:120 (note keyword: i-umlaut)

- Nearby heading: ### Could we use paradigm forms? (Why we decided not to)

```text
118: 
119: **What weighs against Approach D:**
120: - These derived forms already show i-umlaut (*fullijaną → fyllan, not full). We can't simultaneously have the u preserved (from the high-vowel context) AND escape i-umlaut. The derivational base is a different word, not a paradigm form of the simplex noun.
121: 
122: ### Luick's doublets evidence
```

#### Germanic/docs/DEV_NOTES.md:709 (note keyword: i-umlaut)

- Nearby heading: ### Summary of OE syncope rules (scholarly consensus)

```text
707: 1. **Non-high vowel syncope** (`*a/*e → ∅`): Applies **regardless of preceding 
708:    syllable weight**, as long as the syllable is stressed. This affects PWGmc `*a` 
709:    and its i-umlaut product `*e`.
710:    
711:    Examples:
```

#### Germanic/docs/DEV_NOTES.md:742 (note keyword: i-umlaut)

- Nearby heading: ### The milk problem: `*melukz` → `meoloc` (expected `meolc`)

```text
740: with paradigm variation:
741: - Nom.sg.: `*melukz` → `meoloc` (with breaking `e → eo`, no syncope)
742: - Gen./dat.sg.: `*milukiz/*miluki` → Anglian `milc` (with i-umlaut and syncope)
743: 
744: R/T §6.6.4 (p.253): "The usual WS form of 'milk' is `meolc < meoluc < *meluk`... 
```

#### Germanic/docs/DEV_NOTES.md:749 (note keyword: i-umlaut)

- Nearby heading: ### The milk problem: `*melukz` → `meoloc` (expected `meolc`)

```text
747: 
748: **Key point:** The syncopated form `milc` shows **early syncope** that occurred even
749: before i-umlaut — R/T (p.257) notes this as a "possible early instance of syncope."
750: The WS form `meoloc ~ meolc` shows **variable syncope after a light syllable**.
751: 
```

#### Germanic/docs/DEV_NOTES.md:2845 (exact COUNTERPART)

- Nearby heading: ### Options for Resolution

```text
2843:   changes the citation form across all 4 languages in each cognate set
2844: 
2845: **Option B: Change citation form to 3sg pres. indic.** (e.g., *makōþi → macaþ)
2846: - Pro: Regular development with more morphology visible
2847: - Con: More complex form; still needs *ō → -a- modelling in medial position;
```

#### Germanic/docs/DEV_NOTES.md:2914 (exact COUNTERPART)

- Nearby heading: ### Test forms: imperative 2sg and 3sg present indicative

```text
2912: - This path does NOT involve the morphological *-ōja- suffix
2913: 
2914: **3sg present indicative** (*-ōθi): PGmc *makōθi → OE *maceþ (regular) / macaþ (attested, analogical)
2915: - The *i in *-ōθi triggers i-umlaut of the *ō, giving *ē → e
2916: - The regular phonological outcome is -eþ, not -aþ
```

#### Germanic/docs/DEV_NOTES.md:2917 (exact COUNTERPART)

- Nearby heading: ### Test forms: imperative 2sg and 3sg present indicative

```text
2915: - The *i in *-ōθi triggers i-umlaut of the *ō, giving *ē → e
2916: - The regular phonological outcome is -eþ, not -aþ
2917: - Attested macaþ has -aþ by analogy with the rest of the paradigm
2918: 
2919: ### Findings
```

#### Germanic/docs/DEV_NOTES.md:19503 (exact COUNTERPART)

- Nearby heading: ### The Error in Our TSV

```text
19501: The TSV entries for weak class II 3sg forms (rows 2310, 2312, 2314, etc.) claim:
19502: 
19503: > "Regular phonology: *ōθi → -eþ (i-umlaut of *ō). Attested macaþ is analogical."
19504: 
19505: **This is BACKWARDS.** The actual regular outcome is `-aþ`, and the `-eþ` forms 
```

#### Germanic/docs/DEV_NOTES.md:19911 (exact PROTOFORM)

- Nearby heading: ### Historical Forms at This Stage

```text
19909: | Protoform | At this stage | Issue |
19910: |-----------|---------------|-------|
19911: | `*mákōθi` | `*makōθ` | `*ō` followed by `*θ` (medial) |
19912: | `*búrōθi` | `*borōθ` | `*ō` followed by `*θ` (medial) |
19913: | `*mēnōθz` | `*mēnōθ` | `*ō` followed by `*θ` (medial) |
```

### Analysis and dossier hits

#### Germanic/docs/analysis/arestoration_r_l_research.md:456 (note keyword: i-umlaut)

- Nearby heading: ## 7. R/T relative chronology of A-fronting, A-restoration, breaking, and i-umlaut

```text
455: 
456: ## 7. R/T relative chronology of A-fronting, A-restoration, breaking, and i-umlaut
457: 
```

#### Germanic/docs/analysis/arestoration_r_l_research.md:472 (note keyword: i-umlaut)

- Nearby heading: ## 7. R/T relative chronology of A-fronting, A-restoration, breaking, and i-umlaut

```text
471: (3) *a before single C / geminate / sC + back vowel
472:  ↓ I-umlaut (R/T §6.6)
473: (4) modifies remaining *æ but cannot un-restore *a
```

#### Germanic/docs/analysis/arestoration_r_l_research.md:735 (note keyword: i-umlaut)

- Nearby heading: ## 11. Affected TSV rows

```text
734: | 2056 | `*xármaz` | `hearm` | breaking |
735: | 2057 | `*xárbistuz` | `hierfest` | breaking + i-umlaut |
736: | 2077 | `*xáldaną` | `healdan` | breaking |
```

#### Germanic/docs/analysis/compound_archaism_inventory.md:154 (note keyword: i-umlaut)

- Nearby heading: ### Case 6: *líznōn- (learn) — leornian

```text
153: | **Lautgesetzlich output** | `leornian` (from *e-grade root `*leznōn-`) (FST: ✓ correct with corrected proto) |
154: | **Previous FST output** | `liernian` (from incorrect *i-grade root `*liznōn-` + i-umlaut *eo → ie*) |
155: | **DEV_NOTES reference** | §14.518–14.760 (OE leornian 'to learn' — ie vs eo diphthong problem); major cross-reference in mismatch_dossier_mizdo.md (Campbell §123 fn.2 citation) |
```

#### Germanic/docs/analysis/compound_archaism_inventory.md:168 (note keyword: i-umlaut)

- Nearby heading: ### Case 7: *fúwerō / *fūri (fire) — fȳre (dat.sg.) vs. fȳr (nom.sg.)

```text
167: | **PROTO** | `*fūri` (dat.sg., locative singular; singular = u-stem or ī-stem, feminine) |
168: | **OE SIMPLEX (NOM.SG.)** | `fȳr` (nom.sg., attested, showing i-umlaut of *ū → *ȳ*) |
169: | **OE SIMPLEX (DAT.SG.)** | `fȳre` (dat.sg., showing i-umlaut plus **analogically restored** final *-e*) |
```

#### Germanic/docs/analysis/compound_archaism_inventory.md:169 (note keyword: i-umlaut)

- Nearby heading: ### Case 7: *fúwerō / *fūri (fire) — fȳre (dat.sg.) vs. fȳr (nom.sg.)

```text
168: | **OE SIMPLEX (NOM.SG.)** | `fȳr` (nom.sg., attested, showing i-umlaut of *ū → *ȳ*) |
169: | **OE SIMPLEX (DAT.SG.)** | `fȳre` (dat.sg., showing i-umlaut plus **analogically restored** final *-e*) |
170: | **Sound changes** | I-umlaut (*ū → ȳ* before *i) + Apocope (final *-i → Ø* after heavy syllable) + Analogical restoration (*-e added*) |
```

#### Germanic/docs/analysis/cow_root_noun_investigation.md:48 (note keyword: i-umlaut)

- Nearby heading: ### OE paradigm of cū (§6.6.1, line 18238)

```text
47: - **nom.sg.** cū (< leveled *kū, analogical from oblique)
48: - **dat.sg.** cȳ (< *kūi, regular i-umlaut: ū → ȳ)
49: - **nom.-acc.pl.** cȳ (< *kūiz, same i-umlaut)
```

#### Germanic/docs/analysis/cow_root_noun_investigation.md:49 (note keyword: i-umlaut)

- Nearby heading: ### OE paradigm of cū (§6.6.1, line 18238)

```text
48: - **dat.sg.** cȳ (< *kūi, regular i-umlaut: ū → ȳ)
49: - **nom.-acc.pl.** cȳ (< *kūiz, same i-umlaut)
50: - **gen.sg.** cā (< *kūiz? — form uncertain, R/T say "apparently")
```

#### Germanic/docs/analysis/cow_root_noun_investigation.md:61 (note keyword: i-umlaut)

- Nearby heading: ### Hall's Concise Anglo-Saxon Dictionary

```text
60: 
61: This matches R/T's §7 observation (line 21452): "The ō-stem gen. sg. ending -e has spread to fem. root-nouns, where it is in competition with the inherited endingless form with i-umlaut."
62: 
```

#### Germanic/docs/analysis/four_complex_tsv_items.md:46 (note keyword: i-umlaut)

- Nearby heading: ### OE target assessment

```text
45: 3. **Breaking**: \*æhh → \*eahh
46: 4. **i-Umlaut**: \*eahh → \*ieahh → hiehh (WS palatal diphthong umlaut)
47: 
```

#### Germanic/docs/analysis/four_complex_tsv_items.md:105 (note keyword: i-umlaut)

- Nearby heading: ### Proto-form assessment

```text
104: The proto `*skellinăz` does not match Kroonen's reconstruction. The \*e in
105: \*skellinăz would give OE \*sċiellen (via i-umlaut and palatalization), but the
106: attested form is sċilling with *i.
```

#### Germanic/docs/analysis/four_complex_tsv_items.md:114 (note keyword: i-umlaut)

- Nearby heading: ### Pipeline issues

```text
113: 
114: 2. **With current proto** `skellinăz`: the pipeline produces `sċiellen` (with i-umlaut
115:    of *e → *ie, but no mechanism to produce *i in the root).
```

#### Germanic/docs/analysis/fryhtu_investigation.md:26 (note keyword: i-umlaut)

- Nearby heading: ### R/T's analysis

```text
25: 
26: R/T (line 21553) treat OE fyrhtu as an **ī-stem abstract noun**. The i-umlaut
27: (\*u → y) proves an \*i-containing source, since the ō-stem \*furhtō- would give
```

#### Germanic/docs/analysis/fryhtu_investigation.md:34 (note keyword: i-umlaut)

- Nearby heading: ### The \*iþō-abstract analysis

```text
33: with the suffix PGmc \*-iþō-. These are inflectionally ō-stems but contain the
34: derivational element \*-iþ- which triggers i-umlaut. Well-known examples:
35: 
```

#### Germanic/docs/analysis/fryhtu_investigation.md:45 (note keyword: i-umlaut)

- Nearby heading: ### The \*iþō-abstract analysis

```text
44: 
45: 1. **i-umlaut**: \*furhtiþō → \*fyrhtiþō (\*u → \*y, triggered by \*i in suffix)
46: 2. **Medial vowel syncope**: \*fyrhtiþō → \*fyrhþō (unstressed medial \*i lost)
```

#### Germanic/docs/analysis/notable_findings.md:270 (note keyword: i-umlaut)

- Nearby heading: ## 2. NWGmc u-lowering exceptions near labials: a non-Neogrammarian pattern

```text
269:    this out
270: 4. **Derivational forms with \*j/\*i** — would show i-umlaut, giving wrong
271:    root vowel
```

#### Germanic/docs/analysis/notable_findings.md:951 (note keyword: i-umlaut)

- Nearby heading: ## 6. PGmc stem-class disambiguation via OE phonology: \*kraft- and \*stab-

```text
950: **Background:** Two TSV entries (cræft, stæf) had PGmc proto-forms ending in
951: \*-iz (i-stem nominative singular), which our pipeline processed with i-umlaut
952: to yield \*creft and \*stefe. But the attested OE forms are **cræft** and
```

#### Germanic/docs/analysis/notable_findings.md:953 (note keyword: i-umlaut)

- Nearby heading: ## 6. PGmc stem-class disambiguation via OE phonology: \*kraft- and \*stab-

```text
952: to yield \*creft and \*stefe. But the attested OE forms are **cræft** and
953: **stæf** — with æ, not e — indicating that i-umlaut did not apply.
954: 
```

#### Germanic/docs/analysis/ws_vs_anglian_dialect_differences.md:145 (note keyword: i-umlaut)

- Nearby heading: ### Ringe & Taylor §6.9.2 (repo ll. 17663–17760)

```text
144: R/T note an asymmetry (ll. 17769–17772): the raising `æ > é` operated only
145: on `æ < éa` (smoothing-output), **not** on `æ < *a` (i-umlaut output). Hence
146: WS, Merc., North. all keep `ǽht` 'possession', `tǽcnan`, `fǽcne` etc.
```

#### Germanic/docs/analysis/ws_vs_anglian_dialect_differences.md:156 (note keyword: i-umlaut)

- Nearby heading: ### Brunner §119 "Ebnung" (repo ll. 4745–4811)

```text
155: > für ea und eo jeder Herkunft (für ea in ganz alten Texten aber æ ...),
156: > i für io, æ für ea (bei i-Umlaut aber e ...), e für eo, i für io. Solche
157: > anglische Formen sind demnach: ... becen Zeichen, ec auch, leg Seil, ege
```

#### Germanic/docs/analysis/ws_vs_anglian_dialect_differences.md:569 (note keyword: i-umlaut)

- Nearby heading: ## 7. i-mutation outcomes

```text
568: 
569: For most front vowels, i-umlaut outcomes are uniform across dialects.
570: Differences emerge mainly with the diphthongs `ea, eo, io` and with `ǽ`:
```

#### Germanic/docs/dossiers/bugan-scufan-paradigm-cell-review.md:239 (note keyword: i-umlaut)

- Nearby heading: ### §4.2 Phonological assessment

```text
238: * **`bȳhþ` / `bȳhst`** (3/2 sg. pres. ind.): would require
239:   i-umlaut of the *u* (or of the inherited *iu* > *í*-stage)
240:   followed by spirantisation/devoicing of the stem-final consonant
```

#### Germanic/docs/dossiers/bugan-scufan-paradigm-cell-review.md:326 (note keyword: i-umlaut)

- Nearby heading: ### §5.2 Phonological assessment

```text
325:   a-mutation, then *-anaz > -en. Universal attestation.
326: * **`sċȳfþ`** (3 sg. pres. ind.): would require i-umlaut + cluster
327:   realisation parallel to `bȳhþ`; possible but more cascade-
```

#### Germanic/docs/dossiers/g-palatalisation-conditioning.md:32 (note keyword: i-umlaut)

- Nearby heading: ## 1. TL;DR

```text
31: > **Inherited West-Gmc /ɣ/ palatalises to OE [ʝ] > [j] (spelt ġ) when it is
32: > adjacent to a front vowel (i, ī, e, ē, æ, ǣ, y, ȳ from i-umlaut, ie/ī from
33: > i-umlaut, and the front diphthongs io/eo/ea, ie/ȳ) AND a following back
```

#### Germanic/docs/dossiers/g-palatalisation-conditioning.md:33 (note keyword: i-umlaut)

- Nearby heading: ## 1. TL;DR

```text
32: > adjacent to a front vowel (i, ī, e, ē, æ, ǣ, y, ȳ from i-umlaut, ie/ī from
33: > i-umlaut, and the front diphthongs io/eo/ea, ie/ȳ) AND a following back
34: > vowel does not "rescue" it.**
```

#### Germanic/docs/dossiers/g-palatalisation-conditioning.md:79 (note keyword: i-umlaut)

- Nearby heading: ### 2.1 Campbell, *Old English Grammar* (1959), §§ 426–430

```text
78: > i.e. by æ, e, i, by ǣ, ē, ī, by the diphthongs ǣa, ēa, eo, io, by æ̆ and
79: > ē̆ where these are due to i-umlaut, but not by y, ȳ, œ, ø̄ from i-umlaut of
80: > u, ū, o, ō (cf. § 190)."
```

#### Germanic/docs/dossiers/widuwe-u-preservation.md:176 (note keyword: i-umlaut)

- Nearby heading: #### p. 270 — `widuwe` listed under "i, u, y not syncopated"

```text
175: 
176: > A large number of examples show that *i, *u, and *y (the i-umlaut
177: > product of *u) were not syncopated after light syllables. They
```

#### Germanic/docs/dossiers/widuwe-u-preservation.md:1163 (note keyword: i-umlaut)

- Nearby heading: ### B.8 Synthesis across the canvass: answers to questions A-G

```text
1162:   Brunner sec. 114b's account of widwe vs. WS wuduwe.
1163: - Relative to i-umlaut: not directly addressed by these
1164:   authorities for *wi → *wu specifically; Brunner sec. 114a's
```

#### Germanic/docs/dossiers/widuwe-u-preservation.md:1166 (note keyword: i-umlaut)

- Nearby heading: ### B.8 Synthesis across the canvass: answers to questions A-G

```text
1165:   parallel *wir > *wur > *wyr (Anglian) shows *wir → *wur
1166:   precedes i-umlaut.
1167: - Within the cascade: the rule must precede OEMedUnstressedULowering
```

### Local lexical-table hits

#### old_english_wiktionary.tsv

_None_

#### old_english_swadesh.tsv

_None_

## Possibly stale or diagnostic evidence

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:19382 (exact PROTOFORM)

- Nearby heading: ### The Problem

```text
19380: 
19381: After implementing `PWGmcEarlyIApocope` (loss of final `-i` in 3rd/4th syllable position),
19382: we found that weak verb class II 3sg forms like `*mákōθi → macoþ` instead of expected
19383: `maceþ`. The FST is producing `-oþ` instead of `-eþ`.
19384: 
```

#### Germanic/docs/DEV_NOTES.md:19388 (exact PROTOFORM)

- Nearby heading: ### The Problem

```text
19386: | Protoform | FST output | Expected OE | Error |
19387: |-----------|------------|-------------|-------|
19388: | `*mákōθi` | `macoþ` | `maceþ` | `-o-` not `-e-` |
19389: | `*búrōθi` | `boroþ` | `boreþ` | `-o-` not `-e-` |
19390: | `*líznōθi` | `liornoþ` | `liorneþ` | `-o-` not `-e-` |
```

#### Germanic/docs/DEV_NOTES.md:19571 (exact pair)

- Nearby heading: ### What This Means for Our FST

```text
19569: | Form | FST output | TSV expected | Actual regular OE |
19570: |------|------------|--------------|-------------------|
19571: | `*mákōθi` | `macoþ` | `maceþ` ❌ | `macaþ` ✓ |
19572: | `*búrōθi` | `boroþ` | `boreþ` ❌ | `boraþ` ✓ |
19573: | `*líznōθi` | `liornoþ` | `liorneþ` ❌ | `liornaþ` ✓ |
```

#### Germanic/docs/DEV_NOTES.md:19709 (exact pair)

- Nearby heading: ### Test Cases

```text
19707: | Input | Current output | Expected output |
19708: |-------|----------------|-----------------|
19709: | `*mákōθi` | `macoþ` | `macaþ` |
19710: | `*búrōθi` | `boroþ` | `boraþ` |
19711: | `*mēnōθz` | `mōnoþ` | `mōnaþ` |
```

#### Germanic/docs/DEV_NOTES.md:19975 (exact pair)

- Nearby heading: ### The Problem

```text
19973: 
19974: After extending `OEUnstressedLongVowelShortening4` to apply medially (§15.4), we
19975: expected weak class II 3sg forms like `*mákōθi` to produce `macaþ`. Instead, the
19976: FST produces `maceþ` — the `-a-` from `*ō` shortening is being spuriously fronted
19977: to `-e-`.
```

#### Germanic/docs/DEV_NOTES.md:19979 (exact pair)

- Nearby heading: ### The Problem

```text
19977: to `-e-`.
19978: 
19979: **Expected:** `*mákōθi` → `macaþ`  
19980: **Actual:** `*mákōθi` → `maceþ`
19981: 
```

#### Germanic/docs/DEV_NOTES.md:19983 (exact pair)

- Nearby heading: ### The Problem

```text
19981: 
19982: This is a 4-form regression affecting:
19983: - `*mákōθi → maceþ` (expected `macaþ`)
19984: - `*búrōθi → boreþ` (expected `boraþ`)
19985: - `*líkkōθi → licceþ` (expected `liccaþ`)
```

### Analysis and dossier hits

#### Germanic/docs/analysis/mismatch_dossier_mizdo.md:292 (note keyword: i-umlaut)

- Nearby heading: ### 4.1 Primary handbooks

```text
291:   - Standard breaking rule: *e → *eo / __ {r, x}C
292: - **§202** (pp. 80–82): Describes i-umlaut of breaking diphthongs
293:   - "A small group of words (§124) suggest that the mutation of eo was io"
```

#### Germanic/docs/analysis/mismatch_dossier_mizdo.md:518 (note keyword: i-umlaut)

- Nearby heading: ### 6.2 Other *i + rd clusters (rhotacized)

```text
517: 1. `*búrdiz` 'birth' (row 1951) → FST: `byrd` ✓
518:    - Expected: `*búrdiz` → u-lowering → `*bordiz` → breaking (blocked, because *o not *e/*i) → i-umlaut `*byrd` ✓
519: 2. `*xérdō` 'herd' (row 2073) → FST: `heord` ✓
```

#### Germanic/docs/analysis/mismatch_dossier_mizdo_supplement.md:51 (note keyword: i-umlaut)

- Nearby heading: ## 1. Charge of this supplement

```text
50: 
51: 3. **Parallel with \*rēc** (notable_findings.md #10): OE *rēc* 'smoke' shows universal long ē across all dialects where we expect WS diphthong *īe (from *au + i-umlaut). Both *rēc* and *mēd* avoid expected diphthongs. Is there a systematic development *VzC → VːC* that yields ē regularly, making *meord* the marked form rather than *mēd*?
52: 
```

#### Germanic/docs/analysis/mismatch_dossier_mizdo_supplement.md:522 (note keyword: i-umlaut)

- Nearby heading: ### 5.1 The *rēc case (notable_findings.md #10)

```text
521: **OE rēc** 'smoke' < PGmc *\*raukiz (m. i-stem):
522: - **Expected WS outcome**: *\*rīec (from *au + i-umlaut → *īe)
523: - **Attested outcome**: **rēc** (long ē monophthong, **no diphthong**)
```

#### Germanic/docs/analysis/mismatch_dossier_mizdo_supplement.md:556 (note keyword: i-umlaut)

- Nearby heading: ### 5.3 Testing the VzC → VːC hypothesis

```text
555: Other *i + rd clusters (after rhotacism):
556: 1. *\*búrdiz* 'birth' → OE *byrd* (no issue; *u lowers, then i-umlaut)
557: 2. *\*xérdō* 'herd' → OE *heord* ✓ (regular breaking of *e → *eo)
```

## Bibliography-key candidates

### Preferred candidates

| Key | Why it was selected |
| :--- | :--- |
| Kroonen2013 | default Proto-Germanic etymology key for Kroonen |
| Campbell1959 | single available key for Campbell |
| SieversBrunner1965 | single available key for Sievers |
| Luick1914 | single available key for Luick |

### Low-confidence candidates

| Key | Why it was selected |
| :--- | :--- |
| Kroonen2011 | surname mention only: Kroonen |
| Kroonen2006 | surname mention only: Kroonen |

## Paradigm probe

Paradigm probe required for this row, but no built-in `oe_paradigm_probe.py` specification exists yet. This packet should be used to draft the probe configuration before prose drafting.

