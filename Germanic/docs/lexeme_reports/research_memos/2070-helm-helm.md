# Research memo — 2070 helm / helm

## Starting point

- **ID:** 2070
- **CONCEPT:** helm
- **COUNTERPART:** helm
- **PROTO:** *xélmaz
- **PROTOFORM:** *xélmaz
- **DERIVATION_CLASS:** regular
- **NOTE:** Kroonen *helma- m. 'helmet' → OE helm m.; helma is not nom.sg.

This is a note-bearing regular row. No pilot or full lexeme report for this lexeme was found under `Germanic/docs/lexeme_reports/`; `coverage_audit.md` flags row 2070 as needing report coverage because the TSV `NOTE` is non-empty.

## Packet evidence assessment

**Authoritative/current:** the live TSV row and the packet's compact derivation trace agree that the active project row is `*xélmaz -> helm`, with `PROTO = PROTOFORM = *xélmaz` and OE outcome `helm`. That is the current project treatment of the row.

**Useful background:** the packet's note correctly signals the real issue: Kroonen cites the cognate-set lexeme under stem-style `*helma-`, while the project row itself derives a nominative-style input to OE `helm`. The bibliography candidate `[@Kroonen2013]` is therefore genuinely relevant.

**Stale or superseded:** the packet is clean, but it omits older repo history in which project debugging materials still conflated this lexeme with `helma`. That older history survives elsewhere and should not be treated as present lexical authority.

**Irrelevant or misleading:** the packet's `old_english_wiktionary.tsv` hit `helm -> helma` is not direct support for the current helmet row. Repo lexicographic sources show OE `helma` as a separate noun meaning 'rudder/helm', not as the nominative singular of the helmet noun. Used incautiously, that packet hit would blur two different lexemes.

## Additional repo research

Checked beyond the packet:

- `Germanic/data/oe_known_problems.tsv` — no entry for row 2070, `*xélmaz`, `helm`, or `helma`.
- `Germanic/docs/lexeme_reports/coverage_audit.md` — confirms this row needs report coverage because of `NOTE`.
- `docs/refs.bib` — confirms usable keys `[@Kroonen2013]`, `[@ClarkHall1960]`, and `[@BosworthToller1898]`.
- `docs/references/kroonen_etymological_dictionary_pgmc.vision.txt` — distinguishes `*helma-` m. 'helmet' with OE `helm` from separate `*helman-` m. 'rudder' with OE `helma` [@Kroonen2013].
- `docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt` — gives `helm` as the ordinary noun including 'helmet' and separately gives `helma` m. 'helm, rudder' [@ClarkHall1960].
- `docs/references/bosworth_toller_anglo_saxon_dictionary.vision.txt` — gives `helm` with direct helmet attestations and a separate `helma` entry in steering/rudder usage [@BosworthToller1898].
- `Germanic/data/old_english_wiktionary.tsv` — supplementary only; it preserves the ambiguous `helm -> helma` mapping that likely reflects the rudder sense, not the helmet lexeme.
- `Germanic/docs/germanic_transducer_report.md` — preserves stale debugging history with a dataset sweep line `*xelmăz -> helma`, showing earlier project conflation rather than current row authority.
- `Germanic/docs/DEV_NOTES.md` — no relevant hit for this lexeme.
- `Germanic/docs/analysis/` and `Germanic/docs/dossiers/` — no dedicated dossier or analysis file for this lexeme, and none was named in the packet or TSV note.

No pilot lexeme report for `helm` is currently present under `Germanic/docs/lexeme_reports/pilot/`.

## Reconstruction and early-stage forms

This row needs three levels kept separate:

1. **Cognate-set proto / etymological headword:** Kroonen cites the helmet lexeme as `*helma-`, a comparative stem-style headword, not as the live OE row's derivational input [@Kroonen2013].
2. **Project input form:** TSV `PROTO` and `PROTOFORM` are both `*xélmaz`, the nominative-style PGmc input the project actually feeds into the derivation pipeline.
3. **OE target form:** `helm`, the attested OE helmet noun [@ClarkHall1960; @BosworthToller1898].

The comparative distinction matters doubly here because Kroonen also has a separate lexeme `*helman-` 'rudder', whose OE reflex is `helma` [@Kroonen2013]. So `*helma-` in the note is not evidence that the live TSV should switch to `helma`; it is comparative dictionary notation for the helmet cognate set, while OE `helma` belongs to another lexeme altogether.

## Old English philology

`helm` is directly attested and lexicographically ordinary in the repo's OE reference files, so this is not a reconstructed-OE case. Clark Hall lists `helm` with 'helmet' among its senses [@ClarkHall1960], and Bosworth-Toller supplies direct helmet citations such as `Helm galea` and multiple poetic occurrences [@BosworthToller1898].

`helma` is also attested in the repo's dictionaries, but not as the nominative singular of the helmet noun. Clark Hall glosses it as 'helm, rudder' [@ClarkHall1960], and Bosworth-Toller likewise treats it as a separate entry in steering usage [@BosworthToller1898]. The philological issue is therefore lexical ambiguity in English glossing, not uncertainty about an OE inflectional cell.

No dialect, manuscript, or reconstructed-only restriction is supported by the repo evidence checked here.

## Project problem and solution

The project problem is representational rather than phonological. The live derivation `*xélmaz -> helm` is straightforward, but the row note cites Kroonen's stem-style `*helma-`, and the packet's Wiktionary table surfaces OE `helma`; together these can make it look as though `helma` is an OE paradigm rival for the same noun.

The repo evidence points to a cleaner solution: keep the row exactly as a **regular** `*xélmaz -> helm` derivation, treat `*helma-` as cognate-set dictionary notation only, and explicitly recognize OE `helma` as a different lexeme ('rudder/helm') rather than as the target of row 2070. Older project traces that output `helma` should be described as stale debugging history, not as current evidence.

## Paradigm probe

A paradigm probe is **not required** for this row. The live row does not depend on choosing between competing OE paradigm cells; the issue is separation of two lexemes plus distinction between comparative stem notation and the project's active derivational input.

If someone later wanted an explanatory appendix, the useful comparison would not be a same-paradigm probe but a lexical one: current row `*xélmaz -> helm` versus the separate dictionary lexeme `helma` 'rudder'. That is outside the normal paradigm-probe use case and is not needed to justify the row.

## Recommended final report

Recommend a brief final report saying that row 2070 is regular: the project derives attested OE `helm` from live PGmc input `*xélmaz`, while Kroonen's `*helma-` is only comparative stem notation and OE `helma` in the repo's lexical materials belongs to a separate 'rudder/helm' lexeme. The report should also note that older `helma` project traces are stale diagnostic history.

## Data-change recommendations

- **TSV `PROTO`:** no change recommended.
- **TSV `PROTOFORM`:** no change recommended.
- **TSV `COUNTERPART`:** no change recommended.
- **TSV `DERIVATION_CLASS`:** no change recommended.
- **TSV `NOTE`:** **change recommended** — clarify that Kroonen's `*helma-` is comparative stem/headword notation for the helmet lexeme, while OE `helma` in repo lexica is a separate noun 'rudder/helm', not the OE nominative singular competitor to `helm`.
- **`oe_known_problems.tsv`:** no change recommended.
- **DEV_NOTES / dossier text:** no change recommended. There is no dedicated DEV_NOTES or dossier discussion that needs cleanup for this row; the stray `helma` debugging example in `germanic_transducer_report.md` can remain as historical background as long as it is not treated as current lexical authority.
