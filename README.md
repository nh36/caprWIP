# CAPR: Computer Assisted Proto-language Reconstruction

CAPR is a Dockerized stack (Flask API + Svelte UI + Caddy) for managing
wordlists, cognate boards, and finite-state transducers (FSTs). The project
currently focuses on the Burmish and Germanic pipelines; the Germanic dataset
now tracks four doculects (English, Old English, Dutch, German).


## Quick start (development)
1. From the repo root:
   ```bash
   docker compose up -d
   ```
   - Backend ⇨ `http://127.0.0.1:5001`
   - Frontend ⇨ `http://127.0.0.1:8080`
2. In another terminal, proxy the stack through Caddy:
   ```bash
   caddy run --config Caddyfile.dev
   ```
3. Open `http://localhost:5002`, choose `burmish-aligned-final.tsv` or
   `germanic-aligned-final.tsv`, and load the matching FST from `server/fsts/`.
4. Need the longer checklist (regressions, tear-down, hand-offs)? See
   `docs/runbook.md`.

## Documentation map
- `docs/README.md` – master index for all project docs.
- `SETUP.md` – full installation guide (Docker + manual paths).
- `USAGE.md` – UI walkthrough, including the FST editor workflow.
- `docs/runbook.md` + `docs/regression_checks.md` – operational checklist and
  API smoke-test plan (`server/tools/api_regression.py`).
- `DEV_NOTES.md` – dated hand-offs; add a new section per session.
- `docs/germanic_transducer_report.md` – Germanic FST coverage/status summary
  (with supporting files under `docs/germanic_*`).

### Old English data scaffolding
- `server/tools/add_old_english_rows.py` duplicates every English row into an
  Old English placeholder so the TSV always contains 1:1 coverage.
- `server/tools/fetch_old_english_from_wiktionary.py` hits the Wiktionary API to
  pull Old English lemmas from each English entry and writes
  `server/data/old_english_wiktionary.tsv`. Run it whenever you want a fresh
  scrape of the etymology data (results are cached under `server/tmp/`).
- `server/data/old_english_swadesh.tsv` stores the Wiktionary Swadesh export
  used to seed real Old English forms.
- `server/tools/update_old_english_forms.py` applies the Swadesh mappings to
  the gold-standard TSVs (updating `IPA`, `TOKENS`, `COUNTERPART`, `NOTE`). Run
  it whenever the stage3 export is regenerated.
- `server/tools/validate_old_english_pairs.py` confirms both TSVs still have a
  matching Old English row for every English entry (and reports how many
  placeholders remain).

## Project structure
```
.
├── cognate-app/        # Svelte interface (boards + FST editor)
├── docs/               # Project documentation & planning bundles
├── server/             # Flask API, FSTs, data, regression harness
├── docker-compose.yml  # Development stack (backend + frontend)
├── Caddyfile(.dev)     # Reverse proxy definitions
└── SETUP.md / USAGE.md # Detailed setup & usage notes
```

## Current focus: Old English FST development
The project is actively developing the Proto-Germanic → Old English transducer pipeline.

### Recent achievements
- **31.9% match rate** (120/376 OE lexemes) with systematically bucketed mismatches
- **Empirical discovery**: Heavy-syllable nasal apocope rule (PGmc *-ą deletion after heavy stems)
- **A-restoration fix**: Corrected foma syntax bug causing unconditional fronting
- **Refined diagnostics**: Split 256 mismatches into 20+ specific phenomenon buckets

### Status (as of 2026-02-07)
- Latest reports in `server/docs/debug_snapshots/`:
  - `oe_mismatch_report_2026-02-07_refined_v3.txt` (bucketed mismatches)
  - `oe_full_trace_report_2026-02-07_refined_buckets.txt` (stage-by-stage traces)
- Top mismatch buckets: `final_vowel_missing` (38), `vowel_quality_other` (27), `breaking_extra_other` (22)
- Diagnostic tools: `server/tools/oe_mismatch_report.py`, `server/tools/oe_full_trace_report.py`

### Development workflow
1. Run mismatch/trace reports to identify issues
2. Investigate phonological phenomena in reference sources (Hogg, Ringe/Taylor)
3. Implement/fix FST rules in `server/fsts/germanic.txt`
4. Regenerate reports to verify improvements
5. Document findings in `DEV_NOTES.md`

### Operations
- Keep Docker + Caddy steps documented in `docs/runbook.md`
- Record each session in `DEV_NOTES.md` with regression results

## Citations
- Xun Gong & Nathan Hill (2020). *Materials for an Etymological Dictionary of
  Burmish*. Zenodo. https://doi.org/10.5281/zenodo.4311182
- List, J.-M. & R. Forkel (2022). *LingRex*. Zenodo.
- List, J.-M. & R. Forkel (2021). *LingPy*. https://lingpy.org
- Hulden, M. (2009). “Foma: a finite-state compiler and library.” *EACL*.
