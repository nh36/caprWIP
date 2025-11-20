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
