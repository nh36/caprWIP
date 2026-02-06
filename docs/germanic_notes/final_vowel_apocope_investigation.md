# Final Vowel Apocope Investigation

**Date**: 2026-02-06  
**Status**: Investigation complete, experimental fix pending  
**Impact**: 77 mismatches (27% of total errors)

## Executive Summary

The OE pipeline is incorrectly preserving proto *-ą and *-ō as final -a/-ō when these should be deleted in Old English strong noun forms. Analysis of 77 affected words shows **78% have heavy stems** (long vowel OR consonant cluster before the ending), suggesting the fix should be: **delete final *-ą/*-ō after heavy syllables**.

This is a neogrammarian-compatible phonological rule (syllable-weight conditioning).

---

## Problem Statement

**Total mismatches**: 282 / 370 OE words (76% mismatch rate)

**Top mismatch category**: `final_vowel_extra` - 60 reported (actually 77 in full trace)
- 21-27% of all errors
- Single highest-impact issue

### Pattern
Output has final vowel (-a, -ō) where OE expects consonant-final form:
```
*bergą  → beorga   (expected beorg)   - extra -a
*bastą  → bæsta    (expected bæst)    - extra -a
*rastō  → rastō    (expected ræst)    - extra -ō
*xallō  → heallō   (expected heall)   - extra -ō
```

---

## Data Analysis

### Cases with EXTRA final vowel (77 total):

**50 cases**: Proto *-ą → output -a (should be Ø)
- Proto: neuter nom./acc. sg. ending
- OE: Should be deleted (heavy stems) or become -u (light stems)
- Examples: `*bergą → beorga` (exp. `beorg`), `*wurdą → wurda` (exp. `word`)

**23 cases**: Proto *-ō → output -ō (should be Ø)
- Proto: weak feminine nom.sg. ending
- OE: Should be deleted (when behaving as strong nouns)
- Examples: `*rastō → rastō` (exp. `ræst`), `*xelpō → heolpō` (exp. `help`)

**4 others**: Various endings (*-z, *-ē, *-o, *-ī)

### Cases with CORRECT final vowel (19 total):

**11 cases**: Proto *-ō → output -ō (correctly kept!)
- These ARE weak nouns that should preserve ending as -e/-u
- Examples: `*nasō → nasō` (exp. `nosu`), `*bōkō → bōcō` (exp. `bēċe`)

**4 cases**: Proto *-ą → output -a (correctly kept!)
- Example: `*gallą → ġealla` (exp. `ġealla`)

### Key Finding
**Same proto endings, opposite outcomes!**

Both *-ą and *-ō appear in BOTH "keep" and "lose" groups. This means we cannot simply "delete all *-ą" or "delete all *-ō" - we need phonological conditioning.

---

## Historical Background

### From Hogg vol. 1 (§3.3.2-3.3.3)

#### Strong Neuter Nouns (a-stems):
Nom./Acc. Singular endings:
- **Heavy stems** (long vowel OR VC+C): **ZERO ending**
  - `*word → word` (not *worda)
  - CVːC or CVVC or CVCC → Ø
- **Light stems** (short vowel + single C): **-u ending**
  - `*scip → scipu` (CVC)

Example paradigms:
```
        Singular   Plural
Nom.    word       word        (heavy: Ø)
Acc.    word       word
Gen.    wordes     worda
Dat.    worde      wordum

Nom.    scipu      scipu       (light: -u)
Acc.    scipu      scipu
Gen.    scipes     scipa
Dat.    scipe      scipum
```

#### Weak Nouns (n-stems):
All genders kept -a/-e ending regardless of weight:
- Masc nom.sg: `guma` (man)
- Fem nom.sg: `hearpe` (harp)
- Proto *-ō → OE -e/-u via weak-tail reduction

### Proto-Germanic to OE
- Proto neuter *-ą (nom./acc.sg. marker) underwent:
  - **Zero** after heavy syllables (apocope)
  - **-u** after light syllables (preserved, then possibly reduced)
  
- Proto weak *-ō underwent:
  - **-e/-u** (weak nouns - correctly handled by weak-tail reduction)
  - **Ø** (when reanalyzed as strong - currently broken)

---

## Current Pipeline Behavior

Tracing `*bergą → beorga`:

```
ProtoInput:          *b*e*r*g*ą
...
BreakingLengthening: *b*eo*r*g*ą        [e → eo]
...
WeakTailReduction:   *b*eo*r*g*ɔ̆        [ą → ɔ̆ = short schwa]
...
ProtoToOEWeightCleanup: *b*eo*r*g*ɔ̆
ProtoToOE:           *b*eo*r*g*ɔ̆
...
Orthography:         beorga              [ɔ̆ → a]
Surface:             beorga
```

**Problem**: `WeakTailReduction` is preserving *-ą as *-ɔ̆, which then surfaces as -a.

Should have been deleted after heavy syllable `*beorg`.

---

## Phonological Pattern Analysis

### Syllable Weight Analysis (77 cases)

Measured syllable weight of stem (before final vowel):
- **Heavy**: Long vowel OR short vowel + 2+ consonants
- **Light**: Short vowel + 0-1 consonants

#### Results:
```
HEAVY stems:  60 / 77  (78%)
LIGHT(?):     17 / 77  (22%)
CLEAR LIGHT:   0 / 77  (0%)
```

#### The 60 "HEAVY" cases (clear):
- Long vowel stems: `*blōdą, *būrą, *fōdrą, *jērą, *mēlą, *rōdō, *skūrō` etc.
- Cluster stems: `*bergą, *bastą, *landą, *wurdą, *xelpō, *mizdō` etc.

#### The 17 "unclear" cases:
Proto looks light (V+C) BUT becomes heavy in OE after vowel changes:
- `*strawą → strēaw` - *au → ēa (diphthong!) = HEAVY in OE
- `*juką → ġeoc` - *u → eo (diphthong!) = HEAVY in OE
- `*laugō → lēah` - *au → ēa (diphthong!) = HEAVY in OE
- `*braudą → brēad` - *au → ēa (diphthong!) = HEAVY in OE

**Insight**: We need to measure syllable weight **after OE vowel changes** (breaking, lengthening), not in proto!

### Failed Discriminators:
Cannot distinguish by:
- ❌ Penult consonant type (no pattern)
- ❌ Syllable count (both mono and poly in each group)
- ❌ Proto final cluster length alone

---

## The Neogrammarian Constraint

We **CANNOT** condition on:
- Grammatical gender (neuter vs. masculine vs. feminine)
- Stem class (strong vs. weak)
- Declension type (a-stem vs. n-stem vs. ō-stem)
- Morphological category

We **CAN** condition on:
- ✅ Phonological environment
- ✅ Syllable weight (heavy vs. light)
- ✅ Segmental context

**Proposed solution is neogrammarian-compatible**: Delete *-ą/*-ō after **heavy syllables** (measured phonologically in OE).

---

## User's Historical Note

> "A while ago we tried it both ways—deleting the final short vowel vs. not deleting it—and both choices produced a huge number of errors."

This makes perfect sense! Because:
- Some *-ą should → Ø (heavy stems: `*bergą → beorg`)
- Some *-ą should → -u (light stems: `*scip-ą → scipu`)
- Some *-ō should → Ø (strong forms: `*rastō → ræst`)
- Some *-ō should → -e/-u (weak nouns: `*nasō → nosu`)

**Blanket deletion OR blanket preservation both fail.**

The conditioning must be on **syllable weight**.

---

## Proposed Experimental Fix

### Hypothesis
Add apocope rule: Delete *-ą / *-ɔ̆ after heavy syllables (measured after OE vowel changes).

### Implementation Strategy

1. **Timing**: After breaking/lengthening, before weak-tail reduction
   - This way we measure OE syllable weight (not proto)
   
2. **Rule**: Delete *-ą when preceded by:
   - Long vowel: `V̄C*-ą → V̄C`
   - Diphthong: `VVC*-ą → VVC`
   - Consonant cluster: `VCC*-ą → VCC`

3. **Leave alone**: *-ą after light syllable (VC)
   - These should go through weak-tail reduction → -u

### Expected Outcomes

**Fixes (~60-70 cases)**:
- Heavy stem neuters: `*bergą → beorg` ✓
- Strong fem forms: `*rastō → ræst` ✓
- All the consonant-cluster cases

**Collateral damage** (need to check):
- Are there any light-stem *-ą that we're miscategorizing as heavy?
- Are there any that should keep -a for other reasons?

---

## Next Steps

### 1. Literature Check (Ringe/Taylor)
Verify that OE apocope was conditioned by syllable weight:
- Find sections on neuter endings
- Find sections on apocope chronology
- Confirm heavy/light distinction

### 2. Implement Experimental Rule
Create `OldEnglishHeavySyllableApocope`:
```foma
define OldEnglishHeavySyllableApocope [
    {*ą} -> 0 || HeavySyllable _ .#. ,
    {*ɔ̆} -> 0 || HeavySyllable _ .#.
];

define HeavySyllable [
    ... long vowel or diphthong or VC cluster ...
];
```

Place in pipeline AFTER breaking/lengthening, BEFORE weak-tail reduction.

### 3. Test and Measure
- Rebuild FSTs
- Generate new OE reports
- Compare:
  - How many of the 77 extra-vowel cases are fixed?
  - How many NEW errors are introduced?
  - What patterns emerge in the new errors?

### 4. Iterate
- Refine the heavy syllable definition
- Adjust timing in pipeline if needed
- Check for oblique-stem solutions (like "fire", "brand")

---

## Reference Data

### Complete list of 77 "extra vowel" cases:

#### Proto *-ą cases (50):
```
*bastą → bæsta (exp. bæst)           *baθą → bæþa (exp. bæþ)
*bergą → beorga (exp. beorg)         *blōdą → blōda (exp. blōd)
*braudą → brēada (exp. brēad)        *burdą → burda (exp. bord)
*būrą → būra (exp. būr)              *deuzą → dēora (exp. dēor)
*dranką → drænca (exp. drenċ)        *fellą → feolla (exp. fellan)
*flaxsą → fleahsa (exp. fleax)       *fōdrą → fōdra (exp. fōdor)
*frustą → frusta (exp. forst)        *fulką → fulca (exp. folc)
*grasą → græsa (exp. græs)           *gulθą → gulþa (exp. gold)
*xaglą → hæġla (exp. hæġl)           *xaubudą → hēabuda (exp. hēafod)
*xawwją → howa (exp. hīeġ)           *xunăgą → hunaga (exp. huniġ)
*xuzdą → hurda (exp. hord)           *jērą → ġēra (exp. ġēar)
*juką → ġuca (exp. ġeoc)             *knewą → cnēowa (exp. cnēow)
*landą → lænda (exp. land)           *laubą → lēaba (exp. lēaf)
*leθrą → leþra (exp. leþer)          *lībą → lība (exp. līf)
*luką → luca (exp. loc)              *lungwą → lungwa (exp. lungen)
*mēlą → mēla (exp. mǣl)              *natją → netta (exp. net)
*nistą → nista (exp. nest)           *raipą → rāpa (exp. rāp)
*saltą → sealta (exp. sealt)         *seglą → seġla (exp. seġl)
*skaftą → sċæfta (exp. sċeaft)       *stōdą → stōda (exp. stōd)
*strawą → stræwa (exp. strēaw)       *swerdą → sweorda (exp. sweord)
*timrą → timra (exp. timber)         *trugą → truga (exp. troh)
*warpą → wearpa (exp. wearp)         *waxsą → weahsa (exp. weax)
*wedrą → wedra (exp. weder)          *wībą → wība (exp. wīf)
*wundrą → wundra (exp. wundor)       *wurdą → wurda (exp. word)
*θaką → þæċa (exp. þæc)              *þingą → þinga (exp. þing)
```

#### Proto *-ō cases (23):
```
*dawwō → dawō (exp. dēaw)            *furxō → furhō (exp. furh)
*xallō → heallō (exp. heall)         *xelpō → heolpō (exp. help)
*xerdō → heordō (exp. hierd)         *xendjō → hindō (exp. hindan)
*xwīlō → hwīlō (exp. hwīl)           *laugō → lēagō (exp. lēah)
*librō → librō (exp. lifer)          *lindō → lindō (exp. linden)
*markō → mearcō (exp. mearcian)      *mizdō → mierdō (exp. mēd)
*nēθlō → nēþlō (exp. nǣdl)           *rastō → rastō (exp. ræst)
*rindō → rindō (exp. rind)           *rōdō → rōdō (exp. rōd)
*rustō → rustō (exp. rust)           *saiwălō → sāwalō (exp. sāwol)
*salbō → sealbō (exp. sealf)         *skūflō → sċūflō (exp. scofl)
*skūrō → sċūrō (exp. sċūr)           *spannō → spannō (exp. spann)
*surgō → surgō (exp. sorg)
```

#### Other endings (4):
```
*fedwōrez → fedwōre (exp. fēower)    *θūs-undī → þūsyndī (exp. sendan)
*wullo → wullo (exp. wull)           *westănē → westanē (exp. west)
```

---

## Status

- ✅ Data analysis complete
- ✅ Pattern identified (78% heavy stems)
- ✅ Historical justification found
- ⏳ Literature verification pending
- ⏳ Experimental fix pending
- ⏳ Testing pending

---

## Related Files

- Mismatch report: `server/docs/debug_snapshots/oe_mismatch_report_2026-02-06.txt`
- Full trace: `server/docs/debug_snapshots/oe_full_trace_report_2026-02-06.txt`
- Main FST: `server/fsts/germanic.txt`
- Report script: `server/tools/oe_full_trace_report.py`
- References: `docs/references/hogg_vol1.txt`, `ringe_taylor_linguistic_history_vol2.txt`
