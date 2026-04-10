# CAPR: Computer Assisted Proto-language Reconstruction

CAPR is a Dockerized toolkit for comparative linguistics, combining:
- **Cognate board management** — track cognate sets across related languages
- **FST development** — build and test finite-state transducers for sound change modeling
- **Web interface** — Svelte UI for data exploration and FST debugging

## Project Components

This repository contains **three parallel research pipelines** sharing common infrastructure:

| Component | Description | Status |
|-----------|-------------|--------|
| **[Germanic/](Germanic/)** | Proto-Germanic → Old English sound changes | Active development (62 of 1057 rows mismatched) |
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
capr-v3-working/
├── Germanic/               # Proto-Germanic → OE pipeline
│   ├── data/               # TSV wordlists (germanic-aligned-final.tsv)
│   ├── fsts/               # FST sources (germanic.txt)
│   ├── tools/              # Python analysis tools
│   └── docs/               # DEV_NOTES.md, debug snapshots
├── Burmish/                # Proto-Burmish pipeline
│   ├── data/               # Burmish wordlists
│   ├── fsts/               # burmish.txt
│   └── ...
├── Celtic/                 # Proto-Celtic pipeline
│   ├── data/               # celtic-aligned-final.tsv
│   └── fsts/               # celtic.txt + compiled .bin per daughter language
├── app/                    # Shared web application
│   ├── backend/            # Flask API (compare_fst.py, refish.py, etc.)
│   └── frontend/           # Svelte cognate board UI
├── server/                 # Docker working directory (code copied here)
├── cognate-app/            # Svelte source (mirrored in app/frontend/)
├── docs/                   # Shared documentation
│   ├── references/         # Scholarly sources (PDFs, text extracts)
│   ├── runbook.md          # Operational checklist
│   └── README.md           # Documentation index
├── build/                  # Compiled .bin files (gitignored)
├── docker-compose.yml      # Development stack
└── Caddyfile.dev           # Reverse proxy config
```

## Germanic Pipeline

The active focus is modeling Proto-Germanic → Old English sound changes via FST rules.

**Current status:** 62 mismatches out of 1057 lexemes (94% accuracy)

Key files:
- `Germanic/fsts/germanic.txt` — Main FST with all sound change rules
- `Germanic/data/germanic-aligned-final.tsv` — Aligned proto-forms and OE targets
- `Germanic/docs/DEV_NOTES.md` — Detailed research log and phonological decisions

**Development workflow:**
```bash
# Compile FST and check results
docker compose exec -T backend bash -c "cd /usr/app && foma -q -l fsts/germanic.txt -e quit"

# Run mismatch analysis
docker compose exec -T backend python3 tools/oe_mismatch_report.py
```

See [Germanic/README.md](Germanic/README.md) for detailed documentation.

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
  - ./server:/usr/app
  - ./Celtic/data:/usr/app/data
  - ./Celtic/fsts:/usr/app/fsts
```

See [Celtic/README.md](Celtic/README.md) for full documentation.

## Documentation

- [docs/README.md](docs/README.md) — Documentation index
- [SETUP.md](SETUP.md) — Full installation guide
- [USAGE.md](USAGE.md) — UI walkthrough
- [docs/runbook.md](docs/runbook.md) — Operational checklist
- [WORKFLOW.md](WORKFLOW.md) — Development workflow

## Citations

- Xun Gong & Nathan Hill (2020). *Materials for an Etymological Dictionary of Burmish*. Zenodo. https://doi.org/10.5281/zenodo.4311182
- List, J.-M. & R. Forkel (2022). *LingRex*. Zenodo.
- Hulden, M. (2009). "Foma: a finite-state compiler and library." *EACL*.
