# Evidence packet — 2136 needle / nǣdl

> This packet is evidence for drafting. Do not treat all hits as equally authoritative; prefer high-confidence evidence.

## TSV row data

| ID | CONCEPT | COUNTERPART | PROTO | PROTOFORM | DERIVATION_CLASS | NOTE | HISTORY |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2136 | needle | nǣdl | *nḗθlō | *nḗðlō | early_analogy | R/T p.435: PGmc *nēdlō has Verner's alternation; OE nǣdl reflects *d variant | - |

## Manifest status

_No manifest entry._

## High-confidence evidence

### Compact derivation trace entry

```md
# needle
PROTO: *nḗðlō
EXPECTED: nǣdl
OUTPUTS: nǣdl



### Proto-Germanic consonant inheritance

Proto Input: *nḗðlō

| Earlier Germanic developments | Old English developments |
|:---|:---|
| **Proto-West Germanic**<br>PWGmc Dental Hardening: *nḗdlō<br><br>**Northwest Germanic**<br>NWGmc Final Long O Raising: *nḗdlu<br>NWGmc Long E Lowering: *nǣdlu | **Old English**<br>OE High Vowel Apocope: *nǣdl |



### Orthography & surface

Outcome: nǣdl

NOTE: R/T p.435: PGmc *nēdlō has Verner's alternation; OE nǣdl reflects *d variant
```

### Matching oe_known_problems.tsv entries

_None_

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:10245 (row ID)

- Nearby heading: ### Analysis: `*nēθlō` → `nǣdl`

```text
10243: ### Analysis: `*nēθlō` → `nǣdl`
10244: 
10245: **TSV row 2136:**
10246: - PROTOFORM: `*nēθlō` (voiceless `*θ`)
10247: - COUNTERPART: `nǣdl` (voiced `d`)
```

### Analysis and dossier hits

_None_

## Supporting/background evidence

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:1343 (exact COUNTERPART)

- Nearby heading: ### Not this rule: *nēθlō → nǣdl ('needle')

```text
1341: `PWGmcLThVoicing` rule handles both cases correctly regardless.
1342: 
1343: ### Not this rule: *nēθlō → nǣdl ('needle')
1344: R/T p.435: PGmc `*nēþlō / *nēdlō-` has Verner's alternation. OE `nǣdl`
1345: reflects the `*d` variant. The consonant order is `θl` not `lθ`, so
```

#### Germanic/docs/DEV_NOTES.md:1344 (exact COUNTERPART)

- Nearby heading: ### Not this rule: *nēθlō → nǣdl ('needle')

```text
1342: 
1343: ### Not this rule: *nēθlō → nǣdl ('needle')
1344: R/T p.435: PGmc `*nēþlō / *nēdlō-` has Verner's alternation. OE `nǣdl`
1345: reflects the `*d` variant. The consonant order is `θl` not `lθ`, so
1346: `PWGmcLThVoicing` does not apply. Currently a mismatch (our FST keeps `þ`
```

#### Germanic/docs/DEV_NOTES.md:1355 (exact COUNTERPART)

- Nearby heading: ### Scope of Verner's Law in the project

```text
1353: - Where the regular sound change (`*lþ → ld`) gives the right answer, we
1354:   use it (gold, feld, fealdan, etc.)
1355: - Where only Verner's alternation explains the outcome (nǣdl), the item
1356:   remains a known mismatch until we decide on a systematic approach
1357: 
```

#### Germanic/docs/DEV_NOTES.md:10243 (exact COUNTERPART)

- Nearby heading: ### Analysis: `*nēθlō` → `nǣdl`

```text
10241: **Result:** 72 → 71 mismatches. `hladan` now matches.
10242: 
10243: ### Analysis: `*nēθlō` → `nǣdl`
10244: 
10245: **TSV row 2136:**
```

#### Germanic/docs/DEV_NOTES.md:10247 (exact COUNTERPART)

- Nearby heading: ### Analysis: `*nēθlō` → `nǣdl`

```text
10245: **TSV row 2136:**
10246: - PROTOFORM: `*nēθlō` (voiceless `*θ`)
10247: - COUNTERPART: `nǣdl` (voiced `d`)
10248: - NOTE: "R/T p.435: PGmc *nēθlō/*nēdlō has Verner's alternation; OE nǣdl reflects *d variant"
10249: 
```

#### Germanic/docs/DEV_NOTES.md:10248 (exact COUNTERPART)

- Nearby heading: ### Analysis: `*nēθlō` → `nǣdl`

```text
10246: - PROTOFORM: `*nēθlō` (voiceless `*θ`)
10247: - COUNTERPART: `nǣdl` (voiced `d`)
10248: - NOTE: "R/T p.435: PGmc *nēθlō/*nēdlō has Verner's alternation; OE nǣdl reflects *d variant"
10249: 
10250: **Problem:** Same issue — TSV note explicitly acknowledges Verner's alternation
```

### Analysis and dossier hits

_None_

### Local lexical-table hits

#### old_english_wiktionary.tsv

| ENGLISH | OE_FORM | SOURCE | DETAIL | PAGE |
| :--- | :--- | :--- | :--- | :--- |
| needle | nǣdl | inh | template:inh | needle |

#### old_english_swadesh.tsv

_None_

## Possibly stale or diagnostic evidence

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:10259 (concept name)

- Nearby heading: ### Similar Cases to Review

```text
10257: Looking at current mismatches with `θ` → expected `d`:
10258: 1. ✓ `lade`: `*xlaθaną` → `*xlaðaną` (FIXED)
10259: 2. `needle`: `*nēθlō` → `*nēdlō` (TO FIX)
10260: 3. `withy`: `*wīθijăz` → expected `wīþiġ` — this has `þ` in OE, so NOT Verner
10261: 
```

#### Germanic/docs/DEV_NOTES.md:10391 (concept name)

- Nearby heading: ## Mismatch Progress Log (2026-03-14)

```text
10389: | 2026-03-12 | 78 | — | — | Baseline before nasalization work |
10390: | 2026-03-14 12:12 | 72 | -6 | 18b921e | Secondary nasalization (infinitives -an fixed) |
10391: | 2026-03-14 16:17 | 70 | -2 | 223ad24 | Verner TSV fixes: lade, needle |
10392: | 2026-03-14 20:34 | 65 | -5 | 62fced4 | Participle nasalization fix (funden) |
10393: | 2026-03-19 | 57 | -8 | — | Multiple TSV/FST fixes (huniġ, thistle, etc.) |
```

#### Germanic/docs/DEV_NOTES.md:31230 (concept name)

- Nearby heading: ##### §17.19.10.2.b Camp 2: the *u is a PGmc-internal or NWGmc-internal Sproßvokal (epenthetic vowel)

```text
31228: 
31229: §154 (line 6306) specifically on syllabic *l: "Silbenbildendes *l*
31230: ist sehr häufig nach *t* und *d*: *nǣdl ~ nēdl* 'needle', *spātl*
31231: 'spittle', *setl* 'seat', *botl* 'building', die fast nur in dieser
31232: Schreibung vorkommen; dann nach *s* und palatalem *g* wie *hūsl*,
```

### Analysis and dossier hits

_None_

## Bibliography-key candidates

### Preferred candidates

_None_

### Low-confidence candidates

_None_

