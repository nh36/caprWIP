# Old English FST Pipeline — Quick Reference

## Directory Structure

```
capr-v3-working/
├── Germanic/
│   ├── fsts/              # FST source files (edit these)
│   │   ├── germanic.txt   # Main FST with all sound change rules
│   │   └── old_english_sandbox.txt  # Generates trace bins
│   ├── data/              # Data files
│   │   └── germanic-aligned-final.tsv
│   ├── tools/             # Python analysis scripts
│   │   ├── oe_mismatch_report.py    # Summary of mismatches
│   │   ├── oe_full_trace_report.py  # Step-by-step traces
│   │   └── rebuild_oe_bins.sh       # Compile FSTs in Docker
│   ├── docs/              
│   │   ├── DEV_NOTES.md   # Development log
│   │   └── debug_snapshots/  # Report output
│   └── QUICKREF.md        # This file
├── backend/               # Compiled .bin files go here
│   ├── old_english.bin    # Main OE FST
│   ├── old_english_sandbox_after_*.bin  # Trace bins
│   └── english*.bin       # Other FSTs
├── build/                 # OLD bin location (ignore)
└── docker-compose.yml     # Docker config
```

## Common Tasks

### 1. Compile FSTs (after editing germanic.txt)

```bash
# ALWAYS compile inside Docker, not locally
bash Germanic/tools/rebuild_oe_bins.sh
```

This compiles BOTH `germanic.txt` (main FST) AND `old_english_sandbox.txt` (trace bins).

### 2. Run Mismatch Report

```bash
python3 Germanic/tools/oe_mismatch_report.py
# Output: Germanic/docs/debug_snapshots/oe_mismatch_report.txt
```

Shows all mismatches grouped by type (breaking, umlaut, etc.)

### 3. Run Full Trace Report (STEP-BY-STEP DEBUGGING)

```bash
python3 Germanic/tools/oe_full_trace_report.py
# Output: Germanic/docs/debug_snapshots/oe_full_trace_report.txt
```

Shows EVERY lexeme with output after EVERY rule. Use this to see exactly where things go wrong.

### 4. Test Single Form

```bash
# Inside Docker container:
docker compose exec backend bash
echo "akanaz" | flookup -i old_english.bin

# Or from host (if flookup available):
echo "akanaz" | flookup -i backend/old_english.bin
```

### 5. Git Workflow

```bash
git add -A
git commit -m "fix: description

Co-authored-by: Copilot <223556219+Copilot@users.noreply.github.com>"
git push origin update
```

## Debugging Workflow

1. **Run mismatch report** to see what's wrong
2. **Run trace report** to see where it goes wrong
3. **Find the failing rule** in the trace
4. **Edit germanic.txt** (in `Germanic/fsts/`)
5. **Recompile** with `rebuild_oe_bins.sh`
6. **Re-run reports** to verify fix
7. **Document** in DEV_NOTES.md
8. **Commit**

## Key Files to Edit

| Task | File |
|------|------|
| Add/fix sound change rule | `Germanic/fsts/germanic.txt` |
| Add trace stage | `Germanic/fsts/old_english_sandbox.txt` |
| Fix proto/counterpart data | `Germanic/data/germanic-aligned-final.tsv` |
| Document research | `Germanic/docs/DEV_NOTES.md` |

## Foma Gotchas

1. **Epenthesis with multichar symbols doesn't work**
   - BAD: `0 -> {*e} || {*j} _ {*u}`
   - GOOD: `{*j} {*u} -> {*j} {*e} {*u}`

2. **Parentheses make context OPTIONAL**
   - `(X | Y)` = "optionally X or Y" (can match empty!)
   - `[X | Y]` = "required: X or Y"

3. **Multichar outputs for diphthongs**
   - BAD: `{*e} -> {*eo}`
   - GOOD: `{*e} -> {*e} {*o}`

## Current Status

Run `python3 Germanic/tools/oe_mismatch_report.py` to see current mismatches.
