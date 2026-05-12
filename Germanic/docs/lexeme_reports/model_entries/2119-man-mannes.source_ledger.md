# Source extraction ledger — man / mannes

This ledger records the source forms and working distinctions gathered before the
book-style entry was drafted.

| Source | Date / position | Form(s) given | Morphology / formation | Old English form(s) | Claim used for the entry | Citation key available? | Local path | Confidence / review note |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| TSV row 2119 | live row | `PROTO *mánnaz`; `PROTOFORM *mánnas`; `mannes` | lexeme-level noun vs selected gen.sg. cell | `mannes` | The row targets the genitive singular rather than the citation form. The local TSV note still cites `Kurath 1956`, which is not present in `docs/refs.bib`. | no | `Germanic/data/germanic-aligned-final.tsv` | high; keep missing-key issue out of final prose |
| Compact trace | current trace | `*mánnas -> mannes` | regular gen.sg. derivation | `mannes` | Confirms that the selected `PROTOFORM` produces the target directly. | no | `Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.compact.md` | high |
| Campbell | OE paradigm | `mann, man`; `mannes`; `menn` | root noun with oblique singular and plural forms | `mannes` | Supplies the crucial OE genitive singular comparator. | yes — `Campbell1959` | `docs/references/campbell_old_english_grammar.txt` | high |
| Sievers-Brunner | OE phonology and paradigm | `man mannes`; `man ... monnes` | geminate simplification in word-final position; medial geminate retained in inflection | `mannes`; `monnes` | Explains why the citation form simplifies word-finally but the gen.sg. preserves medial `nn`. | yes — `SieversBrunner1965` | `docs/references/brunner_1965_altenglische_grammatik.txt` | high |
| Clark Hall | OE dictionary headword | `mann` | dictionary citation form | `mann` | Confirms that the ordinary headword remains `mann`, not `mannes`. | yes — `ClarkHall1960` | `docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt` | high |
| Ringe-Taylor / Orel / Kroonen | comparative reconstruction | `*mann-`; `*mannz`; `*mannan-` | competing lexeme-level reconstructions | OE `mann ~ monn`; `mann` | Shows that lexeme-level citation reconstruction varies even though the selected gen.sg. cell is stable. | yes — `RingeTaylor2014`; `Orel2003`; `Kroonen2013` | cited in packet/memo/slice | medium |
| Local memo / slice synthesis | current project analysis | gen.sg. `*mannas -> mannes`; controls `*mannăz -> man`, `*manną -> man`, `*mannăi -> manne` | manual paradigm-cell contrast | `mannes`; `man`; `manne` | The late-analogy case depends on a manual paradigm comparison showing that the gen.sg. is the relevant OE cell. | no | `Germanic/docs/lexeme_reports/research_memos/2119-man-mannes.md`; `Germanic/docs/lexeme_reports/dev_notes_slices/2119-man-mannes.md` | high; saved probe still absent |

## Citation-locator full-corpus high-confidence pass

- Added page-specific locators for `Orel2003, 299`.
- This pass was limited to high-confidence sources (`Kroonen2013`, `Orel2003`, `ClarkHall1960`, `RingeTaylor2014`, `Fulk2018`, `Seebold1970`, `BrightCassidyRingler1971`).
- Existing citations to conditional or unresolved locator sources were left unchanged.
