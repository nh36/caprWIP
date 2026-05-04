# Evidence packet — 2309 make (iptv.2sg) / maca

> This packet is evidence for drafting. Do not treat all hits as equally authoritative; prefer high-confidence evidence.

## TSV row data

| ID | CONCEPT | COUNTERPART | PROTO | PROTOFORM | DERIVATION_CLASS | NOTE | HISTORY |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2309 | make (iptv.2sg) | maca | *makōną | *mákô | late_analogy | Class II weak iptv. 2sg test (R/T §5.2). Trimoric *ō → OE -a. | - |

## Manifest status

_No manifest entry._

## High-confidence evidence

### Compact derivation trace entry

```md
# make (iptv.2sg)
PROTO: *mákô
EXPECTED: maca
OUTPUTS: maca



### Proto-Germanic consonant inheritance

Proto Input: *mákô

| Earlier Germanic developments | Old English developments |
|:---|:---|
| **Proto-West Germanic**<br>[no change]<br><br>**Northwest Germanic**<br>[no change] | **Old English**<br>Anglo Frisian Brightening: *mækô<br>OE A Restoration: *makô<br>OE Unstressed Long Vowel Shortening: *maka |



### Orthography & surface

Outcome: maca

NOTE: Class II weak iptv. 2sg test (R/T §5.2). Trimoric *ō → OE -a.
```

### Matching oe_known_problems.tsv entries

_None_

### DEV_NOTES hits

_None_

### Analysis and dossier hits

_None_

## Supporting/background evidence

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:2785 (exact COUNTERPART)

- Nearby heading: ### Issues to Resolve

```text
2783:    root {*a} → {*æ}, but A-restoration doesn't fire because {*ô} is not in
2784:    PGmcStarBackVowel or OEARestorationTriggerVowel. This produces
2785:    *mæċa* (with spurious fronting + palatalization) instead of *maca*.
2786:    FIX: Add {*ô} to OEARestorationTriggerVowel.
2787: 
```

#### Germanic/docs/DEV_NOTES.md:2840 (exact COUNTERPART)

- Nearby heading: ### Options for Resolution

```text
2838: ### Options for Resolution
2839: 
2840: **Option A: Change citation form to iptv. 2sg** (e.g., *makō → maca)
2841: - Pro: Regular sound change, same development as masc. n-stems (trimoric *ō)
2842: - Con: Requires encoding as *makô (trimoric); needs A-restoration fix for {*ô};
```

#### Germanic/docs/DEV_NOTES.md:2865 (exact COUNTERPART)

- Nearby heading: ### A-Restoration Gap for {*ô}

```text
2863: ### A-Restoration Gap for {*ô}
2864: 
2865: Current problem: `makô` → `mæċa` (wrong) instead of `maca` (correct).
2866: 
2867: Derivation trace for `makô`:
```

#### Germanic/docs/DEV_NOTES.md:2909 (exact COUNTERPART)

- Nearby heading: ### Test forms: imperative 2sg and 3sg present indicative

```text
2907: To test the *regular* phonological developments, we use paradigm forms where the suffix is lautgesetzlich:
2908: 
2909: **Imperative 2sg** (*-ō, trimoric): PGmc *makō → OE maca
2910: - The trimoric *ō is modelled as {*ô} in our notation
2911: - {*ô} → OE -a via OEUnstressedLongVowelShortening (line 1317)
```

#### Germanic/docs/DEV_NOTES.md:2930 (exact COUNTERPART)

- Nearby heading: #### 1. A-restoration fix for {*ô}

```text
2928: ```
2929: 
2930: After fix: `makô → maca` ✓
2931: 
2932: **Justification:** {*ô} (trimoric *ō) IS a back vowel — it triggers A-restoration just like any other back vowel in the following syllable. It is deliberately excluded from PGmcStarBackVowel (to avoid regressions in general vowel rules), so it needs explicit inclusion in the trigger set.
```

#### Germanic/docs/DEV_NOTES.md:2952 (exact COUNTERPART)

- Nearby heading: #### 4. Results summary

```text
2950: | Form | FST output | Expected OE | Status |
2951: |------|-----------|-------------|--------|
2952: | makô | maca | maca | ✓ |
2953: | makōθi | maceþ | maceþ (regular) | ✓ |
2954: | burô | bura | bora | ✗ u-lowering |
```

### Analysis and dossier hits

_None_

### Local lexical-table hits

#### old_english_wiktionary.tsv

_None_

#### old_english_swadesh.tsv

_None_

## Possibly stale or diagnostic evidence

### DEV_NOTES hits

_None_

### Analysis and dossier hits

_None_

## Bibliography-key candidates

### Preferred candidates

_None_

### Low-confidence candidates

_None_

## Paradigm probe

Paradigm probe required for this row, but no built-in `oe_paradigm_probe.py` specification exists yet. This packet should be used to draft the probe configuration before prose drafting.

