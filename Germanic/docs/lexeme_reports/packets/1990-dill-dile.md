# Evidence packet — 1990 dill / dile

> This packet is evidence for drafting. Do not treat all hits as equally authoritative; prefer high-confidence evidence.

## TSV row data

| ID | CONCEPT | COUNTERPART | PROTO | PROTOFORM | DERIVATION_CLASS | NOTE | HISTORY |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1990 | dill | dile | *déljaz | *déliz | early_analogy | I-stem *deliz per Kroonen p.93: "evidence for both an i-stem (OE dile) and a ja-stem (OS dilli, OHG tilli)". OE generalized i-stem; OS/OHG generalized ja-stem. | See DEV_NOTES §dile. |

## Manifest status

_No manifest entry._

## High-confidence evidence

### Compact derivation trace entry

```md
# dill
PROTO: *déliz
EXPECTED: dile
OUTPUTS: dile



### Proto-Germanic consonant inheritance

Proto Input: *déliz

| Earlier Germanic developments | Old English developments |
|:---|:---|
| **Proto-West Germanic**<br>[no change]<br><br>**Northwest Germanic**<br>PGmc Final Z Deletion: *déli | **Old English**<br>OE I Umlaut: *dili<br>OE Med Unstressed I Lowering1: *dile |



### Orthography & surface

Outcome: dile

NOTE: I-stem *deliz per Kroonen p.93: "evidence for both an i-stem (OE dile) and a ja-stem (OS dilli, OHG tilli)". OE generalized i-stem; OS/OHG generalized ja-stem.
```

### Matching oe_known_problems.tsv entries

_None_

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:5848 (row ID)

- Nearby heading: ### The solution

```text
5846: **Option A (recommended): Update OE proto-form to i-stem**
5847: 
5848: Change row 1990 from `*deljăz` to `*deliz`.
5849: 
5850: - **Rationale:** OE `dile` is the regular i-stem outcome; OS/OHG `dilli/tilli` are ja-stem outcomes. Each daughter language generalized a different stem class.
```

#### Germanic/docs/DEV_NOTES.md:38488 (exact pair)

- Nearby heading: ### §17.36.5 Step 4 — fold IMarking1 into a direct *i → *e lowering

```text
38486: - All 12 sentinels stable.
38487: - Two formerly-passing forms used as extra checks:
38488:   `*déliz → dile`, `*máxtiz → miht` (both still produced).
38489: - Mismatch count: 20 → 20.
38490: 
```

### Analysis and dossier hits

_None_

## Supporting/background evidence

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:5809 (exact COUNTERPART)

- Nearby heading: ## OE dile 'dill': i-stem vs. ja-stem (2026-03-10)

```text
5807: ---
5808: 
5809: ## OE dile 'dill': i-stem vs. ja-stem (2026-03-10)
5810: 
5811: ### The problem
```

#### Germanic/docs/DEV_NOTES.md:5817 (exact COUNTERPART)

- Nearby heading: ### The problem

```text
5815: **Expected:** `dile` (with single -l-)
5816: 
5817: The mismatch arises because the TSV uses a **ja-stem** proto-form `*deljăz`, which triggers j-gemination (`*-lj- → *-ll-`), producing OE `dill`. But the attested OE form is `dile` with a single -l-, suggesting an **i-stem** input.
5818: 
5819: ### Kroonen's analysis
```

#### Germanic/docs/DEV_NOTES.md:5823 (exact COUNTERPART)

- Nearby heading: ### Kroonen's analysis

```text
5821: Kroonen (p.93, s.v. `*deli- ~ *delja-`) explicitly notes both stem classes:
5822: 
5823: > "The material offers evidence for both an **i-stem** (OE *dile*) and a **ja-stem** (OS *dilli*, OHG *tilli*). Perhaps the forms with rounded vowels (OE *dyle*, MHG *tülle*) can be adduced to reconstruct an additional ablauting pair `*duli- ~ *dulja-`. If so, the original paradigm probably had ablaut of the root, viz. nom. `*deliz`, gen. `*duljaz` < `*dhél-i-s`, `*dʰl̥-i-ós`."
5824: 
5825: **Key point:** Kroonen reconstructs:
```

#### Germanic/docs/DEV_NOTES.md:5829 (exact COUNTERPART)

- Nearby heading: ### Kroonen's analysis

```text
5827: - **Genitive (ja-stem with ablaut):** `*duljaz`
5828: 
5829: The OE form `dile` reflects the **nominative i-stem** `*deliz`, while OS `dilli`, OHG `tilli` reflect the **ja-stem** (generalized from oblique cases or with leveled root vowel).
5830: 
5831: ### Orel's analysis
```

### Analysis and dossier hits

#### Germanic/docs/analysis/dill_stem_class_investigation.md:7 (exact COUNTERPART)

- Nearby heading: ## Current TSV state

```text
6: - **PROTO**: `*deljăz` (all 4 rows)
7: - **OE target**: `dile`
8: - **Pipeline result**: `deljăz → dill` (wrong — expected `dile`)
```

#### Germanic/docs/analysis/dill_stem_class_investigation.md:8 (exact COUNTERPART)

- Nearby heading: ## Current TSV state

```text
7: - **OE target**: `dile`
8: - **Pipeline result**: `deljăz → dill` (wrong — expected `dile`)
9: - **Pipeline with i-stem**: `deliz → dile` ✓
```

#### Germanic/docs/analysis/dill_stem_class_investigation.md:9 (exact COUNTERPART)

- Nearby heading: ## Current TSV state

```text
8: - **Pipeline result**: `deljăz → dill` (wrong — expected `dile`)
9: - **Pipeline with i-stem**: `deliz → dile` ✓
10: 
```

### Local lexical-table hits

#### old_english_wiktionary.tsv

| ENGLISH | OE_FORM | SOURCE | DETAIL | PAGE |
| :--- | :--- | :--- | :--- | :--- |
| dill | dile | inh | template:inh | dill |

#### old_english_swadesh.tsv

_None_

## Possibly stale or diagnostic evidence

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:5813 (row ID)

- Nearby heading: ### The problem

```text
5811: ### The problem
5812: 
5813: **TSV row 1990:** `*deljăz → dile` (Old English)
5814: **FST output:** `*deljăz → dill` (with geminate -ll- from j-gemination)
5815: **Expected:** `dile` (with single -l-)
```

#### Germanic/docs/DEV_NOTES.md:5814 (concept name)

- Nearby heading: ### The problem

```text
5812: 
5813: **TSV row 1990:** `*deljăz → dile` (Old English)
5814: **FST output:** `*deljăz → dill` (with geminate -ll- from j-gemination)
5815: **Expected:** `dile` (with single -l-)
5816: 
```

#### Germanic/docs/DEV_NOTES.md:5815 (exact COUNTERPART)

- Nearby heading: ### The problem

```text
5813: **TSV row 1990:** `*deljăz → dile` (Old English)
5814: **FST output:** `*deljăz → dill` (with geminate -ll- from j-gemination)
5815: **Expected:** `dile` (with single -l-)
5816: 
5817: The mismatch arises because the TSV uses a **ja-stem** proto-form `*deljăz`, which triggers j-gemination (`*-lj- → *-ll-`), producing OE `dill`. But the attested OE form is `dile` with a single -l-, suggesting an **i-stem** input.
```

#### Germanic/docs/DEV_NOTES.md:5839 (concept name)

- Nearby heading: ### Cognate distribution by stem class

```text
5837: | Language | Form | Stem class | Expected from i-stem `*deliz` | Expected from ja-stem `*deljăz` |
5838: |----------|------|------------|------------------------------|--------------------------------|
5839: | **Old English** | `dile` | i-stem ✓ | `*deliz → dile` ✓ | `*deljăz → dill` ✗ |
5840: | **Old Saxon** | `dilli` | ja-stem | — | `*deljăz → dilli` ✓ |
5841: | **Old High German** | `tilli` | ja-stem | — | `*deljăz → tilli` ✓ |
```

#### Germanic/docs/DEV_NOTES.md:5866 (concept name)

- Nearby heading: ### Recommendation

```text
5864: 
5865: 1. **Kroonen explicitly reconstructs `*deliz` as the i-stem nominative** — this is not speculation but standard reconstruction.
5866: 2. **The OE form `dile` (single -l-) is incompatible with j-gemination** — if it were from `*deljăz`, we would expect `*dill`.
5867: 3. **The principle of paradigm-cell matching applies**: use the proto-form that produces the attested outcome for each daughter language.
5868: 4. **The OS/OHG rows can keep `*deljăz`** since their geminate forms `dilli/tilli` are ja-stem outcomes.
```

#### Germanic/docs/DEV_NOTES.md:5879 (concept name)

- Nearby heading: ### What each source says (exhaustive survey)

```text
5877: Kroonen reconstructs **both stems** and explicitly derives OE `dile` from i-stem `*deliz`.
5878: 
5879: **Kluge-Seebold (2011), s.v. *Dill*:**
5880: > "Aus wg. `*delja-` m. 'Dill', auch in ae. *dile*, nschw. *dill*. Daneben ae. *dyle* (selten), nndl. *dulle*, mhd. *tüll(e)*, nnorw. *dylla*. Am ehesten zu Dolde..."
5881: 
```

#### Germanic/docs/DEV_NOTES.md:5916 (row ID)

- Nearby heading: ### Implementation (2026-04-06)

```text
5914: ### Implementation (2026-04-06)
5915: 
5916: **Option A implemented:** Changed TSV row 1990 from `*deljăz` to `*deliz`.
5917: 
5918: Test: `echo "deliz" | flookup -i old_english.bin` → `dile` ✓
```

#### Germanic/docs/DEV_NOTES.md:38518 (exact pair)

- Nearby heading: ### §17.36.6 Step 5 — remove dead *ĭ machinery (cosmetic cleanup)

```text
38516: 
38517: Verification:
38518: - All 14 sentinels (12 standard + `*déliz → dile`, `*máxtiz → miht`)
38519:   still produce expected forms.
38520: - Mismatch count: 20 → 20.
```

### Analysis and dossier hits

_None_

## Bibliography-key candidates

### Preferred candidates

| Key | Why it was selected |
| :--- | :--- |
| Kroonen2013 | default Proto-Germanic etymology key for Kroonen |
| Orel2003 | single available key for Orel |

### Low-confidence candidates

| Key | Why it was selected |
| :--- | :--- |
| Kroonen2011 | surname mention only: Kroonen |
| Kroonen2006 | surname mention only: Kroonen |

