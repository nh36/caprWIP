# CAPR: Computer Assisted Proto-language Reconstruction

CAPR is a Dockerized toolkit for comparative linguistics, combining:
- **Cognate board management** — track cognate sets across related languages
- **FST development** — build and test finite-state transducers for sound change modeling
- **Web interface** — Svelte UI for data exploration and FST debugging

## Project Components

This repository contains **three parallel research pipelines** sharing common infrastructure:

| Component | Description | Status |
|-----------|-------------|--------|
| **[Germanic/](Germanic/)** | Proto-Germanic → Old English sound changes | Active research; [current state](Germanic/docs/CURRENT_STATE.md) owns the phase and protected-baseline pointers. |
| **[Burmish/](Burmish/)** | Proto-Burmish reconstruction | Maintenance mode |
| **[Celtic/](Celtic/)** | Proto-Celtic → daughter languages (Old/Middle Irish, Welsh, Breton, Cornish, Gaulish, Celtiberian) | Early development |

All three use the same web application and FST tooling but have independent data, transducers, and documentation.

## Quick Start

```bash
# Start the Docker stack (Flask API + Svelte UI)
docker compose up -d

# In another terminal, proxy through Caddy
caddy run --config Caddyfile.dev

# Open http://localhost:5002
```

The Docker stack mounts **Germanic/** by default. To switch to Burmish, edit `docker-compose.yml` to mount `Burmish/` paths instead.

## Repository Structure

```
capr/
├── Germanic/               # Proto-Germanic → OE pipeline
│   ├── data/               # TSV wordlists (germanic-aligned-final.tsv)
│   ├── fsts/               # FST sources (germanic.txt)
│   ├── tools/              # Python analysis tools
│   └── docs/               # Task routing, SOURCE, publications and archives
├── Burmish/                # Proto-Burmish pipeline
│   ├── data/               # Burmish wordlists
│   ├── fsts/               # burmish.txt
│   └── ...
├── Celtic/                 # Proto-Celtic pipeline
│   ├── data/               # celtic-aligned-final.tsv
│   └── fsts/               # celtic.txt + compiled .bin per daughter language
├── backend/                # Shared Flask API (compare_fst.py, refish.py)
├── frontend/               # Shared Svelte cognate board UI
├── docs/                   # Shared documentation
│   ├── references/         # Holding metadata and provisioned private sources
│   ├── runbook.md          # Operational checklist
│   └── README.md           # Documentation index
├── .capr-work/             # Ignored local evidence and retained linked worktrees
├── docker-compose.yml      # Development stack
└── Caddyfile.dev           # Reverse proxy config
```

## Germanic Pipeline

The active focus is modeling Proto-Germanic → Old English sound changes via FST rules.

**Current status:** sequential per-SC adjudication with separately instructed
scoped work; [Germanic/docs/CURRENT_STATE.md](Germanic/docs/CURRENT_STATE.md)
owns the phase, commands and protected-baseline pointers; it is not a declaration
that research is complete. [Germanic/docs/README.md](Germanic/docs/README.md)
defines the SOURCE/GENERATED/ARCHIVE hierarchy. The
[generated population summary](Germanic/docs/lexeme_reports/pgmc_integration/population_summary.md)
owns the distinct runnable, audit and editorial populations; this landing page
does not maintain another set of counts.

Key files:
- `Germanic/fsts/germanic.txt` — Main FST with all sound change rules
- `Germanic/data/germanic-aligned-final.tsv` — Aligned proto-forms and OE targets
- `Germanic/docs/README.md` — Task routing and current authority
- `Germanic/docs/archive/DEV_NOTES.md` — Historical research log, not current authority

**Development workflow:**
```bash
# Read-only scientific preparation
python3 Germanic/tools/adjudicate.py SCNNN --prepare

# After authorized SOURCE edits, propagate through the sole artifact graph
python3 Germanic/tools/adjudicate.py --refresh
```

Use [Germanic task routing](Germanic/docs/README.md) before scientific work;
the controller owns container execution and generated-output propagation.

## Burmish Pipeline

Proto-Burmish reconstruction using LingPy/LingRex for cognate detection.

See [Burmish/README.md](Burmish/README.md) for documentation.

## Celtic Pipeline

Proto-Celtic FST-based sound change modeling covering Old/Middle Irish, Welsh, Breton, Cornish, Gaulish, and Celtiberian.

Key files:
- `Celtic/fsts/celtic.txt` — Main FST mapping Proto-Celtic to all daughter languages
- `Celtic/data/celtic-aligned-final.tsv` — Aligned proto-forms and daughter reflexes

**Development workflow:**
```bash
# Compile FST
docker compose exec -T backend bash -c "cd /usr/app && foma -q -l fsts/celtic.txt -e quit"
```

To use Celtic data in the UI, mount Celtic paths in `docker-compose.yml`:
```yaml
volumes:
  - ./backend:/usr/app
  - ./Celtic/data:/usr/app/data
  - ./Celtic/fsts:/usr/app/fsts
```

See [Celtic/README.md](Celtic/README.md) for full documentation.

## Documentation

- [docs/README.md](docs/README.md) — Documentation index
- [docs/SETUP.md](docs/SETUP.md) — Full installation guide
- [docs/USAGE.md](docs/USAGE.md) — UI walkthrough
- [docs/runbook.md](docs/runbook.md) — Operational checklist
- [Germanic/docs/README.md](Germanic/docs/README.md) — Scientific task routing
- [docs/CI_VALIDATION.md](docs/CI_VALIDATION.md) — Portable versus strict validation

## Citations

- Xun Gong & Nathan Hill (2020). *Materials for an Etymological Dictionary of Burmish*. Zenodo. https://doi.org/10.5281/zenodo.4311182
- List, J.-M. & R. Forkel (2022). *LingRex*. Zenodo.
- Hulden, M. (2009). "Foma: a finite-state compiler and library." *EACL*.
