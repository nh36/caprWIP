# Evidence packet — 2204 spar / spearra

> This packet is evidence for drafting. Do not treat all hits as equally authoritative; prefer high-confidence evidence.

## TSV row data

| ID | CONCEPT | COUNTERPART | PROTO | PROTOFORM | DERIVATION_CLASS | NOTE | HISTORY |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2204 | spar | spearra | *spárrô | *spárrô | regular | Kroonen *sparran- m. 'rafter, spar' → OE spearra m.; sperran is the verb 'to bar' | - |

## Manifest status

_No manifest entry._

## High-confidence evidence

### Compact derivation trace entry

```md
# spar
PROTO: *spárrô
EXPECTED: spearra
OUTPUTS: spearra



### Proto-Germanic consonant inheritance

Proto Input: *spárrô

| Earlier Germanic developments | Old English developments |
|:---|:---|
| **Proto-West Germanic**<br>[no change]<br><br>**Northwest Germanic**<br>[no change] | **Old English**<br>Anglo Frisian Brightening: *spærrô<br>OE Breaking: *spearrô<br>OE Unstressed Long Vowel Shortening: *spearra |



### Orthography & surface

Outcome: spearra

NOTE: Kroonen *sparran- m. 'rafter, spar' → OE spearra m.; sperran is the verb 'to bar'
```

### Matching oe_known_problems.tsv entries

_None_

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:30633 (exact pair)

- Nearby heading: ##### Words in the TSV with proto *-aCl-* or *-aCr-* before a back-vowel tail

```text
30631: | 2166 | *sáltą | sealt | breaking |
30632: | 2167 | *sálbō | sealf | breaking |
30633: | 2204 | *spárrô | spearra | breaking + geminate *rr* |
30634: | 2240 | *táppô | tæppa | geminate *pp*, no back-vowel-after-cluster issue (NomSg cluster) |
30635: | 2250 | *θístilas | þistles | (gen.sg., resolved in §17.18.7) |
```

### Analysis and dossier hits

_None_

## Supporting/background evidence

### DEV_NOTES hits

_None_

### Analysis and dossier hits

#### Germanic/docs/analysis/arestoration_r_l_research.md:531 (exact COUNTERPART)

- Nearby heading: ## 8. FST probing results (verbatim)

```text
530: $ echo 'spárrô' | flookup -i old_english.bin
531: spárrô	spearra       # OK — breaking before geminate *rr (Luick §161.2 exclusion)
532: 
```

### Local lexical-table hits

#### old_english_wiktionary.tsv

| ENGLISH | OE_FORM | SOURCE | DETAIL | PAGE |
| :--- | :--- | :--- | :--- | :--- |
| spar | sperran | der | template:der | spar |

#### old_english_swadesh.tsv

_None_

## Possibly stale or diagnostic evidence

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:37760 (concept name)

- Nearby heading: ## §17.32 — *spárēną / sparian closure (row 2205): TSV PROTOFORM switch to class-II *spárōjaną

```text
37758: **Date:** 2026-04-26.
37759: **Status:** TSV-only closure (Plan A), gated on §17.25 phonology fix.
37760: **Dossiers:** `Germanic/docs/dossier-spar-2025.md`, `Germanic/docs/dossier-spar-apocope-2025.md`.
37761: 
37762: ### §17.32.1 Context — what §17.25 established and what was deferred
```

#### Germanic/docs/DEV_NOTES.md:37807 (concept name)

- Nearby heading: ### §17.32.3 Authority survey for the *spar- verb

```text
37805: the only thing missing is the TSV PROTOFORM switch.
37806: 
37807: ### §17.32.3 Authority survey for the *spar- verb
37808: 
37809: | Source | Reconstruction | Page / § |
```

#### Germanic/docs/DEV_NOTES.md:37855 (concept name)

- Nearby heading: ### §17.32.6 Plan-A rationale — why no Anglian relic is admissible

```text
37853: WS infinitive? Two deep-research dossiers were prepared:
37854: 
37855: - `dossier-spar-2025.md` — paradigm-cell survey (Kroonen p. 465, Orel
37856:   p. 363, R/T p. 162, p. 191, Kluge–Seebold p. 859, Campbell §764,
37857:   Brunner §415).
```

#### Germanic/docs/DEV_NOTES.md:37858 (concept name)

- Nearby heading: ### §17.32.6 Plan-A rationale — why no Anglian relic is admissible

```text
37856:   p. 363, R/T p. 162, p. 191, Kluge–Seebold p. 859, Campbell §764,
37857:   Brunner §415).
37858: - `dossier-spar-apocope-2025.md` — OE final-vowel apocope literature
37859:   (Brunner §150, Campbell §766, R/T §6.5–6.6, Fulk §3.20, Hogg-CHEL).
37860: 
```

#### Germanic/docs/DEV_NOTES.md:37871 (concept name)

- Nearby heading: ### §17.32.6 Plan-A rationale — why no Anglian relic is admissible

```text
37869: | `spærede` (Rit. past) | none — pgrmWord has no class-III past slot, and no coherent input is reconstructable | **hybrid past**, levelling |
37870: | `spearad` (VP 3sg) | none — back mutation is not in the cascade for class-II 3sg; apply-up demands pre-broken `*spea-` input | not derivable without new machinery |
37871: | `spæreþ` (cl-III 3sg, Anglian *type* per Campbell §766) | `*spárēθi → spæreþ` ✓ via existing pgrmWeakTailVowel cell (line 435) | **lautgesetzlich but `spæreþ` is unattested** for *spar-* |
37872: | `spære` (cl-III imper.sg) | `*spárē → spære` ✓ | **lautgesetzlich but `spære` is unattested** (verified against Bosworth-Toller, Clark Hall, Brunner paradigm tables) |
37873: 
```

#### Germanic/docs/DEV_NOTES.md:37874 (concept name)

- Nearby heading: ### §17.32.6 Plan-A rationale — why no Anglian relic is admissible

```text
37872: | `spære` (cl-III imper.sg) | `*spárē → spære` ✓ | **lautgesetzlich but `spære` is unattested** (verified against Bosworth-Toller, Clark Hall, Brunner paradigm tables) |
37873: 
37874: The decisive negative finding (dossier-spar-apocope §1) is **Brunner
37875: §150**: "Ein Abfall anderer Endsilbenvokale … findet im Ae. nicht
37876: statt … insbesondere bleiben erhalten: auslautende -e (für älteres -i
```

### Analysis and dossier hits

#### Germanic/docs/analysis/arestoration_r_l_research.md:741 (exact pair)

- Nearby heading: ## 11. Affected TSV rows

```text
740: | 2167 | `*sálbō` | `sealf` | breaking |
741: | 2204 | `*spárrô` | `spearra` | breaking before geminate *rr* (Luick §161.2 exclusion) |
742: | 2205 | `*spárēną` | `sparian` | **partial fix** — see below |
```

## Bibliography-key candidates

### Preferred candidates

| Key | Why it was selected |
| :--- | :--- |
| Kroonen2013 | default Proto-Germanic etymology key for Kroonen |
| Luick1914 | single available key for Luick |

### Low-confidence candidates

| Key | Why it was selected |
| :--- | :--- |
| Kroonen2011 | surname mention only: Kroonen |
| Kroonen2006 | surname mention only: Kroonen |

