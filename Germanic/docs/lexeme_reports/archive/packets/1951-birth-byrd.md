# Evidence packet — 1951 birth / byrd

> This packet is evidence for drafting. Do not treat all hits as equally authoritative; prefer high-confidence evidence.

## TSV row data

| ID | CONCEPT | COUNTERPART | PROTO | PROTOFORM | DERIVATION_CLASS | NOTE | HISTORY |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1951 | birth | byrd | *búrdiz | *búrdiz | regular | Kroonen *burdi- f. > OE (ġe)byrd; using simplex without ge- | - |

## Manifest status

_No manifest entry._

## High-confidence evidence

### Compact derivation trace entry

```md
# birth
PROTO: *búrdiz
EXPECTED: byrd
OUTPUTS: byrd



### Proto-Germanic consonant inheritance

Proto Input: *búrdiz

| Earlier Germanic developments | Old English developments |
|:---|:---|
| **Proto-West Germanic**<br>[no change]<br><br>**Northwest Germanic**<br>PGmc Final Z Deletion: *búrdi | **Old English**<br>OE I Umlaut: *byrdi<br>OE High Vowel Apocope: *byrd |



### Orthography & surface

Outcome: byrd

NOTE: Kroonen *burdi- f. > OE (ġe)byrd; using simplex without ge-
```

### Matching oe_known_problems.tsv entries

_None_

### DEV_NOTES hits

_None_

### Analysis and dossier hits

_None_

## Supporting/background evidence

### DEV_NOTES hits

_None_

### Analysis and dossier hits

_None_

### Local lexical-table hits

#### old_english_wiktionary.tsv

| ENGLISH | OE_FORM | SOURCE | DETAIL | PAGE |
| :--- | :--- | :--- | :--- | :--- |
| birth | ġebyrd | text | Old English link | birth |

#### old_english_swadesh.tsv

_None_

## Possibly stale or diagnostic evidence

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:1791 (concept name)

- Nearby heading: ### English sandbox todo — surface accuracy focus

```text
1789: - ~~**Finish weak-tail deletions.** Extend `EnglishSandboxWeakTailReductions` (or add a follow-up cleanup stage) so reduced `{*a/ą}` tails drop the following `n/m/r` and final schwa in stressed monosyllables. This will convert forms like `beɪkeɪnə/bænnə/brændə/blʌdə` into the expected `bake/ban/brand/blood` without manual patches.~~
1790:   - ✅ 2025-12-11: `{*ă}` now flows through `EnglishSandboxWeakTailReductions → EnglishSandboxWeakTailCleanup → EnglishSandboxWeakTailFinalDrop`; `EnglishSandboxNoFinalWeakTail` filters out residual `{*r/n/m}`+`{*ə}`. Tracer (`*bakăną/*bannăn/*brandăz/*blōdą`) shows single surfaces (`beɪk/bæn/brænd/blʌd`), and `tools/english_apply_down_stats.py` reports 333/376 single-output entries (multiple outputs = 0).
1791: - **Back/round proto rhotics earlier.** Expand `EnglishSandboxProtoRhoticFronting` to push `{*e, *i, *o}` toward `{æ, ɪ, ɔ}` before `{*r}` so `*bergą/*bardăz/*barwōn/*burdiz` feed the ME vowel system with the right backness, unlocking `barrow/beard/bier/birth` reflexes.
1792:   - Diagnostics (2025-12-11): `python3 tools/trace_english_sandbox.py --lexeme-file tmp/rhotic_test_set.txt --brace-diphthongs` still yields `*bergą → bæəʊ`, `*bardăz → bɔː`, `*barwōn → bæʋəʊn`, `*erθo → əθ`, `*fuwer → fʌæ`. Current `EnglishSandboxRhoticBreaking` is a grab-bag of lexeme-specific rewrites with `~[?* … ?*]` filters—phonologically unmotivated.
1793:   - Rhotic data audit: 118 English proto entries contain `{r}`; the problematic clusters are `rdă` (4 entries), `rgă` (1), `rwō` (1), `rθo` (1). These align exactly with `tmp/rhotic_test_set.txt`. We need historically grounded rewrites (e.g. `{*rgă → {*rəʊ}}`, `{*rdă → {*ər}}`, `{*rwō → {*rəʊ}}`, `{*erθo → {*erθ}}) before `EnglishSandboxPostVocalicRLoss` deletes `{*r}`.
```

#### Germanic/docs/DEV_NOTES.md:28174 (exact PROTOFORM)

- Nearby heading: ### §17.13.2 Failed naïve sweep (archived, for future-warning)

```text
28172: - `vowel_quality__u_o_alternation` ×22 (e.g. `*búrdą → burd`
28173:   expected `bord`),
28174: - `final_vowel_extra` ×15 (e.g. `*búrdiz → byrde` expected
28175:   `byrd`),
28176: - `final_vowel_missing__weak_noun_like` ×5,
```

#### Germanic/docs/DEV_NOTES.md:28175 (exact COUNTERPART)

- Nearby heading: ### §17.13.2 Failed naïve sweep (archived, for future-warning)

```text
28173:   expected `bord`),
28174: - `final_vowel_extra` ×15 (e.g. `*búrdiz → byrde` expected
28175:   `byrd`),
28176: - `final_vowel_missing__weak_noun_like` ×5,
28177: - plus scattered breaking, palatal, gemination regressions.
```

### Analysis and dossier hits

#### Germanic/docs/analysis/mismatch_dossier_mizdo.md:517 (row ID)

- Nearby heading: ### 6.2 Other *i + rd clusters (rhotacized)

```text
516: **Search results** (from TSV):
517: 1. `*búrdiz` 'birth' (row 1951) → FST: `byrd` ✓
518:    - Expected: `*búrdiz` → u-lowering → `*bordiz` → breaking (blocked, because *o not *e/*i) → i-umlaut `*byrd` ✓
```

#### Germanic/docs/analysis/mismatch_dossier_mizdo.md:518 (exact pair)

- Nearby heading: ### 6.2 Other *i + rd clusters (rhotacized)

```text
517: 1. `*búrdiz` 'birth' (row 1951) → FST: `byrd` ✓
518:    - Expected: `*búrdiz` → u-lowering → `*bordiz` → breaking (blocked, because *o not *e/*i) → i-umlaut `*byrd` ✓
519: 2. `*xérdō` 'herd' (row 2073) → FST: `heord` ✓
```

#### Germanic/docs/analysis/mismatch_dossier_mizdo_supplement.md:556 (exact pair)

- Nearby heading: ### 5.3 Testing the VzC → VːC hypothesis

```text
555: Other *i + rd clusters (after rhotacism):
556: 1. *\*búrdiz* 'birth' → OE *byrd* (no issue; *u lowers, then i-umlaut)
557: 2. *\*xérdō* 'herd' → OE *heord* ✓ (regular breaking of *e → *eo)
```

## Bibliography-key candidates

### Preferred candidates

| Key | Why it was selected |
| :--- | :--- |
| Kroonen2013 | default Proto-Germanic etymology key for Kroonen |

### Low-confidence candidates

| Key | Why it was selected |
| :--- | :--- |
| Kroonen2011 | surname mention only: Kroonen |
| Kroonen2006 | surname mention only: Kroonen |

