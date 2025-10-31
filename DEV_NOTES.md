# Daily Hand-off Notes

Add a new dated section (reverse chronological) each time you pause work.
Include:
- Services you touched (Docker/Caddy, datasets loaded).
- Regression harness status and notable warnings.
- Next tasks or blockers.

For the broader documentation map, see `docs/README.md`.


## 2025-10-26

### Services & tests
- `docker compose ps` (requires elevated permissions in this environment) → backend + frontend containers still up; Docker repeats the cosmetic `version` warning.
- Patched `server/tools/log_german_stages.sh` so the probe lexemes are single tokens, then ran `bash server/tools/log_german_stages.sh > /tmp/german_stage_log.txt` to capture Proto→stage outputs for `knewą/braudą/blōdą/tōr`.
- Spot-checked `german_after_longv.bin` directly via `docker compose exec backend ... foma` to confirm the `kniː` forms still appear when the stage is loaded manually.

### Surface-filter back-and-forth (Brace-only is the goal)
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
1. Capture the vowel/consonant inventory from `GermanPreSurface` outputs to see which symbols the brace-aware pipeline actually produces.
2. Redefine `GermanSurfaceVowel/Consonant` in the brace alphabet using that inventory (front-rounded vowels, `{ɔy}`, `{pf}`, `{ts}`, `{ç}`, etc.).
3. Recompile (`foma -f fsts/germanic.txt`), rerun `log_german_stages.sh`, and run the API regression harness to confirm coverage once the new filter lands.

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
