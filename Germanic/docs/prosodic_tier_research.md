# Prosodic Tier Research Notes

## 1. Current Germanic Workarounds

### 1.1 Breve Notation for Unstressed Vowels
- `ă` used in weak tails: `-ăz`, `-ăną`, `-ăi`
- Distinguished from full `a` which undergoes different rules
- Example: `*bakăną` (weak unstressed) vs `*bakaną` (full, A-restoration)
- Line 295-322 in germanic.txt: `pgrmWeakTailVowel`

### 1.2 Compound Linking Vowels
- `ă` as linking vowel: `*regnă-bugô` (rainbow)
- Line 433-434: `pgrmLinkingVowel [ă:{*ă} | 0]`
- No stress marking — just position-based

### 1.3 Transponent PROTOFORMs
- Pre-applied sound changes that require prosodic info
- `*wir-aldu` → weorold (pre-applied i-lowering + inter-stress raising)
- `*jugunθ` → geoguþ (pre-applied early i-apocope)
- These AVOID modeling the prosodic rules

### 1.4 Paradigm Cell Forms
- Use oblique cases to get preserved geminates: `*mannas` → mannes
- Use dat.sg. for stress-dependent endings: `*spannăi` → spanne
- Not prosodic per se, but avoids word-final simplification

## 2. Burmish Tone Handling

### 2.1 Input Notation
- Tone written as suffix to syllable: `paH`, `taX`, `ka0`
- Three tonemes: Ø (unmarked), H (high), X (rising/checked)
- Line 37: `pbNotationTone [0 | H:H | X:X ]`

### 2.2 Syllable Structure
- Syllable = Initial + Rime
- Rime = RimeCore + (NasalCoda | StopCoda) + Tone
- Line 39-41: `pbPlainRime [pbPlainRimeSeg pbNotationTone]`

### 2.3 Tone-Conditioned Rules
- Rules reference `pbTone` in environment:
  `{*a} -> {*ɔ} || _ pbTone` (applies before tone marker)
- Tone is part of the string, rules can match it

### 2.4 Key Insight
- Tone is NOT a separate tier — it's inline with segments
- Tone markers follow the vowel/coda in the linear string
- This works because Burmish syllables are simple (CV(C)T)

## 3. Foma Capabilities Assessment

### 3.1 Multi-Character Symbols
- Already using: `{*ai}`, `{*ĕ}`, `{*ŋ}`
- Could add: `{σ}` (syllable boundary), `{ˈ}` (stress), `{ˌ}` (secondary)

### 3.2 Context Matching
- Can match any number of characters: `?*`, `?+`
- Can match specific sets: `[Vowel]+`
- Cannot easily COUNT syllables (no numeric operations)

### 3.3 Possible Approaches

**A. Inline Stress Markers (Burmish model)**
- Input: `*ˈjug.un.θiz` (dots for syllable boundaries, ˈ for stress)
- Rules match stress position: `{*i} -> 0 || ... ˌ [?]+ _`
- Pro: No preprocessing; single-pass FST
- Con: Complex notation in TSV; syllabification must be explicit

**B. Preprocessing Pass**
- First FST: Insert syllable boundaries based on sonority
- Second FST: Apply stress rules
- Third FST: Apply prosodically-conditioned rules
- Pro: Automatic syllabification
- Con: Multi-pass complicates pipeline; error propagation

**C. Syllable Counting via State**
- Use flag diacritics to track syllable count
- `@P.SYLL.1@`, `@P.SYLL.2@`, etc.
- Pro: Real syllable counting
- Con: Flag diacritics are awkward; limited state

## 4. Phenomena Requiring Prosodic Info

### 4.1 Early i-Apocope (Luick §296)
- -i lost in 3rd/4th syllable from stress
- Example: `*xilpis` (3 syll) → `*xilps` (apocopated)
- Requires: syllable count from stressed syllable

### 4.2 Sievers' Law  
- Heavy stem: *-ijăną; Light stem: *-jăną
- Requires: weight of preceding syllable (moras)

### 4.3 Stress-Conditioned Syncope
- Different rules for heavy vs light stems
- Example: `*bindiþi` vs `*biriþi` (R/T p.285)

### 4.4 Medial u-lowering (Campbell §373)
- u → o "protected" but "preserved after accented u"
- ALREADY MODELED via vowel harmony exception (negative context)
- Could generalize: `|| [NonStressed {*u}]+ _ ` needs stress marking

### 4.5 Compound Stress
- Inter-stress raising: `*-ald- → *-uld-` in second element
- Currently: transponent `*wir-aldu`
- Would need: secondary stress marking in compounds

### 4.6 A-Restoration Stress Dependence?
- Some sources suggest stress affects a-restoration
- Need to research further

## 5. Prototype: Early i-Apocope with Inline Syllable Markers

### 5.1 Working Prototype

The following Foma code successfully implements early i-apocope:

```foma
define V [a | e | i | o | u];
define C [b | d | f | g | h | j | k | l | m | n | p | r | s | t | v | w | z];
define Syll [C* V C*];
define Dot ".";
define Stress "ˈ";
define NonDot [V | C | Stress];

# Pattern: at least 2 dots (syllable boundaries) between stress and target
define TwoPlusDots [Stress NonDot* Dot NonDot* Dot];

# Rule: i → ∅ when 3rd+ syllable from stress, before final -z
define ThirdPlusIApocope [i -> 0 || TwoPlusDots ?* _ z .#.];
```

### 5.2 Test Results

| Input | Output | Expected | ✓/✗ |
|-------|--------|----------|-----|
| `ˈhau.bud.um.iz` | `ˈhau.bud.um.z` | apocopate (4th syll) | ✓ |
| `ˈjug.un.thiz` | `ˈjug.un.thz` | apocopate (3rd syll) | ✓ |
| `ˈfot.iz` | `ˈfot.iz` | preserve (2nd syll) | ✓ |
| `ˈword.um.iz` | `ˈword.um.z` | apocopate (3rd syll) | ✓ |

### 5.3 Key Insight

The rule works by counting **dots** (syllable boundaries), not syllables themselves.
This is simpler than true syllable counting and works for this use case.

### 5.4 Notation Requirements

For this approach, PROTOFORMs would need:
1. **Stress mark** `ˈ` before stressed syllable (usually word-initial)
2. **Syllable boundary** `.` between syllables
3. Example: `*ˈjug.un.θiz` instead of `*jugunθiz`

### 5.5 Trade-offs

**Pros:**
- Works within standard Foma (no flag diacritics needed)
- Single-pass FST (no preprocessing)
- Explicit syllabification enables many prosodic rules

**Cons:**
- Requires syllabification in TSV (extra annotation work)
- All ~700 PROTOFORMs would need updating
- Syllable boundaries may shift during derivation (syncope, etc.)

## 7. INVENTORY: Prosodically-Conditioned Phenomena in Germanic

This inventory documents all sound changes in the PGmc → OE pipeline that depend
on prosodic information (stress, syllable weight, syllable count, etc.).

### 7.1 Phenomena ALREADY Modeled (with workarounds)

| Phenomenon | Source | Current Solution | Notes |
|------------|--------|------------------|-------|
| **Weak tail distinction** | — | Breve `ă` | `*bakăną` vs `*bakaną` |
| **Sievers' Law** | R/T pp.69-71 | Input notation `-ijăną` | Heavy stems get explicit -ij- |
| **Compound linking** | — | `ă` linker | `*regnă-bugô` |
| **Early i-apocope (3rd syll)** | Luick §296, Brunner §145 | Transponent PROTOFORM | `*jugunθ` instead of `*jugunθiz` |
| **Inter-stress raising** | R/T §6.3.3 | Transponent PROTOFORM | `*wir-aldu` with pre-raised `-uld-` |
| **Medial u-lowering** | Campbell §373 | Vowel harmony exception | `[EnglishStarVocalic - [{*u}|{*ū}]]` |
| **Paradigm geminates** | Kurath 1956 | Gen.sg. cell | `*mannas` instead of `*mannaz` |

### 7.2 Phenomena NOT Fully Modeled (potential targets)

| Phenomenon | Source | Conditioning | Current Status |
|------------|--------|--------------|----------------|
| **Early i-apocope (general)** | Luick §296 | 3rd/4th syllable from stress | Case-by-case transponent |
| **Late i-apocope** | Brunner §146 | After heavy syllable (2nd syll) | Implicit in cascade |
| **Medial syncope (æ/e)** | Campbell §384-391 | After heavy syllable | Partially modeled |
| **High vowel syncope** | R/T p.285 | Light vs heavy stem | Not explicitly |
| **A-restoration stress** | Various | May be stress-conditioned | Under-researched |
| **Stress-conditioned breaking?** | Campbell | Breaking in unstressed? | Unknown |

### 7.3 Phenomena That WOULD Benefit from Prosodic Tier

**7.3.1 Early i-Apocope (Luick §296)**
- Condition: -i in 3rd/4th syllable from stress
- Examples: `*jugunθiz → *jugunθ`, `*xilpis → *xilps`
- Currently: Use truncated PROTOFORM
- With prosodic tier: `*ˈjug.un.θiz → *ˈjug.un.θz` (automatic)

**7.3.2 Sievers' Law Proper**
- Condition: -ij- after heavy stem, -j- after light
- Currently: Encode in input (`*sturtijăną` vs `*nasjăną`)
- With prosodic tier: Could derive automatically from weight

**7.3.3 General Syncope Rules**
- Condition: Different for heavy vs light stems
- Example: `*bindiþi → *bindþi` vs `*biriþi → *bireþi`
- Currently: Not consistently modeled
- With prosodic tier: Weight-sensitive deletion rules

**7.3.4 Compound Stress Effects**
- Condition: Secondary stress affects vowel reduction
- Example: `*weraldi- → weruldi-` (inter-stress raising)
- Currently: Transponent
- With prosodic tier: Mark `ˌ` for secondary stress

### 7.4 Assessment: How Many Mismatches Are Prosodic?

From current 39 mismatches, estimate prosodic involvement:
- ~5 may involve syncope/apocope timing
- ~2 may involve compound stress
- ~3 may involve i-apocope edge cases
- **TOTAL: ~10 mismatches might be addressable with prosodic modeling**

### 7.5 Decision Criteria

Implement prosodic tier IF:
1. At least 10+ mismatches would be fixed
2. Notation doesn't make TSV unreadable
3. Rules are cleaner than current workarounds
4. Migration effort is manageable (~700 rows)

KEEP transponent workarounds IF:
1. Affected lexemes are few and identifiable
2. Prosodic notation adds too much complexity
3. The workarounds are well-documented

---

## 8. Design Decision Point

At this point, we have:
- ✓ Audit of current workarounds (§1)
- ✓ Burmish model analysis (§2)
- ✓ Foma capabilities assessment (§3)
- ✓ Working prototype for early i-apocope (§5)
- ✓ Inventory of prosodic phenomena (§7)

**Open questions:**
1. Literature review: What approaches do others use? (TODO)
2. Final tradeoff analysis: Is the complexity worth it?
3. If yes: Design the notation system in detail
4. If no: Document why transponents are acceptable

---

## 6. Next Steps

1. ~~Research Foma flag diacritics for state tracking~~ (tested, works but awkward)
2. ~~Prototype inline stress markers for early i-apocope~~ (**DONE**)
3. Inventory ALL phenomena and decide if prosodic tier is worth it
4. Compare complexity of prosodic rules vs transponent workarounds
5. If proceeding: design syllabification notation for TSV
