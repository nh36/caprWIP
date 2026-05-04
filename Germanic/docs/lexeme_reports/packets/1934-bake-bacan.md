# Evidence packet — 1934 bake / bacan

> This packet is evidence for drafting. Do not treat all hits as equally authoritative; prefer high-confidence evidence.

## TSV row data

| ID | CONCEPT | COUNTERPART | PROTO | PROTOFORM | DERIVATION_CLASS | NOTE | HISTORY |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1934 | bake | bacan | *bákaną | *bákaną | regular | Proto encoding: -aną (full vowel) for A-restoration; R/T §6.3.1 | Source: Wiktionary etymology (template:inh) \| Source: Wiktionary etymology (template:inh) |

## Manifest status

_No manifest entry._

## High-confidence evidence

### Compact derivation trace entry

```md
# bake
PROTO: *bákaną
EXPECTED: bacan
OUTPUTS: bacan



### Proto-Germanic consonant inheritance

Proto Input: *bákaną

| Earlier Germanic developments | Old English developments |
|:---|:---|
| **Proto-West Germanic**<br>[no change]<br><br>**Northwest Germanic**<br>[no change] | **Old English**<br>Anglo Frisian Brightening: *bækaną<br>OE A Restoration: *bakaną<br>OE Heavy Syllable Nasal Apocope: *bakan<br>OE Secondary Nasalization: *bakąn<br>OE Weak Tail Reduction: *bakan |



### Orthography & surface

Outcome: bacan

NOTE: Proto encoding: -aną (full vowel) for A-restoration; R/T §6.3.1
```

### Matching oe_known_problems.tsv entries

_None_

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:21743 (exact pair)

- Nearby heading: #### A. Empirical probes (stems with root `*á`, Class VI strong verb infinitives)

```text
21741: |---|---|---|
21742: | `*bákăną` (breve) | `bæcan` ✗ | AFB fires; A-restoration does NOT fire |
21743: | `*bákaną` (plain) | `bacan` ✓ | AFB fires; A-restoration fires, restoring back `a` |
21744: 
21745: The current TSV has `*bákaną` with plain `a` for exactly this reason — the 10
```

#### Germanic/docs/DEV_NOTES.md:21745 (exact PROTOFORM)

- Nearby heading: #### A. Empirical probes (stems with root `*á`, Class VI strong verb infinitives)

```text
21743: | `*bákaną` (plain) | `bacan` ✓ | AFB fires; A-restoration fires, restoring back `a` |
21744: 
21745: The current TSV has `*bákaną` with plain `a` for exactly this reason — the 10
21746: Class VI strong verbs (`bákaną, grábaną, xláðaną, wádaną, wákaną, wáskaną, …`)
21747: rely on the plain `a` in the infinitival suffix to trigger OEARestoration.
```

### Analysis and dossier hits

#### Germanic/docs/analysis/mismatch_dossier_mizdo_supplement.md:428 (row ID)

- Nearby heading: ### 3.12 Summary of source-by-source findings

```text
427: | Brunner | 1965 | ? | ? | ? | ? |
428: | Holthausen (AeEW) | 1934 | ? | ✓ | ? | ? |
429: | Mayrhofer | 2001 | ✗ (Germanic only) | ✗ | — | — |
```

## Supporting/background evidence

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:36 (note keyword: A-restoration)

- Nearby heading: ### Project status and archived work

```text
34: - [Project Status (as of 2026-03-10)](#project-status-as-of-2026-03-10)
35: - [Consonant Mismatch Bucket Refinement (2026-02-07)](#consonant-mismatch-bucket-refinement-2026-02-07)
36: - [A-Restoration Fix (2026-02-06)](#a-restoration-fix-2026-02-06)
37: 
38: ### Working diary
```

#### Germanic/docs/DEV_NOTES.md:47 (note keyword: A-restoration)

- Nearby heading: ### Polished analyses (Feb–Mar 2026)

```text
45: - [Cognate set 379 "rock" → corrected to "coat"](#cognate-set-379-rock--corrected-to-coat-rukkăz)
46: - [Labiovelar Proto-Form Corrections](#labiovelar-proto-form-corrections-and-post-velar-w-loss-rt-642)
47: - [Water fix: PWGmc ō-shortening](#water-fix-pwgmc-ō-shortening-and-a-restoration-correction-3a45a8b)
48: - [A-restoration: ræst, tæppa, stemn](#a-restoration-in-ō-stems-and-n-stems-ræst-tæppa-stemn-fronting_missing__afb)
49: - [The stefn/stemn Problem](#the-stefnstemn-problem-local-transponent-decision)
```

#### Germanic/docs/DEV_NOTES.md:48 (note keyword: A-restoration)

- Nearby heading: ### Polished analyses (Feb–Mar 2026)

```text
46: - [Labiovelar Proto-Form Corrections](#labiovelar-proto-form-corrections-and-post-velar-w-loss-rt-642)
47: - [Water fix: PWGmc ō-shortening](#water-fix-pwgmc-ō-shortening-and-a-restoration-correction-3a45a8b)
48: - [A-restoration: ræst, tæppa, stemn](#a-restoration-in-ō-stems-and-n-stems-ræst-tæppa-stemn-fronting_missing__afb)
49: - [The stefn/stemn Problem](#the-stefnstemn-problem-local-transponent-decision)
50: - [z-loss/rhotacism and bimoraic/trimoraic cross-source analysis](#historical-phonology-of-final--z-loss-and-its-interaction-with-rhotacism)
```

#### Germanic/docs/DEV_NOTES.md:1649 (note keyword: A-restoration)

- Nearby heading: ## A-Restoration Fix (2026-02-06)

```text
1647: ---
1648: 
1649: ## A-Restoration Fix (2026-02-06)
1650: 
1651: **Summary:** Fixed critical foma syntax bug causing A-restoration to apply unconditionally, 
```

#### Germanic/docs/DEV_NOTES.md:1651 (note keyword: A-restoration)

- Nearby heading: ## A-Restoration Fix (2026-02-06)

```text
1649: ## A-Restoration Fix (2026-02-06)
1650: 
1651: **Summary:** Fixed critical foma syntax bug causing A-restoration to apply unconditionally, 
1652: then implemented chronology fix to move apocope after restoration.
1653: 
```

#### Germanic/docs/DEV_NOTES.md:1704 (note keyword: A-restoration)

- Nearby heading: ## A-Restoration Fix (2026-02-06)

```text
1702:   - Also expanded `OldEnglishARestorationBackVowel` to include `{*ă}` and `{*ą}` (reduced back vowels),
1703:     and expanded `OldEnglishARestorationStrongOTail` to include common weak-tail patterns where
1704:     A-restoration should still apply (infinitives, agent nouns, etc.).
1705:   - Result: `fronting_missing_no_trigger` dropped from 30 to 11 (19 words fixed).
1706: - Top mismatch counts (2026-02-06 report; 280 total at the time):
```

#### Germanic/docs/DEV_NOTES.md:1720 (exact COUNTERPART)

- Nearby heading: ## A-Restoration Fix (2026-02-06)

```text
1718:   - **Palatalization missing**: *bōkō (beech) never triggers `VelarPalatalization`; output `bōcō` vs expected `bēċe`. In the trace there is no fronting stage that would supply the trigger, so this is likely a rule/chronology or etymon/expected mismatch.
1719: - Measured ARestoration intervening segments (2026-02-05, OE sandbox):
1720:   - True positives (31 items): top intervening segments `n, k, w, d, j` (e.g., *bakăną -> bacan, inter=`k`; *xanduz -> hand, inter=`nd`).
1721:   - False positives (16 items): top intervening segments `r, s, t, n, p` (e.g., *nadrō -> nǣdre, inter=`dr`; *bastą -> bæst, inter=`st`; *farăną -> fær, inter=`r`).
1722: - Candidate next actions:
```

#### Germanic/docs/DEV_NOTES.md:2427 (exact COUNTERPART)

- Nearby heading: ### PGmc→OE TODOs (consolidated)

```text
2425: - **Proto gate coverage:** `xw/hw` clusters already pass `EnglishProtoInput`; remaining ProtoInput failures are elsewhere (e.g., `*xabukăz`, `*xemenăz`, `*xnakkăz`, `*regna-bugōn`, `*sumerăz`). Focus on missing onset/weak‑tail clusters, not `xw/hw`.
2426: - **High‑vowel apocope expansion:** broaden final `*i/*u` deletion beyond the current “long/diphthong + C” and “two light syllables” conditions; target observed `-i/-u` outputs (e.g., `ballu/bebru/balgi/bugu/crafti/fehu/felþu`) while staying phonetic.
2427: - **Weak‑tail cleanup (`-ana` → `-an`):** reshape or drop weak‑tail `ă/ą` endings in verbs so outputs like `bacana/gennana/brecana/brengana/brūcana` converge on attested `-an`.
2428: - **OE consonant innovations:** add the missing PGmc→OE consonant changes (palatalisation in OE contexts, rhotic prep, targeted lexical replacements) so stage outputs align with `COUNTERPART` without using ME/RP rules.
2429:   - Early final‑ă apocope (post‑z deletion) now in place; `*dagăz` yields `dæġ`. See potential side‑effects list at `docs/debug_snapshots/oe_final_a_apocope_side_effects_2025-12-23.txt`.
```

#### Germanic/docs/DEV_NOTES.md:2478 (exact COUNTERPART)

- Nearby heading: ### OE evaluator snapshot (old_english.bin)

```text
2476: - No output: 21
2477: - Mismatches: 353
2478: - Sample mismatches: `*bakăną -> bacana` vs `bacan`, `*bōkō -> bucō` vs `bēċe`, `*balgiz -> balgi` vs `bielġ`.
2479: - Common issue bucket still dominated by `-ana` outputs and lingering final high vowels.
2480: 
```

#### Germanic/docs/DEV_NOTES.md:2485 (exact COUNTERPART)

- Nearby heading: ### Ending diagnostics (old_english.bin)

```text
2483: - Final high vowels: `i` 22, `u` 20; most common contexts `ti/di` for `-i`, `þu/du/tu` for `-u`.
2484: - Sample `-i/-u` outputs: `ballu` (ball), `bebru` (beaver), `balgi` (belly), `crafti` (craft), `bugu` (bough).
2485: - Sample `-ana` outputs where target is `-an`: `bacana` (bake), `gennana` (begin), `brecana` (break), `brengana` (bring), `brūcana` (brook).
2486: 
2487: ### OE diagnostics refresh (2025-12-21)
```

#### Germanic/docs/DEV_NOTES.md:3151 (exact COUNTERPART)

- Nearby heading: ### Impact

```text
3149: ### Impact
3150: - No regressions. 106 mismatches (unchanged). Health check clean.
3151: - All A-restoration-dependent forms verified: bacan, wadan, wascan, hlaþan, grafan, ġeall, hamer all correct.
3152: 
3153: ---
```

#### Germanic/docs/DEV_NOTES.md:9188 (exact COUNTERPART)

- Nearby heading: ### The Problem

```text
9186: 
9187: - FST: `*bakaną` → `bacen` (wrong)
9188: - Expected: `*bakaną` → `bacan` (correct per R/T)
9189: 
9190: The `-an-` in strong verb infinitives is being fronted to `-en-`.
```

### Analysis and dossier hits

#### Germanic/docs/analysis/arestoration_r_l_research.md:1 (note keyword: A-restoration)

- Nearby heading: # A-Restoration in Old English: the role of intervening *r and *l

```text
1: # A-Restoration in Old English: the role of intervening *r and *l
2: 
```

#### Germanic/docs/analysis/arestoration_r_l_research.md:81 (exact COUNTERPART)

- Nearby heading: ### 2.1 Campbell, *Old English Grammar* (1959) — file `campbell_old_english_grammar.txt`

```text
80: 
81: > § 158. The restoration of *a* is common before all single consonants and geminates, e.g. *faran* go, *calan* be cold, *bacan* bake, *gnagan* gnaw, *grafan* dig, *stapol* pillar, *sadol* saddle, *latost* latest, *lapode* he invited, *cassoc* rough grass, *hassuc* the same, *mattoc* mattock, *hnappian* fall asleep, *racca* cord, *lappa* skirt.
82: >
```

#### Germanic/docs/analysis/compound_archaism_inventory.md:188 (note keyword: A-restoration)

- Nearby heading: ### Case 8: *rastō (rest) — ræst / ræste

```text
187: | **OE NOM.SG. (STANDARD)** | `ræst` (attested as dictionary headword; shows **paradigmatic leveling** from oblique *-æ-* stem) |
188: | **OE OBLIQUE (GEN.SG./ACC.SG./DAT.SG.)** | `ræste` (front vowel throughout, no A-restoration) |
189: | **Sound changes** | AFB (A-restoration trigger = back vowel in suffix *-u*; fires in nom.sg., blocked in obliques with front *-æ*, *-e*) |
```

#### Germanic/docs/analysis/compound_archaism_inventory.md:189 (note keyword: A-restoration)

- Nearby heading: ### Case 8: *rastō (rest) — ræst / ræste

```text
188: | **OE OBLIQUE (GEN.SG./ACC.SG./DAT.SG.)** | `ræste` (front vowel throughout, no A-restoration) |
189: | **Sound changes** | AFB (A-restoration trigger = back vowel in suffix *-u*; fires in nom.sg., blocked in obliques with front *-æ*, *-e*) |
190: | **Lautgesetzlich output** | `rast` (nom.sg., from A-restoration + apocope) BUT oblique cells show `ræste` (front *æ* from AFB, no restoration) |
```

#### Germanic/docs/analysis/compound_archaism_inventory.md:190 (note keyword: A-restoration)

- Nearby heading: ### Case 8: *rastō (rest) — ræst / ræste

```text
189: | **Sound changes** | AFB (A-restoration trigger = back vowel in suffix *-u*; fires in nom.sg., blocked in obliques with front *-æ*, *-e*) |
190: | **Lautgesetzlich output** | `rast` (nom.sg., from A-restoration + apocope) BUT oblique cells show `ræste` (front *æ* from AFB, no restoration) |
191: | **Attested simplex** | `ræst` (standard headword, showing paradigmatic leveling of oblique *-æ-* back to nom.sg.) |
```

#### Germanic/docs/analysis/notable_findings.md:13 (note keyword: A-restoration)

- Nearby heading: ## Table of Contents

```text
12: 3. [PWGmc \*j-related sound changes: formalization of under-specified rules](#3-pwgmc-j-related-sound-changes-formalization-of-under-specified-rules)
13: 4. [A-restoration trigger set: {*æ} is NOT a trigger](#4-a-restoration-trigger-set-æ-is-not-a-trigger)
14: 5. [The stefn/stemn problem: transponent versus reconstruction](#5-the-stefnstemn-problem-transponent-versus-reconstruction)
```

#### Germanic/docs/analysis/notable_findings.md:634 (note keyword: A-restoration)

- Nearby heading: ## 4. A-restoration trigger set: {*æ} is NOT a trigger

```text
633: 
634: ## 4. A-restoration trigger set: {*æ} is NOT a trigger
635: 
```

#### Germanic/docs/analysis/notable_findings.md:638 (note keyword: A-restoration)

- Nearby heading: ## 4. A-restoration trigger set: {*æ} is NOT a trigger

```text
637: 
638: **Background:** A-restoration (R/T §6.3.1) retracts stressed *æ → *a when
639: a back vowel follows in the next syllable. After Anglo-Frisian Brightening
```

#### Germanic/docs/analysis/unstressed_e_o_before_r.md:100 (note keyword: A-restoration)

- Nearby heading: ### A-restoration — RULED OUT for unstressed syllables

```text
99: 
100: ### A-restoration — RULED OUT for unstressed syllables
101: 
```

#### Germanic/docs/analysis/unstressed_e_o_before_r.md:103 (note keyword: A-restoration)

- Nearby heading: ### A-restoration — RULED OUT for unstressed syllables

```text
102: R/T §6.3.1: "those **stressed** \*æ which were immediately followed by a single
103: or geminate consonant... followed by a back vowel became a." A-restoration
104: explicitly applies to **stressed** vowels only. It would not affect the unstressed
```

#### Germanic/docs/analysis/ws_vs_anglian_dialect_differences.md:391 (note keyword: A-restoration)

- Nearby heading: ## 4. Retraction and a-restoration

```text
390: 
391: ## 4. Retraction and a-restoration
392: 
```

#### Germanic/docs/analysis/ws_vs_anglian_dialect_differences.md:393 (note keyword: A-restoration)

- Nearby heading: ## 4. Retraction and a-restoration

```text
392: 
393: a-restoration: Prim. OE `æ` reverts to `a` in open syllables when a back
394: vowel follows in the next syllable. Campbell §157 introduces this as "one
```

#### Germanic/docs/analysis/ws_vs_anglian_dialect_differences.md:419 (note keyword: A-restoration)

- Nearby heading: ## 4. Retraction and a-restoration

```text
418: fronting of /a/ to /a/ or /æ/" — i.e. this is the input to second fronting
419: (see §6 below), distinct from a-restoration proper.
420: 
```

### Local lexical-table hits

#### old_english_wiktionary.tsv

| ENGLISH | OE_FORM | SOURCE | DETAIL | PAGE |
| :--- | :--- | :--- | :--- | :--- |
| bake | bacan | inh | template:inh | bake |

#### old_english_swadesh.tsv

_None_

## Possibly stale or diagnostic evidence

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:1789 (concept name)

- Nearby heading: ### English sandbox todo — surface accuracy focus

```text
1787: ### English sandbox todo — surface accuracy focus
1788: 
1789: - ~~**Finish weak-tail deletions.** Extend `EnglishSandboxWeakTailReductions` (or add a follow-up cleanup stage) so reduced `{*a/ą}` tails drop the following `n/m/r` and final schwa in stressed monosyllables. This will convert forms like `beɪkeɪnə/bænnə/brændə/blʌdə` into the expected `bake/ban/brand/blood` without manual patches.~~
1790:   - ✅ 2025-12-11: `{*ă}` now flows through `EnglishSandboxWeakTailReductions → EnglishSandboxWeakTailCleanup → EnglishSandboxWeakTailFinalDrop`; `EnglishSandboxNoFinalWeakTail` filters out residual `{*r/n/m}`+`{*ə}`. Tracer (`*bakăną/*bannăn/*brandăz/*blōdą`) shows single surfaces (`beɪk/bæn/brænd/blʌd`), and `tools/english_apply_down_stats.py` reports 333/376 single-output entries (multiple outputs = 0).
1791: - **Back/round proto rhotics earlier.** Expand `EnglishSandboxProtoRhoticFronting` to push `{*e, *i, *o}` toward `{æ, ɪ, ɔ}` before `{*r}` so `*bergą/*bardăz/*barwōn/*burdiz` feed the ME vowel system with the right backness, unlocking `barrow/beard/bier/birth` reflexes.
```

#### Germanic/docs/DEV_NOTES.md:9538 (concept name)

- Nearby heading: ### Empirical Validation (Dry Run 2026-03-13)

```text
9536: **Mismatch count:** 78 → 79 (net +1 WORSE)
9537: 
9538: - **Fixed: 6** (bake, grave, wade, wake, wash, will)
9539: - **Regressed: 9** (craft, day, mast, raven, staff, tap, wain, lap, wasp)
9540: 
```

#### Germanic/docs/DEV_NOTES.md:30394 (concept name)

- Nearby heading: ###### §158 (the consonant-environment statement — *the* relevant statement, ref. line 4727ff.)

```text
30392: 
30393: > The restoration of *a* is **common before all single consonants and
30394: > geminates**, e.g. *faran* go, *calan* be cold, *bacan* bake, *gnagan*
30395: > gnaw, *grafan* dig, ***stapol*** pillar, ***sadol*** saddle, *latost*
30396: > latest, *lapode* he invited, *cassoc* rough grass, *hassuc* the same,
```

#### Germanic/docs/DEV_NOTES.md:36531 (concept name)

- Nearby heading: ### §17.25.2 The canonical conditioning of A-restoration (literature consensus)

```text
36529: | Source | Page / § | Quotation (verbatim) |
36530: |---|---|---|
36531: | Campbell §158 | 4733-4753 | "The restoration of *a* is common before all single consonants and geminates, e.g. *faran* go, *calan* be cold, *bacan* bake, *gnagan* gnaw, *grafan* dig, *stapol* pillar, *sadol* saddle […]. *a* is commonly restored also before groups consisting of *f* or *s* followed by another consonant […]. Before other groups, *a* is not restored except for a few instances before consonant plus liquid." |
36532: | Campbell §159 | 4754-4760 | "[…] weak verbs in *-i-* (< *-ói-*), *lapian, macian, hnappian*, &c." (i.e. class II) |
36533: | R/T vol. II §6.3.1 | 10987-11008 | "After breaking had run its course, those stressed *æ* which were immediately followed by a single or geminate consonant or **sC-cluster** which was in turn followed by a back vowel became *a*." |
```

### Analysis and dossier hits

_None_

## Bibliography-key candidates

### Preferred candidates

| Key | Why it was selected |
| :--- | :--- |
| Campbell1959 | single available key for Campbell |
| Mayrhofer1992 | single available key for Mayrhofer |

### Low-confidence candidates

_None_

