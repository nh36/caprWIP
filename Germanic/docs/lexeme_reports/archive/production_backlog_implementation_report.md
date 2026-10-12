# Production backlog implementation report

## Files inspected

- `Germanic/docs/CANONICAL_STATE.md`
- `Germanic/docs/lexeme_reports/coverage_audit.md`
- `Germanic/docs/lexeme_reports/report_schema.md`
- `Germanic/docs/lexeme_reports/report_manifest.tsv`
- `Germanic/docs/lexeme_reports/packets/`
- `Germanic/docs/lexeme_reports/dev_notes_slices/`
- `Germanic/docs/lexeme_reports/research_memos/`
- `Germanic/data/germanic-aligned-final.tsv`

## Files created

- `Germanic/docs/lexeme_reports/production_backlog.md`
- `Germanic/docs/lexeme_reports/production_backlog.tsv`
- `Germanic/docs/lexeme_reports/production_backlog_implementation_report.md`

## Counts extracted

- Total OE rows with real counterpart: **380**
- Rows requiring lexeme report: **148**
- Manifest-backed production reports: **11**
- Source material available but no manifest-backed production report: **136**
- No source material found: **1**
- Regular rows with empty NOTE outside the production-report requirement: **232** (this total includes the separately tracked format-test manifest entry)

## Chosen model-entry candidates

- `2183` shoulder / sċuldrum: Late-analogy dat.pl. case with the richest packet in the backlog; best single stress test for paradigm-cell handling and schema discipline.
- `1980` cow / cȳ: Clean root-noun oblique-cell case with a dedicated analysis dossier; strong late-analogy candidate with manageable scope.
- `2053` hammer / hameres: Gen.sg. oblique-form solution with attested hamor/hamer alternants; ideal for distinguishing citation proto from FST input.
- `1958` both / bū: Regular row but unusually rich lexical note; tests how the final prose separates OE evidence, ModE headword history, and project-specific note history.
- `2302` world / weorold: Early-analogy compound/transponent case with a clear PROTO vs PROTOFORM split; good model for explaining compound-specific inputs without reopening phonology.

## Proposed 10-entry pilot batch

- `2183` shoulder / sċuldrum — late_analogy; exception agent: yes; Dat.pl. paradigm-cell case with explicit packet evidence and a real paradigm-probe requirement; strongest late-analogy stress test.
- `1980` cow / cȳ — late_analogy; exception agent: maybe; Root-noun oblique-cell solution with explicit dat.sg. evidence and a dedicated analysis memo; good contrast with shoulder.
- `2027` follow / fylġan — early_analogy; exception agent: no; Clear Class II citation vs Class I inherited-form split with a well-documented Mercian/Northumbrian target.
- `2296` withy / wīþiġ — early_analogy; exception agent: no; Suffix-etymology correction from *-ijaz to *-agą gives a rich but bounded early-analogy case for the pilot batch.
- `1958` both / bū — regular; exception agent: no; Regular row with dense note/history content; useful for testing concise schema-conformant prose on a non-analogical but philologically messy entry.
- `2095` learn / liornian — regular; exception agent: maybe; Regular row with dialectal selection and ablaut-grade discussion; good test of how much philology a regular report should retain.
- `2273` wasp / wæfs — attested_variant; exception agent: no; Strong attestation dossier for retargeting to the earliest OE form; ideal attested-variant pilot.
- `2087` knob / cnobba — reconstructed_oe; exception agent: maybe; Compact reconstructed-OE case with explicit unattested-status note and a bounded supporting argument.
- `2300` wool / wull — unexplained_unmodelled; exception agent: maybe; Documented exception with no plausible paradigm escape route; useful pilot for the “genuine exception” write-up style.
- `2013` fire / fȳre — manifest_pilot_benchmark; exception agent: no; Existing manifest-backed pilot report to review as a style benchmark before promoting any new entries to production prose.

## Uncertainties / human-review points

- `2055 handle / handlian` is the sole P0 row in the audit, but the audit currently attaches handle-named packet/slice/memo files to adjacent row `2054 hand`. This should be checked before drafting the handle report.
- `2013 fire / fȳre` is included as a style benchmark only. It should be reviewed against the current schema and citation/detail expectations rather than treated as the automatic final template.
- Some older packets (for example `2004 fast / festan`) preserve intermediate research states inside supporting excerpts. The backlog does not treat those packets as authoritative prose; any future drafting pass should re-check them against the canonical compact trace and current row data.

## Scope confirmation

- No TSV data rows were edited.
- No FST rules or tooling were changed.
- No manifest statuses were edited.
- No pilot/full production report content was edited.
- This pass only created planning/indexing documents for the lexical write-up phase.
