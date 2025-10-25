# CAPR Runbook

Use this checklist when you need to bring the stack up, exercise the UI/FST
editor, and capture a regression snapshot. Combine it with the deeper guidance
in `SETUP.md` / `USAGE.md` as needed.

## 1. Start services
1. From the repo root, ensure Docker is available, then run:
   ```bash
   docker compose up -d
   ```
   - Expect backend on `http://127.0.0.1:5001` and frontend on `http://127.0.0.1:8080`.
   - Docker warns about the legacy `version` key in `docker-compose.yml`; this is
     cosmetic for now.
2. Launch Caddy in a second terminal to stitch the API + UI together:
   ```bash
   caddy run --config Caddyfile.dev
   ```
   - Default proxy port is `:5002`; adjust the first line in `Caddyfile.dev` if
     the port is taken.

## 2. Load data in the UI
1. Visit `http://localhost:5002`.
2. Use the “Available input sources” dropdown to select
   `burmish-aligned-final.tsv` or `germanic-aligned-final.tsv` (files live under
   `server/data/`).
3. If you expect boards immediately, confirm a matching FST text file exists in
   `server/fsts/` (e.g., `germanic.txt`).
4. When starting from a blank FST, flip to the FST editor tab *before* pressing
   “Load” to avoid the broken board view (see `USAGE.md`).

## 3. Run the regression harness
1. Keep the Docker backend running.
2. Execute the smoke test script:
   ```bash
   python server/tools/api_regression.py
   ```
   - Uses `http://127.0.0.1:5001` by default; pass `--base-url` if the backend
     is elsewhere.
   - Verifies `/new-board` and `/compare-fst` for Burmish & Germanic; failures
     print diagnostics per pipeline (design documented in
     `docs/regression_checks.md`).
3. Capture the PASS/FAIL summary in your hand-off notes when relevant.

## 4. Record work / hand off
1. Update `DEV_NOTES.md` (add a dated section) with:
   - Which dataset + transducers you loaded.
   - Notable warnings (e.g., Docker compose “version” warning).
   - Outstanding tests or forms to revisit next session.
2. If you touched the Germanic FSTs, also update the status bullets in
   `docs/germanic_transducer_report.md` and, if needed, the desktop refresh
   template.

## 5. Tear down
When finished, shut the stack down so fresh sessions start cleanly:
```bash
caddy stop # or Ctrl+C the running Caddy process
cd /path/to/capr-v3-working
docker compose down
```
Check `docker compose ps` to confirm no lingering containers remain.
