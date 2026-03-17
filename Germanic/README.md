# Germanic Pipeline: Proto-Germanic → Old English

This directory contains the active FST development for modeling sound changes from Proto-Germanic to Old English.

## Current Status

**62 mismatches** out of 1057 lexemes (94% accuracy)

## Directory Structure

```
Germanic/
├── data/
│   ├── germanic-aligned-final.tsv    # Main aligned wordlist
│   ├── old_english_swadesh.tsv       # Swadesh list for OE forms
│   └── old_english_wiktionary.tsv    # Wiktionary-sourced OE data
├── fsts/
│   ├── germanic.txt                  # Main FST (all sound changes)
│   └── old_english_sandbox.txt       # Experimental rules
├── tools/
│   ├── oe_mismatch_report.py         # Analyze FST vs target mismatches
│   ├── oe_full_trace_report.py       # Stage-by-stage derivation traces
│   └── ...                           # Various diagnostic tools
└── docs/
    ├── DEV_NOTES.md                  # Research log and decisions
    ├── debug_snapshots/              # Timestamped reports
    └── analysis/                     # Investigation notes
```

## Development Workflow

### 1. Compile FST
```bash
docker compose exec -T backend bash -c "cd /usr/app && foma -q -l fsts/germanic.txt -e quit"
```

### 2. Run mismatch analysis
```bash
docker compose exec -T backend python3 tools/oe_mismatch_report.py
```

### 3. View results
```bash
cat Germanic/docs/debug_snapshots/oe_mismatch_report.txt
```

### 4. Edit rules and iterate
Edit `Germanic/fsts/germanic.txt`, recompile, and check results.

## Key Documentation

- **DEV_NOTES.md** — Detailed research log with source citations
- **debug_snapshots/** — Historical mismatch reports for comparison
- **analysis/** — Deep-dive investigations on specific phenomena

## Sound Change Pipeline

The FST in `germanic.txt` implements these major stages:

1. **Proto-Germanic input** — normalize proto-forms
2. **West Germanic** — gemination, *z > r, etc.
3. **Pre-Old English** — breaking, i-umlaut, palatalization
4. **Old English output** — final orthographic normalization

## References

Key sources used in development (see `docs/references/`):
- Campbell, A. (1959). *Old English Grammar*
- Hogg, R. M. (1992). *Cambridge History of the English Language, Vol. 1*
- Ringe, D. & Taylor, A. (2014). *A Linguistic History of English, Vol. 2*
- Kroonen, G. (2013). *Etymological Dictionary of Proto-Germanic*
