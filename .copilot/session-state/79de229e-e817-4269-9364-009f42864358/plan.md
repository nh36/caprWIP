# Plan: Phonology Improvement Using Mechanistic Buckets

## Current Status (Checkpoint 016)

**Branch:** `update`, HEAD at `a12b689` (3 uncommitted changes pending)
**Baseline (last commit):** 218 mismatches, 152 exact matches, 0 branching
**With uncommitted changes (tested):** 216 mismatches, 154 exact matches, 0 ProtoToOE branching
- BUT: 6 items have Surface-stage branching from xs/hs orthography overlap (fix implemented but untested)

## Committed work this session (cycles 5-7)

1. `e1bd17e`: OE orthography `*xs → x` — 222→219 mismatches, 148→151 exact
2. `435bfab`: Intervocalic `*j` vocalization — 219→219, palatal_extra__j_triggered 7→1
3. `a12b689`: Back mutation diphthongs (R/T §6.9.4) — 219→218, 151→152

## Uncommitted changes (NEED TESTING)

### A) Input grammar expansion (pgrmWord)
**File:** `server/fsts/germanic.txt`
- Added onsets to `pgrmOnsetCore`: `sm`, `sn`, `xn` (hn-)
- Added weak tail patterns to `pgrmWeakTailVowel`: `enăz`, `erăz`, `ilăz`, `inăz`, `ukăz`
- **Result:** no_output bucket 13→5
- **Remaining 5 no_output:** compound words (`*regna-bugōn`, `*wira-aldiz`), slash forms (`*wurmaz/wurmiz`), complex coda (`*funxwstiz`), missing causative pattern (`*sturtijăną`)

### B) xs/hs branching fix
**File:** `server/fsts/germanic.txt`
- Created `OEXsMerge` define: `{*x} {*s} -> {*xs}` (separate from OldEnglishOrthography)
- Added `{*xs} -> x` to `OldEnglishRemoveStars`
- Added `OEXsMerge` to pipeline before `OldEnglishOrthography`
- Reverted `{x} -> h` back to simple (no context restriction needed)
- **Purpose:** Eliminates branching where `{*x}{*s}` could be processed as either `x` (via multi-symbol rule) or `h`+`s` (via single-symbol `{*x}->h` rule)
- **STATUS: NOT YET TESTED** — terminal died before rebuild

## What to do when resuming

### Immediate (test + commit)
- [ ] Rebuild FSTs: `docker compose exec backend sh -lc 'cd /usr/app && foma -f fsts/germanic.txt'`
- [ ] Rebuild sandbox: `docker compose exec backend sh -lc 'cd /usr/app && foma -f fsts/old_english_sandbox.txt'`
- [ ] Test xs words: `echo "fuxsăz" | flookup -i old_english.bin` — expect `fox` (single output, no branching)
- [ ] Test basic words still work: `echo "dagăz" | flookup -i old_english.bin` — expect `dæġ`
- [ ] Run mismatch report: expect ≤216
- [ ] Run trace report: expect 0 branching in ProtoToOE AND Surface
- [ ] If good: commit with message "Expand input grammar and fix xs/hs orthography branching"
- [ ] Push

### If xs fix doesn't work
- The issue is that foma parallel replacement (comma-separated rules) creates branches when rules overlap
- The `OEXsMerge` approach separates `{*x}{*s}->` into its own composition stage, running BEFORE `OldEnglishOrthography`
- After `OEXsMerge`, the `{*x}{*s}` pair becomes `{*xs}` (single symbol), which `{*x}->h` in orthography can't match
- If this still branches, try: make `OEXsMerge` produce a completely unique symbol (e.g., `{KS}`) and add `{KS} -> x` to RemoveStars

### Continue phonology improvement cycles
Pick next target bucket from current standings (216 total):
- breaking_extra_other: 30 (mostly WS vs Anglian data issues)
- final_vowel_missing__morph_form_mismatch: 27 (data alignment)
- vowel_quality_other: 25 (mixed)
- infl_suffix_extra__an: 18 (data alignment)
- fronting_missing_no_trigger: 7 (a-restoration chronology)
- long_vowel_missing: 7
- final_vowel_missing__weak_noun_like: 9
- final_n_missing__expected_an: 6
- final_vowel_extra: 6
- palatalization_missing: 5
- no_output: 5 (mostly unfixable compound/complex forms)

## Important technical notes

### flookup direction
- `flookup` default = apply UP (lower→upper)
- `flookup -i` = apply DOWN (upper→lower) — THIS IS WHAT WE WANT
- The mismatch report correctly uses `flookup -i` with proto forms stripped of `*`
- When testing manually: always use `echo "dagăz" | flookup -i old_english.bin` (with -i, without *)

### foma parallel replacement branching
- Comma-separated rules in a single `define` create alternatives, not priority
- `{*x} {*s} -> x, {*x} -> h` means BOTH can fire on `{*x}{*s}`, creating branches
- Fix: separate overlapping rules into different composition stages
- The `OEXsMerge` approach runs `{*x}{*s}->` BEFORE the stage that has `{*x}->h`

### Container-only rule
All foma/flookup commands MUST run via `docker compose exec backend sh -lc 'cd /usr/app && ...'`

### Build commands
- `foma -f fsts/germanic.txt` — main FST (~60-90s)
- `foma -f fsts/old_english_sandbox.txt` — sandbox trace FSTs (~60-90s)
- `python3 tools/oe_mismatch_report.py --examples 30` — mismatch report
- `python3 tools/oe_full_trace_report.py --bin-dir /usr/app` — full trace + branching check (~3-4 min)
