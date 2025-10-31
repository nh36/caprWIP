# Germanic Transducer Status — October 2025

This document tracks the Proto-Germanic ⇄ English/Dutch/German FST work. For
operational steps (running Docker, regression harness, desktop refresh), see the
root `README.md`, `docs/runbook.md`, and `docs/germanic_refresh_template.md`.

## Coverage snapshot
| Language | Tokens | With reconstruction | Share | Mean reconstructions/token |
| --- | ---: | ---: | ---: | ---: |
| Dutch | 340 | 24 | 7.1% | 2.00 |
| English | 376 | 39 | 10.4% | 1.87 |
| German | 376 | 11 | 2.9% | 7.91 |

Intersections (Oct 2025 export):
- English ∩ Dutch: 5
- English ∩ German: 2
- Dutch ∩ German: 0
- All three languages: 0

## Key effects delivered so far
- Removed the literal `k → "ch"` rule so phonology stays in IPA.
- Introduced shielded spirantisation (`kk → K`, `k → x/ç`, `K → k`) to model the
  ach/ich split while preserving geminate-derived stops.
- Added English and Dutch initial cluster mapping (`kn-/gn- → n-`) with backward
  restoration so forms like *knight* and *gnaw* still project `*kn-/gn-*`.
- Added English short vowel + diphthong outputs (`e/o → ɛ/ɔ`, `{ai/au} →
  {aɪ/aʊ}`) plus Dutch/German `{e → ɛ}` lowerings; basic sets like *cow*, *meal*,
  *mood*, *fell*, *neck*, *net* no longer need manual overrides (2025‑10‑18).
- Added nominative `*-z` apocope and staged German rules (ew-chain, au
  monophthongisation, final devoicing, shielded stop shift) so `kuː` can reach
  `*kōwz` again.

## Current findings (2025‑10‑31)
- Analyzer probes
  - Command: `docker compose exec backend sh -c "cd /usr/app && printf 'kniː\nbluːt\nbroːt\ndɔr\n' | flookup german.bin"`
  - Results: `kniː` returns `wąknī/ąknī/kąnī/knąī`; `bluːt` yields `blaut/blōwt/blōt/blūt`; `broːt` now maps to `braut`; `dɔr` continues to surface from the full proto bundle.
  - Interpretation: the new `{*au → *ō}` clause keeps `{braudą}` alive through `GermanAfterLongV`, restoring analyzer coverage for `broːt` while leaving other probes unaffected.
- Proto word filter sanity pass (2025‑10‑31)
  - `pgrmOnsetCore` pared down to the usual singletons, s-clusters, and stop+liquid combinations; stray patterns such as `{*n}{*x}{*w}{*s}{*t}` were removed.
  - Nasal vowels are split out of `pgrmShortVowel` and now only pass in genuinely open finals (`apply down nę` ⇒ `*n*ę`, `apply down nęz` ⇒ `???`).
  - Recompiled `fsts/germanic.txt`, reran the analyzer probes, and confirmed the API regression harness stays green.
- Stage logging recap
  - Baseline command: `bash server/tools/log_german_stages.sh > /tmp/german_stage_log.txt` (run after recompiling with `foma -f fsts/germanic.txt`).
  - `GermanAfterAu` feeds `{braudą, brōdą}` into the new rule; `GermanAfterLongV` now outputs `{brūdą}` for that lexeme instead of failing.
  - `GermanPreSurface` supplies `{brūd, brōd}` pairs alongside the existing ew-chain outputs (`knɪw/knɛw/…`), confirming the fix propagates to the surface layer.
  - `GermanReflexes` still inverts `*durą` to `dɔrą`, so consonant-shift handling remains consistent.

### Immediate priorities
1. **Audit remaining German surface inventory** – The current fix only touches long vowels; next pass should confirm `{au}` contexts outside the coronal environment still hold.
2. **Regression loop** – Continue running `server/tools/log_german_stages.sh` and `python server/tools/api_regression.py` whenever further rules change.

### Next surface-filter refresh
1. Extract a complete consonant/vowel inventory from `GermanPreSurface` outputs (or stage 3 TSVs) so we know exactly which tokens the analyzer emits (`pf/ts/ç/x`, `{ɔy}`, `{ɔː}`, etc.).
2. Rebuild `GermanSurfaceVowel/Consonant` in the brace alphabet, populating them from that inventory and keeping the permissive “≤3 consonants” structure for now.
3. Recompile and rerun the stage logger plus `python3 server/tools/api_regression.py` to verify the brace-aware filter behaves as expected.

### Verification commands (2025‑10‑31)
```bash
docker compose exec backend sh -lc "cd /usr/app && printf 'kniː\nbluːt\nbroːt\ndɔr\n' | flookup german.bin"
docker compose exec backend sh -lc "cd /usr/app && printf 'load stack german_after_longv.bin\napply down braudą\nquit\n' | foma"
docker compose exec backend sh -lc "cd /usr/app && printf 'load stack german_pre_surface.bin\napply down durą\nquit\n' | foma"
docker compose exec backend sh -lc "cd /usr/app && printf 'load stack german.bin\napply up dɔr\nquit\n' | foma"
```

### Helper script for surface prep
- File: `server/tools/german_surface_prep.py`.
- Purpose: split cluster sequences (`kn-, br-, pf-`, etc.) and wrap each IPA
  segment in the curly-brace alphabet that `GermanSurface` expects, without
  bloating the main FST.
- Usage example:
  ```bash
  printf 'kniː\nbroːt\n' | python3 server/tools/german_surface_prep.py
  ```
- Workflow: take the `GermanPreSurface` outputs you get from `foma` (e.g.,
  `knɪw`, `knɛw`, `kniː`), run them through the script, then feed the result into
  the UI or any downstream tooling that currently requires brace-wrapped tokens.
- Why a script? Each attempt to bake the prep stage directly into
  `server/fsts/germanic.txt` hit Foma's `Stack full!` limit; keeping it as a
  stand-alone helper lets us keep debugging immediately while we consider
  alternatives (e.g., splitting the Germanic transducer across files or moving
  this part of the pipeline to HFST, which handles larger automata gracefully).

## Active work items
1. Sweep remaining `{au}` contexts (outside coronal environments) to confirm the new rule doesn’t over-apply; add spot checks for forms like `*hlaupaną`.
2. Keep the regression harness + stage logger in the loop for any follow-up tweaks.

## Supporting artifacts
- `docs/germanic_notes/README.md` – links to the October 2025 Word files.
- `docs/germanic_refresh_template.md` – desktop/export checklist; update after
  any major Germanic push.

## Historical session notes
- 2025‑10‑18: ProtoWord now allows chained coda tokens; German `kuː → *kōwz`
  again. Reordered long-vowel chronology ahead of the consonant shift.
- 2025‑10‑19: Added `ew` chain split (`e→i/_w`, `w→u/i_`, `iu→ī/_(a|ą)`) and
  German `{au} → ō / _ {d, ð, t, θ, n}` stage, plus folded base consonant
  devoicing into `GermanConsonantShift`.
- 2025‑10‑25: Confirmed via `flookup german.bin` that knee/bread/blood still
  lack proto analyses; door remains healthy. Next instrumentation pass will log
  each composition step.
