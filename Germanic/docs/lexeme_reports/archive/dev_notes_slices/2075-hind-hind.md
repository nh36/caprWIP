---
row_id: 2075
concept: hind
counterpart: hind
proto: *xéndjō
protoform: *xéndjō
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file: Germanic/docs/lexeme_reports/packets/2075-hind-hind.md
linked_research_memo_file: Germanic/docs/lexeme_reports/research_memos/2075-hind-hind.md
linked_dossier_or_analysis_files:
  - Germanic/docs/germanic_transducer_report.md
  - Germanic/docs/germanic_notes/final_vowel_apocope_investigation.md
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2075 hind / hind

## Current row state

- CONCEPT: `hind`
- COUNTERPART: `hind`
- PROTO: `*xéndjō`
- PROTOFORM: `*xéndjō`
- DERIVATION_CLASS: `regular`
- Live TSV note: `Kroonen *hindō- f. 'hind (deer)' → OE hind f.; hindan 'from behind' is wrong lexeme` [Germanic/data/germanic-aligned-final.tsv:563].
- Packet status is currently regular and internally consistent: `EXPECTED: hind`, `OUTPUTS: hind`, with the compact trace `Proto Input: *xéndjō` > NWGmc `*xéndju` > OE `*çéndju` > `*çindju` > `*çindj` > `*çind`, surfacing as `hind` [Germanic/docs/lexeme_reports/packets/2075-hind-hind.md:17-43].
- `oe_known_problems.tsv`: no row-specific entry is attached; the packet records `_None_`, and the memo likewise states that there is no dedicated current problem entry for this lexeme [Germanic/docs/lexeme_reports/packets/2075-hind-hind.md:45-47; Germanic/docs/lexeme_reports/research_memos/2075-hind-hind.md:25-27, 67-69].
- `report_manifest.tsv`: no manifest entry is present for this row [Germanic/docs/lexeme_reports/packets/2075-hind-hind.md:11-13].
- The memo identifies the real workflow issue as lexeme disambiguation rather than phonological repair: row 2075 must stay tied to noun `hind` 'female deer', while `hindan` belongs to the separate adverb/preposition meaning 'from behind, behind' [Germanic/docs/lexeme_reports/research_memos/2075-hind-hind.md:31-39, 41-51].

## Development-note summary

No securely attachable **row-specific DEV_NOTES authority** currently exists for row 2075. The packet's exact-match review records `_None_` for high-confidence, supporting/background, and stale/diagnostic DEV_NOTES hits, and the research memo separately reports that `DEV_NOTES.md`, `oe_known_problems.tsv`, `Germanic/docs/analysis/`, and `Germanic/docs/dossiers/` contain no dedicated current problem note or dossier for this lexeme [Germanic/docs/lexeme_reports/packets/2075-hind-hind.md:49-61, 79-87; Germanic/docs/lexeme_reports/research_memos/2075-hind-hind.md:25-27, 67-69]. The absence matters: it means there is no surviving DEV_NOTES fragment that overrides the live row's present regular analysis.

What is current instead is the row-plus-packet bundle. The live row's project input remains `*xéndjō` in both `PROTO` and `PROTOFORM`, and the current derivation already lands on OE `hind` without exception handling [Germanic/data/germanic-aligned-final.tsv:563; Germanic/docs/lexeme_reports/packets/2075-hind-hind.md:19-43]. At the same time, the comparative etymological headword preserved in repo literature is Kroonen's `*hindō- f. 'hind' — ... OE hind f. 'id.'`, so the slice must keep three levels distinct: comparative headword `*hindō-`, project derivational input `*xéndjō`, and OE target noun `hind` [docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:12736-12740; Germanic/docs/lexeme_reports/research_memos/2075-hind-hind.md:31-39].

The row's actual philological correction is lexical, not phonological. Clark Hall's dictionary separates noun `hind(y) f. 'hind,' (female deer)` from `hindan`, glossed `from behind, behind, in the rear`, and the memo records the same split from Bosworth-Toller [docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:22069-22069, 22115-22116; Germanic/docs/lexeme_reports/research_memos/2075-hind-hind.md:22-24, 41-45]. That is why the packet's local lexical-table hit `hind -> hindan` is not authority for the row but a false-positive source audit explaining how the lexeme was previously confused [Germanic/data/old_english_wiktionary.tsv:138; Germanic/docs/lexeme_reports/packets/2075-hind-hind.md:67-74; Germanic/docs/lexeme_reports/research_memos/2075-hind-hind.md:43-45].

The practical consequence is narrow but important. Row 2075 does **not** need a paradigm probe, a new repair rule, or a DEV_NOTES-derived exception label. It needs a self-sufficient working note stating explicitly that current authority is the live regular derivation to noun `hind`, while any material expecting `hindan` is comparator/background/diagnostic evidence for a different OE lexeme or for older repo history only [Germanic/docs/lexeme_reports/research_memos/2075-hind-hind.md:39-55, 67-71].

## Relevant DEV_NOTES fragments

No securely attachable **current** row-specific DEV_NOTES fragment survives. The packet records `_None_` under exact-match, supporting/background, and stale/diagnostic DEV_NOTES hits, and the memo independently confirms that there is no dedicated current DEV_NOTES authority to extract for this lexeme [Germanic/docs/lexeme_reports/packets/2075-hind-hind.md:49-61, 79-83; Germanic/docs/lexeme_reports/research_memos/2075-hind-hind.md:25-27, 67-69]. Any project-history material worth preserving for row 2075 comes from non-DEV_NOTES diagnostic files, not from `Germanic/docs/DEV_NOTES.md` itself.

## Superseded or diagnostic material

- The packet's only local lexical-table hit, `hind -> hindan`, is **diagnostic only**. It is useful as evidence for how the row became confused, but it is not lexical authority for noun `hind`; the current row note and the memo both treat it as a headword/template mismatch pointing to the separate adverb/preposition `hindan` [Germanic/data/old_english_wiktionary.tsv:138; Germanic/data/germanic-aligned-final.tsv:563; Germanic/docs/lexeme_reports/research_memos/2075-hind-hind.md:43-45].
- `Germanic/docs/germanic_transducer_report.md` preserves stale project history, not current row policy. It still lists `*xendjō -> hindan` among OE outputs in two January 2026 diagnostic sweeps, so it should be cited only as evidence of the earlier lexeme misidentification and never as authority against the live `hind` row [Germanic/docs/germanic_transducer_report.md:31-38, 54-56; Germanic/docs/lexeme_reports/research_memos/2075-hind-hind.md:25-26, 39-40].
- `Germanic/docs/germanic_notes/final_vowel_apocope_investigation.md` is likewise superseded for this row. Its `Proto *-ō cases` table gives `*xendjō -> hindō (exp. hindan)`, which preserves an older pre-cleanup output and the same wrong expected target; for row 2075 that material is project archaeology only [Germanic/docs/germanic_notes/final_vowel_apocope_investigation.md:304-309; Germanic/docs/lexeme_reports/research_memos/2075-hind-hind.md:25-26, 39-40].
- The absence of a row-specific `oe_known_problems.tsv` entry, manifest row, or DEV_NOTES fragment is itself a current-state fact worth preserving. The row is not being managed as an open OE exception; what remains to watch is only evidence hygiene around noun `hind` versus adverb/preposition `hindan` [Germanic/docs/lexeme_reports/packets/2075-hind-hind.md:11-13, 45-61; Germanic/docs/lexeme_reports/research_memos/2075-hind-hind.md:47-55, 67-71].

## Open questions for later work

- If a final lexeme report is drafted, decide whether to quote Kroonen's `*hindō- f. 'hind' — ... OE hind f. 'id.'` directly so the distinction between comparative headword and project input `*xéndjō` cannot be blurred [docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:12736-12740].
- Review whether `Germanic/data/old_english_wiktionary.tsv` should be corrected or explicitly annotated for this concept, since its current `hind -> hindan` mapping is the clearest reusable false positive in the packet [Germanic/data/old_english_wiktionary.tsv:138; Germanic/docs/lexeme_reports/research_memos/2075-hind-hind.md:71-71].
- Review whether the older diagnostic statements in `Germanic/docs/germanic_transducer_report.md` and `Germanic/docs/germanic_notes/final_vowel_apocope_investigation.md` should be explicitly marked superseded so they cannot be mistaken for live lexical evidence in later row work [Germanic/docs/lexeme_reports/research_memos/2075-hind-hind.md:71-71].
