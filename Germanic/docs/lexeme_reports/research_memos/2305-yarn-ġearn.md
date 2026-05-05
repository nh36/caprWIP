# Research memo — 2305 yarn / ġearn

## Starting point

- **ID:** 2305
- **CONCEPT:** yarn
- **COUNTERPART:** ġearn
- **PROTO:** *gárną
- **PROTOFORM:** *gárną
- **DERIVATION_CLASS:** regular
- **NOTE:** Proto: oblique *garnăn→*garną (n. a-stem nom.sg.; Kroonen)

This is a note-bearing regular row. No pilot or full lexeme report for this lexeme was found under `Germanic/docs/lexeme_reports/`, and `coverage_audit.md` flags row 2305 as needing report coverage because the TSV `NOTE` is non-empty.

## Packet evidence assessment

**Authoritative/current:** the live TSV row; the packet's compact derivation trace showing `*gárną -> ġearn`; and the packet's lexical-table hit from `old_english_wiktionary.tsv`. These support the current live treatment of the row as a regular derivation to the ordinary OE noun.

**Useful background:** the packet note's `oblique *garnăn→*garną` wording is useful comparative-morphological background, and `[@Kroonen2013]` is the right first bibliography key to carry forward. The packet's paradigm note is also directionally right: nothing in the dossier points to a missing OE paradigm-cell workaround.

**Stale or superseded:** there are no explicit stale packet hits here, but the packet is very thin and should not be mistaken for a complete evidential base. Its lack of dossier or `DEV_NOTES` hits means it does not itself settle the difference between Kroonen's etymological headword/stem notation and the project's live derivational input.

**Irrelevant or misleading:** the packet can mislead by compression. Read alone, the note can sound as though the row ought to derive from oblique `*garnăn`, when the live project row actually derives from nominative/accusative-style `*gárną`. The packet also does not explain that dictionary sources often print OE `gearn` without dotted `ġ`, whereas the project counterpart normalizes palatal `ġearn`.

## Additional repo research

Checked beyond the packet:

- `Germanic/data/oe_known_problems.tsv` — no entry for row 2305, `*gárną`, or `ġearn`.
- `Germanic/docs/lexeme_reports/coverage_audit.md` — confirms this row needs report coverage because of `NOTE`, not because of a modelling failure.
- `docs/refs.bib` — confirms usable keys `[@Kroonen2013]`, `[@RingeTaylor2014]`, `[@ClarkHall1960]`, `[@BosworthToller1898]`, and `[@Orel2003]`.
- `docs/references/kroonen_etymological_dictionary_pgmc.vision.txt` and `docs/references/legacy/etymological_dictionary_of_proto_germanic_kroonen.txt` — give the comparative noun as `*garna-`, with OE `gearn` [@Kroonen2013].
- `docs/references/ringe_taylor_linguistic_history_vol2.txt` — explicitly gives `PNWGme *garna 'yarn' > *geern > *gearn > OE gearn` [@RingeTaylor2014].
- `docs/references/orel_handbook_germanic_etymology.vision.txt` — gives the same cognate set with OE `zearn/gearn`, but the OCR text is noisy enough that it is supporting background rather than primary authority [@Orel2003].
- `docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt` — gives noun headword `gearn (e) n. 'yarn, spun wool'` [@ClarkHall1960].
- `docs/references/bosworth_toller_anglo_saxon_dictionary.vision.txt` — gives `gearn` as a glossarial noun entry (`filatum`) and records `gearn-winde` [@BosworthToller1898].
- `docs/references/anglosaxonoldeng00wrig.txt` — preserves direct glossary lines `Filatum, gearn` and `Filatum, gearn` as local attestation support.
- `docs/debug_snapshots/oe_full_trace_report.txt` — confirms the live derivation trace reaches `ġearn`; this is a generated project artifact, useful for confirming current pipeline behavior but not independent lexical authority.

No full dossier or analysis file was named in the packet or TSV note for this lexeme, so the extra pass had to come from the repo dictionaries, reference texts, and coverage/debug files.

## Reconstruction and early-stage forms

This row needs the standard three-way distinction:

1. **Cognate-set proto / etymological headword:** comparative sources cite lemma-style `*garna-` (Kroonen) or equivalent headword notation for the cognate set [@Kroonen2013; @Orel2003].
2. **Project input form for derivation:** TSV `PROTO` and `PROTOFORM` are both `*gárną`, i.e. the nominative/accusative-singular style form that the project actually feeds into the OE derivation. The note's oblique `*garnăn` is not the live FST input.
3. **OE target form:** the row targets the attested OE noun `ġearn`, orthographically corresponding to dictionary `gearn`.

The early-stage chronology is consistent across the live pipeline and repo references: `*gárną/*garną` undergoes Anglo-Frisian brightening and then breaking to yield pre-OE `*gearną`, after which final nasal/apocope gives OE `gearn`, surfaced in project spelling as `ġearn`. `Ringe-Taylor` independently supports the key intermediate chain `*garna > *geern > *gearn > OE gearn` [@RingeTaylor2014]. Nothing in the checked evidence requires replacing the live input with oblique `*garnăn`.

## Old English philology

`gearn/ġearn` is directly attested in the repo's lexical materials, so this is not a reconstructed-OE case. Clark Hall gives noun `gearn (e)` 'yarn, spun wool' [@ClarkHall1960], Bosworth-Toller gives `gearn` as a glossarial noun (`filatum`) and compounds such as `gearn-winde` [@BosworthToller1898], and Wright's glossary reproduces the underlying `Filatum, gearn` evidence.

The main philological caution is lexical, not reconstructive. `gearn` is also a verbal form in dictionary materials (e.g. Clark Hall's separate preterite entry), and Bosworth-Toller has many non-noun `gearn` hits. So only sense-specific noun entries should be treated as evidence for this row. Once that homograph issue is controlled for, the noun itself is straightforwardly attested.

The project counterpart's dotted `ġearn` is therefore best read as a normalization of palatal initial `g`, not as a different lexeme from dictionary `gearn`. Nothing in the checked repo evidence requires a special dialect label, manuscript restriction, or paradigm-cell retargeting.

## Project problem and solution

The project problem is representational rather than derivational. The live row already derives correctly, but the TSV note compresses Kroonen's comparative morphology into wording that can be misread as if oblique `*garnăn` should feed the row or as if the OE target depended on an unmodelled paradigm choice.

The current project solution is the right one: keep row 2305 as a **regular** derivation with `PROTO = PROTOFORM = *gárną`, derive the citation-form target `ġearn`, and treat `*garnăn` / `*garna-` only as comparative background explaining the source literature's stem notation. This row is not an `oe_known_problems.tsv` case and not a paradigm-cell workaround.

## Paradigm probe

A paradigm probe is **not required** for this row. The live TSV does not hinge on choosing among competing OE cells: the selected input already yields the intended attested citation form.

If a future appendix wanted a purely explanatory comparison, it could contrast the live nom./acc.sg.-style derivational input `*gárną -> ġearn` with the note's background oblique stem `*garnăn`, but that is not a current blocker and does not require a formal probe table.

## Recommended final report

Recommend a brief final report saying that row 2305 is regular: the project derives attested OE `ġearn/gearn` directly from `*gárną`, while Kroonen's lemma-style `*garna-` and the note's oblique `*garnăn` are comparative background only. It should also note that dotted `ġ` is an editorial normalization and that noun evidence must be kept distinct from homographic verbal `gearn`.

## Data-change recommendations

- **TSV `PROTO`:** no change recommended.
- **TSV `PROTOFORM`:** no change recommended.
- **TSV `COUNTERPART`:** no change recommended.
- **TSV `DERIVATION_CLASS`:** no change recommended.
- **TSV `NOTE`:** **change recommended** — clarify that the live row intentionally derives OE `ġearn` from nominative/accusative-style `*gárną`, while Kroonen's `*garna-` and the note's oblique `*garnăn` are comparative background only. As written, the note can be misread as if the oblique form should feed the derivation.
- **`oe_known_problems.tsv`:** no change recommended.
- **DEV_NOTES / dossier text:** no change recommended. No dedicated dossier for this lexeme was found, and there is no repo-local problem note that needs cleanup beyond clarifying the TSV note itself.
