# Evidence packet — 1943 begin / beġinnan

## TSV row data

| ID | CONCEPT | COUNTERPART | PROTO | PROTOFORM | DERIVATION_CLASS | NOTE | HISTORY |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1943 | begin | beġinnan | *bigínnaną | *bigínnaną | regular | Palatalization of *g between *i and *i is regular per R/T §6.4.1 Rule 1. OE beġinnan confirmed (Wiktionary, BT). | - |

## Manifest status

_No manifest entry._

## Compact derivation trace entry

```md
# begin
PROTO: *bigínnaną
EXPECTED: beġinnan
OUTPUTS: beġinnan



### Proto-Germanic consonant inheritance

Proto Input: *bigínnaną

| Earlier Germanic developments | Old English developments |
|:---|:---|
| **Proto-West Germanic**<br>[no change]<br><br>**Northwest Germanic**<br>[no change] | **Old English**<br>OE Heavy Syllable Nasal Apocope: *bigínnan<br>OE Secondary Nasalization: *bigínnąn<br>OE Velar Palatalization: *biʤínnąn<br>OE Prefix I Reduction: *bĕʤínnąn<br>OE Weak Tail Reduction: *bĕʤínnan |



### Orthography & surface

Old English Orthography: *bĕġínnan
Outcome: beġinnan

NOTE: Palatalization of *g between *i and *i is regular per R/T §6.4.1 Rule 1. OE beġinnan confirmed (Wiktionary, BT).
```

## Matching oe_known_problems.tsv entries

_None_

## DEV_NOTES hits

### exact PROTOFORM — DEV_NOTES.md:38378

- Nearby heading: ## §17.36 *ĭ (i-breve) cleanup — incremental dismantling

```text
38376: | `*skíllingaz`    | `sċilling` | *-ing- suffix preservation |
38377: | `*wíkingaz`      | `wiċing`   | *-ing- suffix preservation |
38378: | `*bigínnaną`     | `beġinnan` | bi-/ni- prefix root preservation |
38379: | `*xárbistuz`     | `hierfest` | medial *i lowering (the canonical case) |
38380: | `*brínganą`      | `bringan`  | *brengan blocking, suffix-an protection |
```

### exact PROTOFORM — DEV_NOTES.md:38441

- Nearby heading: ### §17.36.3 Step 2 — drop OEUnstressedIMarking2 from the composition

```text
38439: Verification:
38440: - All 12 sentinels produce expected outputs unchanged
38441:   (`*bigínnaną → beġinnan` confirms the prefix protection still works
38442:   via `OEPrefixIReduction`).
38443: - Mismatch count: 20 → 20.
```

### exact COUNTERPART — DEV_NOTES.md:6778

- Nearby heading: ### Implementation Attempt #1: Simple Parallel Rule (FAILED)

```text
6776: 
6777: **Result:** This caused a regression on `begin`:
6778: - `*biginnăną` → `beġennan` (wrong) instead of `beġinnan` (correct)
6779: 
6780: **Problem:** The rule lowered the ROOT vowel `*i` in `ginn-`, not just the
```

### exact COUNTERPART — DEV_NOTES.md:6871

- Nearby heading: # Step 4: Lower only marked unstressed *ĭ to *e

```text
6869:    - After Step 1: `*b*ĭ*ʤ*ĭ*n*n...` (root *i also marked)
6870:    - After Step 3: `*b*ĭ*ʤ*i*n*n...` (root *ĭ restored — stressed)
6871:    - After lowering: prefix *ĭ → *e, root *i preserved → `beġinnan` ✓
6872: 
6873: **Results:**
```

### exact COUNTERPART — DEV_NOTES.md:6875

- Nearby heading: # Step 4: Lower only marked unstressed *ĭ to *e

```text
6873: **Results:**
6874: - `*xarbistuz` → `hierfest` ✓ (fixed from `hierfist`)
6875: - `*biginnăną` → `beġinnan` ✓ (no regression)
6876: - Evaluation: 307/386 matches (79.5%)
6877: 
```

### exact COUNTERPART — DEV_NOTES.md:6922

- Nearby heading: ### Implementation Hurdle: Word-Final *ĭ (Dill Regression)

```text
6920: - `*deliz` → `dile` ✓
6921: - `*xarbistuz` → `hierfest` ✓
6922: - `*biginnăną` → `beġinnan` ✓
6923: - Evaluation: 310/386 matches (80.3%) — net +1 from harvest fix
6924: 
```

### exact COUNTERPART — DEV_NOTES.md:17441

- Nearby heading: #### 12. Fulk vs. Our Implementation of `*i → *e` (2026-04-12)

```text
17439:    But the attested form has *i* (`cwidu`). Is this analogical restoration?
17440: 
17441: 2. `*biginnăną` → OE `beġinnan` — **RESOLVED**: The `*be-` does NOT come from NWGmcILowering!
17442:    It comes from a SEPARATE rule: **OEMedUnstressedILowering** (line ~1729).
17443:    
```

### exact COUNTERPART — DEV_NOTES.md:17452

- Nearby heading: #### 12. Fulk vs. Our Implementation of `*i → *e` (2026-04-12)

```text
17450:    R/T vol.2 p.303 confirms: "So also bi- > be-, ni 'not' > ne."
17451: 
17452: **Summary:** The `*biginnăną → beġinnan` case does NOT test NWGmcILowering. It tests the
17453: separate unstressed prefix lowering rule.
17454: 
```

### concept name — DEV_NOTES.md:2485

- Nearby heading: ### Ending diagnostics (old_english.bin)

```text
2483: - Final high vowels: `i` 22, `u` 20; most common contexts `ti/di` for `-i`, `þu/du/tu` for `-u`.
2484: - Sample `-i/-u` outputs: `ballu` (ball), `bebru` (beaver), `balgi` (belly), `crafti` (craft), `bugu` (bough).
2485: - Sample `-ana` outputs where target is `-an`: `bacana` (bake), `gennana` (begin), `brecana` (break), `brengana` (bring), `brūcana` (brook).
2486: 
2487: ### OE diagnostics refresh (2025-12-21)
```

### concept name — DEV_NOTES.md:6518

- Nearby heading: ### Attestation Evidence

```text
6516: **Campbell (1959) §427** lists **`gift gift`** (not `gieft`) as an example:
6517: > "Examples of initial palatal sounds are: ... **gift gift**, gifre greedy,
6518: > ginnan begin, gefan (W-S giefan) give..."
6519: 
6520: Note Campbell writes `gift` but `giefan` — the difference is precisely because
```

### concept name — DEV_NOTES.md:6777

- Nearby heading: ### Implementation Attempt #1: Simple Parallel Rule (FAILED)

```text
6775: ```
6776: 
6777: **Result:** This caused a regression on `begin`:
6778: - `*biginnăną` → `beġennan` (wrong) instead of `beġinnan` (correct)
6779: 
```

### concept name — DEV_NOTES.md:6866

- Nearby heading: # Step 4: Lower only marked unstressed *ĭ to *e

```text
6864:    - After lowering: `*h*a*r*b*e*s*t*u*z` → `hierfest` ✓
6865: 
6866: 2. `*biginnăną` (begin):
6867:    - Input: `*b*i*ʤ*i*n*n*ă*n*ą` (after palatalization)
6868:    - After Step 2: `*b*ĭ*ʤ*i*n*n...` (prefix *i marked)
```

### concept name — DEV_NOTES.md:23896

- Nearby heading: #### 3. Revised Option δ — in-place split of the PGmc-stage rule

```text
23894: form is the one just produced by Rule 1. `PGmcFinalZDeletion` has not
23895: yet fired, so no `*-a` from `*-az` exists yet. And audit item (1)
23896: confirms no PROTOFORM row has a bare word-final `*-a` to begin with.
23897: 
23898: #### 4. Honest disclosure — relative chronology reversed
```

### concept name — DEV_NOTES.md:43737

- Nearby heading: #### §17.51.A1.1 — Implementation status and open question (medial *u survival)

```text
43735: The original rule's exclusion `[{*u}|{*ū}]` was, in practice, written
43736: to avoid trivially same-vowel mergers, not as a stress-harmony
43737: device, so it was insufficient to begin with. Extending it to `*ú`
43738: treats stress as the discriminator, but stress alone does not
43739: separate the two environments above.
```

## Analysis and dossier hits

### Germanic/docs/analysis/notable_findings.md:420 (concept name)

- Nearby heading: ### Expert consultation (Stefan Schuhmacher, Vienna, 2026-03-20)

```text
419: 
420: **On the scope of the rule:** "To begin with, it must be mentioned that such
421: lowering **affects only stressed vowels**... I do not see that the lowering
```

## Local lexical-table hits

### old_english_wiktionary.tsv

| ENGLISH | OE_FORM | SOURCE | DETAIL | PAGE |
| :--- | :--- | :--- | :--- | :--- |
| begin | beginnan | inh | template:inh | begin |

### old_english_swadesh.tsv

_None_

## Bibliography-key candidates

| Key | Why it was selected |
| :--- | :--- |
| Campbell1959 | author mention: Campbell |

