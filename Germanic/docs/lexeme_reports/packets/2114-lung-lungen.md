# Evidence packet — 2114 lung / lungen

> This packet is evidence for drafting. Do not treat all hits as equally authoritative; prefer high-confidence evidence.

## TSV row data

| ID | CONCEPT | COUNTERPART | PROTO | PROTOFORM | DERIVATION_CLASS | NOTE | HISTORY |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2114 | lung | lungen | *lungō | *lúnganjō | early_analogy | *lunganjō (ō-stem feminine with *-anjō suffix; Wiktionary Reconstruction:Proto-Germanic/*lunganjō). OE lungen specifically reflects the *-anjō derivative. | Previous TSV had *lungō (simpler n-stem per Kroonen p.367). \| Grammar extended to accept *-anjō suffix (2026-04-05). |

## Manifest status

_No manifest entry._

## High-confidence evidence

### Compact derivation trace entry

```md
# lung
PROTO: *lúnganjō
EXPECTED: lungen
OUTPUTS: lungen



### Proto-Germanic consonant inheritance

Proto Input: *lúnganjō

| Earlier Germanic developments | Old English developments |
|:---|:---|
| **Proto-West Germanic**<br>PWGmc J Gemination: *lúngannjō<br><br>**Northwest Germanic**<br>NWGmc Final Long O Raising: *lúngannju | **Old English**<br>OE I Umlaut: *lúngennju<br>OE High Vowel Apocope: *lúngennj<br>OE J Loss After Heavy: *lúngenn<br>OE Final Geminate Simplification: *lúngen |



### Orthography & surface

Outcome: lungen

NOTE: *lunganjō (ō-stem feminine with *-anjō suffix; Wiktionary Reconstruction:Proto-Germanic/*lunganjō). OE lungen specifically reflects the *-anjō derivative.
```

### Matching oe_known_problems.tsv entries

_None_

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:13412 (row ID)

- Nearby heading: ### The mismatch

```text
13410: ```
13411: 
13412: The TSV entry (row 2114) has proto `*lungō` with an earlier note claiming it was fixed
13413: from `*lungwąn` (spurious) to `*lungō` (neut. n-stem per Kroonen). But this note was
13414: **incorrect** — it confused the base form `*lungô` with the derived OE form.
```

### Analysis and dossier hits

_None_

## Supporting/background evidence

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:23 (exact COUNTERPART)

- Nearby heading: ### Mismatch fixes (Mar 2026)

```text
21: - [OE wīþiġ 'withy': ja-stem vs Sievers' Law](#oe-wīþiġ-withy-ja-stem-adjective-vs-sievers-law-syncope-2026-03-19)
22: - [OE heofon 'heaven': Back Umlaut and Nasal Dissimilation](#oe-heofon-heaven-back-umlaut-and-medial-syncope-2026-03-20)
23: - [OE lungen 'lung': The *-anjō Suffix Problem](#oe-lungen-lung-the--anjō-suffix-problem-2026-03-21)
24: 
25: ### Sievers' Law and Class I Weak Verbs (Mar 2026)
```

#### Germanic/docs/DEV_NOTES.md:13401 (exact COUNTERPART)

- Nearby heading: ## OE lungen 'lung': The *-anjō Suffix Problem (2026-03-21)

```text
13399: ---
13400: 
13401: ## OE lungen 'lung': The *-anjō Suffix Problem (2026-03-21)
13402: 
13403: **Date:** 2026-03-21
```

#### Germanic/docs/DEV_NOTES.md:13409 (exact COUNTERPART)

- Nearby heading: ### The mismatch

```text
13407: The mismatch report shows:
13408: ```
13409: *lungō -> lung (expected lungen)
13410: ```
13411: 
```

#### Germanic/docs/DEV_NOTES.md:13419 (exact COUNTERPART)

- Nearby heading: ### Etymology research

```text
13417: 
13418: **Wiktionary reconstruction:**
13419: - OE `lungen` < PGmc **`*lunganjō`** (ō-stem feminine)
13420: - This is an extension of the simpler `*lungô` via the `*-anjō` suffix
13421: - Cognates: OFris `lungene/lungen`, OS `lungannia`, OHG `lunganna/lungunna`
```

#### Germanic/docs/DEV_NOTES.md:13421 (exact COUNTERPART)

- Nearby heading: ### Etymology research

```text
13419: - OE `lungen` < PGmc **`*lunganjō`** (ō-stem feminine)
13420: - This is an extension of the simpler `*lungô` via the `*-anjō` suffix
13421: - Cognates: OFris `lungene/lungen`, OS `lungannia`, OHG `lunganna/lungunna`
13422: 
13423: **The `*-anjō` suffix:**
```

#### Germanic/docs/DEV_NOTES.md:13429 (exact COUNTERPART)

- Nearby heading: ### Etymology research

```text
13427: 
13428: **Bosworth-Toller attestations:**
13429: - `lungen` — nominative singular (glossed as *pulmo*)
13430: - `lungenne` — dative singular ("ðone man ðe biþ lungenne wund" = wounded in the lung)
13431: - `lungena` — genitive plural (*pulmones*)
```

### Analysis and dossier hits

_None_

### Local lexical-table hits

#### old_english_wiktionary.tsv

| ENGLISH | OE_FORM | SOURCE | DETAIL | PAGE |
| :--- | :--- | :--- | :--- | :--- |
| lung | lungen | inh | template:inh | lung |

#### old_english_swadesh.tsv

_None_

## Possibly stale or diagnostic evidence

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:13430 (concept name)

- Nearby heading: ### Etymology research

```text
13428: **Bosworth-Toller attestations:**
13429: - `lungen` — nominative singular (glossed as *pulmo*)
13430: - `lungenne` — dative singular ("ðone man ðe biþ lungenne wund" = wounded in the lung)
13431: - `lungena` — genitive plural (*pulmones*)
13432: 
```

#### Germanic/docs/DEV_NOTES.md:13449 (concept name)

- Nearby heading: ### FST analysis

```text
13447: Current behavior:
13448: ```
13449: *lungō  → lung   (high-vowel apocope deletes final *u from *ō → *u)
13450: *lungô  → lunga  (weak masc. ending -ô → -a)
13451: *lungōn → lunge  (weak fem. with -n retained → -e)
```

#### Germanic/docs/DEV_NOTES.md:13461 (concept name)

- Nearby heading: ### FST analysis

```text
13459: The issue is that our `pgrmWord` grammar doesn't include the `*-anjō` derivational
13460: suffix pattern. The form `*lunganjō` has the structure:
13461: - Root: `lung-`
13462: - Suffix: `-anj-` (derivational)
13463: - Ending: `-ō` (ō-stem nom.sg.)
```

### Analysis and dossier hits

_None_

## Bibliography-key candidates

### Preferred candidates

| Key | Why it was selected |
| :--- | :--- |
| Kroonen2013 | default Proto-Germanic etymology key for Kroonen |
| SieversBrunner1965 | single available key for Sievers |
| BosworthToller1898 | single available key for Toller |

### Low-confidence candidates

| Key | Why it was selected |
| :--- | :--- |
| Kroonen2011 | surname mention only: Kroonen |
| Kroonen2006 | surname mention only: Kroonen |

