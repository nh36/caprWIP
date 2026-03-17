# Final Vowel Missing: Analysis of Morphological Alignment Issues

## Problem Statement
38 OE lexemes in the `final_vowel_missing` bucket show missing final vowels compared to expected OE forms. Investigation reveals this is due to **morphological alignment issues** between PGmc proto-forms and OE citation forms.

## Key Finding: Proto-West Germanic Stage

Our TSV contains **PGmc inflected forms** (often nom./acc.sg.), but these need to pass through the **PWGmc stage** where critical morphological changes occurred.

### Example: 'berry'
- **PGmc**: `*bazją` (neut. nom.-acc.sg. ja-stem with nasal vowel)
- **PWGmc**: `*baʀi` (after denasalization and ja-stem reduction)
- **OE**: `berġe` (expected)
- **Our output**: `bierġ` (final vowel lost via apocope)

### Proto-Form Endings in final_vowel_missing (38 cases)

| Proto Ending | Count | Examples | Expected OE Ending |
|--------------|-------|----------|-------------------|
| `*-ją` | ~2 | bazją, xawwją | -e |
| `*-ą` | ~8 | durą, gallą, jērą, skaftą | -a, -e, -u |
| `*-ōn` | ~15 | bugōn, fulōn, sunnōn, namōn | -a, -e |
| `*-ăną` | ~8 | baugjăną, gebăną, xawwăną | -an (but this is infinitive!) |
| Other | ~5 | various | various |

## Critical PWGmc Developments (R/T §3.1)

### 1. Denasalization of Final Nasal Vowels
**R/T §3.1.4 (line 3960)**: "word-final nasal vowels had lost their nasalization" in PWGmc

- PGmc `*-ą` → PWGmc `*-a`
- PGmc `*-ų` → PWGmc `*-u`  
- PGmc `*-ją` → PWGmc `*-ja` (then further changes)

### 2. Ja-Stem Reduction (Light Roots)
**R/T §6.8.2 (line 21868)**: "PWGmc ja-stems with light root syllables had a nom.-acc. sg. in *-i"

- PGmc `*bazją` → PWGmc `*bazi` (with palatal effects on preceding consonant)
- The `*-i` survives to OE as `-e` (after other vowel reductions)

### 3. Weak Noun Endings (ōn-stems)
**Hogg §3.3 (line 6526ff)**: Weak nouns have characteristic endings:
- Masc. n-stem nom.sg: PGmc `*-ōn` → OE `-a` (e.g., `guma` 'man')
- Fem. n-stem nom.sg: PGmc `*-ōn` → OE `-e` (e.g., `sunne` 'sun', `hearpe` 'harp')

Development:
- PGmc `*sunnōn` → PWGmc `*sunnōn` (no change)
- Then nasal loss: `*sunnō-` → `*sunnō`
- Then vowel reduction: `*-ō` → `-e` (fem.) or `-a` (masc.)

## Why Our FST Fails

Our FST treats proto-forms as **PGmc** and applies OE-specific sound changes directly, **skipping the PWGmc stage**:

1. **Apocope rules delete too aggressively**: Our `HighVowelApocope` and `HeavySyllableNasalApocope` delete `*-ą`, `*-i`, `*-u` without first applying PWGmc denasalization and stem-class specific reductions.

2. **No ja-stem reduction**: We don't have rules that convert `*-ją` → `*-i` for light-root ja-stems.

3. **No ōn-stem reduction**: We don't convert `*-ōn` → `-e`/`-a` for weak nouns.

## Morphological Misalignments

Some cases may also reflect **form mismatches**:

### Example: `*baugjăną` → expected `boga`
- `*baugjăną` is an **infinitive** (class II weak verb: *-ōjan-)
- Expected `boga` is a **noun** (bow)
- These are completely different lexemes/forms - likely a **TSV data error**

### Example: `*kōwz` → expected `cū`  
- `*kōwz` is nom.sg. (cow)
- Expected `cū` shows different vowel (ō vs ū) - possible **stem variant** or **paradigmatic mismatch**

## Solution Options

### Option 1: Add PWGmc Intermediary Rules
Add rules that simulate PWGmc developments before OE-specific changes:
- Denasalize final nasal vowels: `*ą → *a`, etc.
- Reduce ja-stems: `*-ją → *-i` (context: light root syllable)
- Reduce ōn-stems: `*-ōn → *-e`/`*-a` (context: weak declension)

**Problem**: Requires morphological awareness (stem class, gender, syllable weight) which our FST lacks.

### Option 2: Update TSV Proto-Forms to PWGmc
Change proto-forms in TSV from PGmc inflected forms to PWGmc forms:
- `*bazją` → `*baʀi`
- `*sunnōn` → `*sunnō` or already-reduced form
- `*durą` → `*dura`

**Problem**: Large-scale TSV revision; may break Germanic-wide comparisons.

### Option 3: Update TSV to Use Consistent Citation Forms
Ensure both proto and OE forms use same morphological base (e.g., both nom.sg., or both stems):
- If proto is nom.sg inflected, OE should be nom.sg
- If proto is stem, OE should be stem or consistently-derived form

**Problem**: Requires linguistic expertise to determine correct forms; may not match Wiktionary sources.

### Option 4: Accept Morphological Mismatches as Data Issues
Mark these 38 cases as **TSV data quality issues** rather than FST problems:
- Flag entries with morphological misalignment
- Focus FST development on purely phonological phenomena
- Address data alignment separately

## Recommendation

**Immediate**: Investigate representative subset of 38 cases to determine:
1. How many are genuine PWGmc stage issues vs. data errors
2. Whether proto-forms should be PWGmc rather than PGmc
3. Whether OE forms are consistently the same morphological form as proto

**Long-term**: Consider adding explicit PWGmc stage to FST pipeline:
- Define PWGmc inventory and developments
- Apply PWGmc → OE changes rather than PGmc → OE
- This aligns with linguistic reality and tightens correspondences
