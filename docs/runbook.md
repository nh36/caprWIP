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
   `server/data/`). The Germanic board now exposes four doculects (English,
   Old English, Dutch, German); seeing the extra rows under `Old English` is
   expected.
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

## 6. Old English data upkeep
- After regenerating `germanic-aligned-final.tsv` (stage3), run
  `server/tools/add_old_english_rows.py` if any English rows were added, then
  `server/tools/update_old_english_forms.py server/data/germanic-aligned-final.tsv server/pipeline/output/germanic/stage3/germanic-aligned-final.tsv`
  to reapply the attested Swadesh/Wiktionary forms.
- Periodically refresh the Wiktionary scrape via
  `python3 server/tools/fetch_old_english_from_wiktionary.py 
  server/data/old_english_wiktionary.tsv server/data/germanic-aligned-final.tsv`;
  results are cached, so reruns only hit pages that changed.
- Keep the Swadesh source snapshot in `server/data/old_english_swadesh.tsv`
  up to date (`tmp/old_english_swadesh.html` can be refreshed via
  `curl https://en.wiktionary.org/...` when the list changes).
- Before handing off, run
  `server/tools/validate_old_english_pairs.py server/data/germanic-aligned-final.tsv`
  to ensure every English concept still has an Old English counterpart (this
  script also reports how many placeholder notes remain).
- Tracing tip: the English sandbox now emits `english_after_proto_to_oe.bin` right
  after the PGmc→OE stage, so grab that snapshot when debugging early vowel/weak-tail changes.
- Use `python3 server/tools/evaluate_proto_to_oe.py --tsv data/germanic-aligned-final.tsv --bin english_after_proto_to_oe.bin` after each rule batch to quantify how close the stage mirrors the OE column.
