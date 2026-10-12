---
row_id: 2303
concept: worm
counterpart: wyrm
proto: *wúrmiz
protoform: *wúrmiz
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
  - Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2303 worm / wyrm

## Current row state

- The live OE row is now a clean regular row: concept `worm`, counterpart `wyrm`, PROTO `*wúrmiz`, PROTOFORM `*wúrmiz`, DERIVATION_CLASS `regular`, and no surviving row-local `NOTE` text in the TSV itself beyond source provenance. For this slice, the important distinction is that both project proto fields currently point to the i-stem input, not to the older alternant string with a slash [Germanic/data/germanic-aligned-final.tsv:1448-1448].
- Coverage infrastructure treats the row as unattached rather than problematic: `| 2303 | worm | wyrm | regular | no | - | - | - | none |`. So there is still no packet, no memo, and no manifest-backed lexeme report already carrying this material [Germanic/docs/lexeme_reports/coverage_audit.md:420-420; Germanic/docs/lexeme_reports/report_manifest.tsv:1-13].
- The current published OE derivation snapshot already matches the target without repair. It gives `PROTO: *wúrmiz`, `EXPECTED: wyrm`, `OUTPUTS: wyrm`, with the compact derivation `PGmc Final Z Deletion: *wúrmi` > `OE I Umlaut: *wyrmi` > `OE High Vowel Apocope: *wyrm` > `Outcome: wyrm` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:6065-6084].
- `oe_known_problems.tsv` currently lists only a handful of other exception buckets and has no entry for `*wúrmiz` or row `2303`, which is consistent with the successful live trace and the row's present `regular` classification [Germanic/data/oe_known_problems.tsv:1-8].

## Development-note summary

This row still has genuinely row-specific DEV_NOTES support, and that surviving block is the core evidence to preserve. The main current material is the 2026-03-13 note `TSV Fix: *wurmaz/wurmiz → *wurmiz (wyrm 'worm')`, which argues that the older slash-form PROTOFORM was bad FST syntax and bad OE conditioning for this row, while `*wurmiz` is both the parseable input and the historically right OE-driving form because `wyrm` shows i-umlaut [Germanic/docs/DEV_NOTES.md:8381-8474].

Support divides into three layers and the slice should keep those layers distinct. First, there is **row-specific current support**: DEV_NOTES quotes Kroonen, Orel, Ringe–Taylor, Campbell, and Bülbring in order to justify the OE row's i-stem input and says explicitly that “The presence of /y/ in OE wyrm is diagnostic of an i-stem input” [Germanic/docs/DEV_NOTES.md:8397-8450]. Second, there is **shared-background-only diagnostic support** from the earlier no-output cleanup, where `*wurmaz/wurmiz` appears as one of the malformed TSV inputs that failed simply because the grammar does not parse slash alternants; DEV_NOTES calls these “TSV format issues, not phonology bugs” [Germanic/docs/DEV_NOTES.md:8290-8377]. Third, there is **current implementation diagnostic support** in the live derivation snapshot, which confirms that once the row uses `*wúrmiz`, the cascade already derives `wyrm` straightforwardly, so there is no surviving mismatch to explain away [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:6065-6084].

The resulting working stance should stay conservative. For row `2303`, `PROTO` and `PROTOFORM` are both currently the OE-driving i-stem form `*wúrmiz`; the attested/target OE form is `wyrm`; and the old alternant notation `*wurmaz/wurmiz` survives only as historical diagnostic evidence about a former TSV formatting error and an older hesitation over stem class, not as a current row value to restore [Germanic/data/germanic-aligned-final.tsv:1448-1448; Germanic/docs/DEV_NOTES.md:8388-8467].

## Relevant DEV_NOTES fragments

### DEV_NOTES fragment 1

- Source heading: `TSV Fix: *wurmaz/wurmiz → *wurmiz (wyrm 'worm')`
- Source line hint: `Germanic/docs/DEV_NOTES.md:8381-8423`
- Fragment type: `row_specific_source_analysis`
- Status: `current`
- Issue tags: `protoform_selection`; `i_stem`; `literature_support`; `slash_cleanup`
- Recommended next use: `cite when explaining why the OE row keeps *wurmiz rather than a slash alternant or a-stem citation form`
- Shared-with rows if relevant: `primarily row-specific; only loosely shared with other stem-class selection rows`

This is the key row-specific source block and it survives in usable form. DEV_NOTES records that row `2303` formerly had `PROTOFORM: *wurmaz/wurmiz` beside `COUNTERPART: wyrm`, then states that the slash notation is invalid FST input syntax and therefore produced no output [Germanic/docs/DEV_NOTES.md:8388-8395]. It then preserves the literature dossier in quotation form. Kroonen is quoted as reconstructing `“*wurmi- m. 'worm' — Go. waurms m. 'snake', ON ormr m. 'id.', OE wyrm m. 'snake, worm', OFri. wirm m. 'worm', OS wurm m. 'id.', OHG wurm m. 'worm, snake'”`, and DEV_NOTES glosses that as an i-stem citation which in project notation corresponds to `*wurmiz` [Germanic/docs/DEV_NOTES.md:8399-8405]. Orel is quoted more cautiously: `“*wurmaz ~ wurmiz sb.m.: Goth waurms 'snake', ON ormr 'serpent', OE wyrm id., OFri. worm id., OS wurm id., OHG wurm id.”`; DEV_NOTES immediately says that Orel hedges, but that the OE evidence points toward `*wurmiz` for the Old English row [Germanic/docs/DEV_NOTES.md:8407-8411]. Ringe & Taylor are then quoted in the strongest row-local way: `“PGmc *wurmiz 'worm, snake' ... > OE wyrm”` [Germanic/docs/DEV_NOTES.md:8413-8417]. DEV_NOTES writes the repaired preform without the acute accent used in the live TSV, but the stem-class claim is the same: the current row's accented `*wúrmiz` is the present project encoding of that same OE-driving i-stem choice [Germanic/docs/DEV_NOTES.md:8404-8405,8413-8417; Germanic/data/germanic-aligned-final.tsv:1448-1448].

The same fragment also preserves the handbook classification needed for row-specific morphology. DEV_NOTES says that Campbell §602 lists `wyrm` as an i-stem noun in the class “like giest,” and that Bülbring §280, §359 also treats `wyrm` as an i-stem [Germanic/docs/DEV_NOTES.md:8419-8422]. For this slice, that material is not just background bibliography. It directly supports the current row state's choice to keep both PROTO and PROTOFORM on the i-stem side for OE, even if one comparative source allowed alternation at the broader Proto-Germanic lexeme level.

### DEV_NOTES fragment 2

- Source heading: `TSV Fix: *wurmaz/wurmiz → *wurmiz (wyrm 'worm')`
- Source line hint: `Germanic/docs/DEV_NOTES.md:8424-8453`
- Fragment type: `row_specific_phonological_argument`
- Status: `current`
- Issue tags: `i_umlaut`; `oe_y`; `regular_derivation`; `oe_specific_protoform`
- Recommended next use: `cite when distinguishing comparative alternants from the specific OE-driving preform`
- Shared-with rows if relevant: `shared in principle with other OE i-umlaut noun rows, but phrased here specifically for row 2303`

This is the sharpest row-local reasoning in the surviving note, and it should be copied forward almost verbatim in substance. DEV_NOTES states: `“The OE form wyrm shows i-umlaut: PGmc *u > OE y.”` It then lays out the diagnostic contrast explicitly: `“If a-stem *wurmaz: nom.sg. has no umlaut trigger → would give ×wurm”` versus `“If i-stem *wurmiz: nom.sg. *-iz triggers umlaut → gives wyrm ✓”` [Germanic/docs/DEV_NOTES.md:8426-8430]. The sentence that needs to survive intact in working use is DEV_NOTES's own conclusion: `“The presence of /y/ in OE wyrm is diagnostic of an i-stem input.”` [Germanic/docs/DEV_NOTES.md:8432-8432].

DEV_NOTES then explains why the bad slash notation likely appeared in the first place without letting that older hesitation govern the OE row. It suggests that the scraper or source may have hedged between stem classes, that continental West Germanic forms such as OS/OHG `wurm` without umlaut may suggest `*wurmaz`, but that `“OE wyrm requires *wurmiz for regular sound change”` [Germanic/docs/DEV_NOTES.md:8434-8444]. The recommendation is correspondingly OE-specific and should remain so: `“For the OE row, use *wurmiz (i-stem)”` because the handbooks support it, the OE form requires it, and the FST derives `*wurmiz → wyrm` correctly [Germanic/docs/DEV_NOTES.md:8445-8453]. This is the place where PROTO/PROTOFORM/target distinctions matter most: comparative alternation may exist in the literature, but the row's actual OE-driving PROTOFORM must be the i-stem preform, while the attested target remains `wyrm`.

### DEV_NOTES fragment 3

- Source heading: `The Problem` / `Other no_output Issues` in the mismatch-cleanup note
- Source line hint: `Germanic/docs/DEV_NOTES.md:8290-8377`
- Fragment type: `shared_background_only_diagnostic`
- Status: `superseded_but_useful`
- Issue tags: `former_no_output`; `tsv_syntax`; `slash_alternants`; `parser_failure`
- Recommended next use: `cite only when reconstructing why the row once failed before the TSV fix`
- Shared-with rows if relevant: `shared with the other former no-output formatting rows, especially the hyphenated-compound cases`

This earlier fragment is diagnostic rather than authoritative for the row's current analysis, but it is still worth preserving because it explains the old failure mode cleanly. DEV_NOTES lists `*wurmaz/wurmiz | wyrm | Slash for alternants` among the forms that produced no output and later repeats the row in the table of “Remaining no_output forms (4)” [Germanic/docs/DEV_NOTES.md:8290-8298,8367-8375]. The important wording is that these cases are `“TSV format issues, not phonology bugs”` [Germanic/docs/DEV_NOTES.md:8341-8347,8377-8377]. For row `2303`, that means the slash-form belongs in the history of repository cleanup, not in the current phonological explanation of `wyrm`.

## Superseded or diagnostic material

- The old slash-form `*wurmaz/wurmiz` is superseded as live row content. It remains useful only as evidence that the row once mixed comparative alternants into a field that the FST expected to contain a single parseable input [Germanic/docs/DEV_NOTES.md:8388-8395,8462-8467].
- Orel's quoted alternation `*wurmaz ~ wurmiz` is also diagnostic rather than decisive for the present OE row. DEV_NOTES preserves it because it explains why a scraper or editor may have hesitated, but DEV_NOTES does **not** let that alternation override the row-specific OE requirement that `wyrm` be derived from an i-stem input [Germanic/docs/DEV_NOTES.md:8407-8411,8447-8453].
- The no-output bucket is fully superseded for current implementation status. The live derivation snapshot now already returns `wyrm`, and `oe_known_problems.tsv` does not track this row as an exception, so the old parser-failure diagnosis should not be mistaken for a still-open sound-change problem [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:6065-6084; Germanic/data/oe_known_problems.tsv:1-8].
- Continental non-umlaut comparanda (`worm`, `wurm`) are preserved in the DEV_NOTES discussion only as diagnostic background for the older stem-class hesitation. DEV_NOTES explicitly says that whether German/Dutch rows might use `*wurmaz` is “a separate question,” so that material should not be imported back into the OE slice as if it weakened the current OE analysis [Germanic/docs/DEV_NOTES.md:8441-8453].

## Open questions for later work

- If the project later formalizes a policy separating comparative `PROTO` from OE-driving `PROTOFORM`, decide whether this lexeme should display Orel-style alternation at the comparative layer while still keeping row `2303`'s actual PROTOFORM fixed as `*wurmiz`. The current row does not require that distinction, but the literature history makes it a plausible future metadata question [Germanic/docs/DEV_NOTES.md:8407-8411,8447-8453].
- If cross-branch harmonization is attempted later, review whether the Dutch/German/OS/OHG comparanda should be modeled from a different stem-class preform. DEV_NOTES flags that possibility but leaves it unresolved and explicitly outside the OE-row fix [Germanic/docs/DEV_NOTES.md:8441-8453].
- If a later literature pass wants exact source-file verification rather than DEV_NOTES-embedded quotations, re-check the quoted Kroonen, Orel, Ringe–Taylor, Campbell, and Bülbring passages against the repo's reference extracts or scans. For the present row slice, the surviving DEV_NOTES quotations are enough to support the working conclusion without opening a new literature task [Germanic/docs/DEV_NOTES.md:8399-8422].
