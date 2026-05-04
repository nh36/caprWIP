# Evidence packet — 1965 brand / brandes

> This packet is evidence for drafting. Do not treat all hits as equally authoritative; prefer high-confidence evidence.

## TSV row data

| ID | CONCEPT | COUNTERPART | PROTO | PROTOFORM | DERIVATION_CLASS | NOTE | HISTORY |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1965 | brand | brandes | *brándaz | *brándas | early_analogy | - | Source: Wiktionary etymology (template:inh) \| Source: Wiktionary etymology (template:inh) |

## Manifest status

_No manifest entry._

## High-confidence evidence

### Compact derivation trace entry

```md
# brand
PROTO: *brándas
EXPECTED: brandes
OUTPUTS: brandes



### Proto-Germanic consonant inheritance

Proto Input: *brándas

| Earlier Germanic developments | Old English developments |
|:---|:---|
| **Proto-West Germanic**<br>[no change]<br><br>**Northwest Germanic**<br>[no change] | **Old English**<br>Anglo Frisian Brightening: *brándæs<br>OE Unstressed AE Merger: *brándes |



### Orthography & surface

Outcome: brandes
```

### Matching oe_known_problems.tsv entries

_None_

### DEV_NOTES hits

_None_

### Analysis and dossier hits

_None_

## Supporting/background evidence

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:5028 (exact COUNTERPART)

- Nearby heading: # Restricted to *st cluster to avoid overapplication

```text
5026: | Input | → | Output | Gloss |
5027: |-------|---|--------|-------|
5028: | \*brandaz | → | *brandes* (gen.sg.) | 'brand' ✓ (no metathesis) |
5029: | \*bringanan | → | *bringan* | 'to bring' ✓ (no metathesis) |
5030: 
```

### Analysis and dossier hits

_None_

### Local lexical-table hits

#### old_english_wiktionary.tsv

| ENGLISH | OE_FORM | SOURCE | DETAIL | PAGE |
| :--- | :--- | :--- | :--- | :--- |
| brand | brand | inh | template:inh | brand |

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

#### Germanic/docs/DEV_NOTES.md:1789 (concept name)

- Nearby heading: ### English sandbox todo — surface accuracy focus

```text
1787: ### English sandbox todo — surface accuracy focus
1788: 
1789: - ~~**Finish weak-tail deletions.** Extend `EnglishSandboxWeakTailReductions` (or add a follow-up cleanup stage) so reduced `{*a/ą}` tails drop the following `n/m/r` and final schwa in stressed monosyllables. This will convert forms like `beɪkeɪnə/bænnə/brændə/blʌdə` into the expected `bake/ban/brand/blood` without manual patches.~~
1790:   - ✅ 2025-12-11: `{*ă}` now flows through `EnglishSandboxWeakTailReductions → EnglishSandboxWeakTailCleanup → EnglishSandboxWeakTailFinalDrop`; `EnglishSandboxNoFinalWeakTail` filters out residual `{*r/n/m}`+`{*ə}`. Tracer (`*bakăną/*bannăn/*brandăz/*blōdą`) shows single surfaces (`beɪk/bæn/brænd/blʌd`), and `tools/english_apply_down_stats.py` reports 333/376 single-output entries (multiple outputs = 0).
1791: - **Back/round proto rhotics earlier.** Expand `EnglishSandboxProtoRhoticFronting` to push `{*e, *i, *o}` toward `{æ, ɪ, ɔ}` before `{*r}` so `*bergą/*bardăz/*barwōn/*burdiz` feed the ME vowel system with the right backness, unlocking `barrow/beard/bier/birth` reflexes.
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

#### Germanic/docs/DEV_NOTES.md:38130 (concept name)

- Nearby heading: ### §17.35.3 The bigger issue — *-ingaz is missing from pgrmWeakTailVowel

```text
38128: 
38129: By contrast, the *-az* nom.sg. ending alone is fine: `*brándaz` →
38130: `brand`, `*xáubidą` → `hēafod`, `*kuningan-` if it had been entered
38131: without the *-ing-* suffix would also work. Even the present row's
38132: `*skéllinaz` works because `-inaz` is in the grammar.
```

### Analysis and dossier hits

_None_

## Bibliography-key candidates

### Preferred candidates

_None_

### Low-confidence candidates

_None_

