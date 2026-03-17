# CAPR Shared Application

This directory contains the shared web application infrastructure used by both Germanic and Burmish pipelines.

## Components

### Backend (`backend/`)

Flask API providing:
- `/new-board` — Load cognate boards from TSV
- `/refish-board` — Re-run cognate detection with updated FST
- `/compare-fst` — Compare old vs new transducer outputs

Key files:
- `server.py` — Flask app entry point
- `compile_lexicon_to_json.py` — TSV → JSON for UI
- `compare_fst.py` — FST comparison logic
- `refish.py` — Cognate re-fishing
- `foma.py` — Python bindings for foma FST library

### Frontend (`frontend/`)

Svelte application providing:
- Cognate board visualization
- FST editor and debugger
- Apply-up/apply-down testing

## Usage

The application runs via Docker. See the root `docker-compose.yml` for configuration.

Files are copied to `server/` for Docker mounting. The actual source of truth is here in `app/`.

## Development

To modify the backend:
1. Edit files in `app/backend/`
2. Copy to `server/` or update Docker mounts
3. Restart Docker

To modify the frontend:
1. Edit files in `app/frontend/` or `cognate-app/`
2. Rebuild with `npm run build`
