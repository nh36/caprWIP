# Daily Hand-off Notes (2025-10-04)

## Quick Start Tomorrow
1. Open a fresh terminal window.
2. `cd ~/caprWIP-fresh`
3. Start the services: `docker compose up -d`
   - Rebuild first if desired: `docker compose build`
4. Visit http://localhost:5002 in the browser.
5. Load `burmish-aligned-final.tsv`; the cognate boards and FST editor will then both work.

## Current State
- Latest commits pushed to `update` (most recent: `cd31b59 Interfile glottal-initial board titles`).
- Frontend sorting now trims leading `*`/`?` and interfiles `ʔ`+consonant entries with their plain consonant counterparts; `ʔ`+vowel entries still sort near the end.
- Clean stack: `docker compose up -d` is enough to resume work.

## Tips
- Need to adjust ordering further? Edit `cognate-app/src/App.svelte`, rebuild, and restart.
- To inspect board titles in the UI, open the dev console and check `window.loaded.boards` after loading data.

See you tomorrow!
