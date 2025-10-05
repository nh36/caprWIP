# Germanic Transducer Status (2025-10-05)

This note captures the current state of the Proto-Germanic → daughter-language
FSTs after the phonotactic filter work on 2025‑10‑05. The goal is to document
what the transducers do now, how well they interact in the debugger, and where
additional historical rules are most urgently needed.

## 1. Transducer snapshot

| Language | Rule count (`define …Rules`) | Notes |
| --- | --- | --- |
| English | 17 | Covers Grimm’s law reflexes, vowel lengthening, monophthongisation (`ē → iː`, `ō → uː`), and light vowel/sonorant adjustments. |
| Dutch | 16 | Parallel to English with Dutch-specific vowel outputs (`au → œy`, `ai → ɛi`, `g → x`, etc.). |
| German | 16 | Captures High German consonant shift for initial stops and a few unstressed schwa outcomes, but lacks the large-scale vowel shifts and rhyme restructuring that characterise NHG. |

All three languages now pass through surface acceptors that require at least one
licensed vowel and only short onset/coda clusters. These filters stop runaway
strings (such as `rrr…`) but do not make the reconstructions any closer to the
attested forms by themselves.

## 2. How often reconstructions exist

Running the current binaries against the alignments in
`data/germanic-aligned-final.tsv` gives the following picture:

| Language | Word tokens | Tokens with ≥1 reconstruction | Share | Mean # of reconstructions (where ≥1) |
| --- | ---: | ---: | ---: | ---: |
| Dutch | 340 | 24 | **7.1 %** | 2.0 |
| English | 376 | 26 | **6.9 %** | 2.35 |
| German | 376 | 13 | **3.5 %** | 4.31 |

So only around one word in fourteen currently receives any Proto-Germanic back
projection, and German is the least productive of the three. When German does
produce a candidate, the mean candidate set is wide (≈ 4 forms), signalling that
rule coverage is broad but underspecified.

## 3. Cross-language agreement (“checkmarks”)

Looking at intersections of the candidate sets per concept (cognate set ID):

- **English ∩ Dutch:** 1 concept (`COGIDS 139`, *adder*).
- **English ∩ German:** 1 concept (`COGIDS 246`, *dill*).
- **Dutch ∩ German:** 0 concepts.
- **All three languages:** 0 concepts.

Thus the debugger almost never shows a shared reconstruction, matching the UI
experience.

Representative intersections:

- **Adder** (COGID 139) – English / Dutch share `{adar, adaz, azdar, azdaz}`, but
  German only produces High-German-shifted forms like `uwtar`/`uztaz`, so the
  triple intersection is empty.
- **Dill** (COGID 246) – English and German intersect at `del`, while Dutch only
  offers forms such as `dela`, `delaz`, `dezlaz`.

No concept produces a single protoform across all three daughters.

## 4. Word-level inspection

The table below (attested IPA → `apply_up` output) illustrates typical cases.

| Concept | Dutch | English | German |
| --- | --- | --- | --- |
| *adder* | `ɑdər → {adar, adaz, azdar, azdaz}` | `ædər → {adar, adaz, awdar, awdaz, azdar, azdaz}` | `ɔtər → {uwtar, uwtaz, uztar, uztaz}` |
| *dill* | `dɪlə → {dela, delaz, dezla, dezlaz}` | `dɪl → {del}` | `dɪl → {del}` |
| *year* | `jaːr → ∅` | `jɪər → {jewar, jewaz, jezar, jezaz}` | `jaːr → ∅` |
| *bake* | `bɑkə → {baka, bakaz, bazka, bazkaz}` | `beɪk → ∅` | `bakən → ∅` |

Forward projection from the English “year” candidates illustrates the symptom:

```
Proto candidate jewar → English {jɪər, jɪʋər, …}; Dutch {jɪʋər, jɪʋɑr}; German {jɪər, jɪvər}
Proto candidate jezar → English {jɪər, jɪrər};  Dutch {jɪɑr, jɪər, …}; German {jɪər, jɪrər}
```

Neither Dutch nor German has rules to turn *jē- into the observed `jaː-`, so the
convergent candidate set remains empty.

Words with **no** reconstruction tend to be high-frequency items that require
major vowel or inflectional changes. Examples (all fail in all three FSTs):

- *ball*, *bath*, *beaver*, *beech*, *begin*, *belly*.

Words that **do** reconstruct (per language) include:

- Dutch: *adder*, *comb*, *cud*, *day*, *buck* – mostly short CVC stems with
  conservative vowels.
- English: *adder*, *bid*, *deer*, *fire* – rely on simple vowel adjustments or
  consonant shifts already encoded.
- German: *dill*, *fish*, *lime*, *rope*, *side* – typically where the modern
  vowel is close to the proto vowel and only consonant changes are needed.

## 5. Diagnosis by language

### English & Dutch

- Both rulesets cover primary consonant shifts and a few vocalic outcomes, but
  neither addresses nasal+stop clusters (*ban*, *bannan* → `bæ n` / `ban`), or the
  systematic raising/lowering of Proto *ē / ō / ai / au* to the observed modern
  long vowels (`ē → *aː*` in Dutch *jaar*, `ē → iː/əə` patterns in English *beech*).
- English additionally lacks changes for final *-az* → *-es/-s* (e.g., *bast*).

### German

- No representation of the Early New High German vowel shifts (e.g., *ē → iː* or
  *ē → aː*, *ai → aɪ*, *au → aʊ*, *eu → ɔy*).
- Proto endings in *-az / -an* are not mapped to German *-er / -en*.
- The High German consonant shift is handled only word-initially; medial
  transitions (e.g., *-tt-* → *-ss/-tz*, *-pp-* → *-ff*) are absent.
- Schwa epenthesis is only sketched; hence wildly over-generated outputs such as
  `uwtar` for *adder*.

Combined, these gaps explain why pairwise intersections are almost empty: English
and Dutch do reach consonant-level agreement, but German rarely meets them in the
vowel space.

## 6. Suggested next tweaks (no changes applied yet)

The data above point to a few high-value additions, especially for German:

1. **Add Proto vowel developments for German.** Map `ē → aː / eː`, `ai → aɪ`, `au →
   aʊ`, `eu/{ai}`→`ɔy`, and model rounding before /r/. These shifts would allow
   words like *year*, *beech*, *beaver* to land near their attested outputs.
2. **Handle Proto *-az / -an / -ą* endings.** German reflexes typically end in
   `-er`, `-en` or `-e`. Introducing positional rules for `az → er`, `an → en`,
   `ą → an` would increase overlap on items such as *adder*, *ban*, *beaver*.
3. **Add medial High German consonant shifts.** Rules like `pp → pf`, `tt → ts`,
   `k → ch` between vowels are still missing. These would align proto forms with
   German outcomes such as *backen*, *Pfeffer*, etc.
4. **Dutch long vowel adjustments.** Rules for `ē → ie/ee`, `ē → aː` in the right
   environments (e.g. before `r`) would allow words like *jaar* and *beech* to
   reconstruct.
5. **English stressed vowel reductions.** Allow Proto *ā/ō/ē* to give modern `ɔː`,
   `oʊ`, `iː` in specific contexts; this would reduce the need for manual overrides
   on items like *beach/beech*, *boat*, *bone*.

Each of these should be added iteratively, checking the debugger after each step
so we can confirm that new overlaps appear and no over-generation slips through.

## 7. Next investigative steps

- Keep using `compare_fst` (or the UI debugger) to monitor pairwise intersections
  as new rules land; a running tally of “English × German with shared protoform”
  will show when we are making progress.
- Prioritise high-frequency concepts that currently fail (*year*, *beach*, *bath*,
  *beaver*, *begin*). They touch the same missing rules identified above and will
  exercise the vowel shift logic once it is implemented.
- Once German vowel shifts are encoded, rerun the statistics script to see how
  the “tokens with ≥1 reconstruction” proportion improves.

With these changes in view we can expand the German coverage to match English and
Dutch, and more importantly, start seeing regular Proto forms shared by at least
two daughters—exactly the “checkmarks” we want in CAPR.
