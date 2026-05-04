# Evidence packet — 2087 knob / cnobba

> This packet is evidence for drafting. Do not treat all hits as equally authoritative; prefer high-confidence evidence.

## TSV row data

| ID | CONCEPT | COUNTERPART | PROTO | PROTOFORM | DERIVATION_CLASS | NOTE | HISTORY |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2087 | knob | cnobba | *knúppaz | *knúbbô | reconstructed_oe | Unattested Old English cognate; likely *cnobba based on ME knob (Chaucer) and Frisian knobbe. | - |

## Manifest status

_No manifest entry._

## High-confidence evidence

### Compact derivation trace entry

```md
# knob
PROTO: *knúbbô
EXPECTED: cnobba
OUTPUTS: cnobba



### Proto-Germanic consonant inheritance

Proto Input: *knúbbô

| Earlier Germanic developments | Old English developments |
|:---|:---|
| **Proto-West Germanic**<br>[no change]<br><br>**Northwest Germanic**<br>NWGmc U Lowering: *knóbbô | **Old English**<br>OE Unstressed Long Vowel Shortening: *knóbba |



### Orthography & surface

Outcome: cnobba

NOTE: Unattested Old English cognate; likely *cnobba based on ME knob (Chaucer) and Frisian knobbe.
```

### Matching oe_known_problems.tsv entries

_None_

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:14132 (row ID)

- Nearby heading: ### Solution

```text
14130: 
14131: **TSV update:**
14132: - Row 2087: Proto `*knuppăz` → `*knubbô`
14133: - Target: `cnobba` (unchanged, but now matches FST output)
14134: - Note: Keep the "unattested" note, but clarify it now has correct proto
```

#### Germanic/docs/DEV_NOTES.md:14138 (row ID)

- Nearby heading: ### Implementation (2026-04-06)

```text
14136: ### Implementation (2026-04-06)
14137: 
14138: Row 2087 changed:
14139: - Proto: `*knuppăz` → `*knubbô`
14140: 
```

### Analysis and dossier hits

_None_

## Supporting/background evidence

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:1734 (exact COUNTERPART)

- Nearby heading: ## A-Restoration Fix (2026-02-06)

```text
1732:   - Reconstructed PGmc weak noun: **\*knubban‑** (knob family).
1733:   - **OE cnæp** (Kroonen p. 335) is **\*knapp‑**, not the knob etymon; keep families distinct.
1734:   - TSV: OE slot **cnobba** marked **unattested** (based on ME knob + Frisian knobbe); note added in TSV.
1735: - OE weak-tail reduction sanity check (2026-01-26):
1736:   - **Observation:** `OldEnglishWeakTailReduction` appears inert in current builds; `*u` in weak tails (e.g., *tehun, *sebun, *newun) stays `{*u}` at `EnglishAfterProtoToOEWeakTail`, so the new `{*u}->{*o}` line does **not** affect `*-un`.
```

#### Germanic/docs/DEV_NOTES.md:10395 (exact COUNTERPART)

- Nearby heading: ## Mismatch Progress Log (2026-03-14)

```text
10393: | 2026-03-19 | 57 | -8 | — | Multiple TSV/FST fixes (huniġ, thistle, etc.) |
10394: | 2026-04-05 | 55 | -2 | — | span fix (feminine ō-stem dat.sg.) |
10395: | 2026-04-06 | 52 | -3 | — | TSV fixes: dile, lappa, cnobba |
10396: | 2026-04-07 | 49 | -3 | 0a649b3 | būgan/sċūfan past 3pl paradigm cells |
10397: | 2026-04-07 | 48 | -1 | b1cc80e | heord fix: was 'hierd' (herdsman ≠ herd) |
```

#### Germanic/docs/DEV_NOTES.md:14058 (exact COUNTERPART)

- Nearby heading: ## OE cnobba 'knob': Unattested form (2026-04-06)

```text
14056: ---
14057: 
14058: ## OE cnobba 'knob': Unattested form (2026-04-06)
14059: 
14060: ### The problem
```

#### Germanic/docs/DEV_NOTES.md:14066 (exact COUNTERPART)

- Nearby heading: ### The problem

```text
14064: **Expected:** `cnobba`
14065: 
14066: The TSV note says: "Unattested Old English cognate; likely *cnobba based on ME knob (Chaucer) and Frisian knobbe."
14067: 
14068: ### Research
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

#### Germanic/docs/DEV_NOTES.md:1730 (concept name)

- Nearby heading: ## A-Restoration Fix (2026-02-06)

```text
1728:   - Data update: `server/data/germanic-aligned-final.tsv` (OE heċġ → heġġ) with NOTE that **heċġ is the more standard spelling**; Wiktionary TSV left unchanged.
1729:   - As of 2026-01-22g, output is **heġġ** (matches expected); see `docs/debug_snapshots/oe_mismatch_report_2026-01-22g.txt` and `docs/debug_snapshots/oe_full_trace_report_2026-01-22g.txt`.
1730: - Knob (2026-01-22):
1731:   - **Unattested in Old English**; first attested in Middle English (Chaucer): “The knobbes sittynge on his chekes.”
1732:   - Reconstructed PGmc weak noun: **\*knubban‑** (knob family).
```

#### Germanic/docs/DEV_NOTES.md:1732 (concept name)

- Nearby heading: ## A-Restoration Fix (2026-02-06)

```text
1730: - Knob (2026-01-22):
1731:   - **Unattested in Old English**; first attested in Middle English (Chaucer): “The knobbes sittynge on his chekes.”
1732:   - Reconstructed PGmc weak noun: **\*knubban‑** (knob family).
1733:   - **OE cnæp** (Kroonen p. 335) is **\*knapp‑**, not the knob etymon; keep families distinct.
1734:   - TSV: OE slot **cnobba** marked **unattested** (based on ME knob + Frisian knobbe); note added in TSV.
```

#### Germanic/docs/DEV_NOTES.md:1733 (concept name)

- Nearby heading: ## A-Restoration Fix (2026-02-06)

```text
1731:   - **Unattested in Old English**; first attested in Middle English (Chaucer): “The knobbes sittynge on his chekes.”
1732:   - Reconstructed PGmc weak noun: **\*knubban‑** (knob family).
1733:   - **OE cnæp** (Kroonen p. 335) is **\*knapp‑**, not the knob etymon; keep families distinct.
1734:   - TSV: OE slot **cnobba** marked **unattested** (based on ME knob + Frisian knobbe); note added in TSV.
1735: - OE weak-tail reduction sanity check (2026-01-26):
```

#### Germanic/docs/DEV_NOTES.md:2394 (concept name)

- Nearby heading: ### Old English data population

```text
2392: ### Old English data population
2393: - Added a Wiktionary scraper (`server/tools/fetch_old_english_from_wiktionary.py`) and parsed the Swadesh + API data into `server/data/old_english_wiktionary.tsv`; the updater now merges both sources and writes IPA/tokens/notes back into the aligned Germanic TSVs.
2394: - Ran the helper across all 376 English concepts so the Old English rows now have attested lemmas (373 entries auto-filled; annotated `fodder fōdor` and `tongs tange` manually, marked `knob` as lacking an OE cognate per the etymology).
2395: - Documented the workflow in `README.md` + `docs/runbook.md`, and added `server/tools/validate_old_english_pairs.py` to guard the 1:1 English↔OE coverage going forward.
2396: 
```

#### Germanic/docs/DEV_NOTES.md:14062 (row ID)

- Nearby heading: ### The problem

```text
14060: ### The problem
14061: 
14062: **TSV row 2087:** `*knuppăz → cnobba` (Old English)
14063: **FST output:** `*knuppăz → cnopp`
14064: **Expected:** `cnobba`
```

#### Germanic/docs/DEV_NOTES.md:14064 (exact COUNTERPART)

- Nearby heading: ### The problem

```text
14062: **TSV row 2087:** `*knuppăz → cnobba` (Old English)
14063: **FST output:** `*knuppăz → cnopp`
14064: **Expected:** `cnobba`
14065: 
14066: The TSV note says: "Unattested Old English cognate; likely *cnobba based on ME knob (Chaucer) and Frisian knobbe."
```

### Analysis and dossier hits

#### Germanic/docs/dossiers/widuwe-u-preservation.md:501 (concept name)

- Nearby heading: ### Cited only via secondary / not directly opened in this round

```text
500:   primary email file (`docs/references/knob_email_2026-01-22.txt`)
501:   is on a different topic (Kroonen on `knob`). The Schuhmacher
502:   consultation appears not to have a corresponding `.txt` file in
```

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
| KnobEmail2026 | explicit year mention (2026) |

