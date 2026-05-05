# Evidence packet — 2100 lid / hlid

> This packet is evidence for drafting. Do not treat all hits as equally authoritative; prefer high-confidence evidence.

## TSV row data

| ID | CONCEPT | COUNTERPART | PROTO | PROTOFORM | DERIVATION_CLASS | NOTE | HISTORY |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2100 | lid | hlid | *xlídą | *xlídą | regular | Proto: *liθuz → *xlidą (Wiktionary *hlidą 'lid, cover') | - |

## Manifest status

_No manifest entry._

## High-confidence evidence

### Compact derivation trace entry

```md
# lid
PROTO: *xlídą
EXPECTED: hlid
OUTPUTS: hlid



### Proto-Germanic consonant inheritance

Proto Input: *xlídą

| Earlier Germanic developments | Old English developments |
|:---|:---|
| **Proto-West Germanic**<br>[no change]<br><br>**Northwest Germanic**<br>[no change] | **Old English**<br>OE Heavy Syllable Nasal Apocope: *xlíd |



### Orthography & surface

Old English Orthography: h*líd
Outcome: hlid

NOTE: Proto: *liθuz → *xlidą (Wiktionary *hlidą 'lid, cover')
```

### Matching oe_known_problems.tsv entries

_None_

### DEV_NOTES hits

_None_

### Analysis and dossier hits

_None_

## Supporting/background evidence

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:5630 (exact COUNTERPART)

- Nearby heading: #### The regressions

```text
5628: |------|-------|------------|----------|----------|
5629: | fright | \*furxtiθō | forhteþu | fyrhtu | *i lowered incorrectly |
5630: | lid | \*xlidą | hled | hlid | *i lowered incorrectly |
5631: 
5632: Both have **velar \*x** in the word, but not immediately after *i:
```

#### Germanic/docs/DEV_NOTES.md:5651 (exact COUNTERPART)

- Nearby heading: #### Lloyd (1966): OE hlid retains *i, but why?

```text
5649: ginen/genen), indicating that onset velars did NOT consistently block in WGmc.
5650: 
5651: #### Lloyd (1966): OE hlid retains *i, but why?
5652: 
5653: Lloyd lists words that retain *i across dialects: "OE fisc, OHG, OS fisk, ON fiskr;
```

#### Germanic/docs/DEV_NOTES.md:5654 (exact COUNTERPART)

- Nearby heading: #### Lloyd (1966): OE hlid retains *i, but why?

```text
5652: 
5653: Lloyd lists words that retain *i across dialects: "OE fisc, OHG, OS fisk, ON fiskr;
5654: OE, OS witan, ON vita, OHG wizzan; ON hliþó, **OE hlid** (Eng. lid), OHG (h)lit"
5655: (p. 738). The *lid* case shows retention of *i in OE, OHG, and ON. The proto-form
5656: \*xlidą has velar \*x in initial position.
```

#### Germanic/docs/DEV_NOTES.md:5686 (exact COUNTERPART)

- Nearby heading: #### Assessment: Is onset-velar blocking attested for OE?

```text
5684: Cercignani's claim is specific to Old Icelandic and explicitly denied for OHG. Our
5685: hypothesis that onset velars block i-lowering in OE would be a **novel extension**
5686: of the literature, supported by the data (OE hlid retains *i) but not explicitly
5687: attested in prior scholarship.
5688: 
```

#### Germanic/docs/DEV_NOTES.md:5744 (exact COUNTERPART)

- Nearby heading: #### Test cases

```text
5742: | nest | No | No | Lower | nest ✓ |
5743: | wether | No (*w is labial) | No | Lower | weþer ✓ |
5744: | lid | **Yes** (\*x) | No | Block | hlid ✓ |
5745: | fright | **Yes** (\*x) | No | Block | fyrhtu ✓ |
5746: | fish | No | **Yes** (\*k) | Block | fisċ ✓ |
```

#### Germanic/docs/DEV_NOTES.md:5783 (exact COUNTERPART)

- Nearby heading: #### Results

```text
5781: | \*nistą | nist | **nest** | nest | ✓ Fixed (coronal coda, no onset velar) |
5782: | \*wiθră | wiþer | **weþer** | weþer | ✓ Fixed (coronal coda, no onset velar) |
5783: | \*xlidą | hled | **hlid** | hlid | ✓ Fixed (onset *x blocks) |
5784: | \*furxtiθō | forhteþu | **fyrhtu** | fyrhtu | ✓ Fixed (earlier *x blocks) |
5785: | \*fiskăz | fisċ | fisċ | fisċ | ✓ No change (velar *k in coda) |
```

### Analysis and dossier hits

#### Germanic/docs/analysis/notable_findings.md:1126 (exact COUNTERPART)

- Nearby heading: ## 7. NWGmc *i > *e lowering: consonant-conditioned blocking and rule ordering

```text
1125:    i-lowering in Old English:
1126:    - \*xlidą → OE *hlid* (not \**hled*) — onset \*x blocks
1127:    - \*furxtiθō → OE *fyrhtu* (not \**forhteþu*) — earlier \*x blocks
```

#### Germanic/docs/analysis/notable_findings.md:1154 (exact COUNTERPART)

- Nearby heading: ## 7. NWGmc *i > *e lowering: consonant-conditioned blocking and rule ordering

```text
1153: **Results (2026-03-09):** Implementing onset-velar blocking yielded +2 matches
1154: (297 → 299), fixing *lid* (\*xlidą → hlid) and *fright* (\*furxtiθō → fyrhtu)
1155: without regressions. This confirms the onset-velar blocking hypothesis.
```

#### Germanic/docs/analysis/notable_findings.md:1205 (exact COUNTERPART)

- Nearby heading: ### Expert consultation (Stefan Schuhmacher, Vienna, 2026-03-20)

```text
1204: of onset-velar blocking to OE is **our own hypothesis**, supported by OE data
1205: (hlid, fyrhtu) but not stated anywhere in Cercignani. The phrasing "extension of
1206: Cercignani 1980" in our earlier notes was correct but potentially misleading—it
```

### Local lexical-table hits

#### old_english_wiktionary.tsv

| ENGLISH | OE_FORM | SOURCE | DETAIL | PAGE |
| :--- | :--- | :--- | :--- | :--- |
| lid | hlid | inh | template:inh | lid |

#### old_english_swadesh.tsv

_None_

## Possibly stale or diagnostic evidence

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:5621 (concept name)

- Nearby heading: ### Refined analysis: onset velars also block i-lowering (2026-03-09 continued)

```text
5619: ### Refined analysis: onset velars also block i-lowering (2026-03-09 continued)
5620: 
5621: After discovering that our implementation caused 2 regressions (fright, lid) while
5622: fixing 2 words (nest, wether), we investigated the consonant environments more
5623: carefully.
```

#### Germanic/docs/DEV_NOTES.md:5655 (concept name)

- Nearby heading: #### Lloyd (1966): OE hlid retains *i, but why?

```text
5653: Lloyd lists words that retain *i across dialects: "OE fisc, OHG, OS fisk, ON fiskr;
5654: OE, OS witan, ON vita, OHG wizzan; ON hliþó, **OE hlid** (Eng. lid), OHG (h)lit"
5655: (p. 738). The *lid* case shows retention of *i in OE, OHG, and ON. The proto-form
5656: \*xlidą has velar \*x in initial position.
5657: 
```

#### Germanic/docs/DEV_NOTES.md:5792 (concept name)

- Nearby heading: #### Results

```text
5790: - Baseline: 297/386 matches (76.9%)
5791: - After onset-velar blocking: **299/386 matches (77.5%)**
5792: - Net gain: **+2 matches** (lid, fright fixed; no regressions)
5793: 
5794: #### Theoretical significance
```

### Analysis and dossier hits

_None_

## Bibliography-key candidates

### Preferred candidates

| Key | Why it was selected |
| :--- | :--- |
| Lloyd1966 | author + year mention (Lloyd 1966) |
| Cercignani1980 | author + year mention (Cercignani 1980) |

### Low-confidence candidates

| Key | Why it was selected |
| :--- | :--- |
| LloydSpringer1988 | surname mention only: Lloyd |
| Cercignani1979 | surname mention only: Cercignani |

