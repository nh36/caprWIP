# Germanic Transducer Status — October 2025

Outcome of the Proto-Germanic → English/Dutch/German FST work completed on 2025-10-05.

## Coverage snapshot
| Language | Tokens | With reconstruction | Share | Mean reconstructions/token |
| --- | ---: | ---: | ---: | ---: |
| Dutch | 340 | 24 | 7.1% | 2.00 |
| English | 376 | 39 | 10.4% | 1.87 |
| German | 376 | 11 | 2.9% | 7.91 |

## Intersections
- English ∩ Dutch: 5
- English ∩ German: 2
- Dutch ∩ German: 0
- All three languages: 0

## Key effects
- Removed the literal `k → "ch"` rule so phonology stays in IPA.
- Introduced a shielded spirantisation pass (`kk → K`, `k → x/ç`, `K → k`) to model the ach/ich split while preserving geminate-derived stops.
- Added English initial cluster mapping (`kn-/gn- → n-`) with backward restoration so surface forms like *knight*, *gnaw* still supply proto `*kn-/gn-` and intersect with German/Dutch cognates.
- Added an English initial cluster rule (`kn-/gn- → n-`) with backward annotations so Modern English reflexes like *knight*/ *gnaw* can still project proto *kn-/gn-* and align with German/Dutch cognates.
- Adjusted vowel lowering (`u → ɔ`) to recognise the shielded consonant.
- Refactored the German FST into staged composition (`GermanCoreRules`, `GermanStopShift`, `GermanCleanup`) matching the Burmish style.

### Sample mappings
- `*buk` → `bɔx`, `bɔx` → `*buk`.
- `*bukk` → `bɔk`, `bɔk` → `*bukk`.
- `ʃtɔk` currently lacks a shared protoform (cluster handling still pending).

## Next work items
- Add German vowel developments (ē/ō, diphthongs) and admit `ç` in the surface filter.
- Model cluster/geminate reflexes such as `*stukkaz` → `ʃtɔk`.
- Apply the same staged format to English and Dutch FSTs.
- Summarise the Word attachments in Markdown while keeping the originals available.
