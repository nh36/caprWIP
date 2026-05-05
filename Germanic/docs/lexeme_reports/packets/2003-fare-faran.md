# Evidence packet — 2003 fare / faran

> This packet is evidence for drafting. Do not treat all hits as equally authoritative; prefer high-confidence evidence.

## TSV row data

| ID | CONCEPT | COUNTERPART | PROTO | PROTOFORM | DERIVATION_CLASS | NOTE | HISTORY |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2003 | fare | faran | *fáraną | *fáraną | regular | OE target faran (inf. of str.v. class VI 'to fare, go'). Earlier note had færan, conflated with i-umlauted 2/3sg pres fær(e)þ or with weak causative færan 'to frighten' (< *fōrjaną); on the §17.26.0 hypothesis the wrong target was set to match the pre-§17.25 buggy FST output. Corrected per DEV_NOTES §17.26. | - |

## Manifest status

_No manifest entry._

## High-confidence evidence

### Compact derivation trace entry

```md
# fare
PROTO: *fáraną
EXPECTED: faran
OUTPUTS: faran



### Proto-Germanic consonant inheritance

Proto Input: *fáraną

| Earlier Germanic developments | Old English developments |
|:---|:---|
| **Proto-West Germanic**<br>[no change]<br><br>**Northwest Germanic**<br>[no change] | **Old English**<br>Anglo Frisian Brightening: *færaną<br>OE A Restoration: *faraną<br>OE Heavy Syllable Nasal Apocope: *faran<br>OE Secondary Nasalization: *farąn<br>OE Weak Tail Reduction: *faran |



### Orthography & surface

Outcome: faran

NOTE: OE target faran (inf. of str.v. class VI 'to fare, go'). Earlier note had færan, conflated with i-umlauted 2/3sg pres fær(e)þ or with weak causative færan 'to frighten' (< *fōrjaną); on the §17.26.0 hypothesis the wrong target was set to match the pre-§17.25 buggy FST output. Corrected per DEV_NOTES §17.26.
```

### Matching oe_known_problems.tsv entries

_None_

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:36669 (exact pair)

- Nearby heading: ### §17.25.7 Regression after first build — diagnosis and follow-up fix

```text
36667: |------|--------|-------|--------|--------|
36668: | `*spárēną` | `spearen` | `sparen` | `sparian` | mismatch (still); deferred to §17.26 (class III/II) |
36669: | `*fáraną`  | `færan`   | `faran`  | `færan`  | now mismatch (etymologically correct); user deferred to a separate loop |
36670: | `*táppô`   | `tappa`   | `tæppa`  | `tæppa`  | **now matching** (−1 mismatch, but see below — this is wrong-side-of-correct) |
36671: | `*láppô`   | `lappa`   | `læppa`  | `lappa`  | **NEW mismatch** |
```

#### Germanic/docs/DEV_NOTES.md:36783 (row ID)

- Nearby heading: ### §17.25.8 Post-fix verification

```text
36781: buggy *r/*l exclusion:
36782: 
36783: 1. **row 2003 `*fáraną → færan`** — user already explicitly deferred
36784:    to a separate loop iteration ("As for the 'bonus row', I would
36785:    also rather discuss it separately as a third issue").
```

#### Germanic/docs/DEV_NOTES.md:36859 (row ID)

- Nearby heading: ### §17.26.1 Diagnosis

```text
36857: 
36858: After the §17.25 A-restoration conditioning fix, the FST correctly
36859: produces `*fáraną → faran`. The TSV row 2003 lists the OE COUNTERPART
36860: as `færan`, creating a (now exposed) mismatch:
36861: 
```

### Analysis and dossier hits

#### Germanic/docs/analysis/arestoration_r_l_research.md:755 (row ID)

- Nearby heading: ### 11.1 Net count of TSV rows affected by the proposed fix

```text
754: 
755: * **Strictly fixed (current wrong → predicted right):** 1 row (ID 2003 `*fáraną`).
756:   - Caveat: TSV column 6 currently lists the (etymologically incorrect) `færan` as target; per R/T 13432 and Campbell §160(4) the correct OE inf. is `faran`. A separate TSV-data fix is required to take advantage of the FST fix.
```

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

#### Germanic/docs/DEV_NOTES.md:10421 (exact COUNTERPART)

- Nearby heading: ## Mismatch Progress Log (2026-03-14)

```text
10419: | 2026-04-26 | 25 | -1 | 51c6de41 | meorde: paradigm-cell switch *mízdō → *mízdai (§17.24, Crist/Kilday) |
10420: | 2026-04-26 | 24 | -1 | 5c1bf80c | A-restoration before single *r/*l (§17.25) |
10421: | 2026-04-26 | 23 | -1 | 1b9a44f1 | faran: TSV target færan → faran (§17.26) |
10422: | 2026-04-26 | 22 | -1 | 37031f31 | mare: TSV target mære → mare (§17.28) |
10423: | 2026-04-26 | 21 | -1 | 8bb2ecef | sundrian: target sundor- → sundrian (§17.29) |
```

#### Germanic/docs/DEV_NOTES.md:10671 (exact COUNTERPART)

- Nearby heading: ### What the Sources Actually Say About Chronology

```text
10669: > "As in stressed syllables, Anglo-Frisian a was nasalized before a nasal 
10670: > consonant (**but only a tautosyllabic one if the vowel was unstressed**),
10671: > otherwise fronted to æ (§4.11, later e: see below), as in OE faran, OFris.
10672: > fara 'go' and acc. sg. OE naman, OFris. noma, but with fronting in OE
10673: > masc. a-stem gen. sg. -es (early -æs), OFris. -es, and before heterosyllabic
```

#### Germanic/docs/DEV_NOTES.md:10674 (exact COUNTERPART)

- Nearby heading: ### What the Sources Actually Say About Chronology

```text
10672: > fara 'go' and acc. sg. OE naman, OFris. noma, but with fronting in OE
10673: > masc. a-stem gen. sg. -es (early -æs), OFris. -es, and before heterosyllabic
10674: > n in inflected forms of OE OFris. pp. faren- 'gone' < *faræn- < *faran-."
10675: 
10676: **This is the key passage.** Fulk explicitly states:
```

#### Germanic/docs/DEV_NOTES.md:10679 (exact COUNTERPART)

- Nearby heading: ### What the Sources Actually Say About Chronology

```text
10677: 1. Nasalization only occurs before a **tautosyllabic** (same-syllable) nasal
10678: 2. Before a **heterosyllabic** (different-syllable) nasal, fronting occurs
10679: 3. He gives the past participle as an explicit example: `faren-` < `*faræn-` < `*faran-`
10680: 
10681: The participle `*faran-` had fronting because `n` was heterosyllabic (onset of next
```

#### Germanic/docs/DEV_NOTES.md:10681 (exact COUNTERPART)

- Nearby heading: ### What the Sources Actually Say About Chronology

```text
10679: 3. He gives the past participle as an explicit example: `faren-` < `*faræn-` < `*faran-`
10680: 
10681: The participle `*faran-` had fronting because `n` was heterosyllabic (onset of next
10682: syllable), giving `*faræn-` > `faren`. The infinitive `*faran#` had nasalization
10683: because `n` was tautosyllabic (coda of final syllable), blocking fronting.
```

#### Germanic/docs/DEV_NOTES.md:10682 (exact COUNTERPART)

- Nearby heading: ### What the Sources Actually Say About Chronology

```text
10680: 
10681: The participle `*faran-` had fronting because `n` was heterosyllabic (onset of next
10682: syllable), giving `*faræn-` > `faren`. The infinitive `*faran#` had nasalization
10683: because `n` was tautosyllabic (coda of final syllable), blocking fronting.
10684: 
```

### Analysis and dossier hits

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

#### Germanic/docs/analysis/notable_findings.md:754 (exact COUNTERPART)

- Nearby heading: ## 4. A-restoration trigger set: {*æ} is NOT a trigger

```text
753: Silbe" ('PGmc *a = OE a in open syllable before a dark vowel of the
754: following syllable'). His examples (dagas, fatu, gladu, faran, grafan)
755: all have back suffixal vowels. But Kaluza adds a critical observation in
```

#### Germanic/docs/analysis/notable_findings.md:775 (exact COUNTERPART)

- Nearby heading: ## 4. A-restoration trigger set: {*æ} is NOT a trigger

```text
774: (1) "am deutlichsten in offener Silbe" ('most clearly in open syllable'):
775: hara, faran, nacod, macian, dagas, fatu; (2) before long consonants;
776: (3) before s+C and f+C; (4) "nur in wenigen Resten" ('only in a few
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

| ENGLISH | OE_FORM | SOURCE | DETAIL | PAGE |
| :--- | :--- | :--- | :--- | :--- |
| fare | fær | der | template:der | fare |

#### old_english_swadesh.tsv

_None_

## Possibly stale or diagnostic evidence

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:36617 (row ID)

- Nearby heading: ### §17.25.5 Predicted side-effects

```text
36615: (per the dossier §11):
36616: 
36617: - **Row 2003 `*fáraną → færan`**: current output `færan`; under the FST
36618:   fix, `faran`. The TSV target itself is currently wrong: per Campbell
36619:   §160(4) and R/T 13432 the West Saxon infinitive is `faran`, not
```

#### Germanic/docs/DEV_NOTES.md:36736 (row ID)

- Nearby heading: ### §17.25.7 Regression after first build — diagnosis and follow-up fix

```text
36734: either (a) the wrong protoform for that target, or (b) the result of
36735: analogical i-umlaut from another paradigm cell or another stem. It
36736: is parallel to row 2003 (`*fáraną → faran` vs target `færan`) in
36737: that the FST is now correct and the TSV target is the question.
36738: This will be raised as its own follow-up loop (alongside the §17.26
```

#### Germanic/docs/DEV_NOTES.md:36746 (exact PROTOFORM)

- Nearby heading: ### §17.25.7 Regression after first build — diagnosis and follow-up fix

```text
36744: - `*láppô` → `lappa` (matches target — restored from regression).
36745: - `*táppô` → `tappa` (mismatch vs target `tæppa` — now correctly
36746:   diagnosed as a TSV-target issue, parallel to *márōn and *fáraną).
36747: - `*spárōjaną` → `sparian` (the original §17.25 win, retained).
36748: - `*nadrō` → `næder` (no regression).
```

#### Germanic/docs/DEV_NOTES.md:36773 (exact pair)

- Nearby heading: ### §17.25.8 Post-fix verification

```text
36771: - `*táppô → tappa` (lautgesetzlich-correct; TSV target `tæppa` is the question)
36772: - `*márōn → mare` (lautgesetzlich-correct; TSV target `mære` is the question)
36773: - `*fáraną → faran` (etymologically correct; TSV target `færan` deferred per user)
36774: 
36775: Mismatch count: **25 → 27** (net +2).
```

#### Germanic/docs/DEV_NOTES.md:36806 (row ID)

- Nearby heading: ## §17.26 — *fáraną / faran (row 2003): TSV target correction (færan → faran)

```text
36804: issues above are the candidate topics for the next loop iterations.
36805: 
36806: ## §17.26 — *fáraną / faran (row 2003): TSV target correction (færan → faran)
36807: 
36808: ### §17.26.0 Why did we have the wrong target? (methodological note)
```

#### Germanic/docs/DEV_NOTES.md:36810 (row ID)

- Nearby heading: ### §17.26.0 Why did we have the wrong target? (methodological note)

```text
36808: ### §17.26.0 Why did we have the wrong target? (methodological note)
36809: 
36810: The TSV target for row 2003 was `færan` and a hand-wavy explanatory
36811: note ("OE target: fær→færan (inf. of str.v. class VI 'to fare, go')")
36812: asserted internally inconsistent things. The most likely explanation
```

#### Germanic/docs/DEV_NOTES.md:36811 (concept name)

- Nearby heading: ### §17.26.0 Why did we have the wrong target? (methodological note)

```text
36809: 
36810: The TSV target for row 2003 was `færan` and a hand-wavy explanatory
36811: note ("OE target: fær→færan (inf. of str.v. class VI 'to fare, go')")
36812: asserted internally inconsistent things. The most likely explanation
36813: is the **target-tuned-to-buggy-FST anti-pattern**:
```

#### Germanic/docs/DEV_NOTES.md:36864 (concept name)

- Nearby heading: ### §17.26.1 Diagnosis

```text
36862: ```
36863: 2003 | TOKENS: f æ r a n | PROTOFORM: *fáraną | COUNTERPART: færan
36864: NOTE: "OE target: fær→færan (inf. of str.v. class VI 'to fare, go')"
36865: ```
36866: 
```

#### Germanic/docs/DEV_NOTES.md:36868 (concept name)

- Nearby heading: ### §17.26.1 Diagnosis

```text
36866: 
36867: The note is internally inconsistent: it identifies the verb as the
36868: class VI strong verb 'to fare, go', whose infinitive is unambiguously
36869: `faran`, not `færan`. The likely conflations are with:
36870: 
```

#### Germanic/docs/DEV_NOTES.md:36918 (concept name)

- Nearby heading: ### §17.26.3 Proposed TSV change (row 2003)

```text
36916: | TOKENS | `f æ r a n` | `f a r a n` |
36917: | COUNTERPART | `færan` | `faran` |
36918: | NOTE | `OE target: fær→færan (inf. of str.v. class VI 'to fare, go')` | `OE target faran (inf. of str.v. class VI 'to fare, go'). Earlier note conflated this with i-umlauted 2/3sg pres fær(e)þ or with weak causative færan 'to frighten' (< *fōrjaną); on the §17.26.0 hypothesis the wrong target was set to match the pre-§17.25 buggy FST output. Corrected per §17.26.` |
36919: 
36920: ALIGNMENT (`f ɛə r - - ( - - )`) and IPA (`fɛə`) reflect the *modern
```

#### Germanic/docs/DEV_NOTES.md:36921 (concept name)

- Nearby heading: ### §17.26.3 Proposed TSV change (row 2003)

```text
36919: 
36920: ALIGNMENT (`f ɛə r - - ( - - )`) and IPA (`fɛə`) reflect the *modern
36921: English* reflex 'fare' (the convention for these columns in OE rows
36922: across the TSV) and stay as-is. PROTOFORM (`*fáraną`) and PROTO
36923: (`*fáraną`) stay as-is — the protoform is correct.
```

#### Germanic/docs/DEV_NOTES.md:36983 (exact pair)

- Nearby heading: ### §17.27.2 Outstanding §17.25-exposed issue

```text
36981: Of the three TSV-target issues exposed when §17.25 unblocked A-restoration
36982: before single *r/*l, two are now resolved:
36983: - row 2003 *fáraną → faran (TSV correction, §17.26)
36984: - *táppô (ledger triage, this section, §17.27)
36985: 
```

### Analysis and dossier hits

#### Germanic/docs/analysis/arestoration_r_l_research.md:67 (exact pair)

- Nearby heading: ## 1. Executive summary

```text
66: 
67: 6. **TSV impact (`Germanic/data/germanic-aligned-final.tsv`):** of the OE rows whose protoform contains a single intervening *r* or *l* between *a/á* and a back vowel **8 rows** match (see §11). Of those, **only 1 row** is *currently wrong and would be fixed*: row **2003** `*fáraną → faran` (currently emits `færan`). Row **2205** `*spárēną` (target `sparian`) currently produces `spearen`; the proposed fix is necessary but not sufficient (the trigger vowel `*ē` is front, so this is a separate class III→II morphology issue). The remaining 6 rows already produce a correct output and the proposed fix does not perturb them (verified by inspection of the rule structure; see §10.4).
68: 
```

#### Germanic/docs/analysis/arestoration_r_l_research.md:715 (exact pair)

- Nearby heading: ## 11. Affected TSV rows

```text
714: | 1984 | `*dálaz` | `dæl` | `dæl` | `dæl` | monosyllabic; final `*-az → ∅`, no surviving back trigger |
715: | 2003 | `*fáraną` | `færan`† | `færan` | **`faran`** | †TSV target is `færan` but that is itself **wrong**: per R/T 13432 and Campbell §160(4) the W-S inf. is **`faran`**. The recommended fix produces the historically correct form. **TSV column 6 should be updated separately.** |
716: | 2053 | `*xámaras` | `hameres` | `hameres` | `hameres` | intervening `*m` (not r/l); already correct under either rule |
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

#### Germanic/docs/analysis/notable_findings.md:747 (concept name)

- Nearby heading: ## 4. A-restoration trigger set: {*æ} is NOT a trigger

```text
746: of the type fæt ~ fatu, we do find in Old English minimal pairs such as
747: fare 'journey' dat.sg.masc. vs. fare 'journey' dat.sg.fem." But he
748: concedes "the case for therefore assuming a phonemic contrast between /æ/
```

## Bibliography-key candidates

### Preferred candidates

| Key | Why it was selected |
| :--- | :--- |
| Kroonen2013 | default Proto-Germanic etymology key for Kroonen |
| Campbell1959 | single available key for Campbell |
| SieversBrunner1965 | single available key for Sievers |
| Luick1914 | single available key for Luick |
| Kaluza1906 | single available key for Kaluza |
| Fulk2018 | single available key for Fulk |
| Kilday2024 | single available key for Kilday |

### Low-confidence candidates

| Key | Why it was selected |
| :--- | :--- |
| Kroonen2011 | surname mention only: Kroonen |
| Kroonen2006 | surname mention only: Kroonen |
| Crist2001 | surname mention only: Crist |
| Crist2002 | surname mention only: Crist |

