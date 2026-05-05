# Evidence packet — 2235 swan / swanes

> This packet is evidence for drafting. Do not treat all hits as equally authoritative; prefer high-confidence evidence.

## TSV row data

| ID | CONCEPT | COUNTERPART | PROTO | PROTOFORM | DERIVATION_CLASS | NOTE | HISTORY |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2235 | swan | swanes | *swánaz | *swánas | early_analogy | - | Source: Wiktionary etymology (template:inh) \| Source: Wiktionary etymology (template:inh) |

## Manifest status

_No manifest entry._

## High-confidence evidence

### Compact derivation trace entry

```md
# swan
PROTO: *swánas
EXPECTED: swanes
OUTPUTS: swanes



### Proto-Germanic consonant inheritance

Proto Input: *swánas

| Earlier Germanic developments | Old English developments |
|:---|:---|
| **Proto-West Germanic**<br>[no change]<br><br>**Northwest Germanic**<br>[no change] | **Old English**<br>Anglo Frisian Brightening: *swánæs<br>OE Unstressed AE Merger: *swánes |



### Orthography & surface

Outcome: swanes
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
| swan | swan | inh | template:inh | swan |

#### old_english_swadesh.tsv

_None_

## Possibly stale or diagnostic evidence

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:2539 (concept name)

- Nearby heading: ### OE weak‑tail nasal vowel loss (PGmc *‑aną → OE ‑an) (2025-12-21)

```text
2537:   - `docs/debug_snapshots/oe_tracer_log_2025-12-21j.txt` (OE sandbox tracer).
2538: - `docs/debug_snapshots/oe_tail_bucket_2025-12-21j.txt` + `oe_tail_bucket_classified_2025-12-21j.txt` (tail bucket after nasal‑vowel loss).
2539: - Note: the tail bucket still contains `swan` (`*swanăz → sʋana`), which is not from `*‑aną`; flag for later review of `*‑ăz` handling.
2540: 
2541: ### OE diagnostics follow‑up: orthography + rhotacism (2025-12-22)
```

#### Germanic/docs/DEV_NOTES.md:3216 (concept name)

- Nearby heading: ### Case 1: *rastō → rast (expected ræst) — ō-stem feminine

```text
3214: Tested: `rastas → ræstes` ✓ (the gen.sg. form with correct ræ- root).
3215: 
3216: **Decision needed:** We could (a) use gen.sg. *rastas → OE ræstes, changing both the proto and the OE target (parallel to hammer, swan, brand); or (b) document ræst as a known morphological exception with an ALIGNMENT note that the pipeline gives the regular nom.sg. reflex rast but the standard form ræst reflects paradigmatic leveling.
3217: 
3218: **Complication with (a):** The encoding *rastas uses the a-stem gen.sg. ending *-as, but *rastō is an ō-stem, whose gen.sg. is *-ōz (→ PWGmc *-a → OE -e). The pipeline cannot process *-ōz because it is not in the pgrmWeakTailVowel list, and even if added, the *-ō component would trigger A-restoration. Using *-as is thus a pragmatic encoding that gives the correct phonological result but misrepresents the morphological class.
```

### Analysis and dossier hits

_None_

## Bibliography-key candidates

### Preferred candidates

_None_

### Low-confidence candidates

_None_

