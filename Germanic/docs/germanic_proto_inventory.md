# Proto-Germanic inventory audit

## Existing macros
- `ProtoVowel` (`server/fsts/germanic.txt:13`) covers short/long oral vowels plus nasal `ą`, `ą`, diphthongs `{ai}`, `{au}`, `{eu}`, and front rounded series (`ø`, `œ`, `y`, `ʉ`).
- `ProtoConsonant` (`server/fsts/germanic.txt:19`) includes stops, fricatives, nasals, liquids, plus special symbols (`ð`, `ɣ`, `ɪ`, `ʃ`, `ʋ`, `ʌ`, `ʤ`, `ʧ`), but omits `θ` which shows up in later contexts.
- `ProtoOnset/Core` and `ProtoCoda/Core` (`server/fsts/germanic.txt:29-58`) enumerate dozens of clusters, including `θ`-initial/medial clusters (`θl`, `θr`, `nθ`, `lθ`), again assuming `θ` is in the base inventory even though `ProtoConsonant` excludes it.
- `ProtoWord` is currently `ProtoStrongSyllable (ProtoWeakSyllable)?`, so the proto lexicon assumes a stress-based syllable template with optional weak suffixes.

## German rule contexts vs proto inventory
- German consonant rules condition on `θ` multiple times (e.g. `GermanAuMonophthContext d | ð | t | θ | n`, `GermanVowelAdjustments` with `u -> {ɔ} || _ (k | K)`). `θ` never appears in `ProtoConsonant`, so the rule contexts implicitly rely on tokens that the proto alphabet does not define.
- Rules also reference special placeholders (`K` via `kk -> K`) and multi-character proto sequences such as `{iu}`, `{ai}`, `{au}` that are treated as single proto symbols; the current inventory only wraps these in specific rules, not in the shared alphabet.
- The surface filter `GermanSurface` mixes bare symbols (`a`, `p`) with quoted multi-character strings (`"pf"`, `"ts"`, `"ai"`), so tokenisation oscillates between single characters and multi-character atoms. The helper FST `server/fsts/german_surface_prep.txt` and Python script `server/tools/german_surface_prep.py` then wrap outputs in braces, but they each make different segmentation choices (e.g. script splits `ts` to `t` + `s` whereas the Foma filter treats `"ts"` as one token).
- Within `GermanConsonantShift` (`server/fsts/germanic.txt:280-289`), the outputs `{f}`, `{ts}`, `{ʃ}` assume affricates are single tokens. Any new proto inventory must keep those as indivisible symbols so the shift can continue collapsing whole clusters in a single pass.

## Implications for the new proto alphabet
- The Burmish-style two-level approach will need explicit lexical-surface pairs for:
  * all simple consonants, including `θ` and `hw`-like sequences if they appear in the lexicon,
  * long vowels and diphthongs as single lexical atoms `{*aː}`, `{*ai}`, etc.,
  * consonant clusters that function as proto onsets/codas (or else we must derive them compositionally rather than enumerating strings like `ndr`, `stj`).
- Intermediate placeholders such as `K` should become internal rewrite markers rather than part of the lexical inventory; alternatively we can model geminate `kk` via separate medial symbols in the proto definition.
- Surface affricates (`pf`, `ts`) and long vowel graphemes should be tokenised consistently as single two-level symbols to avoid fights between the Foma surface filter and the Python wrapper.

This audit will guide the `pgrmInitC`/`pgrmRime` draft so that every rule context aligns with a declared proto symbol, and the upward application of the stack yields well-formed Proto-Germanic outputs.

## Progress log
- Added `pgrmOnsetCore` and `pgrmCodaComplex` so every cluster enumerated in `ProtoOnsetCore`/`ProtoCodaCore` now has a starred counterpart (`server/fsts/germanic.txt:88-164`). This lets `pgrmWord` accept the standard smoke lexicon (`knewą`, `braudą`, `blōdą`, `tōr`) without resorting to ad-hoc placeholders.
- Captured a comparison harness that compiles temporary FSTs and runs `flookup` comparisons; current outputs show legacy `ProtoWord` and `pgrmWord` (with star stripping) both accept the smoke set, and their `GermanConsonantShift` compositions agree (`server/tools/compare_german_proto.sh`).
- 2025-11-01 follow-up: added `{*z}` to `pgrmWeakCoda`, but `GermanProtoInput` still refuses `*laukaz`; need to track down the remaining filter that blocks `*-kaz/-kiz` verbs before the sound rules run.

## Next steps
- Revisit `GermanLongVowelRules` in a fresh session: keep macron notation through phonological rules, then convert to IPA length marks during the final orthography cleanup.
