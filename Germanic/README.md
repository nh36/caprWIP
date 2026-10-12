# Germanic Pipeline: Proto-Germanic → Old English

This directory contains the active FST development for modeling sound changes from Proto-Germanic to Old English.

## Current Status

Current phase and commands are maintained in [docs/CURRENT_STATE.md](docs/CURRENT_STATE.md):
sequential per-SC adjudication with separately instructed scoped work.
The 2026-04-30 research-completion statement is a historical checkpoint,
not the current programme status.

The selected baseline has **7 documented mismatches out of 387 runnable OE rows**
(**98.2% accuracy**); see `docs/sound_changes/cascade_baseline/cascade_baseline_summary.json`.
This output count does not declare historical research complete. The immutable
original-380 archive and the active migrated subset are distinct; their
fingerprints are recorded in `docs/CURRENT_STATE.md`.
Corpus maturation has since added *who* (OE *hwā*) and *you* (OE *ēow*) as
witnesses for the final-*z* and apocope chronology, *thought* (OE *þōhte*)
for the nasal-spirant law, and *hue* (OE *hīew*) as the *iwj* witness for
West Germanic gemination of *w before *j.

For the SOURCE/GENERATED/ARCHIVE hierarchy, see [docs/README.md](docs/README.md).
Lexical publication currently distinguishes **387 runnable derivation write-ups**,
**393 reconstruction-audit records**, and **160 elaborated assembled model entries**;
the [generated population summary](docs/lexeme_reports/pgmc_integration/population_summary.md)
owns current assembly/selection counts. `docs/archive/CANONICAL_STATE.md` is historical.

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

## Historical sound-change workflow

The commands below record the earlier diagnostic workflow. For current work,
use `docs/CURRENT_STATE.md` and the adjudication interface, not this historical
sequence. Lexical writing uses the live TSV, compact derivation report,
`docs/lexeme_reports/report_schema.md`, manifest, coverage audit and the
generated integration population crosswalk.

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

## TSV Column Conventions

The main data file `germanic-aligned-final.tsv` uses these key columns:

| Column | Purpose |
|--------|---------|
| **PROTOFORM** | The specific morphological form used as FST input (e.g., dat.sg. \*kūi for cȳ) |
| **PROTO** | The cognate-set citation form / dictionary headword (e.g., nom.sg. \*kōz) |
| **COUNTERPART** | The target Old English form |
| **NOTE** | Scholarly notes with citations (Kroonen, R/T, Campbell, etc.) |
| **HISTORY** | Project history: Wiktionary sources, TSV fixes, internal refs |

**PROTOFORM vs PROTO:** These columns diverge when we use a paradigm-cell form
(gen.sg., dat.sg., 3sg pres.) for the FST because the citation form doesn't yield
the attested OE form by regular sound change. For example:
- OE **cȳ** 'cow (dat.sg.)': PROTOFORM=\*kūi (dat.sg.), PROTO=\*kōz (nom.sg.)
- OE **lifeþ** '(he) lives': PROTOFORM=\*libēθi (3sg), PROTO=\*libēną (infinitive)

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
