# Evidence packet — 2138 net / nett

> This packet is evidence for drafting. Do not treat all hits as equally authoritative; prefer high-confidence evidence.

## TSV row data

| ID | CONCEPT | COUNTERPART | PROTO | PROTOFORM | DERIVATION_CLASS | NOTE | HISTORY |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2138 | net | nett | *nátją | *nátją | regular | Orel: OE nett (geminate); Source: Wiktionary etymology (template:inh) | Source: Wiktionary etymology (template:inh) |

## Manifest status

_No manifest entry._

## High-confidence evidence

### Compact derivation trace entry

```md
# net
PROTO: *nátją
EXPECTED: nett
OUTPUTS: nett



### Proto-Germanic consonant inheritance

Proto Input: *nátją

| Earlier Germanic developments | Old English developments |
|:---|:---|
| **Proto-West Germanic**<br>PWGmc J Gemination: *náttją<br><br>**Northwest Germanic**<br>[no change] | **Old English**<br>Anglo Frisian Brightening: *nættją<br>OE Heavy Syllable Nasal Apocope: *nættj<br>OE I Umlaut: *nettj<br>OE J Loss After Heavy: *nett |



### Orthography & surface

Outcome: nett

NOTE: Orel: OE nett (geminate); Source: Wiktionary etymology (template:inh)
```

### Matching oe_known_problems.tsv entries

_None_

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:12143 (row ID)

- Nearby heading: ### TSV Data Issue

```text
12141: ### TSV Data Issue
12142: 
12143: The TSV expects `net` (row 2138), but scholarly sources (Orel, Hall) give `nett`.
12144: 
12145: **TSV row 2138:**
```

#### Germanic/docs/DEV_NOTES.md:12145 (row ID)

- Nearby heading: ### TSV Data Issue

```text
12143: The TSV expects `net` (row 2138), but scholarly sources (Orel, Hall) give `nett`.
12144: 
12145: **TSV row 2138:**
12146: ```
12147: ID: 2138
```

### Analysis and dossier hits

_None_

## Supporting/background evidence

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:12064 (exact COUNTERPART)

- Nearby heading: ## OE nett 'net': ja-stem Gemination Chronology Bug (2026-03-18)

```text
12062: ---
12063: 
12064: ## OE nett 'net': ja-stem Gemination Chronology Bug (2026-03-18)
12065: 
12066: ### The Problem
```

#### Germanic/docs/DEV_NOTES.md:12068 (exact COUNTERPART)

- Nearby heading: ### The Problem

```text
12066: ### The Problem
12067: 
12068: The FST produces `*natją → nete` instead of expected `nett` (or `net`).
12069: 
12070: **Full trace:**
```

#### Germanic/docs/DEV_NOTES.md:12083 (exact COUNTERPART)

- Nearby heading: ### Scholarly Sources on the Correct OE Form

```text
12081: 
12082: **Orel (2003), s.v. `*natjan`:**
12083: > "Goth nati 'net', ON net id., **OE nett** id., OFris net, nette id., OS netti id., OHG nezzi id."
12084: 
12085: Orel clearly gives the OE form as `nett` (with geminate -tt-), not `net` (single -t-).
```

#### Germanic/docs/DEV_NOTES.md:12085 (exact COUNTERPART)

- Nearby heading: ### Scholarly Sources on the Correct OE Form

```text
12083: > "Goth nati 'net', ON net id., **OE nett** id., OFris net, nette id., OS netti id., OHG nezzi id."
12084: 
12085: Orel clearly gives the OE form as `nett` (with geminate -tt-), not `net` (single -t-).
12086: 
12087: **Hall (1916), A Concise Anglo-Saxon Dictionary:**
```

#### Germanic/docs/DEV_NOTES.md:12088 (exact COUNTERPART)

- Nearby heading: ### Scholarly Sources on the Correct OE Form

```text
12086: 
12087: **Hall (1916), A Concise Anglo-Saxon Dictionary:**
12088: Lists compound forms like `ælnett`, `fengnett`, `fisconett`, all with -nett (geminate).
12089: 
12090: **Campbell (1959), §66:**
```

#### Germanic/docs/DEV_NOTES.md:12091 (exact COUNTERPART)

- Nearby heading: ### Scholarly Sources on the Correct OE Form

```text
12089: 
12090: **Campbell (1959), §66:**
12091: Notes that "Double consonant symbols are very frequently simplified at the ends of words" in OE manuscripts. So `net` and `nett` may both appear, but the underlying form has the geminate.
12092: 
12093: **Campbell (1959), §607-609 (ja-stem neuters):**
```

### Analysis and dossier hits

_None_

### Local lexical-table hits

#### old_english_wiktionary.tsv

| ENGLISH | OE_FORM | SOURCE | DETAIL | PAGE |
| :--- | :--- | :--- | :--- | :--- |
| net | net | inh | template:inh | net |

#### old_english_swadesh.tsv

_None_

## Possibly stale or diagnostic evidence

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:1381 (concept name)

- Nearby heading: ### 1. PWGmcSyllabicJ: *ja/*ją → *i (after light syllable, word-finally)

```text
1379: - *bazją → *bazi → berġes ('berry', gen.sg.)
1380: - *harjaz → *hari → here ('army')
1381: - *natją → *nati → net ('net')
1382: **Implementation:** `{*j} {*a} -> {*i}` / `EnglishStarShortVowel EnglishStarConsonant _ .#.`
1383: **Status:** Implemented and working.
```

#### Germanic/docs/DEV_NOTES.md:1596 (concept name)

- Nearby heading: ### Archived: Heavy Syllable Nasal Apocope (2026-02-06) — EMPIRICAL DISCOVERY

```text
1594: 
1595: **Summary:** Implemented experimental rule deleting proto *-ą after heavy syllables, achieving 
1596: net +28 case improvement (41 fixes, 13 collateral). This represents an **empirically-derived 
1597: phonological finding** not explicitly stated in existing literature.
1598: 
```

#### Germanic/docs/DEV_NOTES.md:5408 (concept name)

- Nearby heading: # per Howell & Salmons (1997), but the current implementation does not do so.

```text
5406: ```
5407: 
5408: **Result: 9 regressions** (net −3 matches from 297 to 294):
5409: 
5410: | Concept | Proto | FST output | Expected OE | Blocking C |
```

#### Germanic/docs/DEV_NOTES.md:5792 (concept name)

- Nearby heading: #### Results

```text
5790: - Baseline: 297/386 matches (76.9%)
5791: - After onset-velar blocking: **299/386 matches (77.5%)**
5792: - Net gain: **+2 matches** (lid, fright fixed; no regressions)
5793: 
5794: #### Theoretical significance
```

#### Germanic/docs/DEV_NOTES.md:6923 (concept name)

- Nearby heading: ### Implementation Hurdle: Word-Final *ĭ (Dill Regression)

```text
6921: - `*xarbistuz` → `hierfest` ✓
6922: - `*biginnăną` → `beġinnan` ✓
6923: - Evaluation: 310/386 matches (80.3%) — net +1 from harvest fix
6924: 
6925: ### Exceptions: When Medial *i is Preserved
```

#### Germanic/docs/DEV_NOTES.md:9536 (concept name)

- Nearby heading: ### Empirical Validation (Dry Run 2026-03-13)

```text
9534: ```
9535: 
9536: **Mismatch count:** 78 → 79 (net +1 WORSE)
9537: 
9538: - **Fixed: 6** (bake, grave, wade, wake, wash, will)
```

#### Germanic/docs/DEV_NOTES.md:12147 (row ID)

- Nearby heading: ### TSV Data Issue

```text
12145: **TSV row 2138:**
12146: ```
12147: ID: 2138
12148: PROTOFORM: *natją
12149: EXPECTED: net
```

### Analysis and dossier hits

#### Germanic/docs/analysis/arestoration_r_l_research.md:450 (concept name)

- Nearby heading: ### 6.3 Net conclusion on the counter-examples

```text
449: 
450: ### 6.3 Net conclusion on the counter-examples
451: 
```

#### Germanic/docs/analysis/arestoration_r_l_research.md:753 (concept name)

- Nearby heading: ### 11.1 Net count of TSV rows affected by the proposed fix

```text
752: 
753: ### 11.1 Net count of TSV rows affected by the proposed fix
754: 
```

#### Germanic/docs/analysis/notable_findings.md:504 (concept name)

- Nearby heading: ## 3. PWGmc \*j-related sound changes: formalization of under-specified rules

```text
503: but not explicitly stated as a rule. Our implementation successfully derives:
504: \*bazją → \*bazi → berġes, \*harjaz → \*hari → here, \*natją → \*nati → net.
505: 
```

## Bibliography-key candidates

### Preferred candidates

| Key | Why it was selected |
| :--- | :--- |
| Campbell1959 | author + year mention (Campbell 1959) |
| Orel2003 | author + year mention (Orel 2003) |

### Low-confidence candidates

_None_

