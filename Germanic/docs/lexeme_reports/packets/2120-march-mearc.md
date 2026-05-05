# Evidence packet — 2120 march / mearc

> This packet is evidence for drafting. Do not treat all hits as equally authoritative; prefer high-confidence evidence.

## TSV row data

| ID | CONCEPT | COUNTERPART | PROTO | PROTOFORM | DERIVATION_CLASS | NOTE | HISTORY |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2120 | march | mearc | *márkō | *márkō | regular | Kroonen *markō- f. 'boundary' → OE mearc f.; mearcian is the verb 'to mark' | - |

## Manifest status

_No manifest entry._

## High-confidence evidence

### Compact derivation trace entry

```md
# march
PROTO: *márkō
EXPECTED: mearc
OUTPUTS: mearc



### Proto-Germanic consonant inheritance

Proto Input: *márkō

| Earlier Germanic developments | Old English developments |
|:---|:---|
| **Proto-West Germanic**<br>[no change]<br><br>**Northwest Germanic**<br>NWGmc Final Long O Raising: *márku | **Old English**<br>Anglo Frisian Brightening: *mærku<br>OE Breaking: *mearku<br>OE High Vowel Apocope: *meark |



### Orthography & surface

Outcome: mearc

NOTE: Kroonen *markō- f. 'boundary' → OE mearc f.; mearcian is the verb 'to mark'
```

### Matching oe_known_problems.tsv entries

_None_

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:29435 (exact pair)

- Nearby heading: ### §17.17.8 Implementation results (short-diphthong weight refactor)

```text
29433:      *spéru → speoru, *teru → teoru, *smeru → smeoru).
29434:    - `ShortDiphthong + C + C+` (2+ C) → heavy → apocopate
29435:      (e.g. *xérdō → heord, *márkō → mearc, *xállō → heall).
29436:    - Trisyllabic clauses extended symmetrically for
29437:      ShortDiphthong first-syllables: trisyllabic apocope fires
```

#### Germanic/docs/DEV_NOTES.md:29466 (exact pair)

- Nearby heading: ### §17.17.8 Implementation results (short-diphthong weight refactor)

```text
29464: | *smeru    | smeoru  | smeoru   | LIGHT retains -u      |
29465: | *xérdō    | heord   | heord    | HEAVY (rd cluster)    |
29466: | *márkō    | mearc   | mearc    | HEAVY (rk cluster)    |
29467: | *xállō    | heall   | heall    | HEAVY (ll geminate)   |
29468: | *xémonų   | heofon  | heofon   | trisyllabic (light 1) |
```

### Analysis and dossier hits

_None_

## Supporting/background evidence

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:29475 (exact COUNTERPART)

- Nearby heading: ### §17.17.8 Implementation results (short-diphthong weight refactor)

```text
29473: **Regressions that self-resolved** (all restored to pre-fix
29474: behaviour by the round-3 short-diphthong-plus-cluster and
29475: -u-after-h clauses): heall, heord, mearc, heofon, feoh.
29476: 
29477: **Known remaining issue** (not from this refactor, documented
```

#### Germanic/docs/DEV_NOTES.md:36628 (exact PROTOFORM)

- Nearby heading: ### §17.25.5 Predicted side-effects

```text
36626:   (manual trace verification; full mismatch report will confirm).
36627: 
36628: For breaking-conditioned rows (`*xármaz, *márkō, *kálbaz, *fállaną`
36629: etc., 21 rows total), A-restoration is bled by breaking; unaffected.
36630: 
```

### Analysis and dossier hits

_None_

### Local lexical-table hits

#### old_english_wiktionary.tsv

| ENGLISH | OE_FORM | SOURCE | DETAIL | PAGE |
| :--- | :--- | :--- | :--- | :--- |
| march | mearcian | inh | template:inh | march |

#### old_english_swadesh.tsv

_None_

## Possibly stale or diagnostic evidence

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:16654 (concept name)

- Nearby heading: ### PWGmc *ō → *a Rule: No Redundancy with Epenthesis (2026-04-10)

```text
16652: During this investigation, I discovered that I had accidentally created a duplicate rule:
16653: - `PWGmcFinalOrLowering` (lines ~1175, added April 10)
16654: - `PWGmcPreFinalRShortening` (lines ~1246, added March 6)
16655: 
16656: Both did the same thing: `{*ō} → {*a} || _ {*r} .#.`
```

### Analysis and dossier hits

#### Germanic/docs/analysis/arestoration_r_l_research.md:738 (exact pair)

- Nearby heading: ## 11. Affected TSV rows

```text
737: | 2118 | `*máltaz` | `mealt` | breaking |
738: | 2120 | `*márkō` | `mearc` | breaking |
739: | 2166 | `*sáltą` | `sealt` | breaking |
```

#### Germanic/docs/analysis/notable_findings.md:109 (concept name)

- Nearby heading: ## 1. Medial high-vowel syncope: dental-obstruent conditioning

```text
108: 
109: **Cross-referencing with additional sources (March 2026):**
110: 
```

#### Germanic/docs/analysis/notable_findings.md:299 (concept name)

- Nearby heading: ## 2. NWGmc u-lowering exceptions near labials: a non-Neogrammarian pattern

```text
298: 
299: **Cross-referencing with additional sources (March 2026):**
300: 
```

#### Germanic/docs/analysis/notable_findings.md:547 (concept name)

- Nearby heading: ## 3. PWGmc \*j-related sound changes: formalization of under-specified rules

```text
546: 
547: **Cross-referencing with additional sources (March 2026):**
548: 
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

