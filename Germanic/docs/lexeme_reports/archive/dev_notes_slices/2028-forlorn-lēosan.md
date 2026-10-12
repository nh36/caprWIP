---
row_id: 2028
concept: forlorn
counterpart: lēosan
proto: *léusaną
protoform: *léusaną
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file: Germanic/docs/lexeme_reports/packets/2028-forlorn-lēosan.md
linked_research_memo_file: Germanic/docs/lexeme_reports/research_memos/2028-forlorn-lēosan.md
linked_dossier_or_analysis_files:
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2028 forlorn / lēosan

## Current row state

- CONCEPT: `forlorn`
- COUNTERPART: `lēosan`
- PROTO: `*léusaną`
- PROTOFORM: `*léusaną`
- DERIVATION_CLASS: `regular`
- Live TSV note/history: the row currently models bare infinitive `lēosan` from simplex `*léusaną`, but the preserved history says this was a TSV fix from earlier `forloren`, described there as a “prefixed past participle for-lēosan” replaced by “lēosan (bare infinitive matching proto *leusăną, Kroonen *leusan-)” [Germanic/data/germanic-aligned-final.tsv:380; Germanic/docs/lexeme_reports/packets/2028-forlorn-lēosan.md:7-10].
- `oe_known_problems.tsv`: no row-level entry for `2028`, `*léusaną`, `lēosan`, or `forloren`, so the live project does **not** currently classify this row as a sound-law bug, exception bucket, or known modelling failure [Germanic/docs/lexeme_reports/packets/2028-forlorn-lēosan.md:44-46; Germanic/docs/lexeme_reports/research_memos/2028-forlorn-lēosan.md:24-29].
- `report_manifest.tsv`: no manifest entry is present for this lexeme [Germanic/docs/lexeme_reports/packets/2028-forlorn-lēosan.md:11-13].
- Packet / memo state: the compact derivation trace is fully regular as currently encoded (`*léusaną > lēosan`), but the strongest row-specific lexical evidence gathered in the packet and memo points to **prefixed** OE material instead: the packet's lexical-table hit gives English `forlorn = forloren`, and the memo says the strongest comparative and OE daughter evidence is `forlēosan / forloren`, not unprefixed `lēosan` [Germanic/docs/lexeme_reports/packets/2028-forlorn-lēosan.md:19-42, 68-72; Germanic/docs/lexeme_reports/research_memos/2028-forlorn-lēosan.md:13-20, 24-39, 47-80].

## Development-note summary

No securely attachable **row-specific** DEV_NOTES authority survives for row 2028. Both linked row files are explicit on that point: the packet records `_None_` for DEV_NOTES hits in both its high-confidence and supporting sections, and the research memo likewise states that `Germanic/docs/DEV_NOTES.md` has “no row-specific discussion of this lexeme” [Germanic/docs/lexeme_reports/packets/2028-forlorn-lēosan.md:48-60, 78-86; Germanic/docs/lexeme_reports/research_memos/2028-forlorn-lēosan.md:24-29]. This slice therefore has to function as a replacement working note built from the live TSV row plus the packet/memo evidence, rather than pretending that DEV_NOTES already settled the lexeme.

The first point to preserve is that the **live row is regular in transducer terms**. Nothing in the checked row materials says the sound law `*léusaną > lēosan` is broken; the packet trace matches exactly, `oe_known_problems.tsv` is silent, and the memo explicitly says “The project issue here is not a sound-law failure. The live derivation `*léusaną > lēosan` is regular” [Germanic/docs/lexeme_reports/packets/2028-forlorn-lēosan.md:19-42, 44-46; Germanic/docs/lexeme_reports/research_memos/2028-forlorn-lēosan.md:65-68]. Later report writing should therefore avoid importing exception-language from other verb rows. The instability here is lexical targeting, not phonological derivation.

The second point is the one the row history keeps alive: the current regularity may have been purchased by **de-prefixing away the lexeme that English `forlorn` actually continues**. The packet preserves the exact history string that the row was changed from `forloren` to `lēosan`, and the memo argues that this replaced one problem with another: `forloren` was too specific as a participial cell, but bare `lēosan` strips away a prefix that local comparative sources treat as integral to the daughter evidence [Germanic/data/germanic-aligned-final.tsv:380; Germanic/docs/lexeme_reports/packets/2028-forlorn-lēosan.md:7-10; Germanic/docs/lexeme_reports/research_memos/2028-forlorn-lēosan.md:69-80]. The memo's three-level distinction is worth preserving verbatim in substance: current row input `*léusaną`, comparative lexicalized daughter family centered on prefixed `*fraleusaną`, and the directly relevant OE form behind English `forlorn`, namely `forlēosan` / past participle `forloren` [Germanic/docs/lexeme_reports/research_memos/2028-forlorn-lēosan.md:43-52].

The third point is the **asymmetry of the lexical evidence** already gathered inside the repo. The packet's only local lexical-table hit is not `lēosan` but `forloren` [Germanic/docs/lexeme_reports/packets/2028-forlorn-lēosan.md:66-72]. The memo then broadens that result and reports that Kroonen gives the etymon `*leusan-` but cites OE `for-lēosan`, Orel likewise cites OE `for-leósan`, Ringe says the prefixed comparative verb “never lacks its prefix *fra-” in the daughters, and Ringe-Taylor give the full OE paradigm `forléosan, forléas, forluron, forloren` [Germanic/docs/lexeme_reports/research_memos/2028-forlorn-lēosan.md:30-39, 47-61; @Kroonen2013; @Orel2003; @Ringe2006; @RingeTaylor2014]. Even the memo's more cautious concessions are important: bare `lēosan` is not fabricated out of nothing, because some comparative or pedagogical discussions use it as a family label, but that is weaker than the prefixed lexical evidence for this specific English gloss [Germanic/docs/lexeme_reports/research_memos/2028-forlorn-lēosan.md:35-38, 55-64; @Fulk2018].

For normal workflow, the controlling practical conclusion is therefore narrow but important. This row should currently be described as a **regular de-prefixed normalization**, not as a DEV_NOTES-backed philological closure. If later work leaves the row untouched, the final report needs to say explicitly that `lēosan` is a project normalization chosen to match simplex `*léusaną`, while the direct OE material behind English `forlorn` is prefixed `forlēosan / forloren` [Germanic/docs/lexeme_reports/research_memos/2028-forlorn-lēosan.md:74-80, 97-109]. If later work retargets the row, the memo's recommendation is equally explicit: keep citation-form status but restore the prefix, i.e. prefer `forlēosan` over participial `forloren`, and align the row's proto-side fields to prefixed `*fraléusaną` rather than simplex `*léusaną` [Germanic/docs/lexeme_reports/research_memos/2028-forlorn-lēosan.md:74-80, 101-109].

## Relevant DEV_NOTES fragments

No securely attachable **current** row-specific DEV_NOTES fragment survives. The reviewed ranges below are kept only so later packet or index work can see exactly which literal-search hits were examined and rejected.

### DEV_NOTES:line-844-850

- Source heading: `Current FST rule and needed changes`
- Source line or section hint: `lines 844-850`
- Fragment type: `superseded_or_diagnostic_for_lexeme`
- Status: `diagnostic_only`
- Issue tags: `line_number_collision`; `literal_row_id_search_noise`; `packet_hygiene`
- Recommended next use: `use_as_project_history_only`
- Shared with row IDs:

This is not evidence for row 2028. The only reason it surfaces in a literal search is the phrase “Current rule (lines 2028-2032),” which refers to source-code line numbers inside `germanic.txt`, not to row ID 2028, `lēosan`, `forlēosan`, or `forloren` [DEV_NOTES:line-844-850].

### DEV_NOTES:line-30573-30577

- Source heading: `n-stem ending reduction note citing germanic.txt:2026-2028`
- Source line or section hint: `lines 30573-30577`
- Fragment type: `superseded_or_diagnostic_for_lexeme`
- Status: `diagnostic_only`
- Issue tags: `line_number_collision`; `literal_row_id_search_noise`; `wrong_phenomenon`
- Recommended next use: `use_as_project_history_only`
- Shared with row IDs:

This appendix note is about trimoric `*ô -> *a` in the separate `nafola` discussion. Its apparent relevance comes solely from the string “germanic.txt:2026–2028,” i.e. another line-number reference unrelated to row 2028 or to the `*leusan-` family [DEV_NOTES:line-30573-30577].

### DEV_NOTES:line-30705-30709

- Source heading: `option summary repeating germanic.txt:2026-2028`
- Source line or section hint: `lines 30705-30709`
- Fragment type: `superseded_or_diagnostic_for_lexeme`
- Status: `diagnostic_only`
- Issue tags: `line_number_collision`; `literal_row_id_search_noise`; `wrong_phenomenon`
- Recommended next use: `use_as_project_history_only`
- Shared with row IDs:

This is another non-lexical collision inside the same `nafola` argument. The text says that weak-tail reduction on `*-ô` uses `germanic.txt:2026–2028`; it does not discuss `forlorn`, `lēosan`, prefixed `forlēosan`, or any row-level decision for 2028 [DEV_NOTES:line-30705-30709].

### DEV_NOTES:line-30968-30970

- Source heading: `appendix checklist repeating the trimoric *ô -> *a rule`
- Source line or section hint: `lines 30968-30970`
- Fragment type: `superseded_or_diagnostic_for_lexeme`
- Status: `diagnostic_only`
- Issue tags: `line_number_collision`; `literal_row_id_search_noise`; `wrong_phenomenon`
- Recommended next use: `use_as_project_history_only`
- Shared with row IDs:

This third hit is more of the same diagnostic noise. The appendix checklist again labels the relevant `nafola` rule as “germanic.txt:2026–2028,” so it can be retrieved by a search on `2028`, but it contains no usable authority for row 2028 itself [DEV_NOTES:line-30968-30970].

## Superseded or diagnostic material

There is no surviving **row-specific superseded DEV_NOTES analysis** here comparable to the abandoned paradigm-cell rescues or rollback notes seen in other slices. The superseded material belongs to the row history preserved in the live TSV and memo instead: earlier `forloren` was too narrow because it targeted one participial cell, while current `lēosan` may be too normalized because it suppresses the prefixed lexeme that the memo's comparative and lexical evidence treats as central [Germanic/data/germanic-aligned-final.tsv:380; Germanic/docs/lexeme_reports/research_memos/2028-forlorn-lēosan.md:69-80, 101-109].

The main diagnostic caution is therefore editorial. Because DEV_NOTES is silent, later report prose should not imply that the simplex-vs-prefixed choice has already been adjudicated in DEV_NOTES. The only DEV_NOTES material presently reviewable for this row is literal-search noise on the number `2028` and on `germanic.txt:2026-2028`, not a hidden lexical dossier [Germanic/docs/lexeme_reports/packets/2028-forlorn-lēosan.md:48-60; DEV_NOTES:line-844-850; DEV_NOTES:line-30573-30577; DEV_NOTES:line-30705-30709; DEV_NOTES:line-30968-30970].

## Open questions for later work

- Decide whether row 2028 should remain a deliberate de-prefixed normalization (`*léusaną > lēosan`) or be retargeted to the prefixed citation form `forlēosan` with proto-side alignment to `*fraléusaną` [Germanic/docs/lexeme_reports/research_memos/2028-forlorn-lēosan.md:74-80, 101-109].
- If the row stays as `lēosan`, make the final report say explicitly that English `forlorn` continues OE `forloren` / `forlēosan`, and that bare `lēosan` is being used only as a project normalization rather than as the strongest direct OE counterpart [Germanic/docs/lexeme_reports/packets/2028-forlorn-lēosan.md:68-72; Germanic/docs/lexeme_reports/research_memos/2028-forlorn-lēosan.md:55-64, 97-109].
- If later index integration trims reviewed-only false positives, preserve at minimum the explicit statement that row 2028 has **no securely attachable row-specific DEV_NOTES authority** rather than implying that this slice omitted a richer DEV_NOTES dossier.
