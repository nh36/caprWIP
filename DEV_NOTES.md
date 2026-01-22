## CURRENT FOCUS (as of 2026-01-03)

- Priority: Old English sandbox / PGmc→OE stack. Start here first.
- Modern English sandbox TODOs (below 2025-12-07) are paused unless explicitly requested.
- Key reference: the “Old English core refactor + diagnostics” section under 2025-12-21.
- Latest OE diagnostics (use the unified report script going forward):
  - `docs/debug_snapshots/oe_mismatch_report.txt` (from `server/tools/oe_mismatch_report.py`, now normalizes proto `þ`→`θ`)
  - `docs/debug_snapshots/oe_full_trace_report.txt` (full per‑lexeme stage trace with refined buckets)
  - `docs/debug_snapshots/oe_apply_down_stats_2026-01-02h.txt`
  - `docs/debug_snapshots/oe_mismatch_closeness_2026-01-02a.txt`
  - `docs/debug_snapshots/oe_diacritic_mismatches_traces_2026-01-02.txt`
  - `docs/debug_snapshots/oe_long_vowel_missing_traces_2026-01-02d.txt`
- Start‑here repro (fresh run):
  - `python3 server/tools/oe_mismatch_report.py --output docs/debug_snapshots/oe_mismatch_report_YYYY-MM-DDa.txt`
  - `python3 server/tools/old_english_apply_down_stats.py --output docs/debug_snapshots/oe_apply_down_stats_YYYY-MM-DDa.txt`
- Hedge (2026-01-20):
  - Reverted the orthographic `{ʤj} -> {ċġ}` mapping and removed `{ċġ}` from `OldEnglishSurfaceConsonant` (OE output should stay `ġġ`).
  - Data update: `server/data/germanic-aligned-final.tsv` (OE heċġ → heġġ) with NOTE that **heċġ is the more standard spelling**; Wiktionary TSV left unchanged.
  - Current output is **hæġġ** while expected is **heġġ**; see `docs/debug_snapshots/oe_mismatch_report_2026-01-20d.txt` and `docs/debug_snapshots/oe_full_trace_report_2026-01-20d.txt`.
- Knob (2026-01-22):
  - **Unattested in Old English**; first attested in Middle English (Chaucer): “The knobbes sittynge on his chekes.”
  - Reconstructed PGmc weak noun: **\*knubban‑** (knob family).
  - **OE cnæp** (Kroonen p. 335) is **\*knapp‑**, not the knob etymon; keep families distinct.
  - TSV: OE slot should be **cnobba** marked **unattested** (based on ME knob + Frisian knobbe).
- OE epenthesis update (2026-01-04):
  - Epenthesis is now a real phonological stage **before** star removal and appears in the full trace.
  - Deterministic `r`-epenthesis uses an `{E}` placeholder with back-shift (→`*o`) vs front fallback (→`*e`).
  - `l`-epenthesis is **restricted to final `*gl` only** (added `OldEnglishGLInsertion`), to avoid over-generation (`*xaslăz` → `hæsel` regression).
  - Current OE mismatch report (latest run in `server/docs/debug_snapshots/oe_mismatch_report.txt`): **293 mismatches / 77 matches** (370 total OE rows).
- Next actionable targets (from latest buckets):
  1. **Fronting missing w/ no trigger:** review a-restoration contexts and nasal blocks (see 2026-01-01 subgroup traces).
  2. **Breaking missing:** audit OE breaking contexts before r/l/h clusters and w, then re-trace `oe_breaking_probe`.
  3. **Long-vowel missing (5 items):** map *au/*eu/*iu to long diphthongs and move velar shortening out of OE.
  - 2026-01-10 follow-up: `docs/debug_snapshots/oe_mismatch_report_2026-01-10a.txt` shows long-vowel-missing bucket down to **3** items after extending `OldEnglishDiphthongLeveling`/`OldEnglishEwLongDiphthong`. New log: `docs/debug_snapshots/oe_long_diphthong_traces_2026-01-10.txt`; stats snapshot: `docs/debug_snapshots/oe_apply_down_stats_2026-01-10a.txt`.
- Long‑vowel‑missing deep dive (2026-01-02): see `docs/debug_snapshots/oe_long_vowel_missing_traces_2026-01-02d.txt`.
  - Biggest actionable sources:
    - **PGmc *au not lengthened** → change `*aeu -> *ēa` (or add a dedicated “long diphthong” step right after leveling).
    - **PGmc *eu/*iu not mapped to OE long diphthongs** → add `*eu/*iu -> *ēo` (WS merge).
    - **OE ō before velars should stay long** → move `EnglishVelarShortening` out of the OE block (OE keeps bōc/bōg).
  - “Other” misses (e.g., *end→ān, *utrăz→nǣdre, *xattuz→hōd) are not long‑vowel rules; treat separately.
  - Bucket taxonomy update (2026-01-03): the report now splits the former `uncategorized` bucket into `palatal_marker_variant`, `epenthetic_vowel_missing`, `vowel_quality_other`, `gemination_extra`, and `consonant_mismatch_other`.
  - 2026-01-10 tracing follow-up:
    - `*kewwăną → ċēowan`: `OldEnglishEwLongDiphthong` only sees single `{*w}`; extend the rule to promote `{eww}` to `{ēow}` so duplicated glides still trigger the long diphthong tier.
    - `*fuwer → fȳr`: no rule converts `{uw}` before `{r}` into `{ȳr}`; add a `{uw}` contraction (or targeted `ur` rounding) so `fūr`-class stems reach OE fȳr.
    - `*xattuz → hōd`: expected reflex doesn’t match the provided proto stem (phonologically it yields OE “hat”); fix data alignment rather than phonology.
  - 2026-01-10b data note: the “fire” row now uses dat.sg. *fūri (> fȳre) to avoid modelling nominative levelling; see TSV comment.
  - 2026-01-10 rollback: backed out the short-diphthong lengthening experiment; diagnostics back to the post-*fūri* baseline (293 mismatches) with `slaxăną` still in the long-vowel bucket for future work.

## 2025-12-07

### English sandbox todo — surface accuracy focus

- ~~**Finish weak-tail deletions.** Extend `EnglishSandboxWeakTailReductions` (or add a follow-up cleanup stage) so reduced `{*a/ą}` tails drop the following `n/m/r` and final schwa in stressed monosyllables. This will convert forms like `beɪkeɪnə/bænnə/brændə/blʌdə` into the expected `bake/ban/brand/blood` without manual patches.~~
  - ✅ 2025-12-11: `{*ă}` now flows through `EnglishSandboxWeakTailReductions → EnglishSandboxWeakTailCleanup → EnglishSandboxWeakTailFinalDrop`; `EnglishSandboxNoFinalWeakTail` filters out residual `{*r/n/m}`+`{*ə}`. Tracer (`*bakăną/*bannăn/*brandăz/*blōdą`) shows single surfaces (`beɪk/bæn/brænd/blʌd`), and `tools/english_apply_down_stats.py` reports 333/376 single-output entries (multiple outputs = 0).
- **Back/round proto rhotics earlier.** Expand `EnglishSandboxProtoRhoticFronting` to push `{*e, *i, *o}` toward `{æ, ɪ, ɔ}` before `{*r}` so `*bergą/*bardăz/*barwōn/*burdiz` feed the ME vowel system with the right backness, unlocking `barrow/beard/bier/birth` reflexes.
  - Diagnostics (2025-12-11): `python3 tools/trace_english_sandbox.py --lexeme-file tmp/rhotic_test_set.txt --brace-diphthongs` still yields `*bergą → bæəʊ`, `*bardăz → bɔː`, `*barwōn → bæʋəʊn`, `*erθo → əθ`, `*fuwer → fʌæ`. Current `EnglishSandboxRhoticBreaking` is a grab-bag of lexeme-specific rewrites with `~[?* … ?*]` filters—phonologically unmotivated.
  - Rhotic data audit: 118 English proto entries contain `{r}`; the problematic clusters are `rdă` (4 entries), `rgă` (1), `rwō` (1), `rθo` (1). These align exactly with `tmp/rhotic_test_set.txt`. We need historically grounded rewrites (e.g. `{*rgă → {*rəʊ}}`, `{*rdă → {*ər}}`, `{*rwō → {*rəʊ}}`, `{*erθo → {*erθ}}) before `EnglishSandboxPostVocalicRLoss` deletes `{*r}`.
  - Next session: redesign `EnglishSandboxProtoRhoticFronting`/`EnglishSandboxRhoticBreaking` around those phonetic targets, rerun the rhotic tracer, and rerun `python3 tools/english_apply_down_stats.py` (current baseline: 333/376 single outputs, 20 exact matches).
- **Add the missing palatalisation pass.** Insert a dedicated `EnglishSandboxPalatalisation` stage (after West Germanic or glide deletion) that maps `{*bj→v}`, `{*gj→dʒ}`, `{*kj→tʃ}`, `{*sk→ʃ}` before front vowels. This captures the well-known West Saxon/Midlands changes needed for `believe/beech/chew/shield/ship` and collapses a large swath of remaining errors.
- Once these three TODOs land, rerun `tools/english_apply_down_stats.py` to confirm the “exactly one correct output” count climbs beyond the current ~20/376.

### Rhotic breaking scaffolding (2025-12-06 PM)

- Added `EnglishSandboxRhoticBreaking` with stage checkpoints/tracer support right after `ProtoRhoticFronting`. Current rewrites still leave `*bergą/*bardaz/*barwōn/*erθo` as `bæg/bɔːd/bæʋəʊ/æθɔ`, so the next session should tweak the `{*e/i/o}`→`{*a/ɜ/ɔ}` mappings and add special cases such as `{*rgă → {*rəʊ}}`, `{*rdă → {*ər}}` before re-running `python3 tools/trace_english_sandbox.py --lexeme-file tmp/rhotic_test_set.txt` and `python3 tools/english_apply_down_stats.py`.

### English vowel chronology split into discrete stages

- Extracted the historically early portions of `EnglishSandboxCoreVowelRules` into three stand-alone stages inserted right after `EnglishSandboxBreakingLengthening`: `EnglishSandboxLiquidLowering` (late OE ō→ɔː before liquids/final), `EnglishSandboxVelarShortening` (Anglo-Frisian ō→ʊ before velars), and `EnglishSandboxUrRounding` (WG u→ɔː before r). Each clause now happens once in chronological order before the broader ME vowel machinery runs, reducing the overlap that previously caused branching inside the core block.
- Added tracer checkpoints + `.bin` exports for those stages (`english_sandbox_after_liquid_lowering.bin`, `english_sandbox_after_velar_shortening.bin`, `english_sandbox_after_ur_rounding.bin`) so `trace_english_sandbox.py` can isolate regressions per innovation. Recompiled via `docker compose exec backend ... foma -f fsts/english_brace_sandbox.txt`.
- Ran `server/tools/run_english_sandbox_workflow.sh english_tracer_log_2025-12-07a.txt`; analyzer coverage slipped to **185/376** (down from 206). The ProtoInput bucket is still 5 items, but the “Surface+? but outputs” bucket ballooned. First probes show `*swestēr` still branches in `EnglishSandboxVowelRules`, so the next pass needs to peel the remaining clauses out of `EnglishSandboxCoreVowelRules` and clean up the short-vowel split fallback before widening weak-tail reductions again.

### Short-vowel split sequentialised (WIP)

- Broke `EnglishSandboxShortVowelSplit` into two parts so the contextual rewrites fire before the fallback defaults: `EnglishSandboxShortVowelContextual` now contains every `{u→ʊ}`/{`e→ɪ`}/{`i→ɪ` } clause, while `EnglishSandboxShortVowelFallback` holds the unconditional `{u→ʌ}` and `{e→ɛ}` conversions. The wrapper `EnglishSandboxShortVowelSplit` composes the two stages (`.o.`) so the historical order matches the FOOT/KIT contexts feeding the later defaults.
- Probes (`*swestēr`, `*bardaz`, `*bebruz`, `*bergą`, `*utraz`) no longer branch at `EnglishSandboxVowelRules`; each lexeme now yields a single vowel reflex, which finally exposes the genuine coverage gaps instead of masking them behind duplicated outputs. Tracer log copied to `docs/debug_snapshots/english_tracer_log_2025-12-07b.txt`.
- Regression: analyzer successes dropped to **146/376** because many STRUT/DRESS lexemes now lack the “extra” fallback paths that previously papered over incomplete conditioning. Next step is to audit the English TSV rows with no outputs (see `server/tmp/english_sandbox_results_current.json`, e.g. bæn/brɛd/blʌd) and backfill the missing contexts before moving on to weak-tail reductions. Hold off on adding `{*e}` tails until coverage recovers to the 185 baseline.

### Core vowel audit probes (2025-12-07)

- Added `server/tmp/english_core_probes.txt` spanning long vowels, short rhotics, nasal tails, and glide-rich lexemes, then traced the full stack with `python3 tools/trace_english_sandbox.py --lexeme-file tmp/english_core_probes.txt --brace-diphthongs --save-log tmp/english_tracer_log_core_audit.txt`. Snapshot lives at `docs/debug_snapshots/english_tracer_log_core_audit.txt` for future diffs.
- Quick read-through highlights what *hasn’t* happened yet for each item:
  - `*stānaz` (stone): still surfaces as `stānə`; the `{*ā}` tokens never leave `{ā}`, so the expected Anglo-Frisian rounding (`ā → ɔː`) and later GVS diphthongisation to `{əʊ}` are missing.
  - `*bōkiz` (book): yields `bʊkɪ` because `{*ō}` shortens before velars but never lengthens back to `{uː}`; we still need a later FOOT-stage (or ME-stress shift) to raise `{ʊ}` when morphology demands modern `{uː}`.
  - `*dōmą` (doom): remains `{dō-}` all the way to `dōməʊ`; the ME `{oː → uː}` change is absent, so Great Vowel Shift has nothing to work with.
  - `*bergą` (barrow): currently `bɪgəʊ`; OE `{*e}` before `{*r}` should back/round toward `{æ/ɑ}` before rhotic loss, but that proto rhotic-fronting rule is still trapped inside `EnglishSandboxCoreVowelRules`.
  - `*utraz` (adder): reaches `ʊtrə` because `{u}` already fronts/slackens but there’s no rhotic colouring to convert `{tVr}` into `{dər}`; consonant changes still pending.
  - `*swester` (sister): stage outputs `sʋɪstɪ`; the expected rhotic loss + weak-tail schwa haven’t fired (our weak-tail stage doesn’t cover `{*e}` yet), so it never approaches `sɪstə`.
  - Proto entries with `þ/ð/ai/eu` (e.g. `*fadar`, `*gansą`, `*werþaną`, `*leidą`, `*brōþēr`, `*gebāniz`) fail at `ProtoInput`, reminding us that the lexicon still needs `{þ/ð}` and brace diphthong coverage before the vowel work can be validated on those words.
- Use these annotated gaps to decide which remaining core-vowel rules to peel next: proto rhotic fronting (`{*a → æ || _ {*r}}`) and `{*o → ɔ}` are blocking obvious words (`barrow`, `folk`), while the long-vowel macros (`{*ā, *ō, *ē, *ī, *ū}`) can stay bundled until we add the “LengthRealisation” stage right before `EnglishSandboxShortVowelContextual`.
- Priority shortlist based on the audit:
  1. Add an `EnglishSandboxProtoRhoticFronting` stage so `{*ar}` contexts migrate toward `{æ/ɑ}` before rhotic loss (`*bergą`, `*bardaz`).
  2. Extract `{*o → ɔ}` (and any remaining `{*e}` adjustments) into `EnglishSandboxShortBackLowering` to unblock `*fulkaz`, `*fothą`, etc.
  3. Once those contextual rules have their own checkpoints, introduce `EnglishSandboxLengthRealisation` immediately before `EnglishSandboxShortVowelContextual` so `{*ā/*ō/*ē/*ī/*ū}` finally leave the macro alphabet and feed the Great Vowel Shift cleanly (`*stānaz`, `*dōmą`).

### Proto rhotic fronting + short back lowering staged (2025-12-07 PM)

- Added `EnglishSandboxProtoRhoticFronting` (right after `EnglishSandboxUrRounding`) so the old `{*a -> æ || _ {*r}}` rewrite now happens in its own historical slot. Reran the core probe trace; `*bergą` finally shows `{bæ…}` at the new stage before rhotic loss, confirming the stage fires once and feeds downstream rules cleanly.
- Introduced `EnglishSandboxShortBackLowering` for the blanket `{*o -> ɔ}` mapping. This keeps short back vowels out of `EnglishSandboxCoreVowelRules` and gives us another checkpoint before the short-vowel split. Staged binaries saved (`english_sandbox_after_proto_rhotic_fronting.bin`, `english_sandbox_after_short_back_lowering.bin`).
- Recompiled via `docker compose exec backend … foma -f fsts/english_brace_sandbox.txt` and captured an updated probe log (`docs/debug_snapshots/english_tracer_log_core_audit_post_rhotic.txt`). Highlights: `*stānaz` now reaches `{təʊ/taɪ/teɪ}` options ahead of weak tails, `*bergą` fronts to `{bæ…}` before `{*r}` disappears, and the short `{o}` forms (`*fulkaz`, `*fothą`) stay deterministic through the new stage. Analyzer coverage still sits at 146/376 (not rerun); next change will be the `EnglishSandboxLengthRealisation` stage so `{*ā/*ō/…}` leave the macro alphabet before Great Vowel Shift.

### Star-preserving vowel cascade + STRUT probes (late 2025-12-07)

- Converted the vowel pipeline to stay in the `{*…}` alphabet until the very end: `EnglishSandboxRhoticColoring`/`EnglishSandboxGreatVowelShift` now rewrite starred vowels and a new terminal `EnglishSandboxLongVowelRealisation` emits the IPA symbols right before `RemoveStars`. Tracer logs (`docs/debug_snapshots/english_tracer_log_core_starred.txt`, `docs/debug_snapshots/english_tracer_log_2025-12-07c.txt`) confirm the macrons persist through every historical stage.
- Reran the export→annotate→trace workflow (`english_tracer_log_2025-12-07d.txt`); analyzer coverage climbed to **188/376**, so the star-preserving rewrite didn’t cost us any outputs.
- Began cleaning up the STRUT/DRESS zero-output cluster. `EnglishSandboxWeakTailReductions` now maps `{*ą}`→`{*ə}` and a new `EnglishSandboxShortAFronting` stage fronts short `{*a}` in closed syllables before the short-vowel split. After rebuilding and running `server/tools/run_english_sandbox_workflow.sh english_tracer_log_2025-12-07e.txt`, coverage improved to **195/376**—forms like *ban/*brandaz now emit `bæn`/`brændə`. Updated `server/tmp/english_zero_output_summary.txt` (181 remaining failures) plus dropped the STRUT trace log at `docs/debug_snapshots/english_tracer_log_2025-12-07e.txt` for future comparisons.

## 2025-12-06

### English ConsonantRules made deterministic

- Split the sandbox consonant block into four sequential rules (`EnglishSandboxWGlideRule`, `EnglishSandboxZRhotacism`, `EnglishSandboxZApocope`, `EnglishSandboxDJPalatal`) so non-matching lexemes pass through untouched and matching contexts rewrite exactly once. This removes the earlier branching behaviour that produced multiple outputs (e.g., `{*z}` → `{r}` and `{0}` simultaneously) and stops no-op stems (`*bendaną`, `*grunduz`) from dying at the stage boundary.
- Recompiled `fsts/english_brace_sandbox.txt` and re-ran `server/tools/run_english_sandbox_workflow.sh english_tracer_log_2025-12-06c.txt`. Analyzer successes jumped from 179→205/376; the ConsonantRules bucket disappeared entirely, leaving only ProtoInput (5 items) and the “Surface+? but outputs” bucket (166 items) for follow-up work.
- Captured a tracer snapshot at `docs/debug_snapshots/english_tracer_log_2025-12-06c.txt`. `*bendaną` now flows through ConsonantRules unchanged and reaches Surface, while `*fiskaz` rewrites `{*z}`→`{r}` deterministically.
- Next actions: tackle the remaining vowel-stage issues (KIT/FOOT splits, schwa reductions, rhotic chronology) so the “Surface but mismatched IPA” bucket starts converting into real successes before revisiting ProtoInput compounds.
- Follow-up audit (logs at `docs/debug_snapshots/english_tracer_log_2025-12-06f.txt`) showed that naive rhotic/weak-tail rewrites tanked coverage, so for now only two safe tweaks remain live: short proto `{*a}` now fronts to `{æ}` by default, and `{*ą}` weak tails convert to `{əʊ}` in `EnglishSandboxWeakTailReductions`. Analyzer coverage is still 205/376, but at least the tail vowels surface as `{…əʊ}` for forms like `*gebaną/*br{au}dą`, which will make future schwa/diphthong work easier to verify.

### Rhotic colouring prototype (2025-12-06 — evening)

- Introduced `EnglishSandboxRhoticColoring` between `EnglishSandboxShortVowelSplit` and `EnglishSandboxGreatVowelShift`. The rule only rewrites `{a/e/i/o/u}` when an intervening consonant precedes `{*r}`, so cases like `{*utraz}` now capture the `{t}` between vowel and `{*r}`. Recompiled the cascade and traced the rhotic-heavy probes (`*utraz`, `*bergą`, `*bardaz`, `*bebruz`). Outputs still show brace vowels (e.g., `ʊtræ`, `bɪgəʊ`), but the stage now acts as a dedicated hook for future ME/EME rhotic handling instead of lumping everything into the core block.
- Reran `server/tools/run_english_sandbox_workflow.sh english_tracer_log_2025-12-06g.txt`; analyzer coverage nudged up to **206/376** (one additional success) and the bucket counts shifted to 165 “Surface+? but outputs” plus 5 ProtoInput failures. All new tracer logs live under `docs/debug_snapshots/english_tracer_log_2025-12-06g.txt` for comparison against the earlier rhotic experiment.
- No additional weak-tail rules were enabled yet—`EnglishSandboxWeakTailReductions` still only handles `{*a}` and `{*ą}`. Next session should start widening that stage one vowel class at a time while rerunning the workflow after each addition, so any regressions are easy to pinpoint.

- Follow-up determinism pass: instrumented `trace_english_sandbox.py` for the rhotic probes, then tried to sequentialise both `EnglishSandboxCoreVowelRules` and `EnglishSandboxShortVowelSplit` so each vowel rewrite would fire exactly once (logs in `/usr/app/tmp/vowel_branching_trace.txt`). That change did collapse the outputs (e.g., `*bardaz` finally reduced to a single path), but coverage cratered to 168/376. Reverted to the previous definitions and reran the workflow (`docs/debug_snapshots/english_tracer_log_2025-12-06l.txt`) so we’re back at **206/376** successes with the older branching behaviour intact.
- Takeaway: branching now clearly comes from overlapping clauses inside the core vowel block and the short-vowel split, but wholesale sequentialisation is too disruptive. Next attempt should peel off one context at a time (e.g., only the `{*ō}` liquid rule) and validate immediately rather than rewriting the entire stage.

- Follow-up audit (logs at `docs/debug_snapshots/english_tracer_log_2025-12-06f.txt`) showed that naive rhotic/weak-tail rewrites tanked coverage, so for now only two safe tweaks remain live: short proto `{*a}` now fronts to `{æ}` by default, and `{*ą}` weak tails convert to `{əʊ}` in `EnglishSandboxWeakTailReductions`. Analyzer coverage is still 205/376, but at least the tail vowels surface as `{…əʊ}` for forms like `*gebaną/*br{au}dą`, which will make future schwa/diphthong work easier to verify.

## 2025-12-05

### English sandbox tracer bootstrapped

- Instrumented `server/fsts/english_brace_sandbox.txt` so every stage now has an `EnglishSandboxAfter*` definition plus a saved stack (e.g., `english_sandbox_after_proto_input.bin`, `english_sandbox_after_vowel_rules.bin`). Recompiled inside Docker via `docker compose exec backend sh -lc "cd /usr/app && foma -f fsts/english_brace_sandbox.txt"`; the build now emits 15 `.bin` files under `server/` alongside the existing `english_brace_sandbox.bin`.
- Rewrote `server/tools/trace_english_sandbox.py` to consume those binaries with `flookup` instead of trying to run raw `regex` commands. The script auto-detects whether it’s running on the host (`server/…` paths) or inside the container (`/usr/app`) and accepts `--bin-dir` when the stacks live elsewhere.
- Smoke test inside the backend container: `docker compose exec backend bash -lc "cd /usr/app && python3 tools/trace_english_sandbox.py --lexeme '{*fiskaz}'"`. The tracer now steps through each saved stack (currently returning `+?` for `*fiskaz`, which matches the unresolved KIT bucket, but the stage pipeline itself is inspectable again).

#### CLI polish + harness hooks

- Added `--lexeme-file`, `--brace-diphthongs`, and `--save-log` switches so we can feed large TSV extracts straight into the tracer and drop the output into `docs/debug_snapshots/` without manual copy/paste. Example: `python3 tools/trace_english_sandbox.py --lexeme-file /usr/app/tmp/english_tracer_lexemes.txt --brace-diphthongs --save-log /usr/app/tmp/english_tracer_log.txt` (run inside Docker so `/usr/app/tmp` is writable).
- Sample log (stored at `/usr/app/tmp/english_tracer_log.txt`) now drives the bucket review: `*fiskaz` reaches `Surface: fɪskæ`, `*braudą` reaches `Surface: brōdą`, while `*gebaną` and `*swestēr` still die at the surface filter—exact stage names are now captured in the log for regression diffs.
- Added `tools/annotate_english_sandbox_results.py` to decorate the sandbox regression JSON with stage-by-stage outputs plus a `first_failing_stage` field. Usage (inside Docker so `flookup` is available):
  ```bash
  docker compose exec backend bash -lc \
    "cd /usr/app && python3 tools/annotate_english_sandbox_results.py \
      --input tmp/english_sandbox_results_current.json \
      --output tmp/english_sandbox_results_with_stages.json"
  ```
  The new file (`server/tmp/english_sandbox_results_with_stages.json`) feeds into the bucket triage spreadsheet so every failure row shows its blocking stage.
- Added `tools/export_english_sandbox_results.py` to regenerate `tmp/english_sandbox_results_current.json` directly from `data/germanic-aligned-final.tsv` (filtering the English rows and piping the IPA tokens through `flookup english_brace_sandbox.bin`). Run it inside Docker right before the annotation step so both JSON files stay in sync with the current FST binaries.

- Dropped a snapshot of the four canonical probes into `docs/debug_snapshots/english_tracer_log_2025-12-05.txt` (generated via the tracer’s `--save-log`). Future sessions should append similar logs whenever stage definitions shift.

#### Surface filter triage

- Expanded `EnglishSandboxSurfaceVowel` to accept the macron and nasal vowels (`{ā}/{ē}/{ī}/{ō}/{ū}/{ą}/{ę}`) emitted by the sandbox stages. After recompiling, `*braudą` now flows through `Surface` as `brōdą`; previously it was blocked even though the upstream stages looked fine.
- Updated `EnglishSandboxSurfaceConsonant` so the plain `{g}`/`{w}` outputs (minus braces/stars) survive the final filter. Weak-tail stems such as `*gebaną` and `{sw}` clusters such as `*swestēr` now surface cleanly.
- Remaining `Surface +?` cases flag different follow-ups: continue using the annotated JSON to identify stems that die earlier in the cascade versus genuine surface-template gaps.

### Next steps

1. Feed lexemes straight from `tmp/english_sandbox_results.json` into the tracer (wrap diphthongs with `--brace-diphthongs` once that option exists) so every failure bucket has a representative stage log.
2. Investigate why `{*fiskaz}` still rejects at `EnglishSandboxAfterProtoInput`; likely need either the plain-IPA normaliser or the proto brace rewriter from the German tracer so inputs always match `pgrmWord`.
3. Once the tracer shows real stage outputs, resume the KIT/FOOT fixes with per-stage snapshots checked into `docs/debug_snapshots/` like the German workflow.

## 2025-11-21

### Ach-Laut verification

- Ran the tracer inside the backend container (`python3 tools/trace_german_stages.py --apply-down --stage GermanAfterConsonant --stage GermanAfterStopShift --lexeme laukaz --lexeme milkiz`). `GermanAfterStopShift` now clearly outputs `{*x}` for both probes while `GermanAfterConsonant` still shows the pre-shift `{*k}`, proving the rule fires in isolation again.
- Followed up with analyzer checks (`printf 'laux\nknɛxt\nmɪlx\n' | flookup german.bin`) to ensure the surface words resolve to proto bundles. All three forms now return full reconstruction sets instead of `+?`, so the ach-Laut regression is officially closed.

### Notes / next focus

- Keep the tracer command handy for future regressions; it now provides a clean before/after snapshot for German stop-shift stages.
- With spirantisation unblocked, move back to the `{braudą}` long-vowel contexts plus any residual `{au}` environments that still collapse at `GermanLongVowelRules`.
- Plan for next session: tighten the proto gate so diphthongs cannot leak through as adjacent short vowels. See the action plan below.

### Upcoming work — enforce single-token diphthongs

The tracer still shows `{braudą}` taking two proto paths: one with a genuine `{*au}` token (which monophthongises) and another where `pgrmWord` parses `a` + `u` separately, yielding the unrealistic `braɔt` branch. To keep `GermanAuMonophth` truly exceptionless, we need to prune that second parse. Proposed steps for the next window:

1. Audit `pgrmWord` via `foma` (`regex pgrmWord; apply down braudą`) and check other diphthongs (`ai/eu/iu`) to confirm the ambiguity applies across the board.
2. Add a dedicated filter right after `GermanProtoInput` that rejects any adjacent short-vowel pairs matching the diphthong inventory (`{*a}{*u}`, `{*a}{*i}`, `{*e}{*u}`, `{*i}{*u}`, …). This keeps the base proto definitions readable while ensuring the German cascade only sees the multi-character tokens.
3. Recompile and re-run the tracer/analyzer probes for all diphthong-bearing lexemes (`braudą`, `straumaz`, `flauxz`, `naudiz`, plus `{ai}/{eu}/{iu}` controls) to verify only the `{*ō}` outputs remain.
4. Rerun `python3 server/tools/api_regression.py` so English/Dutch automata (which share `pgrmWord`) don’t regress.
5. Document the new filter in this file and `docs/germanic_transducer_report.md` once it’s in place.

## 2025-11-18

### Checkpoint 0 — baseline capture

- Re-ran the stage tracer inside the backend container with `--normalize-plain` for `laukaz/milkiz/braudą/durą` (the proto control) and saved the outputs to `docs/debug_snapshots/german_stopshift_baseline_2025-11-18.txt`. This is the reference log before touching the `GermanStar*` macros.
- Noted explicitly that `durą` must be used for tracing/apply-down operations (while `dɔr` stays the analyzer control) so the `pgrmWord` inventory always recognizes every segment.

### Checkpoint 1 — proto-backed front/back sets

- Replaced the literal `GermanStarFrontVowel/GermanStarBackVowel` lists with intersections against the proto-derived `GermanStarVowel` output (`server/fsts/germanic.txt`). The helper inventories now define just the front/back subsets, preventing drift if the proto alphabet changes.
- Recompiled the cascade via `docker compose exec backend bash -lc "cd /usr/app && foma -f fsts/germanic.txt"`; compilation succeeded and rebuilt english/dutch/german binaries.
- Spot-checked `GermanStarFrontVowel/GermanStarBackVowel` via `foma` (regex/apply) and re-ran the tracer for `GermanAfterConsonant` only. Outputs for `laukaz/milkiz/braudą/durą` remain identical to the baseline (`*l*au*k*a*z` etc.), so the checkpoint can be considered complete.

### Checkpoint 2 — diphthong alignment

- Introduced `GermanExtraDiphthong` (currently `{*ei}` from `GermanAiShift`) and rewired `GermanStarDiphthong` to reuse `pgrmDiphthong.r` plus that extra inventory. This mirrors the proto definition while keeping room for derived diphthongs.
- Recompiled (`docker compose exec backend ... foma -f fsts/germanic.txt`) and sanity-checked by running small `foma` probes plus tracer dumps for `GermanAfterConsonant`/`GermanAfterStopShift`. The ach-Laut forms still show the baseline `*l*au*k*a*z`, so no behavioural change yet.

### Checkpoint 3 — temporary `{K}` instrumentation (failed)

- Patched `GermanStopShift` so both single-`{*k}` rules output `{K}` instead of `{*x}`; recompiled and ran the tracer restricted to `GermanAfterStopShift`. The ach-Laut probes (`laukaz/milkiz`) still surfaced as `*l*au*k*a*z`, so the contexts are *still* not triggering even with the proto-aligned inventories.
- Reverted the instrumentation immediately (restored `{*k}->{*x}`) so we don't leave the rule in a limbo state. Need a deeper audit of `GermanStarConsonant` / the contexts next session.

### Why the stop-shift contexts are empty

- Direct `foma` checks show `GermanStopShift` does nothing even on a toy input (`regex GermanStopShift; apply down {*l}{*au}{*k}{*a}{*z}`), confirming the left/right contexts never match.
- Initial probes (`regex GermanStarVowel; apply down {*a}` plus `random-words`) showed the `.r`-based definitions were still two-tape relations, not single-tape languages, so intersecting them with literal inventories (`GermanFrontVowelInventory`, etc.) collapsed the set and nothing ever matched `{*au}`. This is now fixed by regenerating the literal brace unions (see the next section), so `random-words` emits real `{*…}` tokens again.
- Burmish never made this change: all of its `{*…}` classes are literal unions, so rules like `*k -> *x` see the expected tokens. We need to follow that model—either generate the literal unions from `pgrm*` via a helper script, or declare multichar symbols up front—because the `.r` projections cannot act as regex contexts.

### GermanStar* regeneration

- Added `server/tools/generate_german_star_sets.py`; it parses the `pgrm*` macros and emits literal unions for `GermanStarVowel/Diphthong/Consonant` plus the front/back subsets (mirroring Burmish). Ran `python3 server/tools/generate_german_star_sets.py --output /tmp/german_star_defs.txt` and pasted the output into `server/fsts/germanic.txt` so every star set is now a single-tape brace list again (`{*a}`, `{*ai}`, `{*b}`, …).
- Recompiled via `docker compose exec backend bash -lc "cd /usr/app && foma -f fsts/germanic.txt"` and sanity-checked with `regex GermanStarVowel; random-words 5` / `regex GermanStarConsonant; random-words 5`. Outputs now show plain `{*…}` tokens instead of the previous `0:yy` relations, confirming the contexts are real languages again.
- Reran the stage tracer for `GermanAfterConsonant` and `GermanAfterStopShift` (with `--normalize-plain`), but the ach-Laut probes still emerge as `*l*au*k*a*z`. So the literal sets were necessary but not sufficient—the `{*k}` contexts still don’t fire even though the inventories now match. Next step is to instrument `GermanStopShift` again or log the immediate environments to see what’s still mismatched.

### Tracer tweaks (still WIP)

- Extended `server/tools/trace_german_stages.py` with `--apply-down`, which shells out to Foma and runs `regex <stage>; apply down …` for each checkpoint. Current limitation: using the raw `*l*au*…` probes still yields `???`, so we need to figure out the exact tokens each stage expects before this mode can replace the old `flookup` path. Keeping the flag so future sessions can iterate without reworking the script.
- 2025-11-20 follow-up: confirmed the failure was on our side rather than the FST. `GermanAfterStopShift` happily outputs `*l*au*x*a*z` when fed plain `laukaz`; the tracer was feeding brace tokens straight into stages that already include `GermanProtoInput`. The helper now tracks both the plain and brace-normalised forms per lexeme, chooses the right flavour per stage (`GermanProtoInput`/`GermanAfter*`/`GermanReflexes` expect plain, raw rules expect braces), and drops the bogus `set verbose-type none` command so `--apply-down` stops printing errors.

### Ach-Laut analyzer gate (2025-11-20)

- Manual stage probes show `GermanAfterStopShift` already produces `*l*au*x*a*z` / `*m*i*l*x*i*z`, so the missing analyzer hits stemmed from `GermanOrthography` rewriting `{*x}` → `h`. Only `lauh/knɛht/mɪlh` had proto traces, whereas the IPA probes (`laux/knɛxt/mɪlx`) still landed on `+?`.
- Changed `GermanOrthography` to emit the literal IPA `x` instead of forcing `{h}`. Recompiled via `docker compose exec backend bash -lc "cd /usr/app && foma -f fsts/germanic.txt"`, then reran `printf 'laux\nknɛxt\nmɪlx\n' | flookup german.bin`—each now dumps the normal proto bundle instead of `+?`.
- Re-ran `python3 tools/trace_german_stages.py --apply-down --lexeme laukaz --lexeme milkiz` inside the backend container to capture a clean trace where the ach-Laut probes visibly pick up `{*x}` after the stop shift, matching the manual Foma spot checks.

### `kniː` / `knɛxt` regression (2025-11-20)

- Analyzer probes for `kniː/knɛxt` still returned `+?` even after the surface inventory fix. Stage traces (`python3 tools/trace_german_stages.py --apply-down --stage GermanAfterConsonant --stage GermanAfterStopShift --lexeme knewą`) showed the culprit: `GermanStopShift` was spirantising the initial `{*k}` in `*knewą`, so `GermanReflexes` produced `xniː` and the analyzer never saw the expected `k`-initial forms.
- Root cause was the permissive `(?* GermanStarBackVowel)` / `(?* GermanStarVocalic)` contexts inside `GermanStopShift`, which happily over-applied at the left edge. Added a guard transducer so the final composite becomes `GermanStopShift = GermanStopShiftCore .o. GermanInitialKFix`, where `GermanInitialKFix` rewrites `{*x}` back to `{*k}` at word onset.
- Recompiled (`docker compose exec backend bash -lc "cd /usr/app && foma -f fsts/germanic.txt"`), then re-ran `python3 tools/trace_german_stages.py --apply-down --stage GermanAfterConsonant --stage GermanAfterStopShift --lexeme knewą` to confirm the stage now stays `*k*n*ī` across the stop-shift boundary.
- Analyzer sanity check: `docker compose exec backend sh -lc "cd /usr/app && printf 'kniː\nknɛxt\n' | flookup german.bin"` now enumerates the expected proto bundle (`knewą/kniwą/...`, `knext`, etc.). Also re-ran `python3 server/tools/api_regression.py` ⇒ PASS for Burmish & Germanic.

### Stop-shift contexts (2025-11-20)

- Removed the temporary `GermanInitialKFix` shim in favour of explicit contexts: defined front/back vowel trigger sets, allowed an optional `{*l}/{*r}` immediately before `{*k}`, and constrained the right-hand side to either true codas (`GermanStarConsonant ?*` / boundary) or the theme vowels that disappear later (`{*a}/{*ą}/{*i}` plus `{*z}/{*n}` mirrors, `{*ō}`, `{*ē}`). This matches the historical ach-/ich-Laut environments without touching initial clusters or `sk-` sequences.
- `server/fsts/germanic.txt:533` now contains the helper sets plus the four targeted `{*k}->{*x}` rules; the old `(?* ...)` expressions are gone.
- Spot checks: `python3 tools/trace_german_stages.py --apply-down --stage GermanAfterConsonant --stage GermanAfterStopShift --lexeme laukaz --lexeme milkiz` confirm the expected `{*x}` appears only after the rule. `knewą` no longer receives a stray `[x]` at the beginning.
- Analyzer (`printf 'kniː\nknɛxt\nlaux\nmɪlx\n' | flookup german.bin`) and `python3 server/tools/api_regression.py` both PASS after the change.

## 2025-11-01

### Germanic tracing primer

- Added `server/tools/trace_german_stages.py`; run it inside the backend container to snapshot any lexeme across the Proto→surface cascade (e.g. `python3 tools/trace_german_stages.py --brace-diphthongs --lexeme laukaz --lexeme milkiz`).
- Current probes (`laukaz/milkiz`) still fail at `GermanProtoInput`; stage outputs show `+?`, so nothing reaches `GermanStopShift` yet. The gate is expecting fully starred multi-character tokens (`{*l}{*au}{*k}{*a}{*z}`), not plain letters.
- Known-good items do pass: `printf 'dɔr\n' | flookup german.bin` returns the expected proto candidates (`durą`, `dąur`, …). Keep using `dɔr` as the analyzer control, but when tracing stages or applying `apply down`, switch to the proto form (`durą`) so every segment lives in the `pgrmWord` alphabet.
- Next: derive the exact brace/star inventory that `pgrmWord` emits (consider extending the tracer to wrap plain IPA automatically), then re-run the stage logger on `laukaz` to catch where `{*k}` should become `{*x}`.

### GermanStopShift audit (2025-11-17 PM)

- Stage logging inside the backend container shows `GermanAfterConsonant` and `GermanAfterStopShift` both output `*l*au*k*a*z` / `*m*i*l*k*i*z` for the ach-Laut probes, while controls like `knewą/braudą/blōdą` already lack a `{*k}`. Command used:

  ```bash
  docker compose exec backend bash -lc '\
    cd /usr/app && foma <<"FST"\n\
    source fsts/germanic.txt\n\
    regex GermanAfterConsonant;\n\
    apply down laukaz\n\
    apply down milkiz\n\
    apply down knewą\n\
    apply down braudą\n\
    apply down blōdą\n\
    apply down durą\n\
    regex GermanAfterStopShift;\n\
    apply down laukaz\n\
    apply down milkiz\n\
    apply down knewą\n\
    apply down braudą\n\
    apply down blōdą\n\
    apply down durą\n\
    quit\n\
  FST'
  ```

- Conclusion: `GermanStopShift` is the first stage where the ach-Laut verbs stall; the “brace vs. no brace” debate was a red herring.
- The real mismatch is inventory drift: `GermanStarVowel`, `GermanStarDiphthong`, `GermanStarConsonant`, etc. still list hard-coded `{*…}` tokens and no longer reflect what `pgrmWord` emits (`*l*au*k*a*z`). When we tried to derive those macros directly from `pgrmShortVowel.r` / `pgrmDiphthong.r`, the downstream automata collapsed, so the refactor needs to be incremental.
- Next session must rebuild the `GermanStar*` sets from the proto macros (mirroring Burmish) and re-run the stage trace + analyzer probes to confirm `{*k}→{*x}` at `GermanStopShift`. Instrumenting the rule to emit `{K}` temporarily should make it easy to see when the contexts match.

### Tiny refactors (2025-11-17 — late)

- Rewired `GermanStarVowel` to reuse the proto projections (`pgrmShortVowel.r | pgrmLongVowel.r | pgrmNasalVowel.r | GermanExtraVowel`). Recompiled via `docker compose exec backend ... foma -f fsts/germanic.txt` and sanity-checked with `regex GermanStarVowel; apply down a/e/ā/ą` — outputs now show the expected `a*`, `e*`, etc. No downstream automata collapsed, so the next incremental step is to replace `GermanStarDiphthong` with `pgrmDiphthong.r` before touching the front/back subsets.
- Attempted to replace `GermanStarDiphthong` with `pgrmDiphthong.r`, but `regex GermanStarDiphthong; apply down ai` returned `???` (Foma expects the literal `{*ai}` output tokens from the original definition). Reverted to the explicit `[ {*ai} | {*au} | {*eu} | {*iu} | {*ei} ]` for now; we’ll revisit once we figure out a clean way to project the brace symbols without collapsing the contexts.

### Diphthong tokenization note

- `pgrmDiphthong` currently maps `{ai} → {*ai}`, `{au} → {*au}`, etc., so the input alphabet includes literal braces. When we tried to consume that via `pgrmDiphthong.r`, `apply down ai` failed because Foma still expects the literal `{ai}` token. Likewise, wrapping `ai` in braces at the CLI (`apply down {ai}`) also fails—the config isn’t using the Burmish-style multichar symbol declarations.
- A clean refactor will probably look like Burmish: declare the multichar symbols up front (so `{ai}` becomes an atomic symbol), normalize the proto lexicon to emit those tokens, then replace the `GermanStar*` macros with `.r` projections. Until that groundwork is in place, the hard-coded `[ {*ai} | … ]` list needs to stay, or the contexts lose sight of the diphthongs.

# Daily Hand-off Notes

Add a new dated section (reverse chronological) each time you pause work.
Include:
- Services you touched (Docker/Caddy, datasets loaded).
- Regression harness status and notable warnings.
- Next tasks or blockers.

For the broader documentation map, see `docs/README.md`.


## 2025-11-01

### Services & probes
- `docker compose exec backend ... flookup german.bin` for `broːt/dɔr/kniː/laux`, plus `bash server/tools/log_german_stages.sh` to capture fresh stage dumps. Docker still prints the obsolete `version` warning before each exec.
- `laux` continues to return `+?`, while `broːt` and `dɔr` now enumerate both nasal-tailed and nasal-free proto forms (`braut/ brautą / braud / braudą`, `dur/durą/...`).

### Findings
- Stage logging shows the failure for ach-Laut items happens immediately: `regex GermanAfterEw; apply down laukaz` yields `???` because `pgrmWeakCoda` omits `{*z}`. Downstream rules therefore never see the form.
- `GermanStopShift` only spirantises `*k` before a consonant or boundary, so `*-kaz` stays as `{*k}`. After `GermanAzLoss` the lingering `{*a}` turns the stem into `lauka`, which the surface filter accepts without the expected `{x}`. The planned apocope after `AzLoss` is still missing.
- Weak-tail rules continue to overgenerate: analyzer output for `broːt` and `kniː` includes parallel paths with and without `{*z}`/`{*ą}` because `GermanFinalNasalLoss` and `GermanAzLoss` remove those segments inconsistently. The dataset migration to `-aną` verbs therefore shows up as duplicated candidates rather than a single cleaned form.
- The noun forms `*braudą`, `*blōdą`, etc. remain correct and should stay untouched; the clean-up needs to focus on the weak-verb paradigms only.
- Added `GermanBraceNormalizer` (drop literal `{`/`}`/`*`) ahead of `pgrmWord`; `GermanProtoInput` now accepts both plain (`laukaz`) and brace-star (`{*l}{*au}{*k}{*a}{*z}`) lexemes.
- Despite the gate fix, the ach-Laut chain still outputs `{*k}`—`regex GermanAfterStopShift; apply down laukaz` returns `*l*au*k*a*z`—so `flookup german.bin` continues to report `+?` for `laux/knɛxt/mɪlx`.
- Replaced the hand-written `GermanStar*` inventories with definitions derived from the proto syllable macros; the contexts now include the full starred alphabet plus `{*æ}`, `{*ɔ}`, `{*x}`, etc., keeping them aligned with ongoing proto edits.
- Observed that the ach-Laut rewrite still fails post-refactor: the starred vowels are matching, but `{*k}` survives because multi-character lexical symbols (`*a`, `*au`) are no longer treated as single units once braces are stripped. Next pass needs to restore a brace wrapper (or declare the `*X` tokens via `multichar_symbols`) so the context sees contiguous vowels around `{*k}`.

### Updates
- Extended `pgrmWeakCoda` to admit `{*z}` and recompiled `server/fsts/germanic.txt`; `regex GermanAfterEw; apply down laukaz` now returns `*l*au*k*a*z`, so ach-Laut verbs reach the sound rules again.
- Reworked `GermanStopShift`/`GermanXPalatalization`/`GermanThemeApocope` to model `{*k} → {*x}` between vowels, palatalise `{*x}` after front vowels, and drop the residual theme vowel once `{*z}` is lost. Rebuilt `german.bin` after the changes.
- Current analyzer run (`printf 'laux\\nknɛxt\\nmɪlx\\n' | flookup german.bin`) still returns `+?`; `GermanProtoInput` appears to refuse `*laukaz`, so the new rules are not exercised yet. Stage logging for the canonical probes (`knewą/braudą/...`) still works as before.
- Recompiled after introducing `GermanBraceNormalizer`; `regex GermanProtoInput; apply down {*l}{*au}{*k}{*a}{*z}` now yields `*l*au*k*a*z` without rejecting the brace input.

### Next focus
1. Track down why `GermanProtoInput` still rejects `*laukaz` (even though `{*z}` was added to the weak-tail macros) and restore `GermanAfterEw` outputs for ach-Laut probes.
2. Once the proto acceptance is fixed, confirm the new spirantisation/palatalisation/apocope rules yield analyzer hits for `laux/knɛxt/mɪlx` and adjust contexts if over/under-generating.
3. Tighten weak-tail handling so `GermanAzLoss` + `GermanFinalNasalLoss` eliminate the tail exactly once for verbs, while noun stems like `*braudą` stay untouched. Re-run `flookup german.bin` for `broːt/dɔr/kniː` after each iteration.


## 2025-10-26

### Services & tests
- `docker compose ps` (requires elevated permissions in this environment) → backend + frontend containers still up; Docker repeats the cosmetic `version` warning.
- Patched `server/tools/log_german_stages.sh` so the probe lexemes are single tokens, then ran `bash server/tools/log_german_stages.sh > /tmp/german_stage_log.txt` to capture Proto→stage outputs for `knewą/braudą/blōdą/tōr`.
- Spot-checked `german_after_longv.bin` directly via `docker compose exec backend ... foma` to confirm the `kniː` forms still appear when the stage is loaded manually.

### Surface Filter (Brace status)
- Brace retarget is complete for the German cascade (surface and intermediate stages all use `{*…}`); English/Dutch still need to be converted.
- Spent most of the session ping-ponging between brace and plain-IPA surface filters; each variant worked in isolation but failed once composed with `GermanReflexes`. The takeaway is that half measures don’t work: either the entire pipeline lives in the brace alphabet (like Burmish) or it will keep collapsing at the final filter.
- We now commit to the brace strategy for Germanic as well. The current files still reflect the older IPA experiments, but the next window will rebuild **every stage** (ProtoWord downward, plus surface filter) so braces are baked in consistently.

### Next plan (next window — brace-first rebuild)
1. Start from `ProtoWord` and reintroduce braces at each German rule, mirroring the Burmish conventions (i.e., every literal surface symbol is wrapped as `{…}` before it leaves its rule block).
2. Recreate `GermanSurfaceVowel/Consonant` in the brace alphabet, making sure the inventory covers all symbols emitted downstream (long vowels, diphthongs, clusters, `{pf}`, `{ts}`, `{ç}`, `{x}`, etc.).
3. Only after the brace-based surface filter composes cleanly with `GermanReflexes` do we rerun `flookup german.bin` for `kniː/broːt/bluːt/tōr` and rerun `server/tools/log_german_stages.sh` to verify everything lines up.
4. With the brace pipeline solid, return to the `{braudą}` long-vowel issue (still dies at `GermanAfterLongV`) and adjust those rules knowing the surface layer is no longer the culprit.

### Findings
- `*knewą` now propagates all the way to `GermanPreSurface` as `{knɪw, knɛw, kniw, kniɔ, kniː}`, so the analyzer gap stems solely from `GermanSurface` still rejecting `{knV}` outputs.
- `*braudą` makes it through `GermanAfterAu` as `{braudą, brōdą}` but vanishes as soon as `GermanLongVowelRules` compose; the long-vowel block (or its contexts) is zeroing out the `{au}` stems.
- `*blōdą` and `*tōr` remain healthy controls (`bloːt/bluːt`, `toːr/tuːr`), matching the prior manual probes.

### Next focus
- Loosen `GermanSurface` / inventory so `{knV}` outputs (and future `{x}/{ç}` cases) pass through to `GermanReflexes`.
- Rework `GermanLongVowelRules` and its neighboring filters so `{braudą → brōdą}` survives past the long-vowel stage instead of collapsing to `???`.

## 2025-10-31

### Services & probes
### German ach-Laut backlog (2025-10-31 follow-up)
- Diagnostics: forms ending in modern `x` such as `laux/knɛxt/mɪlx` still fail because `GermanStopShift` only spirantises `*k` before another consonant or word boundary; it never sees the `*k` when the suffix `*a{z}` is still present. After `GermanAzLoss`, the leftover `{*a}` remains, so the chain produces something like `lauka`, which does not match the UI.
- Plan:
  1. Extend `GermanStopShift` so `*k -> *x` applies before `{*a}{*z}` (and similar suffixal vowels) in `*-kaz/-kiz` paradigms.
  2. Add an apocope rule immediately after `GermanAzLoss` to delete the residual `{*a}` once `{*z}` has gone, yielding the expected ach-Laut codas.
  3. Re-run `server/tools/log_german_stages.sh` with probes `{braudą, laukaz, straumaz, mīlkaz}` and confirm via `flookup` that `laux/knɛxt/mɪlx` now return proto candidates without overgeneration.
  4. Keep weak-tail verbs in the regression set so the new apocope does not undo the recent nasal-tail fixes.

- Containers still running (`docker compose ps`).
- Analyzer checks (post fix): `docker compose exec backend sh -lc "cd /usr/app && printf 'kniː\nbluːt\nbroːt\ndɔr\n' | flookup german.bin"`.
  - `kniː` ⇒ `wąknī/ąknī/kąnī/knąī`.
  - `bluːt` ⇒ `blaut/blōwt/blōt/blūt`.
  - `broːt` now returns `braut`.
  - `dɔr` continues to emit the full `dur` bundle.
- Stage snapshots (`bash server/tools/log_german_stages.sh > /tmp/german_stage_log.txt`).
  - `GermanAfterLongV` now outputs `brūdą` for `braudą`.
  - `GermanPreSurface` shows `brūd/brōd` alongside the existing ew-chain traces.
- Regression harness: `python3 server/tools/api_regression.py` ⇒ PASS for Burmish & Germanic.

### Findings
- Adding `{*au} -> {*ō}` inside `GermanLongVowelRules` keeps `{braudą}` in play; analyzer and staged outputs agree.
- `{durą → dɔr}` remains healthy, so the long-vowel fix didn’t disturb consonant-shift handling.

### Next focus
1. Audit remaining `{au}` contexts to ensure non-coronal environments stay diphthongal after the new rule.
2. Rerun the stage logger + regression harness after any additional tweaks.

### Proto filter follow-up
- Trimmed `pgrmOnsetCore` to the standard singletons, s-clusters, and stop+liquid combos; removed outlier patterns like `{*w}{*w}{*j}` and `{*n}{*x}{*w}{*s}{*t}`.
- Split `pgrmNasalVowel` out of the short-vowel class so we can restrict ą/ę to word-final open syllables; recompiled and confirmed `nę`/`ną` pass while `nęz`/`nąs` are rejected.
- Re-ran `flookup` sanity checks (`kniː/bluːt/broːt/dɔr`) and the API harness (`python3 server/tools/api_regression.py`) — both pipelines still PASS.

### German surface filter (queued)
1. Added `server/tools/collect_german_surface_inventory.py` to pull the segment set from the Stage-3 TSV (with colon→macron and affricate normalisation).
2. Rewrote `GermanSurfaceVowel/Consonant` to use brace tokens populated from that inventory (`{ā}`, `{ɔy}`, `{pf}`, `{ts}`, `{ç}`, `{ʁ}`, etc.) while keeping the ≤3 consonant structure.
3. Recompiled via `foma -f fsts/germanic.txt`, reran `bash server/tools/log_german_stages.sh` and spot `flookup` probes (`broːt/laus/lauf/laux`), then re-ran `python3 server/tools/api_regression.py` — all PASS.

## 2025-10-25

### Services & tests
- `docker compose up -d` (warning: compose `version` key is obsolete).
- Backend reachable at `http://127.0.0.1:5001`; run Caddy via `docs/runbook.md`
  when the UI is needed.
- Regression harness: `python3 server/tools/api_regression.py` ⇒ PASS for both
  burmish/germanic.
- German probes:
  ```bash
  docker compose exec backend sh -c "cd /usr/app && printf 'kniː\nbroːt\nbluːt\ntoːr\n' | flookup german.bin"
  ```
  `kniː`, `broːt`, `bluːt` ⇒ `+?`; `toːr` ⇒ multiple proto outputs.
- Instrumented stages with `foma` (true `apply down`):
  ```bash
  docker compose exec backend sh -c "cd /usr/app && printf 'load stack german_after_longv.bin\napply down knewą\nquit\n' | foma"
  ```
  → `knewą, kniwą, kniuą, kniːą`. After `GermanFinalNasalLoss` the outputs are
  `{knew, kniw, kniu, kniː}`. `GermanPreSurface` yields `{knɪw, knɛw, kniw, kniɔ, kniː}`
  but the final `GermanSurface` filter rejects them, which is why `apply down` on
  `german.bin` still returns `???` for `knewą`.
- Added `server/tools/german_surface_prep.py` as a stop-gap mapper: it splits
  clusters (kn-/pf-/ts-) and wraps each IPA symbol in braces so we can post-
  process `GermanPreSurface` outputs outside the giant FST. Usage example:
  `printf 'kniː\nbroːt\n' | python3 server/tools/german_surface_prep.py`.
  Baking the same logic directly into `server/fsts/germanic.txt` currently hits
  Foma's `Stack full!` limit, so we may eventually need to adopt HFST or split
  the German automaton across multiple files.

### Next focus
- Instrument each German stage (ProtoWord → surface) to capture intermediate
  forms for `*knewą/*braudą/*blōdą`.
- Revisit non-dental `{au}` reflexes and admit `{x}/{ç}` in `GermanSurface` once
  stage logging confirms the choke point.

### Notes
- Documentation index lives in `docs/README.md`; run instructions in
  `docs/runbook.md`.
- Stage logs + surface-filter diagnosis summarized in
  `docs/germanic_transducer_report.md` (2025‑10‑26 update).

## 2025-10-04

### Quick Start Tomorrow
1. Open a fresh terminal window.
2. `cd ~/caprWIP-fresh`
3. Start the services: `docker compose up -d`
   - Rebuild first if desired: `docker compose build`
4. Visit http://localhost:5002 in the browser.
5. Load `burmish-aligned-final.tsv`; the cognate boards and FST editor will then both work.

### Current State
- Latest commits pushed to `update` (most recent: `cd31b59 Interfile glottal-initial board titles`).
- Frontend sorting now trims leading `*`/`?` and interfiles `ʔ`+consonant entries with their plain consonant counterparts; `ʔ`+vowel entries still sort near the end.
- Clean stack: `docker compose up -d` is enough to resume work.

### Tips
- Need to adjust ordering further? Edit `cognate-app/src/App.svelte`, rebuild, and restart.
- To inspect board titles in the UI, open the dev console and check `window.loaded.boards` after loading data.

See you tomorrow!

- Enabled brace-star tokens at the proto layer by removing `RemoveStars` from `GermanProtoInput`; rewrote `GermanEwChain`, `GermanAuMonophth`, and `GermanLongVowelRules` to operate on `{*…}` symbols.
- Added `GermanRemoveStars` immediately after `GermanFinalNasalLoss` so downstream rules still see plain tokens; stage logging now includes both `GermanAfterNasal` (starred) and `GermanAfterStarDrop` (plain) for visibility.
- Updated `GermanHtShift`/`GermanAiShift` contexts to accept star tokens and extended the remover to unwrap `{*ei}` alongside the other brace-star segments.
- Generator still fails on `braudą` in `german.bin` because later rules and the surface filter haven’t been converted yet; brace migration continues in next session.

### Next focus
- Convert the remaining downstream rules (`GermanAzLoss`, vowel adjustments, consonant shift, etc.) so they consume brace-star tokens; push `GermanRemoveStars` as late as possible.
- Rebuild `GermanSurface` as a brace-only filter once the cascade stays in braces; shift any star/brace stripping into the final presentation layer.
- Re-run `server/tools/log_german_stages.sh` and key `flookup` probes after each chunk to confirm analyser/generator symmetry before modifying the surface filter.


- Shifted `GermanRemoveStars` to follow `GermanFinalNasalLoss` after converting that rule to brace-star tokens; stage logging now records `GermanAfterNasal` (starred) before `GermanAfterStarDrop` (plain).
- Converted `GermanHtShift`/`GermanAiShift` contexts to expect star tokens and extended the remover to cover `{*ei}`; downstream stages still operate on plain inventory after the drop.
## 2025-11-30

### Proto gate tightened for diphthongs

- Captured a fresh baseline before touching the proto definitions:
  - `python3 server/tools/api_regression.py` ⇒ PASS for Burmish & Germanic.
  - `python3 tools/trace_german_stages.py --apply-down --stage GermanProtoInput --stage GermanAfterAu --lexeme braudą --lexeme straumaz --lexeme flauxz --lexeme naudiz --lexeme stainaz --lexeme beudan --lexeme liugan --lexeme glaiwaz --lexeme beutan` logged the duplicate `{*a}{*u}` vs `{*au}` outputs for `braudą` only.
- Split the proto weak tails into explicit zero vs. vowel-initial inventories and added `pgrmStrongPlainLight/Heavy` helpers so only heavy syllables (diphthong, long vowel, or short vowel + coda) can precede vowel-headed tails. `pgrmWord` now routes `braudą` through the diphthong path while blocking the `[a] + [u d ą]` parse.
- Recompiled (`docker compose exec backend sh -lc 'cd /usr/app && foma -f fsts/germanic.txt'`) and reran the tracer command above: `GermanProtoInput` now emits a single `{*au}` token for every probe, and `GermanAfterAu` shows only the monophthongised branch for `braudą`.
- Analyzer sanity check: `printf 'laux\nknɛxt\nmɪlx\nbroːt\n' | flookup german.bin` still returns the expected proto bundles; `broːt` no longer keeps the `braɔt` branch alive.
- Front-end payloads unchanged: `python3 server/tools/api_regression.py` still passes for both datasets, confirming that the tightened proto gate does not filter out legitimate entries.

### Emergency English rollback

- Restored the production English cascade to the pre-brace definitions so the UI has a working analyzer again. Replaced the brace-aware block in `server/fsts/germanic.txt` with the legacy IPA rules while keeping the sandbox (`server/fsts/english_brace_sandbox.txt`) intact for ongoing experiments.
- Recompiled via `docker compose exec backend sh -lc 'cd /usr/app && foma -f fsts/germanic.txt'`; the resulting `english.bin` once again has full state/arc counts.
- Regression harness replacement: piped all 362 attested English IPA forms through both stacks. `english.bin` now reconstructs 119 forms (rest still `+?` due to longstanding gaps), while `english_brace_sandbox.bin` remains empty—exactly what we want for comparing future brace work against a functioning baseline.
- Next brace steps stay in the sandbox: feed `pgrmWord`, rebuild brace-aware surface filters, only then swap the finished automaton back into `server/fsts/germanic.txt`.

## 2025-12-01

### Brace sandbox brought online

- Swapped the sandbox cascade onto the brace proto inventory by introducing `EnglishSandboxProtoInput pgrmWord`, rewiring every rule block to consume the `EnglishSandboxStar*` helpers, and pushing `RemoveStars` down to just before the surface filter. `english_brace_sandbox.bin` now compiles as a full 18 kB automaton (195 states / ~8 M paths) instead of the empty 160 byte stub we had yesterday.
- Surface acceptance still mirrors the legacy IPA stack (`EnglishSandboxSurface` expects plain `{b}/{iː}`), but every upstream stage lives entirely in braces so debugging and stage tracing match the German/Burmish pattern. Running the attested-form harness shows 175/362 English IPA forms now reconstruct via the sandbox (production `english.bin` remains at 119/362), giving us a functional brace baseline to compare against.

### Failure inventory & next steps

- Logged the 187 remaining `+?` cases. They cluster around schwa-heavy words (`ə/əʊ` targets such as `bærəʊ`, `fəʊl`, `bɔtəm`), rounded long vowels (`ɔː` in `bɔːl`, `kɔːn`, etc.), and short rounded syllables with `ʊ` (`bʊk`, `brʊk`, `bʊzəm`). These environments currently lack brace-aware mappings in `EnglishSandboxVowelRules`, so the cascade never produces the requested outputs even though the surface filter would admit them.
- Conclusion for tomorrow: add the missing vowel rules (e.g. `{*o}/{*ō}`→`{ɔ}/{ɔː}`, `{*u}`→`{ʊ}` in the relevant contexts, and `{*a}`→`{ə}/{əʊ}` in weak syllables) rather than relaxing the surface filter. After each rule block, recompile and re-run the harness to track how many of the 187 failures drop off. Only once the sandbox meets or exceeds the IPA baseline should we plan the production swap.

### Sandbox vowel expansion

- Introduced `EnglishSandboxStarNasal/Liquid/VelarStop` helpers so the vowel block can target `{*ai}` vs. `{*au}` sequences and the liquid-heavy `{*a}` contexts without repeating literal sets.
- Extended `EnglishSandboxVowelRules` with the first batch of brace-aware mappings:
  - `{*ai}` now yields `{əʊ}` before nasals, velars, labials, and the `gw/kn/xw` clusters that cover the attested `bəʊn/fəʊl/snow/stone/soul/token` cases.
  - `{*au}` exposes an `{əʊ}` branch in addition to `{aʊ}/{oː}`, `{*ō}` can realise `{ɔː}` or `{ʊ}` in the usual `r/l/#` and velar-k environments, and `{*a}` picks up `{ɔː}` before `l/r/w`.
  - Added a dedicated schwa cleanup for the weak-tail templates (`-az/-an/-nē/-gą/-lō/-raz`) so `hammer`, `bottom`, `weapon`, etc. stop stalling solely because the tail vowel stayed as `{a}`.
- `docker compose exec backend sh -lc 'cd /usr/app && foma -f fsts/english_brace_sandbox.txt'` recompiles the sandbox to a 21.7 kB automaton (201 states / 23 M paths). Quick probes such as `printf 'bɔːl\nkɔːn\nfəʊl\nbəʊn\nbʊk\n' | flookup english_brace_sandbox.bin` now return full proto bundles instead of `+?`.
- `python3 server/tools/api_regression.py` still PASS for both Burmish and Germanic datasets, so the extra branches did not perturb the production analyzer.

### Historical staging scaffolding

- Split the vowel stack into `EnglishSandboxCoreVowelRules` (stressed vowels + rounding/raising) and a follow-on `EnglishSandboxLateReductionRules` block that handles the weak-tail schwa conversions. The sandbox now composes these two definitions in series, matching the historical order where vowel quality shifts precede widespread unstressed reduction. No outputs changed, but the pipeline is ready for future WG/ME-era stages without becoming a single monolithic rewrite block.
- Annotated the block with explicit "West Germanic / Old English" and "Late Middle English" comments so the chronological stages are documented directly in the FST, per the Burmish/German style.
- Recompiled (`docker compose exec backend sh -lc 'cd /usr/app && foma -f fsts/english_brace_sandbox.txt'`), yielding the same surface behaviour as before (20.7 kB / 201 states). Future iterations can introduce West Germanic monophthongisation and ME diphthongisation as separate stages without disturbing the late reduction rules.

### WG monophthongisation stage

- Added `EnglishSandboxWestGermanic` to the cascade (between glide deletion and the vowel rules) so proto `{*ai}`/`{*au}` first collapse onto the historical long vowels `{*ā}`/`{*ō}` before Middle/Modern English rules run. The new stage keeps everything in the proto alphabet—no WGMARK tokens—and mirrors how the German/Burmish stacks segregate their era-specific rule blocks.
- Moved the old `{*ai}`/`{*au}` IPA rewrites onto `{*ā}`/`{*ō}` inside `EnglishSandboxCoreVowelRules`, preserving every contextual mapping we already depend on (`bəʊn`/`stəʊn`/`fəʊl`, etc.) while letting us inspect `{*bān}`, `{*stān}` intermediate outputs.
- `docker compose exec backend sh -lc "cd /usr/app && foma -f fsts/english_brace_sandbox.txt"` now produces a 23.5 kB sandbox automaton (209 states / 32 M paths). Spot checks via `printf 'bəʊn\nstəʊn\nfəʊl\nbɔːl\n' | flookup english_brace_sandbox.bin` show the analyzer surfacing both the WG monophthongised forms (`bān/stān/fāl/bōl`) and the legacy `{*bain}` branches, so we can trace the historical stage outputs directly.

### Great Vowel Shift split

- Broke the downstream vowel block into `EnglishSandboxGreatVowelShift` plus the existing late-reduction stage so the open-syllable long vowels now pass through an explicit `{ɑː}/{oː}` layer before modern diphthongs appear. `EnglishSandboxCoreVowelRules` now stops at `{iː}/{uː}/{ɑː}/{oː}/{ɔː}` outputs, while the new stage handles `{oː → aʊ/əʊ}` and `{ɑː → eɪ/aɪ/əʊ}` with the same environments we already tuned.
- Recompiled again (`docker compose exec backend sh -lc 'cd /usr/app && foma -f fsts/english_brace_sandbox.txt'`), yielding a 24.0 kB sandbox automaton (213 states / 29.6 M paths). Regression spot checks for `bəʊn/stəʊn/fəʊl/bɔːl` still produce the expected proto bundles plus the new intermediate stages, confirming behaviour stayed constant while the chronology became inspectable.

## 2025-12-02

### Open-syllable lengthening stage

- Added `EnglishSandboxOpenSyllableLengthening` between the West Germanic collapse and the core vowel rules so short `{*a/e/i/o/u}` lengthen whenever they precede a single consonant plus another vowel (e.g., `*nama` now exposes `{*nāma}` before the Great Vowel Shift layer).
- Recompiled via `docker compose exec backend sh -lc 'cd /usr/app && foma -f fsts/english_brace_sandbox.txt'`; `english_brace_sandbox.bin` grows to 30.4 kB (254 states / 32.9 M paths) and the tracer now shows `{*nāma}` / `{*bēra}` intermediate forms alongside the later Modern English reflexes.
- `python3 server/tools/api_regression.py` still PASS for Burmish & Germanic datasets, confirming the new stage doesn’t perturb production analyzers.

### Breaking/rounding stage

- Pulled the `{*a}`→`{ɔː}` liquid/glide rules out of `EnglishSandboxCoreVowelRules` and replaced them with an Anglo-Frisian style `EnglishSandboxBreakingLengthening` stage that rewrites `{*a}` to `{*ō}` before `{*l}/{*r}/{*w}`.
- Recompiled (`docker compose exec backend sh -lc 'cd /usr/app && foma -f fsts/english_brace_sandbox.txt'`): `english_brace_sandbox.bin` is now 31.0 kB (260 states / 29.3 M paths) and stage logging exposes `{*bōl}/{*bōrd}` outputs prior to the Modern English vowel layers.
- `python3 server/tools/api_regression.py` continues to PASS for both datasets, so the refactor kept the working analyzer stable while making room for future post-vocalic /r/-loss.

### Short-vowel split & weak-tail staging

- Updated `EnglishSandboxCoreVowelRules` to leave short `{*e}`/`{*u}` as `{e}`/`{u}` tokens and inserted a new `EnglishSandboxShortVowelSplit` stage that now pushes `{u}`→`{ʊ}` before velars, weak-tail `z`/`m` clusters, and dark `{l}` codas while handing `{e}`→`{ɪ}` only in nasal/liquid-heavy codas; everything else defaults to `{ɛ}`/`{ʌ}` so the split sits chronologically between the OE core and the Great Vowel Shift.
- Lifted the schwa clean-up rules into `EnglishSandboxWeakTailReductions`, keyed directly to `pgrmWeakTailVowel.r`, and run that stage after the short-vowel split so reductions don’t erase the new conditioning. Recompiling via Docker now yields a 25.1 kB sandbox automaton (223 states / 5.2 M paths) and the regression harness still passes for Burmish & Germanic.
- Spot checks (`printf 'bʊk\nbrʊk\nbʊzəm\n' | flookup english_brace_sandbox.bin`) show `bʊk/brʊk` emitting `bōk/brōk` proto bundles through the new stage, while `bʊzəm` still reports `+?` because the `{u}`→`{ʊ}` rule doesn’t yet cover the `z + weak tail` parse.

### Failure buckets & historical targets

- Bottom-up sweep: `python3 - <<'PY' …` loops the 376 English entries from `server/data/germanic-aligned-final.tsv` through `docker compose exec backend sh -lc 'cd /usr/app && flookup english_brace_sandbox.bin'` and writes `tmp/english_sandbox_results.json`. Current sandbox stats: 119/376 successes (matching the production analyzer) and 257 failures.
- Failure clustering by IPA lines up with the outstanding historical stages: 108 KIT cases (`{ɪ}` in closed syllables), 31 FOOT/STRUT cases (`{ʊ}`), 61 weak-tail schwa outputs (`{ə/əʊ}`), 69 `{r}`-bearing entries still awaiting post-vocalic /r/-loss, and 29 `{ɔ/ɔː}` forms that want better breaking.
- Top-down staging notes before touching code:
  - **Late OE short-vowel conditioning**: finish the FOOT–STRUT stage so `{*u}` first branches to `{ʊ}` in dark-l/velar/alveolar codas, then feeds `{ʌ}` in open or dental contexts; likewise confine the KIT split to nasal/liquid + consonant codas (stop globally rewriting `{e}`).
  - **ME /r/-loss**: add a post-breaking stage that deletes `{r}` after vowels/codas (mirroring historical smoothing) so `{*bōr}` surfaces as `{bɔː}` before Late Reduction derives `board`/`bier` outcomes.
  - **Weak-tail clean-up**: continue driving reductions via `EnglishSandboxWeakTailVowel` so schwa mappings target the templated tails instead of ad-hoc contexts.
- For each block, validate against the relevant bucket from `tmp/english_sandbox_results.json` and log stage traces so the top-down picture stays anchored to the bottom-up error counts.

### TODO (next session)

- Broaden the `{u}`→`{ʊ}` contexts (e.g., `z + weak tail`, alveolar stops) and log which of the remaining `{ʌ}` cases still need special handling so `bʊzəm/pʊt` stop failing.
- Tighten the `{e}`→`{ɪ}` side so KIT only fires in the nasal/liquid clusters we actually attest; add stage logging for representative lez pairs to confirm.
- With the breaking stage in place, start sketching a post-vocalic /r/-loss layer before moving back toward the production cascade swap.

### KIT sweep (status: reverted to baseline)

- Replayed the dockered `flookup` harness (`python3 - <<'PY' …`) to isolate the true KIT cases (filtering out `aɪ/eɪ/ɔɪ`). We still have 35 `{ɪ}` forms headed by `fish/give/six/will` plus the `{ɪə}`+`r` items (`beard/bier/deer/spear/year`).
- Restored the brace-aware helper sets (`EnglishSandboxPlainVocalic/Liquid/Nasal`), the `{*u}` contexts, and `EnglishSandboxPostVocalicRLoss` after rolling back an experimental smoothing stage that tanked the harness. `english_brace_sandbox.bin` is back to the 179/376 success baseline.
- `python3 server/tools/api_regression.py` remains green, so the sandbox is stable again for the next round of KIT work (detailed smoothing + consonant-cluster contexts).

### Short-vowel fixes + /r/-loss scaffold

- Added plain helper sets (`EnglishSandboxPlainVocalic/Liquid/Nasal`) so late-stage rules can reason about the brace-free vowels while still matching against the starred consonants passed along from the proto inventory.
- Reworked `EnglishSandboxShortVowelSplit` to cover the documented FOOT/STRUT environments: `{*u}` now targets `{ʊ}` before velars, `{*z/m/n}` plus weak-tail templates, dark `{*l}`, `{*r}`, and the `{*f}/{*s}/{*θ}` codas (`wolf/wool`), while KIT contexts keep `{*e}`→`{ɪ}` before nasals/liquids. Everything else still falls through to `{ʌ}`/`{ɛ}`.
- Inserted `EnglishSandboxPostVocalicRLoss` (after the vowel stack but before weak-tail reductions) so `{*r}` drops after any plain vowel plus a consonant/word boundary, giving us a chronological hook for the upcoming smoothing work.
- Reran the attested-form sweep (same `python3 - <<'PY' …` harness as above): 179/376 English entries now reconstruct (up from 119), with the failure buckets collapsing to KIT = 61, FOOT = 3, weak-tail schwa = 51, /r/-bearing = 54, and `{ɔ/əʊ}` = 18. Spot checks show `bəʊn/bəʊθ` retrieving `{*bōr}` bundles prior to loss, while known outliers like `bʊzəm` and the irregular `ʋʊl/ʋʊlf` remain on the TODO list.
- `python3 server/tools/api_regression.py` still PASS for Burmish & Germanic after the rewrites, so the sandbox tweaks stay isolated.

### KIT sweep (WIP)

- Fed the KIT bucket through the same dockered `flookup` harness (`python3 - <<'PY' …`) after filtering out diphthongs (`aɪ/eɪ/ɔɪ`). The remaining 35 entries are the genuine `{ɪ}` cases headed by `fish/give/six/will` alongside the `{ɪə}` + post-vocalic /r/ cohort (`beard/bier/deer/spear/ year`, etc.).
- Updated `EnglishSandboxCoreVowelRules` so short `{*i}` finally drops its star and enters the plain alphabet, and extended `EnglishSandboxShortVowelSplit` with `{i}`→`{ɪ}` rewrites in closed syllables / word-final contexts. This keeps the KIT conditioning in the same stage as the `{*e}`/{`*u`} splits instead of leaving `{*i}` untouched.
- The attested-form harness still lands at 179/376 successes (KIT bucket = 35) because the stubborn cases need post-vocalic /r/ smoothing (`{ɪ}`→`{ɪə}` before the new `EnglishSandboxPostVocalicRLoss`) or suffixal analogies (`sieve/singe/timber`). Logged them here so the next pass can target `{ɪə}` outputs without sacrificing the `{bəʊn}/{fʊt}` improvements we just landed.

## 2025-12-04

### KIT/FOOT contexts + /r/-smoothing harness

- Extended  so FOOT now targets alveolar codas in both starred and plain alphabets ( + weak-tail templates, plain  codas) and added a plain  feed so the KIT split can finally act on closed  syllables. Introduced  between the vowel stack and  so  can surface as  before  deletes .
- Recompiled via Opening file 'fsts/germanic.txt'.
defined ProtoVowel: 1.1 kB. 2 states, 22 arcs, 22 paths.
defined ProtoConsonant: 1.4 kB. 2 states, 28 arcs, 28 paths.
defined ProtoSymbol: 2.3 kB. 2 states, 50 arcs, 50 paths.
defined ProtoNucleus: 719 bytes. 4 states, 14 arcs, 14 paths.
defined ProtoOnsetCore: 5.5 kB. 2 states, 125 arcs, 125 paths.
defined ProtoOnset: 5.5 kB. 2 states, 125 arcs, 126 paths.
defined ProtoCodaCore: 5.3 kB. 2 states, 121 arcs, 121 paths.
defined ProtoCoda: 7.2 kB. 3 states, 242 arcs, 14763 paths.
defined ProtoStrongSyllable: 13.9 kB. 7 states, 634 arcs, 26041932 paths.
defined ProtoWeakOnset: 1.4 kB. 2 states, 28 arcs, 29 paths.
defined ProtoWeakOralNucleus: 585 bytes. 2 states, 9 arcs, 9 paths.
defined ProtoWeakNasalNucleus: 203 bytes. 2 states, 1 arc, 1 path.
defined ProtoWeakCoda: 623 bytes. 2 states, 10 arcs, 11 paths.
defined ProtoWeakOralSyllable: 2.0 kB. 4 states, 56 arcs, 2871 paths.
defined ProtoWeakNasalSyllable: 1.4 kB. 3 states, 30 arcs, 29 paths.
defined ProtoWeakTail: 3.4 kB. 7 states, 144 arcs, 8067801 paths.
defined ProtoSyllable: 13.9 kB. 7 states, 634 arcs, 26041932 paths.
defined ProtoWord: 17.8 kB. 13 states, 863 arcs, 209143179497574 paths.
defined Cons: 1.4 kB. 2 states, 28 arcs, 28 paths.
defined Vowel: 1.1 kB. 2 states, 22 arcs, 22 paths.
defined FrontVowel: 630 bytes. 2 states, 10 arcs, 10 paths.
defined BackVowel: 587 bytes. 2 states, 9 arcs, 9 paths.
defined Sonorant: 456 bytes. 2 states, 6 arcs, 6 paths.
defined pgrmInitSimple: 1.5 kB. 24 states, 44 arcs, 22 paths.
defined pgrmMedial: 461 bytes. 6 states, 8 arcs, 4 paths.
defined pgrmOnsetCore: 2.3 kB. 45 states, 99 arcs, 129 paths.
defined pgrmOnset: 2.3 kB. 45 states, 99 arcs, 130 paths.
defined pgrmShortVowel: 577 bytes. 8 states, 12 arcs, 6 paths.
defined pgrmNasalVowel: 347 bytes. 4 states, 4 arcs, 2 paths.
defined pgrmLongVowel: 524 bytes. 7 states, 10 arcs, 5 paths.
defined pgrmDiphthong: 477 bytes. 7 states, 9 arcs, 4 paths.
defined pgrmNucleus: 952 bytes. 14 states, 27 arcs, 15 paths.
defined pgrmCodaSimple: 1.3 kB. 21 states, 38 arcs, 19 paths.
defined pgrmCodaComplex: 3.2 kB. 77 states, 166 arcs, 104 paths.
defined pgrmCodaNonEmpty: 3.4 kB. 79 states, 171 arcs, 123 paths.
defined pgrmCoda: 3.4 kB. 79 states, 171 arcs, 124 paths.
defined pgrmStrongPlainLight: 3.4 kB. 52 states, 159 arcs, 780 paths.
defined pgrmStrongPlainHeavy: 10.5 kB. 150 states, 603 arcs, 256046 paths.
defined pgrmStrongPlain: 10.2 kB. 148 states, 583 arcs, 256826 paths.
defined pgrmStrongNasal: 2.7 kB. 48 states, 119 arcs, 260 paths.
defined pgrmWeakOnset: 461 bytes. 6 states, 8 arcs, 5 paths.
defined pgrmWeakOralNucleus: 519 bytes. 7 states, 10 arcs, 5 paths.
defined pgrmWeakNasalNucleus: 347 bytes. 4 states, 4 arcs, 2 paths.
defined pgrmWeakCoda: 577 bytes. 8 states, 12 arcs, 7 paths.
defined pgrmWeakOralSyllable: 1.0 kB. 19 states, 35 arcs, 175 paths.
defined pgrmWeakNasalSyllable: 611 bytes. 9 states, 14 arcs, 10 paths.
defined pgrmWeakTailZero: 160 bytes. 1 state, 0 arcs, 1 path.
defined pgrmWeakTailVowel: 2.3 kB. 71 states, 98 arcs, 38 paths.
defined pgrmWeakTail: 2.3 kB. 71 states, 98 arcs, 39 paths.
defined pgrmWord: 18.0 kB. 233 states, 1082 arcs, 9992034 paths.
defined RemoveStars: 332 bytes. 1 state, 2 arcs, Cyclic.
defined GermanLexOnset: 2.6 kB. 47 states, 116 arcs, 129 paths.
defined GermanLexCoda: 3.3 kB. 78 states, 167 arcs, 124 paths.
defined GermanLexConsonant: 4.5 kB. 85 states, 237 arcs, 191 paths.
defined GermanLexShortVowel: 577 bytes. 8 states, 12 arcs, 6 paths.
defined GermanLexLongVowel: 524 bytes. 7 states, 10 arcs, 5 paths.
defined GermanLexNasalVowel: 347 bytes. 4 states, 4 arcs, 2 paths.
defined GermanLexVowel: 990 bytes. 15 states, 26 arcs, 13 paths.
defined GermanLexDiphthong: 477 bytes. 7 states, 9 arcs, 4 paths.
defined GermanProtoInput: 18.0 kB. 233 states, 1082 arcs, 9992034 paths.
defined EnglishSurfaceVowel: 897 bytes. 8 states, 20 arcs, 18 paths.
defined EnglishSurfaceConsonant: 1.1 kB. 2 states, 23 arcs, 23 paths.
defined EnglishSurfaceOnset: 1.9 kB. 4 states, 69 arcs, 12720 paths.
defined EnglishSurfaceCoda: 1.9 kB. 4 states, 69 arcs, 12720 paths.
defined EnglishSurfaceSyllable: 5.3 kB. 14 states, 266 arcs, 2912371200 paths.
defined EnglishSurface: 5.9 kB. 12 states, 306 arcs, Cyclic.
defined DutchSurfaceVowel: 890 bytes. 6 states, 18 arcs, 16 paths.
defined DutchSurfaceConsonant: 1004 bytes. 2 states, 19 arcs, 19 paths.
defined DutchSurfaceOnset: 1.6 kB. 4 states, 57 arcs, 7240 paths.
defined DutchSurfaceCoda: 1.6 kB. 4 states, 57 arcs, 7240 paths.
defined DutchSurfaceSyllable: 4.4 kB. 12 states, 212 arcs, 838681600 paths.
defined DutchSurface: 6.0 kB. 12 states, 314 arcs, Cyclic.
defined GermanSurfaceShortVowel: 713 bytes. 2 states, 12 arcs, 12 paths.
defined GermanSurfaceMacronVowel: 418 bytes. 2 states, 5 arcs, 5 paths.
defined GermanSurfaceDiphthong: 414 bytes. 4 states, 5 arcs, 3 paths.
defined GermanSurfaceVowel: 976 bytes. 4 states, 20 arcs, 20 paths.
defined GermanSurfaceConsonant: 1.1 kB. 4 states, 24 arcs, 24 paths.
defined GermanSurfaceOnset: 3.2 kB. 10 states, 156 arcs, 14327 paths.
defined GermanSurfaceCoda: 3.2 kB. 10 states, 156 arcs, 14327 paths.
defined GermanSurfaceSyllable: 9.5 kB. 22 states, 529 arcs, 4105258580 paths.
defined GermanSurface: 12.4 kB. 20 states, 716 arcs, Cyclic.
defined EnglishInitialKnMarkers: 542 bytes. 2 states, 10 arcs, Cyclic.
defined EnglishConsonantRules: 4.3 kB. 10 states, 206 arcs, Cyclic.
defined EnglishGhMarker: 1.7 kB. 3 states, 53 arcs, Cyclic.
defined EnglishSilentInitialCleanup: 418 bytes. 1 state, 4 arcs, Cyclic.
defined EnglishGlideDeletion: 2.0 kB. 4 states, 73 arcs, Cyclic.
defined EnglishGhDeletion: 2.1 kB. 4 states, 76 arcs, Cyclic.
defined EnglishVowelRules: 1.2 kB. 5 states, 30 arcs, Cyclic.
defined EnglishOrthography: 374 bytes. 1 state, 3 arcs, Cyclic.
defined EnglishReflexes: 38.2 kB. 53 states, 2137 arcs, 560537344690722 paths.
defined English: 16.8 kB. 42 states, 762 arcs, 515886581394 paths.
16.8 kB. 42 states, 762 arcs, 515886581394 paths.
Writing to file english.bin.
defined DutchConsonantRules: 862 bytes. 3 states, 22 arcs, Cyclic.
defined DutchSibilantRules: 2.6 kB. 6 states, 108 arcs, Cyclic.
defined DutchVowelRules: 3.3 kB. 7 states, 125 arcs, Cyclic.
defined DutchReductions: 2.1 kB. 3 states, 66 arcs, Cyclic.
defined DutchOrthography: 374 bytes. 1 state, 3 arcs, Cyclic.
defined DutchReflexes: 35.8 kB. 58 states, 1987 arcs, 287148714187734 paths.
defined Dutch: 13.4 kB. 41 states, 555 arcs, 74013248891 paths.
13.4 kB. 41 states, 555 arcs, 74013248891 paths.
Writing to file dutch.bin.
defined GermanConsonantShift: 3.4 kB. 19 states, 179 arcs, Cyclic.
defined GermanFinalDevoicing: 1.0 kB. 4 states, 34 arcs, Cyclic.
defined GermanStopShiftBackVowel: 559 bytes. 4 states, 9 arcs, 8 paths.
defined GermanStopShiftFrontVowel: 632 bytes. 6 states, 12 arcs, 10 paths.
defined GermanStopShiftLiquid: 329 bytes. 3 states, 3 arcs, 2 paths.
defined GermanStopShiftBackLeft: 675 bytes. 6 states, 13 arcs, 24 paths.
defined GermanStopShiftFrontLeft: 764 bytes. 8 states, 17 arcs, 30 paths.
defined GermanStopShiftSuffix: 680 bytes. 9 states, 15 arcs, 16 paths.
defined GermanStopShiftCodaRight: 383 bytes. 3 states, 4 arcs, Cyclic.
defined GermanStopShift: 3.5 kB. 11 states, 175 arcs, Cyclic.
defined GermanXPalatalization: 640 bytes. 3 states, 15 arcs, Cyclic.
defined GermanExtraVowel: 675 bytes. 3 states, 11 arcs, 10 paths.
defined GermanStarVowel: 1.2 kB. 3 states, 24 arcs, 23 paths.
defined GermanStarDiphthong: 445 bytes. 5 states, 7 arcs, 5 paths.
defined GermanStarVocalic: 1.2 kB. 5 states, 27 arcs, 28 paths.
defined GermanStarConsonant: 1.1 kB. 3 states, 23 arcs, 22 paths.
defined GermanStarFrontVowel: 672 bytes. 3 states, 11 arcs, 10 paths.
defined GermanStarBackVowel: 629 bytes. 3 states, 10 arcs, 9 paths.
defined GermanStarFrontTrigger: 804 bytes. 6 states, 16 arcs, 14 paths.
defined GermanEToIBeforeW: 746 bytes. 6 states, 23 arcs, Cyclic.
defined GermanWToUAfterI: 698 bytes. 4 states, 20 arcs, Cyclic.
defined GermanIuToIi: 747 bytes. 6 states, 23 arcs, Cyclic.
defined GermanEwChain: 1.2 kB. 10 states, 50 arcs, Cyclic.
defined GermanAuMonophthContext: 541 bytes. 3 states, 8 arcs, 7 paths.
defined GermanAuMonophth: 1.5 kB. 8 states, 64 arcs, Cyclic.
defined GermanLongVowelRules: 802 bytes. 4 states, 23 arcs, Cyclic.
defined GermanRemoveStars: 5.2 kB. 56 states, 223 arcs, Cyclic.
defined GermanFinalNasalLoss: 455 bytes. 3 states, 8 arcs, Cyclic.
defined GermanAzLoss: 550 bytes. 5 states, 13 arcs, Cyclic.
defined GermanThemeApocope: 640 bytes. 5 states, 17 arcs, Cyclic.
defined GermanAiShift: 1.3 kB. 12 states, 56 arcs, Cyclic.
defined GermanHtShift: 746 bytes. 6 states, 23 arcs, Cyclic.
defined GermanVowelAdjustments: 790 bytes. 2 states, 19 arcs, Cyclic.
defined GermanCleanup: 432 bytes. 2 states, 5 arcs, Cyclic.
defined GermanOrthography: 454 bytes. 3 states, 8 arcs, Cyclic.
defined GermanLengthOrthography: 774 bytes. 2 states, 13 arcs, Cyclic.
defined GermanRules: 48.4 kB. 267 states, 2982 arcs, Cyclic.
defined GermanAfterEw: 18.4 kB. 235 states, 1103 arcs, 9992034 paths.
defined GermanAfterLongV: 18.9 kB. 235 states, 1131 arcs, 10017384 paths.
defined GermanAfterAu: 19.3 kB. 238 states, 1161 arcs, 10017384 paths.
defined GermanAfterNasal: 19.3 kB. 236 states, 1159 arcs, 10017384 paths.
defined GermanAfterConsonant: 20.6 kB. 242 states, 1236 arcs, 10402827 paths.
defined GermanAfterStopShift: 21.5 kB. 249 states, 1290 arcs, 10560777 paths.
defined GermanAfterPalatal: 21.6 kB. 249 states, 1290 arcs, 10560777 paths.
defined GermanAfterAzLoss: 22.2 kB. 250 states, 1328 arcs, 10560777 paths.
defined GermanAfterApocope: 24.1 kB. 251 states, 1448 arcs, 10560777 paths.
defined GermanAfterVowelAdj: 24.2 kB. 249 states, 1450 arcs, 13375942 paths.
defined GermanAfterFinalDevoice: 25.2 kB. 255 states, 1515 arcs, 13375942 paths.
defined GermanAfterCleanup: 25.3 kB. 259 states, 1524 arcs, 13375942 paths.
defined GermanAfterOrthography: 25.3 kB. 252 states, 1524 arcs, 13375942 paths.
defined GermanAfterStarDrop: 25.7 kB. 110 states, 1526 arcs, 15348066 paths.
defined GermanAfterShift: 21.6 kB. 249 states, 1290 arcs, 10560777 paths.
defined GermanPreSurface: 25.7 kB. 110 states, 1526 arcs, 15348066 paths.
defined GermanReflexes: 25.7 kB. 110 states, 1526 arcs, 15348066 paths.
defined German: 27.4 kB. 139 states, 1634 arcs, 11054870 paths.
27.4 kB. 139 states, 1634 arcs, 11054870 paths.
Writing to file german.bin.
defined EnglishSandboxSurfaceVowel: 897 bytes. 8 states, 20 arcs, 18 paths.
defined EnglishSandboxSurfaceConsonant: 1.1 kB. 2 states, 23 arcs, 23 paths.
defined EnglishSandboxSurfaceOnset: 1.9 kB. 4 states, 69 arcs, 12720 paths.
defined EnglishSandboxSurfaceCoda: 1.9 kB. 4 states, 69 arcs, 12720 paths.
defined EnglishSandboxSurfaceSyllable: 5.3 kB. 14 states, 266 arcs, 2912371200 paths.
defined EnglishSandboxSurface: 5.9 kB. 12 states, 306 arcs, Cyclic.
defined EnglishSandboxPlainVocalic: 939 bytes. 8 states, 21 arcs, 22 paths.
defined EnglishSandboxPlainLiquid: 287 bytes. 2 states, 2 arcs, 2 paths.
defined EnglishSandboxPlainNasal: 287 bytes. 2 states, 2 arcs, 2 paths.
defined EnglishSandboxStarVowel: 1.2 kB. 3 states, 24 arcs, 23 paths.
defined EnglishSandboxStarDiphthong: 445 bytes. 5 states, 7 arcs, 5 paths.
defined EnglishSandboxStarConsonant: 1.1 kB. 3 states, 23 arcs, 22 paths.
defined EnglishSandboxStarVocalic: 1.2 kB. 5 states, 27 arcs, 28 paths.
defined EnglishSandboxStarNasal: 329 bytes. 3 states, 3 arcs, 2 paths.
defined EnglishSandboxStarLiquid: 329 bytes. 3 states, 3 arcs, 2 paths.
defined EnglishSandboxStarVelarStop: 329 bytes. 3 states, 3 arcs, 2 paths.
defined EnglishSandboxWeakTailVowel: 2.2 kB. 67 states, 95 arcs, 38 paths.
defined EnglishSandboxInitialKnMarkers: 1.0 kB. 9 states, 40 arcs, Cyclic.
defined EnglishSandboxConsonantRules: 8.6 kB. 26 states, 479 arcs, Cyclic.
defined EnglishSandboxGhMarker: 3.6 kB. 7 states, 171 arcs, Cyclic.
defined EnglishSandboxSilentInitialCleanup: 418 bytes. 1 state, 4 arcs, Cyclic.
defined EnglishSandboxGlideDeletion: 3.8 kB. 9 states, 186 arcs, Cyclic.
defined EnglishSandboxGhDeletion: 3.5 kB. 7 states, 165 arcs, Cyclic.
defined EnglishSandboxWestGermanic: 800 bytes. 5 states, 23 arcs, Cyclic.
defined EnglishSandboxOpenSyllableLengthening: 6.5 kB. 10 states, 321 arcs, Cyclic.
defined EnglishSandboxBreakingLengthening: 3.5 kB. 10 states, 163 arcs, Cyclic.
defined EnglishSandboxShortVowelSplit: 2.7 kB. 5 states, 109 arcs, Cyclic.
defined EnglishSandboxCoreVowelRules: 2.8 kB. 14 states, 131 arcs, Cyclic.
defined EnglishSandboxGreatVowelShift: 3.4 kB. 8 states, 151 arcs, Cyclic.
defined EnglishSandboxPostVocalicRSmoothing: 392 bytes. 2 states, 4 arcs, Cyclic.
defined EnglishSandboxWeakTailReductions: 8.8 kB. 48 states, 515 arcs, Cyclic.
defined EnglishSandboxPostVocalicRLoss: 2.0 kB. 6 states, 87 arcs, Cyclic.
defined EnglishSandboxVowelRules: 11.1 kB. 29 states, 623 arcs, Cyclic.
defined EnglishSandboxOrthography: 512 bytes. 3 states, 10 arcs, Cyclic.
defined EnglishSandboxProtoInput: 18.0 kB. 233 states, 1082 arcs, 9992034 paths.
defined EnglishSandboxReflexes: 47.8 kB. 344 states, 2950 arcs, 48059871 paths.
defined EnglishSandbox: 27.4 kB. 245 states, 1632 arcs, 10110408 paths.
27.4 kB. 245 states, 1632 arcs, 10110408 paths.
## 2025-12-04

### KIT/FOOT contexts + /r/-smoothing harness

- Extended EnglishSandboxShortVowelSplit so FOOT now targets alveolar codas in both starred and plain alphabets ({t/d/z} + weak-tail templates, plain {l/r} codas) and added a plain {*i}->{i} feed so the KIT split can finally act on closed {i} syllables. Introduced EnglishSandboxPostVocalicRSmoothing between the vowel stack and /r/-loss so {ɪ} can surface as {ɪə} before EnglishSandboxPostVocalicRLoss deletes {r}.
- Recompiled via docker compose exec backend sh -lc "cd /usr/app && foma -f fsts/english_brace_sandbox.txt" and wrote the attested-form sweep to tmp/english_sandbox_results.json with the Python harness (loops 376 English IPA forms through flookup english_brace_sandbox.bin).
- Current sandbox stats: 134/376 successes (down from the previous 179 baseline). Failure buckets from the JSON lens land at KIT=49, FOOT=21, weak-tail=44, post-vocalic /r/=58, rounded {ɔ/əʊ}=28, plus 118 uncategorised other items that need triage.
- Spot checks show the new /r/ smoothing exposes {bird/birr} for bɪəd/bɪər, but bʊzəm and pʊdər remain +? even after the broader {u} contexts. Need to audit why so many previously good entries dropped during this pass before attempting further vowel work.

### KIT tracing & stage export plan

- Added  as a first pass at stage tracing, but the sandbox stages currently emit ??? because the cascade never saves intermediate automata. Full traces will require refactoring the FST to save each stage (similar to the GermanAfter* bins) so we can flookup them directly inside Docker.
- Next session: split out the sandbox stages into explicit save targets (e.g., english_sandbox_after_glide.bin, english_sandbox_after_vowel_rules.bin), update the docker build to emit those bins, and then rerun the tracer to capture true stage-by-stage outputs for KIT words (*fiskaz, *gebaną, *swestēr).
- Once tracing works, resume the KIT fixes bucket-by-bucket (post-vocalic /r/, {sk} palatalisation, nasal+stop, sw glides) with harness checks after each change so we stay ≥179/376.
## 2025-12-12

### English gold IPA normalized to RP / non-rhotic baseline

- Cleaned every English row in `server/data/germanic-aligned-final.tsv` whose counterpart contains an orthographic `r` but whose surface tokens still ended in a vowel + `r`. Each of the 40 affected entries now drops the trailing `r` (e.g. `adder ædər→ædə`, `fire faɪər→faɪə`, `door dɔːr→dɔː`). Mirrored the same edits into the staged snapshot (`server/pipeline/output/germanic/stage3/germanic-aligned-final.tsv`) so downstream docs stay in sync.
- Added `server/tools/validate_english_rhoticity.py` to guard the policy going forward. The helper scans any TSV for English rows where the tokens end in `…V r` and fails fast; CI/local runs should call `python3 server/tools/validate_english_rhoticity.py` (optionally pointing it at the stage3 export) whenever the gold data changes.
- Reran the validator on both the canonical and stage3 TSVs — both now report “No rhotic entries detected.” Next time the gold file is touched, run the validator before committing so we don’t regress toward GA-style outputs again. Once the analyzer tweaks land, rerun `python3 server/tools/english_apply_down_stats.py` to confirm the RP-aware surfaces align with the updated targets.

### Rhotic development roadmap (historical targets before coding)

- **Proto rhotic fronting / colouring.** Replace the `{*rgă→rəʊ}` placeholder mindset with staged vowel shifts that mirror the historical chronology.
  - Pre-OE: specify how `{*er}` becomes `{æər}/{ɜːr}`, `{*ir}` becomes `{ɪr}`, `{*or}/{*ur}` becomes `{ɔːr}` before any breaking occurs. List the actual proto clusters (`rdă`, `rgă`, `rwō`, `rθo`, …) so the rules operate on contexts rather than word lists.
  - OE breaking: document the environments that should introduce `{ea/eo/ia}` diphthongs so ME smoothing can later yield RP `ɪə/ɛə/ɜː` without hard-coded outputs.
  - ME smoothing + post-vocalic /r/ loss: describe the sequence (breaking → smoothing → /r/ loss) so `EnglishSandboxRhoticBreaking`/`RhoticColoring` can implement the correct order once we update the rules.
### Modern English (OE→Modern) roadmap — paused
- These steps are intentionally separated from PGmc→OE work; only resume if explicitly requested.

- **Consonant resolution.** Note explicitly why RP keeps /θ/ in `earth/hearth` but /d/ in `herd/word/sword` (OE retention vs. later analogical leveling). The current single-output rewrite matches the intended behaviour, but the reasoning should be recorded so future edits don’t reintroduce branching.
- **Weak-tail & schwa preservation.** RP retains final /ə/ in orthographic `-er/-re` endings (`faɪə`, `ædə`). Outline which morphological endings should keep vs. drop the schwa so `EnglishSandboxWeakTailCleanup` can be rewritten with historical cues instead of deleting every `{*ə}` at word end.
- **Next execution steps:** once the above roadmap is nailed down, implement the stages in order (ProtoRhoticFronting → OE breaking/smoothing → Post-vocalic /r/ loss → Weak-tail cleanup). After each change, rerun `python3 tools/trace_english_sandbox.py --lexeme-file tmp/rhotic_test_set.txt --brace-diphthongs` and `python3 server/tools/english_apply_down_stats.py` to measure progress beyond the current 21/376 baseline.

#### Detailed blueprint (grounded in the standard OE/ME chronology)

- **Anglian colouring before breaking (pre-7th c.).**
  - `{*e}` in `{*er}` clusters should front/back toward `{æɑr}` so the later OE breaking produces `ea`. Limit this to `{*r}` followed by a consonant or boundary; leave glide environments alone so `seer`-type words stay bright.
  - `{*i}` in `{*ir}` (except before `{*j}`) lowers to `{*er}` then `{*æɑr}`, matching the documented change that feeds `bird`, `first`, etc.
  - `{*o}`/`{*u}` before `{*r}` should raise to `{*ur}/{*ɔːr}` only when followed by a consonant, mirroring WG rounding that later yields RP /ɔː/.
  - Capture these contexts in `EnglishSandboxProtoRhoticFronting` so OE breaking has the right inputs.

- **OE breaking + ME smoothing.**
  - Add an `EnglishSandboxOEBreaking` stage: `{æ}` → `{ea}` before `{*rC}` or `{*lC}`, `{e}` → `{eo}` before `{*rC}`, `{i}` → `{ie}` before `{*rC}`. These match the conditions in Campbell §§216–219 and explain why `bear/bier` diverge from `bar`.
  - Follow with an `EnglishSandboxMESmoothing` stage (before post-vocalic /r/ loss) that maps `{ea/eo/ie}` + `{*r}` to the RP nuclei: `{ea}` → `{ɛə}`, `{ie}` → `{ɪə}`, `{eo}` → `{ɜː}` (voicing-dependent). This should replace the lexeme-specific rewrites currently living in `EnglishSandboxRhoticBreaking`.

- **Consonant outcomes.**
  - Document the historical split: native `{*rθ/ð}` clusters retain /θ/ in RP (`earth/hearth`), while `{*rd}` words level to /d/ in late ME (`herd/word/sword/bird`). Keep the Foma rule single-output but annotate these buckets so we know why the mapping exists and where it should apply.

- **Weak-tail schwa.**
  - RP keeps schwa in orthographic `-er/-re` (from OE `-ere`). Plan to guard those endings via a morphological check (e.g., look for `{*r}` + weak-tail vowel) so `EnglishSandboxWeakTailCleanup` only drops `{*ə}` when the historical dialect really loses it.

- **Execution order reminder.**
  1. Implement the contextual colouring rules in `EnglishSandboxProtoRhoticFronting` (using the `list_rhotic_contexts.py` inventory as a sanity check) and verify via tracer that `{*bergą/*bardaz/*barwōn}` take the correct vowels before breaking.
  2. Introduce the explicit OE breaking + ME smoothing stages, removing the hacky `{*rgă→rəʊ}` rewrites from `EnglishSandboxRhoticBreaking`.
  3. Revisit `EnglishSandboxRhoticBreaking` only after the vowel stages are in place so it simply handles consonant selection (θ vs. d) and any remaining diphthong adjustments.
  4. Redesign the weak-tail cleanup to respect RP schwa retention.
  5. After each milestone, rerun the rhotic tracer and `english_apply_down_stats.py` to ensure we stay branch-free and track improvements beyond the current 21/376 exact matches.

### Old English staging / TSV overhaul (PGmc → OE layer)
- Completed and superseded; see the 2025-12-21 consolidated PGmc→OE TODOs for current work.
- Open question: should the TSV adopt PGmc **ǭ** (e.g., *rindǭ*) instead of the current **ō**-only convention? For now we normalized to **ō** to keep the dataset consistent; revisit if we decide to shift the entire PGmc orthography.

## 2025-12-12

### Old English data population
- Added a Wiktionary scraper (`server/tools/fetch_old_english_from_wiktionary.py`) and parsed the Swadesh + API data into `server/data/old_english_wiktionary.tsv`; the updater now merges both sources and writes IPA/tokens/notes back into the aligned Germanic TSVs.
- Ran the helper across all 376 English concepts so the Old English rows now have attested lemmas (373 entries auto-filled; annotated `fodder fōdor` and `tongs tange` manually, marked `knob` as lacking an OE cognate per the etymology).
- Documented the workflow in `README.md` + `docs/runbook.md`, and added `server/tools/validate_old_english_pairs.py` to guard the 1:1 English↔OE coverage going forward.

- **PGmc→OE stage split.** Added `EnglishProtoToOE` inside `server/fsts/germanic.txt` so the early vowel/weak-tail rules share a single hook and tracer snapshot (`english_after_proto_to_oe.bin`).

### Proto→OE instrumentation & findings (2025-12-12)
- Consolidated the early PGmc→OE vowel/weak-tail rules under `EnglishProtoToOE` and added the `english_after_proto_to_oe.bin` stage log so we can trace that layer independently of the later ME/RP stack.
- Wrote `server/tools/evaluate_proto_to_oe.py` and ran it against `english_after_proto_to_oe.bin`: only 1/376 Old English rows matched at that time; this baseline is superseded by the 2025-12-21 diagnostics (see current focus above).
- Next coding steps now live in the consolidated PGmc→OE TODOs under 2025-12-21.

## 2025-12-21

### Old English core refactor + diagnostics
- Split the English pipeline into `OldEnglishCore` + `EnglishOEToModern` so the OE transducer is not just an alias of Modern English (`server/fsts/germanic.txt`).
- Added OE-specific surface filter and orthography: `OldEnglishSurface`, `OldEnglishRemoveStars`, `OldEnglishOrthography` now apply at the end of the OE stack (including `x -> h`, `θ -> þ`, `ʃ -> ċ`).
- Phonological tweaks in the PGmc→OE block:
  - Removed blanket final *a apocope; retained only `*ą/*ă -> *a` (per high-vowel apocope focus).
  - Added `OldEnglishSkPalatalization` (`*sk -> ʃ` before front vowels).
  - Added a conservative high-vowel apocope rule for final `*i/*u` after heavy or two-light syllable patterns (approximate segmental conditioning; still needs refinement).

### PGmc→OE TODOs (consolidated)
- **Separation model:** Old English is its own doculect with a PGmc→OE stack (`OldEnglishCore` + OE surface/orthography). Modern English is a separate doculect with an OE→Modern stack (`EnglishOEToModern`), and OE work should not use ME/RP rules.
- **Definition locality (housekeeping):** move PGmc→OE rule definitions so they live adjacent to the OE stack (mirroring how Dutch-specific rules sit near the Dutch stack), instead of being scattered among Modern English rule blocks.
- **Proto gate coverage:** `xw/hw` clusters already pass `EnglishProtoInput`; remaining ProtoInput failures are elsewhere (e.g., `*xabukăz`, `*xemenăz`, `*xnakkăz`, `*regna-bugōn`, `*sumerăz`). Focus on missing onset/weak‑tail clusters, not `xw/hw`.
- **High‑vowel apocope expansion:** broaden final `*i/*u` deletion beyond the current “long/diphthong + C” and “two light syllables” conditions; target observed `-i/-u` outputs (e.g., `ballu/bebru/balgi/bugu/crafti/fehu/felþu`) while staying phonetic.
- **Weak‑tail cleanup (`-ana` → `-an`):** reshape or drop weak‑tail `ă/ą` endings in verbs so outputs like `bacana/gennana/brecana/brengana/brūcana` converge on attested `-an`.
- **OE consonant innovations:** add the missing PGmc→OE consonant changes (palatalisation in OE contexts, rhotic prep, targeted lexical replacements) so stage outputs align with `COUNTERPART` without using ME/RP rules.
  - Early final‑ă apocope (post‑z deletion) now in place; `*dagăz` yields `dæġ`. See potential side‑effects list at `docs/debug_snapshots/oe_final_a_apocope_side_effects_2025-12-23.txt`.
- **Validation loop:** after each change, rerun the OE evaluator (`python3 tools/evaluate_proto_to_oe.py --bin old_english.bin`) and keep `docs/debug_snapshots/` traces for regressions.

### PGmc→OE chronology audit (2025-12-21)
- **Sources consulted (web, Dec 21 2025):**
  - Wikipedia: *Phonological history of Old English* (breaking/back mutation, high‑vowel loss, h‑loss, syncopation ordering).
  - Wikipedia: *Ingvaeonic nasal spirant law* (nasal loss before fricatives + compensatory lengthening).
  - Wikipedia: *Old English phonology* (palatalization/velar vs palatal distributions).
  - Cambridge Core: *Reconstructing the historical phonology of Old English* (debate over standard chronology of fronting/breaking).

- **Reference timeline (condensed, with known debates):**
  - i‑umlaut (front mutation) precedes many OE alternations; later syncopation and vowel loss are ordered after it in standard accounts. 
  - Breaking/retraction of front vowels before h, rC, lC (and some w contexts) is dialect‑conditioned and not uniform across OE. 
  - Ingvaeonic nasal spirant law deletes nasals before fricatives with compensatory lengthening (‑ns‑, ‑nþ‑, ‑mf‑). 
  - Back mutation (u‑umlaut) diphthongizes short e/i (sometimes a) before back vowels in the following syllable, with strong dialect differences. 
  - High‑vowel loss deletes unstressed i/u after heavy syllables (long vowel/diphthong or closed syllable), but not after light syllables. 
  - H‑loss and contraction occur after breaking in standard accounts; vowel contraction follows h‑loss.
  - Palatalization of velars (k/g, and sc) before front vowels yields ċ/ġ alternations and later phonemic splits.

- **What our current PGmc→OE stack already models:**
  - WG monophthongisation (*ai/*au → *ā/*ō).
  - Open‑syllable lengthening.
  - Anglo‑Frisian breaking/rounding before liquids, r, and w.
  - Velar shortening of *ō; u‑rounding before r.
  - Weak‑tail marker/reduction; conservative high‑vowel apocope.
  - *sk‑palatalisation before front vowels.

- **Major gaps vs. the reference chronology (priority‑ordered):**
  1. i‑umlaut is absent (core OE morphology driver).
  2. Back mutation (u‑umlaut) is absent and dialect‑sensitive.
  3. Ingvaeonic nasal spirant law is absent and should affect vowel length and nasal loss.
  4. High‑vowel loss conditioning is under‑applied relative to heavy vs. light syllable split.
  5. H‑loss + contraction are missing, and the timing vs. breaking is not modeled.
  6. Breaking/back‑mutation order and dialect conditioning are not modeled; current rules are too broad.
  7. Palatalization of velars beyond *sk (k/g before front vowels; ċ/ġ outcomes) is missing.

- **Immediate next steps (OE‑only, chronological order):**
  1. Add i‑umlaut with clean conditioning; trace impact on OE counterparts.
  2. Add back‑mutation (u‑umlaut) with conservative, dialect‑agnostic defaults.
  3. Add Ingvaeonic nasal spirant law + compensatory lengthening.
  4. Re‑specify close‑vowel loss to match heavy vs. light syllable conditioning.
  5. Add h‑loss and contraction; re‑check breaking order afterward.
  6. Add palatalization for velars before front vowels (ċ/ġ), not just *sk.

### OE evaluator snapshot (old_english.bin)
- Total OE rows: 376
- Matches: 2
- No output: 21
- Mismatches: 353
- Sample mismatches: `*bakăną -> bacana` vs `bacan`, `*bōkō -> bucō` vs `bēċe`, `*balgiz -> balgi` vs `bielġ`.
- Common issue bucket still dominated by `-ana` outputs and lingering final high vowels.

### Ending diagnostics (old_english.bin)
- Final vowel distribution: `a` 212, `n` 43, `ō` 33, `i` 22, `u` 20.
- Final high vowels: `i` 22, `u` 20; most common contexts `ti/di` for `-i`, `þu/du/tu` for `-u`.
- Sample `-i/-u` outputs: `ballu` (ball), `bebru` (beaver), `balgi` (belly), `crafti` (craft), `bugu` (bough).
- Sample `-ana` outputs where target is `-an`: `bacana` (bake), `gennana` (begin), `brecana` (break), `brengana` (bring), `brūcana` (brook).

### OE diagnostics refresh (2025-12-21)
- Recompiled FSTs and reran `tools/evaluate_proto_to_oe.py` against `old_english.bin`; totals unchanged (Matches 2 / No output 21 / Mismatches 353). Snapshot: `docs/debug_snapshots/oe_eval_2025-12-21.txt`.
- Recomputed final‑vowel distribution + `-i/-u` contexts; counts unchanged and examples still dominated by final high vowels and `-ana` endings. Snapshot: `docs/debug_snapshots/oe_final_vowel_diag_2025-12-21.txt`.

## 2025-12-21 (plan update: regular sound change only)

### Guiding assumption (Hill 2014)
- Sound change is regular and phonetically conditioned; apparent grammatical conditioning is modeled as regular sound change plus analogy/borrowing. We encode only the regular phonological development in the FSTs.

### New diagnostics captured
- `docs/debug_snapshots/oe_tail_bucket_2025-12-21b.txt`: lists all `-i`, `-u`, `-ana` outputs with proto + attested OE.
- `docs/debug_snapshots/oe_tail_bucket_classified_2025-12-21b.txt`: classifies `-ana` outputs by attested OE ending (e.g., `-an`, `-ian`, `-can`, `other`).
- `docs/debug_snapshots/oe_high_vowel_targets_2025-12-21b.txt`: classifies `-i/-u` outputs by attested OE final (vowel vs consonant).
- `docs/debug_snapshots/oe_high_vowel_weight_diag_2025-12-21b.txt`: estimates heavy vs light syllable before final `-i/-u`.
- `docs/debug_snapshots/oe_ana_noninfinitive_2025-12-21b.txt`: isolates `-ana` outputs with non‑infinitive attested endings (must not be deleted by OE sound change).

### Next steps (phonological only, no morphological conditioning)
1. **High‑vowel loss (regular):** use the weight diagnostics to implement a heavy‑syllable‑conditioned final *i/*u apocope. Prefer explicit heavy/light marking (H/L) inserted by segmental context, then delete markers after the rule; avoid morphological categories.
2. **Weak‑tail *a (schwa) handling:** do **not** blanket delete `-ana` in PGmc→OE. Only apply any *a loss if a purely phonological environment deletes it without touching the non‑infinitive list; otherwise defer to later (OE→ME) as analogical leveling.
3. **Umlaut/back‑mutation sanity check:** confirm the new umlaut/back‑mutation rules apply only in phonological environments (following *i/*j or back vowels/w) with a small probe list; tighten triggers if over‑application appears.
4. After each change: rebuild via Docker, rerun OE evaluator + the two diagnostics, and snapshot in `docs/debug_snapshots/`.

### High‑vowel loss debug (2025-12-21)
- Found nondeterminism in the new H‑marker rule: `OldEnglishWeightMarkers` was inserting `{H}` in multiple optional positions, yielding both apocopated and non‑apocopated outputs (e.g., `ballu` + `ball`).
- Fixed by rewriting final `*i/*u` directly to `{H}{*i}/{H}{*u}` in heavy contexts, then deleting `{H}{*i}/{H}{*u}` in `OldEnglishHighVowelApocope`.
- Added stage bins to isolate the fix:
  - `english_after_proto_to_oe_weak_tail.bin`
  - `english_after_proto_to_oe_weight_markers.bin`
  - `english_after_proto_to_oe_apocope.bin`
  - `english_after_proto_to_oe_weight_cleanup.bin`
- Verification (sample probes): `balluz/balgiz/bebruz` now yield a **single** output at each stage, with apocope firing deterministically in heavy contexts.
- Updated diagnostics:
  - `docs/debug_snapshots/oe_eval_2025-12-21e.txt` (Matches 8 / No output 18 / Mismatches 350).
  - `docs/debug_snapshots/oe_final_vowel_diag_2025-12-21e.txt` shows **0** final `-i/-u` outputs after the heavy‑syllable apocope.

### OE weak‑tail marker fix (2025-12-21)
- Renamed `EnglishWeakTailMarker/EnglishWeakTailReduction` to `OldEnglishWeakTailMarker/OldEnglishWeakTailReduction` and confined them to marking only the weak‑tail vowel.
- Old behaviour collapsed `*a n(n) ą` into a single `{*ă}`, deleting the `n(n)` cluster (e.g., `*banną → *ba` in `ProtoToOE`), which violated the “no blanket -ana deletion” policy.
- New marker rules only rewrite `*n/*m + *ą` to `*n/*m + *ă`, so `*banną → *banna` at `ProtoToOE` and the tail stays intact for later, phonologically justified cleanup.
- Recompiled `fsts/germanic.txt` + `fsts/old_english_sandbox.txt` and captured:
  - `docs/debug_snapshots/oe_eval_2025-12-21g.txt` (Matches 5 / No output 11 / Mismatches 360).
  - `docs/debug_snapshots/oe_apply_down_stats_2025-12-21g.txt` (apply‑down coverage snapshot).
  - `docs/debug_snapshots/oe_tracer_log_2025-12-21g.txt` (OE sandbox tracer).

### OE weak‑tail nasal vowel loss (PGmc *‑aną → OE ‑an) (2025-12-21)
- Replaced the heavy‑syllable apocope experiment with a chronologically correct PGmc→OE rule: drop final `*ą` after `*n`/`*m` at word‑end, then reduce remaining `*ą/*ă` to `*a`.
- This targets the early loss of final nasal vowels (infinitive `*‑aną → ‑an`) without touching the later loss of final `‑n`.
- Diagnostics (post‑change):
  - `docs/debug_snapshots/oe_eval_2025-12-21j.txt` (Matches 13 / No output 11 / Mismatches 352).
  - `docs/debug_snapshots/oe_apply_down_stats_2025-12-21j.txt` (apply‑down coverage snapshot).
  - `docs/debug_snapshots/oe_tracer_log_2025-12-21j.txt` (OE sandbox tracer).
- `docs/debug_snapshots/oe_tail_bucket_2025-12-21j.txt` + `oe_tail_bucket_classified_2025-12-21j.txt` (tail bucket after nasal‑vowel loss).
- Note: the tail bucket still contains `swan` (`*swanăz → sʋana`), which is not from `*‑aną`; flag for later review of `*‑ăz` handling.

### OE diagnostics follow‑up: orthography + rhotacism (2025-12-22)

- Updated `server/tools/evaluate_proto_to_oe.py` to default to `old_english.bin` (post‑orthography + surface filter). New totals: Matches 24 / No output 18 / Mismatches 334.
- Comparing `english_after_proto_to_oe.bin` vs `old_english.bin` shows 7 items lose outputs only after the OE surface filter; all 7 still contain `{*z}` (or heavy clusters) and are rejected by `OldEnglishSurfaceConsonant` (no `z`).
- Tracing those 7 (`bazją`, `deuzą`, `xazwăz`, `xuzdą`, `liznōjăną`, `mizdō`, `funxwstiz`) shows `EnglishZRhotacism` never fires; `ConsonantRules` leaves `{*z}` intact in every case.
- Likely structural issue: `EnglishStarVocalic` (and other `EnglishStar*`) are defined before `GermanStar*` and appear to compile as literal symbols (foma logs show 1‑arc sets), so the rhotacism context never matches.
- Even if the set is fixed, the current rule `V _ V` is historically too narrow: PGmc *z should rhotacize in post‑vocalic contexts like V‑z‑j/w/n/d‑V (berry, hair, learn, meed, hoard) before later glide/umlaut changes. Chronology: rhotacism must be early (before w‑glide changes and OE vowel rules).
- `funxwstiz` (fist) is not a rhotacism case; it survives with a heavy `xʋst` cluster and fails the OE surface coda limit (needs separate cluster simplification / h‑loss logic).

### OE sandbox mismatch patterns (2025-12-22)
- **Scope note:** work is focused on the **OE sandbox** for now; do not apply ME/RP fixes to these issues.
- **Mismatch pattern sweep (summary):**
  - Missing i‑umlaut/fronting (most frequent).
  - Missing palatalization (ċ/ġ outcomes absent).
  - Missing breaking/diphthongs (eo/ie).
  - Missing final ‑e.
  - Missing final ‑n (including infinitive ‑an).
- **OE sandbox TODOs (from mismatch patterns):**
  1. **I‑umlaut/fronting:** broaden or re‑order triggers so OE front vowels appear where expected.
  2. **Palatalization:** add/repair k/g → ċ/ġ before front vowels (and ordering vs. umlaut).
  3. **Breaking:** strengthen OE breaking contexts (before r/l/h clusters, etc.).
  4. **Final ‑e retention:** prevent weak‑tail cleanup from removing OE final ‑e where attested.
  5. **Final ‑n retention:** ensure infinitive/weak verb ‑an survives; confirm no over‑drop after nasal‑vowel loss.

### OE i‑umlaut status (2025-12-22)
- **What we added:** expanded `OldEnglishIUmlaut` to cover `*æ → *e`, `*e → *i`, and `*ū → *ȳ`; added `*ȳ` to starred vowel inventories + `OldEnglishRemoveStars`.
- **What works now (ordering probe):** i‑umlaut fires inside the PGmc→OE block before weak‑tail cleanup/apocope (e.g., `mūsiz → *m*ȳ*s`, `brūdiz → *b*r*ȳ*d`, `fōtiz → *f*ē*t`). Snapshot: `docs/debug_snapshots/oe_iumlaut_ordering_probe_2025-12-22.txt`.
- **What is still missing:** fronting/raising does not trigger in many common i/j contexts (`laubjăną`, `sandjăną`, `bazją` still un‑fronted), so the **trigger environment is still too narrow** and diphthong umlaut (ea/eo → ie/īe) is not modeled yet.
- **Resources & probes already available:**
  - Ordering probe: `docs/debug_snapshots/oe_iumlaut_ordering_probe_2025-12-22.txt`
  - Full‑set i/j‑trigger probe: `docs/debug_snapshots/oe_iumlaut_fullset_probe_2025-12-22.txt`
  - Candidate list (heuristic i/j triggers): `docs/debug_snapshots/oe_iumlaut_candidates_2025-12-22.txt`
- **Next steps:** relax the right‑context for i‑umlaut (beyond `EnglishStarConsonantSeq` where needed), add diphthong umlaut rules (ea/ēa, eo/ēo → ie/īe), and re‑run the full‑set probe + OE apply‑down stats to check for over‑application.

### OE breaking reorder + diagnostics (2025-12-22)
- **Breaking now precedes GH‑marking and W‑glide** so the conditioning consonants are still visible when OE breaking applies; this matches the chronology (breaking before h‑loss and before later glide re‑analysis). Implemented in both `server/fsts/germanic.txt` and `server/fsts/english_brace_sandbox.txt`.
- **Sandbox breaking rules aligned to OE** (`*a/*æ → *ea`, `*e → *eo`, `*i → *ie` in rC/lC/h/w contexts). This replaced the old `{*a → *ō}` placeholder.
- **Tracer instrumentation updated** to include `WGlide` and rebuilt the per‑stage bins; new probe log: `docs/debug_snapshots/oe_breaking_probe_2025-12-22f.txt` (shows `*bergą → *eo`, `*bardăz → *ea`, `*erθo → *eo`, `*fextăną → *eo` at `BreakingLengthening`).
- **Regression scan (OE apply‑down):** `docs/debug_snapshots/oe_apply_down_stats_2025-12-22p.txt` shows 22 exact matches / 370; mismatch buckets still dominated by i‑umlaut/fronting and missing breaking/diphthongs.

### OE i‑umlaut deep dive (2025-12-23)
- **Targeted umlaut misses (tight heuristic):** only 3 suspected true i‑umlaut failures when PGmc has an i/j trigger and OE expected shows an umlauted vowel but output does not. See `docs/debug_snapshots/oe_i_umlaut_deep_dive_2025-12-23.txt`.
  - `*rugiz` → expected **ryġe**, output **rūġ** (u‑umlaut miss)
  - `*jugunθiz` → expected **ġeoguþ**, output **ġūgyþ** (u‑umlaut miss)
  - `*sōkjăną` → expected **sēċan**, output **suscġan** (ō‑umlaut miss)
- **Palatalization warning:** cases where expected **ċ** surface as **sc** are now visible; that’s a palatalisation failure in the OE stack (orthography is masking it), not a spelling preference. Keep an eye on outputs like `suscġan` vs expected `sēċan`.

### OE palatalization vs fronting/umlaut split (2025-12-23)
- **Snapshot:** `docs/debug_snapshots/oe_palatal_vs_fronting_split_2025-12-23.txt`.
- **Key diagnosis:** the 7 “palatalization missing” cases are **not** palatalization-rule failures; palatalization never triggers because the **front‑vowel context is missing**. These are **fronting/breaking/umlaut issues** upstream.
- **True i‑umlaut misses (strict trigger):** only 1 case (`*rugiz → ryġe` expected, output `rūġ`).  
  The bulk of the “i‑umlaut/fronting missing” bucket is actually **fronting missing with no i/j trigger** (143 cases).
- **Next actions:** prioritize fronting/breaking changes that create front‑vowel contexts (esp. for *bōkō, *θankăz, *dranką, *fleugăną, *xunăgą), then re‑check palatalization buckets.

### OE i‑umlaut/fronting bucket diagnostics (2026-01-01)
- **RemoveStars fix:** added `{*ċ} -> ċ` and `{*ġ} -> ġ` in `OldEnglishRemoveStars` so orthography outputs no longer leak starred palatals. This dropped `no_output` mismatches from 50 → 12.
- **Updated apply‑down stats:** `docs/debug_snapshots/oe_apply_down_stats_2026-01-01a.txt` (still 40 exact matches / 370 total).
- **Top buckets:** i_umlaut_or_fronting_missing (147), other (124), breaking_missing (30), no_output (12), long_vowel_missing (10).
- **Bucket subgrouping (heuristic, broader set = 178 items):** `docs/debug_snapshots/oe_iumlaut_fronting_subgroups_2026-01-01.txt`.
  - back_vowel_follow_only: 98 (likely **a‑restoration** contexts per Hogg)
  - iumlaut_trigger_only: 3 (cleanest true i‑mutation misses)
  - nasal_block_only: 2 (fronting blocked before nasals)
- **Staged traces for each subgroup:** `docs/debug_snapshots/oe_iumlaut_fronting_subgroup_traces_2026-01-01.txt`.
  - i‑mutation trigger examples: *furxtīn → fōrhtīn (expected fryhtu), *raukiz → reaċ (expected rēc), *rugiz → rūġ (expected ryġe)
  - back‑vowel follow examples: *bergą → beorga (expected beorg), *bōkō → bucō (expected bēċe), *gennăną → ġennan (expected beginnan)
  - nasal‑block examples: *dranką → drænca (expected drenċ), *tangō → tængō (expected tange)

### OE ai cleanup + ǣ surface fix (2026-01-01)
- Removed `OldEnglishAiMonophthongization` (never fires because WG monophthongization already rewrites *ai → *ā).
- Added `{*ǣ} -> ǣ` to `OldEnglishRemoveStars` so OE surface accepts long fronted a (e.g., *dailiz → dǣl, *xaiθiz → hǣþ).
- Updated mismatch totals (post-fix): Total mismatches 324; i_umlaut_or_fronting_missing 22; breaking_missing 18; long_vowel_missing 30; palatalization_missing 17; other 225; no_output 12.
- New snapshot: `docs/debug_snapshots/oe_stage_traces_2026-01-01i.txt`.

### OE diagnostics: mismatch closeness + diacritics (2026-01-02)
- Apply-down stats (latest run): `docs/debug_snapshots/oe_apply_down_stats_2026-01-02h.txt`
  - Exactly one correct output: **64 / 370** (no_output 12; multiple outputs 0).
  - Mismatch buckets: i_umlaut_missing_true 16; fronting_missing_no_trigger 33; breaking_missing 20; long_vowel_missing 6; palatalization_missing 3; other 216.
- **Closeness scan** highlights that many mismatches are near-misses:
  - `docs/debug_snapshots/oe_mismatch_closeness_2026-01-02a.txt` shows most mismatches at distance 1–2 (81 at dist=1, 112 at dist=2).
  - `docs/debug_snapshots/oe_mismatch_closeness_norm0_2026-01-02.txt` lists 11 cases where normalized (diacritic-stripped) distance is 0, e.g. `*dōną → dōn` vs expected `don`, `*etăną → ētan` vs `etan`, `*fiskăz → fisc` vs `fisċ`, `*skīnăną → scīnan` vs `sċīnan`.
- **Diacritic mismatch traces** (`docs/debug_snapshots/oe_diacritic_mismatches_traces_2026-01-02.txt`) confirm these are orthography/diacritic alignment issues rather than phonology failures (e.g., `*tredăną → trēdan`, `*sturmăz → stōrm`, `*θurnuz → þōrn`, `*fadēr → fædēr`).
- **Long-vowel missing probe narrowed** to 6 items (previously 7):
  - Current list: `*kewwăną → ċeowwan (expected ċēowan)`, `*xazwăz → hærw (expected hǣr)`, `*xattuz → hatt (expected hōd)`, `*end → end (expected ān)`, `*slaxăną → sleaan (expected slēan)`, `*wegăz → weġ (expected wē)`.
  - Traces in `docs/debug_snapshots/oe_long_vowel_missing_traces_2026-01-02d.txt`.

### Unified OE mismatch report (2026-01-03)
- New script: `server/tools/oe_mismatch_report.py` supersedes `oe_mismatch_patterns.py` + the separate “other subtypes” report.
- Latest unified report: `docs/debug_snapshots/oe_mismatch_report_2026-01-03a.txt` (includes the main buckets plus the “other” subcategories side by side).

### OE orthography cleanup + reports (2026-01-18)
- **Dotted palatal orthography:** `OldEnglishOrthography` now maps `/ʃ/` to `{sċ}` and allows `{sċ}` in the surface filter.
- **/dʒ/ + /j/ spelling:** `OldEnglishOrthography` maps `{ʤj}` to `{ċġ}`; `{ʤ}` and `{j}` still map to `ġ`.
- **Reports run (latest):**
  - `server/docs/debug_snapshots/oe_mismatch_report_2026-01-18w.txt`
  - `server/docs/debug_snapshots/oe_full_trace_report_2026-01-18w.txt`
- **Totals (2026-01-18w):** total mismatches 294; `palatal_marker_variant` = 0; `gemination_extra` = 2.
- **Hedge trace:** `oe_full_trace_report_2026-01-18w.txt` shows `hedge` outputs **both** `hæġġ` and `hæċġ` (Orthography + Surface), indicating nondeterminism is still present.
- **Open issue:** need deterministic pre-orthography cleanup so `*dʒ` + `*j` (and `dʒ` + `j`) coalesce to `{ʤj}` before orthography; avoid producing both `ħeġġ`/`hæġġ` and `hæċġ`.
- **Operational note:** Docker socket permissions intermittently blocked `docker compose exec` in this session; reports were rerun only after restoring Docker access.

### Foma CLI gotchas (2026-01-18)
- **Semicolons matter:** `regex` commands must end with `;` or the network won’t compile (no output from `print words/size`).
- **Reliable one-off tests:** use `foma` with stdin to avoid interactive issues, e.g.
  - `printf 'regex {ʤ} {*j} -> {ʤj};\napply down "ç*æʤ*j"\nquit\n' | foma`
  - Output: `"ç*æʤj"` (confirms the merge rule works on the hedge pre‑orthography form).
