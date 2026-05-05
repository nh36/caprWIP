# Research memo — 2120 march / mearc

## Starting point

- **ID:** 2120
- **CONCEPT:** march
- **COUNTERPART:** mearc
- **PROTO:** `*márkō`
- **PROTOFORM:** `*márkō`
- **DERIVATION_CLASS:** `regular`
- **NOTE:** `Kroonen *markō- f. 'boundary' → OE mearc f.; mearcian is the verb 'to mark'`

This is a note-bearing regular row, so it still requires lexeme-report coverage. `Germanic/docs/lexeme_reports/coverage_audit.md` lists row 2120 among required rows with no report, and there is no manual pilot/full report for this lexeme under `Germanic/docs/lexeme_reports/`.

## Packet evidence assessment

- **Authoritative/current:** the live TSV row; the packet's compact derivation trace `*márkō -> mearc`; and the packet's exact-pair `DEV_NOTES.md` hits at 29435 and 29466 showing that the current OE stack treats `*márkō` as a breaking-plus-apocope success case.
- **Useful background:** the packet's Kroonen-based note is the real lexical warning for the row: the OE target is noun `mearc`, while `mearcian` is a separate verb. The packet's `arestoration_r_l_research.md` hit is also useful as class-level background because it confirms this row belongs to the breaking-conditioned set.
- **Stale or superseded:** the packet's own "possibly stale or diagnostic" bucket is correctly labelled. The concept-name hits in `notable_findings.md` are not row-level evidence, and the A-restoration table entry is only diagnostic background, not lexical authority.
- **Irrelevant or misleading:** the packet's `old_english_wiktionary.tsv` hit `march -> mearcian` is actively easy to misread. It reflects a Modern-English gloss match to the verb, not authority against the row's noun target `mearc`.

## Additional repo research

Checked beyond the packet:

- `Germanic/docs/lexeme_reports/coverage_audit.md`.
- `Germanic/data/oe_known_problems.tsv`.
- `docs/debug_snapshots/oe_full_trace_report.txt`.
- `Germanic/docs/germanic_transducer_report.md`.
- `Germanic/docs/germanic_notes/final_vowel_apocope_investigation.md`.
- `Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.md` and `.audit.md`.
- `docs/references/kroonen_etymological_dictionary_pgmc.vision.txt`.
- `docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt`.
- `docs/references/bosworth_toller_anglo_saxon_dictionary.vision.txt`.
- `docs/references/campbell_old_english_grammar.txt`.

Main findings from that extra pass:

- No `oe_known_problems.tsv` entry exists for row 2120, `*márkō`, or `mearc`.
- The fuller trace in `docs/debug_snapshots/oe_full_trace_report.txt` confirms the current derivation path `*markō -> *marku -> *mærku -> *mearku -> mearc`.
- Repo-local reference extracts support noun `mearc` directly: Kroonen has `*markō- f. 'boundary, region' ... OE mearc f. 'boundary, district'` [@Kroonen2013]; Clark Hall has `mearc ... 'mark,' sign, line of division ... boundary, limit, term, border` [@ClarkHall1960]; Bosworth-Toller likewise gives `mearc` under the boundary/limit headword [@BosworthToller1898].
- Those same reference extracts also show that `mearcian` is a separate verb entry, not the noun counterpart for this row [@Kroonen2013; @ClarkHall1960; @BosworthToller1898].
- There is no dedicated dossier for this lexeme. The only named analysis file in the packet (`arestoration_r_l_research.md`) is broad class background rather than a full row dossier.
- Older project-history files still preserve the earlier gloss confusion: `Germanic/docs/germanic_transducer_report.md` lists `*markō -> mearcian`, and `Germanic/docs/germanic_notes/final_vowel_apocope_investigation.md` has `*markō -> mearcō (exp. mearcian)`. Those are stale diagnostics, not current row authority.
- The debug-snapshot report with lexeme-report headings contains only the carried-over TSV note for this row, not a vetted pilot/full report.

## Reconstruction and early-stage forms

This row is straightforward if three levels are kept distinct:

1. **Cognate-set proto / etymological headword:** Kroonen's lexical entry is stem-style `*markō-` [@Kroonen2013].
2. **Project input form used for derivation:** the TSV row uses `PROTO = PROTOFORM = *márkō`, i.e. the PGmc input form actually fed into the OE derivation trace.
3. **OE target form:** the row targets OE noun `mearc`, not the verb `mearcian`.

The current phonological path is regular. The live trace shows NWGmc final long-`ō` raising to `-u`, then Anglo-Frisian brightening (`a > æ`), then OE breaking before `rC` (`æ > ea`), then final high-vowel apocope, yielding `mearc`. The packet's A-restoration background is consistent with this chronology: breaking bleeds any would-be restoration here, so `mearc` is unaffected by that later investigation.

## Old English philology

This is an attested OE noun case, not a reconstructed-OE workaround. Kroonen, Clark Hall, and Bosworth-Toller all support noun `mearc` as the relevant OE lexeme, with boundary/limit/district senses [@Kroonen2013; @ClarkHall1960; @BosworthToller1898].

The main philological issue is lexical differentiation, not sound change. The repo's reference extracts treat `mearcian` separately as a verb 'to mark / fix bounds' [@Kroonen2013; @ClarkHall1960; @BosworthToller1898], so the packet's Wiktionary-table hit is supplementary only and misleading if treated as row-level evidence.

Campbell is also consistent with the form-side result: he cites `mearc` as an OE example with unsmoothed `ea` before `rc`, which fits the row's breaking output [@Campbell1959].

No dialect-specific, manuscript-specific, or paradigm-cell-specific complication turned up in the repo research.

## Project problem and solution

The project problem is editorial/headword disambiguation, not an unresolved derivation. The current row already models a regular noun pathway `*márkō -> mearc`, but the English concept gloss `march` and some older repo materials can pull the reader toward verb `mearcian`.

The correct project reading is therefore:

- keep row 2120 as the noun `mearc` row;
- treat the Kroonen note as the controlling lexical guidance;
- treat `mearcian` hits as evidence for a related but distinct verb, not as a reason to change the OE target or derivation class;
- treat older repo expectations of `mearcian` as stale project history only.

## Paradigm probe

A paradigm probe is **not required**.

This is not a late-analogy or paradigm-cell selection case. The row already targets an attested citation-form noun, and the evidence problem is lexical disambiguation between noun `mearc` and verb `mearcian`, not uncertainty about which OE inflectional cell should stand in the TSV.

## Recommended final report

Recommend a brief final report saying that row 2120 is a regular derivation to attested OE noun `mearc`, that Kroonen's `*markō-` is the cognate-set headword behind the row, and that packet-era `mearcian` hits belong to a separate verb and to stale project history rather than to the noun target.

## Data-change recommendations

- **TSV `PROTO`:** no change recommended.
- **TSV `PROTOFORM`:** no change recommended.
- **TSV `COUNTERPART`:** no change recommended.
- **TSV `DERIVATION_CLASS`:** no change recommended.
- **TSV `NOTE`:** no change recommended. The current note already states the crucial noun/verb distinction clearly enough.
- **`oe_known_problems.tsv`:** no change recommended.
- **DEV_NOTES / dossier text:** no change recommended. The current `DEV_NOTES.md` material for this row is accurate as implementation history, and no lexeme-specific dossier exists. If later cleanup is wanted, it belongs instead in stale non-dossier background files such as `Germanic/docs/germanic_transducer_report.md` and `Germanic/docs/germanic_notes/final_vowel_apocope_investigation.md`, not in the live TSV row.
