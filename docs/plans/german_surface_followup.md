# German Surface Follow-up Plan (next window)

## Goal
Recover reliable proto→surface traces for the German FST, then decide whether
to relax the existing `GermanSurface` filter, split the automaton, or migrate the
surface layer to HFST.

## Steps

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
