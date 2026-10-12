# Evidence packet — 2203 span / spanne

> This packet is evidence for drafting. Do not treat all hits as equally authoritative; prefer high-confidence evidence.

## TSV row data

| ID | CONCEPT | COUNTERPART | PROTO | PROTOFORM | DERIVATION_CLASS | NOTE | HISTORY |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2203 | span | spanne | *spannō | *spánnai | late_analogy | Dat.sg. paradigm-cell (Brunner §252). Fem. ō-stem dat.sg. *-ai preserves medial geminate; unstressed word-final *ai→*ē (R/T §6.1.5; §17.12). | See DEV_NOTES §fem-ō-stem-datsg. |

## Manifest status

| REPORT_PATH | STATUS |
| :--- | :--- |
| pilot/span.md | pilot |

## High-confidence evidence

### Compact derivation trace entry

```md
# span
PROTO: *spánnai
EXPECTED: spanne
OUTPUTS: spanne



### Proto-Germanic consonant inheritance

Proto Input: *spánnai

| Earlier Germanic developments | Old English developments |
|:---|:---|
| **Proto-West Germanic**<br>PWGmc Ai Monophthongization: *spánnē<br><br>**Northwest Germanic**<br>[no change] | **Old English**<br>OE Unstressed Long Vowel Shortening: *spánne |



### Orthography & surface

Outcome: spanne

NOTE: Dat.sg. paradigm-cell (Brunner §252). Fem. ō-stem dat.sg. *-ai preserves medial geminate; unstressed word-final *ai→ē (R/T §6.1.5; §17.12).
```

### Matching oe_known_problems.tsv entries

_None_

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:13940 (row ID)

- Nearby heading: ### Next Steps

```text
13938: 2. Add `{ai}:{*ai}` to pgrmWeakTailVowel (already done)
13939: 3. Test: `echo "spannai" | flookup -i old_english.bin` should give `spanne`
13940: 4. Update TSV row 2203 (span): proto `*spannai`, target `spanne`
13941: 5. Run mismatch report to verify improvement
13942: 
```

#### Germanic/docs/DEV_NOTES.md:28121 (exact pair)

- Nearby heading: ### §17.12.4 Verification

```text
28119: 
28120: - Mismatch count: 33 (unchanged from baseline).
28121: - `*spánnai → spanne` ✓ (dat.sg. with medial geminate
28122:   preserved, unstressed word-final *ai → *ē → *e).
28123: - No regression on stressed-*ai forms (e.g. `*stainaz`
```

### Analysis and dossier hits

_None_

## Supporting/background evidence

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:93 (note keyword: dat.sg.)

- Nearby heading: ### Could we use paradigm forms? (Why we decided not to)

```text
91: 
92: **Approach A: Use a u-stem or root-noun form.**
93: R/T notes that u-stems and root nouns regularly preserve *u because their paradigms have predominantly high-vowel suffixes (nom.sg. *-uz, acc.sg. *-ŷ, gen.sg. *-iz, dat.sg. *-i, nom.pl. *-iz, etc.). For example, *lustuz (u-stem nom.sg.) → OE lust with preserved u (R/T p.45). If *wulf-, *fugl-, or *bukk- were u-stems, we could use the nom.sg. in *-uz.
94: 
95: **What weighs against Approach A:**
```

#### Germanic/docs/DEV_NOTES.md:742 (note keyword: dat.sg.)

- Nearby heading: ### The milk problem: `*melukz` → `meoloc` (expected `meolc`)

```text
740: with paradigm variation:
741: - Nom.sg.: `*melukz` → `meoloc` (with breaking `e → eo`, no syncope)
742: - Gen./dat.sg.: `*milukiz/*miluki` → Anglian `milc` (with i-umlaut and syncope)
743: 
744: R/T §6.6.4 (p.253): "The usual WS form of 'milk' is `meolc < meoluc < *meluk`... 
```

#### Germanic/docs/DEV_NOTES.md:763 (note keyword: dat.sg.)

- Nearby heading: ### The milk problem: `*melukz` → `meoloc` (expected `meolc`)

```text
761: **Possible explanations:**
762: 
763: 1. **Paradigmatic leveling:** The syncopated form `milc` (< gen./dat.sg. `*milyci` 
764:    with heavy syllable from consonant cluster) was generalized to nom./acc.
765:    
```

#### Germanic/docs/DEV_NOTES.md:1773 (note keyword: dat.sg.)

- Nearby heading: ## A-Restoration Fix (2026-02-06)

```text
1771:     - `*fuwer → fȳr`: no rule converts `{uw}` before `{r}` into `{ȳr}`; add a `{uw}` contraction (or targeted `ur` rounding) so `fūr`-class stems reach OE fȳr.
1772:     - `*xattuz → hōd`: expected reflex doesn’t match the provided proto stem (phonologically it yields OE “hat”); fix data alignment rather than phonology.
1773:   - 2026-01-10b data note: the “fire” row now uses dat.sg. *fūri (> fȳre) to avoid modelling nominative levelling; see TSV comment.
1774:   - 2026-01-10 rollback: backed out the short-diphthong lengthening experiment; diagnostics back to the post-*fūri* baseline (293 mismatches) with `slaxăną` still in the long-vowel bucket for future work.
1775: 
```

#### Germanic/docs/DEV_NOTES.md:3195 (note keyword: dat.sg.)

- Nearby heading: ### Case 1: *rastō → rast (expected ræst) — ō-stem feminine

```text
3193: - Acc.sg. *rastō̃ → PWGmc *rasta → AFB *ræstæ → ræste (front suffix, no restoration)
3194: - Gen.sg. *rastōz → PWGmc *rasta → AFB *ræstæ → ræste (front suffix, no restoration)
3195: - Dat.sg. *rastōi → PWGmc *rastē → AFB (no *a in suffix to front) → ræste (no restoration)
3196: 
3197: Only the nom.sg. has the back suffix *-u that triggers A-restoration. All oblique cases (acc., gen., dat.) have front suffix vowels → no restoration → ræst- throughout. The majority oblique pattern was generalized to the nom.sg.: ræst.
```

#### Germanic/docs/DEV_NOTES.md:3202 (note keyword: dat.sg.)

- Nearby heading: ### Case 1: *rastō → rast (expected ræst) — ō-stem feminine

```text
3200: 
3201: **Sources:**
3202: - BT: headword "ræst" f. 'rest, repose, bed, grave'. Oblique forms: ræste (gen./dat.sg.).
3203: - Kroonen (p.420): *rasto- f. 'interval' — Go. rasta, ON rost, OE rest, OS rasta, OHG rasta. (Kroonen gives OE "rest", i.e. ræst with late OE æ→e.)
3204: - R/T §6.3.1–6.3.2: paradigmatic alternation between a and æ due to A-restoration is explicitly discussed for a-stems (dæg/dagas); same logic applies to ō-stems.
```

#### Germanic/docs/DEV_NOTES.md:13828 (exact COUNTERPART)

- Nearby heading: ### Problem

```text
13826:   ```
13827: - Word-final `*a` (no following consonant) does NOT front
13828: - Result: `*spannāz → *spannā → *spanna → spanna` (wrong, expected `spanne`)
13829: 
13830: ### Attempted solutions
```

#### Germanic/docs/DEV_NOTES.md:13861 (exact COUNTERPART)

- Nearby heading: ### Solution: Use dat.sg. instead of gen.sg.

```text
13859: **Proposed:**
13860: - Add dat.sg. `*-ai` to pgrmWeakTailVowel
13861: - Use `*spannai → spanne` for the paradigm-cell mapping
13862: 
13863: **Scholarly justification:**
```

#### Germanic/docs/DEV_NOTES.md:13918 (exact COUNTERPART)

- Nearby heading: # - Stressed *ai → *ā (elsewhere, including word-initial)

```text
13916: 1. Input: `*spannai` (dat.sg. of fem. ō-stem)
13917: 2. `PWGmcAiMonophthongization`: `*ai → *ē` (unstressed) → `*spannē`
13918: 3. `OEUnstressedLongVowelShortening`: `*ē → *e` → `*spanne`
13919: 4. Final: `spanne` ✓
13920: 
```

#### Germanic/docs/DEV_NOTES.md:13919 (exact COUNTERPART)

- Nearby heading: # - Stressed *ai → *ā (elsewhere, including word-initial)

```text
13917: 2. `PWGmcAiMonophthongization`: `*ai → *ē` (unstressed) → `*spannē`
13918: 3. `OEUnstressedLongVowelShortening`: `*ē → *e` → `*spanne`
13919: 4. Final: `spanne` ✓
13920: 
13921: ### Input Notation
```

#### Germanic/docs/DEV_NOTES.md:13926 (exact COUNTERPART)

- Nearby heading: ### Input Notation

```text
13924: mark that this diphthong is in unstressed position. This would make the TSV entry:
13925: - Proto: `*spannăi`
13926: - Target: `spanne`
13927: 
13928: This parallels our existing convention where `*ă` marks unstressed short vowels 
```

#### Germanic/docs/DEV_NOTES.md:13939 (exact COUNTERPART)

- Nearby heading: ### Next Steps

```text
13937: 1. Update `PWGmcAiMonophthongization` with context-sensitive rule
13938: 2. Add `{ai}:{*ai}` to pgrmWeakTailVowel (already done)
13939: 3. Test: `echo "spannai" | flookup -i old_english.bin` should give `spanne`
13940: 4. Update TSV row 2203 (span): proto `*spannai`, target `spanne`
13941: 5. Run mismatch report to verify improvement
```

#### Germanic/docs/DEV_NOTES.md:28099 (exact PROTOFORM)

- Nearby heading: ### §17.12.3 Implementation

```text
28097: ### §17.12.3 Implementation
28098: 
28099: 1. **TSV**: row 1057 `*spánnăi → *spánnai`.
28100: 2. **Grammar** (`germanic.txt`):
28101:    - Delete `pgrmUnstressedDiphthong` (was `{ăi}:{*ăi}`).
```

### Analysis and dossier hits

#### Germanic/docs/analysis/compound_archaism_inventory.md:30 (note keyword: dat.sg.)

- Nearby heading: ## Introduction

```text
29: - **Dialectal doublets** — one OE dialect retains the lautgesetzlich form while another shows analogical leveling. Anglian forms are particularly prone to this because of conservative scribal traditions in Bede glosses, the Vespasian Psalter, and parts of the poetic corpus.
30: - **Oblique paradigm cells** — non-nominative cases (gen.sg., dat.sg., pl.) sometimes retain forms that the nom.sg. has lost.
31: - **Plurals** that resisted paradigmatic regularization.
```

#### Germanic/docs/analysis/compound_archaism_inventory.md:58 (note keyword: dat.sg.)

- Nearby heading: ### Case 1: *mízdō (reward, wage) — meord (dialectal doublet, NOT compound)

```text
57: | **Preservation locus** | **Dialectal doublet** — not a compound. The lautgesetzlich post-rhotacism + breaking output (*z → r*; *i → eo / _r+C*) is preserved as the Anglian-leaning simplex *meord*, while WS shows the post-z-loss outcome *mēd* (z-loss + comp. lengthening + lowering of long *ī to ē). |
58: | **Primary witnesses for meord** | (i) **BT Supplement** s.v. *meord*: OE Bede 4.17, Schipper 549.7 (form *meorde*, dat.sg.); (ii) **Bright's Anglo-Saxon Reader**, line 12498 of repo OCR — *"þæs him meorde wile ... eadge forgyldan"* (likely *Phoenix*); glossary marks "(dial.)"; (iii) **Hall's Concise** s.v. *meard*: lists *meord* as a real headword. |
59: | **Lautgesetzlich output** | **meord** ✓ (FST currently produces this from `*mizdō`). |
```

#### Germanic/docs/analysis/compound_archaism_inventory.md:132 (note keyword: dat.sg.)

- Nearby heading: ### Case 5: *nábulō (navel) — nafola / nafela

```text
131: | **OE ATTESTED** | `nafola` (early, preserving medial *u → *o vowel-harmony stage); `nafela` (later WS majority, showing vowel-harmony *o → *e*) |
132: | **OE OBLIQUE** | `nafolan` (nom.sg./gen.sg./dat.sg./acc.sg. oblique, all showing *a*; preserved in strong n-stem declension) |
133: | **Sound changes** | Vowel harmony: *u → *o (medial reduction), then *o → *e (harmony with front root vowel) |
```

#### Germanic/docs/analysis/cow_root_noun_investigation.md:48 (note keyword: dat.sg.)

- Nearby heading: ### OE paradigm of cū (§6.6.1, line 18238)

```text
47: - **nom.sg.** cū (< leveled *kū, analogical from oblique)
48: - **dat.sg.** cȳ (< *kūi, regular i-umlaut: ū → ȳ)
49: - **nom.-acc.pl.** cȳ (< *kūiz, same i-umlaut)
```

#### Germanic/docs/analysis/cow_root_noun_investigation.md:57 (note keyword: dat.sg.)

- Nearby heading: ### Hall's Concise Anglo-Saxon Dictionary

```text
56: - gen.sg. cū(e), cȳ, or cūs (multiple competing forms — inherited umlaut cȳ vs. analogical -e/-s from other classes)
57: - dat.sg. cȳ
58: - nom.-acc.pl. cȳ
```

#### Germanic/docs/analysis/cow_root_noun_investigation.md:70 (note keyword: dat.sg.)

- Nearby heading: ## Full PGmc paradigm reconstruction (Wiktionary + Kroonen + R/T)

```text
69: | gen.sg. | *kūiz | cā (or cȳ, cū(e)) | cȳ would be regular i-umlaut; cā is uncertain |
70: | dat.sg. | *kūi | cȳ | **Lautgesetzlich**: i-umlaut ū → ȳ, then contraction/loss of *-i |
71: | nom.pl. | *kōiz | cȳ | Mixed: zero-grade stem + umlaut (analogical from oblique?) |
```

#### Germanic/docs/analysis/meord_med_chronological_review.md:627 (note keyword: dat.sg.)

- Nearby heading: ### 2.21 Lexicographical witnesses (Bosworth–Toller, Bright, Hall)

```text
626: in §1 — all three list *meord* as a real lemma cross-referenced to
627: *mēd*, with *meorde* (dat.sg.) the actual attested form. No source
628: in the local repo cites a bare nom.sg. attestation of *meord* — it is
```

#### Germanic/docs/analysis/meord_med_chronological_review.md:629 (note keyword: dat.sg.)

- Nearby heading: ### 2.21 Lexicographical witnesses (Bosworth–Toller, Bright, Hall)

```text
628: in the local repo cites a bare nom.sg. attestation of *meord* — it is
629: universally a lexicographer's reconstruction from the dat.sg. obliques.
630: 
```

#### Germanic/docs/analysis/meord_med_chronological_review.md:692 (note keyword: dat.sg.)

- Nearby heading: ## 3. Synthesis: which authors support which hypothesis?

```text
691:    §2.10/§2.11 above). No author proposes that, e.g., *mizdai*
692:    (dat.sg.) gives *meorde* lautgesetzlich while *mizdō* (nom.sg.)
693:    gives *mēd* lautgesetzlich, with later levelling.
```

#### Germanic/docs/analysis/notable_findings.md:709 (note keyword: dat.sg.)

- Nearby heading: ## 4. A-restoration trigger set: {*æ} is NOT a trigger

```text
708: 
709: | | nom.sg. | gen.sg. | dat.sg. | nom.pl. | dat.pl. |
710: |---|---|---|---|---|---|
```

#### Germanic/docs/analysis/notable_findings.md:747 (note keyword: dat.sg.)

- Nearby heading: ## 4. A-restoration trigger set: {*æ} is NOT a trigger

```text
746: of the type fæt ~ fatu, we do find in Old English minimal pairs such as
747: fare 'journey' dat.sg.masc. vs. fare 'journey' dat.sg.fem." But he
748: concedes "the case for therefore assuming a phonemic contrast between /æ/
```

#### Germanic/docs/analysis/notable_findings.md:1609 (note keyword: dat.sg.)

- Nearby heading: ## 11. PGmc \*mizdō 'reward': the méd / meord dialectal doublet and z-loss before dentals

```text
1608: - **meord** — a less frequent dialectal variant, attested in BT Supplement
1609:   s.v. *meord* (citing OE Bede 4.17, Schipper 549.7; form *meorde* dat.sg.),
1610:   in Bright's *Anglo-Saxon Reader* (in a poetic line, glossed "(dial.)"), and
```

#### Germanic/docs/analysis/unstressed_e_o_before_r.md:75 (note keyword: dat.sg.)

- Nearby heading: ### For \*mōdēr

```text
74:   later reflex" (i.e. leveled from paradigm forms with back vowels)
75: - The regular outcome is -er (cf. dat.sg. mēder, brēder from \*-ri)
76: - The -or/-ur forms have the back vowel **leveled in** from other case forms
```

#### Germanic/docs/analysis/unstressed_e_o_before_r.md:173 (note keyword: dat.sg.)

- Nearby heading: ### 3. \*mōdēr/mōdor → fix target

```text
172: The regular neogrammarian nom.sg. outcome is "mōder" (via \*ē → \*ǣ → e).
173: R/T: early WS "modor ~ -ur" alongside dat.sg. "mēder" (regular, from \*-ri).
174: 
```

#### Germanic/docs/analysis/unstressed_e_o_before_r.md:176 (note keyword: dat.sg.)

- Nearby heading: ### 3. \*mōdēr/mōdor → fix target

```text
175: Note for TSV: "R/T §7.2.1: 'modor ~ -ur' has suffixal vowel leveled from
176: oblique cases (analogical). Regular nom.sg. reflex is mōder (cf. dat.sg. mēder
177: < \*mōdri). The regular form mōder matches OE fæder < \*fader."
```

### Local lexical-table hits

#### old_english_wiktionary.tsv

| ENGLISH | OE_FORM | SOURCE | DETAIL | PAGE |
| :--- | :--- | :--- | :--- | :--- |
| span | spann | inh | template:inh | span |

#### old_english_swadesh.tsv

_None_

## Possibly stale or diagnostic evidence

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:10394 (concept name)

- Nearby heading: ## Mismatch Progress Log (2026-03-14)

```text
10392: | 2026-03-14 20:34 | 65 | -5 | 62fced4 | Participle nasalization fix (funden) |
10393: | 2026-03-19 | 57 | -8 | — | Multiple TSV/FST fixes (huniġ, thistle, etc.) |
10394: | 2026-04-05 | 55 | -2 | — | span fix (feminine ō-stem dat.sg.) |
10395: | 2026-04-06 | 52 | -3 | — | TSV fixes: dile, lappa, cnobba |
10396: | 2026-04-07 | 49 | -3 | 0a649b3 | būgan/sċūfan past 3pl paradigm cells |
```

#### Germanic/docs/DEV_NOTES.md:13790 (concept name)

- Nearby heading: # MUST use *a (not *ă) to undergo unstressed fronting: *a → *æ → *e

```text
13788: | 1936 | ban | `*banną` | ban | bann | word-final degemination |
13789: | 2119 | man | `*mannăz` | man | mann | word-final degemination |
13790: | 2203 | span | `*spannō` | span | spann | word-final degemination |
13791: | 2300 | wool | `*wullo` | wollo | wull | degemination + vowel |
13792: 
```

#### Germanic/docs/DEV_NOTES.md:13800 (concept name)

- Nearby heading: # MUST use *a (not *ă) to undergo unstressed fronting: *a → *æ → *e

```text
13798: 1. ✓ Updated row 2119 (man): proto `*mannas`, target `mannes`
13799: 2. ✓ Updated row 1936 (ban): proto `*bannas`, target `bannes` 
13800: 3. For span (fem. ō-stem), different paradigm — investigate separately
13801: 4. For wool, different issue (vowel) — investigate separately
13802: 
```

#### Germanic/docs/DEV_NOTES.md:13807 (concept name)

- Nearby heading: ## Fem. ō-stem gen.sg. paradigm-cell for span (2026-04-06)

```text
13805: ---
13806: 
13807: ## Fem. ō-stem gen.sg. paradigm-cell for span (2026-04-06)
13808: 
13809: ### Problem
```

#### Germanic/docs/DEV_NOTES.md:13811 (concept name)

- Nearby heading: ### Problem

```text
13809: ### Problem
13810: 
13811: For `*spannō → span` (expected `spann`), we want to use a paradigm-cell approach
13812: similar to what we did for masc. a-stems (mann, bann).
13813: 
```

#### Germanic/docs/DEV_NOTES.md:14032 (row ID)

- Nearby heading: ### Implementation completed (2026-04-06)

```text
14030:    ```
14031: 
14032: 6. **Updated TSV row 2203** (span):
14033:    - Proto: `*spannăi` (was `*spannās`)
14034:    - Target: `spanne`
```

### Analysis and dossier hits

#### Germanic/docs/analysis/fryhtu_investigation.md:149 (concept name)

- Nearby heading: ### The standard accounts

```text
148: regular from those where it is blocked; he notes only that "much irregularity
149: ensued, which could be levelled out through analogy." His examples span many
150: following-consonant environments (past tense *-d-, comparative *-r-, abstract
```

#### Germanic/docs/analysis/mismatch_dossier_mizdo.md:61 (note keyword: dat.sg.)

- Nearby heading: ### 2.1 Standard dictionary lemmata

```text
60: - Etymology: "from PGmc. *mizdō"
61: - Inflection: strong fem. ō-stem (nom.sg. mēd, acc.sg. mēd/mēde, gen.sg. mēde, dat.sg. mēde)
62: 
```

#### Germanic/docs/analysis/mismatch_dossier_mizdo.md:415 (note keyword: dat.sg.)

- Nearby heading: ### H2: Target switch to a paradigm cell that doesn't require breaking

```text
414: - **Gen.sg.**: `*mizdōz` → final *-ōz → PWGmc *-a → `*mirda` → breaking → `*meorda` → WS `*meorde`
415: - **Dat.sg.**: `*mizdōi` → `*mirdōi` → breaking → `*meordōi` → apocope → `*meorde`
416: 
```

#### Germanic/docs/analysis/mismatch_dossier_mizdo.md:626 (note keyword: dat.sg.)

- Nearby heading: ### Option 4: Switch to an oblique case form (paradigm-cell strategy)

```text
625: **Action**:
626: - **Change PROTOFORM** from nom.sg. `*mízdō` to gen.sg. `*mízdōz` or dat.sg. `*mízdōi`
627: - **Change COUNTERPART** to match expected oblique form (e.g., gen.sg. `*meorde`)
```

## Bibliography-key candidates

### Preferred candidates

| Key | Why it was selected |
| :--- | :--- |
| Kroonen2013 | default Proto-Germanic etymology key for Kroonen |
| BrightCassidyRingler1971 | single available key for Bright |

### Low-confidence candidates

| Key | Why it was selected |
| :--- | :--- |
| Kroonen2011 | surname mention only: Kroonen |
| Kroonen2006 | surname mention only: Kroonen |

## Paradigm probe

### Paradigm probe — span / spanne

- PROTO: *spannō
- PROTOFORM: *spánnai
- DERIVATION_CLASS: late_analogy
- Morphology source: Hand-specified pilot comparison for feminine ō-stem singular cells.
- ProtoGate bypassed: no
- Generated cells: nom.sg., dat.sg.
- Omitted cells: gen.sg. and plural cells omitted in v1; dat.sg. is the only selected cell explicitly justified in the row note and DEV_NOTES.
- Winning form unique: yes

| Cell | Candidate input | FST output | Match? | Comment |
|:---|:---|:---|:---|:---|
| nom.sg. | *spannō | span | no | Citation nominative singular. |
| dat.sg. | *spánnai | spanne | yes | Chosen dative singular cell in TSV. |

