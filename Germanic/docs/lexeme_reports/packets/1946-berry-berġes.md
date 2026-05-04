# Evidence packet — 1946 berry / berġes

> This packet is evidence for drafting. Do not treat all hits as equally authoritative; prefer high-confidence evidence.

## TSV row data

| ID | CONCEPT | COUNTERPART | PROTO | PROTOFORM | DERIVATION_CLASS | NOTE | HISTORY |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1946 | berry | berġes | *bázją | *bázjas | late_analogy | Note: using gen.sg. *bazjas (> berġes); R/T vol.2 §6.8.2: *rj did not geminate in PWGmc | Source: Wiktionary etymology (template:inh) \| Source: Wiktionary etymology (template:inh) |

## Manifest status

| REPORT_PATH | STATUS |
| :--- | :--- |
| pilot/berry.md | pilot |

## High-confidence evidence

### Compact derivation trace entry

```md
# berry
PROTO: *bázjas
EXPECTED: berġes
OUTPUTS: berġes



### Proto-Germanic consonant inheritance

Proto Input: *bázjas
Rhotacism: *bárjas

| Earlier Germanic developments | Old English developments |
|:---|:---|
| **Proto-West Germanic**<br>[no change]<br><br>**Northwest Germanic**<br>[no change] | **Old English**<br>Anglo Frisian Brightening: *bærjæs<br>OE I Umlaut: *berjæs<br>OE Unstressed AE Merger: *berjes |



### Orthography & surface

Old English Orthography: *berġes
Outcome: berġes

NOTE: Note: using gen.sg. *bazjas (> berġes); R/T vol.2 §6.8.2: *rj did not geminate in PWGmc
```

### Matching oe_known_problems.tsv entries

_None_

### DEV_NOTES hits

_None_

### Analysis and dossier hits

_None_

## Supporting/background evidence

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:93 (note keyword: gen.sg.)

- Nearby heading: ### Could we use paradigm forms? (Why we decided not to)

```text
91: 
92: **Approach A: Use a u-stem or root-noun form.**
93: R/T notes that u-stems and root nouns regularly preserve *u because their paradigms have predominantly high-vowel suffixes (nom.sg. *-uz, acc.sg. *-ŷ, gen.sg. *-iz, dat.sg. *-i, nom.pl. *-iz, etc.). For example, *lustuz (u-stem nom.sg.) → OE lust with preserved u (R/T p.45). If *wulf-, *fugl-, or *bukk- were u-stems, we could use the nom.sg. in *-uz.
94: 
95: **What weighs against Approach A:**
```

#### Germanic/docs/DEV_NOTES.md:1379 (exact COUNTERPART)

- Nearby heading: ### 1. PWGmcSyllabicJ: *ja/*ją → *i (after light syllable, word-finally)

```text
1377: **Conditioning:** After a light syllable (short vowel + single consonant), word-finally.
1378: **Examples in our data:**
1379: - *bazją → *bazi → berġes ('berry', gen.sg.)
1380: - *harjaz → *hari → here ('army')
1381: - *natją → *nati → net ('net')
```

#### Germanic/docs/DEV_NOTES.md:2733 (note keyword: gen.sg.)

- Nearby heading: ### The Three Fates of Word-Final *ō

```text
2731: - Examples: ō-stem acc.sg. *gebō(n?) → *gebō (after ending loss) → PWGmc
2732:     *geba → OE giefe
2733:   ō-stem gen.sg. *gebōz → *gebō (after z-loss) → PWGmc *geba → OE giefe
2734:   fem. n-stem nom.sg. *tungōn → *tungō̃ (after n-loss, nasalized) →
2735:     PWGmc *tunga → OE tunge
```

#### Germanic/docs/DEV_NOTES.md:2738 (note keyword: gen.sg.)

- Nearby heading: ### The Three Fates of Word-Final *ō

```text
2736: - **Our FST**: For fem. n-stems, modelled by NWGmcNStemNLoss: {*ō}{*n} →
2737:   {*ǭ} word-finally, then {*ǭ} → {*æ} → OE -e. This covers the n-stem case.
2738:   For other "surviving bimoric" cases (acc.sg., gen.sg. of ō-stems), we DON'T
2739:   have a rule — but these paradigm cells aren't in our TSV data.
2740: 
```

#### Germanic/docs/DEV_NOTES.md:3131 (note keyword: gen.sg.)

- Nearby heading: ### Root cause: {*æ} should NOT trigger A-restoration

```text
3129: ### Root cause: {*æ} should NOT trigger A-restoration
3130: 
3131: The `{*æ}` symbol was added to the A-restoration trigger set based on an incorrect analysis that suffix *a (like gen.sg. *-as), after being fronted to *æ by AFB, still triggers restoration as an "underlyingly back" vowel.
3132: 
3133: **R/T's paradigm disproves this (§6.3.2, p. 199):**
```

#### Germanic/docs/DEV_NOTES.md:3134 (note keyword: gen.sg.)

- Nearby heading: ### Root cause: {*æ} should NOT trigger A-restoration

```text
3132: 
3133: **R/T's paradigm disproves this (§6.3.2, p. 199):**
3134: - gen.sg. *dagas → *dæges → OE **dæges** (NOT *dages) — A-restoration does NOT fire
3135: - nom.pl. *dagos → OE **dagas** — A-restoration DOES fire (suffix *-os has genuine back *o)
3136: - dat.pl. *dagum → OE **dagum** — A-restoration DOES fire (suffix *-um has genuine back *u)
```

### Analysis and dossier hits

#### Germanic/docs/analysis/compound_archaism_inventory.md:30 (note keyword: gen.sg.)

- Nearby heading: ## Introduction

```text
29: - **Dialectal doublets** — one OE dialect retains the lautgesetzlich form while another shows analogical leveling. Anglian forms are particularly prone to this because of conservative scribal traditions in Bede glosses, the Vespasian Psalter, and parts of the poetic corpus.
30: - **Oblique paradigm cells** — non-nominative cases (gen.sg., dat.sg., pl.) sometimes retain forms that the nom.sg. has lost.
31: - **Plurals** that resisted paradigmatic regularization.
```

#### Germanic/docs/analysis/compound_archaism_inventory.md:132 (note keyword: gen.sg.)

- Nearby heading: ### Case 5: *nábulō (navel) — nafola / nafela

```text
131: | **OE ATTESTED** | `nafola` (early, preserving medial *u → *o vowel-harmony stage); `nafela` (later WS majority, showing vowel-harmony *o → *e*) |
132: | **OE OBLIQUE** | `nafolan` (nom.sg./gen.sg./dat.sg./acc.sg. oblique, all showing *a*; preserved in strong n-stem declension) |
133: | **Sound changes** | Vowel harmony: *u → *o (medial reduction), then *o → *e (harmony with front root vowel) |
```

#### Germanic/docs/analysis/compound_archaism_inventory.md:176 (note keyword: gen.sg.)

- Nearby heading: ### Case 7: *fúwerō / *fūri (fire) — fȳre (dat.sg.) vs. fȳr (nom.sg.)

```text
175: | **Classification** | **Paradigm-cell case**: The dat.sg. `*fūri` → `fȳre` shows a **post-apocope analogical restoration** of the dative ending *-e (generalized from other weak stems). The nom.sg. `fȳr` is the pure lautgesetzlich product. The TSV targets the dat.sg. cell (`*fūri → fȳre`) because it preserves the original singular form; it is not a compound/fossil case but a **methodological choice to target oblique cells over analogically-restored nominatives**. |
176: | **Methodological use** | Parallel to cow (*kūi → cȳ*), night (*naxti → niht*), hammer (*xamaras → hameres*): when the lautgesetzlich nominative singular has been analogically restored with extraneous endings, the TSV explicitly targets the oblique paradigm cell (dat.sg., gen.sg., etc.) whose lautgesetzlich outcome is derivable. |
177: | **Implementation** | TSV targets proto `*fūri` (dat.sg.) with target `fȳre`. The FST produces `fȳr` (nom.sg.), which is actually lautgesetzlich; the mismatch is resolved by understanding that `fȳre` is the attested dat.sg. form (post-apocope restoration). |
```

#### Germanic/docs/analysis/cow_root_noun_investigation.md:50 (note keyword: gen.sg.)

- Nearby heading: ### OE paradigm of cū (§6.6.1, line 18238)

```text
49: - **nom.-acc.pl.** cȳ (< *kūiz, same i-umlaut)
50: - **gen.sg.** cā (< *kūiz? — form uncertain, R/T say "apparently")
51: - **dat.pl.** cūm (< *kūm(az))
```

#### Germanic/docs/analysis/cow_root_noun_investigation.md:56 (note keyword: gen.sg.)

- Nearby heading: ### Hall's Concise Anglo-Saxon Dictionary

```text
55: Hall's confirms:
56: - gen.sg. cū(e), cȳ, or cūs (multiple competing forms — inherited umlaut cȳ vs. analogical -e/-s from other classes)
57: - dat.sg. cȳ
```

#### Germanic/docs/analysis/cow_root_noun_investigation.md:69 (note keyword: gen.sg.)

- Nearby heading: ## Full PGmc paradigm reconstruction (Wiktionary + Kroonen + R/T)

```text
68: | acc.sg. | *kōų | cū | Possibly regular (acc. *kōų > *kū after loss of *-ų?), but uncertain |
69: | gen.sg. | *kūiz | cā (or cȳ, cū(e)) | cȳ would be regular i-umlaut; cā is uncertain |
70: | dat.sg. | *kūi | cȳ | **Lautgesetzlich**: i-umlaut ū → ȳ, then contraction/loss of *-i |
```

#### Germanic/docs/analysis/meord_med_chronological_review.md:809 (note keyword: gen.sg.)

- Nearby heading: ## 5. FST-probe relevance

```text
808: 4. The FST output of `meorde` from BOTH `mizdai` (dat.sg.) and
809:    `mizdōz` (gen.sg.) is striking: it means the **paradigm-cell
810:    targeting** approach (the user's preferred framing under
```

#### Germanic/docs/analysis/notable_findings.md:504 (exact COUNTERPART)

- Nearby heading: ## 3. PWGmc \*j-related sound changes: formalization of under-specified rules

```text
503: but not explicitly stated as a rule. Our implementation successfully derives:
504: \*bazją → \*bazi → berġes, \*harjaz → \*hari → here, \*natją → \*nati → net.
505: 
```

#### Germanic/docs/analysis/notable_findings.md:581 (note keyword: gen.sg.)

- Nearby heading: ## 3. PWGmc \*j-related sound changes: formalization of under-specified rules

```text
580: all the environments in which it might be expected." The examples are
581: instructive: Go. ja-stem gen.sg. harjis 'army' (light stem: *j retained)
582: vs. hairdeis 'herdsman' (heavy stem: *ij > *i), but jō-stems show no
```

#### Germanic/docs/analysis/notable_findings.md:585 (note keyword: gen.sg.)

- Nearby heading: ## 3. PWGmc \*j-related sound changes: formalization of under-specified rules

```text
584: bandi 'band' and mawi 'maiden'"), and even ja-stems have exceptions:
585: "gen.sg. arbjis 'heritage' for expected *arbeis."
586: 
```

#### Germanic/docs/analysis/unstressed_e_o_before_r.md:66 (note keyword: gen.sg.)

- Nearby heading: ### For \*sumaraz and \*xamaras

```text
65: 4. Both `hamor` and `hamer` are **attested** (Wiktionary: "OE hamor, hamer, homer")
66: 5. Hall's dictionary gives gen.sg. **sumeres** (with -e-), confirming -e- in oblique forms
67: 
```

#### Germanic/docs/analysis/unstressed_e_o_before_r.md:150 (note keyword: gen.sg.)

- Nearby heading: ### 1. \*sumerăz/sumor → fix proto AND target

```text
149: "sumer" (via \*a → \*æ by a-fronting → e by unstressed æ/i merger). Both forms
150: are attested (Kroonen: "OE sumer, sumor m."; Hall's: gen.sg. "sumeres").
151: 
```

### Local lexical-table hits

#### old_english_wiktionary.tsv

| ENGLISH | OE_FORM | SOURCE | DETAIL | PAGE |
| :--- | :--- | :--- | :--- | :--- |
| berry | berġe | inh | template:inh | berry |

#### old_english_swadesh.tsv

_None_

## Possibly stale or diagnostic evidence

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:90 (concept name)

- Nearby heading: ### Could we use paradigm forms? (Why we decided not to)

```text
88: ### Could we use paradigm forms? (Why we decided not to)
89: 
90: For other problematic items (fire, brand, berry, thorn), we successfully resolved mismatches by adopting a paradigm form in which the phonological development is lautgesetzlich. The question is whether the same approach works for the u-lowering exceptions.
91: 
92: **Approach A: Use a u-stem or root-noun form.**
```

#### Germanic/docs/DEV_NOTES.md:1535 (concept name)

- Nearby heading: ## Proto-West Germanic Stage Implementation (2026-02-07) - EARLIER

```text
1533: 4. **Denasalization of final nasal vowels** (§3.1.4): *ą → *a, *ę → *e, etc.
1534: 
1535: **Test case: 'berry' (PGmc *bazją → PWGmc *bazi → OE berġe)**
1536: 
1537: Step-by-step per sources:
```

#### Germanic/docs/DEV_NOTES.md:2547 (concept name)

- Nearby heading: ### OE diagnostics follow‑up: orthography + rhotacism (2025-12-22)

```text
2545: - Tracing those 7 (`bazją`, `deuzą`, `xazwăz`, `xuzdą`, `liznōjăną`, `mizdō`, `funxwstiz`) shows `EnglishZRhotacism` never fires; `ConsonantRules` leaves `{*z}` intact in every case.
2546: - Likely structural issue: `EnglishStarVocalic` (and other `EnglishStar*`) are defined before `GermanStar*` and appear to compile as literal symbols (foma logs show 1‑arc sets), so the rhotacism context never matches.
2547: - Even if the set is fixed, the current rule `V _ V` is historically too narrow: PGmc *z should rhotacize in post‑vocalic contexts like V‑z‑j/w/n/d‑V (berry, hair, learn, meed, hoard) before later glide/umlaut changes. Chronology: rhotacism must be early (before w‑glide changes and OE vowel rules).
2548: - `funxwstiz` (fist) is not a rhotacism case; it survives with a heavy `xʋst` cluster and fails the OE surface coda limit (needs separate cluster simplification / h‑loss logic).
2549: 
```

### Analysis and dossier hits

#### Germanic/docs/analysis/final_vowel_missing_analysis.md:10 (concept name)

- Nearby heading: ### Example: 'berry'

```text
9: 
10: ### Example: 'berry'
11: - **PGmc**: `*bazją` (neut. nom.-acc.sg. ja-stem with nasal vowel)
```

#### Germanic/docs/analysis/mismatch_dossier_mizdo.md:61 (note keyword: gen.sg.)

- Nearby heading: ### 2.1 Standard dictionary lemmata

```text
60: - Etymology: "from PGmc. *mizdō"
61: - Inflection: strong fem. ō-stem (nom.sg. mēd, acc.sg. mēd/mēde, gen.sg. mēde, dat.sg. mēde)
62: 
```

#### Germanic/docs/analysis/mismatch_dossier_mizdo.md:260 (note keyword: gen.sg.)

- Nearby heading: ### 3.5 Pathway reconciliation

```text
259: **Option 2**: Analogical leveling from oblique cases
260: - If oblique forms like gen.sg. `*mirdōz` underwent cluster simplification (*rd → *d) early, and the resulting `*mīdōz` was then generalized to the nominative, bypassing the breaking that would have applied to the nom.sg. form
261: - This is highly speculative and lacks parallels
```

#### Germanic/docs/analysis/mismatch_dossier_mizdo.md:414 (note keyword: gen.sg.)

- Nearby heading: ### H2: Target switch to a paradigm cell that doesn't require breaking

```text
413: - **Acc.sg.**: `*mizdō` → same as nom.sg. → `meord`
414: - **Gen.sg.**: `*mizdōz` → final *-ōz → PWGmc *-a → `*mirda` → breaking → `*meorda` → WS `*meorde`
415: - **Dat.sg.**: `*mizdōi` → `*mirdōi` → breaking → `*meordōi` → apocope → `*meorde`
```

## Bibliography-key candidates

### Preferred candidates

| Key | Why it was selected |
| :--- | :--- |
| Kroonen2013 | default Proto-Germanic etymology key for Kroonen |

### Low-confidence candidates

| Key | Why it was selected |
| :--- | :--- |
| Kroonen2011 | surname mention only: Kroonen |
| Kroonen2006 | surname mention only: Kroonen |

## Paradigm probe

### Paradigm probe — berry / berġes

- PROTO: *bázją
- PROTOFORM: *bázjas
- DERIVATION_CLASS: late_analogy
- Morphology source: Hand-specified pilot comparison for ja-stem citation vs. selected gen.sg. cell.
- ProtoGate bypassed: no
- Generated cells: nom.sg., gen.sg.
- Omitted cells: dat.sg. and plural cells omitted in v1; the pilot focuses on the nominative/genitive contrast discussed in the TSV note.
- Winning form unique: yes

| Cell | Candidate input | FST output | Match? | Comment |
|:---|:---|:---|:---|:---|
| nom.sg. | *bázją | bere | no | Citation proto. |
| gen.sg. | *bázjas | berġes | yes | Chosen gen.sg. cell in TSV. |

