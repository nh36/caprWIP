# Non-Firing FST Rules Analysis — Old English Stack
**Date:** 2026-02-06  
**Baseline:** `oe_mismatch_report_2026-02-06.txt` (282 total mismatches)  
**Status:** Post A-restoration chronology fix (280→282)

**Related Documentation:**
- `docs/germanic_notes/weak_tail_vowels_and_a_restoration.md` — comprehensive analysis of weak-tail triggers and paradigmatic alternations
- `docs/germanic_notes/oe_a_restoration_debug.md` — technical debugging notes

---

## Executive Summary

After fixing the A-restoration foma syntax bug AND implementing the chronology fix (moving apocope after restoration), we have **282 total mismatches** across 14 buckets. 

**Two rules already addressed:**
1. ✅ **LiquidLowering** — commented out (2026-01-27), awaiting final-long-vowel shortening infrastructure
2. ✅ **A-restoration** — fixed foma syntax bug (2026-02-06) AND chronology (apocope moved after restoration)
   - Result: `fronting_missing_no_trigger` improved 11→3 (only Category B words remain)
   - Note: `back_expected_front_out` regressed 4→8 due to **paradigmatic alternation problem** (see weak_tail_vowels_and_a_restoration.md)

---

## Mismatch Bucket → Rule Mapping

| Bucket | Count | Primary Rule(s) Implicated | Status |
|--------|-------|---------------------------|--------|
| **final_vowel_extra** | 56 | OldEnglishWeakTailReduction | ❌ Nucleus not deleted |
| **consonant_mismatch_other** | 40 | Multiple weak-tail + gemination | ❌ Complex interactions |
| **final_vowel_missing** | 34 | Final-long-vowel shortening | ❌ Rule missing |
| **vowel_quality_other** | 23 | Multiple (A-rest, breaking, etc) | ⚠️ Mixed causes |
| **breaking_extra_other** | 23 | EnglishBreaking* | ⚠️ Over-application |
| **breaking_missing** | 19 | EnglishBreakingA (w-context) | ❌ Missing context |
| **length_extra_other** | 17 | Various lengthening/shortening | ⚠️ Mixed causes |
| **palatal_extra_other** | 16 | OldEnglishPalatalisation | ⚠️ Over-application |
| **no_output** | 13 | pgrmWord gate | ❌ Proto gate rejects |
| **fronting_missing_no_trigger** | 11 | OldEnglishARestoration | ⚠️ Still reversing fronting |
| **final_n_missing** | 10 | Infinitive + weak-tail | ❌ -an preservation |
| **palatalization_missing** | 6 | OldEnglishVelarFricativePalatalization | ❌ Wrong chronology |
| **i_umlaut_missing_true** | 4 | OldEnglishIUmlaut | ⚠️ Specific contexts |
| **back_expected_front_out** | 4 | Anglo-Frisian Brightening | ⚠️ Over-application |

---

## Tier 1: Critical Missing Infrastructure (90+ mismatches)

### 1. Final-Long-Vowel Shortening (34 mismatches: final_vowel_missing)

**What it should do:**  
After nominative `-z` apocope, word-final unstressed long vowels shorten.

**Historical phonology:**  
Ringe/Taylor Vol 2 §6.8.3 (lines ~17110–17130): "After apocope of final short high vowels, word‑final unstressed long vowels were shortened."

**Chronology:**  
General syncope → internal long‑vowel shortening → apocope of final short high vowels → **final long‑vowel shortening**

**Current status:**  
Rule does not exist. This blocks revival of `EnglishLiquidLowering` (which creates `*ɔː` that should then shorten).

**Examples from mismatch report:**
```
*kōwz -> cōw (expected cū)     # Final *ō should shorten to *o
*kwiθuz -> cwiþ (expected cudu) # Similar issue
*baugjăną -> bīeġan (expected boga) # Infinitive lost final vowel
```

**Where it should apply:**  
After `OldEnglishHighVowelApocope`, before `OldEnglishWeakTailReduction`

**Proposed implementation:**
```foma
define OldEnglishFinalLongVowelShortening [
  {*ā} -> {*a} ,
  {*ē} -> {*e} ,
  {*ī} -> {*i} ,
  {*ō} -> {*o} ,
  {*ū} -> {*u} ,
  {*ǣ} -> {*æ} ,
  {*ȳ} -> {*y}
] || _ .#. ;
```

**Dependencies:**  
None (foundational rule)

**Estimated effort:** 1-2 hours

---

### 2. Weak-Tail Vowel Nucleus Deletion (56 mismatches: final_vowel_extra)

**What it should do:**  
After weak-tail reduction removes `*ă/*ą` diacritics, the vowel nucleus itself must be deleted in final position.

**Historical phonology:**  
Hogg Vol 1 §3.3.3.2: Late OE reduced vowels merge and are lost via apocope/syncope. Final unstressed syllables typically disappear unless protected by consonants.

**Current status:**  
`OldEnglishWeakTailReduction` changes `{*ă} -> 0` and `{*ą} -> 0` but this only removes diacritic marks, not the vowel slot itself. Result: `*bergą` becomes `*beorga` (with dangling `a`) instead of `beorg`.

**Examples from mismatch report:**
```
*bergą -> beorga (expected beorg)    # Final -a should delete
*blōdą -> blōda (expected blōd)      # Final -a should delete
*burdą -> burda (expected bord)      # Final -a should delete
*būrą -> būra (expected būr)         # Final -a should delete
*braudą -> brēada (expected brēad)   # Final -a should delete
```

**Where it should apply:**  
After `OldEnglishWeakTailReduction`, as part of the weak-tail cleanup sequence

**Root cause diagnosis:**  
The rule targets `{*ă}` and `{*ą}` as multichar symbols, but after stripping the diacritics, a plain `a` or schwa remains. The rule needs a second pass to delete the remaining vowel.

**Proposed implementation:**
```foma
define OldEnglishWeakTailNucleusDeletion [
  [{a} | {e} | {o} | {u}] -> 0 
  || EnglishStarConsonant _ .#.
] ;
```

Or alternatively, combine reduction and deletion:
```foma
define OldEnglishWeakTailReduction [
  {*ă} -> 0 ,
  {*ą} -> 0 ,
  {*ă}{*n} -> {*n} ,
  {*ą}{*n} -> {*n}
] || _ .#. ;
```

**Dependencies:**  
None (but interacts with consonant preservation for infinitives)

**Estimated effort:** 2-3 hours

---

### 3. A-Restoration Context Refinement (11+ mismatches: fronting_missing_no_trigger)

**What it should do:**  
Restore PGmc `*a` when followed by back vowel in next syllable, but ONLY in appropriate morphophonological contexts (not across consonant clusters that block the process).

**Historical phonology:**  
Hogg Vol 1 §5.5.1: A-restoration (also called "back umlaut" or "a-restoration") occurs when PGmc `*a` that has been fronted to OE `æ` is restored to `a` before a back vowel in the following syllable, typically with single intervening consonant.

Ringe/Taylor Vol 2: Notes that the process is sensitive to syllable weight and intervening consonant type. Clusters like `-dr-`, `-st-`, `-rn-` typically do NOT trigger restoration.

**Current status:**  
Fixed foma syntax bug (2026-02-06) but still 11 mismatches. The rule applies in some contexts where it shouldn't.

**Examples from mismatch report:**
```
*bastą -> basta (expected bæst)      # st cluster should block
*baθą -> baþa (expected bæþ)         # Single þ should block? (investigate)
*dranką -> dranca (expected drenċ)   # nc cluster should block
*grasą -> grasa (expected græs)      # s alone should block
*grabăną -> graban (expected græf)   # Complex: infinitive + b
```

**Measured intervening segments (2026-02-05):**
- **True positives** (31 items): `k, w, d, j` (single consonants in back-vowel suffix contexts)
- **False positives** (16 items): `r, s, t, n, p` (singletons or clusters that shouldn't trigger)

**Where it currently applies:**  
After `OldEnglishAngloFrisianBrightening`, before `OldEnglishIUmlaut`

**Proposed refinement:**
The intervening context needs to exclude:
1. Clusters (anything with 2+ consonants)
2. Sibilants and liquids (s, r) which seem to block in the data
3. Weak-tail contexts (already excluded via `OldEnglishARestorationWeakTailVowel`)

Current definition (server/fsts/germanic.txt lines 1142-1148):
```foma
define OldEnglishARestorationIntervening [
  {*k} | {*g} | {*w} | {*d} | {*ð} | {*b} | {*p} | 
  {*f} | {*t} | {*θ} | {*x} | {*h} | {*m} | {*n} |
  {*l} | {*r} | {*s} | {*z} | {*j} | {*ʤ} | {*ʧ}
];
```

**Proposed implementation:**
```foma
# Exclude liquids (l, r) and sibilants (s, z) which block in the data
define OldEnglishARestorationIntervening [
  {*k} | {*g} | {*w} | {*d} | {*ð} | {*b} | {*p} | 
  {*f} | {*t} | {*θ} | {*x} | {*h} | {*m} | {*n} |
  {*j} | {*ʤ} | {*ʧ}
];

# Ensure single consonant only (no clusters)
define OldEnglishARestoration (
  {*æ} -> {*a} || _ 
    OldEnglishARestorationIntervening   # SINGLE consonant
    OldEnglishARestorationBackVowel 
) ;
```

**Dependencies:**  
Interacts with `EnglishAngloFrisianBrightening` (must run after)

**Estimated effort:** 2-3 hours (requires testing against full dataset)

---

## Tier 2: Major Rule Gaps (40-60 mismatches)

### 4. Breaking W-Context Missing (19 mismatches: breaking_missing)

**What it should do:**  
Short vowels break (become diphthongs) before `w` in certain contexts, particularly in weak-tail syllables.

**Historical phonology:**  
Hogg Vol 1 §5.3: Breaking occurs before `h`, `r+consonant`, `l+consonant`, and also **before `w`** in words like PGmc `*fedwōr` → OE `fēower` (four).

**Current status:**  
`EnglishBreakingA` (line 1078) has contexts for `h`, `r+C`, `l+C` but NO `w` context defined.

**Examples from mismatch report:**
```
*fedwōrez -> fedwōre (expected fēower)  # o should break to eo before w
*dawwō -> dawō (expected dēaw)          # a should break to ea before w
*brustz -> brust (expected brēost)      # u-breaking missing (separate issue)
```

**Where it should apply:**  
In `EnglishBreakingLengthening` composition, before `OldEnglishAngloFrisianBrightening`

**Current definition (lines 1078-1100):**
```foma
define EnglishBreakingA [
  {*a} -> {*ea} || _ EnglishBreakingHContext  |
                    _ EnglishBreakingRContext  |
                    _ EnglishBreakingLContext
];

define EnglishBreakingE [
  {*e} -> {*eo} || _ EnglishBreakingHContext         |
                    _ EnglishBreakingXContextNonWeakA |
                    _ EnglishBreakingRContext         |
                    _ EnglishBreakingLContextE
];
```

**Proposed implementation:**
```foma
# Add w-context
define EnglishBreakingWContext [{*w}];

define EnglishBreakingA [
  {*a} -> {*ea} || _ EnglishBreakingHContext  |
                    _ EnglishBreakingRContext  |
                    _ EnglishBreakingLContext  |
                    _ EnglishBreakingWContext    # NEW
];

define EnglishBreakingE [
  {*e} -> {*eo} || _ EnglishBreakingHContext         |
                    _ EnglishBreakingXContextNonWeakA |
                    _ EnglishBreakingRContext         |
                    _ EnglishBreakingLContextE        |
                    _ EnglishBreakingWContext           # NEW
];

define EnglishBreakingO [
  {*o} -> {*eo} || _ EnglishBreakingWContext    # NEW (for *fedwōr)
];

define EnglishBreakingLengthening EnglishBreakingA
  .o. EnglishBreakingE
  .o. EnglishBreakingI
  .o. EnglishBreakingO ;  # Add new rule
```

**Note:** U-breaking (line 39: `*brustz -> brēost`) is a separate issue. Historical sources show this is a different process (possibly West Saxon specific).

**Dependencies:**  
None

**Estimated effort:** 1-2 hours

---

### 5. Velar Fricative Palatalization — Wrong Chronology (6 mismatches: palatalization_missing)

**What it should do:**  
Palatalize velar fricatives `*x → *ç` and `*ɣ → *j` when adjacent to front vowels or `*j`.

**Historical phonology:**  
Hogg Vol 1 §3.3.4.1 (pp. 89-92): /x/ has allophones [h] initially, [x] elsewhere, and [ç] adjacent to front vowels. This is phonemic in early OE but becomes allophonic.

Ringe/Taylor Vol 2 (lines ~1125-1140): "h is [h] word-initially, [ç] after a stressed front vowel, otherwise [x]."

**Current status:**  
`OldEnglishVelarFricativePalatalization` runs **after** `EnglishBreakingLengthening`, but its context is `EnglishStarFrontVowel`, which **excludes breaking diphthongs**. By the time the rule runs, all front vowels have already become diphthongs (`*e → *eo`, `*i → *ie`), so the rule never matches.

**Dataset evidence (2026-01-27):**  
- Stage summary shows **0 hits** for `VelarFricativePalatalization`
- 16 lexemes with `*x` near front vowels, but all show carry-through (no palatalization)
- Example: `*fexu → *feoxu` (breaking already applied) → rule sees `*eo`, not `*e`

**Examples from mismatch report:**
```
*bōkō -> bōcō (expected bēċe)         # k should palatalize to ċ before front vowel
*xunăgą -> hunaga (expected huniġ)    # g should palatalize to ġ
*fleugăną -> flēogan (expected flȳġe) # g should palatalize
```

Note: These examples show VELAR STOP palatalization (`k→ċ`, `g→ġ`), which is `OldEnglishVelarPalatalization`, not fricative palatalization. The fricative rule is also affected by chronology but has no dataset targets (no PGmc `*ɣ` in the OE data).

**Where it currently applies:**  
Line 1412 in the PGmc→OE composition, after `BreakingLengthening`

**Proposed fix:**  
Move `OldEnglishVelarFricativePalatalization` to **before** `EnglishBreakingLengthening`, OR expand its context to include breaking diphthongs:

**Option 1: Reorder (preferred)**
```foma
define EnglishProtoToOE (
  ...
  .o. OldEnglishVelarFricativePalatalization  # MOVE HERE
  .o. EnglishBreakingLengthening
  .o. OldEnglishAngloFrisianBrightening
  ...
) ;
```

**Option 2: Expand context**
```foma
define OldEnglishVelarFricativePalatalizationContext [
  EnglishStarFrontVowel | {*eo} | {*ea} | {*ie}  # Add breaking diphthongs
];

define OldEnglishVelarFricativePalatalization [
  {*x} -> {*ç} || OldEnglishVelarFricativePalatalizationContext _ ,
                  _ OldEnglishVelarFricativePalatalizationContext ;
  {*ɣ} -> {*j} || OldEnglishVelarFricativePalatalizationContext _ ,
                  _ OldEnglishVelarFricativePalatalizationContext
];
```

**Dependencies:**  
Must coordinate with `EnglishBreakingLengthening` chronology

**Estimated effort:** 1 hour (reordering) or 2 hours (context expansion + testing)

---

### 6. Consonant Mutations in Weak Tails (40 mismatches: consonant_mismatch_other)

**What it should do:**  
Preserve or mutate final consonants in weak-tail contexts, particularly:
1. Infinitives should preserve `-n` after weak-tail reduction
2. Gemination should be preserved from proto
3. Voiced/voiceless alternations should follow phonological rules

**Historical phonology:**  
Complex interaction of multiple processes:
- Hogg Vol 1 §6.3: Final `-n` in infinitives is typically preserved in OE
- Hogg Vol 1 §7: Gemination patterns from PGmc `-jj-` contexts
- Various devoicing and voicing assimilation rules

**Current status:**  
Multiple issues:
- `OldEnglishWeakTailNasalLoss` may be over-applying
- Gemination from `-jj-` contexts not always preserved
- Infinitive `-an` sometimes becomes `-a` or disappears entirely

**Examples from mismatch report:**
```
*fellą -> feolla (expected fellan)    # Final -n missing from infinitive
*gangăz -> ġæng (expected gangan)     # Final -n missing
*lindō -> lindō (expected linden)     # Final -n missing
*lungwą -> lungwa (expected lungen)   # Final -n missing
*banną -> bann (expected bannan)      # Single n instead of geminate
*bebruz -> beber (expected befer)     # b instead of f (voicing issue)
```

**Where relevant rules apply:**
- `OldEnglishWeakTailNasalLoss` (line 1207)
- `OldEnglishJGemination` (line 1272)
- Various consonant rules in `OldEnglishConsonantRules`

**Root cause diagnosis:**  
This bucket is heterogeneous. Subcategories:
1. **Infinitive -n preservation**: `*-ăną` → `-an` should preserve final `-n`
2. **Gemination**: Pre-geminated consonants (from `*-jj-`) should stay geminate
3. **Voicing alternations**: Final obstruent devoicing or other processes

**Proposed approach:**  
Need to investigate each subcategory separately:
1. Add infinitive-specific rule to preserve `-n` after weak-tail reduction
2. Audit `OldEnglishJGemination` to ensure it fires before weak-tail processes
3. Add final devoicing rule if needed

**Dependencies:**  
Interacts with weak-tail reduction (Tier 1, issue #2)

**Estimated effort:** 4-6 hours (complex, multiple sub-issues)

---

## Tier 3: Over-Application Issues (30-40 mismatches)

### 7. Breaking Over-Application (23 mismatches: breaking_extra_other)

**What's happening:**  
Breaking applies in contexts where it shouldn't, creating diphthongs in words that should have monophthongs.

**Examples from mismatch report:**
```
*bazją -> bierġa (expected berġe)       # ie instead of e
*barwōn -> bearwōn (expected bēr)       # ea instead of ē
*felθuz -> feolþ (expected feld)        # eo instead of e
*leusăną -> lēosan (expected forloren)  # ēo instead of o (complex)
*xazwăz -> hearw (expected hǣr)         # ea instead of ǣ
```

**Root cause:**  
Breaking contexts may be too permissive, or breaking is applying before other rules that should have removed the trigger.

**Investigation needed:**
1. Check if breaking contexts include cases that should be excluded
2. Verify chronology: does breaking run before/after the right rules?
3. Check for interaction with A-restoration, i-umlaut, etc.

**Estimated effort:** 3-4 hours

---

### 8. Palatalization Over-Application (16 mismatches: palatal_extra_other)

**What's happening:**  
Consonants are being palatalized when they shouldn't be.

**Examples from mismatch report:**
```
*biginnăną -> biġinnan (expected beginnan)  # ġ instead of g
*burōjăną -> burēġan (expected borian)      # ġ instead of (no palatal marker?)
*brekăną -> breċan (expected brecan)        # ċ instead of c
*kalbăz -> ċealb (expected cealf)           # ċ instead of c
*kambăz -> ċæmb (expected camb)             # ċ instead of c
```

**Root cause:**  
`OldEnglishPalatalisation` or related rules applying in contexts where they shouldn't. May be chronology issue (running too early) or context issue (too permissive).

**Investigation needed:**
1. Check palatalization context definitions
2. Verify that i-umlaut or other front-vowel sources are legitimate triggers
3. May need to restrict to only certain morphological contexts

**Estimated effort:** 2-3 hours

---

## Tier 4: Small-Impact or Edge Cases (<10 mismatches each)

### 9. Proto Gate Rejects (13 mismatches: no_output)

**What's happening:**  
`pgrmWord` (the proto gate) rejects certain reconstructions, causing `+?` output.

**Examples:**
```
*funxwstiz -> +? (expected fȳst)
*xabukăz -> +? (expected hafoc)
*xemenăz -> +? (expected heofon)
*xnakkăz -> +? (expected hnecca)
*regna-bugōn -> +? (expected reġnboga)
```

**Root cause:**  
These reconstructions likely contain:
1. Consonant clusters not in `pgrmOnsetCore`
2. Unusual weak-tail patterns
3. Compound structures (e.g., `*regna-bugōn`)

**Solution:**  
Case-by-case investigation:
1. Check if reconstruction is correct
2. Expand `pgrmWord` phonotactics if legitimate
3. Flag for etymological review if questionable

**Estimated effort:** 2-3 hours

---

### 10. I-Umlaut Missing (4 mismatches: i_umlaut_missing_true)

**Examples:**
```
*flaiskăz -> flāsc (expected flǣsċ)       # ā instead of ǣ
*sai -> sā (expected sǣ)                  # ā instead of ǣ
*strawjăną -> strowan (expected strewian) # o instead of e
*wainōjăną -> wānēġan (expected hwīnan)   # ā instead of ī
```

**Root cause:**  
`OldEnglishIUmlaut` not triggering in these specific contexts. May be:
1. Intervening consonants blocking (but should allow palatals per 2026-01-22 fix)
2. Trigger vowel lost before umlaut applies
3. Diphthong contexts need special handling

**Estimated effort:** 2-3 hours

---

### 11. Back-Fronting Over-Application (4 mismatches: back_expected_front_out)

**Examples:**
```
*brandăz -> brænd (expected brand)    # æ instead of a
*xamarăz -> hæmær (expected hamor)    # æ instead of a
*swanăz -> swæn (expected swan)       # æ instead of a
*θankăz -> þænc (expected þancas)     # æ instead of a
```

**Root cause:**  
`EnglishAngloFrisianBrightening` applying when it shouldn't. These look like cases where PGmc `*a` should stay `a` but is being fronted to `æ`.

**Investigation needed:**  
Check if these words have nasal contexts or other factors that should block A-F brightening.

**Estimated effort:** 1-2 hours

---

## Implementation Roadmap

### Phase 1: Foundation (Critical Infrastructure)
**Goal:** Fix foundational rules that block other fixes  
**Time:** 4-6 hours

1. ✅ Add `OldEnglishFinalLongVowelShortening` after high-vowel apocope
2. ✅ Fix `OldEnglishWeakTailReduction` to delete vowel nucleus
3. ✅ Rebuild bins and run baseline reports

**Expected impact:** ~90 mismatches resolved

---

### Phase 2: Major Gaps (High-Value Rules)
**Goal:** Add missing phonological processes  
**Time:** 6-8 hours

4. ✅ Add w-context to `EnglishBreaking*` rules
5. ✅ Reorder `OldEnglishVelarFricativePalatalization` before breaking
6. ✅ Refine `OldEnglishARestoration` intervening context (exclude liquids/sibilants)
7. ✅ Rebuild bins and run reports

**Expected impact:** ~35-40 mismatches resolved (cumulative ~125-130)

---

### Phase 3: Consonant Cleanup (Complex Interactions)
**Goal:** Fix weak-tail consonant issues  
**Time:** 4-6 hours

8. ✅ Add infinitive `-n` preservation rule
9. ✅ Audit `OldEnglishJGemination` chronology
10. ✅ Add final devoicing if needed
11. ✅ Rebuild bins and run reports

**Expected impact:** ~30-40 mismatches resolved (cumulative ~155-170)

---

### Phase 4: Fine-Tuning (Edge Cases)
**Goal:** Address over-application and edge cases  
**Time:** 6-10 hours

12. ✅ Investigate breaking over-application contexts
13. ✅ Investigate palatalization over-application
14. ✅ Fix proto gate rejections (case-by-case)
15. ✅ Debug remaining i-umlaut gaps
16. ✅ Fix A-F brightening over-application

**Expected impact:** ~50-60 mismatches resolved (target: <50 remaining)

---

## Quick Reference Table

| Issue | Bucket(s) | Mismatches | Priority | Effort | Phase |
|-------|-----------|------------|----------|--------|-------|
| Final long vowel shortening | final_vowel_missing | 34 | HIGH | 1-2h | 1 |
| Weak-tail nucleus deletion | final_vowel_extra | 56 | HIGH | 2-3h | 1 |
| A-restoration context | fronting_missing_no_trigger | 11 | HIGH | 2-3h | 2 |
| Breaking w-context | breaking_missing | 19 | HIGH | 1-2h | 2 |
| Velar fricative chronology | palatalization_missing | 6 | MEDIUM | 1h | 2 |
| Consonant mutations | consonant_mismatch_other | 40 | MEDIUM | 4-6h | 3 |
| Breaking over-application | breaking_extra_other | 23 | MEDIUM | 3-4h | 4 |
| Palatalization over-application | palatal_extra_other | 16 | MEDIUM | 2-3h | 4 |
| Proto gate rejects | no_output | 13 | LOW | 2-3h | 4 |
| I-umlaut gaps | i_umlaut_missing_true | 4 | LOW | 2-3h | 4 |
| Back-fronting over-application | back_expected_front_out | 4 | LOW | 1-2h | 4 |
| Other vowel quality issues | vowel_quality_other | 23 | MIXED | TBD | 4 |
| Other length issues | length_extra_other | 17 | MIXED | TBD | 4 |
| Final n missing | final_n_missing | 10 | MEDIUM | incl. in #6 | 3 |

**Total estimated effort:** 30-40 hours across 4 phases

---

## Testing Strategy

For each fix:

1. **Isolation test:** Test the rule in isolation with `apply down` on:
   - Positive examples (should match)
   - Negative examples (should NOT match)
   
2. **Stage test:** Rebuild bins, run `oe_full_trace_report.py`, check that the specific stage shows expected changes

3. **Integration test:** Run full `oe_mismatch_report.py` and verify:
   - Target bucket count decreases
   - No new mismatches in other buckets (regression)
   
4. **Spot-check:** Manually verify 3-5 example words from the target bucket

---

## Next Steps

**Immediate priorities:**
1. Start with Phase 1, Issue #1: `OldEnglishFinalLongVowelShortening`
2. Test in isolation, add to FST stack, rebuild bins
3. Run reports to establish new baseline
4. Move to Issue #2

**One rule at a time.** Each fix should be committed separately with:
- Rule definition changes
- Updated reports showing impact
- Documentation update in this file

---

## Historical Context

**Rules already addressed:**
1. ✅ **EnglishLiquidLowering** (2026-01-27): Commented out, awaiting final-long-vowel shortening (this doc, Phase 1 Issue #1)
2. ✅ **VelarFricativePalatalization** (2026-01-27): Identified as non-firing due to chronology (this doc, Phase 2 Issue #5)
3. ✅ **OldEnglishARestoration** (2026-02-06): Fixed foma syntax bug (optional context parens), but context still needs refinement (this doc, Phase 2 Issue #3)

---

## References

**Historical phonology sources:**
- `docs/references/hogg_vol1.txt` — Hogg, *A Grammar of Old English*, Vol. 1
- `docs/references/ringe_taylor_linguistic_history_vol2.txt` — Ringe & Taylor, *The Development of Old English*, Vol. 2

**FST source:**
- `server/fsts/germanic.txt` — All OE rules (lines 542-1508)

**Reports:**
- `docs/debug_snapshots/oe_mismatch_report_2026-02-06.txt` — Current baseline
- `docs/debug_snapshots/oe_full_trace_report_2026-02-06.txt` — Stage-by-stage traces

**Prior analysis:**
- `docs/germanic_transducer_report.md` — LiquidLowering and VelarFricativePalatalization investigations
- `DEV_NOTES.md` lines 40-69 — A-restoration debug summary
