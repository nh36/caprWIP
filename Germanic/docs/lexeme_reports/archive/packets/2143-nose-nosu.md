# Evidence packet — 2143 nose / nosu

> This packet is evidence for drafting. Do not treat all hits as equally authoritative; prefer high-confidence evidence.

## TSV row data

| ID | CONCEPT | COUNTERPART | PROTO | PROTOFORM | DERIVATION_CLASS | NOTE | HISTORY |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2143 | nose | nosu | *nasō | *núsō | early_analogy | - | Source: Wiktionary Old English Swadesh list (retrieved 2025-12-12) \| Source: Wiktionary etymology (template:inh) \| Source: Wiktionary etymology (template:inh) |

## Manifest status

_No manifest entry._

## High-confidence evidence

### Compact derivation trace entry

```md
# nose
PROTO: *núsō
EXPECTED: nosu
OUTPUTS: nosu



### Proto-Germanic consonant inheritance

Proto Input: *núsō

| Earlier Germanic developments | Old English developments |
|:---|:---|
| **Proto-West Germanic**<br>[no change]<br><br>**Northwest Germanic**<br>NWGmc U Lowering: *nósō<br>NWGmc Final Long O Raising: *nósu | **Old English**<br>[no change] |



### Orthography & surface

Outcome: nosu
```

### Matching oe_known_problems.tsv entries

_None_

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:19857 (exact PROTOFORM)

- Nearby heading: ### The Fix

```text
19855: ### The Fix
19856: 
19857: Change PROTOFORM from `*násō` to `*núsō` to match the zero-grade ablaut variant
19858: that actually yields OE `nosu`. This is a TSV data correction, not an FST change.
19859: 
```

#### Germanic/docs/DEV_NOTES.md:19921 (exact pair)

- Nearby heading: ### Why *násō Worked Differently

```text
19919: ### Why *násō Worked Differently
19920: 
19921: For `*násō → nosu` (now fixed to `*núsō`):
19922: 1. The `*ō` was in **final** position
19923: 2. `NWGmcFinalLongORaising` applied: `*ō → *u` (final position)
```

#### Germanic/docs/DEV_NOTES.md:39801 (exact pair)

- Nearby heading: ### Q4 finding — lautgesetz status (cell-switch, not wontfix)

```text
39799: * **Cascade order is fixed by other rows.** Reordering
39800:   `NWGmcFinalLongORaising` before `NWGmcULowering` would
39801:   regress TSV rows 2143 (*núsō → nosu*), 2200 (*súrgō → sorg*),
39802:   2185 (*skúflō → sċofl*) — all attest the lowered + apocopated
39803:   outcome. So Option Z (add/reorder a rule) is blocked by the
```

### Analysis and dossier hits

_None_

## Supporting/background evidence

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:934 (exact COUNTERPART)

- Nearby heading: ### Source analysis

```text
932: **R/T (vol.2, p.385) on OE u-stems:**
933: 
934: > "The u-stems remained a recognizable inflectional class, but its membership was reduced to a few very common and basic words. Still inflected as u-stems in early OE are masc. *sunu* 'son' and *wudu* 'wood' and fem. *hand* 'hand', *nosu* 'nose', and ***duru* 'door'** (the last **originally a root-noun that had shifted into the u-stems**)."
935: 
936: R/T also note (p.28) in discussing u-lowering:
```

#### Germanic/docs/DEV_NOTES.md:959 (exact COUNTERPART)

- Nearby heading: ### Stem-class history

```text
957: 3. **OE**: *duru* inflects as an **u-stem feminine** (R/T vol.2 p.385)
958: 
959: The transition from ō-stem `*durō` to u-stem *duru* involves analogical reshaping. The u-stem paradigm (like *sunu*, *nosu*, *hand*) pulled *duru* into its orbit. The nominative singular *-u* (from `*-uz` or by analogy) yielded the form we see.
960: 
961: ### Why u-lowering doesn't apply
```

#### Germanic/docs/DEV_NOTES.md:19774 (exact COUNTERPART)

- Nearby heading: ## §15.3 TSV Correction: OE nosu 'nose' — Ablaut *nasō ~ *nusō (2026-04-15)

```text
19772: ---
19773: 
19774: ## §15.3 TSV Correction: OE nosu 'nose' — Ablaut *nasō ~ *nusō (2026-04-15)
19775: 
19776: ### The Issue
```

#### Germanic/docs/DEV_NOTES.md:19782 (exact COUNTERPART)

- Nearby heading: ### The Issue

```text
19780: 
19781: ```
19782: *násō -> nasu (expected nosu)
19783: ```
19784: 
```

#### Germanic/docs/DEV_NOTES.md:19785 (exact COUNTERPART)

- Nearby heading: ### The Issue

```text
19783: ```
19784: 
19785: The FST correctly produced `nasu`, but the expected form was `nosu` with `o`.
19786: 
19787: ### Research: The Etymological Ablaut
```

#### Germanic/docs/DEV_NOTES.md:19790 (exact COUNTERPART)

- Nearby heading: ### Research: The Etymological Ablaut

```text
19788: 
19789: **Campbell §116** provides the key evidence:
19790: > "We find o before Prim. Gmc. -ō, which has become -u in OE, e.g. OE **nosu < *nusō**"
19791: 
19792: This explicitly reconstructs `*nusō` (with `*u`), not `*nasō` (with `*a`).
```

#### Germanic/docs/DEV_NOTES.md:24287 (exact PROTOFORM)

- Nearby heading: #### 3. Root-cause: U-lowering has been bled

```text
24285: raising by keeping raising pre-z-loss.
24286: 
24287: The side effect: for a form like \*núsō, raising now fires *first*,
24288: rewriting the suffix to \*-u **before** U-lowering ever sees the
24289: original non-high \*-ō. U-lowering then inspects a high-high sequence
```

#### Germanic/docs/DEV_NOTES.md:24299 (exact PROTOFORM)

- Nearby heading: #### 3. Root-cause: U-lowering has been bled

```text
24297: ──────────────────────────────-|───────────────────────────────-
24298: 1. NWGmcFinalLongORaising      | 1. NWGmcULowering
24299:      *núsō → *núsu             |      *núsō → *nósō
24300: 2. PGmcFinalZDeletion          | 2. NWGmcFinalLongORaising
24301:      (no effect)               |      *nósō → *nósu
```

### Analysis and dossier hits

_None_

### Local lexical-table hits

#### old_english_wiktionary.tsv

| ENGLISH | OE_FORM | SOURCE | DETAIL | PAGE |
| :--- | :--- | :--- | :--- | :--- |
| nose | nosu | inh | template:inh | nose |

#### old_english_swadesh.tsv

| NUMBER | ENGLISH | OLD_ENGLISH | IPA_RAW |
| :--- | :--- | :--- | :--- |
| 75 | nose | nosu | /nozu/ |

## Possibly stale or diagnostic evidence

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:19795 (concept name)

- Nearby heading: ### Research: The Etymological Ablaut

```text
19793: 
19794: **Kroonen (EDPG p.424)** documents the ablaut paradigm:
19795: > "*nasō- ~ *nusō- f. 'nose' — ON nọs f. 'nostril', Far. nọs f., nasar pl. 'nose', 
19796: > OSw. nasær f.pl. 'id.', **OE nosu** f. 'id.', E nose, OFri. nose f. 'id.', 
19797: > OS nasa-druppo m. 'cold', Du. neus c. 'nose', OHG nasa f. 'id.', G Nase f. 'id.'"
```

#### Germanic/docs/DEV_NOTES.md:19796 (concept name)

- Nearby heading: ### Research: The Etymological Ablaut

```text
19794: **Kroonen (EDPG p.424)** documents the ablaut paradigm:
19795: > "*nasō- ~ *nusō- f. 'nose' — ON nọs f. 'nostril', Far. nọs f., nasar pl. 'nose', 
19796: > OSw. nasær f.pl. 'id.', **OE nosu** f. 'id.', E nose, OFri. nose f. 'id.', 
19797: > OS nasa-druppo m. 'cold', Du. neus c. 'nose', OHG nasa f. 'id.', G Nase f. 'id.'"
19798: 
```

#### Germanic/docs/DEV_NOTES.md:19797 (concept name)

- Nearby heading: ### Research: The Etymological Ablaut

```text
19795: > "*nasō- ~ *nusō- f. 'nose' — ON nọs f. 'nostril', Far. nọs f., nasar pl. 'nose', 
19796: > OSw. nasær f.pl. 'id.', **OE nosu** f. 'id.', E nose, OFri. nose f. 'id.', 
19797: > OS nasa-druppo m. 'cold', Du. neus c. 'nose', OHG nasa f. 'id.', G Nase f. 'id.'"
19798: 
19799: Kroonen explicitly notes:
```

#### Germanic/docs/DEV_NOTES.md:19801 (concept name)

- Nearby heading: ### Research: The Etymological Ablaut

```text
19799: Kroonen explicitly notes:
19800: > "The origin of the exclusively Germanic ablaut of **\*nasō-** (ON nọs, OHG nasa) 
19801: > vs. **\*nusō-** (**OE nosu**, OFri. nose, Du. neus) is unclear, but the root 
19802: > **\*nus-** is likely to have arisen as a secondary zero grade following a 
19803: > remodeling of the original paradigm."
```

#### Germanic/docs/DEV_NOTES.md:24263 (exact pair)

- Nearby heading: #### 2. Regression cluster

```text
24261: | PROTOFORM  | Got     | Expected |
24262: |------------|---------|----------|
24263: | \*núsō     | nusu    | nosu     |
24264: | \*skúflō   | sċufl   | sċofl    |
24265: | \*súrgō    | surg    | sorg     |
```

#### Germanic/docs/DEV_NOTES.md:24402 (exact pair)

- Nearby heading: #### 6. Expected outcome

```text
24400:   - OE shortening: \*rǣstǣ → \*rǣste. ✓
24401: 
24402: - `*núsō → nosu` **restored**. Derivation:
24403:   - PGmcConsonantRules: no effect.
24404:   - NWGmcULowering: \*núsō → \*nósō ✓ (original suffix visible).
```

#### Germanic/docs/DEV_NOTES.md:24446 (exact pair)

- Nearby heading: #### 1. Probe outcome (vs. post-§17.10.23 baseline of 38)

```text
24444: 
24445: - Case 3 target `*rástōz → ræste` still passes ✓.
24446: - `*núsō → nosu`, `*skúflō → sċofl`, `*súrgō → sorg`, `*láimōn → lām`,
24447:   `*wéstanē → west` — **fixed** by the reorder (root-*u lowered
24448:   again). `*skúldrō` and `*mízdō` shift back to their pre-§17.10.23
```

### Analysis and dossier hits

_None_

## Bibliography-key candidates

### Preferred candidates

| Key | Why it was selected |
| :--- | :--- |
| Campbell1959 | single available key for Campbell |

### Low-confidence candidates

_None_

