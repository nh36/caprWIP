# Evidence packet — 2055 handle / handlian

> This packet is evidence for drafting. Do not treat all hits as equally authoritative; prefer high-confidence evidence.

## TSV row data

| ID | CONCEPT | COUNTERPART | PROTO | PROTOFORM | DERIVATION_CLASS | NOTE | HISTORY |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2055 | handle | handlian | *xándlōjaną | *xándlōjaną | regular | Du handelen / G handeln are the verb. | TSV fix: was handle (noun f.); changed to handlian (verb 'to handle' < *handulōną, Kroonen/Wiktionary). |

## Manifest status

_No manifest entry._

## High-confidence evidence

### Compact derivation trace entry

```md
# handle
PROTO: *xándlōjaną
EXPECTED: handlian
OUTPUTS: handlian



### Proto-Germanic consonant inheritance

Proto Input: *xándlōjaną

| Earlier Germanic developments | Old English developments |
|:---|:---|
| **Proto-West Germanic**<br>[no change]<br><br>**Northwest Germanic**<br>[no change] | **Old English**<br>OE Heavy Syllable Nasal Apocope: *xándlōjan<br>OE Secondary Nasalization: *xándlōjąn<br>OE I Umlaut: *xándlējąn<br>OE Unstressed Long Vowel Shortening: *xándlejąn<br>OE Weak Tail Reduction: *xándlejan<br>OE Intervocalic J Vocalization: *xándleian<br>OE Unstressed EI Contraction: *xándlian |



### Orthography & surface

Old English Orthography: h*ándlian
Outcome: handlian

NOTE: Du handelen / G handeln are the verb.
```

### Matching oe_known_problems.tsv entries

_None_

### DEV_NOTES hits

_None_

### Analysis and dossier hits

_None_

## Supporting/background evidence

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:37897 (exact COUNTERPART)

- Nearby heading: ### §17.32.7 The choice: very-early vs very-late analogy

```text
37895:   by regular sound change from this shape, exactly as it does for the
37896:   other class-III→II refashioned verbs already in the TSV
37897:   (`búrōjaną → borian`, `líznōjaną → liornian`, `xándlōjaną → handlian`,
37898:   `súndrōjaną → sundrian`, etc.).
37899: 
```

### Analysis and dossier hits

_None_

### Local lexical-table hits

#### old_english_wiktionary.tsv

| ENGLISH | OE_FORM | SOURCE | DETAIL | PAGE |
| :--- | :--- | :--- | :--- | :--- |
| handle | handle | der | template:der | handle |

#### old_english_swadesh.tsv

_None_

## Possibly stale or diagnostic evidence

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:2830 (concept name)

- Nearby heading: ### All 8 Class II Weak Verbs in TSV (all produce -eian)

```text
2828: | *likkōjăną     | liċceian      | liccian         | palatal_extra__j_triggered |
2829: | *skawōjăną     | sċaweian      | scēawian        | breaking_missing__ea  |
2830: | *xandlōjăną    | handleian     | handle          | final_vowel_missing   |
2831: | *sundrōjăną    | sundreian     | sundor-         | cons_mismatch        |
2832: | *wainōjăną     | wāneian       | hwīnan          | i_umlaut_missing     |
```

#### Germanic/docs/DEV_NOTES.md:3592 (concept name)

- Nearby heading: #### Pipeline verification

```text
3590: 5. **OEUnstressedLongVowelShortening handles {*ô} → {*a}** as a late change (line 1340), after AFB and A-restoration, so the resulting -a is not fronted — giving OE -a for trimoraic forms, matching all sources.
3591: 
3592: A hypothetical trimoraic *-ôz (e.g., nom.pl.) is not currently in the suffix list (not needed for our TSV data), but the system would handle it correctly: PGmcFinalOZShortening would not match ({*ō} ≠ {*ô}); PGmcFinalZDeletion would delete {*z}; the freed {*ô} would pass through ō-raising and AFB unchanged; OEUnstressedLongVowelShortening would produce {*a}. Result: -a, matching R/T and Bülbring for nom.pl.
3593: 
3594: ---
```

#### Germanic/docs/DEV_NOTES.md:4046 (concept name)

- Nearby heading: ### The fix (implemented)

```text
4044: 1. **Removed** PGmcBAllophony from PGmcConsonantRules (which fires early in the pipeline)
4045: 2. **Added** PGmcBAllophony after PWGmcJGemination in EnglishProtoToOE
4046: 3. **Added** geminate-restore clause to handle R/T vol.1 §3.2.4 — geminates are always stops:
4047:    ```
4048:    {*β} -> {*b} || _ {*b}
```

#### Germanic/docs/DEV_NOTES.md:5172 (concept name)

- Nearby heading: ### Why the disagreement exists

```text
5170: 1. We cannot confidently identify the conditioning environment
5171: 2. We cannot determine when the change occurred
5172: 3. Different scholars handle the uncertainty differently:
5173:    - Conservative: reconstruct \*nista-, note lowering happened "somewhere"
5174:    - Phonologically explicit: reconstruct \*nesta- for WGmc
```

#### Germanic/docs/DEV_NOTES.md:7849 (concept name)

- Nearby heading: ### What Would Need to Change for Consistency

```text
7847:    The output would be the same, but the rule would document the PGmc allophony.
7848: 
7849: 3. **Leave PWGmcDentalHardening to handle only intervocalic/final `*ð`:**
7850:    ```foma
7851:    define PWGmcDentalHardening [
```

#### Germanic/docs/DEV_NOTES.md:8004 (concept name)

- Nearby heading: ### Root Cause: NSL Rule Missing `*y`

```text
8002: ```
8003: 
8004: **The rule doesn't handle `*y`!**
8005: 
8006: When `*funxstiz` undergoes i-umlaut, `*u → *y`. Then when NSL tries to apply,
```

### Analysis and dossier hits

#### Germanic/docs/analysis/four_complex_tsv_items.md:69 (concept name)

- Nearby heading: ### Pipeline issues (2 independent problems)

```text
68: 
69: Even with j-gemination, our breaking rules would need to handle the unique
70: case of breaking before palatalized *[x'x']. R/T (§6.2.5, lines 10943-10955)
```

#### Germanic/docs/analysis/four_complex_tsv_items.md:127 (concept name)

- Nearby heading: ### Verdict: DOCUMENTED EXCEPTION

```text
126: reconstruction is contested (Kroonen gives \*skeld-linga-, but the Gothic form
127: has \*i). Our pipeline is not designed to handle compound words. Best treated
128: as a documented exception.
```

#### Germanic/docs/analysis/notable_findings.md:406 (concept name)

- Nearby heading: ## 2. NWGmc u-lowering exceptions near labials: a non-Neogrammarian pattern

```text
405: Following R/T's honest assessment, we treat the basic lowering as a
406: regular sound law and handle the handful of exceptions by marking them as
407: documented irregularities in the TSV. A Bülbring-style labial-blocking
```

#### Germanic/docs/analysis/notable_findings.md:554 (concept name)

- Nearby heading: ## 3. PWGmc \*j-related sound changes: formalization of under-specified rules

```text
553: separate problems, but for the FST they converge in a single module that
554: must handle all *j-bearing forms.
555: 
```

#### Germanic/docs/dossiers/g-palatalisation-conditioning.md:109 (concept name)

- Nearby heading: ### 2.1 Campbell, *Old English Grammar* (1959), §§ 426–430

```text
108: in front-V _ consonant environment: *æcer, nægl, fægr, wegn, regn, segl* —
109: exactly the cases the over-narrow proposal would mis-handle.
110: 
```

#### Germanic/docs/dossiers/g-palatalisation-conditioning.md:367 (concept name)

- Nearby heading: ## 5. The single-ġ / geminate-ċġ split, and dialect notes

```text
366:   `*wégaz → ʋeɪ`) shows that downstream rules (`SilentCleanup`, `Surface`,
367:   `Orthography`) handle the [j] vocalisation correctly when the cascade
368:   receives a single-segment palatal output. **As long as the narrowing is
```

#### Germanic/docs/dossiers/un-to-on-chronology.md:466 (concept name)

- Nearby heading: ## Implications for FST design

```text
465:   closed-syllable, ending-specific, or word-final conditioning needs
466:   to be added to handle the pret.pl.; the harmony rule alone yields
467:   the right phonological output, and the morphological overlay
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

