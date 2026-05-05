# Evidence packet — 2069 hedge / heġġ

> This packet is evidence for drafting. Do not treat all hits as equally authoritative; prefer high-confidence evidence.

## TSV row data

| ID | CONCEPT | COUNTERPART | PROTO | PROTOFORM | DERIVATION_CLASS | NOTE | HISTORY |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2069 | hedge | heġġ | *xágjaz | *xágjaz | regular | Note: heċġ is the more standard spelling; using heġġ here | Source: Wiktionary etymology (template:inh) \| Source: Wiktionary etymology (template:inh) |

## Manifest status

_No manifest entry._

## High-confidence evidence

### Compact derivation trace entry

```md
# hedge
PROTO: *xágjaz
EXPECTED: heġġ
OUTPUTS: heġġ



### Proto-Germanic consonant inheritance

Proto Input: *xágjaz

| Earlier Germanic developments | Old English developments |
|:---|:---|
| **Proto-West Germanic**<br>PWGmc J Gemination: *xággjaz<br><br>**Northwest Germanic**<br>PGmc Final Z Deletion: *xággja | **Old English**<br>PWGmc Final Bare A Loss: *xággj<br>Anglo Frisian Brightening: *xæggj<br>OE Velar Fricative Palatalization: *çæggj<br>OE Velar Palatalization: *çæʤʤj<br>OE I Umlaut: *çeʤʤj<br>OE J Loss After Heavy: *çeʤʤ |



### Orthography & surface

Old English Orthography: h*eġġ
Outcome: heġġ

NOTE: Note: heċġ is the more standard spelling; using heġġ here
```

### Matching oe_known_problems.tsv entries

_None_

### DEV_NOTES hits

_None_

### Analysis and dossier hits

_None_

## Supporting/background evidence

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:1728 (exact COUNTERPART)

- Nearby heading: ## A-Restoration Fix (2026-02-06)

```text
1726: - Hedge (2026-01-20):
1727:   - Reverted the orthographic `{ʤj} -> {ċġ}` mapping and removed `{ċġ}` from `OldEnglishSurfaceConsonant` (OE output should stay `ġġ`).
1728:   - Data update: `server/data/germanic-aligned-final.tsv` (OE heċġ → heġġ) with NOTE that **heċġ is the more standard spelling**; Wiktionary TSV left unchanged.
1729:   - As of 2026-01-22g, output is **heġġ** (matches expected); see `docs/debug_snapshots/oe_mismatch_report_2026-01-22g.txt` and `docs/debug_snapshots/oe_full_trace_report_2026-01-22g.txt`.
1730: - Knob (2026-01-22):
```

#### Germanic/docs/DEV_NOTES.md:1729 (exact COUNTERPART)

- Nearby heading: ## A-Restoration Fix (2026-02-06)

```text
1727:   - Reverted the orthographic `{ʤj} -> {ċġ}` mapping and removed `{ċġ}` from `OldEnglishSurfaceConsonant` (OE output should stay `ġġ`).
1728:   - Data update: `server/data/germanic-aligned-final.tsv` (OE heċġ → heġġ) with NOTE that **heċġ is the more standard spelling**; Wiktionary TSV left unchanged.
1729:   - As of 2026-01-22g, output is **heġġ** (matches expected); see `docs/debug_snapshots/oe_mismatch_report_2026-01-22g.txt` and `docs/debug_snapshots/oe_full_trace_report_2026-01-22g.txt`.
1730: - Knob (2026-01-22):
1731:   - **Unattested in Old English**; first attested in Middle English (Chaucer): “The knobbes sittynge on his chekes.”
```

#### Germanic/docs/DEV_NOTES.md:1753 (exact COUNTERPART)

- Nearby heading: ## A-Restoration Fix (2026-02-06)

```text
1751:   - Standard descriptions show WGmc **gemination before *j** in short stems and **i‑mutation following *i/*j**, with classic paths like *satjan > *sattjan > *sættjan > *settian > OE settan; palatalization of velars by *j precedes i‑mutation in the usual OE chronology. Sources: Hasenfratz appendices (WVU “Reading Old English”) and the OE phonological history summary citing Campbell.
1752:   - Implementation aligned to this: allow **palatalized consonants** (ʤ/ʧ/ʃ/ç/ʒ/j) to count as intervening segments for i‑umlaut so raising can apply **after palatalization** rather than being blocked by non‑star symbols.
1753:   - Result: *xagjăz → **heġġ** and *sangjăną → **senġan** in `oe_full_trace_report_2026-01-22g.txt`; *baugjăną still mispredicts `bīeġan` (see final_vowel_missing bucket).
1754: - OE epenthesis update (2026-01-04):
1755:   - Epenthesis is now a real phonological stage **before** star removal and appears in the full trace.
```

#### Germanic/docs/DEV_NOTES.md:3074 (exact COUNTERPART)

- Nearby heading: ### Implementation

```text
3072: 
3073: All three steps restricted to medial (non-initial) position to prevent regressions
3074: on stressed-syllable forms (e.g. \*xagjăz → heġġ, which should keep stressed \*e).
3075: 
3076: ---
```

### Analysis and dossier hits

_None_

### Local lexical-table hits

#### old_english_wiktionary.tsv

| ENGLISH | OE_FORM | SOURCE | DETAIL | PAGE |
| :--- | :--- | :--- | :--- | :--- |
| hedge | heċġ | inh | template:inh | hedge |

#### old_english_swadesh.tsv

_None_

## Possibly stale or diagnostic evidence

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:1726 (concept name)

- Nearby heading: ## A-Restoration Fix (2026-02-06)

```text
1724:   2. Add `a/æ + w` breaking plus explicit **u‑breaking** rules to `EnglishBreakingLengthening`, then regenerate.
1725:   3. Deep dive `palatalization_missing` (e.g., *bōkō) to confirm whether the rule/chronology or the expected form is wrong.
1726: - Hedge (2026-01-20):
1727:   - Reverted the orthographic `{ʤj} -> {ċġ}` mapping and removed `{ċġ}` from `OldEnglishSurfaceConsonant` (OE output should stay `ġġ`).
1728:   - Data update: `server/data/germanic-aligned-final.tsv` (OE heċġ → heġġ) with NOTE that **heċġ is the more standard spelling**; Wiktionary TSV left unchanged.
```

#### Germanic/docs/DEV_NOTES.md:2637 (concept name)

- Nearby heading: ### OE orthography cleanup + reports (2026-01-18)

```text
2635:   - `server/docs/debug_snapshots/oe_full_trace_report_2026-01-18w.txt`
2636: - **Totals (2026-01-18w):** total mismatches 294; `palatal_marker_variant` = 0; `gemination_extra` = 2.
2637: - **Hedge trace:** `oe_full_trace_report_2026-01-18w.txt` shows `hedge` outputs **both** `hæġġ` and `hæċġ` (Orthography + Surface), indicating nondeterminism is still present.
2638: - **Open issue:** need deterministic pre-orthography cleanup so `*dʒ` + `*j` (and `dʒ` + `j`) coalesce to `{ʤj}` before orthography; avoid producing both `ħeġġ`/`hæġġ` and `hæċġ`.
2639: - **Operational note:** Docker socket permissions intermittently blocked `docker compose exec` in this session; reports were rerun only after restoring Docker access.
```

#### Germanic/docs/DEV_NOTES.md:2645 (concept name)

- Nearby heading: ### Foma CLI gotchas (2026-01-18)

```text
2643: - **Reliable one-off tests:** use `foma` with stdin to avoid interactive issues, e.g.
2644:   - `printf 'regex {ʤ} {*j} -> {ʤj};\napply down "ç*æʤ*j"\nquit\n' | foma`
2645:   - Output: `"ç*æʤj"` (confirms the merge rule works on the hedge pre‑orthography form).
2646: 
2647: ### HIGH PRIORITY: PGmc final *-un behavior (2026-01-25)
```

#### Germanic/docs/DEV_NOTES.md:31365 (concept name)

- Nearby heading: ##### §17.19.10.2.f Camp 1 vs Camp 2 adjudication

```text
31363: | Camp 2 (epenthetic *u) | EWA s.v. *apful* (line 6048); Brunner §152, §154; Schatz §98 | PIE *h₃nobʰ-l-on- > PGmc *nablan-; *u inserted later as Sproßvokal | Better cognate-internal (Lat./OIr. show inherited vowel; Skt. has none); aligns with the *aplu, *fuglaz pattern |
31364: | Camp 2′ (Kroonen 2013) | Kroonen *nablan-, *fuglaz | Same as Camp 2, but Kroonen uses bare-cluster headwords as a **lemmatisation convention**, not necessarily as a sound-historical claim | Conservative; agnostic on chronology |
31365: | Hedge (Orel 2003) | *nab(u)lōn- | Refuses to commit | Honest about the disagreement |
31366: 
31367: **My adjudication:** the *u must be present *somewhere* between PGmc
```

#### Germanic/docs/DEV_NOTES.md:31394 (concept name)

- Nearby heading: ##### §17.19.10.2.f Camp 1 vs Camp 2 adjudication

```text
31392: **morphological** form is *nablan-) and R/T's derivational input
31393: (the **phonological** form at the moment OE A-restoration applies is
31394: *nabulō with *u). It also matches Orel's deliberate hedge.
31395: 
31396: ---
```

#### Germanic/docs/DEV_NOTES.md:31439 (concept name)

- Nearby heading: ##### §17.19.10.3.b OHG nabalo / nabulo: doublet

```text
31437: OHG *nabalo, nabulo* with the comment (line 64938): "Aus g.
31438: **\*nab(u)lōn** m. 'Nabel'" — i.e. Kluge-Seebold also adopt Orel's
31439: parenthesised hedge.
31440: 
31441: The OHG *-a-* form *nabalo* is best read as the result of medial
```

### Analysis and dossier hits

_None_

## Bibliography-key candidates

### Preferred candidates

| Key | Why it was selected |
| :--- | :--- |
| KnobEmail2026 | author + year mention (Knob 2026) |
| Campbell1959 | single available key for Campbell |

### Low-confidence candidates

_None_

