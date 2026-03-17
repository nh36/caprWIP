# Investigation: *kōwz "cow" — Root Noun Paradigm and TSV Fix Options

## Current TSV state

- **IDs**: 1091 (German), 1092 (English), 1093 (Dutch), 1980 (Old English)
- **PROTO**: `*kōwz` (all 4 rows)
- **OE target**: `cū`
- **Pipeline result**: `kōwz → +?` (fails)
- **Source**: Wiktionary (noted in OE row)

The `-w-` in `*kōwz` is **spurious** — neither Kroonen nor R/T reconstruct it.

## Kroonen's reconstruction (*kō- ~ *ku-)

Kroonen (p. 299, line 18098):

> *kō- ~ *ku- f. 'cow' — ON kyr f. 'id.', OE cū, pl. cȳ f. 'id.', OFri. kū f. 'id.', OS kō f. 'id.', Du. koe c. 'id.', OHG kuo f. 'id.', G Kuh f. 'id.'
>
> A root noun continuing the common IE word for 'cow'. Germanic has two different root variants, i.e. *kō- and *kū-, both of which belonged to an originally ablauting paradigm **nom. *kōz, obl. *kū-**, continuing a PIE u-stem *gʷéh₃-u-s, obl. *gʷh₃-u-.

Key points:
- Full-grade stem: *kō- (nominative)
- Zero-grade stem: *kū- (oblique cases)
- Both are PIE-inherited ablaut grades, not analogical innovations

## R/T's reconstruction

### PWGmc nominative (vol. 2, line 5468)

> PNWGmc *kūaz 'cow' (?; ON kyr) > PWGmc *kuz (?) > OE cū.

R/T propose that the zero-grade stem *kū- was already generalized to the nominative in PNWGmc, giving *kūaz (with nom. ending *-az). After loss of final *-z in monosyllables, this yields PWGmc *kūz → OE cū.

The question marks indicate uncertainty about the MECHANISM (why final *-z was lost) — not that the form is unattested. R/T discuss several scenarios for final *-z loss in monosyllables in the same passage (pp. 85–87).

### Root noun endings in PWGmc (line 7100)

> Whatever the nom. sg. ending of root nouns might have been in PGmc, it is reasonable to suppose that there was no ending in PWGmc, as none of the daughters exhibits any.

This means PWGmc nom.sg. of root nouns was endingless: *fōt, *tand, *naht, *mūs — and *kū.

### OE paradigm of cū (§6.6.1, line 18238)

> The root-noun cū 'cow' likewise exhibits dat. sg., nom.-acc. pl. cȳ < *cūi, dat. pl. cūm < *cūm, and apparently gen. sg. cā < *cūiz.

So the attested OE paradigm is:
- **nom.sg.** cū (< leveled *kū, analogical from oblique)
- **dat.sg.** cȳ (< *kūi, regular i-umlaut: ū → ȳ)
- **nom.-acc.pl.** cȳ (< *kūiz, same i-umlaut)
- **gen.sg.** cā (< *kūiz? — form uncertain, R/T say "apparently")
- **dat.pl.** cūm (< *kūm(az))

### Hall's Concise Anglo-Saxon Dictionary

Hall's confirms:
- gen.sg. cū(e), cȳ, or cūs (multiple competing forms — inherited umlaut cȳ vs. analogical -e/-s from other classes)
- dat.sg. cȳ
- nom.-acc.pl. cȳ
- dat.pl. cūm

This matches R/T's §7 observation (line 21452): "The ō-stem gen. sg. ending -e has spread to fem. root-nouns, where it is in competition with the inherited endingless form with i-umlaut."

## Full PGmc paradigm reconstruction (Wiktionary + Kroonen + R/T)

| Case | PGmc | OE (attested) | Derivation |
|------|------|--------|------------|
| nom.sg. | *kōz | cū | NOT lautgesetzlich — cū has zero-grade *kū-, but nom. was full-grade *kō- |
| acc.sg. | *kōų | cū | Possibly regular (acc. *kōų > *kū after loss of *-ų?), but uncertain |
| gen.sg. | *kūiz | cā (or cȳ, cū(e)) | cȳ would be regular i-umlaut; cā is uncertain |
| dat.sg. | *kūi | cȳ | **Lautgesetzlich**: i-umlaut ū → ȳ, then contraction/loss of *-i |
| nom.pl. | *kōiz | cȳ | Mixed: zero-grade stem + umlaut (analogical from oblique?) |
| dat.pl. | *kūmaz | cūm | Regular |

## Pipeline test results

```
kōwz  → +?      (current TSV — fails, -w- is spurious)
kōz   → cu      (correct PGmc nom. — but OE output has short vowel, wrong)
kūz   → cū  ✓   (R/T's PWGmc nom. — CORRECT output)
kūi   → cȳe     (PGmc dat.sg. — close to cȳ but has extra -e)
kūiz  → cȳe     (PGmc gen.sg. — same issue)
kūmaz → +?      (PGmc dat.pl. — fails)
```

For comparison, other root nouns with dat.sg. *-i:
```
mūsi  → mȳs  ✓  (mouse: consonant between root vowel and -i)
fōti  → fēt  ✓  (foot: consonant between root vowel and -i)
naxti → niht  ✓  (night: consonant between root vowel and -i)
```

The pipeline handles root noun oblique forms correctly WHEN there is an intervening consonant. For *kūi (vowel-final stem + *-i), the pipeline produces cȳe instead of cȳ because the final *-i surfaces as -e rather than being absorbed by contraction. This is a pipeline limitation specific to vowel hiatus in root nouns.

## Options for TSV fix

### Option A: PWGmc *kūz → OE cū

- **Proto**: `*kūz` (R/T's PWGmc reconstruction, line 5468)
- **OE target**: `cū` (nom.sg., unchanged)
- **Pipeline**: `kūz → cū` ✓
- **Pro**: Pipeline works. R/T explicitly reconstruct this form. OE target stays as the most common form.
- **Pro**: Dutch koe, German Kuh, English cow can all be derived from the same leveled *kū- stem.
- **Con**: The user initially objected to *kūz as "a form that never existed." However, R/T DO reconstruct it (albeit with ?). It's the zero-grade stem generalized to nominative — a real historical development, not an invented form.
- **Note**: R/T's ? marks are about the MECHANISM of final *-z loss (several competing theories), not about whether *kūz existed as a form.

### Option B: PGmc dat.sg. *kūi → OE cȳ

- **Proto**: `*kūi` (PGmc dative singular)
- **OE target**: `cȳ` (dat.sg., well-attested)
- **Pipeline**: `kūi → cȳe` ✗ (has extra -e)
- **Pro**: Clearly lautgesetzlich per R/T §6.6.1. Both proto and OE are oblique forms. Satisfies the user's requirement of "oblique PGmc form + oblique OE form."
- **Con**: Pipeline produces wrong output (cȳe not cȳ). Would need a pipeline fix for vowel-hiatus contraction, OR we accept the mismatch.
- **Con**: Dutch koe, German Kuh are nominatives — would create paradigm-cell inconsistency across language rows (unless we also change their targets to dative forms, which are identical to nominative in modern Dutch/German).

### Option C: Mark as documented exception

- **Proto**: Fix to `*kōz` (correct PGmc nom. per Kroonen)
- **OE target**: Keep `cū`
- **Pipeline**: `kōz → cu` ✗ (mismatch stays)
- **Pro**: Intellectually honest. OE cū IS from analogical paradigm leveling. Fixes the spurious -w-.
- **Con**: Doesn't reduce mismatch count. Item stays in TSV-fixable bucket.

### Option D: *kūz with explanatory note (= Option A + documentation)

Same as Option A but with a detailed NOTE in the TSV explaining:
- The PGmc root noun had ablaut: nom. *kōz, obl. *kū-
- OE leveled the zero-grade *kū- to all cases
- PWGmc *kūz is R/T's reconstruction (vol. 2, line 5468)
- The form tests the pipeline's handling of the *kū- stem

## Resolution: Option B implemented (commit 6763b73)

**Option B was chosen** — the theoretically satisfying approach with oblique forms on both sides.

### Pipeline fix
The limitation was that `OEHighVowelApocope` required `OEAnyConsonant+` between the long vowel and final `{*i}`. Added a new rule line:
```
{*i} -> 0 || EnglishStarLongVowel _ .#.
```
This handles R/T §6.6.1 vowel-hiatus contraction in root nouns (and is consistent with the existing *fūri → fȳre treatment).

After fix: `kūi → cȳ` ✓

### TSV changes
- **OE row (ID 1980)**: proto `*kūi`, target `cȳ` (PGmc dat.sg. → OE dat.sg., lautgesetzlich)
- **Du/En/De rows**: proto `*kōz` (correct PGmc nom.sg. per Kroonen; spurious `-w-` removed)

Mismatches: 121 → 120.

## References

- Kroonen, Guus. *Etymological Dictionary of Proto-Germanic*. Leiden: Brill, 2013. s.v. *kō- ~ *ku-.
- Ringe, Don & Ann Taylor. *A Linguistic History of English, Volume II*. Oxford, 2014.
  - §3.1.3, line 5468 (PNWGmc *kūaz)
  - §4.2.1, line 7100 (root noun endings in PWGmc)
  - §6.6.1, line 18238 (OE cū paradigm)
  - §7.2.1, line 21452 (gen.sg. -e spread)
- Hall, J.R.C. *A Concise Anglo-Saxon Dictionary*. 4th ed. Cambridge, 1960. s.v. cū.
- Campbell, A. *Old English Grammar*. Oxford, 1962. §§252–5.
