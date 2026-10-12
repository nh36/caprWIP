# Evidence packet — 1954 bone / bān

> This packet is evidence for drafting. Do not treat all hits as equally authoritative; prefer high-confidence evidence.

## TSV row data

| ID | CONCEPT | COUNTERPART | PROTO | PROTOFORM | DERIVATION_CLASS | NOTE | HISTORY |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1954 | bone | bān | *báiną | *báiną | regular | Proto: oblique *bainăn→*bainą (n. a-stem nom.sg.; Kroonen) | - |

## Manifest status

_No manifest entry._

## High-confidence evidence

### Compact derivation trace entry

```md
# bone
PROTO: *báiną
EXPECTED: bān
OUTPUTS: bān



### Proto-Germanic consonant inheritance

Proto Input: *báiną

| Earlier Germanic developments | Old English developments |
|:---|:---|
| **Proto-West Germanic**<br>PWGmc Ai Monophthongization: *bāną<br><br>**Northwest Germanic**<br>[no change] | **Old English**<br>OE Heavy Syllable Nasal Apocope: *bān |



### Orthography & surface

Outcome: bān

NOTE: Proto: oblique *bainăn→bainą (n. a-stem nom.sg.; Kroonen)
```

### Matching oe_known_problems.tsv entries

_None_

### DEV_NOTES hits

_None_

### Analysis and dossier hits

_None_

## Supporting/background evidence

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:1571 (exact COUNTERPART)

- Nearby heading: ## Consonant Mismatch Bucket Refinement (2026-02-07)

```text
1569: **New buckets created:**
1570: 1. **inflectional_suffix_extra: 15** - Output has extra inflectional suffix (-an, -en) that shouldn't be there
1571:    - Examples: `*bainăn → bānan` (expected `bān`), `*kurnăn → cornan` (expected `corn`)
1572:    - Likely TSV data issues (wrong inflectional form selected)
1573: 2. **final_devoicing_missing: 1** - Word-final/pre-consonantal devoicing not applied
```

#### Germanic/docs/DEV_NOTES.md:2262 (exact COUNTERPART)

- Nearby heading: ### WG monophthongisation stage

```text
2260: 
2261: - Added `EnglishSandboxWestGermanic` to the cascade (between glide deletion and the vowel rules) so proto `{*ai}`/`{*au}` first collapse onto the historical long vowels `{*ā}`/`{*ō}` before Middle/Modern English rules run. The new stage keeps everything in the proto alphabet—no WGMARK tokens—and mirrors how the German/Burmish stacks segregate their era-specific rule blocks.
2262: - Moved the old `{*ai}`/`{*au}` IPA rewrites onto `{*ā}`/`{*ō}` inside `EnglishSandboxCoreVowelRules`, preserving every contextual mapping we already depend on (`bəʊn`/`stəʊn`/`fəʊl`, etc.) while letting us inspect `{*bān}`, `{*stān}` intermediate outputs.
2263: - `docker compose exec backend sh -lc "cd /usr/app && foma -f fsts/english_brace_sandbox.txt"` now produces a 23.5 kB sandbox automaton (209 states / 32 M paths). Spot checks via `printf 'bəʊn\nstəʊn\nfəʊl\nbɔːl\n' | flookup english_brace_sandbox.bin` show the analyzer surfacing both the WG monophthongised forms (`bān/stān/fāl/bōl`) and the legacy `{*bain}` branches, so we can trace the historical stage outputs directly.
2264: 
```

#### Germanic/docs/DEV_NOTES.md:2263 (exact COUNTERPART)

- Nearby heading: ### WG monophthongisation stage

```text
2261: - Added `EnglishSandboxWestGermanic` to the cascade (between glide deletion and the vowel rules) so proto `{*ai}`/`{*au}` first collapse onto the historical long vowels `{*ā}`/`{*ō}` before Middle/Modern English rules run. The new stage keeps everything in the proto alphabet—no WGMARK tokens—and mirrors how the German/Burmish stacks segregate their era-specific rule blocks.
2262: - Moved the old `{*ai}`/`{*au}` IPA rewrites onto `{*ā}`/`{*ō}` inside `EnglishSandboxCoreVowelRules`, preserving every contextual mapping we already depend on (`bəʊn`/`stəʊn`/`fəʊl`, etc.) while letting us inspect `{*bān}`, `{*stān}` intermediate outputs.
2263: - `docker compose exec backend sh -lc "cd /usr/app && foma -f fsts/english_brace_sandbox.txt"` now produces a 23.5 kB sandbox automaton (209 states / 32 M paths). Spot checks via `printf 'bəʊn\nstəʊn\nfəʊl\nbɔːl\n' | flookup english_brace_sandbox.bin` show the analyzer surfacing both the WG monophthongised forms (`bān/stān/fāl/bōl`) and the legacy `{*bain}` branches, so we can trace the historical stage outputs directly.
2264: 
2265: ### Great Vowel Shift split
```

#### Germanic/docs/DEV_NOTES.md:14038 (exact COUNTERPART)

- Nearby heading: ### Implementation completed (2026-04-06)

```text
14036: **Test results:**
14037: - `echo "spannăi" | flookup -i old_english.bin` → `spanne` ✓
14038: - Stressed *ai forms still work: `*bainą → bān`, `*dailiz → dǣl` ✓
14039: - Mismatch count: 56 → 55 (1 fix for span)
14040: 
```

### Analysis and dossier hits

_None_

### Local lexical-table hits

#### old_english_wiktionary.tsv

| ENGLISH | OE_FORM | SOURCE | DETAIL | PAGE |
| :--- | :--- | :--- | :--- | :--- |
| bone | bān | inh | template:inh | bone |

#### old_english_swadesh.tsv

| NUMBER | ENGLISH | OLD_ENGLISH | IPA_RAW |
| :--- | :--- | :--- | :--- |
| 65 | bone | bān | /bɑːn/ |

## Possibly stale or diagnostic evidence

### DEV_NOTES hits

_None_

### Analysis and dossier hits

_None_

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

Philological note; no paradigm probe required for this row under the current classification. The note mentions paradigm forms, but it does not yet depend on a paradigm-cell solution.

