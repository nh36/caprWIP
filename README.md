# CAPR: Computer Assisted Proto-language Reconstruction

CAPR is a Dockerized stack (Flask API + Svelte UI + Caddy) for managing
wordlists, cognate boards, and finite-state transducers (FSTs). The project
currently focuses on the Burmish and Germanic pipelines.


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

## Active workstreams
### Germanic FST refresh
- Goal: German `kniː/broːt/bluːt` and cognate sets such as *year/fell/neck* must
  reconstruct without overrides. The ew→iu→ī chain, short-a umlaut, and second
  consonant shift are partially implemented.
- Current focus: the brace-first rewrite is complete for the German cascade;
  English and Dutch still emit plain tokens downstream of their sound laws.
- Next actions:
  1. Refine the proto templates (`ProtoWord`, `pgrmWord`) so final nasal vowels
     behave cleanly as weak syllables without spawning duplicate outputs.
  2. Convert the English and Dutch pipelines to the `{*…}` alphabet (sound laws,
     orthography, and a single star-drop at the end), mirroring the German and
     Burmish placements.
  3. Rebuild the English/Dutch/German surface filters so they accept brace
     tokens and smoke-test the UI to confirm the `{*…}` alphabet flows end-to-end.
  Track detailed progress in `docs/germanic_transducer_report.md`.

### Operations
- Keep Docker + Caddy steps documented in `docs/runbook.md`, and record each
  session in `DEV_NOTES.md` (include regression harness results and warnings).

## Citations
- Xun Gong & Nathan Hill (2020). *Materials for an Etymological Dictionary of
  Burmish*. Zenodo. https://doi.org/10.5281/zenodo.4311182
- List, J.-M. & R. Forkel (2022). *LingRex*. Zenodo.
- List, J.-M. & R. Forkel (2021). *LingPy*. https://lingpy.org
- Hulden, M. (2009). “Foma: a finite-state compiler and library.” *EACL*.
