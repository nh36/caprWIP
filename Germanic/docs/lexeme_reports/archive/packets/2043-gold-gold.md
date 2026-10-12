# Evidence packet — 2043 gold / gold

> This packet is evidence for drafting. Do not treat all hits as equally authoritative; prefer high-confidence evidence.

## TSV row data

| ID | CONCEPT | COUNTERPART | PROTO | PROTOFORM | DERIVATION_CLASS | NOTE | HISTORY |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2043 | gold | gold | *gúlθą | *gúlθą | regular | R/T §5.1.3 p.171: *gulθa-/*gulda- may reflect Verner's alternation or regular PWGmc *lθ→*ld; either gives OE gold | - |

## Manifest status

_No manifest entry._

## High-confidence evidence

### Compact derivation trace entry

```md
# gold
PROTO: *gúlθą
EXPECTED: gold
OUTPUTS: gold



### Proto-Germanic consonant inheritance

Proto Input: *gúlθą

| Earlier Germanic developments | Old English developments |
|:---|:---|
| **Proto-West Germanic**<br>PWGmc L Th Voicing: *gúldą<br><br>**Northwest Germanic**<br>NWGmc U Lowering: *góldą | **Old English**<br>OE Heavy Syllable Nasal Apocope: *góld |



### Orthography & surface

Outcome: gold

NOTE: R/T §5.1.3 p.171: *gulθa-/gulda- may reflect Verner's alternation or regular PWGmc *lθ→ld; either gives OE gold
```

### Matching oe_known_problems.tsv entries

_None_

### DEV_NOTES hits

_None_

### Analysis and dossier hits

_None_

## Supporting/background evidence

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:59 (exact COUNTERPART)

- Nearby heading: ### Companion documents

```text
57: - `docs/analysis/notable_findings.md` — Cross-referenced scholarly discussion (§§1–7)
58: - `server/fsts/germanic.txt` — FST source
59: - `server/data/germanic-aligned-final.tsv` — Gold standard data
60: 
61: ---
```

#### Germanic/docs/DEV_NOTES.md:1337 (exact COUNTERPART)

- Nearby heading: ### Ambiguous examples (rule OR Verner's Law)

```text
1335: R/T explicitly notes that two words might reflect Verner's Law alternation
1336: `*þ ~ *d` rather than (or in addition to) the `*lþ → *ld` rule:
1337: - `*gulþa- ~ *gulda-` → OE gold ('gold') — R/T §5.1.3 p.171
1338: - `*felþu- ~ *feldu-` → OE feld ('field') — R/T §5.1.3 p.171
1339: 
```

#### Germanic/docs/DEV_NOTES.md:1354 (exact COUNTERPART)

- Nearby heading: ### Scope of Verner's Law in the project

```text
1352: mechanism. The current approach is case-by-case:
1353: - Where the regular sound change (`*lþ → ld`) gives the right answer, we
1354:   use it (gold, feld, fealdan, etc.)
1355: - Where only Verner's alternation explains the outcome (nǣdl), the item
1356:   remains a known mismatch until we decide on a systematic approach
```

#### Germanic/docs/DEV_NOTES.md:2342 (exact COUNTERPART)

- Nearby heading: ### English gold IPA normalized to RP / non-rhotic baseline

```text
2340: ## 2025-12-12
2341: 
2342: ### English gold IPA normalized to RP / non-rhotic baseline
2343: 
2344: - Cleaned every English row in `server/data/germanic-aligned-final.tsv` whose counterpart contains an orthographic `r` but whose surface tokens still ended in a vowel + `r`. Each of the 40 affected entries now drops the trailing `r` (e.g. `adder ædər→ædə`, `fire faɪər→faɪə`, `door dɔːr→dɔː`). Mirrored the same edits into the staged snapshot (`server/pipeline/output/germanic/stage3/germanic-aligned-final.tsv`) so downstream docs stay in sync.
```

#### Germanic/docs/DEV_NOTES.md:2345 (exact COUNTERPART)

- Nearby heading: ### English gold IPA normalized to RP / non-rhotic baseline

```text
2343: 
2344: - Cleaned every English row in `server/data/germanic-aligned-final.tsv` whose counterpart contains an orthographic `r` but whose surface tokens still ended in a vowel + `r`. Each of the 40 affected entries now drops the trailing `r` (e.g. `adder ædər→ædə`, `fire faɪər→faɪə`, `door dɔːr→dɔː`). Mirrored the same edits into the staged snapshot (`server/pipeline/output/germanic/stage3/germanic-aligned-final.tsv`) so downstream docs stay in sync.
2345: - Added `server/tools/validate_english_rhoticity.py` to guard the policy going forward. The helper scans any TSV for English rows where the tokens end in `…V r` and fails fast; CI/local runs should call `python3 server/tools/validate_english_rhoticity.py` (optionally pointing it at the stage3 export) whenever the gold data changes.
2346: - Reran the validator on both the canonical and stage3 TSVs — both now report “No rhotic entries detected.” Next time the gold file is touched, run the validator before committing so we don’t regress toward GA-style outputs again. Once the analyzer tweaks land, rerun `python3 server/tools/english_apply_down_stats.py` to confirm the RP-aware surfaces align with the updated targets.
2347: 
```

#### Germanic/docs/DEV_NOTES.md:2346 (exact COUNTERPART)

- Nearby heading: ### English gold IPA normalized to RP / non-rhotic baseline

```text
2344: - Cleaned every English row in `server/data/germanic-aligned-final.tsv` whose counterpart contains an orthographic `r` but whose surface tokens still ended in a vowel + `r`. Each of the 40 affected entries now drops the trailing `r` (e.g. `adder ædər→ædə`, `fire faɪər→faɪə`, `door dɔːr→dɔː`). Mirrored the same edits into the staged snapshot (`server/pipeline/output/germanic/stage3/germanic-aligned-final.tsv`) so downstream docs stay in sync.
2345: - Added `server/tools/validate_english_rhoticity.py` to guard the policy going forward. The helper scans any TSV for English rows where the tokens end in `…V r` and fails fast; CI/local runs should call `python3 server/tools/validate_english_rhoticity.py` (optionally pointing it at the stage3 export) whenever the gold data changes.
2346: - Reran the validator on both the canonical and stage3 TSVs — both now report “No rhotic entries detected.” Next time the gold file is touched, run the validator before committing so we don’t regress toward GA-style outputs again. Once the analyzer tweaks land, rerun `python3 server/tools/english_apply_down_stats.py` to confirm the RP-aware surfaces align with the updated targets.
2347: 
2348: ### Rhotic development roadmap (historical targets before coding)
```

### Analysis and dossier hits

#### Germanic/docs/analysis/four_complex_tsv_items.md:97 (exact COUNTERPART)

- Nearby heading: ### Proto-form assessment

```text
96: 
97: > Go. skilliggs m. 'solidus', ON skillingr, OE scilling, OHG scilling 'aureus (a gold
98: > coin)' as continuing \*skeld-linga- (Schröder 1918: 254ff).
```

#### Germanic/docs/analysis/notable_findings.md:366 (exact COUNTERPART)

- Nearby heading: ## 2. NWGmc u-lowering exceptions near labials: a non-Neogrammarian pattern

```text
365: vowel system: "u > o before mid and low vowels. In OE forms this change
366: occurs with considerable regularity, e.g. dohtor daughter, god god, gold
367: gold, geoc yoke, and passive participles of strong verbs of Classes II,
```

#### Germanic/docs/analysis/notable_findings.md:367 (exact COUNTERPART)

- Nearby heading: ## 2. NWGmc u-lowering exceptions near labials: a non-Neogrammarian pattern

```text
366: occurs with considerable regularity, e.g. dohtor daughter, god god, gold
367: gold, geoc yoke, and passive participles of strong verbs of Classes II,
368: III, and IV, e.g. coren, boren, holpen." But he immediately notes the
```

### Local lexical-table hits

#### old_english_wiktionary.tsv

| ENGLISH | OE_FORM | SOURCE | DETAIL | PAGE |
| :--- | :--- | :--- | :--- | :--- |
| gold | gold | inh | template:inh | gold |

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

