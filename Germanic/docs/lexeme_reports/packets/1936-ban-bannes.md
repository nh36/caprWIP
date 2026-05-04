# Evidence packet — 1936 ban / bannes

> This packet is evidence for drafting. Do not treat all hits as equally authoritative; prefer high-confidence evidence.

## TSV row data

| ID | CONCEPT | COUNTERPART | PROTO | PROTOFORM | DERIVATION_CLASS | NOTE | HISTORY |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1936 | ban | bannes | *bánną | *bánnas | late_analogy | Gen.sg. paradigm cell: *bannas → bannes. Word-final geminates are phonologically simplified; using gen.sg. preserves medial geminate. Note: a-stem neuter, gen.sg. same as masc. | Original: *banną → bann (nom.sg.). |

## Manifest status

| REPORT_PATH | STATUS |
| :--- | :--- |
| pilot/ban.md | pilot |

## High-confidence evidence

### Compact derivation trace entry

```md
# ban
PROTO: *bánnas
EXPECTED: bannes
OUTPUTS: bannes



### Proto-Germanic consonant inheritance

Proto Input: *bánnas

| Earlier Germanic developments | Old English developments |
|:---|:---|
| **Proto-West Germanic**<br>[no change]<br><br>**Northwest Germanic**<br>[no change] | **Old English**<br>Anglo Frisian Brightening: *bánnæs<br>OE Unstressed AE Merger: *bánnes |



### Orthography & surface

Outcome: bannes

NOTE: Gen.sg. paradigm cell: *bannas → bannes. Word-final geminates are phonologically simplified; using gen.sg. preserves medial geminate. Note: a-stem neuter, gen.sg. same as masc.
```

### Matching oe_known_problems.tsv entries

_None_

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:13788 (row ID)

- Nearby heading: # MUST use *a (not *ă) to undergo unstressed fronting: *a → *æ → *e

```text
13786: | Row | Concept | Current proto | Output | Target | Issue |
13787: |-----|---------|---------------|--------|--------|-------|
13788: | 1936 | ban | `*banną` | ban | bann | word-final degemination |
13789: | 2119 | man | `*mannăz` | man | mann | word-final degemination |
13790: | 2203 | span | `*spannō` | span | spann | word-final degemination |
```

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

#### Germanic/docs/DEV_NOTES.md:1379 (note keyword: gen.sg.)

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

#### Germanic/docs/DEV_NOTES.md:13702 (exact COUNTERPART)

- Nearby heading: ### Paradigm-cell approach for geminate-stem words

```text
13700: Option A (paradigm-cell): Switch geminate-stem nouns to gen.sg. targets
13701:   - Pro: Geminates preserved by regular phonology
13702:   - Con: Targets become `mannes`, `bannes`, etc. (less intuitive as headwords)
13703:   - Con: Requires adding gen.sg. ending to grammar
13704: 
```

#### Germanic/docs/DEV_NOTES.md:13794 (exact COUNTERPART)

- Nearby heading: # MUST use *a (not *ă) to undergo unstressed fronting: *a → *æ → *e

```text
13792: 
13793: **Neuter a-stems:** Gen.sg. uses the same `-es` ending as masculines (Brunner §237).
13794: Therefore `*banną` (neuter) can use gen.sg. `*bannas` → `bannes`.
13795: 
13796: **Implementation completed (2026-04-05):**
```

#### Germanic/docs/DEV_NOTES.md:16908 (exact COUNTERPART)

- Nearby heading: # This targets only *ă (the linking vowel marker), not *a from inflectional endings.

```text
16906: - `*regnă-bugô → reġnboga` ✓ (was `reġnafoga`)
16907: - `*wiră-aldiz → weraield` (still wrong — separate issue with `*wir-` breaking)
16908: - `*bannas → bannes` ✓ (suffix vowel correctly preserved)
16909: 
16910: **Status:** Implemented for compound linking vowels. The `*wiră-aldiz` case has
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

#### Germanic/docs/analysis/notable_findings.md:644 (note keyword: gen.sg.)

- Nearby heading: ## 4. A-restoration trigger set: {*æ} is NOT a trigger

```text
643: **What we initially assumed:** We included `{*æ}` in the trigger set, on the
644: reasoning that suffix *a (like gen.sg. *-as) had been fronted to *æ by AFB
645: but was "underlyingly back" and should still trigger restoration. This seemed
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
| ban | bannan | inh | template:inh | ban |

#### old_english_swadesh.tsv

_None_

## Possibly stale or diagnostic evidence

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:1789 (concept name)

- Nearby heading: ### English sandbox todo — surface accuracy focus

```text
1787: ### English sandbox todo — surface accuracy focus
1788: 
1789: - ~~**Finish weak-tail deletions.** Extend `EnglishSandboxWeakTailReductions` (or add a follow-up cleanup stage) so reduced `{*a/ą}` tails drop the following `n/m/r` and final schwa in stressed monosyllables. This will convert forms like `beɪkeɪnə/bænnə/brændə/blʌdə` into the expected `bake/ban/brand/blood` without manual patches.~~
1790:   - ✅ 2025-12-11: `{*ă}` now flows through `EnglishSandboxWeakTailReductions → EnglishSandboxWeakTailCleanup → EnglishSandboxWeakTailFinalDrop`; `EnglishSandboxNoFinalWeakTail` filters out residual `{*r/n/m}`+`{*ə}`. Tracer (`*bakăną/*bannăn/*brandăz/*blōdą`) shows single surfaces (`beɪk/bæn/brænd/blʌd`), and `tools/english_apply_down_stats.py` reports 333/376 single-output entries (multiple outputs = 0).
1791: - **Back/round proto rhotics earlier.** Expand `EnglishSandboxProtoRhoticFronting` to push `{*e, *i, *o}` toward `{æ, ɪ, ɔ}` before `{*r}` so `*bergą/*bardăz/*barwōn/*burdiz` feed the ME vowel system with the right backness, unlocking `barrow/beard/bier/birth` reflexes.
```

#### Germanic/docs/DEV_NOTES.md:1841 (concept name)

- Nearby heading: ### Star-preserving vowel cascade + STRUT probes (late 2025-12-07)

```text
1839: - Converted the vowel pipeline to stay in the `{*…}` alphabet until the very end: `EnglishSandboxRhoticColoring`/`EnglishSandboxGreatVowelShift` now rewrite starred vowels and a new terminal `EnglishSandboxLongVowelRealisation` emits the IPA symbols right before `RemoveStars`. Tracer logs (`docs/debug_snapshots/english_tracer_log_core_starred.txt`, `docs/debug_snapshots/english_tracer_log_2025-12-07c.txt`) confirm the macrons persist through every historical stage.
1840: - Reran the export→annotate→trace workflow (`english_tracer_log_2025-12-07d.txt`); analyzer coverage climbed to **188/376**, so the star-preserving rewrite didn’t cost us any outputs.
1841: - Began cleaning up the STRUT/DRESS zero-output cluster. `EnglishSandboxWeakTailReductions` now maps `{*ą}`→`{*ə}` and a new `EnglishSandboxShortAFronting` stage fronts short `{*a}` in closed syllables before the short-vowel split. After rebuilding and running `server/tools/run_english_sandbox_workflow.sh english_tracer_log_2025-12-07e.txt`, coverage improved to **195/376**—forms like *ban/*brandaz now emit `bæn`/`brændə`. Updated `server/tmp/english_zero_output_summary.txt` (181 remaining failures) plus dropped the STRUT trace log at `docs/debug_snapshots/english_tracer_log_2025-12-07e.txt` for future comparisons.
1842: 
1843: ## 2025-12-06
```

#### Germanic/docs/DEV_NOTES.md:11933 (concept name)

- Nearby heading: ### The Etymology of OE sæp 'sap'

```text
11931: And critically:
11932: 
11933: > "Within Germanic, the co-occurrence of the three stems \*saf/ban-, \*sappa-
11934: > and \*sapa- clearly points to **dialectal dissolution of a primary n-stem** \*safō,
11935: > gen. \*sappaz < \*sHp-ón, \*sHp-n-ós."
```

#### Germanic/docs/DEV_NOTES.md:13657 (concept name)

- Nearby heading: ### Paradigm-cell approach for geminate-stem words

```text
13655: - `*lunganjō → lungen` ✓ (correct! j-gemination → final degemination)
13656: - `*mannăz → man` ✗ (wrong! target is `mann` in orthography)
13657: - `*banną → ban` ✗ (wrong! target is `bann`)
13658: 
13659: A selective rule that only degeminates "secondary" (j-derived) geminates but preserves 
```

#### Germanic/docs/DEV_NOTES.md:13799 (row ID)

- Nearby heading: # MUST use *a (not *ă) to undergo unstressed fronting: *a → *æ → *e

```text
13797: 
13798: 1. ✓ Updated row 2119 (man): proto `*mannas`, target `mannes`
13799: 2. ✓ Updated row 1936 (ban): proto `*bannas`, target `bannes` 
13800: 3. For span (fem. ō-stem), different paradigm — investigate separately
13801: 4. For wool, different issue (vowel) — investigate separately
```

### Analysis and dossier hits

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

#### Germanic/docs/dossiers/bugan-scufan-paradigm-cell-review.md:575 (concept name)

- Nearby heading: ### PGmc / PIE handbooks

```text
574: * **Orel**, *A Handbook of Germanic Etymology*, 2003. s.v.
575:   `*beuganan`, `*skeu̯ban`.
576: * **Bammesberger**, *Die Morphologie des urgermanischen Nomens*,
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

### Paradigm probe — ban / bannes

- PROTO: *bánną
- PROTOFORM: *bánnas
- DERIVATION_CLASS: late_analogy
- Morphology source: Hand-specified pilot comparison for n-stem singular cells.
- ProtoGate bypassed: no
- Generated cells: nom.sg., gen.sg.
- Omitted cells: dat.sg. and plural cells omitted in v1; the pilot only compares the citation-form nomination against the selected gen.sg. cell.
- Winning form unique: yes

| Cell | Candidate input | FST output | Match? | Comment |
|:---|:---|:---|:---|:---|
| nom.sg. | *bánną | ban | no | Citation-form comparison. |
| gen.sg. | *bánnas | bannes | yes | Chosen paradigm-cell input in TSV. |

