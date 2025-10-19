# CAPR: Computer Assisted Proto-language Reconstruction

This repository holds the re-write and working implementation of the interface and code for reconstructing Proto-Burmese, as found here:

> Xun Gong, & Nathan Hill. (2020). Materials for an Etymological Dictionary of Burmish. Zenodo. https://doi.org/10.5281/zenodo.4311182

To run while developing (with Python 3), follow these steps:
(Untested on Windows, works fine on Mac and Linux)

```
docker-compose up --build
```

Open a new terminal, then run Caddy to connect the interface and API.
```
caddy run --config Caddyfile.dev
# opens interface at specified port (5002 by default)
```

## Important Notes

For much more in-depth instructions, see [SETUP.md](https://github.com/knightss27/capr/blob/update/SETUP.md).

For usage instructions, see [USAGE.md](https://github.com/knightss27/capr/blob/update/USAGE.md).

### Germanic FST caveat

- The recent ProtoWord template update landed safely, but a lingering issue remains for the Germanic "year" set: English `jɪər` and Dutch/German `jaːr` currently reconstruct cleanly only when we add a direct override.
- We intentionally reverted that stop-gap override for now; the better fix is to adjust the English rules so that the sequence `an` only deletes at absolute word end, preventing runaway deletion while keeping `*jēran` reachable.
- Pick this thread up in the next session before making further Germanic QA changes.
- 2025-10-18 update: English short mid vowels and `{ai/au}` now reach `{ɛ/ɔ}` and `{aɪ/aʊ}` without overrides, but German/Dutch still need complementary rules so cognate sets like *fell*, *neck*, *net* resurface.
- 2025-10-18 session recap: experiments with a multi-token `ProtoCoda` and reordered long-vowel chronology let German `kuː` recover `*kōwz`, but knee/neck/net/nest/knight still fail without the missing WGmc `ew→iu→ī` development, short-a umlaut, and second-shift affrication.
- Open items: (1) model the PG `ew` pathway through West Germanic `iu` to reach German `iː`; (2) finish the High German consonant shift for `k/t` clusters plus the accompanying umlaut; (3) admit `{x}/{ç}` in the German surface inventory so forms like `Buch`/`suchen` reconstruct instead of falling back to `*surface`.

## Project Structure
```
.
├── cognate-app/
│   └── [svelte code for cognate reassignment and fst editor]
├── orthoprofiles/ *deprecated*
│   └── [orthographical profiles for pipeline stages]
├── pipeline/
│   └── [wordlist to tokenized lexicon, ran through lexstat to find intial cognates]
├── reconstruct/ *deprecated*
│   └── [intial fsts for pipeline usage]
└── server/
    └── [all api routes and associated functions]
```

You can read more about each individual folder in their respective READMEs.

## Citations

> List, J.-M. and R. Forkel (2022): LingRex: Linguistic Reconstruction with LingPy. [Computer software, Version 1.2.0]. Geneva: Zenodo. DOI: 10.5281/zenodo.1544943


> List, J.-M. and R. Forkel (2021): LingPy. A Python library for quantitative tasks in historical linguistics. Version 2.6.9. Max Planck Institute for Evolutionary Anthropology: Leipzig. https://lingpy.org


> Hulden, M. (2009). Foma: a finite-state compiler and library. In Proceedings of the 12th Conference of the European Chapter of the Association for Computational Linguistics (pp. 29–32).

## Status — Proto-Germanic templates

- Proto-Germanic template now splits into a strong (accented) syllable and an optional weak syllable, so lexical items ending in nasal vowel `ą` (e.g. `*knewą`, `*blōdą`) are well-formed.
- German vowel pipeline still needs work: `kniː`, `broːt`, `bluːt` fail to project `*knewą`, `*braudą`, `*blōdą`. Next action: step through the ew→iu→ī + final `ą` deletion chronology to see where we lose analyses.
- After the vowel fixes, retest high-priority cognate sets (knee/bread/blood/door) and refresh the README.

## 2025-10-19 — Proto templates & German ew chain

- Proto-Germanic words now consist of a strong syllable plus an optional weak syllable; this legalises neuter `*-ą` forms in the template.
- German `ew → iu → ī` is now split into contextual steps (`e→i/_w`, `w→u/i_`, `iu→ī/_(a|ą)`) so the transformation no longer deletes surrounding material.
- Still missing: German `kniː`, `broːt`, `bluːt` fail to reconstruct `*knewą`, `*braudą`, `*blōdą`; next pass is to trace the long-vowel and nasal-deletion stages to see where candidates disappear.

## 2025-10-19 — German long-vowel tracing

- Stepped through `ProtoWord` + contextual `ew` rules; `*knewą`, `*braudą`, `*blōdą` survive to the long-vowel stage.
- After the long-vowel adjustments / vowel cleanup the candidates still collapse, so the blockage now lies in `GermanLongVowelRules` + `GermanVowelAdjustments` (or the surface filter).
- Next action: inspect those stages directly and adjust them so the nasal-vowel stems (`kniː`, `broːt`, `bluːt`) persist to the surface.

## 2025-10-19 — WGmc `au` monophthongisation

- Added a dedicated `GermanAuMonophth` stage (`{au} → ō / _ {d, ð, t, θ, n}`) ahead of the long-vowel rules so `*braudą` now feeds `ō` and the cascade outputs `brɔːd` instead of collapsing.
- Confirmed nominative `*-auz` forms still pass through the existing `{au} → {uː} / _ z` mapping; next fix is final devoicing so `brɔːd` reaches `broːt`.

## 2025-10-19 — German final devoicing

- Folded base consonant devoicing (`b/d/g/v → p/t/k/f / _ #`) into `GermanConsonantShift` so ‘bread/blood’ now surface as `brɔːt` / `bluːt` without overrides.
- Remaining gaps: `{au}` before non-dentals (e.g. `lauf`) still drifts to `{ɔː}` via later vowel cleanup; earmarked for a dedicated pass after consonant QA.

## 2025-10-19 — Proto filter notes

- We still allow every proto candidate to end in a single `*-ą`, but the current `ProtoWord` template also admits doubled nasal vowels (`*-ąą`). Tighten this later (e.g. via an explicit neuter suffix component) so we don’t have to track morphology while keeping the phonotactics realistic.

## TODO — German nasal-vowel debugging plan

1. Instrument staged transducers
   - Save intermediate FSTs after each component of the German cascade (ProtoWord, ew chain, long-vowel rules, final nasal loss, az-loss, vowel adjustments, etc.).
   - For each stage, run `apply down` on `k n e w ą`, `b r a u d ą`, `b l ō d ą` (and maybe `tōr`) to record the exact output string; note when the form collapses to the empty set.
2. Nail the long-vowel chronology
   - Ensure the ew-chain outputs `knīą` and the long-vowel block converts `ī → {iː}` without undoing the change later.
   - Confirm final nasal deletion (`ą → 0`) happens after `{iː}` has been created.
3. Fill the missing sound laws
   - Revisit `{au}` reflexes outside dental codas (e.g. `lauf`, `Haus`) now that devoicing is in place to ensure no collateral regressions.
4. Regression pass
   - Re-run `apply down` / `apply up` for `kniː`, `broːt`, `bluːt`; then spot-check other `*-ą` stems to make sure no collateral damage.
