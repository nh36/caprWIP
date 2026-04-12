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

## 9. ALTERNATIVE: Stressed Vowel Notation (User Suggestion)

The user suggested a simpler approach: mark stressed vowels with acute accent
(like `á`, `ú`) just as we mark unstressed with breve (`ă`). Syllable counting
can be done by counting vowels rather than explicit boundaries.

### 9.1 Notation Comparison

| Approach | Example Input | Pros | Cons |
|----------|---------------|------|------|
| **Dot boundaries** | `*ˈjug.un.θiz` | Explicit structure | Conflicts with `*` prefix; extra chars |
| **Stressed vowels** | `*júgunθiz` | Minimal change; natural | Requires vowel inventory update |
| **CVC template** | `CVC.VCC.VCz` | Shows weight | Separate from segments |

### 9.2 Stressed Vowel Approach — Prototype

```foma
# Stressed vowels (acute accent)
define StressedV [á:{*á} | ú:{*ú} | í:{*í} | é:{*é} | ó:{*ó}];

# Unstressed vowels (plain or breve)
define UnstressedV [a:{*a} | u:{*u} | i:{*i} | e:{*e} | o:{*o} | ă:{*ă}];

# Any vowel
define AnyV [StressedV | UnstressedV];

# Consonants
define C [...];

# Count vowels: at least 2 vowels between stressed and target
define TwoVowelsBetween [StressedV C* [AnyV C*]+];

# Early i-apocope: delete *i in 3rd+ syllable
define EarlyIApocope [{*i} -> 0 || TwoVowelsBetween _ {*z} .#.];
```

### 9.3 Test Results

| Input | Output | Expected | ✓ |
|-------|--------|----------|---|
| `júgunθiz` | `*j*ú*g*u*n*θ*z` | apocopate (3rd) | ✓ |
| `fótiz` | `*f*ó*t*i*z` | preserve (2nd) | ✓ |
| `háubudumiz` | `*h*á*u*b*u*d*u*m*z` | apocopate (4th) | ✓ |

### 9.4 Integration with Existing System

**Minimal changes needed:**
1. Add `{*á}`, `{*é}`, `{*í}`, `{*ó}`, `{*ú}` to symbol inventory
2. Add `á:{*á}`, etc. to lexicon patterns (`pgrmRoot`, etc.)
3. Update TSV: mark stressed vowel in first syllable (usually predictable)

**Fits existing convention:**
- Already use `ă` for unstressed → use `á` for stressed
- Already use `{*ă}` multi-char symbol → add `{*á}`
- Counting vowels works because Germanic stress is initial

### 9.5 Syllable Weight via Structure

For Sievers' Law (heavy vs light stems), we can check weight by pattern:
- **Light:** single short vowel + single consonant (CV)
- **Heavy:** long vowel OR diphthong OR closed syllable (CVV, CVC, CVCC)

```foma
# Light stem: short stressed vowel + single consonant + j
define LightStem [C StressedShortV C {*j}];

# Heavy stem: anything else before j
define HeavyStem [[C StressedLongV | C StressedShortV C C] [{*i}] {*j}];
```

This doesn't require explicit syllable boundaries — weight is inferable from
the segment sequence.

### 9.6 Advantages Over Dot Notation

1. **No conflict with `*` prefix** — dots might be parsed oddly
2. **Minimal TSV changes** — just change first vowel per word
3. **Natural reading** — `*júgunθiz` reads like a proto-form
4. **Vowel counting is simple** — no explicit boundary tracking
5. **Compatible with diphthongs** — `*áu` marks stressed diphthong

### 9.7 Resolved Questions

**1. Long vowels:** Treat macron vowels (`ā, ē, ī, ō, ū`) as inherently stressed.
   - Germanic has initial stress, so long vowels in first syllable = stressed
   - For unstressed long vowels (rare), could use breve+macron: `ā̆`
   - Simplification: macron = stressed in root syllables

**2. Secondary stress in compounds:** Use grave accent (`à, è, ì, ò, ù`)
   - Primary: `á, é, í, ó, ú` (acute)
   - Secondary: `à, è, ì, ò, ù` (grave)
   - Unstressed: `a, e, i, o, u` (plain) or `ă` (explicit unstressed)
   - Example: `*wér-àldu` (primary on first element, secondary on second)

**3. Diphthongs:** Count as ONE vowel (one syllable nucleus)
   - Stressed: `*áu, *ái, *éu, *éi`
   - Unstressed: `*au, *ai, *eu, *ei`
   - Example: `*háubudumiz` = 4 syllables (*áu + *u + *u + *i)

### 9.8 Full Symbol Inventory for Prosodic Notation

| Type | Short | Long | Diphthong |
|------|-------|------|-----------|
| **Primary stress** | á é í ó ú | ā́ ḗ ī́ ṓ ū́ (or just ā ē ī ō ū) | áu ái éu éi |
| **Secondary stress** | à è ì ò ù | ā̀ ḕ ī̀ ṑ ū̀ | àu àì |
| **Unstressed** | a e i o u | — | au ai eu ei |
| **Explicit unstressed** | ă ĕ ĭ ŏ ŭ | — | — |

**Simplification:** In practice, we may only need:
- Acute for primary stress: `á, ú, áu`
- Plain for unstressed in polysyllables: `a, u, au`
- Breve for grammatical endings: `ă` (already in use)
- Grave for secondary stress in compounds (rare)

### 9.9 Next Steps for Implementation

1. **Add symbols to germanic.txt:**
   - Add `{*á}, {*é}, {*í}, {*ó}, {*ú}` to vowel inventories
   - Add `{*áu}, {*ái}` to diphthong inventory
   - Add `á:{*á}`, etc. to lexicon patterns

2. **Update TSV entries (~700 rows):**
   - Mark first syllable vowel as stressed (acute accent)
   - Most entries: just change first vowel (predictable stress)
   - Compounds: mark secondary stress if needed

3. **Write prosodic rules:**
   - Early i-apocope (Luick §296)
   - Possibly: Sievers' Law weight check
   - Possibly: stress-conditioned syncope

---

## 10. IMPLEMENTATION DESIGN (Redundant System)

The user prefers **redundancy** — it's acceptable to have both macron AND acute on a vowel
(e.g., `ā́` for stressed long ā). This simplifies the design: stress marking is explicit
and orthogonal to vowel length.

### 10.1 Notation System

#### 10.1.1 Stressed Short Vowels (New)
| Vowel | Input | Starred |
|-------|-------|---------|
| á | `á:{*á}` | `{*á}` |
| é | `é:{*é}` | `{*é}` |
| í | `í:{*í}` | `{*í}` |
| ó | `ó:{*ó}` | `{*ó}` |
| ú | `ú:{*ú}` | `{*ú}` |
| ý | `ý:{*ý}` | `{*ý}` |

#### 10.1.2 Stressed Long Vowels (New, Redundant Marking)
| Vowel | Input | Starred | Notes |
|-------|-------|---------|-------|
| ā́ | `ā́:{*ā́}` | `{*ā́}` | U+0101 + U+0301 |
| ḗ | `ḗ:{*ḗ}` | `{*ḗ}` | U+1E17 (precomposed) |
| ī́ | `ī́:{*ī́}` | `{*ī́}` | U+012B + U+0301 |
| ṓ | `ṓ:{*ṓ}` | `{*ṓ}` | U+1E53 (precomposed) |
| ū́ | `ū́:{*ū́}` | `{*ū́}` | U+016B + U+0301 |

**Fallback:** If combining marks cause issues, use `ā́` as `{ā́}` multichar symbol.

#### 10.1.3 Secondary Stress (Compounds)
| Vowel | Input | Starred | Notes |
|-------|-------|---------|-------|
| à | `à:{*à}` | `{*à}` | Secondary stress, short |
| è | `è:{*è}` | `{*è}` | Secondary stress, short |
| etc. | | | |
| ā̀ | `ā̀:{*ā̀}` | `{*ā̀}` | Secondary stress, long |

#### 10.1.4 Stressed Diphthongs (New)
| Diphthong | Input | Starred |
|-----------|-------|---------|
| áu | `{áu}:{*áu}` | `{*áu}` |
| ái | `{ái}:{*ái}` | `{*ái}` |
| éu | `{éu}:{*éu}` | `{*éu}` |
| íu | `{íu}:{*íu}` | `{*íu}` |

#### 10.1.5 Nasalized Vowels with Stress
| Vowel | Input | Starred | Notes |
|-------|-------|---------|-------|
| ą́ | `ą́:{*ą́}` | `{*ą́}` | Stressed nasal (if needed) |

#### 10.1.6 Existing Unstressed Markers (Kept)
| Vowel | Input | Starred | Notes |
|-------|-------|---------|-------|
| ă | `ă:{*ă}` | `{*ă}` | Weak tail unstressed |
| ĕ | (add) | `{*ĕ}` | If needed |

### 10.2 Vowel Hierarchy for Rules

```foma
# ==== PRIMARY STRESS ====
# Short stressed (acute)
define StressedShortV [
    {*á} | {*é} | {*í} | {*ó} | {*ú} | {*ý}
];

# Long stressed (macron + acute, redundant)
define StressedLongV [
    {*ā́} | {*ḗ} | {*ī́} | {*ṓ} | {*ū́}
];

# Stressed diphthongs (acute on first element)
define StressedDiphthong [
    {*áu} | {*ái} | {*éu} | {*íu}
];

# All primary-stressed vocalics
define PrimaryStressedV [StressedShortV | StressedLongV | StressedDiphthong];

# ==== SECONDARY STRESS ====
define SecondaryStressedShortV [
    {*à} | {*è} | {*ì} | {*ò} | {*ù}
];
define SecondaryStressedLongV [
    {*ā̀} | {*ḕ} | {*ī̀} | {*ṑ} | {*ū̀}
];
define SecondaryStressedV [SecondaryStressedShortV | SecondaryStressedLongV];

# ==== UNSTRESSED ====
# Plain short vowels (unstressed by default in non-initial position)
define UnstressedShortV [
    {*a} | {*e} | {*i} | {*o} | {*u} | {*y}
];

# Explicit unstressed (breve)
define ExplicitUnstressedV [
    {*ă} | {*ĕ} | {*ĭ} | {*ŏ} | {*ŭ}
];

# Nasalized (typically unstressed endings)
define NasalV [
    {*ą} | {*ę} | {*ų}
];

# Long vowels in weak tails (rare, usually unstressed)
define WeakTailLongV [
    {*ē} | {*ō} | {*ī}
];

# ==== COMBINED CLASSES ====
# Any stressed vowel
define AnyStressedV [PrimaryStressedV | SecondaryStressedV];

# Any unstressed vowel
define AnyUnstressedV [
    UnstressedShortV | ExplicitUnstressedV | NasalV | WeakTailLongV
];

# All vocalic segments (for syllable counting)
define AllVocalic [AnyStressedV | AnyUnstressedV];

# Consonants (existing PGmcStarConsonant)
define C PGmcStarConsonant;
```

### 10.3 Prosodically-Conditioned Rules

#### 10.3.1 Early i-Apocope (Luick §296, Brunner §145)

```foma
# Early i-apocope: *i lost in 3rd or 4th syllable from stress
# Condition: At least 2 vowels between stressed vowel and target *i
# Effect: *i → 0 word-finally before *z
# Timing: BEFORE i-umlaut (proven by lack of umlaut)
#
# Example: *júgunθiz → *júgunθz (then -z deletion → *júgunθ → geoguþ)
#          3 vowels: ú-u-i, so i is in 3rd position → delete
#
# Counterexample: *fṓtiz → *fṓtiz (2 vowels: ṓ-i, so i is in 2nd position → keep)

define TwoOrMoreUnstressedAfterStress [
    C* AnyUnstressedV [C* AnyUnstressedV]+
];

define EarlyIApocope [
    {*i} -> 0 || PrimaryStressedV TwoOrMoreUnstressedAfterStress C* _ {*z} .#.
];
```

#### 10.3.2 Inter-Stress Raising (R/T vol.2 p.255)

```foma
# Inter-stress raising: unstressed *a → *u between primary and secondary stress
# Applies in compounds: *wér-àldu → *wér-ùldu
# R/T vol.2 p.255: "*a became u in the first member of compounds when directly
#                  followed by a stressed syllable"
#
# This rule would replace the transponent approach for weorold.

define InterStressRaising [
    {*a} -> {*u} || PrimaryStressedV C+ _ C+ SecondaryStressedV
];
```

#### 10.3.3 Sievers' Law Weight Check (Optional)

```foma
# Sievers' Law: heavy stems have -ij- surface, light stems have -j- surface
# Heavy = long V OR diphthong OR closed syllable
# Currently encoded in input; could derive if stress markers present
#
# NOT IMPLEMENTING NOW — input encoding is sufficient
```

### 10.4 Changes to germanic.txt

#### 10.4.1 Symbol Inventories

Add after line ~475 (PGmcStarVowel):

```foma
# ===== PROSODIC STRESS MARKERS =====
# Added 2026-04-12 for syllable-counting rules (Luick §296, etc.)

define PGmcStressedShortVowel [
    {*á} | {*é} | {*í} | {*ó} | {*ú} | {*ý}
];

define PGmcStressedLongVowel [
    {*ā́} | {*ḗ} | {*ī́} | {*ṓ} | {*ū́}
];

define PGmcStressedDiphthong [
    {*áu} | {*ái} | {*éu} | {*íu}
];

define PGmcSecondaryStressVowel [
    {*à} | {*è} | {*ì} | {*ò} | {*ù} |
    {*ā̀} | {*ḕ} | {*ī̀} | {*ṑ} | {*ū̀}
];

define PGmcPrimaryStressed [
    PGmcStressedShortVowel | PGmcStressedLongVowel | PGmcStressedDiphthong
];

define PGmcAnyStressed [PGmcPrimaryStressed | PGmcSecondaryStressVowel];
```

#### 10.4.2 Lexicon Patterns (pgrmShortVowel etc.)

Modify lines 131-145:

```foma
# Original (unstressed or unmarked)
define pgrmShortVowel [
    a:{*a} | e:{*e} | i:{*i} | o:{*o} | u:{*u} | y:{*y}
];

# ADD: Stressed short vowels
define pgrmStressedShortVowel [
    á:{*á} | é:{*é} | í:{*í} | ó:{*ó} | ú:{*ú} | ý:{*ý}
];

# Original long vowels
define pgrmLongVowel [
    ā:{*ā} | ē:{*ē} | ī:{*ī} | ō:{*ō} | ū:{*ū} | ô:{*ô}
];

# ADD: Stressed long vowels (redundant macron+acute)
define pgrmStressedLongVowel [
    {ā́}:{*ā́} | {ḗ}:{*ḗ} | {ī́}:{*ī́} | {ṓ}:{*ṓ} | {ū́}:{*ū́}
];

# Original diphthongs
define pgrmDiphthong [
    {ai}:{*ai} | {au}:{*au} | {eu}:{*eu} | {iu}:{*iu}
];

# ADD: Stressed diphthongs
define pgrmStressedDiphthong [
    {áu}:{*áu} | {ái}:{*ái} | {éu}:{*éu} | {íu}:{*íu}
];

# Combined root vowels (for pgrmStrongSyllable)
define pgrmRootVowel [
    pgrmShortVowel | pgrmStressedShortVowel |
    pgrmLongVowel | pgrmStressedLongVowel |
    pgrmDiphthong | pgrmStressedDiphthong
];
```

#### 10.4.3 Strong Syllable Pattern

Modify line ~280:

```foma
define pgrmStrongPlainLight pgrmOnset [pgrmShortVowel | pgrmStressedShortVowel] 0;
define pgrmStrongPlainHeavy [
    pgrmOnset [pgrmLongVowel | pgrmStressedLongVowel | pgrmDiphthong | pgrmStressedDiphthong] pgrmCoda |
    pgrmOnset [pgrmShortVowel | pgrmStressedShortVowel] pgrmCodaNonEmpty
];
```

#### 10.4.4 RemoveStars Update

Modify line ~567 to strip stress marks:

```foma
define RemoveStars [
    {*} -> 0,
    {á} -> {a}, {é} -> {e}, {í} -> {i}, {ó} -> {o}, {ú} -> {u}, {ý} -> {y},
    {à} -> {a}, {è} -> {e}, {ì} -> {i}, {ò} -> {o}, {ù} -> {u},
    {ā́} -> {ā}, {ḗ} -> {ē}, {ī́} -> {ī}, {ṓ} -> {ō}, {ū́} -> {ū},
    {ā̀} -> {ā}, {ḕ} -> {ē}, {ī̀} -> {ī}, {ṑ} -> {ō}, {ū̀} -> {ū}
];
```

### 10.5 Rule Ordering

Insert prosodic rules at appropriate chronological positions:

```
PGmc stage:
  ... (existing)

NWGmc/PWGmc stage:
  ... (existing)
  EarlyIApocope          # NEW — before i-umlaut (Luick §296)
  ... (existing)

Pre-OE stage:
  InterStressRaising     # NEW — compounds only, if implemented
  ... (existing)
  OEIUmlaut
  ... (existing)
```

### 10.6 TSV Migration Strategy

#### 10.6.1 Priority Order

1. **Test words only** — Validate with 5-10 known forms first
2. **Prosodic-sensitive forms** — Forms that currently use transponents (~50)
3. **All simple words** — Bulk update: first vowel → stressed (~650)

#### 10.6.2 Automated Conversion

For simple words (non-compounds, initial stress):
- Replace first vowel with stressed variant
- `a` → `á`, `e` → `é`, `i` → `í`, `o` → `ó`, `u` → `ú`
- `ā` → `ā́`, `ē` → `ḗ`, etc.

For compounds:
- Mark primary stress on first element
- Mark secondary stress on second element
- `*wiră-aldu` → `*wírăn-àldu` (if implementing inter-stress raising)
- Or keep transponent if simpler

#### 10.6.3 Validation Script

```python
# Check that every PROTOFORM has exactly one primary-stressed vowel
# Check that stress is on first syllable (Germanic initial stress)
# Flag exceptions for manual review
```

### 10.7 Testing Plan

1. **Unit tests:** Individual rules in isolation
   - EarlyIApocope: `*júgunθiz → *júgunθz` ✓, `*fṓtiz → *fṓtiz` ✓
   - InterStressRaising: `*wér-àldu → *wér-ùldu` ✓

2. **Integration tests:** Full pipeline
   - `*júgunθ → ġeoguþ` (no i-umlaut because early apocope)
   - `*fṓtiz → fēt` (normal i-umlaut because no early apocope)

3. **Regression tests:** Ensure existing forms still work
   - Batch test all ~700 rows before/after migration

### 10.8 Rollback Plan

Keep the `prosodic-tier-exploration` branch separate. If prosodic tier proves
unworkable, the main branch is unaffected. Transponent workarounds remain valid.

---

## 6. Next Steps (Updated)

1. ~~Research Foma flag diacritics for state tracking~~ (tested, works but awkward)
2. ~~Prototype inline stress markers for early i-apocope~~ (**DONE**)
3. ~~Inventory ALL phenomena and decide if prosodic tier is worth it~~ (**DONE - worth it**)
4. ~~Design implementation~~ (**DONE - see §10**)
5. **NEXT:** Implement Phase 1 — Add symbols to germanic.txt
6. **NEXT:** Implement Phase 2 — Test with 5 known forms
7. **NEXT:** Implement Phase 3 — Bulk TSV migration
8. **NEXT:** Implement Phase 4 — Write prosodic rules
