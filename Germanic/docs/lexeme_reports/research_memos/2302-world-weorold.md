# Research memo — 2302 world / weorold

## Starting point

- **ID:** 2302
- **CONCEPT:** world
- **COUNTERPART:** weorold
- **PROTO:** *wíra-àldiz
- **PROTOFORM:** *wír-àldu
- **DERIVATION_CLASS:** early_analogy
- **NOTE:** current note says the input keeps PIE-root *i and derives `weorold` by NWGmc i-lowering, inter-stress raising, back mutation, medial `u > o`, and apocope, but it also says “PROTO *weraldiz is etymological headword,” which no longer matches the live `PROTO` field.

This is therefore a row where the live TSV, the packet, and older DEV_NOTES history need to be kept separate.

## Packet evidence assessment

**Authoritative/current**

- The live TSV row and the packet’s compact derivation trace are current evidence for the project’s present row state: `PROTO *wíra-àldiz`, `PROTOFORM *wír-àldu`, target `weorold`.
- The packet’s “none” result for `oe_known_problems.tsv` is current and important: this row is not being treated as an unmodelled exception.

**Useful background**

- The packet’s DEV_NOTES excerpt at 16913ff is useful background on the lexeme’s comparative history: compound structure, ō-stem shift, `*weraldiz > *weraldu > *weruld`, and the OE variant set `weorold ~ worold / weoruld / woruld / wiarald` [@RingeTaylor2014; @Campbell1959; @SieversBrunner1965].
- The analysis and dossier hits are also useful background, especially for dialectal distribution and the special behaviour of back mutation after initial `w`.

**Stale or superseded**

- DEV_NOTES 17149ff (`*wer-uldu`) and 17175ff (`*wer-oldu`) are superseded project-history states. They record earlier transponent choices before later work on `OEInterStressRaising`, later rule ordering, and the acute/grave notation migration.
- The packet’s reuse of those excerpts is diagnostic, not current authority.
- The live TSV note’s clause “PROTO *weraldiz is etymological headword” is itself stale relative to the current TSV `PROTO`.

**Irrelevant or misleading**

- The packet’s older “milk problem” hit using Modern English **world** is not evidence for this row’s reconstruction; it is only a passing analogy.
- The packet should not be read as if every `weorold`/`woruld` mention were evidence for the exact current row settings.

## Additional repo research

Checked beyond the packet:

- `Germanic/docs/DEV_NOTES.md` (especially 16913–17932, 23393–23472, 27740–28000)
- `Germanic/docs/analysis/ws_vs_anglian_dialect_differences.md`
- `Germanic/docs/dossiers/widuwe-u-preservation.md`
- `docs/references/ringe_taylor_linguistic_history_vol2.txt`
- `docs/references/campbell_old_english_grammar.txt`
- `docs/references/brunner_1965_altenglische_grammatik.txt`
- `docs/references/kluge_seebold_etymologisches_woerterbuch.txt`
- `docs/references/orel_handbook_germanic_etymology.vision.txt`
- `docs/references/seebold_vergleichendes_woerterbuch.txt`
- `docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt`
- `docs/references/bright_anglo_saxon_reader.txt`

No pilot lexeme report for this lexeme is present in `docs/lexeme_reports/pilot/`.

Repo-local verification against `backend/old_english.bin` confirms that the current project input `*wír-àldu` yields `weorold`, and that the older transponents `*wer-uldu` and `*wer-oldu` also yield `weorold`; by contrast `*wir-uldu` does not. That matters because it shows that the older `*wer-...` solutions are no longer required by the live FST.

## Reconstruction and early-stage forms

Three levels must be kept distinct.

1. **Cognate-set proto / etymological comparative form.** The live cogset uses `*wíra-àldiz`, matching comparative sources that preserve the older `*wir-` element in the compound, e.g. Orel `*wira-aldiz` and Kluge-Seebold `*wira-aldō`, even though Kluge also gives simplex `*wera-` [@Orel2003; @KlugeSeebold2011].
2. **Lowered comparative/pre-OE stage discussed in the literature.** Ringe–Taylor discuss the word as `*weraldiz > *weraldu > *weruld`, i.e. with lowered `e` in the root and a pre-OE ō-stem stage [@RingeTaylor2014]. This is strong comparative background, but it is not the same thing as the row’s current `PROTOFORM`.
3. **Project input form.** The live `PROTOFORM` `*wír-àldu` is the project’s OE-directed transponent: it already encodes the analogical ō-stem shift (`-u`) and the syncopated compound shape used by the OE pipeline, while still leaving i-lowering, inter-stress raising, back mutation, medial `u > o`, and apocope to the FST.

So `*weraldiz` is best treated here as a comparative/literature stage, not as the row’s sole authoritative `PROTO`; and the older project transponents `*wer-uldu` / `*wer-oldu` should be treated as superseded implementation history.

## Old English philology

The OE target is not a singleton form. Repo sources give a cluster of attested variants:

- WS `weorold ~ worold` (R/T; Brunner)
- forms with `u` in the second syllable, especially `weoruld / woruld`
- Northumbrian `world`
- Kentish `wiarald` [@RingeTaylor2014; @Campbell1959; @SieversBrunner1965]

This means:

- `weorold` is a defensible attested OE target, especially as a WS-type surface form.
- It should not be described as the only OE form or the only dictionary headword. Clark Hall and Bright group it under a broader `woruld / worold / weoruld / world` variant set, and Brunner likewise lists `worold, woruld, weorold, world`.
- The final report should therefore present `weorold` as the project’s selected OE target form, while explicitly acknowledging the wider variant cluster.

## Project problem and solution

The project problem is not a missing paradigm cell; it is a lexeme-level staging problem.

- Comparative evidence points to a compound ‘age of men’ with older `*wir-`/`*wira-` etymology.
- The OE outcome requires an analogical ō-stem stage plus regular OE developments.
- Earlier project history solved this by feeding pre-lowered/pre-raised transponents such as `*wer-uldu`.
- Later work implemented `OEInterStressRaising`, removed the unsupported direct `*i > eo` back-mutation shortcut, and showed that the project can now use `*wir-aldu` and later prosodically marked `*wír-àldu` while still deriving `weorold`.

The live row therefore makes sense as:

- **PROTO:** cognate-set/etymological `*wíra-àldiz`
- **PROTOFORM:** project OE input `*wír-àldu`
- **OE target:** selected attested form `weorold`

`DERIVATION_CLASS = early_analogy` is still the right label, because the crucial non-regular step is the early stem-class reassignment to the ō-stem; the later steps are now treated as regular phonology within the project.

## Paradigm probe

A paradigm probe is **not required** for this memo.

Reason: this is not a late-analogy or cell-selection case where the project depends on choosing one inflected cell over another. The issue is lexeme-level reconstruction and pipeline staging. If a future review nevertheless wants a probe, the useful cells would be nominal citation-form singular comparanda for the i-stem vs ō-stem analyses, not a late-analogy oblique-cell test.

## Recommended final report

The final `### Lexeme report` should be concise and source-led. It should:

- state that `weorold` is the project’s selected OE target within a broader OE variant set;
- distinguish current `PROTO *wíra-àldiz` from current `PROTOFORM *wír-àldu`;
- mention Ringe–Taylor’s `*weraldiz > *weraldu > *weruld` as comparative background, not as the live TSV setting;
- identify the ō-stem shift as the early analogical step that motivates the row.

## Data-change recommendations

- **TSV `PROTO`:** **no change recommended**. Keep `*wíra-àldiz` as the live cognate-set proto unless the whole cognate set is centrally retargeted.
- **TSV `PROTOFORM`:** **no change recommended**. Keep `*wír-àldu`; it matches the current pipeline and current later DEV_NOTES history.
- **TSV `COUNTERPART`:** **no change recommended**. `weorold` is attested and usable as the row’s selected OE target, though the final report must acknowledge `worold / weoruld / woruld / world`.
- **TSV `DERIVATION_CLASS`:** **no change recommended**. `early_analogy` still fits.
- **TSV `NOTE`:** **change recommended**. Rewrite it so it no longer says “PROTO *weraldiz is etymological headword.” The note should instead distinguish: current cognate-set `PROTO *wíra-àldiz`, current project input `PROTOFORM *wír-àldu`, and literature-stage lowered `*wer-...` forms as background only.
- **`oe_known_problems.tsv`:** **no change recommended**.
- **`DEV_NOTES` text:** **cleanup recommended**. Add or revise a brief status note so the older `*wer-uldu` / `*wer-oldu` sections are clearly marked as superseded by the later `*wír-àldu` solution.
- **Dossier text:** **no change recommended**. The cited dossier material is general phonological background, not row-specific stale data.
