# Research memo — 1981 craft / cræft

## Starting point

- **ID:** 1981
- **CONCEPT:** craft
- **COUNTERPART:** cræft
- **PROTO:** `*kráftiz`
- **PROTOFORM:** `*kráftaz`
- **DERIVATION_CLASS:** `early_analogy`
- **NOTE:** `Kroonen: *kraftu- m. 'strength' (u-stem); Orel: *kraftiz ~ *kraftuz. OE cræft has æ (not e), ruling out i-stem *-iz which would trigger i-umlaut. Using a-stem *kraftăz.`

The live row already encodes the key project distinction: `PROTO` preserves a cognate-set headword, while `PROTOFORM` is the pre-OE input actually fed to the cascade. A pilot report exists at `Germanic/docs/lexeme_reports/pilot/craft.md`, but it is background only, not final authority.

## Packet evidence assessment

**Authoritative/current:**
- The aligned TSV row is current project data.
- The packet's compact derivation trace is current in substance: the live FST still supports `*kráftaz -> cræft`.
- The row-specific `DEV_NOTES.md` section on PGmc stem-class disagreement and the matching summary in `analysis/notable_findings.md` remain the strongest repo-local explanations of the problem.
- `old_english_wiktionary.tsv` is modest but current confirmation that the OE headword is `cræft`.

**Useful background:**
- `pilot/craft.md` is useful as a concise prior synthesis, especially because it already separates `PROTO` from `PROTOFORM`.
- The packet's bibliography-key suggestions are useful for later report drafting.
- The manifest/coverage notices are useful only to show that this row is already in pilot coverage.

**Stale or superseded:**
- The packet preserves an older `DEV_NOTES` recommendation to change both `PROTOFORM` and `PROTO` to an a-stem. That is no longer the best reading of the live row: the current project state deliberately keeps the cognate-set proto separate from the modelling input.
- Regression snippets such as `kraftăz -> craft (should be cræft)` are diagnostic implementation history, not lexical authority.
- Several packet hits are broad `i-umlaut` keyword matches from unrelated analyses and dossiers; they are not row-specific evidence.

**Irrelevant or misleading:**
- The packet's concept-name snippets can blur philology if read incautiously. In particular, the `DEV_NOTES` table line glossing Kroonen with `"OE craft"` is not safe as direct spelling evidence: the repo's Kroonen extract actually has `OE cræft`, while Orel normalizes `craft`.
- The packet's unrelated dossier hits about other umlaut problems do not materially bear on row 1981.

## Additional repo research

Checked beyond the packet:
- `Germanic/docs/DEV_NOTES.md`
- `Germanic/docs/analysis/notable_findings.md`
- `Germanic/docs/lexeme_reports/pilot/craft.md`
- `Germanic/docs/lexeme_reports/report_manifest.tsv`
- `Germanic/docs/lexeme_reports/coverage_audit.md`
- `Germanic/data/old_english_wiktionary.tsv`
- `docs/references/kroonen_etymological_dictionary_pgmc.vision.txt`
- `docs/references/orel_handbook_germanic_etymology.vision.txt`
- `docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt`
- `docs/references/bosworth_toller_anglo_saxon_dictionary.vision.txt`
- `docs/references/luick_historische_grammatik.txt`
- live FST artifacts `backend/old_english.bin` and `Germanic/fsts/old_english.bin` via the repo's `oe_full_trace_report` helpers

Main findings from that extra pass:
- The live FST confirms the three-way comparator that matters here: `*kráftiz -> creft`, `*kráftuz -> craft`, and `*kráftaz -> cræft` in both authoritative bins.
- Kroonen's repo text gives `*kraftu- m.` with `OE cræft m.`; Orel gives `*kraftiz *kraftuz` with normalized `OE craft`; the comparative disagreement is real.
- `Clark Hall` and `Bosworth-Toller` both support the OE headword `cræft`; `Clark Hall` also gives it as masculine and glosses it as strength / might / skill.
- `Luick` explicitly lists `cræft` and `cræftas` among OE `æ` examples, which supports the anti-i-umlaut argument and the philological reality of the OE vowel.

## Reconstruction and early-stage forms

This row needs a strict three-way distinction.

1. **Cognate-set proto:** TSV `PROTO = *kráftiz` is functioning as the row's comparative headword shorthand, not as a claim that pre-OE necessarily still had an i-stem ending. Repo sources themselves disagree between u-stem and i/u-stem analyses.
2. **Project input form used for derivation:** TSV `PROTOFORM = *kráftaz` is the modelling choice for the OE run. The live cascade shows that this input alone gives the target `cræft`; the i-stem gives `creft`, and the u-stem comparator gives `craft`.
3. **OE target form:** `cræft` is the attested Old English lemma represented by the row.

So the project should not be read as proving that Proto-Germanic was definitely an a-stem. The narrower and safer claim is that the pre-OE stage fed to the English derivation must have lacked both the i-umlaut trigger of `*-iz` and the surviving back-vowel trigger that would yield `craft` under a u-stem analysis.

## Old English philology

`cræft` is an attested OE citation form, not a reconstructed paradigm cell and not a dialect-smoothing convenience form. The repo's lexical materials support that straightforwardly:
- `old_english_wiktionary.tsv`: `craft | cræft`
- `Clark Hall`: `cræft m. physical strength, might, courage ... skill, art`
- `Bosworth-Toller`: headword `cræft`
- `Luick`: `cræft` and `cræftas` as `æ` examples

The philological issue is therefore not attestation but prehistory. Nothing in the repo materials requires a special dialect or manuscript claim for this row. The safe statement is simply that OE `cræft` with `æ` is the target, and that this vowel is incompatible with a straightforward inherited i-stem citation-form input.

The later English form `craft` with `a` should not be projected back onto OE. It is later history, not evidence against the OE headword.

## Project problem and solution

The project problem was that a direct citation-style i-stem input produced the wrong OE vowel (`creft`). The current row's solution is the right type of solution: keep the comparative headword visible in `PROTO`, but feed the FST with an early analogical / pre-OE modelling input `*kráftaz` in `PROTOFORM`.

That means row 1981 should be understood as an `early_analogy` case, not as a late OE paradigm-cell substitution and not as proof that the comparative dictionaries have been definitively overruled. The row models the OE outcome by separating etymological headword from derivational input.

## Paradigm probe

No paradigm probe is required.

This is not a `late_analogy` case where the project needs to choose among OE inflectional cells such as nominative versus genitive or dative. The decisive contrast is upstream stem-class/input selection, and the live comparator run `*kráftiz / *kráftuz / *kráftaz` already answers that question. If a future appendix wants an illustrative control table, those three citation-style comparators are enough; no missing OE paradigm cells need to be probed for the memo stage.

## Recommended final report

Recommend a concise final report stating that OE `cræft` is the attested target, that comparative sources disagree on the cognate-set stem class, and that the project therefore keeps `PROTO` as comparative background while using `PROTOFORM = *kráftaz` as the pre-OE modelling input because it is the only comparator that yields regular `cræft` in the live FST.

## Data-change recommendations

- **TSV `PROTO`: no change recommended.** Keep `*kráftiz` as the cognate-set headword shorthand, but do not treat it as the direct pre-OE input.
- **TSV `PROTOFORM`: no change recommended.** `*kráftaz` is the right project input for the OE derivation.
- **TSV `COUNTERPART`: no change recommended.** `cræft` is the correct OE target.
- **TSV `DERIVATION_CLASS`: no change recommended.** `early_analogy` correctly describes the row.
- **TSV `NOTE`: change recommended.** Revise the wording so it explicitly distinguishes comparative stem-class disagreement from the modelling choice: Kroonen's u-stem and Orel's i/u-stem belong to the cognate-set discussion, while `*kráftaz` is the project's pre-OE input because the live FST gives `creft`, `craft`, and `cræft` for the i-, u-, and a-stem comparators respectively.
- **`oe_known_problems.tsv`: no change recommended.** This row does not belong there in its current early-analogy treatment.
- **`DEV_NOTES` / dossier text: change recommended.** Annotate or clean the 2026-03-09 `DEV_NOTES` section so it no longer implies that the live solution should rewrite `PROTO` itself to an a-stem, and so its Kroonen summary does not get reused as if `"OE craft"` were the precise philological form. No separate dossier text change is required beyond that cleanup.
