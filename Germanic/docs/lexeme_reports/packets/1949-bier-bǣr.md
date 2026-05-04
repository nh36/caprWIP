# Evidence packet — 1949 bier / bǣr

> This packet is evidence for drafting. Do not treat all hits as equally authoritative; prefer high-confidence evidence.

## TSV row data

| ID | CONCEPT | COUNTERPART | PROTO | PROTOFORM | DERIVATION_CLASS | NOTE | HISTORY |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1949 | bier | bǣr | *bḗrō | *bḗrō | regular | Wiktionary: PGmc *bērō > OE bēr/bǣr (bier); *barwōn is wrong lexeme | - |

## Manifest status

_No manifest entry._

## High-confidence evidence

### Compact derivation trace entry

```md
# bier
PROTO: *bḗrō
EXPECTED: bǣr
OUTPUTS: bǣr



### Proto-Germanic consonant inheritance

Proto Input: *bḗrō

| Earlier Germanic developments | Old English developments |
|:---|:---|
| **Proto-West Germanic**<br>[no change]<br><br>**Northwest Germanic**<br>NWGmc Final Long O Raising: *bḗru<br>NWGmc Long E Lowering: *bǣru | **Old English**<br>OE High Vowel Apocope: *bǣr |



### Orthography & surface

Outcome: bǣr

NOTE: Wiktionary: PGmc *bērō > OE bēr/bǣr (bier); *barwōn is wrong lexeme
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
| bier | bēr | inh | template:inh | bier |

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

#### Germanic/docs/DEV_NOTES.md:2296 (concept name)

- Nearby heading: ### Failure buckets & historical targets

```text
2294: - Top-down staging notes before touching code:
2295:   - **Late OE short-vowel conditioning**: finish the FOOT–STRUT stage so `{*u}` first branches to `{ʊ}` in dark-l/velar/alveolar codas, then feeds `{ʌ}` in open or dental contexts; likewise confine the KIT split to nasal/liquid + consonant codas (stop globally rewriting `{e}`).
2296:   - **ME /r/-loss**: add a post-breaking stage that deletes `{r}` after vowels/codas (mirroring historical smoothing) so `{*bōr}` surfaces as `{bɔː}` before Late Reduction derives `board`/`bier` outcomes.
2297:   - **Weak-tail clean-up**: continue driving reductions via `EnglishSandboxWeakTailVowel` so schwa mappings target the templated tails instead of ad-hoc contexts.
2298: - For each block, validate against the relevant bucket from `tmp/english_sandbox_results.json` and log stage traces so the top-down picture stays anchored to the bottom-up error counts.
```

#### Germanic/docs/DEV_NOTES.md:2308 (concept name)

- Nearby heading: ### KIT sweep (status: reverted to baseline)

```text
2306: ### KIT sweep (status: reverted to baseline)
2307: 
2308: - Replayed the dockered `flookup` harness (`python3 - <<'PY' …`) to isolate the true KIT cases (filtering out `aɪ/eɪ/ɔɪ`). We still have 35 `{ɪ}` forms headed by `fish/give/six/will` plus the `{ɪə}`+`r` items (`beard/bier/deer/spear/year`).
2309: - Restored the brace-aware helper sets (`EnglishSandboxPlainVocalic/Liquid/Nasal`), the `{*u}` contexts, and `EnglishSandboxPostVocalicRLoss` after rolling back an experimental smoothing stage that tanked the harness. `english_brace_sandbox.bin` is back to the 179/376 success baseline.
2310: - `python3 server/tools/api_regression.py` remains green, so the sandbox is stable again for the next round of KIT work (detailed smoothing + consonant-cluster contexts).
```

#### Germanic/docs/DEV_NOTES.md:2322 (concept name)

- Nearby heading: ### KIT sweep (WIP)

```text
2320: ### KIT sweep (WIP)
2321: 
2322: - Fed the KIT bucket through the same dockered `flookup` harness (`python3 - <<'PY' …`) after filtering out diphthongs (`aɪ/eɪ/ɔɪ`). The remaining 35 entries are the genuine `{ɪ}` cases headed by `fish/give/six/will` alongside the `{ɪə}` + post-vocalic /r/ cohort (`beard/bier/deer/spear/ year`, etc.).
2323: - Updated `EnglishSandboxCoreVowelRules` so short `{*i}` finally drops its star and enters the plain alphabet, and extended `EnglishSandboxShortVowelSplit` with `{i}`→`{ɪ}` rewrites in closed syllables / word-final contexts. This keeps the KIT conditioning in the same stage as the `{*e}`/{`*u`} splits instead of leaving `{*i}` untouched.
2324: - The attested-form harness still lands at 179/376 successes (KIT bucket = 35) because the stubborn cases need post-vocalic /r/ smoothing (`{ɪ}`→`{ɪə}` before the new `EnglishSandboxPostVocalicRLoss`) or suffixal analogies (`sieve/singe/timber`). Logged them here so the next pass can target `{ɪə}` outputs without sacrificing the `{bəʊn}/{fʊt}` improvements we just landed.
```

#### Germanic/docs/DEV_NOTES.md:2370 (concept name)

- Nearby heading: #### Detailed blueprint (grounded in the standard OE/ME chronology)

```text
2368: 
2369: - **OE breaking + ME smoothing.**
2370:   - Add an `EnglishSandboxOEBreaking` stage: `{æ}` → `{ea}` before `{*rC}` or `{*lC}`, `{e}` → `{eo}` before `{*rC}`, `{i}` → `{ie}` before `{*rC}`. These match the conditions in Campbell §§216–219 and explain why `bear/bier` diverge from `bar`.
2371:   - Follow with an `EnglishSandboxMESmoothing` stage (before post-vocalic /r/ loss) that maps `{ea/eo/ie}` + `{*r}` to the RP nuclei: `{ea}` → `{ɛə}`, `{ie}` → `{ɪə}`, `{eo}` → `{ɜː}` (voicing-dependent). This should replace the lexeme-specific rewrites currently living in `EnglishSandboxRhoticBreaking`.
2372: 
```

### Analysis and dossier hits

_None_

## Bibliography-key candidates

### Preferred candidates

_None_

### Low-confidence candidates

_None_

