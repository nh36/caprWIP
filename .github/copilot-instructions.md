# CAPR Copilot instructions

## Build, test, and lint commands
- Start the default dev stack from the repo root with `docker compose up -d`, then run `caddy run --config Caddyfile.dev` and use `http://localhost:5002`.
- Frontend commands live in `frontend/`: `npm run dev`, `npm run build`, and `npm run check`.
- The default mounted FST workflow is Germanic: `docker compose exec -T backend bash -lc 'cd /usr/app && foma -q -l fsts/germanic.txt -e quit'`, then `docker compose exec -T backend python3 /usr/app/tools/oe_mismatch_report.py`.
- Python tests currently live under `Germanic/tests`: run the file with `cd Germanic/tests && python3 -m unittest test_english_apply_down_stats`, or a single test with `cd Germanic/tests && python3 -m unittest test_english_apply_down_stats.NormalizeProtoTests.test_strips_markers`.
- Active Germanic publication builds: `python3 Germanic/docs/assembly/build_sound_change_volume.py`, `bash Germanic/docs/assembly/build_sound_change_volume.sh`, `python3 Germanic/docs/sound_changes/reader_facing/check_reader_facing_style.py`, and `bash Germanic/docs/sound_changes/reader_facing/build_reader_facing_pilot_docker.sh`.

## High-level architecture
- CAPR is a shared Flask API in `backend/` plus a Svelte UI in `frontend/`, used by three parallel research pipelines: Germanic, Burmish, and Celtic.
- `docker-compose.yml` mounts Germanic data, FSTs, tools, and docs into `/usr/app` by default, so the running backend operates on Germanic unless those volume mounts are changed.
- `/new-board` calls `compile_to_json_full_cognates()` to ingest TSV rows into board/word/syllable JSON; `data_profiles.py` auto-detects the dataset family and decides how `syllables_parsed` is built.
- `/compare-fst` and `/refish-board` compile Foma text in temporary directories, load doculect bins through the mappings in `compare_fst.py` and `refish.py`, and return correspondence output or reassigned boards; missing bins are surfaced as `missing_transducers`.
- `frontend/src/App.svelte` owns board and FST state and persists both to `localStorage`; `frontend/src/api.ts` prefers `/api` via Caddy but falls back to direct backend ports.

## Key conventions
- Any command that uses `foma` or `flookup`, or Python scripts that shell out to them, should run inside the backend container rather than against a host-local install.
- When compiling `Germanic/fsts/germanic.txt`, always include `-e quit`; the file does not terminate on its own and otherwise leaves `foma` hanging.
- New TSVs are not automatically exposed in the UI: `backend/server.py` allowlists the visible datasets in `list_inputs()`.
- FST filenames and exported network names must match pipeline/doculect expectations: the seed file is `<pipeline>.txt` under `fsts/`, and the exported lowercase transducer names must line up with the mappings in `compare_fst.py` and `refish.py`.
- Germanic is now in write-up/publication mode by default: start with `Germanic/docs/CANONICAL_STATE.md`, and treat the live TSV plus the compact derivation report, lexeme packets, manifest, schema, and coverage audit as authoritative instead of older debug snapshots.
- Reader-facing Germanic sound-change chapters are rule-centered: one `define` per `foma` block, labelled rule sections, page-numbered citations, italicized Old English forms with first-mention single-quoted glosses, and raw LaTeX `\emph{*form}` for reconstructed forms.
