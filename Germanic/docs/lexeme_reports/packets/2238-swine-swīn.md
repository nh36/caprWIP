# Evidence packet — 2238 swine / swīn

> This packet is evidence for drafting. Do not treat all hits as equally authoritative; prefer high-confidence evidence.

## TSV row data

| ID | CONCEPT | COUNTERPART | PROTO | PROTOFORM | DERIVATION_CLASS | NOTE | HISTORY |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2238 | swine | swīn | *swī́ną | *swḯną | regular | Proto: oblique *swīnăn→*swīną (n. a-stem nom.sg.; Kroonen) §17.46 Phase 2: PROTOFORM accented (ḯ = stressed long *ī, U+1E2F) so NWGmcInStemNLoss does not fire on the root *ī. | - |

## Manifest status

_No manifest entry._

## High-confidence evidence

### Compact derivation trace entry

```md
# swine
PROTO: *swḯną
EXPECTED: swīn
OUTPUTS: swīn



### Proto-Germanic consonant inheritance

Proto Input: *swḯną

| Earlier Germanic developments | Old English developments |
|:---|:---|
| **Proto-West Germanic**<br>[no change]<br><br>**Northwest Germanic**<br>[no change] | **Old English**<br>OE Heavy Syllable Nasal Apocope: *swḯn |



### Orthography & surface

Outcome: swīn

NOTE: Proto: oblique *swīnăn→swīną (n. a-stem nom.sg.; Kroonen) §17.46 Phase 2: PROTOFORM accented (ḯ = stressed long *ī, U+1E2F) so NWGmcInStemNLoss does not fire on the root *ī.
```

### Matching oe_known_problems.tsv entries

_None_

### DEV_NOTES hits

_None_

### Analysis and dossier hits

_None_

## Supporting/background evidence

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:41769 (exact COUNTERPART)

- Nearby heading: ### A. Round 3 probe (post-Fix-1' application)

```text
41767: But the mismatch report rose 13 → 14, with one regression:
41768: 
41769: > `*swīną → swī (expected swīn)`
41770: 
41771: `*swīną` is a neuter a-stem 'swine' (root-stressed monosyllable).
```

#### Germanic/docs/DEV_NOTES.md:41777 (exact COUNTERPART)

- Nearby heading: ### A. Round 3 probe (post-Fix-1' application)

```text
41775: 2. `*swī*n*ą` (after gate)
41776: 3. ... (NWGmc / OE stages with no effect on this segmentation)
41777: 4. `*swīn` (after `OEHeavySyllableNasalApocope` strips nasal *-ą)
41778: 5. `*swī` (after the new `NWGmcInStemNLoss`, which over-applies to the
41779:    monosyllabic root-stressed *ī)
```

#### Germanic/docs/DEV_NOTES.md:41794 (exact COUNTERPART)

- Nearby heading: ### B. Diagnosis: rule context too broad

```text
41792:   stressed root + cluster).
41793: * The unintended target: stem-internal stressed *ī*n in
41794:   monosyllables (*swīn, *līn 'flax', *grīn 'snare', *wīn 'wine',
41795:   *swī*n itself...).
41796: 
```

#### Germanic/docs/DEV_NOTES.md:41821 (exact COUNTERPART)

- Nearby heading: ### B. Diagnosis: rule context too broad

```text
41819: exception:
41820: 
41821: * OE `swīn` (n.) — preserved
41822: * OE `līn` (n.) 'flax' — preserved
41823: * OE `wīn` (n.) 'wine' — preserved
```

#### Germanic/docs/DEV_NOTES.md:41851 (exact COUNTERPART)

- Nearby heading: ### C. Proposed Fix 3: restrict left context

```text
41849:   the rule as worded here is whether `*pylwin` reaches it with the
41850:   required left context. **This needs verification post-fix.**
41851: * Excludes monosyllabic `*swīn` (no preceding root + consonants
41852:   before the *ī*n; the *ī IS the root vowel) ✓
41853: 
```

#### Germanic/docs/DEV_NOTES.md:41861 (exact COUNTERPART)

- Nearby heading: ### D. Coverage-check shortlist

```text
41859: | Input | Expected | Reason |
41860: |---|---|---|
41861: | `*swīną` | `swīn` | Regression-recovery (a-stem n.sg.n.) |
41862: | `*pylwin` | `pyle` | Campbell §473 loanword case |
41863: | `*managīn` | `menige` | Brunner §280 / R/T 2 in-stem npl./obl. |
```

#### Germanic/docs/DEV_NOTES.md:42028 (exact PROTOFORM)

- Nearby heading: ### E. TSV migration (Phase 4)

```text
42026: | 5 | 2286, 2290, 2296 | hwīnan, wīf, wīþiġ |
42027: 
42028: Plus the seed migration of `*swīną → *swḯną` (id 1076, OE row 1194)
42029: in Phase 2 that originally cleared the regression.
42030: 
```

### Analysis and dossier hits

_None_

### Local lexical-table hits

#### old_english_wiktionary.tsv

| ENGLISH | OE_FORM | SOURCE | DETAIL | PAGE |
| :--- | :--- | :--- | :--- | :--- |
| swine | swīn | inh | template:inh | swine |

#### old_english_swadesh.tsv

_None_

## Possibly stale or diagnostic evidence

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:41257 (concept name)

- Nearby heading: ### F. Scope check on the proto-gate

```text
41255: * No other PROTOFORM in `Germanic/data/germanic-aligned-final.tsv`
41256:   ends in `*-īn` or contains medial `*-īn-`.
41257: * Search confirms `*swīną` (acc.sg. neut. n-stem 'swine') has *-n-ą
41258:   (with short *a) not *-īn, so is unaffected.
41259: 
```

#### Germanic/docs/DEV_NOTES.md:41771 (concept name)

- Nearby heading: ### A. Round 3 probe (post-Fix-1' application)

```text
41769: > `*swīną → swī (expected swīn)`
41770: 
41771: `*swīną` is a neuter a-stem 'swine' (root-stressed monosyllable).
41772: The cascade derives:
41773: 
```

### Analysis and dossier hits

_None_

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

## Paradigm probe

Philological note; no paradigm probe required for this row under the current classification. The note mentions paradigm forms, but it does not yet depend on a paradigm-cell solution.

