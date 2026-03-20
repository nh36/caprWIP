# Major Discoveries and Open Questions

This file documents significant findings, puzzles, and unresolved questions 
encountered during the FST development. These are cases where the literature 
is unclear, contradictory, or where we've identified issues requiring further 
specialist research.

---

## 1. þistel (thistle) — Root Vowel Controversy (2026-03-19)

**The Puzzle:**
For OE `þistel` 'thistle', the root vowel is disputed:
- **PGmc `*þistilaz`** (with *i): Kroonen, Kluge-Seebold (primary reconstruction)
- **PGmc `*þestel-`** (with *e): R/T vol.1 §87, some scholars

**The Problem:**
Those who reconstruct `*þestellaz` (with *e) cannot explain how the vowel becomes OE `i`:
- There is no regular OE sound change raising `*e` → `i` before `st` clusters
- No conditioning environment (i-umlaut, raising before nasals, etc.) applies here
- Kroonen explicitly states: "The e-vocalism in the reconstruction is unexplained"

**FST Decision:**
We use `*þistilaz` (with *i) following Kroonen and K-S, which correctly yields `þistel`.

**Flag:**
We do not understand how scholars who reconstruct *e in the root vowel make the phonology work. This requires further specialist literature research.

**See:** DEV_NOTES.md section "þistel 'thistle': Etymology Research and Source Verification"

---

## 2. wīþiġ (withy) — ja-stem vs. -ig Suffix Problem (2026-03-20)

**The Puzzle:**
For OE `wīþiġ` 'withy, willow', no standard ja-stem reconstruction yields the attested form:
- **Wiktionary/TSV:** `*wīþijaz`
- **Kluge-Seebold:** `*wīþja/ō`

**The Problem:**
According to Adamczyk 2001 on OE reflexes of Sievers' Law, heavy monosyllabic ja-stems 
produce OE **`-e`**, not `-ig`:
- `*andijaz` → OE `ende` 'end'
- `*witijam` → OE `wite` 'punishment'  
- `*linþijaz` → OE `līðe` 'gentle'

Therefore `*wīþijaz` (heavy monosyllable) should yield OE `*wīþe` or `*wīþ`, **NOT** `wīþig`.

**Possible Explanations (none confirmed by sources):**
1. Different suffix: `*wīþigaz` or `*wīþagaz` (with *-iga-/*-aga- suffix) — but no source attests this
2. Analogical restoration: productive OE `-ig` suffix restored after regular phonological loss
3. Late formation: post-PGmc derivative `*wīþ-` + OE `-ig`
4. Kluge-Seebold's speculative `*wīþw-` stem (based on non-Gmc cognates like Gk ἰτέα, OPruss *witwan*)

**FST Behavior:**
Pipeline correctly produces `wīþ` from `*wīþijaz` — the Sievers' Law syncope and 
j-loss rules are working as they should. The problem is finding a proto-form that 
yields the attested `wīþig`.

**Flag:**
No authoritative source provides a proto-form that directly yields OE `wīþig` through 
regular sound change. The word requires further specialist research.

**Sources Consulted:**
- Campbell §576 (ja-nouns), §376 (-ig suffix)
- Kluge-Seebold "Weide 1" entry
- Kroonen (no entry for this word)
- R/T vol.2 p.70 (ja-stem overview)
- Bülbring §327
- Adamczyk 2001 "Old English reflexes of Sievers' Law"
- Erdmann 1972 "Suffixal j in Germanic"
- Pierce 1999, 2003, 2006 (Sievers' Law studies)

**See:** DEV_NOTES.md section "OE wīþiġ 'withy': ja-stem Adjective vs Sievers' Law Syncope"

---

*Last updated: 2026-03-20*
