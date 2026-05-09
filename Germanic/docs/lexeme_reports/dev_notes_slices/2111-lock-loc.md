---
row_id: 2111
concept: lock
counterpart: loc
proto: *lúką
protoform: *lúką
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
  - Germanic/docs/germanic_notes/final_vowel_apocope_investigation.md
current_status: current_no_row_specific_dev_notes_block
needs_literature_agent: no
---

# DEV_NOTES material — 2111 lock / loc

## Current row state

- The live OE row is the simplex `lock / loc` entry, not the adjacent geminate row `lock / locc`: `2111 ... loc ... *lúką ... regular`, immediately beside `2112 ... locc ... *lúkkaz ... regular`. `PROTO` and `PROTOFORM` are both still `*lúką`; no alternate paradigm cell or repair input is currently in play [Germanic/data/germanic-aligned-final.tsv:700-704].
- The row has no live row-specific `NOTE`; the only attached provenance is duplicated Wiktionary inheritance sourcing. Coverage infrastructure likewise still treats it as uncovered report territory: `| 2111 | lock | loc | regular | no | - | - | - | none |` [Germanic/data/germanic-aligned-final.tsv:702-702; Germanic/docs/lexeme_reports/coverage_audit.md:299-299].
- `oe_known_problems.tsv` has no entry for `*lúką`, so the row is not currently being tracked as a mismatch bucket, wontfix item, or exception class [Germanic/data/oe_known_problems.tsv:1-8].
- The published derivation snapshot is clean and minimal: `PROTO: *lúką`, `EXPECTED: loc`, `OUTPUTS: loc`, with the only named steps `NWGmc U Lowering: *lóką` and then `OE Heavy Syllable Nasal Apocope: *lók`, yielding surface `loc` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2984-3003].
- The full trace confirms the same point in rule-by-rule form. `NWGmcULowering` changes `*lúką` to `*lóką`; `PWGmcFinalBareALoss` does nothing while final `*ą` is still present; `OEHeavySyllableNasalApocope` is the rule that actually removes the ending; after that, all later OE cleanup rules are `[no-change]`, including `OEHighVowelApocope` [Germanic/docs/debug_snapshots/oe_full_trace_report.txt:19866-19918].

## Development-note summary

No row-specific `lock / loc / *lúką` block survives in `DEV_NOTES.md`. The surviving DEV_NOTES support is shared apocope material, not a bespoke lexeme note, so this slice has to say that plainly and build conservatively from the shared rule history plus the current row trace.

The closest surviving DEV_NOTES material is the archived heavy-syllable nasal-apocope note. That note records an `experimental rule deleting proto *-ą after heavy syllables`, says the extra-vowel problem was concentrated in heavy stems, cites the background that Ringe–Taylor explicitly discuss high-vowel loss after heavy syllables and that Hogg describes strong neuters with zero ending after heavy stems and `-u` after light stems, but also admits that `Neither source explicitly extends this pattern to *-ą` [Germanic/docs/DEV_NOTES.md:1591-1612]. For row `2111`, that is the crucial surviving substance: after NWGmc `*u > *o`, the form is `*lóką`, a heavy monosyllable (`ó` + coda `k`), and the live trace shows final-vowel loss happening exactly through the heavy-syllable nasal-apocope rule rather than through any row-specific workaround [Germanic/docs/DEV_NOTES.md:1595-1612; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2991-3003; Germanic/docs/debug_snapshots/oe_full_trace_report.txt:19869-19918].

So the replacement working position should remain narrow. `PROTO` = `PROTOFORM` = `*lúką`; the target OE form is the attested simplex `loc`; and the best surviving project rationale is shared-weight conditioning on final `*-ą`, not a special `lock` dossier. The row is therefore well supported by current implementation state, but only thinly supported by DEV_NOTES as DEV_NOTES [Germanic/data/germanic-aligned-final.tsv:700-704; Germanic/docs/DEV_NOTES.md:1591-1620].

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-1591-1612

- Source heading: `Archived: Heavy Syllable Nasal Apocope (2026-02-06) — EMPIRICAL DISCOVERY`
- Source line hint: `lines 1591-1612`
- Fragment type: `shared_rule_background`
- Status: `shared-background-only`
- Issue tags: `heavy_syllable_nasal_apocope`; `final_-ą`; `heavy_vs_light_weight`; `strong_neuter_endings`
- Recommended next use: `cite_when_explaining_why_final_-ą_drops_in_*lúką`
- Shared-with rows if relevant: `1937 barrow / beorg`; `2179 sheep / sċēap`; `2263 town / tūn`; other heavy-stem `*-ą` rows

This fragment is the nearest thing DEV_NOTES now has to a rationale for row `2111`, but it is not row-local. DEV_NOTES says the extra-vowel mismatch cluster was dominated by heavy stems and summarizes the project inference as an `experimental rule deleting proto *-ą after heavy syllables`; it then anchors that inference in two pieces of background evidence: `Ringe/Taylor §6.8.1: "short *i and *u were lost word-finally after a heavy syllable"` and `Hogg §3.3.2: Neuter strong nouns show zero ending after heavy stems, -u after light stems` [Germanic/docs/DEV_NOTES.md:1595-1607]. Just as important, the note does **not** overclaim: `Neither source explicitly extends this pattern to *-ą` [Germanic/docs/DEV_NOTES.md:1604-1608]. For `*lúką > loc`, that means the usable inheritance from DEV_NOTES is the shared weight-conditioned deletion logic only. Once the live cascade has produced `*lóką`, the row falls straight into the heavy-stem side of that shared pattern, and no further row-specific repair is needed [Germanic/docs/debug_snapshots/oe_full_trace_report.txt:19869-19918].

### DEV_NOTES:line-1617-1625

- Source heading: `Archived: Heavy Syllable Nasal Apocope (2026-02-06) — EMPIRICAL DISCOVERY`
- Source line hint: `lines 1617-1625`
- Fragment type: `implementation_history`
- Status: `diagnostic_but_still_relevant`
- Issue tags: `rule_history`; `pipeline_order`; `mismatch_cleanup`; `final_vowel_extra`
- Recommended next use: `use_for_project_history_only_not_for_current_rule_order`
- Shared-with rows if relevant: the broad `final_vowel_extra` cohort formerly yielding `-a/-ō`

This fragment preserves why the project introduced the rule at all. DEV_NOTES records adding `OldEnglishHeavySyllableNasalApocope`, extending the heavy marker to `*-ą`, and reports the initial mismatch payoff (`41 fixes, 13 collateral`) [Germanic/docs/DEV_NOTES.md:1617-1625]. That history is still relevant for row `2111` because earlier diagnostic work had exactly this lexeme in the extra-vowel bucket as `*luką → luca (exp. loc)` [Germanic/docs/germanic_notes/final_vowel_apocope_investigation.md:273-302]. But the ordering details in the archived note are no longer safe to quote as current-state mechanics: DEV_NOTES says the rule was inserted after `OldEnglishHighVowelApocope`, whereas the present full trace for row `2111` shows `OEHeavySyllableNasalApocope` firing earlier, with `OEHighVowelApocope` already moot afterward [Germanic/docs/DEV_NOTES.md:1618-1620; Germanic/docs/debug_snapshots/oe_full_trace_report.txt:19902-19918].

## Superseded or diagnostic material

- No row-specific DEV_NOTES block survives for `*lúką / loc`. That absence should be stated directly rather than papered over: the row currently inherits only shared apocope reasoning plus live trace support.
- The most useful diagnostic predecessor is `Final Vowel Apocope Investigation`, which treated this lexeme as part of the big pre-fix `*-ą` problem set. It frames the whole issue as OE wrongly preserving final `-a` where heavy stems should lose it, and its long case list includes the row explicitly as `*luką → luca (exp. loc)` [Germanic/docs/germanic_notes/final_vowel_apocope_investigation.md:7-10,38-41,202-219,291-291]. For row work today, that file is historical diagnosis, not live derivational authority.
- The archived DEV_NOTES implementation note is likewise partly superseded. Its empirical motivation remains useful, but its recorded pipeline placement no longer matches the current trace ordering for row `2111`; later writers should therefore cite it for **why** the rule entered the project, not for the exact present-day sequencing [Germanic/docs/DEV_NOTES.md:1617-1625; Germanic/docs/debug_snapshots/oe_full_trace_report.txt:19902-19918].
- Do not conflate this row with the neighboring geminate lexeme `*lúkkaz > locc`. The live TSV and published trace keep them separate, and the present slice is only for the simplex neuter `*lúką > loc` [Germanic/data/germanic-aligned-final.tsv:700-704; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2984-3005].

## Open questions for later work

- If a full lexeme report is ever written, decide whether shared heavy-stem `*-ą` material is enough for indexing or whether row `2111` should remain a slice-only case until a dedicated packet or memo exists [Germanic/docs/lexeme_reports/coverage_audit.md:299-299].
- If stronger philological support is wanted, add direct handbook or dictionary citations for OE `loc` and for the heavy/light strong-neuter ending split; the present slice relies mainly on shared DEV_NOTES reasoning plus current trace behavior, not on a row-specific literature packet.
- If DEV_NOTES is ever normalized, reconcile the archived rule-order note with the live trace order so future documentation does not quote the old placement (`after OldEnglishHighVowelApocope`) as if it were still the active cascade [Germanic/docs/DEV_NOTES.md:1618-1620; Germanic/docs/debug_snapshots/oe_full_trace_report.txt:19902-19918].
