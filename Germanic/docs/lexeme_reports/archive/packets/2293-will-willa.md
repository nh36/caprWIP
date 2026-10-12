# Evidence packet — 2293 will / willa

> This packet is evidence for drafting. Do not treat all hits as equally authoritative; prefer high-confidence evidence.

## TSV row data

| ID | CONCEPT | COUNTERPART | PROTO | PROTOFORM | DERIVATION_CLASS | NOTE | HISTORY |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2293 | will | willa | *wéljô | *wéljô | regular | Kroonen *weljan- 2 m. 'will, wish' → OE willa m.; cf. G Wille, Du. wil (noun); willan is the verb 'to want' (belongs with *waljăną) | - |

## Manifest status

_No manifest entry._

## High-confidence evidence

### Compact derivation trace entry

```md
# will
PROTO: *wéljô
EXPECTED: willa
OUTPUTS: willa



### Proto-Germanic consonant inheritance

Proto Input: *wéljô

| Earlier Germanic developments | Old English developments |
|:---|:---|
| **Proto-West Germanic**<br>PWGmc J Gemination: *wélljô<br><br>**Northwest Germanic**<br>[no change] | **Old English**<br>OE I Umlaut: *willjô<br>OE Unstressed Long Vowel Shortening: *willja<br>OE J Loss After Heavy: *willa |



### Orthography & surface

Outcome: willa

NOTE: Kroonen *weljan- 2 m. 'will, wish' → OE willa m.; cf. G Wille, Du. wil (noun); willan is the verb 'to want' (belongs with *waljăną)
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
| will | willan | inh | template:inh | will |

#### old_english_swadesh.tsv

_None_

## Possibly stale or diagnostic evidence

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:606 (concept name)

- Nearby heading: ### Research on blocking medial u → o in labial environments (2026-03-21)

```text
604: 4. Campbell's preservation conditions cluster around labial/rounded environments
605: 
606: We will block `OEMedUnstressedULowering` when medial `*u` is immediately preceded or 
607: followed by `*w`. This is a conservative, empirically-driven fix.
608: 
```

#### Germanic/docs/DEV_NOTES.md:1789 (concept name)

- Nearby heading: ### English sandbox todo — surface accuracy focus

```text
1787: ### English sandbox todo — surface accuracy focus
1788: 
1789: - ~~**Finish weak-tail deletions.** Extend `EnglishSandboxWeakTailReductions` (or add a follow-up cleanup stage) so reduced `{*a/ą}` tails drop the following `n/m/r` and final schwa in stressed monosyllables. This will convert forms like `beɪkeɪnə/bænnə/brændə/blʌdə` into the expected `bake/ban/brand/blood` without manual patches.~~
1790:   - ✅ 2025-12-11: `{*ă}` now flows through `EnglishSandboxWeakTailReductions → EnglishSandboxWeakTailCleanup → EnglishSandboxWeakTailFinalDrop`; `EnglishSandboxNoFinalWeakTail` filters out residual `{*r/n/m}`+`{*ə}`. Tracer (`*bakăną/*bannăn/*brandăz/*blōdą`) shows single surfaces (`beɪk/bæn/brænd/blʌd`), and `tools/english_apply_down_stats.py` reports 333/376 single-output entries (multiple outputs = 0).
1791: - **Back/round proto rhotics earlier.** Expand `EnglishSandboxProtoRhoticFronting` to push `{*e, *i, *o}` toward `{æ, ɪ, ɔ}` before `{*r}` so `*bergą/*bardăz/*barwōn/*burdiz` feed the ME vowel system with the right backness, unlocking `barrow/beard/bier/birth` reflexes.
```

#### Germanic/docs/DEV_NOTES.md:1835 (concept name)

- Nearby heading: ### Proto rhotic fronting + short back lowering staged (2025-12-07 PM)

```text
1833: - Added `EnglishSandboxProtoRhoticFronting` (right after `EnglishSandboxUrRounding`) so the old `{*a -> æ || _ {*r}}` rewrite now happens in its own historical slot. Reran the core probe trace; `*bergą` finally shows `{bæ…}` at the new stage before rhotic loss, confirming the stage fires once and feeds downstream rules cleanly.
1834: - Introduced `EnglishSandboxShortBackLowering` for the blanket `{*o -> ɔ}` mapping. This keeps short back vowels out of `EnglishSandboxCoreVowelRules` and gives us another checkpoint before the short-vowel split. Staged binaries saved (`english_sandbox_after_proto_rhotic_fronting.bin`, `english_sandbox_after_short_back_lowering.bin`).
1835: - Recompiled via `docker compose exec backend … foma -f fsts/english_brace_sandbox.txt` and captured an updated probe log (`docs/debug_snapshots/english_tracer_log_core_audit_post_rhotic.txt`). Highlights: `*stānaz` now reaches `{təʊ/taɪ/teɪ}` options ahead of weak tails, `*bergą` fronts to `{bæ…}` before `{*r}` disappears, and the short `{o}` forms (`*fulkaz`, `*fothą`) stay deterministic through the new stage. Analyzer coverage still sits at 146/376 (not rerun); next change will be the `EnglishSandboxLengthRealisation` stage so `{*ā/*ō/…}` leave the macro alphabet before Great Vowel Shift.
1836: 
1837: ### Star-preserving vowel cascade + STRUT probes (late 2025-12-07)
```

#### Germanic/docs/DEV_NOTES.md:1851 (concept name)

- Nearby heading: ### English ConsonantRules made deterministic

```text
1849: - Captured a tracer snapshot at `docs/debug_snapshots/english_tracer_log_2025-12-06c.txt`. `*bendaną` now flows through ConsonantRules unchanged and reaches Surface, while `*fiskaz` rewrites `{*z}`→`{r}` deterministically.
1850: - Next actions: tackle the remaining vowel-stage issues (KIT/FOOT splits, schwa reductions, rhotic chronology) so the “Surface but mismatched IPA” bucket starts converting into real successes before revisiting ProtoInput compounds.
1851: - Follow-up audit (logs at `docs/debug_snapshots/english_tracer_log_2025-12-06f.txt`) showed that naive rhotic/weak-tail rewrites tanked coverage, so for now only two safe tweaks remain live: short proto `{*a}` now fronts to `{æ}` by default, and `{*ą}` weak tails convert to `{əʊ}` in `EnglishSandboxWeakTailReductions`. Analyzer coverage is still 205/376, but at least the tail vowels surface as `{…əʊ}` for forms like `*gebaną/*br{au}dą`, which will make future schwa/diphthong work easier to verify.
1852: 
1853: ### Rhotic colouring prototype (2025-12-06 — evening)
```

#### Germanic/docs/DEV_NOTES.md:2029 (concept name)

- Nearby heading: ### Diphthong tokenization note

```text
2027: 
2028: - `pgrmDiphthong` currently maps `{ai} → {*ai}`, `{au} → {*au}`, etc., so the input alphabet includes literal braces. When we tried to consume that via `pgrmDiphthong.r`, `apply down ai` failed because Foma still expects the literal `{ai}` token. Likewise, wrapping `ai` in braces at the CLI (`apply down {ai}`) also fails—the config isn’t using the Burmish-style multichar symbol declarations.
2029: - A clean refactor will probably look like Burmish: declare the multichar symbols up front (so `{ai}` becomes an atomic symbol), normalize the proto lexicon to emit those tokens, then replace the `GermanStar*` macros with `.r` projections. Until that groundwork is in place, the hard-coded `[ {*ai} | … ]` list needs to stay, or the contexts lose sight of the diphthongs.
2030: 
2031: # Daily Hand-off Notes
```

#### Germanic/docs/DEV_NOTES.md:2079 (concept name)

- Nearby heading: ### Surface Filter (Brace status)

```text
2077: ### Surface Filter (Brace status)
2078: - Brace retarget is complete for the German cascade (surface and intermediate stages all use `{*…}`); English/Dutch still need to be converted.
2079: - Spent most of the session ping-ponging between brace and plain-IPA surface filters; each variant worked in isolation but failed once composed with `GermanReflexes`. The takeaway is that half measures don’t work: either the entire pipeline lives in the brace alphabet (like Burmish) or it will keep collapsing at the final filter.
2080: - We now commit to the brace strategy for Germanic as well. The current files still reflect the older IPA experiments, but the next window will rebuild **every stage** (ProtoWord downward, plus surface filter) so braces are baked in consistently.
2081: 
```

### Analysis and dossier hits

#### Germanic/docs/analysis/arestoration_r_l_research.md:703 (concept name)

- Nearby heading: ### 10.6 What about *appla, accras*?

```text
702: 
703: Campbell §158 lists *appla, accras* as the surviving *a*-forms of *Cr/Cl* clusters. Under the recommended change these will *not* be produced by sound change (intervening `*pl/*kr` not in set); they would have to be input-specified in the lexicon as exceptional. This is consistent with Luick §161.4 ("nur in wenigen Resten") and §161 Anm. 5 (the few survivals are due to a *failure* of analogical levelling, not a productive sound-change pathway). No regression is expected for the FST's current rule already produces *æpplas, æcras* in its general behaviour.
704: 
```

#### Germanic/docs/analysis/dill_stem_class_investigation.md:74 (concept name)

- Nearby heading: ## Literature to consult (waiting for user)

```text
73: 1. **Kluge, F.** *Etymologisches Wörterbuch der deutschen Sprache*. 24th ed. (2002). s.v. Dill.
74:    - Will show what stem is reconstructed for the German form
75: 2. **EWAhd** (*Etymologisches Wörterbuch des Althochdeutschen*). s.v. tilli.
```

#### Germanic/docs/analysis/notable_findings.md:921 (concept name)

- Nearby heading: ## 5. The stefn/stemn problem: transponent versus reconstruction

```text
920: 
921: **Future plan:** When OHG and Gothic transducers are built, this word will
922: serve as a cross-branch test case. If a single PGmc form can feed all
```

#### Germanic/docs/dossiers/widuwe-u-preservation.md:571 (concept name)

- Nearby heading: ## §7. Honest residual uncertainty

```text
570:    alone. If the TSV is later expanded to include them, their
571:    handling will need to be re-audited (with the cascade rule
572:    *as currently stated*, they should lower regularly to `gearowe`,
```

#### Germanic/docs/dossiers/widuwe-u-preservation.md:1138 (concept name)

- Nearby heading: ### B.8 Synthesis across the canvass: answers to questions A-G

```text
1137: the shape *wi-C-*a-... (e.g. *witana → wuton path), the rule
1138: will fail.
1139: 
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

