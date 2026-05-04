# Evidence packet — 1942 beech / bōc

> This packet is evidence for drafting. Do not treat all hits as equally authoritative; prefer high-confidence evidence.

## TSV row data

| ID | CONCEPT | COUNTERPART | PROTO | PROTOFORM | DERIVATION_CLASS | NOTE | HISTORY |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1942 | beech | bōc | *bōkō | *bōkō | regular | Kroonen *bōk(j)ō- f. > OE bōc (nom.sg.); bēċe is oblique form | - |

## Manifest status

_No manifest entry._

## High-confidence evidence

### Compact derivation trace entry

```md
# beech
PROTO: *bōkō
EXPECTED: bōc
OUTPUTS: bōc



### Proto-Germanic consonant inheritance

Proto Input: *bōkō

| Earlier Germanic developments | Old English developments |
|:---|:---|
| **Proto-West Germanic**<br>[no change]<br><br>**Northwest Germanic**<br>NWGmc Final Long O Raising: *bōku | **Old English**<br>OE High Vowel Apocope: *bōk |



### Orthography & surface

Outcome: bōc

NOTE: Kroonen *bōk(j)ō- f. > OE bōc (nom.sg.); bēċe is oblique form
```

### Matching oe_known_problems.tsv entries

_None_

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:1718 (exact pair)

- Nearby heading: ## A-Restoration Fix (2026-02-06)

```text
1716:   - **Fronting undone by A‑restoration**: *nadrō (adder) fronting yields `*æ`, but `OldEnglishARestoration` flips it back due to a back vowel in the next syllable; output `nadrō` vs expected `nǣdre`. Consistent across `fronting_missing_no_trigger`.
1717:   - **Breaking gaps**: *brustz (breast) shows no u‑breaking; output `brust` vs expected `brēost`. *dawwō (dew) passes A‑F brightening (`*æw`) but `EnglishBreakingA` lacks a `w` context; output `dawō` vs expected `dēaw`.
1718:   - **Palatalization missing**: *bōkō (beech) never triggers `VelarPalatalization`; output `bōcō` vs expected `bēċe`. In the trace there is no fronting stage that would supply the trigger, so this is likely a rule/chronology or etymon/expected mismatch.
1719: - Measured ARestoration intervening segments (2026-02-05, OE sandbox):
1720:   - True positives (31 items): top intervening segments `n, k, w, d, j` (e.g., *bakăną -> bacan, inter=`k`; *xanduz -> hand, inter=`nd`).
```

### Analysis and dossier hits

_None_

## Supporting/background evidence

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:1766 (exact COUNTERPART)

- Nearby heading: ## A-Restoration Fix (2026-02-06)

```text
1764:     - **PGmc *au not lengthened** → change `*aeu -> *ēa` (or add a dedicated “long diphthong” step right after leveling).
1765:     - **PGmc *eu/*iu not mapped to OE long diphthongs** → add `*eu/*iu -> *ēo` (WS merge).
1766:     - **OE ō before velars should stay long** → move `EnglishVelarShortening` out of the OE block (OE keeps bōc/bōg).
1767:   - “Other” misses (e.g., *end→ān, *utrăz→nǣdre, *xattuz→hōd) are not long‑vowel rules; treat separately.
1768:   - Bucket taxonomy update (2026-01-03): the report now splits the former `uncategorized` bucket into `palatal_marker_variant`, `epenthetic_vowel_missing`, `vowel_quality_other`, `gemination_extra`, and `consonant_mismatch_other`.
```

#### Germanic/docs/DEV_NOTES.md:2478 (exact PROTOFORM)

- Nearby heading: ### OE evaluator snapshot (old_english.bin)

```text
2476: - No output: 21
2477: - Mismatches: 353
2478: - Sample mismatches: `*bakăną -> bacana` vs `bacan`, `*bōkō -> bucō` vs `bēċe`, `*balgiz -> balgi` vs `bielġ`.
2479: - Common issue bucket still dominated by `-ana` outputs and lingering final high vowels.
2480: 
```

#### Germanic/docs/DEV_NOTES.md:2593 (exact PROTOFORM)

- Nearby heading: ### OE palatalization vs fronting/umlaut split (2025-12-23)

```text
2591: - **True i‑umlaut misses (strict trigger):** only 1 case (`*rugiz → ryġe` expected, output `rūġ`).  
2592:   The bulk of the “i‑umlaut/fronting missing” bucket is actually **fronting missing with no i/j trigger** (143 cases).
2593: - **Next actions:** prioritize fronting/breaking changes that create front‑vowel contexts (esp. for *bōkō, *θankăz, *dranką, *fleugăną, *xunăgą), then re‑check palatalization buckets.
2594: 
2595: ### OE i‑umlaut/fronting bucket diagnostics (2026-01-01)
```

#### Germanic/docs/DEV_NOTES.md:20578 (exact PROTOFORM)

- Nearby heading: ### §16.1 Inventory

```text
20576: | Unstressed short vowel (inflection / suffix) | `ă` | `*dagăz`, `*bakăną` |
20577: | Unstressed nasalized vowel (inflection) | `ą ę ų` | `*dagą`, `*xundą` |
20578: | Unstressed long vowel in inflection | `ō ē ī ū` (no accent) | `*bōkō`, `*mēnōθz` |
20579: 
20580: ### §16.2 Convention
```

### Analysis and dossier hits

_None_

### Local lexical-table hits

#### old_english_wiktionary.tsv

| ENGLISH | OE_FORM | SOURCE | DETAIL | PAGE |
| :--- | :--- | :--- | :--- | :--- |
| beech | bēċe | inh | template:inh | beech |
| book | bōc | inh | template:inh | book |

#### old_english_swadesh.tsv

_None_

## Possibly stale or diagnostic evidence

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:1725 (exact PROTOFORM)

- Nearby heading: ## A-Restoration Fix (2026-02-06)

```text
1723:   1. Tighten `OldEnglishARestoration` so it ignores weak‑tail vowels (or move it after weak‑tail reduction), then regenerate reports.
1724:   2. Add `a/æ + w` breaking plus explicit **u‑breaking** rules to `EnglishBreakingLengthening`, then regenerate.
1725:   3. Deep dive `palatalization_missing` (e.g., *bōkō) to confirm whether the rule/chronology or the expected form is wrong.
1726: - Hedge (2026-01-20):
1727:   - Reverted the orthographic `{ʤj} -> {ċġ}` mapping and removed `{ċġ}` from `OldEnglishSurfaceConsonant` (OE output should stay `ġġ`).
```

#### Germanic/docs/DEV_NOTES.md:1795 (concept name)

- Nearby heading: ### English sandbox todo — surface accuracy focus

```text
1793:   - Rhotic data audit: 118 English proto entries contain `{r}`; the problematic clusters are `rdă` (4 entries), `rgă` (1), `rwō` (1), `rθo` (1). These align exactly with `tmp/rhotic_test_set.txt`. We need historically grounded rewrites (e.g. `{*rgă → {*rəʊ}}`, `{*rdă → {*ər}}`, `{*rwō → {*rəʊ}}`, `{*erθo → {*erθ}}) before `EnglishSandboxPostVocalicRLoss` deletes `{*r}`.
1794:   - Next session: redesign `EnglishSandboxProtoRhoticFronting`/`EnglishSandboxRhoticBreaking` around those phonetic targets, rerun the rhotic tracer, and rerun `python3 tools/english_apply_down_stats.py` (current baseline: 333/376 single outputs, 20 exact matches).
1795: - **Add the missing palatalisation pass.** Insert a dedicated `EnglishSandboxPalatalisation` stage (after West Germanic or glide deletion) that maps `{*bj→v}`, `{*gj→dʒ}`, `{*kj→tʃ}`, `{*sk→ʃ}` before front vowels. This captures the well-known West Saxon/Midlands changes needed for `believe/beech/chew/shield/ship` and collapses a large swath of remaining errors.
1796: - Once these three TODOs land, rerun `tools/english_apply_down_stats.py` to confirm the “exactly one correct output” count climbs beyond the current ~20/376.
1797: 
```

#### Germanic/docs/DEV_NOTES.md:2605 (exact PROTOFORM)

- Nearby heading: ### OE i‑umlaut/fronting bucket diagnostics (2026-01-01)

```text
2603: - **Staged traces for each subgroup:** `docs/debug_snapshots/oe_iumlaut_fronting_subgroup_traces_2026-01-01.txt`.
2604:   - i‑mutation trigger examples: *furxtīn → fōrhtīn (expected fryhtu), *raukiz → reaċ (expected rēc), *rugiz → rūġ (expected ryġe)
2605:   - back‑vowel follow examples: *bergą → beorga (expected beorg), *bōkō → bucō (expected bēċe), *gennăną → ġennan (expected beginnan)
2606:   - nasal‑block examples: *dranką → drænca (expected drenċ), *tangō → tængō (expected tange)
2607: 
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

## Paradigm probe

Philological note; no paradigm probe required for this row under the current classification. The note mentions paradigm forms, but it does not yet depend on a paradigm-cell solution.

