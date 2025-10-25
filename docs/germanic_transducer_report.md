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
