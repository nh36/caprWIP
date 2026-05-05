# Evidence packet — 2141 nightmare / mare

> This packet is evidence for drafting. Do not treat all hits as equally authoritative; prefer high-confidence evidence.

## TSV row data

| ID | CONCEPT | COUNTERPART | PROTO | PROTOFORM | DERIVATION_CLASS | NOTE | HISTORY |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2141 | nightmare | mare | *márōn | *márōn | regular | Unattested OE compound *nihtmare; second element is OE mare 'nightmare' (n-stem fem., < PWGmc *mara, *marōn-, cf. ON mara, OHG mara). Per Ringe & Taylor *Development of Old English* vol. 2 p. 192 the attested OE forms are mare (nom.sg.), maran (obl.), and variant mere. Earlier target mære reflected Wiktionary headword (Orel-style spelling) and was conflated with the unrelated OE adjective mǣre 'famous' (< PGmc *mēriz, jō/jā-stem); corrected per §17.28. | Source: Wiktionary etymology (template:inh) \| Source: Wiktionary etymology (template:inh) |

## Manifest status

_No manifest entry._

## High-confidence evidence

### Compact derivation trace entry

```md
# nightmare
PROTO: *márōn
EXPECTED: mare
OUTPUTS: mare



### Proto-Germanic consonant inheritance

Proto Input: *márōn

| Earlier Germanic developments | Old English developments |
|:---|:---|
| **Proto-West Germanic**<br>[no change]<br><br>**Northwest Germanic**<br>NWGmc N Stem N Loss: *márǭ | **Old English**<br>Anglo Frisian Brightening: *mærǭ<br>OE A Restoration: *marǭ<br>OE Unstressed Long Vowel Shortening: *maræ<br>OE Unstressed AE Merger: *mare |



### Orthography & surface

Outcome: mare

NOTE: Unattested OE compound *nihtmare; second element is OE mare 'nightmare' (n-stem fem., < PWGmc *mara, *marōn-, cf. ON mara, OHG mara). Per Ringe & Taylor *Development of Old English* vol. 2 p. 192 the attested OE forms are mare (nom.sg.), maran (obl.), and variant mere. Earlier target mære reflected Wiktionary headword (Orel-style spelling) and was conflated with the unrelated OE adjective mǣre 'famous' (< PGmc *mēriz, jō/jā-stem); corrected per §17.28.
```

### Matching oe_known_problems.tsv entries

_None_

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:36672 (exact pair)

- Nearby heading: ### §17.25.7 Regression after first build — diagnosis and follow-up fix

```text
36670: | `*táppô`   | `tappa`   | `tæppa`  | `tæppa`  | **now matching** (−1 mismatch, but see below — this is wrong-side-of-correct) |
36671: | `*láppô`   | `lappa`   | `læppa`  | `lappa`  | **NEW mismatch** |
36672: | `*márōn`   | `mære`    | `mare`   | `mære`   | **NEW mismatch** |
36673: 
36674: Net: **+2 to mismatch count**. Two distinct bugs are surfaced.
```

#### Germanic/docs/DEV_NOTES.md:36727 (exact pair)

- Nearby heading: ### §17.25.7 Regression after first build — diagnosis and follow-up fix

```text
36725: Fix: add `{*ô}` to `OEARestorationStrongOTail`.
36726: 
36727: **Independent — `*márōn → mare` is not a bug in our rule.**
36728: 
36729: For `*márōn`, intervening *r and trigger *ōn-: under §17.25.3 the
```

#### Germanic/docs/DEV_NOTES.md:36729 (exact PROTOFORM)

- Nearby heading: ### §17.25.7 Regression after first build — diagnosis and follow-up fix

```text
36727: **Independent — `*márōn → mare` is not a bug in our rule.**
36728: 
36729: For `*márōn`, intervening *r and trigger *ōn-: under §17.25.3 the
36730: restoration rule fires correctly (single *r is not a blocker;
36731: `{*ō} {*n}` is in StrongOTail at line 1845). The output `mare` is
```

### Analysis and dossier hits

_None_

## Supporting/background evidence

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:10422 (exact COUNTERPART)

- Nearby heading: ## Mismatch Progress Log (2026-03-14)

```text
10420: | 2026-04-26 | 24 | -1 | 5c1bf80c | A-restoration before single *r/*l (§17.25) |
10421: | 2026-04-26 | 23 | -1 | 1b9a44f1 | faran: TSV target færan → faran (§17.26) |
10422: | 2026-04-26 | 22 | -1 | 37031f31 | mare: TSV target mære → mare (§17.28) |
10423: | 2026-04-26 | 21 | -1 | 8bb2ecef | sundrian: target sundor- → sundrian (§17.29) |
10424: | 2026-04-26 | 20 | -1 | 871ec6ab | bēġen: TSV revert + monosyllable apocope guard (§17.30/31) |
```

### Analysis and dossier hits

#### Germanic/docs/analysis/arestoration_r_l_research.md:141 (exact COUNTERPART)

- Nearby heading: ### 2.2 Ringe & Taylor (2014), *A Linguistic History of English vol. II* — file `ringe_taylor_linguistic_history_vol2.txt`

```text
140: >
141: > PNWGmc *marōn- 'nightmare' (ON mara) > PWGmc *mara, *marōn- (OHG mara) > *mærē, *mærōn- >— OE **mare, maran**, and *mere*;
142: >
```

#### Germanic/docs/analysis/arestoration_r_l_research.md:370 (exact COUNTERPART)

- Nearby heading: ### 4.1 Pro-restoration evidence with single intervening *r* or *l* (back vowel triggers)

```text
369: | **maga** 'stomach' | *\*magō → \*mæga → maga* | R/T 11119 |
370: | **mara, maran** 'nightmare' | *\*marō, \*marōn- → \*mærē, \*mærōn- → mare, maran* | R/T 11116 |
371: | **hara** 'hare' | *\*hasō → \*hærē → hara* | R/T 11117 |
```

#### Germanic/docs/analysis/arestoration_r_l_research.md:717 (exact PROTOFORM)

- Nearby heading: ## 11. Affected TSV rows

```text
716: | 2053 | `*xámaras` | `hameres` | `hameres` | `hameres` | intervening `*m` (not r/l); already correct under either rule |
717: | 2141 | `*márōn` | `mære` | `mære` | `mære` | long `*ā/ǣ`, out of scope of short A-restoration |
718: | 2201 | `*sáiwalō` | `sāwol` | `sāwol` | `sāwol` | intervening `*iwal` is multi-segment; restoration not triggered for first *a* (already covered by other rules) |
```

### Local lexical-table hits

#### old_english_wiktionary.tsv

| ENGLISH | OE_FORM | SOURCE | DETAIL | PAGE |
| :--- | :--- | :--- | :--- | :--- |
| nightmare | mære | inh | template:inh (unattested; reconstructed *nihtmare) (OE mære attested (cognate with -mare); compound not attested) | nightmare |

#### old_english_swadesh.tsv

_None_

## Possibly stale or diagnostic evidence

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:36731 (exact COUNTERPART)

- Nearby heading: ### §17.25.7 Regression after first build — diagnosis and follow-up fix

```text
36729: For `*márōn`, intervening *r and trigger *ōn-: under §17.25.3 the
36730: restoration rule fires correctly (single *r is not a blocker;
36731: `{*ō} {*n}` is in StrongOTail at line 1845). The output `mare` is
36732: the expected lautgesetzlich result. The TSV target `mære` for row
36733: 2141 (`*nihtmare`, gloss "nightmare", PROTO `*marōn`) is most likely
```

#### Germanic/docs/DEV_NOTES.md:36733 (concept name)

- Nearby heading: ### §17.25.7 Regression after first build — diagnosis and follow-up fix

```text
36731: `{*ō} {*n}` is in StrongOTail at line 1845). The output `mare` is
36732: the expected lautgesetzlich result. The TSV target `mære` for row
36733: 2141 (`*nihtmare`, gloss "nightmare", PROTO `*marōn`) is most likely
36734: either (a) the wrong protoform for that target, or (b) the result of
36735: analogical i-umlaut from another paradigm cell or another stem. It
```

#### Germanic/docs/DEV_NOTES.md:36746 (exact PROTOFORM)

- Nearby heading: ### §17.25.7 Regression after first build — diagnosis and follow-up fix

```text
36744: - `*láppô` → `lappa` (matches target — restored from regression).
36745: - `*táppô` → `tappa` (mismatch vs target `tæppa` — now correctly
36746:   diagnosed as a TSV-target issue, parallel to *márōn and *fáraną).
36747: - `*spárōjaną` → `sparian` (the original §17.25 win, retained).
36748: - `*nadrō` → `næder` (no regression).
```

#### Germanic/docs/DEV_NOTES.md:36772 (exact pair)

- Nearby heading: ### §17.25.8 Post-fix verification

```text
36770: - `*láppô → lappa` ✓ (Bug A fixed: geminate now matches as two segments)
36771: - `*táppô → tappa` (lautgesetzlich-correct; TSV target `tæppa` is the question)
36772: - `*márōn → mare` (lautgesetzlich-correct; TSV target `mære` is the question)
36773: - `*fáraną → faran` (etymologically correct; TSV target `færan` deferred per user)
36774: 
```

#### Germanic/docs/DEV_NOTES.md:36786 (row ID)

- Nearby heading: ### §17.25.8 Post-fix verification

```text
36784:    to a separate loop iteration ("As for the 'bonus row', I would
36785:    also rather discuss it separately as a third issue").
36786: 2. **row 2141 `*nihtmare` PROTO `*marōn` → mære** — parallel to row
36787:    2003. FST output `mare` is regular; target `mære` likely reflects
36788:    analogical i-umlaut or a different protoform. Defer to its own
```

#### Germanic/docs/DEV_NOTES.md:36787 (exact COUNTERPART)

- Nearby heading: ### §17.25.8 Post-fix verification

```text
36785:    also rather discuss it separately as a third issue").
36786: 2. **row 2141 `*nihtmare` PROTO `*marōn` → mære** — parallel to row
36787:    2003. FST output `mare` is regular; target `mære` likely reflects
36788:    analogical i-umlaut or a different protoform. Defer to its own
36789:    loop alongside §17.26 follow-ups.
```

#### Germanic/docs/DEV_NOTES.md:36987 (row ID)

- Nearby heading: ### §17.27.2 Outstanding §17.25-exposed issue

```text
36985: 
36986: One remains for a future loop:
36987: - row 2141 *márōn / *nihtmare → mare (target mære) — substantive
36988:   reconstruction question, deferred.
36989: 
```

#### Germanic/docs/DEV_NOTES.md:36990 (row ID)

- Nearby heading: ## §17.28 *márōn / *nihtmare row 2141: TSV target correction (mære → mare)

```text
36988:   reconstruction question, deferred.
36989: 
36990: ## §17.28 *márōn / *nihtmare row 2141: TSV target correction (mære → mare)
36991: 
36992: ### §17.28.1 Context
```

#### Germanic/docs/DEV_NOTES.md:36996 (row ID)

- Nearby heading: ### §17.28.1 Context

```text
36994: The third TSV-target issue exposed when §17.25 unblocked A-restoration
36995: before single *r/*l. Prior summary in the §17.27.2 outstanding-list:
36996: "row 2141 *márōn / *nihtmare → mare (target mære) — substantive
36997: reconstruction question, deferred."
36998: 
```

#### Germanic/docs/DEV_NOTES.md:37004 (row ID)

- Nearby heading: ### §17.28.1 Context

```text
37002: > For `*márōn`, intervening *r and trigger *ōn-: under §17.25.3 the
37003: > output `mare` is the expected lautgesetzlich result. The TSV target
37004: > `mære` for row 2141 (`*nihtmare`, gloss "nightmare", PROTO `*marōn`)
37005: > is most likely a TSV-target issue parallel to *fáraną.
37006: 
```

#### Germanic/docs/DEV_NOTES.md:37009 (concept name)

- Nearby heading: ### §17.28.2 The reconstruction is uncontroversial

```text
37007: ### §17.28.2 The reconstruction is uncontroversial
37008: 
37009: PGmc / PNWGmc *marōn- 'nightmare' (n-stem fem.) is the standard
37010: reconstruction. Cognates:
37011: 
```

#### Germanic/docs/DEV_NOTES.md:37012 (concept name)

- Nearby heading: ### §17.28.2 The reconstruction is uncontroversial

```text
37010: reconstruction. Cognates:
37011: 
37012: - ON  `mara` 'nightmare, ogress' (n-stem fem.)
37013: - OHG `mara` (n-stem fem.)
37014: - MLG `mare`
```

#### Germanic/docs/DEV_NOTES.md:37019 (concept name)

- Nearby heading: ### §17.28.2 The reconstruction is uncontroversial

```text
37017: Sources:
37018: - **Orel, *A Handbook of Germanic Etymology* p. 261**, lemma `*marōn
37019:   sb.f.`: "ON mara 'nightmare, ogress', OE *mære* 'nightmare', MLG
37020:   mare, OHG mara". Orel cites OE `mære` *but* gives no philological
37021:   evidence for a long-front-vowel form.
```

#### Germanic/docs/DEV_NOTES.md:37025 (concept name)

- Nearby heading: ### §17.28.2 The reconstruction is uncontroversial

```text
37023:   in the canonical paradigm-list of *PWGmc *-ō / *-ōn-* n-stems
37024:   illustrating the A-restoration alternation:
37025:     > PNWGmc *maron- 'nightmare' (ON mara) > PWGmc *mara, *marōn-
37026:     > (OHG mara) > *mærǣ, *meron- >— **OE mare, maran, and mere**;
37027:   This is the same passage that gives `crabba` (with A-restoration),
```

#### Germanic/docs/DEV_NOTES.md:37059 (row ID)

- Nearby heading: ### §17.28.4 Why the TSV target `mære` is wrong

```text
37057: Two plausible sources of the mistaken target:
37058: 
37059: 1. **Wiktionary contamination**: the TSV NOTE for row 2141 explicitly
37060:    says "Source: Wiktionary etymology (template:inh)". Wiktionary's OE
37061:    entry for the nightmare word lists a long-vowel headword `mǣre`,
```

### Analysis and dossier hits

_None_

## Bibliography-key candidates

### Preferred candidates

| Key | Why it was selected |
| :--- | :--- |
| Orel2003 | single available key for Orel |

### Low-confidence candidates

| Key | Why it was selected |
| :--- | :--- |
| Ringe2006 | surname mention only: Ringe |
| Ringe2017 | surname mention only: Ringe |
| RingeTaylor2014 | surname mention only: Ringe |
| Ringe1984 | surname mention only: Ringe |

## Paradigm probe

Philological note; no paradigm probe required for this row under the current classification. The note mentions paradigm forms, but it does not yet depend on a paradigm-cell solution.

