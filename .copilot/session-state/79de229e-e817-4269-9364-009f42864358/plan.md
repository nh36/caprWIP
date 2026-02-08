# Plan: Phonology Improvement Using Mechanistic Buckets

## Checkpoint 012: NWGmc *ē₁ Lowering In Progress

### What was accomplished this session

1. **Bucket refactor committed and pushed** (`6154db6`): Split 6 monolithic junk-drawer
   buckets into 35+ mechanistic sub-buckets. No sound-change rules changed. 230 mismatches.

2. **Cycle 1 target identified**: `vowel_quality_other` (27 items), specifically the sub-pattern
   of 7 items where PGmc *ē₁ produces OE ē but should produce OE ǣ:
   - `*ēlăz → ēl` (expected ǣl)
   - `*lētăną → lētan` (expected lǣtan)
   - `*mēlą → mēl` (expected mǣl)
   - `*rēdăną → rēdan` (expected rǣdan)
   - `*nēθlō → nēþl` (expected nǣdl)
   - `*slēpăną → slēpan` (expected slǣp)
   - `*wēpnăn → wēpnan` (expected wǣpn)

3. **Research completed** (R/T vol.2 §5.1.2, §6.1.2):
   - PGmc *ē₁ → NWGmc *ā (unconditional lowering)
   - NWGmc *ā → OE ǣ via Anglo-Frisian Brightening (fronting of non-nasalized *ā)
   - *ā from *ai monophthongization was NOT fronted (monophthongization happened AFTER fronting)
   - Before nasals, *ā was nasalized and rounded to *ō (explains *mēnōθz → mōnaþ)

4. **Implementation in progress — UNCOMMITTED changes**:

   **a) `server/fsts/germanic.txt`**:
   - Added `NWGmcLongELowering` rule (~line 1298): `{*ē} → {*ā} || _ [EnglishStarConsonant - EnglishStarNasal]`
   - Extended `AngloFrisianBrightening` (~line 1184): added `{*ā} → {*ǣ}` alongside existing `{*a} → {*æ}`
   - Added `NWGmcLongELowering` to main pipeline after `NWGmcFinalLongORaising`
   - Added `NWGmcLongELowering` to sandbox trace pipeline

   **b) `server/fsts/old_english_sandbox.txt`**:
   - Added `OESandboxAfterNWGmcLongELowering` stage definition
   - Added regex/save for new .bin file

   **c) `server/tools/trace_old_english_sandbox.py`**:
   - Added `NWGmcLongELowering` trace stage entry

   **d) `server/tools/oe_full_trace_report.py`**:
   - Added `NWGmcLongELowering` trace stage entry

5. **Build status**: `foma -f fsts/germanic.txt` compiled successfully. Sandbox also compiled.
   BUT initial testing showed problems — `flookup` returned `+?` for several key items
   (ēlăz, lētăną, etc.) and `dēdiz → dide` (wrong). This needs debugging.

### Known issues with the uncommitted changes

- Many words with *ē are returning `+?` after the change. This suggests the `{*ā}` from
  NWGmcLongELowering is being consumed or blocking downstream rules.
- `*dēdiz → dide` instead of `dǣd` — something is going very wrong.
- The `{*ā} → {*ǣ}` addition to AFB may have unintended interactions with *ā from other
  sources (e.g., *ai monophthongization produces *ā which should NOT be fronted).
- Need to trace individual words to find where derivations diverge.

### Possible fix for the *ai/*ā conflict

The core problem: `PWGmcAiMonophthongization` converts `{*ai} → {*ā}` BEFORE AFB runs.
If AFB now fronts all `{*ā} → {*ǣ}`, then *ai-derived *ā gets wrongly fronted too.

Options:
A) **Use a distinct symbol** for *ā < *ē₁ (e.g., `{*ā₁}`) to avoid conflating with *ā < *ai.
   Have NWGmcLongELowering produce `{*ā₁}` and AFB front `{*ā₁} → {*ǣ}`.
B) **Skip the *ā intermediate** entirely: just do `{*ē} → {*ǣ}` directly in NWGmcLongELowering,
   and DON'T add `{*ā} → {*ǣ}` to AFB. This is simpler but historically less accurate.
   The nasal exception `_ [C - Nasal]` handles the *mēnōθz case.
C) **Reorder**: Move PWGmcAiMonophthongization to after AFB (R/T actually says
   monophthongization was later). But this is a risky structural change.

**Recommendation**: Option B is safest. Revert the AFB change, and instead have
NWGmcLongELowering do `{*ē} → {*ǣ}` directly. This avoids ALL interaction with *ai/*ā.

### Next steps when resuming

1. Debug the uncommitted changes OR revert and try Option B
2. If Option B: change NWGmcLongELowering from `{*ē} → {*ā}` to `{*ē} → {*ǣ}`,
   and revert the AFB addition of `{*ā} → {*ǣ}`
3. Build, trace key items (`*ēlăz`, `*lētăną`, `*dēdiz`, `*stainaz`)
4. Run mismatch report, compare to 230 baseline
5. If improvement: commit and push, write bucket investigation note
6. Then proceed to next cycle target

---

# Previous Plan (for reference)

## Old Plan: Stage Labelling, PGmc→PWGmc Phonology, and Berry Fix

## Problem Statement

The FST pipeline mixes rule names from different historical stages without consistent labelling. Some rules attributed to "OldEnglish" actually belong to Proto-West Germanic or Anglo-Frisian. The trace stages now match the actual pipeline and non-determinism is eliminated (255 mismatches, 0 branching). The next priorities are:

1. Rename rules so their historical stage is unambiguous from the name alone
2. Deepen the PGmc→PWGmc modelling based on sources
3. Fix berry (*bazją → OE berġe), currently producing "ber"

## Scholarly Consensus (from Ringe/Taylor vol. 2 §3.1, Hogg/Fulk vol. 1)

### Historical Stage Boundaries

**Proto-Germanic (PGmc):** Common to all Germanic. Ends with the split of NWGmc from Gothic.

**Northwest Germanic (NWGmc):** Shared by North and West Germanic but not Gothic.
- *u-lowering: *u → *o before non-high vowels in next syllable (NWGmcULowering ✓)

**Proto-West Germanic (PWGmc):** Shared by all WGmc but not North Germanic. Key changes in order:
1. Loss of final *-z in unstressed syllables
2. Loss of word-final *-a and *-ā (short low vowels)
3. Postconsonantal *j, *w → syllabic *i, *u (after the vowel losses expose them)
4. *Cj gemination (after *j→*i, so only in paradigmatic forms where *j survived)
5. Merger of *z with *r (rhotacism — already modelled in ConsonantRules)
6. Monophthongization of *ai → *ā before certain consonants

**Anglo-Frisian:** Shared by OE and Old Frisian but not OS/OHG.
- First Fronting / Brightening: *a → *æ (except before nasals)

**Old English (OE):** Changes specific to OE after the Anglo-Frisian period.
- Breaking, a-restoration, velar/palatal changes, i-umlaut, syncope, apocope, etc.

### Berry Derivation (per R/T and Kroonen)
- PGmc *bazją (Kroonen: *basja- ~ *bazja-)
- → Rhotacism: *barją
- → PWGmc *j→*i after final vowel loss: *bari (R/T p.46: "preceding postconsonantal *j and *w became syllabic *i")
- → Anglo-Frisian brightening: *bæri
- → i-umlaut: *beri
- → Final *i → *e lowering (NOT apocope, because ba.ri is light): *bere
- → Palatalization of *r before front vowel? → berġe (the ġ needs investigation)
- Expected OE: berġe (Kroonen: OE berige f.)

Key insight from R/T §6.8.1: "short *i and *u were lost word-finally after a **heavy** syllable." The syllable *be in *be.ri is LIGHT (CV, open), so *i is preserved and later lowered to *e.

### The Weight Marker Bug
The `OldEnglishHeavyMarker` (line 1411) uses `EnglishStarConsonant+` (one or more consonants after a short vowel), but the standalone `EnglishHighVowelApocope` (line 1402) correctly uses `EnglishStarConsonant EnglishStarConsonant` (two or more). The HeavyMarker incorrectly treats *beri as heavy because *e + *r satisfies "short vowel + 1 consonant."

The fix: change lines 1411-1412 from `EnglishStarConsonant+` to `EnglishStarConsonant EnglishStarConsonant+` (matching the standalone rule). Also add the trisyllabic condition (light + unstressed + final) from lines 1404-1405.

## Workplan

### Phase 1: Rule Naming Audit and Cleanup
- [ ] 1.1 Rename rules with clear stage prefixes:
  - `PGmc_` for Proto-Germanic changes
  - `NWGmc_` for Northwest Germanic (already done for NWGmcULowering ✓)
  - `PWGmc_` for Proto-West Germanic changes
  - `AngloFrisian_` for Anglo-Frisian changes
  - `OE_` for Old English changes
  - `ModE_` for Modern English changes
- [ ] 1.2 Audit each rule's historical placement against R/T and Hogg:
  - `EnglishWestGermanic` → Should be `PWGmc_CoreChanges` or similar
  - `WGmcMonophthongization` → Already PWGmc, rename to `PWGmc_AiMonophthongization`
  - `WGmcSyllabicJ` → `PWGmc_SyllabicJ`
  - `EnglishAngloFrisianBrightening` → `AngloFrisian_Brightening`
  - `EnglishBreakingLengthening` → `OE_Breaking`
  - `OldEnglishAuFronting` → Verify stage; rename `OE_AuFronting`
  - `OldEnglishWWSimplification` → Verify stage
  - `OldEnglishDiphthongLeveling` → Verify stage
  - `OldEnglishEwLongDiphthong` → Verify stage
  - etc. for all rules in the pipeline
- [ ] 1.3 Update all references (pipeline definition, trace stages, sandbox, trace scripts)
- [ ] 1.4 Rebuild, verify 255 mismatches, commit

### Phase 2: Fix the Weight Marker (Berry Fix, Part 1)
- [ ] 2.1 Change OldEnglishHeavyMarker short-vowel rules (lines 1411-1412):
  - FROM: `EnglishStarShortVowel EnglishStarConsonant+ _ .#.`
  - TO: `EnglishStarShortVowel EnglishStarConsonant EnglishStarConsonant+ _ .#.`
  (Require 2+ consonants after short vowel, matching the standalone rule)
- [ ] 2.2 Add trisyllabic apocope condition to HeavyMarker:
  - Add: `{*i} -> {*H} {*i} || EnglishStarShortVowel EnglishStarConsonant EnglishStarShortVowel EnglishStarConsonant _ .#.`
  (Light + unstressed + final high vowel)
- [ ] 2.3 Do the same for `{*u}` and `{*ą}` variants
- [ ] 2.4 Rebuild, trace berry (expect: no *H marker, *i preserved)
- [ ] 2.5 Run mismatch report, compare to 255 baseline
- [ ] 2.6 If regression, analyze which words are affected and whether the regression is historically correct
- [ ] 2.7 Commit if net improvement or neutral

### Phase 3: Berry Fix, Part 2 — Final *i Lowering and Palatalization
- [ ] 3.1 Verify that OldEnglishWeakTailReduction handles *i → *e word-finally
- [ ] 3.2 Investigate the ġ in berġe — is it from palatalization of *r before front vowel, or from a different source?
- [ ] 3.3 Check Kroonen: OE form is "berige f." — this suggests a trisyllabic form with intervocalic *g palatalized, not just *bere
  - If berġe = beriġe with syncope, we may need the full nom.sg. form *baziją or similar
  - The ġ may come from the *z > *r path differently, or from a different morphological form
- [ ] 3.4 Trace other words in the `final_vowel_missing` bucket to see if the weight marker fix helps them too
- [ ] 3.5 Implement any additional rules needed
- [ ] 3.6 Rebuild, test, commit

### Phase 4: Broader PGmc→PWGmc Improvements
- [ ] 4.1 Review whether any other PWGmc changes are missing from the pipeline
- [ ] 4.2 Check the mismatch buckets to see if PWGmc-stage issues account for remaining mismatches
- [ ] 4.3 Implement incrementally, testing after each change

## Notes

- The standalone `EnglishHighVowelApocope` (lines 1399-1406) is correctly implemented but unused — it was replaced by the HeavyMarker + separate apocope system. The HeavyMarker has a bug the standalone didn't have.
- PWGmc = West Germanic = WGmc — these are the same stage. The codebase currently uses "WestGermanic" and "WGmc" interchangeably.
- Berry's OE form "berige" (Kroonen) suggests there may be more morphology here than just *bari → *bere. Need to investigate whether the input form in the TSV is correct.
- Current pipeline status: 255 mismatches, 0 branching, commit 082d4da on `update` branch.
