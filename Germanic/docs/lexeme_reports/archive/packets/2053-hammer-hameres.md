# Evidence packet — 2053 hammer / hameres

> This packet is evidence for drafting. Do not treat all hits as equally authoritative; prefer high-confidence evidence.

## TSV row data

| ID | CONCEPT | COUNTERPART | PROTO | PROTOFORM | DERIVATION_CLASS | NOTE | HISTORY |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2053 | hammer | hameres | *xámaraz | *xámaras | late_analogy | Note: using gen.sg. *xamaras (> hameres). Both hamor and hamer attested; hameres is the regular reflex via a-fronting (R/T §5.1.2, §6.9.6). hamores has unexplained -o- in unstressed syllable (R/T §3.1.5). | Source: Wiktionary etymology (template:inh) \| Source: Wiktionary etymology (template:inh) |

## Manifest status

_No manifest entry._

## High-confidence evidence

### Compact derivation trace entry

```md
# hammer
PROTO: *xámaras
EXPECTED: hameres
OUTPUTS: hameres



### Proto-Germanic consonant inheritance

Proto Input: *xámaras

| Earlier Germanic developments | Old English developments |
|:---|:---|
| **Proto-West Germanic**<br>[no change]<br><br>**Northwest Germanic**<br>[no change] | **Old English**<br>Anglo Frisian Brightening: *xámæræs<br>OE Unstressed AE Merger: *xámeres |



### Orthography & surface

Old English Orthography: h*ámeres
Outcome: hameres

NOTE: Note: using gen.sg. *xamaras (> hameres). Both hamor and hamer attested; hameres is the regular reflex via a-fronting (R/T §5.1.2, §6.9.6). hamores has unexplained -o- in unstressed syllable (R/T §3.1.5).
```

### Matching oe_known_problems.tsv entries

_None_

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:39966 (exact pair)

- Nearby heading: ### Project precedent

```text
39964: This is the same move applied for *durą → *duruz* (DEV_NOTES line
39965: 908ff.), *spéru → speoru* (§17.16), *fūri → fȳre* dat.sg. (line
39966: 1715), *xámaras → hameres* gen.sg., loam (§17.39), weasel (§17.37),
39967: west (§17.38): switch the per-row PROTOFORM to the paradigm cell
39968: that yields the attested OE form by regular sound change, leaving
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

#### Germanic/docs/DEV_NOTES.md:3208 (exact COUNTERPART)

- Nearby heading: ### Case 1: *rastō → rast (expected ræst) — ō-stem feminine

```text
3206: **Proposed resolution — oblique form approach:**
3207: 
3208: Following the precedent of fire (*fūri → fȳre, dat.sg.), cow (*kūi → cȳ, dat.sg.), night (*naxti → niht, dat.sg.), and hammer (*xamaras → hameres, gen.sg.), we can use an oblique form of *rastō where the suffix does NOT trigger A-restoration.
3209: 
3210: The difficulty is that the standard ō-stem oblique endings (*-ōz gen.sg., *-ōi dat.sg.) contain *-ō, which is a back vowel that would ALSO trigger restoration in our pipeline. The pipeline applies rules at the PGmc input level and does not separately model the pre-AFB shortening of *-ōz → PWGmc *-a.
```

#### Germanic/docs/DEV_NOTES.md:17927 (exact COUNTERPART)

- Nearby heading: #### 14.6 Implementing Inter-Stress Raising: `*a → *u` (2026-04-12)

```text
17925: - `*hlab-ardu → *hlab-urdu → hlafurd` ✓ (consonant before u is d)
17926: - `*lunganjō → lungen` ✓ (j before u blocks rule)
17927: - `*xamaras → hameres` ✓ (no u in following syllable)
17928: 
17929: **Mismatch count:** Unchanged at 40 (no regression).
```

### Analysis and dossier hits

#### Germanic/docs/analysis/arestoration_r_l_research.md:525 (exact COUNTERPART)

- Nearby heading: ## 8. FST probing results (verbatim)

```text
524: $ echo 'xámaras' | flookup -i old_english.bin
525: xámaras	hameres       # OK — single *m intervening; restoration applies under any rule
526: 
```

#### Germanic/docs/analysis/compound_archaism_inventory.md:176 (exact COUNTERPART)

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

#### Germanic/docs/analysis/unstressed_e_o_before_r.md:8 (exact COUNTERPART)

- Nearby heading: ## The three mismatch items

```text
7: | \*sumerăz  | sumer          | sumor      | medial e vs o |
8: | \*xamaras   | hameres        | hamores    | medial e vs o |
9: | \*mōdēr    | mōder          | mōdor      | final e vs o |
```

#### Germanic/docs/analysis/unstressed_e_o_before_r.md:44 (exact COUNTERPART)

- Nearby heading: ### \*xamaras

```text
43: ### \*xamaras
44: - Proto \*a → AFBrightening → \*æ → WeakTailReduction → \*e → output "hameres"
45: - Same path; \*o never appears
```

#### Germanic/docs/analysis/unstressed_e_o_before_r.md:134 (exact COUNTERPART)

- Nearby heading: ### Conclusion: no missing sound change

```text
133: would produce medial -o- from \*a in these words. The -er forms (sumer,
134: hameres, mōder) are the **regular neogrammarian outcome**. The -or forms
135: (sumor, hamores, mōdor) represent either:
```

### Local lexical-table hits

#### old_english_wiktionary.tsv

| ENGLISH | OE_FORM | SOURCE | DETAIL | PAGE |
| :--- | :--- | :--- | :--- | :--- |
| hammer | hamor | inh | template:inh | hammer |

#### old_english_swadesh.tsv

_None_

## Possibly stale or diagnostic evidence

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:2249 (concept name)

- Nearby heading: ### Sandbox vowel expansion

```text
2247:   - `{*ai}` now yields `{əʊ}` before nasals, velars, labials, and the `gw/kn/xw` clusters that cover the attested `bəʊn/fəʊl/snow/stone/soul/token` cases.
2248:   - `{*au}` exposes an `{əʊ}` branch in addition to `{aʊ}/{oː}`, `{*ō}` can realise `{ɔː}` or `{ʊ}` in the usual `r/l/#` and velar-k environments, and `{*a}` picks up `{ɔː}` before `l/r/w`.
2249:   - Added a dedicated schwa cleanup for the weak-tail templates (`-az/-an/-nē/-gą/-lō/-raz`) so `hammer`, `bottom`, `weapon`, etc. stop stalling solely because the tail vowel stayed as `{a}`.
2250: - `docker compose exec backend sh -lc 'cd /usr/app && foma -f fsts/english_brace_sandbox.txt'` recompiles the sandbox to a 21.7 kB automaton (201 states / 23 M paths). Quick probes such as `printf 'bɔːl\nkɔːn\nfəʊl\nbəʊn\nbʊk\n' | flookup english_brace_sandbox.bin` now return full proto bundles instead of `+?`.
2251: - `python3 server/tools/api_regression.py` still PASS for both Burmish and Germanic datasets, so the extra branches did not perturb the production analyzer.
```

#### Germanic/docs/DEV_NOTES.md:3216 (concept name)

- Nearby heading: ### Case 1: *rastō → rast (expected ræst) — ō-stem feminine

```text
3214: Tested: `rastas → ræstes` ✓ (the gen.sg. form with correct ræ- root).
3215: 
3216: **Decision needed:** We could (a) use gen.sg. *rastas → OE ræstes, changing both the proto and the OE target (parallel to hammer, swan, brand); or (b) document ræst as a known morphological exception with an ALIGNMENT note that the pipeline gives the regular nom.sg. reflex rast but the standard form ræst reflects paradigmatic leveling.
3217: 
3218: **Complication with (a):** The encoding *rastas uses the a-stem gen.sg. ending *-as, but *rastō is an ō-stem, whose gen.sg. is *-ōz (→ PWGmc *-a → OE -e). The pipeline cannot process *-ōz because it is not in the pgrmWeakTailVowel list, and even if added, the *-ō component would trigger A-restoration. Using *-as is thus a pragmatic encoding that gives the correct phonological result but misrepresents the morphological class.
```

#### Germanic/docs/DEV_NOTES.md:17852 (concept name)

- Nearby heading: #### 14.6 Implementing Inter-Stress Raising: `*a → *u` (2026-04-12)

```text
17850: **Problem 1: Over-application**
17851: 
17852: The rule triggered on `*xamaras` (hammer) → `*xamuras` and `*lunganjō` → `*lungunjō`
17853: because `PGmcStarBackVowel` includes `*a`. So any `*a` followed by C+ and another `*a`
17854: was incorrectly raised.
```

### Analysis and dossier hits

#### Germanic/docs/analysis/arestoration_r_l_research.md:716 (exact pair)

- Nearby heading: ## 11. Affected TSV rows

```text
715: | 2003 | `*fáraną` | `færan`† | `færan` | **`faran`** | †TSV target is `færan` but that is itself **wrong**: per R/T 13432 and Campbell §160(4) the W-S inf. is **`faran`**. The recommended fix produces the historically correct form. **TSV column 6 should be updated separately.** |
716: | 2053 | `*xámaras` | `hameres` | `hameres` | `hameres` | intervening `*m` (not r/l); already correct under either rule |
717: | 2141 | `*márōn` | `mære` | `mære` | `mære` | long `*ā/ǣ`, out of scope of short A-restoration |
```

#### Germanic/docs/analysis/compound_archaism_inventory.md:195 (concept name)

- Nearby heading: ### Case 8: *rastō (rest) — ræst / ræste

```text
194: | **Classification** | **Paradigm-cell case via oblique**: The oblique gen.sg. `*rastōz` → `ræste` is the lautgesetzlich output. The nom.sg. `ræst` shows **analogical leveling** from the oblique stem. This is the reverse of the *spere* case: here the oblique is lautgesetzlich and the nom.sg. is leveled, rather than the other way around. |
195: | **Methodological use** | Per the precedent of fire/cow/night/hammer (§3.150), the TSV can target either (a) the oblique form `*rastōz → ræste` (changing both proto and target), or (b) document `ræst` as a paradigmatic-leveling exception with an ALIGNMENT note. The decision depends on whether we prefer "pure lautgesetzlich" or "conventional attested form." |
196: | **Implementation** | TSV now uses gen.sg. `*rastōz`, target `ræste` (following the precedent of paradigm-cell targeting; see §3.399: "RST row 2152 (ræst) now uses genuine PGmc gen.sg. *rastōz, target ræste..."). |
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

_None_

### Low-confidence candidates

_None_

## Paradigm probe

Paradigm probe required for this row, but no built-in `oe_paradigm_probe.py` specification exists yet. This packet should be used to draft the probe configuration before prose drafting.

