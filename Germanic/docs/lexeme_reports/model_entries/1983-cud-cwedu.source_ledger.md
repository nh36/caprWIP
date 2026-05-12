# Source extraction ledger — cud / cwedu

This ledger records the evidence used for the P3 rewrite from pilot material.

| Source | Form(s) given | Claim relevant to the entry | Citation key available? | Where this claim was found locally | Confidence / review note |
| :--- | :--- | :--- | :--- | :--- | :--- |
| TSV row 1983 and compact trace | `PROTO *kwíθuz`; `PROTOFORM *kwéðuz`; `*kwéðuz -> cwedu` | Establish the live selected input and the stale lexeme-level proto metadata that was not changed in this pass. | no | `Germanic/data/germanic-aligned-final.tsv`; `Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.compact.md` | high |
| Pilot report and research memo | `cwedu`; `cwidu`; `cweodu`; `cwudu`; `cudu` | Confirm that the row is an attested-variant choice rather than a paradigm-cell rescue. | no | `Germanic/docs/lexeme_reports/pilot/cud.md`; `Germanic/docs/lexeme_reports/research_memos/1983-cud-cwedu.md` | high |
| Kroonen; Orel | `*kwedu-2`; OE `cwidu`, `cweodu`, `c(w)udu` | Supply the comparative proto and the wider OE variant family. | yes — `Kroonen2013`; `Orel2003` | local vision-backed comparative dictionary files; memo | high |
| Ringe and Taylor | `cwidu`; `cwudu`; `cudu`; `cweodu`; `cwidwes` | Supplies the variant chain and u-stem support. | yes — `RingeTaylor2014` | local grammar file; memo | high |
| Clark Hall | `cwudu`; `cweodu`; `cudu` | Confirms the Old English lexical family in dictionary form. | yes — `ClarkHall1960` | local dictionary file; memo | high |

## Citation-locator pilot 01 note

- Verified page locators in the local reference files for `Kroonen2013` (p. 355),
  `Orel2003` (p. 266), `RingeTaylor2014` (p. 338), and `ClarkHall1960`
  (p. 84).
- Updated the paired model entry to use page-specific Pandoc locators for those
  source-specific claims.

## Notes

- The live TSV `PROTO` field is stale (`*kwíθuz`) relative to the current analysis, but the user explicitly asked for review-or-upgrade work without TSV edits; the stale metadata is therefore recorded here and in the implementation report, not corrected in this pass.
- Existing local vision-backed reference files were sufficient; no additional Google Vision rescue was needed.
- No OCR or encoding artifact was reproduced in final prose.
