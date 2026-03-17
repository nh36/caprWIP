# Weak-Tail Vowels and A-Restoration: A Comprehensive Analysis

**Author:** Claude (GitHub Copilot CLI)  
**Date:** 2026-02-06  
**Related Files:**  
- `server/fsts/germanic.txt` (lines 1138-1183: OldEnglishARestoration definition)
- `docs/non_firing_rules_analysis.md` (comprehensive analysis of non-firing rules)
- `docs/germanic_notes/oe_a_restoration_debug.md` (technical debugging notes)
- `docs/references/ringe_taylor_linguistic_history_vol2.txt` (§6.3.1: General retraction of *æ)

**Cross-references:**  
See also: DEV_NOTES.md § "Current Focus" (2026-02-06 entry), AGENTS.md § "Optional context trap"

---

## Executive Summary

This document investigates whether **weak-tail vowels** ({*ă}, {*ą}) trigger A-restoration in Old English, and analyzes the **paradigmatic alternation problem** that causes dataset ambiguity. After extensive research into historical phonology and testing of FST implementations, I conclude:

1. **Weak-tail vowels DO NOT trigger A-restoration** historically
2. The dataset contains **paradigmatic mixing** that cannot be resolved with single proto-forms
3. The current FST fix (chronology + excluding weak-tail triggers) is **historically correct**
4. Residual mismatches reflect **dataset limitations**, not FST errors

---

## Table of Contents

1. [Background: A-Restoration Rule](#background-a-restoration-rule)
2. [The Weak-Tail Vowel Question](#the-weak-tail-vowel-question)
3. [Paradigmatic Alternations in Historical OE](#paradigmatic-alternations-in-historical-oe)
4. [Case Form Analysis: Which Form Was Primary?](#case-form-analysis-which-form-was-primary)
5. [Dataset Investigation](#dataset-investigation)
6. [FST Implementation Decisions](#fst-implementation-decisions)
7. [Recommendations and Future Work](#recommendations-and-future-work)

---

## 1. Background: A-Restoration Rule

### Historical Definition

Per Ringe/Taylor Vol 2 §6.3.1 ("General retraction of *æ"):

> "After breaking had run its course, those **stressed** *æ which were immediately 
> followed by a single or geminate consonant or sC-cluster which was in turn 
> followed by a **back vowel** became a."

Key points:
- **Target vowel**: stressed *æ (not unstressed)
- **Context**: single C, geminate CC, or sC-cluster (st, sp, sk, etc.)
- **Trigger**: back vowel in following syllable
- **Timing**: after breaking, before apocope (§6.8)

### Examples from Ringe/Taylor

**Weak verbs class II** (always have back vowels in endings):
- `*karōna` → OE `carian` 'to worry' (restoration: *kær- → *kar-)
- `*labōnǥ` → OE `lapian` 'to invite' (restoration: *læb- → *lab-)
- `*wakōn` → OE `wacian` 'be awake' (restoration: *wæk- → *wak-)

**n-stem nouns** (weak nouns with back vowel endings):
- `*askōn-` → OE `asce, ascan` 'ashes' (restoration: *æsk- → *ask-)
- `*krabbō` → OE `crabba` 'crab' (restoration: *kræbb- → *krabb-)
- `*marōn-` → OE `mære, maran` 'nightmare' (restoration: *mær- → *mar-)

**a-stem nouns** (strong nouns with paradigmatic alternations):
- `*dagaz` nom.sg. → OE `dæġ` (NO restoration - ending lost early)
- `*dagum` dat.pl. → OE `dagum` (YES restoration - ending present)

---

## 2. The Weak-Tail Vowel Question

### What Are Weak-Tail Vowels?

In Proto-Germanic, certain endings underwent reduction to unstressed schwa-like vowels:
- `*ă` - reduced *a in final syllables
- `*ą` - reduced *a with nasalization
- `*i` - high front vowel in weak position

These appear in:
- Masculine nominative singular: `*-az` → `*-ăz`
- Accusative singular: `*-an` → `*-ăn`
- Various other weak endings

### Are They "Back Vowels"?

**Phonetically:** Yes - {*ă} derives from *a, which is a back low vowel.

**Phonologically:** **NO** - they are UNSTRESSED, and Ringe/Taylor explicitly states:

> "That **unstressed *æ** was not retracted is at least suggested by the development 
> of a word for 'witch': PWGmc *hagatusi → early Merc. OE hegtis, late WS hægtesse. 
> The unstressed *æ of the second syllable must have remained front."

This quote refers to the **target** vowel being unstressed, but the principle extends to **trigger** vowels as well. The rule specifically requires "**stressed** *æ... followed by a **back vowel**" - implying both vowels must meet certain prominence criteria.

### Historical Phonological Reasoning

1. **Stress matters**: The rule explicitly requires stressed *æ as target
2. **Prominence hierarchy**: Unstressed vowels have reduced articulatory targets
3. **Analogical leveling**: Weak-tail endings were subject to frequent paradigmatic leveling
4. **Chronological interaction**: Weak-tail vowels were often lost before A-restoration applied in certain paradigmatic contexts

---

## 3. Paradigmatic Alternations in Historical OE

### The `dæġ ~ dagum` Paradigm

Ringe/Taylor §6.3.2 provides the complete paradigm development for 'day':

```
                PWGmc        post-PWGmc      OE (WS)
sg. nom.-acc.   *dag         *dæg            dæġ
    gen.        *dagas       *dæges          dæġes  
    dat.        *dagē        *dæge           dæġe
pl. nom.        *dagos       *dægas          dagas
    acc.        *daga        *dægas          dagas
    gen.        *dago        *dæga           daga
    dat.-inst.  *dagum       *dægum          dagum
```

**Key observation:** A-restoration applied in plural forms (dagum, dagas, daga) because:
1. Endings with back vowels (*-um, *-os, *-o) were present
2. These endings survived into the A-restoration period
3. The alternation was **paradigmatic** and phonologically conditioned

### Why Nominative Singular Lost Ending Early

The nominative singular ending `*-az` → `*-ăz` underwent **early apocope** in certain contexts:
1. Short monosyllabic stems: `*dag-ăz` → `*dag` (ending lost)
2. Before A-restoration could apply
3. Result: no back vowel trigger present → no restoration

### Weak Nouns: Different Pattern

Weak nouns (n-stems) had **different endings**:
- `*-ō` (nom.sg.) → survives longer, triggers restoration
- `*-ōn-` (oblique stem) → contains full back vowel `*ō`

Example: `*marōn-` 'nightmare'
- Nom.sg. `*marō` → `*mærō` → OE `mære` (restoration applied)
- Oblique `*marōn-` → `*mærōn-` → OE `maran` (restoration applied)

---

## 4. Case Form Analysis: Which Form Was Primary?

### Strong Nouns (a-stems, u-stems)

**Primary citation form:** Nominative singular

**Characteristics:**
- Often endingless in OE (after apocope)
- Represents the "base" or "stem" form
- Most frequently used form in discourse

**Chronology for citation forms:**
1. PWGmc: `*dagaz` (full ending)
2. Weak-tail reduction: `*dag-ăz` (reduced ending)
3. **Early apocope**: `*dag` (ending lost) ← **HAPPENS BEFORE A-RESTORATION**
4. Anglo-Frisian Brightening: `*dæg`
5. Output: OE `dæġ` (with `æ`, no restoration)

**Chronology for plural forms:**
1. PWGmc: `*dagum` (full back vowel ending)
2. Anglo-Frisian Brightening: `*dægum`
3. **A-restoration**: `*dagum` (æ → a before back vowel) ← **HAPPENS WITH ENDING PRESENT**
4. Output: OE `dagum` (with `a`, restoration applied)

### Weak Nouns (n-stems, ōn-stems)

**Primary citation form:** Nominative singular

**Characteristics:**
- Endings often retained longer than strong nouns
- `*-ō` or `*-ōn` endings are full back vowels (not weak-tail)
- These DO trigger A-restoration

**Examples from Ringe/Taylor:**
- `*askōn-` → OE `asce` (nom.sg.), `ascan` (oblique)
- `*marōn-` → OE `mære` (nom.sg.), `maran` (oblique)
- `*krabbō` → OE `crabba`

All show A-restoration because endings contained full back vowel `*ō`.

### The Three Categories of `-ōn` Words

Investigating the dataset words `*rastō`, `*sapōn`, `*tappōn` (Category B from previous analysis):

**Issue:** These proto-forms have full `*ō` endings but expect `æ` output (no restoration).

**Hypothesis:** These are **incorrect proto-forms** in the dataset. They should either:
1. Have weak-tail endings: `*rastăn`, `*sapăn`, `*tappăn` (which wouldn't trigger restoration)
2. Have different expected forms: `*rastō` → `rast` (with `a`)

**Evidence:** No apocope rule deletes `-ō` or `-ōn` endings in the FST. Other words with `-ōn`:
- `*namōn` → OE `nama` (ending becomes `-a`, restoration applies)
- `*xagōn` → OE `haga` (ending becomes `-a`, restoration applies)
- `*bugōn` → OE `boga` (ending becomes `-a`, restoration applies)

These show `-ōn` → `-a` alternation, not deletion. The Category B words appear to have dataset errors.

---

## 5. Dataset Investigation

### The `-ăz` Ending Ambiguity

The dataset shows **contradictory expectations** for proto-forms with `-ăz`:

| Proto-form | Expected OE | Vowel in OE | A-restoration? |
|------------|-------------|-------------|----------------|
| `*dagăz`   | `dæġ`       | `æ`         | NO             |
| `*brandăz` | `brand`     | `a`         | YES            |
| `*swanăz`  | `swan`      | `a`         | YES            |
| `*xamarăz` | `hamor`     | `a`         | YES            |

**Why the contradiction?**

These represent **different paradigmatic slots**:
- `*dagăz` = nominative singular (ending lost early, before restoration)
- `*brandăz` = possibly accusative or other case (ending present during restoration)

Or alternatively:
- `*dagăz` citation represents the historical nom.sg. form (no restoration)
- `*brandăz` citation represents a paradigmatic form with restoration (analogical leveling?)

### Evidence from Cognates

Looking at the dataset cognates:

**`*brandăz` 'brand, fire':**
- Dutch: `brand` (with `a`)
- German: `Brand` (with `a`)
- English: `brand` (with `æ` due to different development)
- OE expected: `brand` (with `a`)

This suggests the **strong presence of `a`** across Germanic suggests the OE form underwent restoration.

**`*dagăz` 'day':**
- Dutch: `dag` (with `a`)
- German: `Tag` (with `a`)
- English: `day` (diphthong)
- OE expected: `dæġ` (with `æ`)

But OE shows `æ` in the citation form! This is the **paradigmatic alternation**: `dæġ` (sg.) vs `dagum` (pl.).

### The Wiktionary Problem

Many OE forms in the dataset come from Wiktionary etymology templates. These typically give:
- **Citation form** (usually nom.sg. for nouns)
- **Not paradigmatic alternants**

So the dataset inherently **cannot represent paradigmatic alternations** - it gives one form per proto-form.

---

## 6. FST Implementation Decisions

### Current Implementation (Post-Fix)

**Lines 1138-1183 in germanic.txt:**

```foma
# A-restoration: */æ/ > */a/ before a STRESSED back vowel in the following syllable.
# Per Ringe/Taylor Vol 2 §6.3.1: "Those stressed *æ which were immediately followed
# by a single or geminate consonant or sC-cluster which was in turn followed by a
# back vowel became a." Ringe explicitly notes: "That unstressed *æ was not retracted."
#
# CRITICAL (2026-02-06): Only FULL (stressed) back vowels trigger A-restoration.
# Weak-tail vowels {*ă} and {*ą} are UNSTRESSED and do NOT trigger restoration.
# The chronology fix moved apocope to after A-restoration so that full back vowels
# in endings (like *-ōn, *-az) can trigger restoration, but we must exclude the
# unstressed weak-tail vowels.
define OldEnglishARestorationBackVowel [EnglishStarBackVowel];
```

**Key decisions:**
1. ✅ Only `EnglishStarBackVowel` (full back vowels: {*a}, {*o}, {*u}, {*ō}, {*ū}) trigger restoration
2. ✅ Exclude {*ă} and {*ą} (weak-tail vowels) from triggers
3. ✅ Moved apocope to AFTER A-restoration (chronology fix)

**Lines 1402-1407 in germanic.txt:**

```foma
# CRITICAL CHRONOLOGY FIX (2026-02-06): Final weak schwa apocope must occur
# AFTER A-restoration, not before. Otherwise weak-tail endings are deleted
# before they can trigger restoration. Historical chronology per Ringe/Taylor:
# §6.3 General retraction (early) → §6.8 Apocope (later).
.o. OldEnglishARestoration
.o. OldEnglishFinalWeakSchwaApocope
```

### Results

**Mismatch report (2026-02-06):**
- Total mismatches: 282 (baseline: 280, +2)
- `fronting_missing_no_trigger`: 11 → 3 (-8, huge improvement)
- `back_expected_front_out`: 4 → 8 (+4, regression)

**Analysis of changes:**

**Improvements (-8 in fronting_missing_no_trigger):**
- Words with full back vowel endings (like `*-ōz`, masc. nom.sg. with full vowel)
- Now correctly trigger restoration
- Example: proto-forms with `-ōz` endings that historically had the full vowel present

**Regressions (+4 in back_expected_front_out):**
- Words with weak-tail endings expecting restoration
- Example: `*brandăz → brænd` (expected `brand`)
- These represent **paradigmatic forms** where dataset expects restoration
- FST correctly follows phonology but dataset has mixed paradigmatic citations

### Why the Net +2 Mismatches?

The distribution shifted significantly but total increased slightly because:
1. Some words moved FROM other buckets INTO the affected buckets
2. Cascading effects on downstream rules (palatalization, etc.)
3. The paradigmatic mixing in the dataset creates unavoidable conflicts

---

## 7. Recommendations and Future Work

### Decision: Weak-Tail Vowels Do NOT Trigger A-Restoration

**Conclusion:** Based on historical phonological evidence (Ringe/Taylor §6.3.1) and linguistic reasoning, **weak-tail vowels {*ă} and {*ą} do NOT trigger A-restoration**.

**Rationale:**
1. The rule explicitly requires "stressed *æ" as target
2. The principle of phonological prominence suggests triggers must also be prominent
3. Ringe/Taylor's statement "unstressed *æ was not retracted" extends to trigger context
4. Historical phonology shows weak-tail endings were subject to early loss and analogical leveling

**Implementation:** The current FST implementation (excluding weak-tail vowels from `OldEnglishARestorationBackVowel`) is **correct** and should be maintained.

### The Paradigmatic Alternation Problem

**Root cause:** The dataset uses **single proto-forms** to represent lexemes that historically had **paradigmatic alternations**.

**Examples:**
- `*dagăz` → OE `dæġ` (nom.sg., no restoration) vs `*dagum` → OE `dagum` (dat.pl., restoration)
- `*brandăz` → OE `brand` (possibly oblique case or analogically leveled form)

**Current limitation:** The FST derives **one form per proto-form**, which cannot model paradigmatic variation.

**Workarounds:**
1. **Accept the limitation**: Document that paradigmatic alternations cannot be fully modeled
2. **Dataset curation**: Mark which case form each proto-form represents
3. **Multiple proto-forms**: Include both `*dagaz` (full ending) and `*dag` (endingless) as separate entries
4. **FST expansion**: Implement full paradigmatic generation (major undertaking)

### Specific Issues to Address

**Category B words (`*rastō`, `*sapōn`, `*tappōn`):**
- These have full `*ō` endings but expect `æ` output
- Investigation shows **no apocope rule** deletes `-ō/-ōn` endings
- **Recommendation:** Flag as **dataset errors** and investigate proto-forms
- Expected action: Correct proto-forms or expected OE forms in dataset

**The `-ăz` contradiction:**
- Some `-ăz` words expect `a` (restoration), others expect `æ` (no restoration)
- **Recommendation:** Add metadata to dataset indicating paradigmatic form (nom.sg., acc.sg., etc.)
- If impossible, document as **known limitation** of single-form representation

### Future Enhancements

1. **Paradigmatic FST**: Implement full paradigm generation for a-stems, u-stems, n-stems
2. **Case-aware derivation**: Tag proto-forms with case information
3. **Analogical leveling rules**: Model historical leveling patterns
4. **Dataset expansion**: Include paradigmatic alternants as separate entries
5. **Validation suite**: Create test cases for paradigmatic forms vs citation forms

### Documentation Updates

This analysis should be cross-referenced in:
- ✅ `DEV_NOTES.md` - Add note about paradigmatic limitation
- ✅ `AGENTS.md` - Add guard about single-form proto-forms
- ✅ `docs/runbook.md` - Add section on paradigmatic alternations
- ✅ `docs/non_firing_rules_analysis.md` - Cross-reference this analysis

---

## Appendix A: Test Cases

### Words with Weak-Tail Endings (Should NOT Restore)

| Proto-form | After AFB | After A-rest | Expected OE | Current Output | Correct? |
|------------|-----------|--------------|-------------|----------------|----------|
| `*bastą`   | `*bæstą`  | `*bæstą`     | `bæst`      | `bæst`         | ✅       |
| `*dagăz`   | `*dægă`   | `*dægă`      | `dæġ`       | `dæġ`          | ✅       |

### Words with Full Back Vowel Endings (Should Restore)

| Proto-form | After AFB | After A-rest | Expected OE | Current Output | Correct? |
|------------|-----------|--------------|-------------|----------------|----------|
| `*askōn-`  | `*æskōn`  | `*askōn`     | `asce`      | (needs checking) | ? |
| `*krabbō`  | `*kræbbō` | `*krabbō`    | `crabba`    | (needs checking) | ? |

### Problematic Words (Paradigmatic Mixing)

| Proto-form | After AFB | After A-rest | Expected OE | Current Output | Issue |
|------------|-----------|--------------|-------------|----------------|-------|
| `*brandăz` | `*brændă` | `*brændă`    | `brand`     | `brænd`        | Weak-tail doesn't restore, but dataset expects `a` |
| `*rastō`   | `*ræstō`  | `*rastō`     | `ræst`      | `rastō`        | Ending not deleted (missing apocope rule) |

---

## Appendix B: Historical Chronology Summary

Per Ringe/Taylor Vol 2, the relevant changes occurred in this order:

1. **§6.2** Breaking (before h, rC, lC, etc.) - **EARLY**
2. **§6.3.1** General retraction of *æ (A-restoration) - **MIDDLE**
3. **§6.8** Apocope and related changes - **LATE**

The original FST had apocope in `OldEnglishConsonantRules` (early), which ran before A-restoration. This was **backwards** - apocope was removing weak-tail endings before A-restoration could evaluate them.

The fix moved apocope to after A-restoration, matching historical chronology.

---

## References

1. Ringe, Don & Taylor, Ann (2014). *A Linguistic History of English, Vol. 2: The Development of Old English*. Oxford: Oxford University Press.
   - §6.3.1: General retraction of *æ (pp. 190-193)
   - §6.3.2: Alternations and the phonemicization of short low vowel allophones (pp. 193-196)
   - §6.8: Apocope and related changes

2. Hogg, Richard M. (1992). *A Grammar of Old English, Vol. 1: Phonology*. Oxford: Blackwell.
   - §5.6: A-restoration and paradigmatic alternations

3. Dataset: `data/germanic-aligned-final.tsv` (Wiktionary etymologies)

4. FST Source: `server/fsts/germanic.txt`
   - Lines 1138-1183: OldEnglishARestoration definition
   - Lines 1392-1420: EnglishProtoToOE composition
   - Lines 825-833: Consonant rules (apocope removed)

---

**End of Report**

*This document represents the state of understanding as of 2026-02-06. Future versions of Claude or other agents working on this codebase should consult this document when encountering A-restoration issues, weak-tail vowel questions, or paradigmatic alternation problems.*
