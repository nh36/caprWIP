# Evidence packet — 2251 thorn / þorn

> This packet is evidence for drafting. Do not treat all hits as equally authoritative; prefer high-confidence evidence.

## TSV row data

| ID | CONCEPT | COUNTERPART | PROTO | PROTOFORM | DERIVATION_CLASS | NOTE | HISTORY |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2251 | thorn | þorn | *θúrnaz | *θúrnaz | regular | Adopt *θurnăz (m. a-stem; Kroonen *θurna-). A u-stem reformation *θurnuz is reflected in Gothic þaurnus (u-stem), and Old Norse also shows an ija-stem variant þyrnir 'thorn' (alongside þorn). | - |

## Manifest status

_No manifest entry._

## High-confidence evidence

### Compact derivation trace entry

```md
# thorn
PROTO: *θúrnaz
EXPECTED: þorn
OUTPUTS: þorn



### Proto-Germanic consonant inheritance

Proto Input: *θúrnaz

| Earlier Germanic developments | Old English developments |
|:---|:---|
| **Proto-West Germanic**<br>[no change]<br><br>**Northwest Germanic**<br>NWGmc U Lowering: *θórnaz<br>PGmc Final Z Deletion: *θórna | **Old English**<br>PWGmc Final Bare A Loss: *θórn |



### Orthography & surface

Old English Orthography: þ*órn
Outcome: þorn

NOTE: Adopt *θurnăz (m. a-stem; Kroonen *θurna-). A u-stem reformation *θurnuz is reflected in Gothic þaurnus (u-stem), and Old Norse also shows an ija-stem variant þyrnir 'thorn' (alongside þorn).
```

### Matching oe_known_problems.tsv entries

_None_

### DEV_NOTES hits

_None_

### Analysis and dossier hits

_None_

## Supporting/background evidence

### DEV_NOTES hits

_None_

### Analysis and dossier hits

_None_

### Local lexical-table hits

#### old_english_wiktionary.tsv

| ENGLISH | OE_FORM | SOURCE | DETAIL | PAGE |
| :--- | :--- | :--- | :--- | :--- |
| thorn | þorn | inh | template:inh | thorn |

#### old_english_swadesh.tsv

_None_

## Possibly stale or diagnostic evidence

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:90 (concept name)

- Nearby heading: ### Could we use paradigm forms? (Why we decided not to)

```text
88: ### Could we use paradigm forms? (Why we decided not to)
89: 
90: For other problematic items (fire, brand, berry, thorn), we successfully resolved mismatches by adopting a paradigm form in which the phonological development is lautgesetzlich. The question is whether the same approach works for the u-lowering exceptions.
91: 
92: **Approach A: Use a u-stem or root-noun form.**
```

#### Germanic/docs/DEV_NOTES.md:2944 (concept name)

- Nearby heading: #### 3. θ/þ encoding convention

```text
2942: #### 3. θ/þ encoding convention
2943: 
2944: The FST uses θ (Greek theta, U+03B8) for the voiceless dental fricative in proto-forms. The original test rows incorrectly used þ (thorn, U+00FE) in the PROTO column. The mismatch report's `normalize_proto()` converts þ→θ, masking this issue.
2945: 
2946: **Convention:** PROTO column in TSV must use θ, matching existing entries like `*baθą`.
```

#### Germanic/docs/DEV_NOTES.md:8304 (concept name)

- Nearby heading: ### Root Cause: θ/þ Inconsistency

```text
8302: The grammar (`pgrmWord`) uses TWO different characters for the dental fricative:
8303: - **θ (Greek theta, U+03B8)**: Used in 12 input patterns
8304: - **þ (Latin thorn, U+00FE)**: Used in only 2 input patterns
8305: 
8306: These map to DIFFERENT internal symbols:
```

#### Germanic/docs/DEV_NOTES.md:8314 (concept name)

- Nearby heading: ### Root Cause: θ/þ Inconsistency

```text
8312: **Critical mismatch for `*libēθi`:**
8313: - TSV row 2107 has: `*libēθi` (theta)
8314: - Grammar line 344 has: `ē:{*ē} þ:{*þ} i:{*i}` (thorn!)
8315: - Result: The input `ēθi` doesn't match the pattern `ēþi`, so no parse
8316: 
```

#### Germanic/docs/DEV_NOTES.md:8325 (concept name)

- Nearby heading: ### Investigation: Which Character Should We Use?

```text
8323: - Con: Confusing since OE uses þ orthographically
8324: 
8325: **Option B: Standardize on þ (thorn)**
8326: - Pro: Matches OE orthographic convention
8327: - Pro: More intuitive for Germanic linguists
```

#### Germanic/docs/DEV_NOTES.md:8352 (concept name)

- Nearby heading: ### Sources

```text
8350: 
8351: - Unicode Standard: θ = U+03B8 (Greek Small Letter Theta)
8352: - Unicode Standard: þ = U+00FE (Latin Small Letter Thorn)
8353: 
8354: ### Implementation (2026-03-13)
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

