# Research memo — 1990 dill / dile

## Starting point

- **ID:** 1990
- **CONCEPT:** dill
- **COUNTERPART:** dile
- **PROTO:** `*déljaz`
- **PROTOFORM:** `*déliz`
- **DERIVATION_CLASS:** `early_analogy`
- **NOTE:** I-stem `*deliz` per Kroonen p.93: "evidence for both an i-stem (OE dile) and a ja-stem (OS dilli, OHG tilli)". OE generalized i-stem; OS/OHG generalized ja-stem.

The live TSV already separates the cognate-set headword from the OE derivational input: `PROTO` stays `*déljaz`, but `PROTOFORM` is the OE-facing i-stem `*déliz`. No pilot or full lexeme report exists for this row; the packet is the starting dossier, not final authority.

## Packet evidence assessment

- **Authoritative/current:** the live TSV row; the packet's compact derivation trace showing `*déliz -> dile`; the exact-pair `DEV_NOTES.md` sentinel checks at 38488 and 38518 confirming that `*déliz -> dile` still passes; and the underlying linguistic point that `*deljăz` would give geminate `dill`, not `dile`.
- **Useful background:** the longer `DEV_NOTES.md` discussion at 5809-5920; the packet's pointer to `analysis/dill_stem_class_investigation.md`; and the lexical-table hit `old_english_wiktionary.tsv: dill -> dile`.
- **Stale or superseded:** the packet's preserved problem statements at `DEV_NOTES.md` 5813-5817, where row 1990 still had `*deljăz`; and the standalone analysis file's closing "blocked / waiting for user" status, which predates the implemented TSV change.
- **Irrelevant or misleading:** the packet's lack of a manifest entry is not evidence either way; and broader concept-name hits are methodological background only unless they directly bear on stem class, attestation, or the row's implemented input.

The main packet risk is chronological: it mixes the current row state with pre-fix diagnostics. For this lexeme, packet material is useful only if read against the live TSV and the later implementation notes.

## Additional repo research

Checked beyond the packet:

- `Germanic/docs/DEV_NOTES.md` 5809-5920.
- `Germanic/docs/analysis/dill_stem_class_investigation.md`.
- `Germanic/data/germanic-aligned-final.tsv` row 1990 and neighboring cognate rows.
- `Germanic/data/old_english_wiktionary.tsv`.
- `Germanic/data/oe_known_problems.tsv`.
- `Germanic/docs/lexeme_reports/coverage_audit.md`.
- `docs/references/kroonen_etymological_dictionary_pgmc.vision.txt`.
- `docs/references/fulk_comparative_grammar_early_germanic.vision.txt`.
- `docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt`.
- `docs/references/bosworth_toller_anglo_saxon_dictionary.vision.txt`.
- `docs/references/anglosaxonoldeng00wrig.txt`.
- `docs/references/kluge_seebold_etymologisches_woerterbuch.txt`.
- `docs/references/orel_handbook_germanic_etymology.vision.txt`.

Main findings from that extra pass:

- Wright's vocabularies show both `dili` and `dile` glossing Latin `anetum`, so the repo does have direct OE glossary support for the single-`l` forms.
- Bosworth-Toller has `dile` and addenda `dili, dil`; Clark Hall gives `dile` with a cross-reference from `dill`, and also notes `dyle = dile`.
- Kroonen is the strongest repo-local source for the exact split relevant to this row: OE belongs with an i-stem side, while OS/OHG belong with a ja-stem side, with a deeper proterokinetic explanation available.
- Fulk is useful but not identical to Kroonen: he treats `dili/dile` as evidence that some ja-stems were transferred to the i-stems in OE. That supports the OE i-stem outcome, but it cautions against phrasing the OE form as if it were a simple untouched reflex of a single universal PGmc citation stem.
- No `oe_known_problems.tsv` entry exists, and no existing pilot/full report for this lexeme turned up.

## Reconstruction and early-stage forms

This row needs the standard three-way distinction kept explicit.

1. **Cognate-set proto / etymological headword:** TSV `PROTO` `*déljaz`. In project terms this is the cross-doculect headword shorthand, matching the continental ja-stem side that also suits English/Dutch/German outputs in the aligned set.
2. **Project derivational input:** TSV `PROTOFORM` `*déliz`. This is the OE-specific input actually fed to the cascade so that the row produces `dile`.
3. **OE target form:** `dile`, the Old English form represented by the row.

Kroonen's entry is more nuanced than the bare TSV pair. He prints `*deli- ~ *delja-` and then suggests an older paradigm with nominative `*deliz` and genitive `*duljaz`. That does **not** force the project to replace TSV `PROTO` with a more complex notation, but it does mean the memo and eventual report should avoid flattening everything into "PGmc `*déljaz` directly became OE `dile`". The implemented row is already doing the right project move: keep the wider cognate-set label in `PROTO`, but use the nominative/i-stem side as `PROTOFORM` for Old English.

## Old English philology

The OE side is better supported than the packet alone suggests, but it still needs careful wording.

- `dile` is supported by glossary/dictionary material in the repo's local references.
- `dili` is also attested in the glossary material and matters because it supports an OE i-stem classification or transfer into the i-stems.
- `dyle` is a rarer rounded-vowel variant noted by Kroonen, Kluge-Seebold, and Clark Hall; it should be treated as comparative background, not as the target of row 1990.
- The target `dile` should not be over-described as a dialect-specific form on the basis of the materials checked here. Fulk's wording specifically mentions Corpus Glossary `dili` and early West Saxon accusative singular `dile`, which is useful philological orientation, but the memo stage should still distinguish normalized dictionary citation from particular textual forms.

So the safest formulation is: row 1990 targets a well-supported OE `dile`/`dili` lexeme family with single `l`, and that single `l` is the decisive philological fact for the modelling choice. The row is not about proving one exact manuscript headword spelling to the exclusion of all others.

## Project problem and solution

The project problem was the old mismatch between the cognate-set ja-stem input and the OE target. A direct run from `*deljăz` gives `dill`, because `*-lj-` triggers gemination. The live derivational input `*déliz` yields `dile`, which matches the OE row.

That makes this an `early_analogy` row, not a `late_analogy` paradigm-cell row. The special move happens **before** the OE sound changes modeled by the FST: the project chooses the OE-appropriate stem/input shape, while leaving the wider cognate-set `PROTO` untouched. In other words, row 1990 is not claiming that OE kept the same stem choice as every other daughter language; it is explicitly modelling daughter-language stem divergence.

## Paradigm probe

No paradigm probe is required.

This is not a case where the project must choose among OE inflectional cells such as nominative vs genitive or infinitive vs 3sg. The decisive contrast is upstream stem selection: cognate-set `PROTO` `*déljaz` versus OE derivational `PROTOFORM` `*déliz`. A simple control derivation already shows the point (`deliz -> dile`; `deljăz -> dill`), so there are no missing paradigm cells that need to be probed for the memo stage.

## Recommended final report

Recommend a concise final report that says row 1990 keeps `PROTO = *déljaz` as the cognate-set headword but derives OE `dile` from `PROTOFORM = *déliz`, because the OE evidence supports the single-`l` i-stem side while continental West Germanic generalized the ja-stem side. It should also treat the older `*deljăz -> dile` mismatch discussion as superseded project history, not current evidence.

## Data-change recommendations

- **TSV `PROTO`:** no change recommended. `*déljaz` still works as the project's cognate-set headword shorthand, even though Kroonen's fuller discussion is more complex.
- **TSV `PROTOFORM`:** no change recommended. `*déliz` is the correct implemented OE derivational input.
- **TSV `COUNTERPART`:** no change recommended. `dile` is the right OE target for this row.
- **TSV `DERIVATION_CLASS`:** no change recommended. `early_analogy` is the right classification.
- **TSV `NOTE`:** change recommended. The current note is basically right, but it should say more explicitly that `PROTO` is the cognate-set headword while `PROTOFORM` is the OE-specific input, and it could mention the repo-local `dili/dile` glossary evidence alongside Kroonen.
- **`oe_known_problems.tsv`:** no change recommended.
- **DEV_NOTES/dossier text:** change recommended. `DEV_NOTES.md` should flag the `*deljăz -> dile` wording at 5813-5817 more explicitly as pre-fix diagnostic history, and `Germanic/docs/analysis/dill_stem_class_investigation.md` should be marked as superseded or updated so it no longer ends in a stale "blocked" state after the TSV change was implemented.
