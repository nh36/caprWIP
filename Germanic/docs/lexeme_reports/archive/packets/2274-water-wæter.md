# Evidence packet — 2274 water / wæter

> This packet is evidence for drafting. Do not treat all hits as equally authoritative; prefer high-confidence evidence.

## TSV row data

| ID | CONCEPT | COUNTERPART | PROTO | PROTOFORM | DERIVATION_CLASS | NOTE | HISTORY |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2274 | water | wæter | *wátną | *wátōr | early_analogy | Kroonen *watar-/*watan- r/n-stem, nom.sg. *watōr; R/T §3.1.4 *ō→*a before final *r in PWGmc. | Source: Wiktionary Old English Swadesh list (retrieved 2025-12-12) \| Source: Wiktionary etymology (template:inh) \| Source: Wiktionary etymology (template:inh) \| TSV fix: proto *watną → *watōr. |

## Manifest status

_No manifest entry._

## High-confidence evidence

### Compact derivation trace entry

```md
# water
PROTO: *wátōr
EXPECTED: wæter
OUTPUTS: wæter



### Proto-Germanic consonant inheritance

Proto Input: *wátōr

| Earlier Germanic developments | Old English developments |
|:---|:---|
| **Proto-West Germanic**<br>PWGmc Final Or Lowering: *wátar<br><br>**Northwest Germanic**<br>[no change] | **Old English**<br>Anglo Frisian Brightening: *wætær<br>OE Unstressed AE Merger: *wæter |



### Orthography & surface

Outcome: wæter

NOTE: Kroonen *watar-/watan- r/n-stem, nom.sg. *watōr; R/T §3.1.4 *ō→a before final *r in PWGmc.
```

### Matching oe_known_problems.tsv entries

_None_

### DEV_NOTES hits

_None_

### Analysis and dossier hits

_None_

## Supporting/background evidence

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:3123 (exact COUNTERPART)

- Nearby heading: ### Problem

```text
3121: 
3122: ### Problem
3123: PGmc *watōr (r/n-stem nom.sg.; Kroonen *watar-/*watan-) needed to produce OE wæter. Two issues:
3124: 
3125: 1. **PWGmc ō-shortening (R/T §3.1.4):** "Word-finally, and before word-final *r, surviving bimoric long ō-vowels became PWGmc *a." So *watōr → PWGmc *watar.
```

#### Germanic/docs/DEV_NOTES.md:3127 (exact COUNTERPART)

- Nearby heading: ### Problem

```text
3125: 1. **PWGmc ō-shortening (R/T §3.1.4):** "Word-finally, and before word-final *r, surviving bimoric long ō-vowels became PWGmc *a." So *watōr → PWGmc *watar.
3126: 
3127: 2. **A-restoration over-application:** After AFB fronted both *a's in *watar to *æ (giving *wætær), A-restoration incorrectly fired because `{*æ}` was in `OEARestorationTriggerVowel`. This restored stressed *æ → *a, giving "water" instead of "wæter".
3128: 
3129: ### Root cause: {*æ} should NOT trigger A-restoration
```

#### Germanic/docs/DEV_NOTES.md:3147 (exact COUNTERPART)

- Nearby heading: ### Derivation

```text
3145: 
3146: ### Derivation
3147: *watōr → (PWGmc ō-shortening) *watar → (AFB) *wætær → (A-restoration: NO trigger, *æ is not back) *wætær → (§6.9.6 unstressed merger) wæter ✓
3148: 
3149: ### Impact
```

#### Germanic/docs/DEV_NOTES.md:3481 (exact COUNTERPART)

- Nearby heading: #### Why this resolves the exceptionlessness concern

```text
3479: #### Why this resolves the exceptionlessness concern
3480: 
3481: The previous version of these notes worried about the different fates of inherited *-r (preserved in *watōr → wæter) versus inflectional *-z (lost in *-ōz → -e). If rhotacism had applied to final *-z, then inherited *-r and rhotacized *-r (< *-z) would have been phonologically identical at some stage, and their different fates would require a non-phonological (grammatically conditioned) explanation.
3482: 
3483: But since z-loss **preceded** rhotacism, there was **no merger**:
```

#### Germanic/docs/DEV_NOTES.md:3524 (exact COUNTERPART)

- Nearby heading: #### Pipeline trace comparison: inherited *-ōr vs. gen.sg. *-ōz

```text
3522: | After AFB | *wætær | *ræstæ |
3523: | After A-restoration | *wætær (no back trigger) | *ræstæ (no back trigger) |
3524: | After weak-tail reduction | *wæter | *ræste |
3525: | Final OE output | wæter | ræste |
3526: 
```

#### Germanic/docs/DEV_NOTES.md:3525 (exact COUNTERPART)

- Nearby heading: #### Pipeline trace comparison: inherited *-ōr vs. gen.sg. *-ōz

```text
3523: | After A-restoration | *wætær (no back trigger) | *ræstæ (no back trigger) |
3524: | After weak-tail reduction | *wæter | *ræste |
3525: | Final OE output | wæter | ræste |
3526: 
3527: Both root vowels undergo identical treatment (PGmc *a → OE æ via AFB, with no A-restoration because the suffix vowel *-a/*-æ is front). The only output difference is the final consonant: *-r survives as -er, *-z (already lost) is absent giving -e. This reflects different input phonemes, not grammatically conditioned change.
```

### Analysis and dossier hits

#### Germanic/docs/analysis/notable_findings.md:190 (exact COUNTERPART)

- Nearby heading: ## 1. Medial high-vowel syncope: dental-obstruent conditioning

```text
189: it would create a syllable coda with a disfavored sonority sequence, e.g.
190: wæter 'water', bydel (PDE beadle)."
191: 
```

#### Germanic/docs/analysis/notable_findings.md:197 (exact COUNTERPART)

- Nearby heading: ## 1. Medial high-vowel syncope: dental-obstruent conditioning

```text
196: sequencing (stop before lateral); a cluster like *-cl-* (micles) or *-tr-*
197: (betra) does not. Wæter is a light-stem case where the following consonant
198: is *t*, not *l* or *r*, so Kaluza's and Fulk's light-stem restriction
```

#### Germanic/docs/analysis/notable_findings.md:652 (exact COUNTERPART)

- Nearby heading: ## 4. A-restoration trigger set: {*æ} is NOT a trigger

```text
651: then incorrectly fired (because the unstressed *æ was in the trigger set),
652: restoring stressed *æ → *a → "water" instead of correct "wæter".
653: 
```

#### Germanic/docs/analysis/unstressed_e_o_before_r.md:25 (exact COUNTERPART)

- Nearby heading: ## Evidence from R/T §6.9.6

```text
24: - \*hwabar → \*hwæþər → OE **hwæþer** (NOT hwæþor)
25: - \*watar → \*wætər → OE **wæter** (NOT wætor)
26: 
```

#### Germanic/docs/analysis/ws_vs_anglian_dialect_differences.md:536 (exact COUNTERPART)

- Nearby heading: ### Ringe & Taylor §6.5.2 (repo ll. 12601–12674)

```text
535: 
536: R/T's `*æ > e` table (ll. 12619–12636): WS `hwæt, fæt, wæter, fæder, bæc,
537: æfter, hæfde, hreþ, æsce, wæstm, dæg, mæg, sægde` ← → Merc. (VP) `hwet,
```

#### Germanic/docs/dossiers/bugan-scufan-paradigm-cell-review.md:292 (exact COUNTERPART)

- Nearby heading: ### §5.1 Sources for the attested forms

```text
291:   > "**Sceaf** þā mid þām scylde, þæt se sceaft tōbærst, Byrhtnoth."
292:   > "Hē hī tō helle **sceaf** wælgrim wæter, Sat. 26."
293:   and past-ptcp. citations:
```

### Local lexical-table hits

#### old_english_wiktionary.tsv

| ENGLISH | OE_FORM | SOURCE | DETAIL | PAGE |
| :--- | :--- | :--- | :--- | :--- |
| water | wæter | inh | template:inh | water |

#### old_english_swadesh.tsv

| NUMBER | ENGLISH | OLD_ENGLISH | IPA_RAW |
| :--- | :--- | :--- | :--- |
| 150 | water | wæter | /ˈwæter/ |

## Possibly stale or diagnostic evidence

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:47 (concept name)

- Nearby heading: ### Polished analyses (Feb–Mar 2026)

```text
45: - [Cognate set 379 "rock" → corrected to "coat"](#cognate-set-379-rock--corrected-to-coat-rukkăz)
46: - [Labiovelar Proto-Form Corrections](#labiovelar-proto-form-corrections-and-post-velar-w-loss-rt-642)
47: - [Water fix: PWGmc ō-shortening](#water-fix-pwgmc-ō-shortening-and-a-restoration-correction-3a45a8b)
48: - [A-restoration: ræst, tæppa, stemn](#a-restoration-in-ō-stems-and-n-stems-ræst-tæppa-stemn-fronting_missing__afb)
49: - [The stefn/stemn Problem](#the-stefnstemn-problem-local-transponent-decision)
```

#### Germanic/docs/DEV_NOTES.md:1179 (concept name)

- Nearby heading: ### The answer: Kroonen (2006), "Gemination and allomorphy in the Proto-Germanic mn-stems"

```text
1177: 
1178: Kroonen (2006:23) also addresses why some forms show `-n-` instead of `-m-`:
1179: > "Final m was apparently assimilated to n in many languages (Fick 1909: 275): OE *bodan*, OFri. *boden*... ON *botn* is probably due to assimilation too. Alternatively, it can be analyzed as a typical Scandinavian thematization of a secondary n-stem nom. `*budmōn` ~ gen. `*buttnaz` like in *nafn* n. 'name' and *vatn* n. 'water'."
1180: 
1181: **Summary of Kroonen's analysis:**
```

#### Germanic/docs/DEV_NOTES.md:3120 (concept name)

- Nearby heading: ## Water fix: PWGmc ō-shortening and A-restoration correction (3a45a8b)

```text
3118: **New weak tail:** w:{*w} ō:{*ō} n:{*n} added for *swalwōn
3119: 
3120: ## Water fix: PWGmc ō-shortening and A-restoration correction (3a45a8b)
3121: 
3122: ### Problem
```

#### Germanic/docs/DEV_NOTES.md:3144 (concept name)

- Nearby heading: ### Fix

```text
3142: 2. **Added `PWGmcPreFinalRShortening`:** `{*ō} → {*a} || _ {*r} .#.` in PWGmcChanges
3143: 3. **Added `ō:{*ō} r:{*r}` weak tail** for r-stem endings
3144: 4. **TSV:** OE water proto *watną → *watōr (correct PGmc r/n-stem nom.sg.)
3145: 
3146: ### Derivation
```

#### Germanic/docs/DEV_NOTES.md:6122 (concept name)

- Nearby heading: #### Orel (2003) p.279, s.v. `*naþraz`

```text
6120: 
6121: > "*naþraz sb.m.: Goth nadrs 'adder, viper, snake', ON naðr 'viper, adder,
6122: > snake'. Related to Lat natrix 'water snake', OIr nathir id., W neidr 'snake',
6123: > Corn nader id., MBret azr id. See also *nēþrōn ~ *naþrōn."
6124: 
```

### Analysis and dossier hits

#### Germanic/docs/analysis/arestoration_r_l_research.md:137 (concept name)

- Nearby heading: ### 2.2 Ringe & Taylor (2014), *A Linguistic History of English vol. II* — file `ringe_taylor_linguistic_history_vol2.txt`

```text
136: >
137: > PNWGmc *laguz 'water, the sea' … > *lægu > OE **lagu**.
138: >
```

#### Germanic/docs/analysis/arestoration_r_l_research.md:368 (concept name)

- Nearby heading: ### 4.1 Pro-restoration evidence with single intervening *r* or *l* (back vowel triggers)

```text
367: | **magu** 'boy' | *\*maguz → magu* (u-stem) | R/T 11104 |
368: | **lagu** 'water, sea' | *\*laguz → \*lægu → lagu* | R/T 11106 |
369: | **maga** 'stomach' | *\*magō → \*mæga → maga* | R/T 11119 |
```

## Bibliography-key candidates

### Preferred candidates

| Key | Why it was selected |
| :--- | :--- |
| Kroonen2013 | default Proto-Germanic etymology key for Kroonen |
| Kaluza1906 | single available key for Kaluza |
| Fulk2018 | single available key for Fulk |

### Low-confidence candidates

| Key | Why it was selected |
| :--- | :--- |
| Kroonen2011 | surname mention only: Kroonen |
| Kroonen2006 | surname mention only: Kroonen |

