# Evidence packet — 1943 begin / beġinnan

> This packet is evidence for drafting. Do not treat all hits as equally authoritative; prefer high-confidence evidence.

## TSV row data

| ID | CONCEPT | COUNTERPART | PROTO | PROTOFORM | DERIVATION_CLASS | NOTE | HISTORY |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1943 | begin | beġinnan | *bigínnaną | *bigínnaną | regular | Palatalization of *g between *i and *i is regular per R/T §6.4.1 Rule 1. OE beġinnan confirmed (Wiktionary, BT). | - |

## Manifest status

_No manifest entry._

## High-confidence evidence

### Compact derivation trace entry

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

### Matching oe_known_problems.tsv entries

_None_

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:38378 (exact pair)

- Nearby heading: ## §17.36 *ĭ (i-breve) cleanup — incremental dismantling

```text
38376: | `*skíllingaz`    | `sċilling` | *-ing- suffix preservation |
38377: | `*wíkingaz`      | `wiċing`   | *-ing- suffix preservation |
38378: | `*bigínnaną`     | `beġinnan` | bi-/ni- prefix root preservation |
38379: | `*xárbistuz`     | `hierfest` | medial *i lowering (the canonical case) |
38380: | `*brínganą`      | `bringan`  | *brengan blocking, suffix-an protection |
```

### Analysis and dossier hits

_None_

## Supporting/background evidence

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:1491 (note keyword: palatalization)

- Nearby heading: ## Project Status (as of 2026-03-10)

```text
1489: - **Stem-class corrections**: god (*gudą), door (dor target vs duru)
1490: 
1491: **Remaining work:** 78 mismatches (u-lowering exceptions, breaking, palatalization, consonant clusters, data alignment).
1492: See `docs/analysis/notable_findings.md` for flagged scholarly issues.
1493: 
```

#### Germanic/docs/DEV_NOTES.md:1712 (note keyword: palatalization)

- Nearby heading: ## A-Restoration Fix (2026-02-06)

```text
1710:   - `breaking_missing`: 19
1711:   - `breaking_extra_other`: 23
1712:   - `palatalization_missing`: 6
1713:   - `fronting_missing_no_trigger`: 11
1714:   - `no_output`: 13
```

#### Germanic/docs/DEV_NOTES.md:1718 (note keyword: palatalization)

- Nearby heading: ## A-Restoration Fix (2026-02-06)

```text
1716:   - **Fronting undone by A‑restoration**: *nadrō (adder) fronting yields `*æ`, but `OldEnglishARestoration` flips it back due to a back vowel in the next syllable; output `nadrō` vs expected `nǣdre`. Consistent across `fronting_missing_no_trigger`.
1717:   - **Breaking gaps**: *brustz (breast) shows no u‑breaking; output `brust` vs expected `brēost`. *dawwō (dew) passes A‑F brightening (`*æw`) but `EnglishBreakingA` lacks a `w` context; output `dawō` vs expected `dēaw`.
1718:   - **Palatalization missing**: *bōkō (beech) never triggers `VelarPalatalization`; output `bōcō` vs expected `bēċe`. In the trace there is no fronting stage that would supply the trigger, so this is likely a rule/chronology or etymon/expected mismatch.
1719: - Measured ARestoration intervening segments (2026-02-05, OE sandbox):
1720:   - True positives (31 items): top intervening segments `n, k, w, d, j` (e.g., *bakăną -> bacan, inter=`k`; *xanduz -> hand, inter=`nd`).
```

#### Germanic/docs/DEV_NOTES.md:1725 (note keyword: palatalization)

- Nearby heading: ## A-Restoration Fix (2026-02-06)

```text
1723:   1. Tighten `OldEnglishARestoration` so it ignores weak‑tail vowels (or move it after weak‑tail reduction), then regenerate reports.
1724:   2. Add `a/æ + w` breaking plus explicit **u‑breaking** rules to `EnglishBreakingLengthening`, then regenerate.
1725:   3. Deep dive `palatalization_missing` (e.g., *bōkō) to confirm whether the rule/chronology or the expected form is wrong.
1726: - Hedge (2026-01-20):
1727:   - Reverted the orthographic `{ʤj} -> {ċġ}` mapping and removed `{ċġ}` from `OldEnglishSurfaceConsonant` (OE output should stay `ġġ`).
```

#### Germanic/docs/DEV_NOTES.md:1751 (note keyword: palatalization)

- Nearby heading: ## A-Restoration Fix (2026-02-06)

```text
1749:   - If a rule seems inert, confirm it against the **exact** bin used by reports (`old_english_sandbox_after_proto_to_oe_weak_tail.bin`) rather than a locally built test transducer.
1750: - OE *-gj- chronology check (2026-01-22):
1751:   - Standard descriptions show WGmc **gemination before *j** in short stems and **i‑mutation following *i/*j**, with classic paths like *satjan > *sattjan > *sættjan > *settian > OE settan; palatalization of velars by *j precedes i‑mutation in the usual OE chronology. Sources: Hasenfratz appendices (WVU “Reading Old English”) and the OE phonological history summary citing Campbell.
1752:   - Implementation aligned to this: allow **palatalized consonants** (ʤ/ʧ/ʃ/ç/ʒ/j) to count as intervening segments for i‑umlaut so raising can apply **after palatalization** rather than being blocked by non‑star symbols.
1753:   - Result: *xagjăz → **heġġ** and *sangjăną → **senġan** in `oe_full_trace_report_2026-01-22g.txt`; *baugjăną still mispredicts `bīeġan` (see final_vowel_missing bucket).
```

#### Germanic/docs/DEV_NOTES.md:1752 (note keyword: palatalization)

- Nearby heading: ## A-Restoration Fix (2026-02-06)

```text
1750: - OE *-gj- chronology check (2026-01-22):
1751:   - Standard descriptions show WGmc **gemination before *j** in short stems and **i‑mutation following *i/*j**, with classic paths like *satjan > *sattjan > *sættjan > *settian > OE settan; palatalization of velars by *j precedes i‑mutation in the usual OE chronology. Sources: Hasenfratz appendices (WVU “Reading Old English”) and the OE phonological history summary citing Campbell.
1752:   - Implementation aligned to this: allow **palatalized consonants** (ʤ/ʧ/ʃ/ç/ʒ/j) to count as intervening segments for i‑umlaut so raising can apply **after palatalization** rather than being blocked by non‑star symbols.
1753:   - Result: *xagjăz → **heġġ** and *sangjăną → **senġan** in `oe_full_trace_report_2026-01-22g.txt`; *baugjăną still mispredicts `bīeġan` (see final_vowel_missing bucket).
1754: - OE epenthesis update (2026-01-04):
```

#### Germanic/docs/DEV_NOTES.md:6778 (exact COUNTERPART)

- Nearby heading: ### Implementation Attempt #1: Simple Parallel Rule (FAILED)

```text
6776: 
6777: **Result:** This caused a regression on `begin`:
6778: - `*biginnăną` → `beġennan` (wrong) instead of `beġinnan` (correct)
6779: 
6780: **Problem:** The rule lowered the ROOT vowel `*i` in `ginn-`, not just the
```

#### Germanic/docs/DEV_NOTES.md:6871 (exact COUNTERPART)

- Nearby heading: # Step 4: Lower only marked unstressed *ĭ to *e

```text
6869:    - After Step 1: `*b*ĭ*ʤ*ĭ*n*n...` (root *i also marked)
6870:    - After Step 3: `*b*ĭ*ʤ*i*n*n...` (root *ĭ restored — stressed)
6871:    - After lowering: prefix *ĭ → *e, root *i preserved → `beġinnan` ✓
6872: 
6873: **Results:**
```

#### Germanic/docs/DEV_NOTES.md:6875 (exact COUNTERPART)

- Nearby heading: # Step 4: Lower only marked unstressed *ĭ to *e

```text
6873: **Results:**
6874: - `*xarbistuz` → `hierfest` ✓ (fixed from `hierfist`)
6875: - `*biginnăną` → `beġinnan` ✓ (no regression)
6876: - Evaluation: 307/386 matches (79.5%)
6877: 
```

#### Germanic/docs/DEV_NOTES.md:6922 (exact COUNTERPART)

- Nearby heading: ### Implementation Hurdle: Word-Final *ĭ (Dill Regression)

```text
6920: - `*deliz` → `dile` ✓
6921: - `*xarbistuz` → `hierfest` ✓
6922: - `*biginnăną` → `beġinnan` ✓
6923: - Evaluation: 310/386 matches (80.3%) — net +1 from harvest fix
6924: 
```

#### Germanic/docs/DEV_NOTES.md:17441 (exact COUNTERPART)

- Nearby heading: #### 12. Fulk vs. Our Implementation of `*i → *e` (2026-04-12)

```text
17439:    But the attested form has *i* (`cwidu`). Is this analogical restoration?
17440: 
17441: 2. `*biginnăną` → OE `beġinnan` — **RESOLVED**: The `*be-` does NOT come from NWGmcILowering!
17442:    It comes from a SEPARATE rule: **OEMedUnstressedILowering** (line ~1729).
17443:    
```

#### Germanic/docs/DEV_NOTES.md:17452 (exact COUNTERPART)

- Nearby heading: #### 12. Fulk vs. Our Implementation of `*i → *e` (2026-04-12)

```text
17450:    R/T vol.2 p.303 confirms: "So also bi- > be-, ni 'not' > ne."
17451: 
17452: **Summary:** The `*biginnăną → beġinnan` case does NOT test NWGmcILowering. It tests the
17453: separate unstressed prefix lowering rule.
17454: 
```

### Analysis and dossier hits

#### Germanic/docs/analysis/arestoration_r_l_research.md:696 (note keyword: palatalization)

- Nearby heading: ### 10.5 Predicted effects on neighbouring rule behaviour

```text
695: * `*hnappōjan → hnappian` (Campbell §158): intervening `*pp` — geminate in set — restoration applies. ✓
696: * `*flaskōn → flasce` (germanic.txt comment line 1798): intervening `*sk` — `sC` in set — restoration applies, then `SkPalatalization` runs after the *a*. ✓ (Still produces `flasce`, not `flæsce`.)
697: * `*næglaz` plural `*næglas` → `næglas` (Campbell §158): intervening `*gl` — `Cl` cluster, **not** in the new set — restoration does *not* apply. ✓ (consistent with Campbell's "always *næglas*").
```

#### Germanic/docs/analysis/four_complex_tsv_items.md:105 (note keyword: palatalization)

- Nearby heading: ### Proto-form assessment

```text
104: The proto `*skellinăz` does not match Kroonen's reconstruction. The \*e in
105: \*skellinăz would give OE \*sċiellen (via i-umlaut and palatalization), but the
106: attested form is sċilling with *i.
```

#### Germanic/docs/analysis/fryhtu_investigation.md:299 (note keyword: palatalization)

- Nearby heading: ### Test battery (all verified)

```text
298: | furxtiθō | fyrhtu | fyrhtu | ✓ |
299: | strangiθō | strenġþu | strengþu | ✓ (palatalization variant) |
300: | langiθō | lenġþu | lengþu | ✓ |
```

#### Germanic/docs/analysis/notable_findings.md:1425 (note keyword: palatalization)

- Nearby heading: ### Resolution (DEV_NOTES §17.10.35, 2026-04-23)

```text
1424:    (Campbell §376 *e > *i / _g) → *wīþ-igą → (apocope of nasal
1425:    vowel; palatalization of *g before *i) → wīþ-iġ ✓
1426: 
```

#### Germanic/docs/analysis/notable_findings.md:1561 (note keyword: palatalization)

- Nearby heading: ## 10. OE rēc 'smoke': the missing WS rīec problem

```text
1560: reading. So whatever the right input is, it cannot be one that
1561: triggers OEVelarPalatalization on the final *k.
1562: 
```

#### Germanic/docs/dossiers/g-palatalisation-conditioning.md:118 (note keyword: palatalization)

- Nearby heading: ### 2.2 Hogg, *Grammar of Old English* vol. 1 (1992), §§ 7.34 ff. (palatalisation chapter)

```text
117: 
118: > "Pre-OE /k/ and /ɣ/ underwent palatalization when the velar consonant was
119: > adjacent to and in the same syllable as a front vowel or a palatal
```

#### Germanic/docs/dossiers/g-palatalisation-conditioning.md:122 (note keyword: palatalization)

- Nearby heading: ### 2.2 Hogg, *Grammar of Old English* vol. 1 (1992), §§ 7.34 ff. (palatalisation chapter)

```text
121: > syllable as a front vowel and palatalizes; but in *cyning*, where /y/ is
122: > from i-umlaut of /u/, the conditioning is absent because palatalization
123: > had ceased to operate by the time *y* arose."
```

#### Germanic/docs/dossiers/g-palatalisation-conditioning.md:142 (note keyword: palatalization)

- Nearby heading: ### 2.3 Ringe & Taylor, *The Development of Old English* (= *A Linguistic History of English* vol. 2, 2014), § 6.4.1

```text
141: 
142: > "We can summarize the conditioning of palatalization as follows.
143: >
```

### Local lexical-table hits

#### old_english_wiktionary.tsv

| ENGLISH | OE_FORM | SOURCE | DETAIL | PAGE |
| :--- | :--- | :--- | :--- | :--- |
| begin | beginnan | inh | template:inh | begin |

#### old_english_swadesh.tsv

_None_

## Possibly stale or diagnostic evidence

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:2485 (concept name)

- Nearby heading: ### Ending diagnostics (old_english.bin)

```text
2483: - Final high vowels: `i` 22, `u` 20; most common contexts `ti/di` for `-i`, `þu/du/tu` for `-u`.
2484: - Sample `-i/-u` outputs: `ballu` (ball), `bebru` (beaver), `balgi` (belly), `crafti` (craft), `bugu` (bough).
2485: - Sample `-ana` outputs where target is `-an`: `bacana` (bake), `gennana` (begin), `brecana` (break), `brengana` (bring), `brūcana` (brook).
2486: 
2487: ### OE diagnostics refresh (2025-12-21)
```

#### Germanic/docs/DEV_NOTES.md:6518 (concept name)

- Nearby heading: ### Attestation Evidence

```text
6516: **Campbell (1959) §427** lists **`gift gift`** (not `gieft`) as an example:
6517: > "Examples of initial palatal sounds are: ... **gift gift**, gifre greedy,
6518: > ginnan begin, gefan (W-S giefan) give..."
6519: 
6520: Note Campbell writes `gift` but `giefan` — the difference is precisely because
```

#### Germanic/docs/DEV_NOTES.md:6777 (concept name)

- Nearby heading: ### Implementation Attempt #1: Simple Parallel Rule (FAILED)

```text
6775: ```
6776: 
6777: **Result:** This caused a regression on `begin`:
6778: - `*biginnăną` → `beġennan` (wrong) instead of `beġinnan` (correct)
6779: 
```

#### Germanic/docs/DEV_NOTES.md:6866 (concept name)

- Nearby heading: # Step 4: Lower only marked unstressed *ĭ to *e

```text
6864:    - After lowering: `*h*a*r*b*e*s*t*u*z` → `hierfest` ✓
6865: 
6866: 2. `*biginnăną` (begin):
6867:    - Input: `*b*i*ʤ*i*n*n*ă*n*ą` (after palatalization)
6868:    - After Step 2: `*b*ĭ*ʤ*i*n*n...` (prefix *i marked)
```

#### Germanic/docs/DEV_NOTES.md:23896 (concept name)

- Nearby heading: #### 3. Revised Option δ — in-place split of the PGmc-stage rule

```text
23894: form is the one just produced by Rule 1. `PGmcFinalZDeletion` has not
23895: yet fired, so no `*-a` from `*-az` exists yet. And audit item (1)
23896: confirms no PROTOFORM row has a bare word-final `*-a` to begin with.
23897: 
23898: #### 4. Honest disclosure — relative chronology reversed
```

#### Germanic/docs/DEV_NOTES.md:38441 (exact pair)

- Nearby heading: ### §17.36.3 Step 2 — drop OEUnstressedIMarking2 from the composition

```text
38439: Verification:
38440: - All 12 sentinels produce expected outputs unchanged
38441:   (`*bigínnaną → beġinnan` confirms the prefix protection still works
38442:   via `OEPrefixIReduction`).
38443: - Mismatch count: 20 → 20.
```

#### Germanic/docs/DEV_NOTES.md:43737 (concept name)

- Nearby heading: #### §17.51.A1.1 — Implementation status and open question (medial *u survival)

```text
43735: The original rule's exclusion `[{*u}|{*ū}]` was, in practice, written
43736: to avoid trivially same-vowel mergers, not as a stress-harmony
43737: device, so it was insufficient to begin with. Extending it to `*ú`
43738: treats stress as the discriminator, but stress alone does not
43739: separate the two environments above.
```

### Analysis and dossier hits

#### Germanic/docs/analysis/notable_findings.md:420 (concept name)

- Nearby heading: ### Expert consultation (Stefan Schuhmacher, Vienna, 2026-03-20)

```text
419: 
420: **On the scope of the rule:** "To begin with, it must be mentioned that such
421: lowering **affects only stressed vowels**... I do not see that the lowering
```

## Bibliography-key candidates

### Preferred candidates

| Key | Why it was selected |
| :--- | :--- |
| Kroonen2013 | default Proto-Germanic etymology key for Kroonen |
| Campbell1959 | single available key for Campbell |

### Low-confidence candidates

| Key | Why it was selected |
| :--- | :--- |
| Kroonen2011 | surname mention only: Kroonen |
| Kroonen2006 | surname mention only: Kroonen |

