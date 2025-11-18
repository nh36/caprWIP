### 2025-11-01 — German tracing note

- Set up `tools/trace_german_stages.py` so we can trace lexemes through each German stage inside the container; add `--brace-diphthongs` for plain IPA probes.
- Observed that `laukaz/milkiz` still fail right at `GermanProtoInput`, implying the gate expects Burmish-style brace/star tokens (e.g. `{*l}{*au}{*k}{*a}{*z}`). Need to map inputs into that alphabet before checking spirantisation.
- Working examples (e.g. `dɔr`) still analyze successfully. Keep using `dɔr` on the analyzer side, but feed the proto form (`durą`) into any staged traces once the proto gate inputs are fixed.

**Update (2025-11-17):** Stage logging pinpoints `GermanStopShift` as the ach-Laut blocker. The gate already emits `*l*au*k*a*z`; the problem is that `GermanStarVowel/Diphthong/Consonant` list stale `{*…}` tokens, so the stop-shift context never matches. Next pass should rebuild those inventories from the proto macros (mirroring Burmish), instrument `GermanStopShift` to prove the contexts fire, and rerun the six-word trace plus the analyzer probes (`laux/knɛxt/mɪlx` + controls).


# German Surface Follow-up Plan (next window)

## Goal
Recover reliable proto→surface traces for the German FST, then decide whether
to relax the existing `GermanSurface` filter, split the automaton, or migrate the
surface layer to HFST.

## Steps

0. **Unblock proto input first**
   - Confirm `GermanProtoInput` now accepts `*laukaz`/`*milkiz`; walk the staged FSTs to ensure `GermanAfterEw` actually emits the starred strings before continuing with surface tweaks.
   - Re-derive `GermanStarVowel/Diphthong/Consonant` from `pgrmShortVowel.r`, `pgrmLongVowel.r`, `pgrmDiphthong.r`, etc., verifying each via `foma` before wiring them into `GermanStopShift`.
     - (For diphthongs, we first need to decide whether to declare real multichar symbols—as Burmish does—or to normalize the proto inputs so `{ai}` tokens actually reach `pgrmDiphthong`. Until then, keep the explicit `[ {*ai} | ... ]` list.)
   - Temporarily rewrite `{*k}`→`{K}` at `GermanStopShift`, rerun the six-lexeme stage trace to confirm the contexts match, then switch back to `{*x}` and rerun the analyzer (`printf 'laux…' | flookup german.bin`).
1. **Reintroduce staged saves (temporarily)**
   - Edit `server/fsts/germanic.txt` to re-add the instrumentation block:
     - Definitions: `GermanAfterEw`, `GermanAfterAu`, `GermanAfterLongV`,
       `GermanAfterNasal`, `GermanAfterShift`, `GermanAfterVowelAdj`,
       `GermanAfterCleanup`, `GermanPreSurface`.
     - Compilation commands: `clear stack / regex ... / save stack german_after_*.bin`.
   - Recompile via `docker compose exec backend foma -f fsts/germanic.txt`.
   - If `Stack full!` appears before finishing, temporarily comment out the
     `GermanSurface` portion, compile just the proto→pre-surface cascade, and
     record outputs before re-enabling the surface block.

2. **Log each stage (down direction)**
   - For each stage binary, use `load stack …; apply down …` to capture
     `knewą`, `braudą`, `blōdą`, `tōr`:
     ```bash
     docker compose exec backend bash -lc "cd /usr/app && printf 'load stack german_after_longv.bin\\napply down knewą\\nquit\\n' | foma"
     ```
   - Confirm whether `GermanPreSurface` still emits IPA strings (e.g., `knɪw`).

3. **Test `GermanSurface` in isolation**
   - Take an IPA output from step 2 and feed it directly to the surface filter:
     ```bash
     docker compose exec backend bash -lc "cd /usr/app && printf 'k n i ː\n' | flookup german_surface.bin"
     ```
     (If we don’t have `german_surface.bin`, build a tiny one just for this test.)
   - If the filter rejects valid strings, relax it to accept both brace-wrapped
     tokens and plain IPA (`{k}` or `k`)—without changing the upstream stages.

4. **Decision point**
   - If the filter is the only rejection point, either:
     - Allow mixed alphabet (brace + plain) in `GermanSurface`, or
     - Keep using the helper script (`server/tools/german_surface_prep.py`) and
       adjust the UI/regression harness to wrap strings before filtering.
   - If we still can’t compile the full cascade, prepare for a larger change:
     - Consider splitting the German automaton into smaller files (compile
       `GermanRules` alone, then compose with surface filter via CLI), or
     - Draft an HFST migration plan (identify equivalents of the current rules,
       tooling needed, and expected effort).

Document all findings (DEV_NOTES + docs/germanic_transducer_report.md) so the
next window knows exactly which stage fails and what the recommended fix is.
