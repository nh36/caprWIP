# Evidence packet — 2242 ten / tēon

> This packet is evidence for drafting. Do not treat all hits as equally authoritative; prefer high-confidence evidence.

## TSV row data

| ID | CONCEPT | COUNTERPART | PROTO | PROTOFORM | DERIVATION_CLASS | NOTE | HISTORY |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2242 | ten | tēon | *téxun | *téxun | attested_variant | Retargeted from WS tīen to (Anglian/Northumbrian/early-WS) tēon, the regular lautgesetzlich outcome of *tehun via intervocalic *h-loss + contraction (Brunner §129.2, §234, §325; Bülbring §557e; Kaluza; Hirt; Ringe-Taylor 2014). WS tien is secondary, levelled out of i-umlauted inflected i-stem cells (Stiles 1985-6, NOWELE 7). The un-umlauted stem tēon- is preserved in the ordinal tēoða and the compound -tēontig (hundtēontig '100'). See DEV_NOTES §17.48 and §17.48.1. | Source: Wiktionary etymology (template:inh) \| Source: Wiktionary etymology (template:inh) |

## Manifest status

_No manifest entry._

## High-confidence evidence

### Compact derivation trace entry

```md
# ten
PROTO: *téxun
EXPECTED: tēon
OUTPUTS: tēon



### Proto-Germanic consonant inheritance

Proto Input: *téxun

| Earlier Germanic developments | Old English developments |
|:---|:---|
| **Proto-West Germanic**<br>[no change]<br><br>**Northwest Germanic**<br>[no change] | **Old English**<br>OE Med Unstressed U Lowering: *téxon<br>OE Breaking: *téoxon<br>OE H Loss: *téoon<br>OE Contraction: *tḗon |



### Orthography & surface

Outcome: tēon

NOTE: Retargeted from WS tīen to (Anglian/Northumbrian/early-WS) tēon, the regular lautgesetzlich outcome of *tehun via intervocalic *h-loss + contraction (Brunner §129.2, §234, §325; Bülbring §557e; Kaluza; Hirt; Ringe-Taylor 2014). WS tien is secondary, levelled out of i-umlauted inflected i-stem cells (Stiles 1985-6, NOWELE 7). The un-umlauted stem tēon- is preserved in the ordinal tēoða and the compound -tēontig (hundtēontig '100'). See DEV_NOTES §17.48 and §17.48.1.
```

### Matching oe_known_problems.tsv entries

_None_

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:1450 (exact pair)

- Nearby heading: ## Project Status (as of 2026-04-30) — research phase complete

```text
1448: * `*ḗ` long-vowel stress tier (§17.49) — 5-phase refactor that landed
1449:   cleanly without behavioural regression and unblocked subsequent work.
1450: * `*téxun → tēon` (§17.48) ten-paradigm-cell research and dossier.
1451: * `*néwun → nigon` (§17.50) — NSGmc/Ingvaeonic *nigun adopted at TSV
1452:   level after a thorough Bugge's-velarization controversy review.
```

#### Germanic/docs/DEV_NOTES.md:42352 (exact pair)

- Nearby heading: ## §17.48 — *téxun → tēon (ten): paradigm-cell-matching dossier

```text
42350: 4. The `cons_mismatch__f_vs_s__cluster` bucket should be empty.
42351: 
42352: ## §17.48 — *téxun → tēon (ten): paradigm-cell-matching dossier
42353: 
42354: ### Problem
```

#### Germanic/docs/DEV_NOTES.md:42399 (exact COUNTERPART)

- Nearby heading: ### Current FST trace (*téxun)

```text
42397: 
42398: The cascade gets within one step of the regular outcome: *éo + *o
42399: should contract to *ḗo (long ēo), giving surface **tēon**.
42400: 
42401: ### Existing OEContraction (lines 2973–2997)
```

#### Germanic/docs/DEV_NOTES.md:42428 (exact pair)

- Nearby heading: ### Paradigm-cell candidates for *téxun

```text
42426: |---|---|---|---|
42427: | **tien / tīen** | WS uninflected | NO — requires i-umlaut from i-stem inflection | Fulk §10.2; Brunner §129 Anm.6 |
42428: | **tēon** | WGmc/early-WS uninflected, preserved in compound `hund-tēon-tig` | YES — *téxun → breaking → *téoxun → h-loss + contraction → *tḗon | Fulk §10.2; Campbell §238.2 |
42429: | **tēn** | Mercian/Anglian uninflected | YES via Anglian smoothing path | Campbell §682; Fulk §10.2 |
42430: | **tēo** | Late Northumbrian (final *n loss) | YES via further -n loss | Campbell §682 |
```

#### Germanic/docs/DEV_NOTES.md:42499 (exact pair)

- Nearby heading: ### Implementation plan

```text
42497: Step 2. Add four `*eo/*éo + *o` clauses to OEContraction.
42498: Step 3. TSV row 1210: COUNTERPART `tīen → tēon`; append NOTE.
42499: Step 4. Rebuild bins; verify `*téxun → tēon`; verify no regression
42500:         on `*féxu/*féxtaną/*sláxaną` (which already work).
42501: Step 5. Mismatch report → expect 11 → 10. `long_vowel_missing` bucket
```

#### Germanic/docs/DEV_NOTES.md:42627 (exact pair)

- Nearby heading: #### C. The contraction rule itself

```text
42625: *sláxaną → slēan*, *fehu → fēo*, etc.  The gap in `OEContraction` is
42626: that the existing clauses cover *eo + a → ēo* (slēan-type) but not
42627: *eo + o → ēo* (the *téxun → tēon* type).  Adding the four parallel
42628: *[ée]o + *o → *[ḗē]o* clauses fills the gap and makes the cascade match
42629: Brunner §129.2 as stated.
```

#### Germanic/docs/DEV_NOTES.md:42684 (exact pair)

- Nearby heading: ## §17.49 Stressed long-ē tier (`*ḗ`) — extending the §17.46 stress-tier convention

```text
42682: 
42683: **Motivation.** §17.48 introduced the long stressed diphthong `*ḗo` for
42684: the contraction product *téxun → *tḗun → *tēun → tēon* (and parallel
42685: ordinal/compound forms).  The introduction of `*ḗo` and the older
42686: `*ḗa` (lengthened breaking, §17.46) created an inconsistency: the
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

#### Germanic/docs/DEV_NOTES.md:42356 (exact PROTOFORM)

- Nearby heading: ### Problem

```text
42354: ### Problem
42355: 
42356: - TSV row 1210 (Old_English): PROTOFORM `*téxun`, COUNTERPART `tīen`.
42357: - FST output (current): `teoon` (no contraction; intervocalic h has
42358:   been lost but `*éo` + `*o` does not coalesce).
```

#### Germanic/docs/DEV_NOTES.md:42371 (exact COUNTERPART)

- Nearby heading: ### Source audit

```text
42369:   > in Gmc.; so Brunner 1965: §129 Anm. 6); the Mercian equivalent
42370:   > is thus correctly tēn. The uninflected form without umlaut is
42371:   > reflected in *hund-tēon-tig* '100'**" (§10.5).
42372: - **Campbell §682** (line 18870):
42373:   > "tien; nW-S tēn, lNorth. also tēo, tēa."
```

#### Germanic/docs/DEV_NOTES.md:42385 (exact PROTOFORM)

- Nearby heading: ### Current FST trace (*téxun)

```text
42383:   cardinal in nW-S retains the un-umlauted form **tēn**.
42384: 
42385: ### Current FST trace (*téxun)
42386: 
42387: ```
```

#### Germanic/docs/DEV_NOTES.md:42423 (exact PROTOFORM)

- Nearby heading: ### Paradigm-cell candidates for *téxun

```text
42421: `*eo + *o` pattern that arises from *V-x-u → breaking → weak-tail.
42422: 
42423: ### Paradigm-cell candidates for *téxun
42424: 
42425: | Candidate | Cell | Lautgesetzlich? | Citation |
```

#### Germanic/docs/DEV_NOTES.md:42434 (exact COUNTERPART)

- Nearby heading: #### Option A — retarget to **tēon** + add contraction clauses (RECOMMENDED)

```text
42432: ### Options
42433: 
42434: #### Option A — retarget to **tēon** + add contraction clauses (RECOMMENDED)
42435: 
42436: 1. TSV row 1210: COUNTERPART `tīen → tēon`. NOTE: cite Fulk §10.2,
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

#### Germanic/docs/dossiers/bugan-scufan-paradigm-cell-review.md:156 (note keyword: Anglian)

- Nearby heading: ## §3. The fault-line: `-un > -on` for stem-`u` verbs is analogical

```text
155:   Brunner §364.2 Anm. 4). For the two specific verbs we care about
156:   here, the early Anglian/Mercian witnesses simply do not contain
157:   a finite 3 pl. pret. token — the verb is unattested in those
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

| ENGLISH | OE_FORM | SOURCE | DETAIL | PAGE |
| :--- | :--- | :--- | :--- | :--- |
| ten | tīen | inh | template:inh | ten |

#### old_english_swadesh.tsv

| NUMBER | ENGLISH | OLD_ENGLISH | IPA_RAW |
| :--- | :--- | :--- | :--- |
| 134 | to pull | tēon | /ˈteːo̯n/ |

## Possibly stale or diagnostic evidence

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:2648 (concept name)

- Nearby heading: ### HIGH PRIORITY: PGmc final *-un behavior (2026-01-25)

```text
2646: 
2647: ### HIGH PRIORITY: PGmc final *-un behavior (2026-01-25)
2648: - **Problem:** PGmc final `*-un` is misbehaving across the “ten/seven/nine” set.
2649:   - `*texun` → model output **teoun**, expected **tīen** (full trace: `server/docs/debug_snapshots/oe_full_trace_report_2026-01-25e.txt`).
2650:   - `*sebun` → model output **sobun**, expected **seofon** (same report).
```

#### Germanic/docs/DEV_NOTES.md:20560 (exact PROTOFORM)

- Nearby heading: #### Regressions Identified (56 vs 43 mismatches)

```text
20558: - `-æ` vs `-e` endings: `*érθōn → eorþæ`, `*fádēr → fædær`, `*fláskōn → flascæ`, 
20559:   `*nēdrōn → nǣdræ`, `*xábēθi → hæfæþ`
20560: - Other: `*mízdō`, `*táixōn`, `*téxun`, `*wír-aldu`
20561: 
20562: **8 items fixed** (no longer mismatching):
```

#### Germanic/docs/DEV_NOTES.md:24464 (concept name)

- Nearby heading: #### 1. Probe outcome (vs. post-§17.10.23 baseline of 38)

```text
24462: | \*spēnuz   | spōno   | spōn     |
24463: 
24464: Net: five fixes, ten new-or-shifted regressions, +12 total mismatches.
24465: 
24466: #### 2. Root-cause: z-loss fires too late, spoofing OEMedUnstressedULowering
```

#### Germanic/docs/DEV_NOTES.md:24488 (concept name)

- Nearby heading: #### 2. Root-cause: z-loss fires too late, spoofing OEMedUnstressedULowering

```text
24486: syncope pattern).
24487: 
24488: Ten different forms fail for this exact reason. The rhotacism
24489: restriction (context `V _ ?`) is independent of this and is not
24490: implicated.
```

#### Germanic/docs/DEV_NOTES.md:30082 (concept name)

- Nearby heading: #### §17.18.7.1  Resolved policy

```text
30080: unchanged. The FST's current behavior (no parasiting in `-Cl/Cn/Cm#`,
30081: plus the special-case `OEGLInsertion` for `-gl#`) is correct for these
30082: ten lemmas: it produces an unbroken cluster which matches the early /
30083: poetic / Anglian register chosen by the dataset.
30084: 
```

#### Germanic/docs/DEV_NOTES.md:30092 (concept name)

- Nearby heading: #### §17.18.7.1  Resolved policy

```text
30090:   arises by the late-WS parasiting rule that we have decided not to
30091:   model in the FST (since it would falsify the unbroken targets in the
30092:   other ten rows).
30093: 
30094: The resolution is therefore to **target a different, fully attested,
```

### Analysis and dossier hits

#### Germanic/docs/analysis/mismatch_dossier_mizdo.md:13 (note keyword: Anglian)

- Nearby heading: # Mismatch Dossier: *mízdō 'reward, wage'

```text
12: >   Reader (in a poetic line, glossed as "(dial.)"), and Hall's Concise Dictionary.
13: >   It is a dialectal (Anglian-leaning) variant of WS *mēd*.
14: >
```

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
| RingeTaylor2014 | author + year mention (Taylor 2014) |
| Stiles1985 | author + year mention (Stiles 1985) |
| Kroonen2013 | default Proto-Germanic etymology key for Kroonen |
| Campbell1959 | single available key for Campbell |
| Luick1914 | single available key for Luick |
| Kaluza1906 | single available key for Kaluza |
| Fulk2018 | single available key for Fulk |
| Hirt1931 | single available key for Hirt |
| Kilday2024 | single available key for Kilday |

### Low-confidence candidates

| Key | Why it was selected |
| :--- | :--- |
| Ringe2006 | surname mention only: Ringe |
| Ringe2017 | surname mention only: Ringe |
| Ringe1984 | surname mention only: Ringe |
| SieversBrunner1965 | explicit year mention (1965) |
| Kroonen2011 | surname mention only: Kroonen |
| Kroonen2006 | surname mention only: Kroonen |
| Stiles2012 | surname mention only: Stiles |
| Stiles2017 | surname mention only: Stiles |
| Stiles1986a | surname mention only: Stiles |
| Stiles1986b | surname mention only: Stiles |

## Paradigm probe

Paradigm probe required for this row, but no built-in `oe_paradigm_probe.py` specification exists yet. This packet should be used to draft the probe configuration before prose drafting.

