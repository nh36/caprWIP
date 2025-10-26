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

## Current findings (2025‑10‑25)
- Surface-to-proto tests
  - Command: `docker compose exec backend sh -c "cd /usr/app && printf 'kniː\n'
    | flookup german.bin"`
  - Results: `kniː`, `broːt`, `bluːt` still return `+?` (no proto analyses) while
    `toːr` delivers the expected bundles (multiple `tōr`/`tōrą` variants).
  - Interpretation: the nasal-vowel stems still collapse before the surface
    filter, whereas plain long-vowel sets like *door* survive.
- Stage inspection todo
  - Need to instrument each stage of the German cascade (ProtoWord, ew-chain,
    GermanAuMonophth, GermanLongVowelRules, GermanVowelAdjustments, surface
    filter) and capture the intermediate strings for `*knewą/*braudą/*blōdą`.
  - Add those logs to this report once gathered.

### Instrumentation proposal (before changing rules)
1. **Label intermediate stages** so each block of `GermanRules` can be tested in
   isolation, e.g. conceptual definitions such as:
   ```foma
   define GermanAfterEw ProtoWord .o. GermanEwChain;
   define GermanAfterAu GermanAfterEw .o. GermanAuMonophth;
   define GermanAfterLongV GermanAfterAu .o. GermanLongVowelRules;
   define GermanAfterNasal GermanAfterLongV .o. GermanFinalNasalLoss;
   define GermanAfterShift GermanAfterNasal .o. GermanConsonantShift .o. GermanStopShift;
   define GermanAfterVowelAdj GermanAfterShift .o. GermanVowelAdjustments;
   define GermanAfterCleanup GermanAfterVowelAdj .o. GermanFinalDevoicing .o. GermanCleanup;
   ```
2. **Compile/save each stage** temporarily (`regex GermanAfterLongV; save stack
   german_after_longv.bin`) and run `flookup` for `kniː/broːt/bluːt/tōr` in both
   directions. This reveals the first stage that collapses the nasal-vowel stems.
3. **Record the strings** at each stage inside this report so we know whether to
   adjust the ew-chain, the long-vowel block, or the cleanup/surface filter.
4. **Only after logging** should we touch the actual rule definitions, keeping a
   copy of the staged binaries for regression.

### Stage log snapshot (2025‑10‑26)
- Commands (Proto → stage, true down direction via `foma`):
  ```bash
  docker compose exec backend sh -c \
    "cd /usr/app && printf 'load stack german_after_longv.bin\\napply down knewą\\nquit\\n' | foma"
  ```
- Commands (Surface → stage / analysis):
  ```bash
  docker compose exec backend sh -c \
    "cd /usr/app && printf 'load stack german_after_nasal.bin\\napply up kniː\\nquit\\n' | foma"
  ```
- Findings:
  - `GermanAfterEw` now explicitly glues `{iu}` and adds a fallback `{ew → ī}` rule (`server/fsts/germanic.txt:305-317`), so applying *down* yields `{knewą, kniwą, kniuą, knīą}` as expected.
  - Through `GermanAfterLongV` we obtain `{knewą, kniwą, kniuą, kniːą}`; after `GermanFinalNasalLoss` this becomes `{knew, kniw, kniu, kniː}`.
  - The analyzer (`apply up`) already produced the richer proto sets we saw earlier; the missing reconstructions stem entirely from the final surface filter (`GermanSurface`). `GermanPreSurface` emits `{knɪw, knɛw, kniw, kniɔ, kniː}`, but composing with `GermanSurface` currently rejects all of them, so `load stack german.bin; apply down knewą` still returns `???`.
  - Conclusion: ew→iu→ī chronology is functioning; the real blockage is the surface admissibility layer, which needs to accept the `{knV}` outputs (and eventually `{x}/{ç}` for other sets).

### Rule-design proposals (phonology-aligned; no code yet)
1. **ew→iu→ī chronology** – In West Germanic, `ew` first fronts to `iw/iu` and
   then contracts to long `ī` before nasal vowels (cf. OHG `knī` < PG `*knew-`).
   Our rules currently create the sequence `i u` but expect a multi-symbol `{iu}`;
   proposal: either glue the sequence via a dedicated recombination (`i u -> {iu}`)
   or rewrite the contraction to match the literal `i u`. Ensure nasal deletion
   fires afterward so `knīą` survives to the surface.
2. **Non-dental `{au}` contexts** – Historical pattern: `{au}` only monophthongises
   before coronal obstruents/nasals (`*braudą → brōt`, `*hlaupaną → laufen`).
   Introduce an explicit preservation stage (e.g. `{au} -> {ɔu}` globally, then
   `{ɔu} -> ō / _ {d, ð, t, θ, n}`) so forms like `lauf/Haus` keep `{au}` while
   `broːt`, `bluːt` move toward `{oː}/{uː}`.
3. **Surface inventory `{x}/{ç}`** – High German shift outputs `x` (ach) and `ç`
   (ich) from velars and front contexts (e.g. *Buch*, *suchen*, *Knecht*). Add
   `{ç}` (and any other missing spirants) to `GermanSurfaceConsonant` so valid
   outputs aren’t filtered before we refine the shift rules themselves.
4. **Cluster follow-ups** – Once the above is stable, revisit `{t → ts}` and
   `{k/kk → x}` in shielded contexts plus cluster reflexes like `*stukkaz → ʃtɔk`.

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
1. **ew→iu→ī chronology audit** – ensure the chain outputs `knīą` before nasal
   deletion; confirm long-vowel rules convert `{ī → iː}` without undoing.
2. **Non-dental `{au}` reflexes** – dedicated rule for sequences like `lauf` /
   `Haus` now that final devoicing is in place.
3. **High German consonant shift completion** – finish `{t → ts}` and
   `{k/kk → x}` even with shielding, plus admit `{x}/{ç}` in `GermanSurface` so
   *Buch* / *suchen* stop falling back to `*surface`.
4. **Cluster/geminate reflexes** – e.g. `*stukkaz → ʃtɔk`; depends on the second
   shift and new surface symbols.
5. **Regression + logging** – once the above steps land, re-run
   `server/tools/api_regression.py` and refresh the coverage numbers here.

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
