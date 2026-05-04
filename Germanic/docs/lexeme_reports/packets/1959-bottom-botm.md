# Evidence packet — 1959 bottom / botm

> This packet is evidence for drafting. Do not treat all hits as equally authoritative; prefer high-confidence evidence.

## TSV row data

| ID | CONCEPT | COUNTERPART | PROTO | PROTOFORM | DERIVATION_CLASS | NOTE | HISTORY |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1959 | bottom | botm | *búdmaz | *búttmaz | early_analogy | Kroonen p.82: OE < *buttma- (oblique stem variant via PIE dissimilation) | Source: Wiktionary etymology (template:inh) \| Source: Wiktionary etymology (template:inh) |

## Manifest status

| REPORT_PATH | STATUS |
| :--- | :--- |
| pilot/bottom.md | pilot |

## High-confidence evidence

### Compact derivation trace entry

```md
# bottom
PROTO: *búttmaz
EXPECTED: botm
OUTPUTS: botm



### Proto-Germanic consonant inheritance

Proto Input: *búttmaz

| Earlier Germanic developments | Old English developments |
|:---|:---|
| **Proto-West Germanic**<br>[no change]<br><br>**Northwest Germanic**<br>NWGmc U Lowering: *bóttmaz<br>PGmc Final Z Deletion: *bóttma | **Old English**<br>PWGmc Final Bare A Loss: *bóttm<br>OE Preconsonantal Degemination: *bótm |



### Orthography & surface

Outcome: botm

NOTE: Kroonen p.82: OE < *buttma- (oblique stem variant via PIE dissimilation)
```

### Matching oe_known_problems.tsv entries

_None_

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:29891 (exact pair)

- Nearby heading: #### §17.18.2  Current TSV state (11 candidate words)

```text
29889: | 1 | \*θístilaz | **þistel** | þistl | ❌ MISMATCH |
29890: | 2 | \*bōsmaz | bōsm | bōsm | ✓ |
29891: | 3 | \*búttmaz | botm | botm | ✓ |
29892: | 4 | \*xáslaz | hæsl | hæsl | ✓ |
29893: | 5 | \*nēðlō | nǣdl | nǣdl | ✓ |
```

#### Germanic/docs/DEV_NOTES.md:42114 (exact pair)

- Nearby heading: ### The diagnosis: a missing apocope environment

```text
42112: 
42113: Disyllabic apocope handles `shortV + 2+C + finalV` correctly (line
42114: 2836); that's how `*búttmaz → botm` works. But the trisyllabic
42115: extension of the same first-syllable shape is absent.
42116: 
```

#### Germanic/docs/DEV_NOTES.md:42174 (exact pair)

- Nearby heading: ### Verification plan

```text
42172: 3. Probe `*spénnilō` → expect `spinl`.
42173: 4. Spot-probe regression candidates with shape `V̆CC + V̆C + V`:
42174:    `*búttmaz → botm` (control), `*nátilō → netl`, `*fátilō → fetl`,
42175:    `*fásilō → fesl` — all should be unchanged.
42176: 5. `python3 Germanic/tools/oe_mismatch_report.py` — expect
```

### Analysis and dossier hits

_None_

## Supporting/background evidence

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:11 (exact COUNTERPART)

- Nearby heading: ### Polished topic sections

```text
9: - [OE Medial Vowel Syncope: meolc and netle](#oe-medial-vowel-syncope-meolc-and-netle-2026-03-21)
10: - [OE duru 'door': Stem-Class Correction](#oe-duru-door-stem-class-correction)
11: - [OE botm 'bottom': Paradigmatic Leveling](#oe-botm-bottom-paradigmatic-leveling)
12: - [PGmc *i > WGmc *e Lowering](#pgmc-i--wgmc-e-lowering-the-case-of-nest-2026-03-09h)
13: 
```

#### Germanic/docs/DEV_NOTES.md:1025 (exact COUNTERPART)

- Nearby heading: ## OE botm 'bottom': Paradigmatic Leveling and Kluge's Law

```text
1023: ---
1024: 
1025: ## OE botm 'bottom': Paradigmatic Leveling and Kluge's Law
1026: 
1027: **Date:** 2026-03-10
```

#### Germanic/docs/DEV_NOTES.md:1032 (exact COUNTERPART)

- Nearby heading: ### The problem

```text
1030: ### The problem
1031: 
1032: The TSV lists `*budmăz → botm`, but our FST produces `bodm` (with voiced *d*). The expected form `botm` shows voiceless *t*. The discrepancy reflects complex PIE morphophonology.
1033: 
1034: ### PIE and Proto-Germanic etymology
```

#### Germanic/docs/DEV_NOTES.md:1092 (exact COUNTERPART)

- Nearby heading: ### Daughter-language stem variants

```text
1090: | **Old Saxon** | `bodom` | `*budma-` | nominative stem (with `*d`) |
1091: | **Old High German** | `bodam` | `*buþma-` (?) | variant with fricative (Orel: `*-þ-`) |
1092: | **Old English** | `botm` | `*buttma-` | oblique stem (with `*tt`) |
1093: | **Old Norse** | `botn` | `*buttna-` | oblique stem (with `*n` suffix) |
1094: 
```

#### Germanic/docs/DEV_NOTES.md:1096 (exact COUNTERPART)

- Nearby heading: ### Daughter-language stem variants

```text
1094: 
1095: Kroonen (p.82):
1096: > "The resulting paradigm **\*budmṓ, \*buttaz** gave rise to multiple stem variants, i.e. OS bodom < \*budma-, OE botm < \*buttma- and ON botn < \*buttna-."
1097: 
1098: #### The OE form `*buttma-`
```

#### Germanic/docs/DEV_NOTES.md:1106 (exact COUNTERPART)

- Nearby heading: #### Other WGmc evidence

```text
1104: Orel (`*buðmaz ~ *butmaz`) notes: "Unexplained fluctuations in the intervocalic dental." This reflects the paradigmatic alternation that Kroonen 2006 explains.
1105: 
1106: R/T vol.2 (§6.9.5) lists the dialect variation in consonant quality: "Here too belongs botm 'bottom, ground, foundation' (OFri. bodem (*-d-), OS bodom, OHG bodam (*-þ-), ON botn)".
1107: 
1108: ### Campbell on the phonology
```

### Analysis and dossier hits

_None_

### Local lexical-table hits

#### old_english_wiktionary.tsv

| ENGLISH | OE_FORM | SOURCE | DETAIL | PAGE |
| :--- | :--- | :--- | :--- | :--- |
| bottom | botm | inh | template:inh | bottom |

#### old_english_swadesh.tsv

_None_

## Possibly stale or diagnostic evidence

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:1038 (concept name)

- Nearby heading: #### The PIE mn-stem paradigm

```text
1036: #### The PIE mn-stem paradigm
1037: 
1038: The PIE word for 'bottom, ground' was a **hysterodynamic mn-stem** (Kroonen p.82):
1039: 
1040: | Case | PIE Form | Meaning |
```

#### Germanic/docs/DEV_NOTES.md:1042 (concept name)

- Nearby heading: #### The PIE mn-stem paradigm

```text
1040: | Case | PIE Form | Meaning |
1041: |------|----------|---------|
1042: | Nominative | `*bʰudʰ-mḗn` | 'bottom' |
1043: | Genitive | `*bʰudʰ-mn-ós` | 'of the bottom' |
1044: 
```

#### Germanic/docs/DEV_NOTES.md:1043 (concept name)

- Nearby heading: #### The PIE mn-stem paradigm

```text
1041: |------|----------|---------|
1042: | Nominative | `*bʰudʰ-mḗn` | 'bottom' |
1043: | Genitive | `*bʰudʰ-mn-ós` | 'of the bottom' |
1044: 
1045: The root is `*bʰudʰ-` 'bottom', cognate with:
```

#### Germanic/docs/DEV_NOTES.md:1045 (concept name)

- Nearby heading: #### The PIE mn-stem paradigm

```text
1043: | Genitive | `*bʰudʰ-mn-ós` | 'of the bottom' |
1044: 
1045: The root is `*bʰudʰ-` 'bottom', cognate with:
1046: - Sanskrit `budhná-` 'bottom, ground'
1047: - Greek `πυθμήν` (pythmḗn) 'bottom, depth, root'
```

#### Germanic/docs/DEV_NOTES.md:1314 (row ID)

- Nearby heading: ### Implementation (2026-03-10)

```text
1312: ### Implementation (2026-03-10)
1313: 
1314: Changed PROTOFORM from `*budmăz` to `*buttmăz` in TSV row 1959 only.
1315: 
1316: **Result:** 301 → **302/380 matches (+1)**
```

### Analysis and dossier hits

#### Germanic/docs/dossiers/widuwe-u-preservation.md:577 (concept name)

- Nearby heading: ## §8. Bottom line

```text
576: 
577: ## §8. Bottom line
578: 
```

#### Germanic/docs/dossiers/widuwe-u-preservation.md:1309 (concept name)

- Nearby heading: ### B.9 RECOMMENDATIONS

```text
1308: 
1309: **Bottom line.** The draft rule is **safe but narrow**. It
1310: correctly derives the one form it is designed to derive. If
```

## Bibliography-key candidates

### Preferred candidates

| Key | Why it was selected |
| :--- | :--- |
| Kroonen2013 | default Proto-Germanic etymology key for Kroonen |
| Campbell1959 | single available key for Campbell |
| Orel2003 | single available key for Orel |
| KlugeSeebold2011 | single available key for Kluge |

### Low-confidence candidates

| Key | Why it was selected |
| :--- | :--- |
| Kroonen2011 | surname mention only: Kroonen |
| Kroonen2006 | author + year mention (Kroonen 2006) |

