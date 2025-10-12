# API Regression Harness Plan

We want a lightweight script that sanity-checks the two main pipelines by
driving the existing Flask API. The harness will live alongside the server
code so future FST changes can be verified quickly.

## Scope

- Hit `/new-board` for both `burmish-aligned-final.tsv` and
  `germanic-aligned-final.tsv`.
- Assert that the response includes populated `syllables_parsed`, and that the
  doculect inventory matches the TSV.
- For each pipeline, call `/compare-fst` with a representative pair of
  doculects (e.g., `Atsi`/`Maru` and `English`/`German`) and verify the
  returned `chapters` contain rows.
- Capture `missing_transducers` and surface them in the output so the user
  knows if a language was skipped (e.g., Rangoon in the Burmish set).
- Record the total time and status for each check; exit non-zero if any step
  fails.

## Implementation Notes

- Script location: `server/tools/api_regression.py`.
- Dependencies: `requests` (already in the backend image). Use plain stdout;
  no third-party test runner is required.
- The script assumes the Docker backend is running on `127.0.0.1:5001`. If it
  cannot connect, it should fail quickly with a readable message.
- Provide a `--base-url` option so the harness can target remote deployments
  if needed.

## Usage Story

1. Ensure `docker compose up -d` is running.
2. Execute `python server/tools/api_regression.py`.
3. Review the summary table; any failed assertion prints diagnostic details
   (HTTP status, sample payload, first error encountered).
4. Example output with the current state (Oct 2025):

   ```text
   PASS  burmish (burmish-aligned-final.tsv)
   PASS  germanic (germanic-aligned-final.tsv)

   Completed in 4.1s
   ```

Future extensions could add more doculect combinations or hook into CI, but
the initial goal is a fast manual smoke test for FST tweaks.
