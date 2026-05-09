# Model entry implementation report — 2183 shoulder / sċuldrum

## Files inspected

- `Germanic/docs/CANONICAL_STATE.md`
- `Germanic/docs/lexeme_reports/report_schema.md`
- `Germanic/docs/lexeme_reports/production_backlog.md`
- `Germanic/docs/lexeme_reports/production_backlog.tsv`
- `Germanic/docs/lexeme_reports/packets/2183-shoulder-sċuldrum.md`
- `Germanic/docs/lexeme_reports/dev_notes_slices/2183-shoulder-sċuldrum.md`
- `Germanic/docs/lexeme_reports/research_memos/2183-shoulder-sċuldrum.md`
- `Germanic/docs/dossier-shoulder-2026.md`
- `Germanic/docs/dossier-shoulder-paradigm-survey-2026.md`
- `Germanic/docs/DEV_NOTES.md` (especially §17.41 and the later implementation log)
- `Germanic/data/germanic-aligned-final.tsv` (row 2183)
- `Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.compact.md`
- `docs/refs.bib`

## Files created

- `Germanic/docs/lexeme_reports/model_entries/2183-shoulder-sċuldrum.model.md`
- `Germanic/docs/lexeme_reports/model_entries/2183-shoulder-sċuldrum.model_implementation_report.md`

## Source hierarchy used

- **Primary current data:** the live TSV row, the compact derivation trace, the report schema, and the shoulder packet.
- **Research rationale:** the shoulder dev-note slice, the shoulder research memo, the main shoulder dossier, the paradigm-survey dossier, and current §17.41 material in `DEV_NOTES.md`.
- **Historical material used only as labeled background:** the superseded `*skúldru -> sċuldor` detour inside the later §17.41 history. It was mentioned only because it remains a serious discarded alternative, not as current row policy.

## Drafting decisions

- The model entry treats `PROTO = *skuldrō` as the **cognate-set headword** and `PROTOFORM = *skúldramiz` as the **row-specific FST input**. This distinction is central to the draft because the lexeme's literature and the project history do not agree on a single stem-class label.
- The report treats `sċuldrum` as an **attested inflected target**, not as a reconstructed form and not as the ordinary lemma. The ordinary lemma `sculdor` and the weak-feminine `sċuldra` are both discussed in the philology section, but the row is explicitly framed as an inflected-cell entry.
- The report keeps the superseded `*skúldru -> sċuldor` route in view as a serious alternative considered by the project, but it does not present it as the live solution.
- The `late_analogy` label is justified in terms of the lexeme's analogically disturbed singular history, even though the chosen dative-plural cell itself is treated as a regular inherited pathway.
- The `Paradigm probe` section summarizes the already completed conceptual probe work from the shoulder paradigm survey instead of pretending that a new automated probe was run in this pass.

## Bibliography keys used in the model entry

- `Kroonen2013`
- `Orel2003`
- `RingeTaylor2014`
- `Campbell1959`
- `Fulk2018`
- `Hogg1992`
- `SieversBrunner1965`
- `BosworthToller1898`
- `ClarkHall1960`

## Review-sensitive points

- The draft currently keeps the technical `*-amiz` rationale fairly concise in the main prose. If Nathan wants the model entry to carry more of that suffix-history argument directly, the most likely expansion point is the end of `#### Reconstruction and early-stage alternatives`.
- The draft includes the superseded `*skúldru -> sċuldor` alternative because it is a real part of the row's project history. If that feels too historical for the final production style, this is the first place to trim.
- The draft does **not** cite repo file paths inside the model entry itself except implicitly through project-language phrases such as "the shoulder dossiers" and "the current §17.41 material." That was intentional to keep the model closer to publication prose.
- No reusable automated shoulder probe exists yet. The draft therefore states the current probe result and the remaining tooling gap explicitly, rather than pretending the gap does not exist.

## Scope confirmation

- No TSV rows were edited.
- No FST files were edited.
- No derivation traces were edited.
- `report_manifest.tsv` was not changed.
- No existing production reports, packets, slices, or research memos were modified.
- This pass only drafted the new model-entry file and its implementation report.
