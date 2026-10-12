---
row_id: 2042
concept: god
counterpart: god
proto: '*gúdą'
protoform: '*gúdą'
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
  - Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md
  - Germanic/docs/analysis/notable_findings.md
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2042 god / god

## Current row state

- The live OE row is `2042`, with `CONCEPT = god`, `COUNTERPART = god`, `PROTO = *gúdą`, `PROTOFORM = *gúdą`, and `DERIVATION_CLASS = regular`; the row's note field is empty, so the TSV itself preserves no row-local explanation beyond source/import metadata [Germanic/data/germanic-aligned-final.tsv:434-434].
- `oe_known_problems.tsv` has no entry for row `2042`, for `god`, or for `*gúdą`, so this lexeme is not currently being carried as a live OE exception case [Germanic/data/oe_known_problems.tsv:1-8].
- Coverage tracking still lists `2042 | god | god | regular | no | - | - | - | none`, and `report_manifest.tsv` has no row-2042 report entry. No packet or research memo for this exact row survives, so the preferred filename `2042-god-god.md` is the correct replacement-slice stem [Germanic/docs/lexeme_reports/coverage_audit.md:257-257; Germanic/docs/lexeme_reports/report_manifest.tsv:1-14].
- The published derivation trace is already an exact match: `PROTO: *gúdą`, `EXPECTED: god`, `OUTPUTS: god`, with the compact path `NWGmc U Lowering: *gódą` and `OE Heavy Syllable Nasal Apocope: *gód`, followed by surface `god` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1766-1785].

## Development-note summary

No dedicated row-2042 mini-dossier survives in `DEV_NOTES.md`. The surviving material is thin and uneven: one project-status ledger line says only `Stem-class corrections: god (*gudą), door (dor target vs duru)`, while a much later shared phonology section quotes Campbell to the effect that OE `god` is one of the ordinary examples of NWGmc/early OE `u > o` before a following non-high vowel [Germanic/docs/DEV_NOTES.md:1481-1491,25974-25985].

That means this slice has to function as a replacement working note built from shared but relevant material rather than from a preserved row-specific argument. The safest current claim is modest: the live pipeline now treats `*gúdą > *gódą > god` as regular, and the debug trace confirms that this is exactly what the transducer currently does [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1775-1785]. What does **not** survive is an explicit DEV_NOTES explanation of what earlier `god` “stem-class corrections” changed. The ledger wording should therefore be preserved, but not expanded beyond the evidence.

A further notation distinction should remain explicit. The live row stores accented project notation `*gúdą`, whereas the surviving project-status bullet writes unaccented `*gudą` [Germanic/data/germanic-aligned-final.tsv:434-434; Germanic/docs/DEV_NOTES.md:1489-1489]. In this slice the accented form is the current row metadata; the unaccented form is only the spelling preserved in that historical DEV_NOTES ledger line.

## Relevant DEV_NOTES fragments

The row has no surviving dedicated DEV_NOTES section. The two fragments below are the closest relevant material: one row-local but extremely compressed status note, and one shared phonological discussion that explicitly names `god` as a regular outcome.

### DEV_NOTES:line-1481-1491

- Source label: `DEV_NOTES:line-1481-1491`
- Source heading: `Project Status (as of 2026-04-30) — research phase complete`
- Source line or section hint: `lines 1481-1491`
- Fragment type: `brief_row_local_status_ledger`
- Status: `current_but_underspecified`
- Issue tags: `stem_class_correction`; `historical_cleanup`; `notation_variant`
- Recommended next use: `cite_for_project_history_only_not_for_full_philological_argument`
- Shared with row IDs: `1992`

This is the only plainly row-local surviving DEV_NOTES mention. In the bullet list of "Key recent achievements," DEV_NOTES records: `Stem-class corrections: god (*gudą), door (dor target vs duru)` [Germanic/docs/DEV_NOTES.md:1489-1489]. For row `2042`, that line matters because it shows that `god` had once been important enough to enter the project's correction ledger, and it preserves the lexeme alongside the proto spelling `*gudą`.

What the fragment does **not** do is explain the correction. It does not identify an earlier wrong stem class, an earlier wrong target, or a before/after derivational chain. Since the live row is now `regular` and the published trace already reaches `god`, the most conservative use of this fragment is simply to preserve the historical fact that some earlier `god` classification or alignment issue had been cleaned up by late April 2026 [Germanic/data/germanic-aligned-final.tsv:434-434; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1766-1785]. It should not be treated as if it supplied a full stem-class argument that no longer survives in prose.

### DEV_NOTES:line-25940-25990

- Source label: `DEV_NOTES:line-25940-25990`
- Source heading: `§17.10.34 Cluster: u-lowering "exceptions" (wulf, fugol, bucc, rust, wull) — paradigm-cell switch for 4/5`
- Source line or section hint: `lines 25974-25990, especially the Campbell quotation`
- Fragment type: `shared_current_rule_note`
- Status: `current_but_shared`
- Issue tags: `u_lowering`; `regular_example`; `campbell_quote`; `shared_policy_background`
- Recommended next use: `primary_DEV_NOTES_support_for_why_row_2042_is_now_regular`
- Shared with row IDs: `2030; 2043; 2162; 2298; 2300`

This section is not a row-2042 packet; it is a shared discussion of the five OE forms that keep `u` where the project normally expects lowering. Its value for `god` is that DEV_NOTES preserves Campbell's contrastive statement in full: `u > o before mid and low vowels. In OE forms this change occurs with considerable regularity, e.g. dohtor daughter, god god, gold gold, geoc yoke ...` but `There are, however, many exceptions in OE, which have preserved u ... e.g. full full, fugol bird, bucca buck, wulf wolf ...` [Germanic/docs/DEV_NOTES.md:25974-25985]. For row `2042`, this is the clearest surviving DEV_NOTES authority that `god` belongs on the regular side of the split, not the exceptional side.

The fragment also matters because it shows how the project was reasoning comparatively. The same section is built around forms like `fugol`, `wulf`, and `bucc`, where the FST's lowered `o` output conflicts with attested OE `u`; `god` is invoked precisely as the opposite kind of example, one where the regular lowering is expected and acceptable [Germanic/docs/DEV_NOTES.md:25940-25990]. That shared framing matches the live derivation trace for row `2042`: the transducer lowers `*u` to `*o` in Northwest Germanic, then carries the form through to OE `god` without any extra exception mechanism [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1775-1785].

## Superseded or diagnostic material

- No row-specific narrative section survives that would let us reconstruct the earlier `god` problem in detail. The phrase `Stem-class corrections: god (*gudą)` is therefore best treated as a diagnostic residue of earlier cleanup, not as a self-sufficient analysis [Germanic/docs/DEV_NOTES.md:1489-1489].
- The live debug trace is useful operational evidence, but it is not itself DEV_NOTES prose. Its main diagnostic value is to show the current implemented path `*gúdą > *gódą > god`, which is consistent with Campbell's regular-example treatment and with the row's present `regular` classification [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1766-1785].
- `analysis/notable_findings.md` repeats the same Campbell quotation, including `god god` among the regular examples [Germanic/docs/analysis/notable_findings.md:364-374]. That file is useful as cross-checking background, but for this row it does not materially exceed the DEV_NOTES fragment from which it is derived.
- Because no packet, research memo, or dossier survives for row `2042`, this slice necessarily carries more uncertainty about project history than slices for rows with preserved pilot reports. That uncertainty should be stated plainly rather than hidden behind confident retroactive reconstruction [Germanic/docs/lexeme_reports/coverage_audit.md:257-257; Germanic/docs/lexeme_reports/report_manifest.tsv:1-14].

## Open questions for later work

- If an older packet or pre-slice memo for `god` is ever recovered outside the current surviving report set, the first question should be what exactly the April 2026 `stem-class corrections` bullet meant for this lexeme: protoform normalization, inflectional-class reassignment, target cleanup, or some narrower data-alignment fix [Germanic/docs/DEV_NOTES.md:1489-1489].
- Any later fuller report should keep the distinction between live row metadata `*gúdą` and the ledger's unaccented `*gudą` explicit. The two spellings are close, but they are not identical documentary objects in the repo [Germanic/data/germanic-aligned-final.tsv:434-434; Germanic/docs/DEV_NOTES.md:1489-1489].
- If later documentation expands the shared NWGmc `u > o` discussion, row `2042` should remain attached to the regular set with comparators like `gold`, not be presented as if it still needed the same kind of exception handling as `wulf` or `fugol` [Germanic/docs/DEV_NOTES.md:25974-25990; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1766-1785].
