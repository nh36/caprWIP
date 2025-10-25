# Daily Hand-off Notes

Add a new dated section (reverse chronological) each time you pause work.
Include:
- Services you touched (Docker/Caddy, datasets loaded).
- Regression harness status and notable warnings.
- Next tasks or blockers.

For the broader documentation map, see `docs/README.md`.


## 2025-10-25

### Services & tests
- `docker compose up -d` (warning: compose `version` key is obsolete).
- Backend reachable at `http://127.0.0.1:5001`; run Caddy via `docs/runbook.md`
  when the UI is needed.
- German surface-to-proto probe:
  ```bash
  docker compose exec backend sh -c "cd /usr/app && printf 'kniː\nbroːt\nbluːt\ntoːr\n' | flookup german.bin"
  ```
  `kniː`, `broːt`, `bluːt` ⇒ `+?`; `toːr` ⇒ multiple proto outputs (healthy control).

### Next focus
- Instrument each German stage (ProtoWord → surface) to capture intermediate
  forms for `*knewą/*braudą/*blōdą`.
- Revisit non-dental `{au}` reflexes and admit `{x}/{ç}` in `GermanSurface` once
  stage logging confirms the choke point.

### Notes
- Documentation index lives in `docs/README.md`; run instructions in
  `docs/runbook.md`.

## 2025-10-04

### Quick Start Tomorrow
1. Open a fresh terminal window.
2. `cd ~/caprWIP-fresh`
3. Start the services: `docker compose up -d`
   - Rebuild first if desired: `docker compose build`
4. Visit http://localhost:5002 in the browser.
5. Load `burmish-aligned-final.tsv`; the cognate boards and FST editor will then both work.

### Current State
- Latest commits pushed to `update` (most recent: `cd31b59 Interfile glottal-initial board titles`).
- Frontend sorting now trims leading `*`/`?` and interfiles `ʔ`+consonant entries with their plain consonant counterparts; `ʔ`+vowel entries still sort near the end.
- Clean stack: `docker compose up -d` is enough to resume work.

### Tips
- Need to adjust ordering further? Edit `cognate-app/src/App.svelte`, rebuild, and restart.
- To inspect board titles in the UI, open the dev console and check `window.loaded.boards` after loading data.

See you tomorrow!
