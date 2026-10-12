# Evidence packet — 2232 sunder / sundrian

> This packet is evidence for drafting. Do not treat all hits as equally authoritative; prefer high-confidence evidence.

## TSV row data

| ID | CONCEPT | COUNTERPART | PROTO | PROTOFORM | DERIVATION_CLASS | NOTE | HISTORY |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2232 | sunder | sundrian | *súndrōjaną | *súndrōjaną | regular | OE class II weak verb sundrian 'to sunder, separate' (cf. ā-sundrian; well attested BT, Hall). Direct reflex of PGmc *sundrōjaną (Orel *Handbook* pp. 386-7). Earlier target sundor- erroneously slotted the unrelated adverb sundor < PGmc *sunþraz (different lexeme: comparative *-ter- formation, cf. Goth sundro, ON sundr); cogset siblings (NL afzonderen, E sunder, G sondern) confirm a class-II verb reading. Corrected per §17.29. | Source: Wiktionary etymology (template:der) \| Source: Wiktionary etymology (template:der) |

## Manifest status

_No manifest entry._

## High-confidence evidence

### Compact derivation trace entry

```md
# sunder
PROTO: *súndrōjaną
EXPECTED: sundrian
OUTPUTS: sundrian



### Proto-Germanic consonant inheritance

Proto Input: *súndrōjaną

| Earlier Germanic developments | Old English developments |
|:---|:---|
| **Proto-West Germanic**<br>[no change]<br><br>**Northwest Germanic**<br>[no change] | **Old English**<br>OE Heavy Syllable Nasal Apocope: *súndrōjan<br>OE Secondary Nasalization: *súndrōjąn<br>OE I Umlaut: *súndrējąn<br>OE Unstressed Long Vowel Shortening: *súndrejąn<br>OE Weak Tail Reduction: *súndrejan<br>OE Intervocalic J Vocalization: *súndreian<br>OE Unstressed EI Contraction: *súndrian |



### Orthography & surface

Outcome: sundrian

NOTE: OE class II weak verb sundrian 'to sunder, separate' (cf. ā-sundrian; well attested BT, Hall). Direct reflex of PGmc *sundrōjaną (Orel *Handbook* pp. 386-7). Earlier target sundor- erroneously slotted the unrelated adverb sundor < PGmc *sunþraz (different lexeme: comparative *-ter- formation, cf. Goth sundro, ON sundr); cogset siblings (NL afzonderen, E sunder, G sondern) confirm a class-II verb reading. Corrected per §17.29.
```

### Matching oe_known_problems.tsv entries

_None_

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:37112 (row ID)

- Nearby heading: ### .1 Context

```text
37110: ### .1 Context
37111: 
37112: Mismatch-loop entry (post-§17.28). Row 2232:
37113: 
37114: | col | value |
```

#### Germanic/docs/DEV_NOTES.md:37167 (exact PROTOFORM)

- Nearby heading: ### .4 Why FST output `sundrian` is correct

```text
37165: ### .4 Why FST output `sundrian` is correct
37166: 
37167: `*súndrōjaną` is a class II weak verb infinitive. The FST chain:
37168: 
37169: - A-restoration: *u stays *u (no fronting before back ō)
```

#### Germanic/docs/DEV_NOTES.md:37196 (row ID)

- Nearby heading: ### .6 Proposed change

```text
37194: ### .6 Proposed change
37195: 
37196: Single TSV edit, row 2232:
37197: 
37198: | field | before | after |
```

#### Germanic/docs/DEV_NOTES.md:37207 (row ID)

- Nearby heading: ### .7 Predicted side-effects

```text
37205: ### .7 Predicted side-effects
37206: 
37207: - Row 2232 mismatch resolves: `sundrian == sundrian`. Mismatch count
37208:   25 → 24.
37209: - Bucket `cons_mismatch__n_vs_-__word_final` drops to 0.
```

#### Germanic/docs/DEV_NOTES.md:37215 (row ID)

- Nearby heading: ### .8 Verification plan

```text
37213: ### .8 Verification plan
37214: 
37215: 1. Edit row 2232 (COUNTERPART, NOTE).
37216: 2. `python3 Germanic/tools/oe_mismatch_report.py` → expect 25 → 24.
37217: 3. `python3 Germanic/tools/oe_known_problems_report.py` → tractable
```

### Analysis and dossier hits

_None_

## Supporting/background evidence

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:10423 (exact COUNTERPART)

- Nearby heading: ## Mismatch Progress Log (2026-03-14)

```text
10421: | 2026-04-26 | 23 | -1 | 1b9a44f1 | faran: TSV target færan → faran (§17.26) |
10422: | 2026-04-26 | 22 | -1 | 37031f31 | mare: TSV target mære → mare (§17.28) |
10423: | 2026-04-26 | 21 | -1 | 8bb2ecef | sundrian: target sundor- → sundrian (§17.29) |
10424: | 2026-04-26 | 20 | -1 | 871ec6ab | bēġen: TSV revert + monosyllable apocope guard (§17.30/31) |
10425: | 2026-04-26 | 19 | -1 | dc035fda | streċċan: OEVelarPalatalization *kk before *j (§17.34) |
```

#### Germanic/docs/DEV_NOTES.md:37116 (exact PROTOFORM)

- Nearby heading: ### .1 Context

```text
37114: | col | value |
37115: |---|---|
37116: | PROTOFORM | `*súndrōjaną` |
37117: | PROTO     | `*sundrōjaną` |
37118: | COUNTERPART | `sundor-` |
```

#### Germanic/docs/DEV_NOTES.md:37119 (exact COUNTERPART)

- Nearby heading: ### .1 Context

```text
37117: | PROTO     | `*sundrōjaną` |
37118: | COUNTERPART | `sundor-` |
37119: | FST output | `sundrian` |
37120: | Cogset | `sunder` (parallel rows: NL `afzonderen`, E `sunder`, G `sondern`) |
37121: | Bucket | `cons_mismatch__n_vs_-__word_final` |
```

#### Germanic/docs/DEV_NOTES.md:37138 (exact COUNTERPART)

- Nearby heading: ### .2 Three distinct PGmc lexemes (Orel, *Handbook of Germanic Etymology*

```text
37136:    **OE `syndrian`** 'to sunder, separate' (i-umlaut visible). T-F 444.
37137: 3. **`*sunþrōjanan` wk.vb. (cl.II, ō-suffix)** — ON `sundra` 'to break
37138:    asunder', **OE `sundrian`** 'to sunder, separate', MLG `sonderen`,
37139:    OHG `suntarōn`. T-F 444; H AEEW 330; KS 771.
37140: 
```

#### Germanic/docs/DEV_NOTES.md:37152 (exact COUNTERPART)

- Nearby heading: ### .3 What the cogset actually wants

```text
37150: 
37151: - NL `afzonderen` (cl.II weak)
37152: - E `sunder` (< OE `sundrian`/`āsundrian`)
37153: - G `sondern` (< OHG `suntarōn`)
37154: 
```

#### Germanic/docs/DEV_NOTES.md:37156 (exact COUNTERPART)

- Nearby heading: ### .3 What the cogset actually wants

```text
37154: 
37155: These all map cleanly to **lexeme #3, `*sunþrōjanan`**. The OE counterpart
37156: in the same cogset must therefore be `sundrian`, not the unrelated adverb
37157: `sundor` (lexeme #1).
37158: 
```

### Analysis and dossier hits

_None_

### Local lexical-table hits

#### old_english_wiktionary.tsv

| ENGLISH | OE_FORM | SOURCE | DETAIL | PAGE |
| :--- | :--- | :--- | :--- | :--- |
| sunder | sundor- | der | template:der | sunder |

#### old_english_swadesh.tsv

_None_

## Possibly stale or diagnostic evidence

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:37108 (exact pair)

- Nearby heading: ## §17.29 — *súndrōjaną → sundrian (target was `sundor-`, wrong lexeme)

```text
37106: 4. Commit + push.
37107: 
37108: ## §17.29 — *súndrōjaną → sundrian (target was `sundor-`, wrong lexeme)
37109: 
37110: ### .1 Context
```

#### Germanic/docs/DEV_NOTES.md:37120 (concept name)

- Nearby heading: ### .1 Context

```text
37118: | COUNTERPART | `sundor-` |
37119: | FST output | `sundrian` |
37120: | Cogset | `sunder` (parallel rows: NL `afzonderen`, E `sunder`, G `sondern`) |
37121: | Bucket | `cons_mismatch__n_vs_-__word_final` |
37122: 
```

#### Germanic/docs/DEV_NOTES.md:37132 (concept name)

- Nearby heading: ### .2 Three distinct PGmc lexemes (Orel, *Handbook of Germanic Etymology*

```text
37130: 
37131: 1. **`*sunþraz` adj./adv.** — Goth adv. `sundro`, ON `sundr`,
37132:    **OE `sundor`** 'alone, apart', OFris prep. `sunder`, OS `sundar`,
37133:    OHG `suntar` 'remote, separate'. Continues a comparative
37134:    *-ter- formation (cf. Skt sanutár-, Gk áter, W hanner).
```

#### Germanic/docs/DEV_NOTES.md:37136 (concept name)

- Nearby heading: ### .2 Three distinct PGmc lexemes (Orel, *Handbook of Germanic Etymology*

```text
37134:    *-ter- formation (cf. Skt sanutár-, Gk áter, W hanner).
37135: 2. **`*sunþrjanan` wk.vb. (cl.I, j-suffix)** — Swed `söndra`,
37136:    **OE `syndrian`** 'to sunder, separate' (i-umlaut visible). T-F 444.
37137: 3. **`*sunþrōjanan` wk.vb. (cl.II, ō-suffix)** — ON `sundra` 'to break
37138:    asunder', **OE `sundrian`** 'to sunder, separate', MLG `sonderen`,
```

#### Germanic/docs/DEV_NOTES.md:37148 (concept name)

- Nearby heading: ### .3 What the cogset actually wants

```text
37146: ### .3 What the cogset actually wants
37147: 
37148: The "sunder" cogset's other rows are unambiguously verbal class-II
37149: reflexes:
37150: 
```

### Analysis and dossier hits

_None_

## Bibliography-key candidates

### Preferred candidates

| Key | Why it was selected |
| :--- | :--- |
| Orel2003 | single available key for Orel |

### Low-confidence candidates

_None_

