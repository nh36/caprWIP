# Evidence packet — 2234 swallow / swealwe

> This packet is evidence for drafting. Do not treat all hits as equally authoritative; prefer high-confidence evidence.

## TSV row data

| ID | CONCEPT | COUNTERPART | PROTO | PROTOFORM | DERIVATION_CLASS | NOTE | HISTORY |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2234 | swallow | swealwe | *swálwōn | *swálwōn | regular | Kroonen *swalwōn- f. 'swallow (bird)' → OE swealwe f.; swelgan is the verb 'to swallow' | TSV fix: proto *swalgwōn → *swalwōn (Kroonen *swalwōn-, R/T *swalwa; no *g in this etymology, confused with *swelganą to swallow). |

## Manifest status

_No manifest entry._

## High-confidence evidence

### Compact derivation trace entry

```md
# swallow
PROTO: *swálwōn
EXPECTED: swealwe
OUTPUTS: swealwe



### Proto-Germanic consonant inheritance

Proto Input: *swálwōn

| Earlier Germanic developments | Old English developments |
|:---|:---|
| **Proto-West Germanic**<br>[no change]<br><br>**Northwest Germanic**<br>NWGmc N Stem N Loss: *swálwǭ | **Old English**<br>Anglo Frisian Brightening: *swælwǭ<br>OE Breaking: *swealwǭ<br>OE Unstressed Long Vowel Shortening: *swealwæ<br>OE Unstressed AE Merger: *swealwe |



### Orthography & surface

Outcome: swealwe

NOTE: Kroonen *swalwōn- f. 'swallow (bird)' → OE swealwe f.; swelgan is the verb 'to swallow'
```

### Matching oe_known_problems.tsv entries

_None_

### DEV_NOTES hits

_None_

### Analysis and dossier hits

_None_

## Supporting/background evidence

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:3088 (exact COUNTERPART)

- Nearby heading: ### The problem

```text
3086: Three mismatch items involved PGmc *gw clusters from labiovelars:
3087: - *snaigwăz → snāgw (expected snāw): cons_mismatch__g_vs_w
3088: - *swalgwōn → swealgwe (expected swealwe): cons_mismatch__g_vs_w
3089: - *singwăną → singwan (expected singan): cons_mismatch__w_vs_n
3090: - Also *θegnăz → þeġn (expected þæġn): vowel_quality__ae_e_alternation
```

#### Germanic/docs/DEV_NOTES.md:3108 (exact COUNTERPART)

- Nearby heading: ### Analysis of *gw developments

```text
3106: 1. After nasal (*ngw): *g = stop [g], so *w is lost → *ng (singan, stincan)
3107: 2. Post-vocalic (*Vgw): *g = fricative [ɣ], so *g is lost → *Vw (snāw)
3108: 3. After liquid (*lgw): same as post-vocalic → *lw (swealwe)
3109: 
3110: For cases 2-3, we corrected the TSV proto-forms to remove the spurious *g.
```

#### Germanic/docs/DEV_NOTES.md:3850 (exact COUNTERPART)

- Nearby heading: ### Case 3: \*flaskō → \*flaskōn (OE flasce 'flask, bottle')

```text
3848: | \*flaskōn | flæsċe | flasce | flasce | **fixed** |
3849: | \*wartōn | wearte | wearte | wearte | unchanged (\*r blocks) |
3850: | \*swalwōn | swealwe | swealwe | swealwe | unchanged (\*l blocks) |
3851: | \*sapōn | sæpe | sape | sæp | bucket change (pre-existing length issue) |
3852: | \*xertōn | heorte | heorte | heorte | unchanged (\*e root) |
```

### Analysis and dossier hits

#### Germanic/docs/analysis/arestoration_r_l_research.md:534 (exact COUNTERPART)

- Nearby heading: ## 8. FST probing results (verbatim)

```text
533: $ echo 'swálwōn' | flookup -i old_english.bin
534: swálwōn	swealwe       # OK — breaking before *lw
535: 
```

### Local lexical-table hits

#### old_english_wiktionary.tsv

| ENGLISH | OE_FORM | SOURCE | DETAIL | PAGE |
| :--- | :--- | :--- | :--- | :--- |
| swallow | swelgan | inh | template:inh | swallow |

#### old_english_swadesh.tsv

_None_

## Possibly stale or diagnostic evidence

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:3096 (concept name)

- Nearby heading: ### Research

```text
3094: **Snow (*snaigwăz → *snaiwăz):** Both Kroonen (p.460, *snaiwa-) and R/T (p.171, *snaiwaz) reconstruct PGmc with *w, not *gw. There was never a labiovelar in this word. The TSV proto was simply wrong, likely from automated extraction confusion.
3095: 
3096: **Swallow (*swalgwōn → *swalwōn):** Kroonen (p.495, *swalwōn-) and R/T (p.185, PWGmc *swalwa) both reconstruct without *g. The TSV proto was confused with the verb *swelganą 'to swallow (food)' — the bird name has no etymological *g.
3097: 
3098: **Sing (*singwăną):** This genuinely had a PGmc labiovelar *g^w (Kroonen p.437, *singwan-; R/T p.215, *sing^wanan). After PWGmc labiovelar resolution (R/T §3.1.3), the cluster became *ngw. Then per R/T §6.4.2, *w was lost after non-initial velars: *singwan → singan.
```

#### Germanic/docs/DEV_NOTES.md:3117 (concept name)

- Nearby heading: ### Implementation

```text
3115: **Rule:** `OEPostVelarWLoss` — `{*w} → 0 || {*n} {*g} _`
3116: **Pipeline position:** After OEVelarPalatalization (per R/T chronology)
3117: **TSV changes:** snow, swallow protos corrected; thane target corrected
3118: **New weak tail:** w:{*w} ō:{*ō} n:{*n} added for *swalwōn
3119: 
```

### Analysis and dossier hits

#### Germanic/docs/analysis/arestoration_r_l_research.md:743 (exact pair)

- Nearby heading: ## 11. Affected TSV rows

```text
742: | 2205 | `*spárēną` | `sparian` | **partial fix** — see below |
743: | 2234 | `*swálwōn` | `swealwe` | breaking before *lw* |
744: | 2269 | `*wárpą` | `wearp` | breaking |
```

#### Germanic/docs/dossiers/widuwe-u-preservation.md:88 (concept name)

- Nearby heading: #### §365 — parasite vowel `-uw-` lowers

```text
87: > praise, … *gearuwe* n.p. ready, **beaduwe** d.s. battle,
88: > **seonuwa** n.p. sinews, *swaluwe* swallow. *ij* can be
89: > monophthongized to *i* … . **By §§ 373, 385, *u* often appears as
```

#### Germanic/docs/dossiers/widuwe-u-preservation.md:426 (concept name)

- Nearby heading: ## §5. Regression watchlist

```text
425:   `swaluwan`, `gearuwe` are present as OE entries — the TSV
426:   entries for `battle`, `sinew`, `swallow`, `ready` either don't
427:   exist or use different paradigm cells).
```

#### Germanic/docs/dossiers/widuwe-u-preservation.md:445 (concept name)

- Nearby heading: ## §5. Regression watchlist

```text
444: | oblique of *badwō ('battle') | beadowe ~ beaduwe | only beaduwe (Campbell §365 says beadowe is regular) |
445: | oblique of *swalwōn ('swallow') | swalewan ~ swaluwan | only swaluwan |
446: | oblique of *sinwō ('sinew') | seonowa ~ seonuwa | only seonuwa |
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

