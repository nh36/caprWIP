# Reader-facing foma width check 01

_Generated from the current fenced `foma` blocks in the reader-facing chapter files._

## Summary

- Foma blocks checked: 17.
- Blocks over the conservative 90-character threshold: 2.
- Width-safe rendering protocol: `ReaderFacingFoma` uses `fvextra`/`Verbatim` with `breaklines=true`, `breakanywhere=true`, and `fontsize=\small` in the Docker XeLaTeX build.

| File | Rule section | Start line | Longest line | Over threshold under old rendering |
| --- | --- | --- | --- | --- |
| 049-050-b-allophony-and-sievers-law-syncope.md | SC049. Distribution of \emph{*b} after vowels and liquids (`PGmcBAllophony`) {#rule-PGmcBAllophony} | 31 | 38 | no |
| 049-050-b-allophony-and-sievers-law-syncope.md | SC050. Sievers-law syncope (`SieversLawSyncope`) {#rule-SieversLawSyncope} | 57 | 72 | no |
| 051-sk-palatalization.md | SC051. Palatalization of \emph{*sk} to \emph{*sc} (`OESkPalatalization`) {#rule-OESkPalatalization} | 30 | 77 | no |
| 052-velar-palatalization.md | SC052. Palatalization of \emph{*k} before front vowels and \emph{*j} (`OEVelarPalatalizationKFront`) {#rule-OEVelarPalatalizationKFront} | 59 | 58 | no |
| 052-velar-palatalization.md | SC052. Velar palatalization before front vowels (`OEVelarPalatalization`) {#rule-OEVelarPalatalization} | 101 | 74 | no |
| 053-054-pre-umlaut-bridge-and-w-loss.md | SC053. Loss of \emph{*w} after velars (`OEPostVelarWLoss`) {#rule-OEPostVelarWLoss} | 26 | 28 | no |
| 053-054-pre-umlaut-bridge-and-w-loss.md | SC054. Loss of \emph{*w} before final \emph{*i} (`OEWLossBeforeI`) {#rule-OEWLossBeforeI} | 49 | 46 | no |
| 055-056-i-umlaut-core.md | SC055. Fronting under i-umlaut (`OEIUmlautFronting`) {#rule-OEIUmlautFronting} | 50 | 70 | no |
| 055-056-i-umlaut-core.md | SC055. Raising under i-umlaut (`OEIUmlautRaising`) {#rule-OEIUmlautRaising} | 100 | 69 | no |
| 055-056-i-umlaut-core.md | SC055. Diphthongal outcomes under i-umlaut (`OEIUmlautDiphthong`) {#rule-OEIUmlautDiphthong} | 131 | 72 | no |
| 055-056-i-umlaut-core.md | SC055. The composite i-umlaut rule (`OEIUmlaut`) {#rule-OEIUmlaut} | 175 | 34 | no |
| 055-056-i-umlaut-core.md | SC056. West Saxon palatal diphthongization (`OEWsPalatalDiphthongization`) {#rule-OEWsPalatalDiphthongization} | 212 | 110 | yes |
| 057-j-cluster-coalescence.md | SC057. Coalescence of velar + \emph{*j} clusters (`OEJClusterCoalescence`) {#rule-OEJClusterCoalescence} | 25 | 30 | no |
| 058-nasal-dissimilation.md | SC058. Nasal dissimilation in short-vowel environments (`OENasalDissimilation`) {#rule-OENasalDissimilation} | 33 | 100 | yes |
| 059-oe-back-mutation.md | SC059. Back mutation before labials and liquids (`OEBackMutation`) {#rule-OEBackMutation} | 27 | 90 | no |
| 060-ws-palatal-umlaut-note.md | SC060. West Saxon palatal umlaut before \emph{*h}-clusters (`OEWsPalatalUmlaut`) {#rule-OEWsPalatalUmlaut} | 21 | 56 | no |
| 061-weak-tail-nasal-loss-note.md | SC061. Reduction of final nasal weak-tail endings (`OEWeakTailNasalLoss`) {#rule-OEWeakTailNasalLoss} | 20 | 31 | no |

## Lines that would have overflowed under the old rendering

### 055-056-i-umlaut-core.md:212 — SC056. West Saxon palatal diphthongization (`OEWsPalatalDiphthongization`) {#rule-OEWsPalatalDiphthongization}

- `110` chars — `    {*æ} -> {*ea} || .#. [{*ʧ} | {*ʤ} | {*ʃ} | {*j}] _ [EnglishStarConsonant | EnglishPalatalConsonant | .#.],`
- `110` chars — `    {*ǣ} -> {*ēa} || .#. [{*ʧ} | {*ʤ} | {*ʃ} | {*j}] _ [EnglishStarConsonant | EnglishPalatalConsonant | .#.],`
- `110` chars — `    {*e} -> {*ie} || .#. [{*ʧ} | {*ʤ} | {*ʃ} | {*j}] _ [EnglishStarConsonant | EnglishPalatalConsonant | .#.],`
- `110` chars — `    {*ē} -> {*īe} || .#. [{*ʧ} | {*ʤ} | {*ʃ} | {*j}] _ [EnglishStarConsonant | EnglishPalatalConsonant | .#.],`
- `110` chars — `    {*é} -> {*íe} || .#. [{*ʧ} | {*ʤ} | {*ʃ} | {*j}] _ [EnglishStarConsonant | EnglishPalatalConsonant | .#.],`
- `109` chars — `    {*ḗ} -> {*īe} || .#. [{*ʧ} | {*ʤ} | {*ʃ} | {*j}] _ [EnglishStarConsonant | EnglishPalatalConsonant | .#.]`

### 058-nasal-dissimilation.md:33 — SC058. Nasal dissimilation in short-vowel environments (`OENasalDissimilation`) {#rule-OENasalDissimilation}

- `100` chars — `    {*m} -> {*f} || EnglishStarShortVowel _ EnglishStarShortVowel {*n} [EnglishStarShortVowel | .#.]`

## Interpretation

The conservative character threshold identifies blocks that were likely to overflow under the previous unwrapped PDF rendering. The current build-side `ReaderFacingFoma` environment wraps these lines, so the presence of long source lines no longer implies right-margin loss in the final PDF.
