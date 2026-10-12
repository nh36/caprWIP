---
row_id: 1977
concept: climb
counterpart: climban
proto: "*klímbaną"
protoform: "*klímbaną"
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files: []
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 1977 climb / climban

## Current row state

- The live Old English row currently reads `CONCEPT = climb`, `COUNTERPART = climban`, `PROTO = *klímbaną`, `PROTOFORM = *klímbaną`, and `DERIVATION_CLASS = regular`; the row carries only inherited-etymology provenance rather than a row-local explanatory note [Germanic/data/germanic-aligned-final.tsv:179-179].
- The repo's OE source import agrees with that live row state: `old_english_wiktionary.tsv` also gives `climb\tclimban\tinh\ttemplate:inh\tclimb`, so there is no in-repo counterpart split or alternate OE stem to reconcile for this lexeme [Germanic/data/old_english_wiktionary.tsv:43-43].
- Existing report infrastructure is still absent. `coverage_audit.md` lists row `1977` as `| 1977 | climb | climban | regular | no | - | - | - | none |`, which is consistent with the present lack of any row-specific packet, research memo, or attached dossier/analysis file to link in metadata [Germanic/docs/lexeme_reports/coverage_audit.md:216-216].
- `oe_known_problems.tsv` contains only unrelated OE exception rows at present, so row `1977` is not being tracked as an open OE exception bucket or known-problem item [Germanic/data/oe_known_problems.tsv:1-8].
- The published OE derivation snapshot already lands exactly on the live target with no repair step: `PROTO: *klímbaną`, `EXPECTED: climban`, `OUTPUTS: climban`, with OE-side stages `Heavy Syllable Nasal Apocope: *klímban`, `Secondary Nasalization: *klímbąn`, and `Weak Tail Reduction: *klímban` before surface `climban` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:694-712].

## Development-note summary

DEV_NOTES support for row `1977` is real but very thin, and the thinness itself needs to be preserved rather than papered over. No lexeme-specific `climban` dossier, repair narrative, or target-selection dispute was located in `Germanic/docs/DEV_NOTES.md`. The only materially relevant surviving passage is a shared Class III strong-verb discussion in which Campbell's paradigm list includes `climban climb` among ordinary Old English verbs of the class [Germanic/docs/DEV_NOTES.md:7074-7082].

That surviving passage is useful, but only in a narrow way. DEV_NOTES quotes Campbell's Class III paradigm as `"bindan, bind — band, bond — bundon — bunden ... springan spring, climban climb..."` and then immediately turns to the special OE history of `findan/funde` [Germanic/docs/DEV_NOTES.md:7076-7082]. For row `1977`, the transferable substance is simply that `climban` is being treated as an ordinary OE Class III strong verb. The follow-on discussion about generalized `d` and `funde` is not a hidden argument about `climban`; it belongs to the neighboring `findan` problem and should not be back-projected onto this row [Germanic/docs/DEV_NOTES.md:7081-7111].

Because the DEV_NOTES support is so limited, the safest replacement note is conservative. It should say explicitly that row `1977` does **not** currently preserve a row-local project controversy. What the repo does preserve is a regular, internally consistent picture: live TSV and OE import both give `climban`; DEV_NOTES treats `climban` as a normal Class III comparator; Ringe-Taylor likewise list `*klimban 'to climb' > OE *climban (past clam, pl. clumbon)`; and Clark Hall has the dictionary headword `climban` [Germanic/data/germanic-aligned-final.tsv:179-179; Germanic/docs/DEV_NOTES.md:7074-7082; docs/references/ringe_taylor_linguistic_history_vol2.txt:7537-7538; docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:9219-9219].

The practical conclusion is therefore mostly negative but still important for later reporting. This row currently looks like a genuine no-drama regular item: exact live derivation, no exception-bucket status, no memo infrastructure, and only a small amount of shared DEV_NOTES support. That is enough to justify a replacement working note, but probably not enough by itself to justify treating row `1977` as an index anchor unless later work adds a more lexeme-specific memo or a wider Class III dossier [Germanic/docs/lexeme_reports/coverage_audit.md:216-216; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:694-712].

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-7074-7082

- Source heading: `The Levelling Chronology`
- Source line or section hint: `lines 7074-7082`
- Fragment type: `shared_family_background_with_explicit_lexeme_hit`
- Status: `current`
- Issue tags: `class_iii_strong_verb`; `explicit_climban_hit`; `family_context`
- Recommended next use: `cite_if_explaining_why_row_is_treated_as_ordinary_class_iii`
- Shared with row IDs:

This is the only clearly attachable DEV_NOTES fragment for row `1977`, so it should be preserved almost verbatim and also handled carefully. DEV_NOTES says: `**Campbell (1959) §741** describes the OE Class III paradigm`, then quotes: `"bindan, bind — band, bond — bundon — bunden / Similarly many verbs, e.g. drincan drink, gelimpan happen, grindan grind, / springan spring, climban climb..."` [Germanic/docs/DEV_NOTES.md:7074-7079].

For `climban`, the value of the fragment is classificatory rather than problem-solving. It shows that the project's live notes treat `climban` as part of the ordinary OE Class III strong-verb pattern, not as a target under special repair, analogical substitution, or exception handling [Germanic/docs/DEV_NOTES.md:7074-7082]. That is enough to support the row's current regular status, but not enough to invent a thicker lexeme-specific history than the repo actually preserves.

## Superseded or diagnostic material

- No superseded row-specific DEV_NOTES analysis was located for `climban`. The absence matters: current project history does not preserve an earlier alternate target, alternate protoform, or exception-handling phase for row `1977` [Germanic/docs/lexeme_reports/coverage_audit.md:216-216; Germanic/docs/DEV_NOTES.md:7074-7082].
- The surrounding DEV_NOTES prose after the Campbell quote is **diagnostic/background only** for this row. Those lines explain the special levelling history of `findan` (`d` throughout, pret. sg. `funde`, preference for a regular voiced paradigm cell), but that is a neighboring argument, not a `climban` argument [Germanic/docs/DEV_NOTES.md:7081-7111].
- The published derivation trace is also diagnostic rather than DEV_NOTES authority. Its value is implementation-facing: it shows that the current OE cascade already derives `climban` exactly from `*klímbaną` without any row-local workaround [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:694-712].

## Open questions for later work

- If later lexeme-report curation considers row `1977` for `index.tsv`, decide whether a single shared Class III DEV_NOTES fragment is enough to make the row index-worthy, or whether it should stay effectively no-index until a more lexeme-specific memo exists.
- If a future Class III strong-verb family memo is written, attach `climban` there explicitly with its ordinary paradigm comparators (`bindan`, `springan`, `swimman`, etc.), since the surviving DEV_NOTES support is classificatory rather than row-local [Germanic/docs/DEV_NOTES.md:7074-7079; docs/references/campbell_old_english_grammar.txt:20784-20788].
- If later OE phonology or morphology work revisits `-mb-` verbs or strong-verb paradigm reporting, keep row `1977` as a useful control item: current repo evidence consistently treats it as a straightforward regular reflex with no exception status [Germanic/data/germanic-aligned-final.tsv:179-179; Germanic/data/oe_known_problems.tsv:1-8; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:694-712].
