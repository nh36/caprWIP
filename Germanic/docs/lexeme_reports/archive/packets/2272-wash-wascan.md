# Evidence packet — 2272 wash / wascan

> This packet is evidence for drafting. Do not treat all hits as equally authoritative; prefer high-confidence evidence.

## TSV row data

| ID | CONCEPT | COUNTERPART | PROTO | PROTOFORM | DERIVATION_CLASS | NOTE | HISTORY |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2272 | wash | wascan | *wáskaną | *wáskaną | regular | Proto encoding: -aną (full vowel) for A-restoration; R/T §6.3.1 \| Medial sc before back vowel: not palatalized in early OE (Campbell §440); wascan [sk] is the conservative form. | Source: Wiktionary etymology (template:inh) |

## Manifest status

_No manifest entry._

## High-confidence evidence

### Compact derivation trace entry

```md
# wash
PROTO: *wáskaną
EXPECTED: wascan
OUTPUTS: wascan



### Proto-Germanic consonant inheritance

Proto Input: *wáskaną

| Earlier Germanic developments | Old English developments |
|:---|:---|
| **Proto-West Germanic**<br>[no change]<br><br>**Northwest Germanic**<br>[no change] | **Old English**<br>Anglo Frisian Brightening: *wæskaną<br>OE A Restoration: *waskaną<br>OE Heavy Syllable Nasal Apocope: *waskan<br>OE Secondary Nasalization: *waskąn<br>OE Weak Tail Reduction: *waskan |



### Orthography & surface

Outcome: wascan

NOTE: Proto encoding: -aną (full vowel) for A-restoration; R/T §6.3.1 | Medial sc before back vowel: not palatalized in early OE (Campbell §440); wascan [sk] is the conservative form.
```

### Matching oe_known_problems.tsv entries

_None_

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:30637 (exact pair)

- Nearby heading: ##### Words in the TSV with proto *-aCl-* or *-aCr-* before a back-vowel tail

```text
30635: | 2250 | *θístilas | þistles | (gen.sg., resolved in §17.18.7) |
30636: | 2271 | *wárpą | wearp | breaking |
30637: | 2272 | *wáskaną | wascan | sC cluster, A-restoration fires (Campbell §158, *flasce*-class) |
30638: | 2289 | *wáldaną | wealdan | breaking |
30639: | 2297 | *wálθuz | weald | breaking |
```

### Analysis and dossier hits

_None_

## Supporting/background evidence

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:36 (note keyword: A-restoration)

- Nearby heading: ### Project status and archived work

```text
34: - [Project Status (as of 2026-03-10)](#project-status-as-of-2026-03-10)
35: - [Consonant Mismatch Bucket Refinement (2026-02-07)](#consonant-mismatch-bucket-refinement-2026-02-07)
36: - [A-Restoration Fix (2026-02-06)](#a-restoration-fix-2026-02-06)
37: 
38: ### Working diary
```

#### Germanic/docs/DEV_NOTES.md:47 (note keyword: A-restoration)

- Nearby heading: ### Polished analyses (Feb–Mar 2026)

```text
45: - [Cognate set 379 "rock" → corrected to "coat"](#cognate-set-379-rock--corrected-to-coat-rukkăz)
46: - [Labiovelar Proto-Form Corrections](#labiovelar-proto-form-corrections-and-post-velar-w-loss-rt-642)
47: - [Water fix: PWGmc ō-shortening](#water-fix-pwgmc-ō-shortening-and-a-restoration-correction-3a45a8b)
48: - [A-restoration: ræst, tæppa, stemn](#a-restoration-in-ō-stems-and-n-stems-ræst-tæppa-stemn-fronting_missing__afb)
49: - [The stefn/stemn Problem](#the-stefnstemn-problem-local-transponent-decision)
```

#### Germanic/docs/DEV_NOTES.md:48 (note keyword: A-restoration)

- Nearby heading: ### Polished analyses (Feb–Mar 2026)

```text
46: - [Labiovelar Proto-Form Corrections](#labiovelar-proto-form-corrections-and-post-velar-w-loss-rt-642)
47: - [Water fix: PWGmc ō-shortening](#water-fix-pwgmc-ō-shortening-and-a-restoration-correction-3a45a8b)
48: - [A-restoration: ræst, tæppa, stemn](#a-restoration-in-ō-stems-and-n-stems-ræst-tæppa-stemn-fronting_missing__afb)
49: - [The stefn/stemn Problem](#the-stefnstemn-problem-local-transponent-decision)
50: - [z-loss/rhotacism and bimoraic/trimoraic cross-source analysis](#historical-phonology-of-final--z-loss-and-its-interaction-with-rhotacism)
```

#### Germanic/docs/DEV_NOTES.md:1649 (note keyword: A-restoration)

- Nearby heading: ## A-Restoration Fix (2026-02-06)

```text
1647: ---
1648: 
1649: ## A-Restoration Fix (2026-02-06)
1650: 
1651: **Summary:** Fixed critical foma syntax bug causing A-restoration to apply unconditionally, 
```

#### Germanic/docs/DEV_NOTES.md:1651 (note keyword: A-restoration)

- Nearby heading: ## A-Restoration Fix (2026-02-06)

```text
1649: ## A-Restoration Fix (2026-02-06)
1650: 
1651: **Summary:** Fixed critical foma syntax bug causing A-restoration to apply unconditionally, 
1652: then implemented chronology fix to move apocope after restoration.
1653: 
```

#### Germanic/docs/DEV_NOTES.md:1704 (note keyword: A-restoration)

- Nearby heading: ## A-Restoration Fix (2026-02-06)

```text
1702:   - Also expanded `OldEnglishARestorationBackVowel` to include `{*ă}` and `{*ą}` (reduced back vowels),
1703:     and expanded `OldEnglishARestorationStrongOTail` to include common weak-tail patterns where
1704:     A-restoration should still apply (infinitives, agent nouns, etc.).
1705:   - Result: `fronting_missing_no_trigger` dropped from 30 to 11 (19 words fixed).
1706: - Top mismatch counts (2026-02-06 report; 280 total at the time):
```

#### Germanic/docs/DEV_NOTES.md:3151 (exact COUNTERPART)

- Nearby heading: ### Impact

```text
3149: ### Impact
3150: - No regressions. 106 mismatches (unchanged). Health check clean.
3151: - All A-restoration-dependent forms verified: bacan, wadan, wascan, hlaþan, grafan, ġeall, hamer all correct.
3152: 
3153: ---
```

#### Germanic/docs/DEV_NOTES.md:9504 (exact COUNTERPART)

- Nearby heading: ### Empirical Validation (Dry Run 2026-03-13)

```text
9502:    - `*wadaną` → `*wadăną` (wadan)
9503:    - `*wakaną` → `*wakăną` (wacan)
9504:    - `*waskaną` → `*waskăną` (wascan)
9505: 
9506: **Results (targeted forms):**
```

#### Germanic/docs/DEV_NOTES.md:9512 (exact COUNTERPART)

- Nearby heading: ### Empirical Validation (Dry Run 2026-03-13)

```text
9510: wadăną → wadan ✓ (was wæden)
9511: wakăną → wacan ✓ (was wæcen)
9512: waskăną → wascan ✓ (was wæscen)
9513: weljăną → willan ✓ (was willen)
9514: ```
```

#### Germanic/docs/DEV_NOTES.md:36566 (exact COUNTERPART)

- Nearby heading: #   3. an sC-cluster (e.g. wascan, ascan, flascan, brastlian);

```text
36564: #      faran, sparian, warian, talian, sadol, nafola, gafol, hara, mara);
36565: #   2. a geminate (e.g. hnappian, racca, crabba, mattuc — Luick §161.2);
36566: #   3. an sC-cluster (e.g. wascan, ascan, flascan, brastlian);
36567: #   4. an fC-cluster (e.g. sæftriende — Campbell §158).
36568: # Other clusters (Cr, Cl, Cn, Cm, Ct, Cb, Cp, hC, etc.) BLOCK retraction
```

### Analysis and dossier hits

#### Germanic/docs/analysis/arestoration_r_l_research.md:83 (exact COUNTERPART)

- Nearby heading: ### 2.1 Campbell, *Old English Grammar* (1959) — file `campbell_old_english_grammar.txt`

```text
82: >
83: > *a* is commonly restored also before groups consisting of *f* or *s* followed by another consonant, e.g. *\*wascan* wash, *asce* ash, *flasce* flask (after inflected *ascan*, *flascan*), *brastlian* crackle, *sæftriende* rheumatic. **Before other groups, *a* is not restored except for a few instances before consonant plus liquid:** W-S *appla, apla* apples, *watrode* he watered, Angl. (Rit., Ru.) *accras, acras* fields, beside *æplas, æcras, weterode*, and always *sægdon, hæfdon, fedras, næglas*, &c. Yet it need not be doubted that *a* was originally widely restored before groups, and that it was subsequently removed by the analogy of forms in which a front vowel followed. This is reflected by some doublets, e.g. *gæfel, gafol* tribute, *hægel, hagol* hail, *fægen, fagen* glad, *wæcer, wacor* awake … (emphasis added)
84: 
```

#### Germanic/docs/analysis/arestoration_r_l_research.md:214 (exact COUNTERPART)

- Nearby heading: ### 2.5 Luick, *Historische Grammatik der englischen Sprache* — file `luick_historische_grammatik.txt`

```text
213: >
214: > 3. vielfach vor *s+Kons.* und *f+Kons.* (während vor *h+Kons.* Brechung eingetreten war): *wascan* waschen, *ascan* plur. 'Aschen' …, *flascan* Flaschen …, *brastlian* krachen, *wrastlian* ringen, *sæftriende* rheumatisch usw.;
215: >
```

#### Germanic/docs/analysis/arestoration_r_l_research.md:625 (exact COUNTERPART)

- Nearby heading: #   3. an sC-cluster (e.g. wascan, ascan, flascan, brastlian — Luick §161.3);

```text
624: #   2. a geminate (e.g. hnappian, racca, crabba, mattuc, cassuc — Luick §161.2);
625: #   3. an sC-cluster (e.g. wascan, ascan, flascan, brastlian — Luick §161.3);
626: #   4. an fC-cluster (e.g. sæftriende — Campbell §158).
```

#### Germanic/docs/analysis/compound_archaism_inventory.md:188 (note keyword: A-restoration)

- Nearby heading: ### Case 8: *rastō (rest) — ræst / ræste

```text
187: | **OE NOM.SG. (STANDARD)** | `ræst` (attested as dictionary headword; shows **paradigmatic leveling** from oblique *-æ-* stem) |
188: | **OE OBLIQUE (GEN.SG./ACC.SG./DAT.SG.)** | `ræste` (front vowel throughout, no A-restoration) |
189: | **Sound changes** | AFB (A-restoration trigger = back vowel in suffix *-u*; fires in nom.sg., blocked in obliques with front *-æ*, *-e*) |
```

#### Germanic/docs/analysis/compound_archaism_inventory.md:189 (note keyword: A-restoration)

- Nearby heading: ### Case 8: *rastō (rest) — ræst / ræste

```text
188: | **OE OBLIQUE (GEN.SG./ACC.SG./DAT.SG.)** | `ræste` (front vowel throughout, no A-restoration) |
189: | **Sound changes** | AFB (A-restoration trigger = back vowel in suffix *-u*; fires in nom.sg., blocked in obliques with front *-æ*, *-e*) |
190: | **Lautgesetzlich output** | `rast` (nom.sg., from A-restoration + apocope) BUT oblique cells show `ræste` (front *æ* from AFB, no restoration) |
```

#### Germanic/docs/analysis/compound_archaism_inventory.md:190 (note keyword: A-restoration)

- Nearby heading: ### Case 8: *rastō (rest) — ræst / ræste

```text
189: | **Sound changes** | AFB (A-restoration trigger = back vowel in suffix *-u*; fires in nom.sg., blocked in obliques with front *-æ*, *-e*) |
190: | **Lautgesetzlich output** | `rast` (nom.sg., from A-restoration + apocope) BUT oblique cells show `ræste` (front *æ* from AFB, no restoration) |
191: | **Attested simplex** | `ræst` (standard headword, showing paradigmatic leveling of oblique *-æ-* back to nom.sg.) |
```

#### Germanic/docs/analysis/notable_findings.md:13 (note keyword: A-restoration)

- Nearby heading: ## Table of Contents

```text
12: 3. [PWGmc \*j-related sound changes: formalization of under-specified rules](#3-pwgmc-j-related-sound-changes-formalization-of-under-specified-rules)
13: 4. [A-restoration trigger set: {*æ} is NOT a trigger](#4-a-restoration-trigger-set-æ-is-not-a-trigger)
14: 5. [The stefn/stemn problem: transponent versus reconstruction](#5-the-stefnstemn-problem-transponent-versus-reconstruction)
```

#### Germanic/docs/analysis/notable_findings.md:796 (exact COUNTERPART)

- Nearby heading: ## 4. A-restoration trigger set: {*æ} is NOT a trigger

```text
795: consonants and geminates," then: "a is commonly restored also before groups
796: consisting of f or s followed by another consonant, e.g. wascan wash, asce
797: ash...Before other groups, a is not restored except for a few instances
```

#### Germanic/docs/analysis/unstressed_e_o_before_r.md:100 (note keyword: A-restoration)

- Nearby heading: ### A-restoration — RULED OUT for unstressed syllables

```text
99: 
100: ### A-restoration — RULED OUT for unstressed syllables
101: 
```

#### Germanic/docs/analysis/unstressed_e_o_before_r.md:103 (note keyword: A-restoration)

- Nearby heading: ### A-restoration — RULED OUT for unstressed syllables

```text
102: R/T §6.3.1: "those **stressed** \*æ which were immediately followed by a single
103: or geminate consonant... followed by a back vowel became a." A-restoration
104: explicitly applies to **stressed** vowels only. It would not affect the unstressed
```

#### Germanic/docs/analysis/ws_vs_anglian_dialect_differences.md:391 (note keyword: A-restoration)

- Nearby heading: ## 4. Retraction and a-restoration

```text
390: 
391: ## 4. Retraction and a-restoration
392: 
```

#### Germanic/docs/analysis/ws_vs_anglian_dialect_differences.md:393 (note keyword: A-restoration)

- Nearby heading: ## 4. Retraction and a-restoration

```text
392: 
393: a-restoration: Prim. OE `æ` reverts to `a` in open syllables when a back
394: vowel follows in the next syllable. Campbell §157 introduces this as "one
```

#### Germanic/docs/analysis/ws_vs_anglian_dialect_differences.md:419 (note keyword: A-restoration)

- Nearby heading: ## 4. Retraction and a-restoration

```text
418: fronting of /a/ to /a/ or /æ/" — i.e. this is the input to second fronting
419: (see §6 below), distinct from a-restoration proper.
420: 
```

### Local lexical-table hits

#### old_english_wiktionary.tsv

| ENGLISH | OE_FORM | SOURCE | DETAIL | PAGE |
| :--- | :--- | :--- | :--- | :--- |
| wash | wasċan | inh | template:inh | wash |

#### old_english_swadesh.tsv

_None_

## Possibly stale or diagnostic evidence

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:9538 (concept name)

- Nearby heading: ### Empirical Validation (Dry Run 2026-03-13)

```text
9536: **Mismatch count:** 78 → 79 (net +1 WORSE)
9537: 
9538: - **Fixed: 6** (bake, grave, wade, wake, wash, will)
9539: - **Regressed: 9** (craft, day, mast, raven, staff, tap, wain, lap, wasp)
9540: 
```

#### Germanic/docs/DEV_NOTES.md:30401 (concept name)

- Nearby heading: ###### §158 (the consonant-environment statement — *the* relevant statement, ref. line 4727ff.)

```text
30399: >
30400: > *a* is commonly restored also **before groups consisting of *f* or *s*
30401: > followed by another consonant**, e.g. *waścan* wash, *asce* ash,
30402: > *flasce* flask (after inflected *ascan, flascan*), *brastlian* crackle,
30403: > *sæftriende* rheumatic. **Before other groups, *a* is not restored
```

### Analysis and dossier hits

_None_

## Bibliography-key candidates

### Preferred candidates

| Key | Why it was selected |
| :--- | :--- |
| Campbell1959 | single available key for Campbell |
| Luick1914 | single available key for Luick |

### Low-confidence candidates

_None_

