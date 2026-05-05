# Research memo — 2104 linden / lind

## Starting point

- **ID:** 2104
- **CONCEPT:** linden
- **COUNTERPART:** lind
- **PROTO:** *líndō
- **PROTOFORM:** *líndō
- **DERIVATION_CLASS:** regular
- **NOTE:** Kroonen *lindō- f. 'linden/lime tree' → OE lind f.; linden is not standard OE form

This is a note-bearing regular row. `Germanic/docs/lexeme_reports/coverage_audit.md` flags row 2104 as requiring lexeme-report coverage because the TSV `NOTE` is non-empty, and no pilot or full lexeme report for this lexeme is present under `Germanic/docs/lexeme_reports/`.

## Packet evidence assessment

- **Authoritative/current:** the live TSV row and the packet's compact derivation trace agree that the active row is `*líndō -> lind`. The current OE generator also still returns `lind` for `líndō`, so the row's live project target is stable.
- **Useful background:** the packet note correctly identifies the real issue: Kroonen's comparative headword is `*lindō-` and the OE target for this row is `lind`, not imported Modern English `linden`. The Kroonen bibliography candidate is therefore genuinely relevant.
- **Stale or superseded:** the packet itself is fairly clean, but broader repo history contains stale debugging material that still expected `linden` (for example in `Germanic/docs/germanic_transducer_report.md`, `Germanic/docs/non_firing_rules_analysis.md`, and `Germanic/docs/germanic_notes/final_vowel_apocope_investigation.md`). Those are diagnostic remnants of earlier project assumptions, not current lexical authority for row 2104.
- **Irrelevant or misleading:** the packet's only lexical-table support is `old_english_wiktionary.tsv: linden -> linden`. That is not good row-level authority for the current OE noun target. Repo dictionary material instead supports `lind` as the noun headword, and Clark Hall also has `linden` as an adjective meaning 'made of linden-wood', which makes the packet's bare `linden` hit especially easy to misread.

## Additional repo research

Checked beyond the packet:

- `Germanic/data/oe_known_problems.tsv` — no row-specific entry for `*líndō`, `lind`, or `linden`.
- `Germanic/docs/lexeme_reports/coverage_audit.md` — confirms row 2104 needs report coverage because of `NOTE`.
- `docs/refs.bib` — confirms usable keys including `[@Kroonen2013]`, `[@ClarkHall1960]`, and `[@BosworthToller1898]`.
- `docs/references/kroonen_etymological_dictionary_pgmc.vision.txt` — gives `*lindō- f. 'lime tree'` with OE `lind` [@Kroonen2013].
- `docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt` — gives `lind I. f. lime-tree, linden` and also separately `linden` 'made of linden-wood' [@ClarkHall1960].
- `docs/references/bosworth_toller_anglo_saxon_dictionary.vision.txt` — preserves `lind` as the OE lexeme and attestation base, not `linden` as the ordinary noun headword [@BosworthToller1898].
- `Germanic/data/old_english_wiktionary.tsv` — supplementary only; it has `linden -> linden` and no `lind` row, so it is inadequate as sole evidence for the OE target.
- `Germanic/docs/germanic_transducer_report.md`, `Germanic/docs/non_firing_rules_analysis.md`, and `Germanic/docs/germanic_notes/final_vowel_apocope_investigation.md` — useful only as stale project history showing earlier expectation drift toward `linden`.
- `Germanic/docs/DEV_NOTES.md` — no relevant row-specific discussion found.
- `Germanic/docs/analysis/` and `Germanic/docs/dossiers/` — no dedicated dossier or analysis file for this lexeme, and none was named in the packet or TSV note.
- Live probe: `printf 'líndō\n' | flookup -i old_english.bin` returns `lind`, matching the current packet and TSV.

No pilot lexeme report for `linden / lind` is currently present.

## Reconstruction and early-stage forms

This row needs three levels kept distinct:

1. **Cognate-set proto / etymological headword:** Kroonen's lexeme is cited as stem-style `*lindō-` 'lime tree' [@Kroonen2013].
2. **Project input form:** the TSV row uses `PROTO = PROTOFORM = *líndō`, the nominative-style PGmc input actually fed into the OE derivation.
3. **OE target form:** the row targets OE `lind`, not `linden` [@Kroonen2013; @ClarkHall1960].

The live derivation is straightforward: the packet trace shows NWGmc final long-`ō` raising to `*líndu`, then OE high-vowel apocope to `lind`. Nothing in the current repo evidence requires a different PGmc input or a different OE citation target.

## Old English philology

`lind` is an attested OE noun and the ordinary lexical target supported by the repo's dictionary materials. Kroonen gives OE `lind` under the cognate set [@Kroonen2013], and Clark Hall lists `lind` as a feminine noun meaning 'lime-tree, linden' [@ClarkHall1960]. This is therefore not a reconstructed-OE case.

The important philological caution is negative: the repo does **not** support treating `linden` as the ordinary OE noun counterpart for this row. Clark Hall's separate `linden` entry is adjectival ('made of linden-wood') [@ClarkHall1960], and the packet's Wiktionary-table hit does not distinguish that from the noun. So the lexical-table evidence is supplementary at best and misleading if treated as decisive.

No dialect-specific, manuscript-specific, or reconstructed-only restriction is supported by the repo evidence checked here.

## Project problem and solution

The project problem is editorial, not phonological. The current derivation `*líndō -> lind` is regular and already works. The risk comes from the concept gloss `linden`, the packet's `old_english_wiktionary.tsv` hit `linden -> linden`, and stale debugging notes that still expected `linden`; together these can make the row look like an OE final-`-n` problem when it is really a headword-selection problem.

The solution is to keep row 2104 exactly as a regular OE noun row targeting `lind`, explicitly treat Kroonen's `*lindō-` as cognate-set headword notation rather than a reason to change the OE output, and describe `linden` in packet-era lexical or debugging material as non-authoritative background only.

## Paradigm probe

A paradigm probe is **not required** for this row. The row does not hinge on choosing among competing OE paradigm cells or on diagnosing an analogy class; the live issue is simply distinguishing the attested OE noun target `lind` from misleading lexicographic or historical-project material involving `linden`.

## Recommended final report

Recommend a brief final report stating that row 2104 is a regular derivation `*líndō -> lind`, that Kroonen's `*lindō-` is comparative headword material consistent with OE `lind`, and that packet-era `linden` evidence is supplementary or stale rather than authority for the OE target.

## Data-change recommendations

- **TSV `PROTO`:** no change recommended.
- **TSV `PROTOFORM`:** no change recommended.
- **TSV `COUNTERPART`:** no change recommended.
- **TSV `DERIVATION_CLASS`:** no change recommended.
- **TSV `NOTE`:** no change recommended; it already captures the crucial point that `linden` is not the standard OE form.
- **`oe_known_problems.tsv`:** no change recommended.
- **DEV_NOTES / dossier text:** no change recommended. There is no dedicated DEV_NOTES or dossier treatment for this row that needs cleanup.
