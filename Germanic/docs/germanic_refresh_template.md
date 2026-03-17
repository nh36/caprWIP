# Germanic Refresh Checklist (template)

Use this template each time we refresh the Germanic planning bundle on the Desktop. Copy it to a dated note (or the daily log) and fill in the blanks as you go.

## Prep
- [ ] Date of refresh: `YYYY-MM-DD`
- [ ] Branch checked out: ``
- [ ] Latest commit hash: ``
- [ ] Confirm no uncommitted work that would be clobbered.

## 1. Archive the previous Desktop snapshot
- Target folder: `~/Desktop/CAPR/expand Germanic FSTs`
- Commands:
  ```bash
  cd ~/Desktop/CAPR/expand\ Germanic\ FSTs
  stamp=$(date '+%Y%m%d_%H%M')
  mkdir "snapshot_${stamp}"
  for f in *; do
      if [ "$f" != "snapshot_${stamp}" ]; then
          mv "$f" "snapshot_${stamp}/"
      fi
  done
  ```
- Notes: ___________________________________________

## 2. Rebuild transducers & run regression harness
- From the repo root:
  ```bash
  cd ~/capr-v3-working
  docker compose up -d backend
  docker compose exec backend python tools/api_regression.py --base-url http://127.0.0.1:5000
  ```
- Expected outcome: both Burmish and Germanic report `PASS`.
- If failures occur, record details here: _______________________________

## 3. Export fresh compare reports
- With the backend running, run the manual Python snippet (see appendix) or your preferred helper script.
- Verify new files appear under `~/Desktop/CAPR/expand Germanic FSTs/compare_*.{json,md,html}`.
- Capture anomalies (e.g., missing reconstructions) here: ____________________

## 4. Update planning documents
- Overwrite / regenerate in `~/Desktop/CAPR/expand Germanic FSTs`:
  - `germanic_fst_todo.md`
  - `Codex new Germanic FST plan.docx`
  - `Prompt to improve Germanic FSTs.docx`
  - `germanic_fsts_<timestamp>.txt`
- Suggested command pattern:
  ```bash
  # After editing Markdown notes
  textutil -convert docx plan_temp.txt -output "Codex new Germanic FST plan.docx"
  textutil -convert docx prompt_temp.txt -output "Prompt to improve Germanic FSTs.docx"
  ```
- Record highlights / key decisions here: _______________________________

## 5. Tear down containers
- Command:
  ```bash
  docker compose down
  ```
- Confirm no stray containers remain.

## 6. Final checks
- [ ] Compare diff of `~/Desktop/CAPR/expand Germanic FSTs` to ensure only intended files changed.
- [ ] Update repo docs (`docs/germanic_transducer_report.md`) if priorities shifted.
- [ ] Log outstanding issues (e.g., `knee` still missing) in `germanic_fst_todo.md`.

## Appendix – Manual export snippet
Use this Python block to regenerate the compare files when no helper script is available:
```python
import json
from pathlib import Path
import requests

BASE = 'http://127.0.0.1:5001'
TARGET = Path('~/Desktop/CAPR/expand Germanic FSTs').expanduser()
TARGET.mkdir(parents=True, exist_ok=True)

board = requests.post(f'{BASE}/new-board', json={"dataPath": "germanic-aligned-final.tsv", "transducer": "internal"}).json()
trans = requests.post(f'{BASE}/get-transducers', json={"name": "germanic.txt"}).json()['transducer']

pairs = [("English", "German"), ("English", "Dutch"), ("German", "Dutch")]

# paste the latest export loop here
```

Keep the full export loop alongside this template (e.g., in `docs/scripts/`) so the commands stay in sync with how we actually generate the snapshot.
