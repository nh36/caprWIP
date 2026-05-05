# Evidence packet — 2181 shilling / sċilling

> This packet is evidence for drafting. Do not treat all hits as equally authoritative; prefer high-confidence evidence.

## TSV row data

| ID | CONCEPT | COUNTERPART | PROTO | PROTOFORM | DERIVATION_CLASS | NOTE | HISTORY |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2181 | shilling | sċilling | *skíllingaz | *skíllingaz | regular | Kroonen EDPG s.v. *skellinga- ~ *skillinga- (m.); WGmc cognates (OS skilling, OHG scilling, OFris skilling) and ON skillingr all confirm *-ing- derivational suffix. PROTOFORM corrected from *skéllinaz to *skíllingaz 2026-04-27. Required new pgrmWeakTailVowel shape *-ingaz and an *_*ng exemption in OEMedUnstressedILowering. See DEV_NOTES §17.35 and dossier-ing-lowering-2026.md. | Source: Wiktionary etymology (template:inh) \| Source: Wiktionary etymology (template:inh) |

## Manifest status

_No manifest entry._

## High-confidence evidence

### Compact derivation trace entry

```md
# shilling
PROTO: *skíllingaz
EXPECTED: sċilling
OUTPUTS: sċilling



### Proto-Germanic consonant inheritance

Proto Input: *skíllingaz

| Earlier Germanic developments | Old English developments |
|:---|:---|
| **Proto-West Germanic**<br>[no change]<br><br>**Northwest Germanic**<br>PGmc Final Z Deletion: *skíllinga | **Old English**<br>PWGmc Final Bare A Loss: *skílling<br>OE Sk Palatalization: *ʃílling<br>OE Med Unstressed I Lowering1: *ʃílleng<br>OE Med Unstressed I Lowering: *ʃílling |



### Orthography & surface

Old English Orthography: sċ*ílling
Outcome: sċilling

NOTE: Kroonen EDPG s.v. *skellinga- ~ *skillinga- (m.); WGmc cognates (OS skilling, OHG scilling, OFris skilling) and ON skillingr all confirm *-ing- derivational suffix. PROTOFORM corrected from *skéllinaz to *skíllingaz 2026-04-27. Required new pgrmWeakTailVowel shape *-ingaz and an *_ng exemption in OEMedUnstressedILowering. See DEV_NOTES §17.35 and dossier-ing-lowering-2026.md.
```

### Matching oe_known_problems.tsv entries

_None_

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:38085 (row ID)

- Nearby heading: ## §17.35 — *skéllinaz / sċilling (row 2181): missing PGmc *-ingaz derivational suffix

```text
38083: overgeneration that the mismatch report currently masks.
38084: 
38085: ## §17.35 — *skéllinaz / sċilling (row 2181): missing PGmc *-ingaz derivational suffix
38086: 
38087: ### §17.35.1 The mismatch
```

#### Germanic/docs/DEV_NOTES.md:38089 (row ID)

- Nearby heading: ### §17.35.1 The mismatch

```text
38087: ### §17.35.1 The mismatch
38088: 
38089: TSV row 2181 has PROTOFORM `*skéllinaz` and target `sċilling`. The FST
38090: produces `sċillen`. The vowel and palatalisation are right; the missing
38091: piece is the final `-g` and the underlying `-ing-` morpheme.
```

#### Germanic/docs/DEV_NOTES.md:38125 (exact pair)

- Nearby heading: ### §17.35.3 The bigger issue — *-ingaz is missing from pgrmWeakTailVowel

```text
38123: *kúningaz   → +?    (should yield cyning)
38124: *wíkingaz   → +?    (should yield wīcing)
38125: *skíllingaz → +?    (should yield sċilling)
38126: *kéttingaz  → +?    (synthetic, but a structural test)
38127: ```
```

#### Germanic/docs/DEV_NOTES.md:38159 (exact COUNTERPART)

- Nearby heading: ### §17.35.4 The PGmc `-ingaz` suffix (philological background)

```text
38157: - In nom.sg., *-az* is lost by PWGmc final-syllable apocope (§…
38158:   cited at line 21354), leaving bare *-ing*. Hence OE *cyning*,
38159:   *sċilling* are bare nom.sg. forms with no overt ending.
38160: 
38161: ### §17.35.5 What the FST should produce from *skíllingaz
```

#### Germanic/docs/DEV_NOTES.md:38161 (exact PROTOFORM)

- Nearby heading: ### §17.35.5 What the FST should produce from *skíllingaz

```text
38159:   *sċilling* are bare nom.sg. forms with no overt ending.
38160: 
38161: ### §17.35.5 What the FST should produce from *skíllingaz
38162: 
38163: Predicted derivation (manual, pending probe after the fix):
```

#### Germanic/docs/DEV_NOTES.md:38202 (row ID)

- Nearby heading: ### §17.35.6 Plan

```text
38200: `-ingaz`.
38201: 
38202: **(B) TSV PROTOFORM correction.** Row 2181: change
38203: `PROTOFORM` and `PROTO` from `*skéllinaz` to `*skíllingaz` (with
38204: acute on *í* per Kroonen and the i-umlaut requirement; the
```

#### Germanic/docs/DEV_NOTES.md:38248 (row ID)

- Nearby heading: ### §17.35.9 Files to change

```text
38246: - `Germanic/fsts/germanic.txt`: one new line in `pgrmWeakTailVowel`.
38247: - `Germanic/data/germanic-aligned-final.tsv`: rows 962, 963, 2181:
38248:   PROTOFORM `*skéllinaz` → `*skíllingaz`; PROTO same; row 2181
38249:   NOTE rewritten.
38250: - Reports + bins regenerated.
```

#### Germanic/docs/DEV_NOTES.md:38295 (exact pair)

- Nearby heading: ### §17.35.10 Closure (2026-04-27)

```text
38293: | ------------------ | ----------- | ------ |
38294: | `*kúningaz`        | `cyning`    | ✓ fixed |
38295: | `*skíllingaz`      | `sċilling`  | ✓ fixed |
38296: | `*wíkingaz`        | `wiċing`    | ✓ fixed |
38297: | `*brínganą`        | `bringan`   | ✓ no change |
```

#### Germanic/docs/DEV_NOTES.md:38350 (row ID)

- Nearby heading: ### §17.35.12 Files changed in this closure

```text
38348:     *e → *i restoration before *ng cluster.
38349: - `Germanic/data/germanic-aligned-final.tsv`: rows 962/963/2181
38350:   PROTOFORM `*skéllinaz` → `*skíllingaz`; row 2181 NOTE rewritten.
38351: - `Germanic/docs/dossier-ing-lowering-2026.md`: new (research
38352:   dossier produced by background agent).
```

#### Germanic/docs/DEV_NOTES.md:38376 (exact pair)

- Nearby heading: ## §17.36 *ĭ (i-breve) cleanup — incremental dismantling

```text
38374: | ---------------- | ---------- | ----- |
38375: | `*kúningaz`      | `cyning`   | *-ing- suffix preservation |
38376: | `*skíllingaz`    | `sċilling` | *-ing- suffix preservation |
38377: | `*wíkingaz`      | `wiċing`   | *-ing- suffix preservation |
38378: | `*bigínnaną`     | `beġinnan` | bi-/ni- prefix root preservation |
```

### Analysis and dossier hits

#### Germanic/docs/analysis/four_complex_tsv_items.md:90 (row ID)

- Nearby heading: ## 2. *skellinăz → sċilling "shilling" (ID 2181)

```text
89: 
90: ## 2. *skellinăz → sċilling "shilling" (ID 2181)
91: 
```

## Supporting/background evidence

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:38095 (exact COUNTERPART)

- Nearby heading: ### §17.35.2 Etymology — the proto is wrong

```text
38093: ### §17.35.2 Etymology — the proto is wrong
38094: 
38095: OE *sċilling* is universally reconstructed with PGmc derivational
38096: suffix `-ing-` (a-stem masc). Sources concur:
38097: 
```

#### Germanic/docs/DEV_NOTES.md:38112 (exact PROTOFORM)

- Nearby heading: ### §17.35.3 The bigger issue — *-ingaz is missing from pgrmWeakTailVowel

```text
38110: ### §17.35.3 The bigger issue — *-ingaz is missing from pgrmWeakTailVowel
38111: 
38112: When I tried correcting the PROTOFORM to `*skíllingaz` (or any
38113: `*Vingaz` variant), the FST returned `+?` (no output) at the
38114: `proto_input` stage. The proto-input grammar `pgrmWeakTailVowel`
```

#### Germanic/docs/DEV_NOTES.md:38148 (exact COUNTERPART)

- Nearby heading: ### §17.35.4 The PGmc `-ingaz` suffix (philological background)

```text
38146:   ('member of'), diminutive. Examples: *cyning* 'king' < ?\*kunja-
38147:   'kin' + -ing-; *æþeling* 'noble's son'; *wīcing* 'viking';
38148:   *Wōdening* 'descendant of Wōden'; *sċilling* 'shilling' (probably
38149:   divisional, < *skel-).
38150: - *-ungō* (ō-stem fem): action/abstract nouns from verbs, e.g.
```

#### Germanic/docs/DEV_NOTES.md:38165 (exact PROTOFORM)

- Nearby heading: ### §17.35.5 What the FST should produce from *skíllingaz

```text
38163: Predicted derivation (manual, pending probe after the fix):
38164: 
38165: 1. `*skíllingaz` (PGmc).
38166: 2. PWGmc *z-loss + *a-loss in nom.sg.: `*skíllingØ`.
38167: 3. *sk-palatalisation before front vowel: `*ʃkíllingØ`.
```

#### Germanic/docs/DEV_NOTES.md:38203 (exact PROTOFORM)

- Nearby heading: ### §17.35.6 Plan

```text
38201: 
38202: **(B) TSV PROTOFORM correction.** Row 2181: change
38203: `PROTOFORM` and `PROTO` from `*skéllinaz` to `*skíllingaz` (with
38204: acute on *í* per Kroonen and the i-umlaut requirement; the
38205: parallel English row 963 and German row 962 also share this
```

### Analysis and dossier hits

#### Germanic/docs/analysis/four_complex_tsv_items.md:13 (exact COUNTERPART)

- Nearby heading: ## Overview

```text
12: | `*xlaxjăną` | hliehan | hlæhhan | Mismatch |
13: | `*skellinăz` | sċiellen | sċilling | Mismatch |
14: | `*furxtīn` | fyrhten | fryhtu | Mismatch |
```

#### Germanic/docs/analysis/fryhtu_investigation.md:305 (exact COUNTERPART)

- Nearby heading: ### Test battery (all verified)

```text
304: | θestilăz | þistel | þistel | ✓ (no regression) |
305: | skellinăz | sċiellen | sċilling | — (pre-existing mismatch) |
306: | wīθijăz | wīþeġ | wīþiġ | — (pre-existing mismatch) |
```

### Local lexical-table hits

#### old_english_wiktionary.tsv

| ENGLISH | OE_FORM | SOURCE | DETAIL | PAGE |
| :--- | :--- | :--- | :--- | :--- |
| shilling | sċilling | inh | template:inh | shilling |

#### old_english_swadesh.tsv

_None_

## Possibly stale or diagnostic evidence

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:10426 (exact PROTOFORM)

- Nearby heading: ## Mismatch Progress Log (2026-03-14)

```text
10424: | 2026-04-26 | 20 | -1 | 871ec6ab | bēġen: TSV revert + monosyllable apocope guard (§17.30/31) |
10425: | 2026-04-26 | 19 | -1 | dc035fda | streċċan: OEVelarPalatalization *kk before *j (§17.34) |
10426: | 2026-04-27 | 18 | -1 | 56586a61 | *skíllingaz: pgrm grammar + *i lowering (§17.35/36 cleanup) |
10427: | 2026-04-28 | 17 | -1 | 8917de42 | weasel: target retarget Anglian weosule → WS wesle (§17.37) |
10428: | 2026-04-28 | 16 | -1 | 7f8a289b | westene: target alignment with *wéstanē (§17.38) |
```

#### Germanic/docs/DEV_NOTES.md:38252 (row ID)

- Nearby heading: ### §17.35.9 Files to change

```text
38250: - Reports + bins regenerated.
38251: 
38252: Expected post-fix: row 2181 mismatch closed; mismatches 21 → 20.
38253: Probes of *kuningaz* / *wīkingaz* / *æþelingaz* should also
38254: succeed but they are not in the TSV, so they don't affect the
```

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

