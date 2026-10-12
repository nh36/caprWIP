# Evidence packet — 1961 bow / bīeġan

> This packet is evidence for drafting. Do not treat all hits as equally authoritative; prefer high-confidence evidence.

## TSV row data

| ID | CONCEPT | COUNTERPART | PROTO | PROTOFORM | DERIVATION_CLASS | NOTE | HISTORY |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1961 | bow | bīeġan | *báugijaną | *báugijaną | regular | Kroonen *baugjan- wv. 'to (make) bend' → OE bīeġan; boga is the noun *bugan- | - |

## Manifest status

_No manifest entry._

## High-confidence evidence

### Compact derivation trace entry

```md
# bow
PROTO: *báugijaną
EXPECTED: bīeġan
OUTPUTS: bīeġan



### Proto-Germanic consonant inheritance

Proto Input: *báugijaną

| Earlier Germanic developments | Old English developments |
|:---|:---|
| **Proto-West Germanic**<br>[no change]<br><br>**Northwest Germanic**<br>[no change] | **Old English**<br>OE Au Fronting: *báeugijaną<br>OE Diphthong Leveling: *bēagijaną<br>OE Heavy Syllable Nasal Apocope: *bēagijan<br>OE Secondary Nasalization: *bēagijąn<br>Sievers Law Syncope: *bēagjąn<br>OE Velar Palatalization: *bēaʤjąn<br>OE I Umlaut: *bīeʤjąn<br>OE Weak Tail Reduction: *bīeʤjan<br>OE J Loss After Heavy: *bīeʤan |



### Orthography & surface

Old English Orthography: *bīeġan
Outcome: bīeġan

NOTE: Kroonen *baugjan- wv. 'to (make) bend' → OE bīeġan; boga is the noun *bugan-
```

### Matching oe_known_problems.tsv entries

_None_

### DEV_NOTES hits

_None_

### Analysis and dossier hits

#### Germanic/docs/dossiers/bugan-scufan-paradigm-cell-review.md:404 (row ID)

- Nearby heading: ### §7.1 *būgan* (row 1962)

```text
403:   in row 1963 (`*búgô / boga`, the noun 'bow (curve)'), and a
404:   Class-I weak causative in row 1961 (`*báugijaną / bīeġan` 'to
405:   make bend'); adding a fourth cell here would mean the cogset
```

## Supporting/background evidence

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:1753 (exact COUNTERPART)

- Nearby heading: ## A-Restoration Fix (2026-02-06)

```text
1751:   - Standard descriptions show WGmc **gemination before *j** in short stems and **i‑mutation following *i/*j**, with classic paths like *satjan > *sattjan > *sættjan > *settian > OE settan; palatalization of velars by *j precedes i‑mutation in the usual OE chronology. Sources: Hasenfratz appendices (WVU “Reading Old English”) and the OE phonological history summary citing Campbell.
1752:   - Implementation aligned to this: allow **palatalized consonants** (ʤ/ʧ/ʃ/ç/ʒ/j) to count as intervening segments for i‑umlaut so raising can apply **after palatalization** rather than being blocked by non‑star symbols.
1753:   - Result: *xagjăz → **heġġ** and *sangjăną → **senġan** in `oe_full_trace_report_2026-01-22g.txt`; *baugjăną still mispredicts `bīeġan` (see final_vowel_missing bucket).
1754: - OE epenthesis update (2026-01-04):
1755:   - Epenthesis is now a real phonological stage **before** star removal and appears in the full trace.
```

#### Germanic/docs/DEV_NOTES.md:8980 (exact COUNTERPART)

- Nearby heading: ### Evidence from Ringe & Taylor (2014) Vol.2

```text
8978: | `*sōkijăną` | `*sōkijană` | sēċan | p.157: "PGmc *sōkijană 'to look for, to seek'" |
8979: | `*galaubijăną` | `*galaubijana` | ġelīefan | p.245: "PGmc *galaubijana 'to believe'" |
8980: | `*baugijăną` | `*baugijana` | bīeġan | p.158: "PNWGmc *baugijana 'to bend (it)'" |
8981: | `*laistijăną` | `*laistijana` | lǣstan | p.231: "PGmc *laistijana 'to follow'" |
8982: | `*laidijăną` | `*laidijană` | lǣdan | p.229: "PGmc *laidijană 'to make go'" |
```

### Analysis and dossier hits

_None_

### Local lexical-table hits

#### old_english_wiktionary.tsv

| ENGLISH | OE_FORM | SOURCE | DETAIL | PAGE |
| :--- | :--- | :--- | :--- | :--- |
| bow | boga | inh | template:inh | bow |

#### old_english_swadesh.tsv

_None_

## Possibly stale or diagnostic evidence

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:1462 (concept name)

- Nearby heading: ## Project Status (as of 2026-04-30) — research phase complete

```text
1460:   (`widuwe-u-preservation.md` Appendix D, `un-to-on-chronology.md`,
1461:   `bugun-scufun-attestation.md`, `bugan-scufan-paradigm-cell-review.md`),
1462:   and retargeted the bow/shove cogset rows from 3pl pret. (analogical
1463:   overlay) to 1/3 sg pret. (genuinely Lautgesetzlich + universally
1464:   attested: `*báug → bēag`, `*skáub → sċēaf`).
```

#### Germanic/docs/DEV_NOTES.md:14363 (concept name)

- Nearby heading: ### The Problem

```text
14361: | Proto | FST Output | Expected | Gloss |
14362: |-------|------------|----------|-------|
14363: | `*beugăną` | `bēogan` | `būgan` | 'to bow, bend' |
14364: | `*skeubăną` | `sċēofan` | `sċūfan` | 'to shove' |
14365: | `*newun` | `nēowon` | `nigon` | 'nine' |
```

#### Germanic/docs/DEV_NOTES.md:14417 (concept name)

- Nearby heading: #### Kroonen (Etymological Dictionary)

```text
14415: 
14416: For *beugan- ~ *būgan- (s.v.):
14417: > "*beugan- ~ *būgan- s.v. 'to bow, bend' — Go. *biugan* s.v. 'id.', ON *bjūga* s.v. 
14418: > 'id.', ... OE *būgan* s.v. 'to bend', ... OHG *biogan* s.v. 'to bend, swing'"
14419: 
```

#### Germanic/docs/DEV_NOTES.md:14489 (concept name)

- Nearby heading: #### Results: Past plural and PPP ARE lautgesetzlich

```text
14487: 
14488: **Kroonen** (s.v. *beugan-):
14489: > "*beugan- ~ *būgan- s.v. 'to bow, bend'"
14490: 
14491: Kroonen lists both variants, showing that `*būgan-` (with long `ū`) coexisted 
```

#### Germanic/docs/DEV_NOTES.md:26621 (exact pair)

- Nearby heading: ### §17.10.35 *wīθijaz → wīþ (expected wīþiġ): wrong suffix etymology

```text
26619:   Row  PROTOFORM         Current FST    Target           Status
26620:   ──── ───────────────── ─────────────  ─────────────── ─────────────
26621:   1961 *báugijaną        bīeġan         bīeġan          ✓ already correct
26622:                                                           (via existing *gj→ʤ)
26623:   1976 *kéwwaną          ċēowan         ċēowan          ✓ no *j present
```

#### Germanic/docs/DEV_NOTES.md:26648 (exact PROTOFORM)

- Nearby heading: ### §17.10.35 *wīθijaz → wīþ (expected wīþiġ): wrong suffix etymology

```text
26646:     *aww-, *eww- verbs and *Vw- nouns), or *ō intervenes between *w
26647:     and *j (Class II *-ōjan-), or the form is already handled by an
26648:     existing rule (*gj→ʤ for *báugijaną).
26649: 
26650: Rule scope
```

#### Germanic/docs/DEV_NOTES.md:26682 (row ID)

- Nearby heading: ### §17.10.35 *wīθijaz → wīþ (expected wīþiġ): wrong suffix etymology

```text
26680:   Class II verbs  *skáwōjaną (row 2186) — *ō between        VERY LOW
26681:                   *w and *j blocks rule                     (rule won't fire)
26682:   Class I *gj/*kj *báugijaną (row 1961) — already handled   NONE (different
26683:                   by existing *gj→ʤ; rule is *aw+j only      input shape)
26684:   Class VII       *kéwwaną, *xáwwaną — no *j present         NONE
```

#### Germanic/docs/DEV_NOTES.md:42903 (concept name)

- Nearby heading: ## 3. Parallel forms in OE (and northern WGmc)

```text
42901: 
42902: OE doublets that may show synchronic /w/~/g/ alternation (cf. Hall: "nig- = niw-"):
42903: - *niwian / nigan* 'to bow, incline' (Holthausen treats as one verb)
42904: - *nēowol / nigol* 'prone' — though here *nēowol* is the standard form
42905: - *frēa-* compounds vs. occasional *frīga-* in proper names (Frīgedæg 'Friday' < \*Frijjō; different etymon, but illustrative)
```

#### Germanic/docs/DEV_NOTES.md:43938 (concept name)

- Nearby heading: #### §17.51.A1.4 — Paradigm-cell review and retargeting (būgan, sċūfan)

```text
43936: 
43937: Following the open question raised at the end of §17.51.A1.3, a
43938: paradigm-cell review was carried out for *būgan* 'to bow, bend' and
43939: *sċūfan* 'to shove, push'. The full investigation is recorded in
43940: `Germanic/docs/dossiers/bugan-scufan-paradigm-cell-review.md`
```

### Analysis and dossier hits

#### Germanic/docs/analysis/final_vowel_missing_analysis.md:67 (concept name)

- Nearby heading: ### Example: `*baugjăną` → expected `boga`

```text
66: - `*baugjăną` is an **infinitive** (class II weak verb: *-ōjan-)
67: - Expected `boga` is a **noun** (bow)
68: - These are completely different lexemes/forms - likely a **TSV data error**
```

#### Germanic/docs/dossiers/bugun-scufun-attestation.md:13 (concept name)

- Nearby heading: ## Question

```text
12: **lexeme-specific** question: is the 3 pl. pret. of *bēogan / búgan*
13: 'to bow' actually attested anywhere in the OE corpus as `bugun`, and
14: is the 3 pl. pret. of *sċūfan* 'to shove' actually attested as
```

#### Germanic/docs/dossiers/bugun-scufun-attestation.md:86 (concept name)

- Nearby heading: ### Local handbook evidence

```text
85: 
86: > "bugan (bow)   bȳhþ   beag   **bugon**   bogen"
87: 
```

## Bibliography-key candidates

### Preferred candidates

| Key | Why it was selected |
| :--- | :--- |
| Kroonen2013 | default Proto-Germanic etymology key for Kroonen |
| Campbell1959 | single available key for Campbell |

### Low-confidence candidates

| Key | Why it was selected |
| :--- | :--- |
| Kroonen2011 | surname mention only: Kroonen |
| Kroonen2006 | surname mention only: Kroonen |

