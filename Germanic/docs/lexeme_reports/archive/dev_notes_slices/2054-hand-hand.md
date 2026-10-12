---
row_id: 2054
concept: hand
counterpart: hand
proto: *xánduz
protoform: *xánduz
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files: []
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2054 hand / hand

## Current row state

- Live TSV row 2054 is fully regular in current repo state: `CONCEPT = hand`, `COUNTERPART = hand`, `PROTO = *xánduz`, `PROTOFORM = *xánduz`, `DERIVATION_CLASS = regular`. The row carries inherited-source history strings but no row-local explanatory note, so the active OE-facing input and the comparative proto headword are presently the same form [Germanic/data/germanic-aligned-final.tsv:1-1; Germanic/data/germanic-aligned-final.tsv:482-482].
- `coverage_audit.md` records row 2054 as `regular`, with no packet, no memo, no attached DEV_NOTES fragment, and `none` in the final column. That matters: this slice is replacing consultation of the big DEV_NOTES file, not summarizing an already-built row packet [Germanic/docs/lexeme_reports/coverage_audit.md:264-264].
- The required known-problems check is negative. `oe_known_problems.tsv` lists only other exception rows, so row 2054 is not presently treated as an analogical, unresolved, or FST-mismatch case [Germanic/data/oe_known_problems.tsv:1-8].
- `report_manifest.tsv` still contains only the pilot-report rows; row 2054 is not among them, so there is no pre-existing manifest-backed lexeme report to defer to [Germanic/docs/lexeme_reports/report_manifest.tsv:1-14].
- Current derivation snapshots show an exact match. The published compact trace has `PROTO: *xánduz`, `EXPECTED: hand`, `OUTPUTS: hand`, and the orthographic outcome `h*ánd > hand` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1990-2010]. The fuller March trace uses the same input without the acute (`*xanduz`) and shows the relevant successful stages explicitly: `ConsonantRules: *x*a*n*d*u` (final `*z` gone), `HighVowelApocope: *x*a*n*d` (final high vowel lost), and `Orthography: hand` / `Surface: hand` [Germanic/docs/debug_snapshots/oe_full_trace_report_2026-03-11.txt:5888-5941].

## Development-note summary

No dedicated hand-specific DEV_NOTES block survives for row 2054. The replacement note therefore has to be conservative: the usable DEV_NOTES evidence consists of (a) one **shared-background-only** passage in the `duru` note where `hand` appears as a comparator for the tiny surviving OE feminine u-stem class, (b) one **row-specific diagnostic** passage in the `*nd`-cluster audit confirming that `*xanduz` keeps original `*d` and does not need `*ð`, and (c) one older **diagnostic-only** A-restoration debug mention that should not be elevated into a hand-specific historical explanation [Germanic/docs/DEV_NOTES.md:932-959; Germanic/docs/DEV_NOTES.md:7538-7570; Germanic/docs/DEV_NOTES.md:1697-1724].

That limited DEV_NOTES record is still enough for a careful row note. The live row already behaves as a clean exact-match item, and nothing in DEV_NOTES argues for changing either target or input. `PROTO` and `PROTOFORM` are identical because no alternate paradigm cell, analogical repair form, or substituted comparator is currently doing explanatory work here; the row is simply being run as `*xánduz > hand` [Germanic/data/germanic-aligned-final.tsv:482-482; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1990-2010].

The one durable morphological point that does survive from DEV_NOTES is background rather than dossier-level argument: the project explicitly quotes Ringe-Taylor's statement that early OE still had a very small u-stem class including feminine `hand`, and DEV_NOTES also uses `hand` as a comparator for old root-noun behavior inside the `duru` discussion [Germanic/docs/DEV_NOTES.md:932-959]. That helps explain why a nominative singular in `*-uz` is not suspicious for the row, but it does **not** amount to a dedicated hand etymology note. The only clearly row-local DEV_NOTES judgment is narrower: the row's `nd` cluster is to be left with plain `d`, not recast as a Verner-alternant `*nð` form [Germanic/docs/DEV_NOTES.md:7538-7570].

## Relevant DEV_NOTES fragments

### Fragment 1 — surviving u-stem background from the `duru` note

- Source heading: `OE duru 'door': Stem-Class Correction`
- Source line hint: `Germanic/docs/DEV_NOTES.md:932-959`
- Fragment type: `copied_shared_lexeme_fragment`
- Status: `shared-background-only`
- Issue tags: `u_stem`; `morphological_background`; `root_noun_comparator`; `proto_vs_protoform`
- Recommended next use: `cite only for background on OE hand as a surviving feminine u-stem; do not treat as a hand-specific lexeme dossier`
- Shared-with rows if relevant: `the door/duru row and any later notes on surviving OE u-stems`

This is the closest thing DEV_NOTES preserves to positive lexical background for row 2054, but it survives only indirectly inside the `duru` discussion. DEV_NOTES quotes R/T: "The u-stems remained a recognizable inflectional class, but its membership was reduced to a few very common and basic words. Still inflected as u-stems in early OE are masc. *sunu* 'son' and *wudu* 'wood' and fem. *hand* 'hand', *nosu* 'nose', and ***duru* 'door'** (the last **originally a root-noun that had shifted into the u-stems**)" [Germanic/docs/DEV_NOTES.md:932-935]. For row 2054, the important use of that quotation is modest but real: it supports treating OE `hand` as one of the small set of inherited feminine u-stems still alive in early Old English. That fits the live row's `PROTO = PROTOFORM = *xánduz`, i.e. a nominative singular with final high vowel before later apocope, and it gives background support for not inventing a different stem-class story in the slice.

The same `duru` note then uses `hand` again as comparator background rather than direct row analysis. DEV_NOTES summarizes the door etymology with "PIE: Root-noun `*dhur-` (like 'hand', 'tooth', 'goose')" and later says that analogical reshaping into the OE u-stem paradigm happened under the pull of forms "like *sunu*, *nosu*, *hand*" [Germanic/docs/DEV_NOTES.md:952-959]. For row 2054, those lines are useful only as shared morphological context: they show that the project already treats `hand` as a classic old noun in the background literature, but they do not supply a hand-specific bibliography, do not discuss `*xánduz` by name, and do not justify any alteration of the live row.

### Fragment 2 — row-specific `*nd`-cluster audit

- Source heading: `Systematic Check: TSV Forms with *nd Clusters (2026-03-11)`
- Source line hint: `Germanic/docs/DEV_NOTES.md:7538-7570`
- Fragment type: `lexeme_specific_diagnostic`
- Status: `current`
- Issue tags: `dental_representation`; `nd_cluster`; `no_verner_respelling`; `consonant_history`
- Recommended next use: `cite when defending plain *d in the protoform and when explaining why no *nð rewrite is needed`
- Shared-with rows if relevant: `other OE rows with inherited *nd clusters`

This is the only surviving DEV_NOTES fragment that speaks to row 2054 as row 2054 rather than as background illustration. The note says it "Reviewed all TSV entries with `*nd` clusters to confirm none require `*nð`" and then gives the table row `| hand | *xanduz | *kont-? "hand" | original | No |` [Germanic/docs/DEV_NOTES.md:7538-7549]. The accentless spelling in that March audit (`*xanduz`) should be read as the same project input as the live TSV's accented `*xánduz`; the issue under discussion there is the dental segment, not accent notation.

The conclusion is explicit and still current: "Having exactly one `*ð` form in the TSV (`*funðanăz`) is **correct and complete**. All other `*nd` forms have original `*d` from PIE sources other than `*t`" [Germanic/docs/DEV_NOTES.md:7567-7570]. For row 2054 that settles a narrow but important point. The row should continue to be documented with plain `d`; there is no surviving project rationale for replacing the protoform with `*xanðuz`, no nasal-spirant-lengthening issue is in play here, and no Verner-style alternant is needed to explain the OE target.

### Fragment 3 — A-restoration debug mention

- Source heading: `A-restoration debug summary (2026-02-03, FIXED 2026-02-06)` and follow-on mismatch triage bullets
- Source line hint: `Germanic/docs/DEV_NOTES.md:1697-1724`
- Fragment type: `superseded_or_diagnostic_for_lexeme`
- Status: `diagnostic-only`
- Issue tags: `a_restoration`; `debug_history`; `search_artifact`; `not_row_authority`
- Recommended next use: `use only to explain why hand appeared in an earlier debug basket; do not use as the row's main explanatory note`
- Shared-with rows if relevant: `many rows touched by the February A-restoration audit`

This mention should be preserved because it is one of the very few places where `*xanduz -> hand` appears in DEV_NOTES outside the later `*nd` audit, but it should be labelled carefully. After describing the A-restoration bug and its fix, DEV_NOTES records measured intervening segments and says: "True positives (31 items): top intervening segments `n, k, w, d, j` (e.g., *bakăną -> bacan, inter=`k`; *xanduz -> hand, inter=`nd`)" [Germanic/docs/DEV_NOTES.md:1697-1724]. Taken alone, that line could misleadingly suggest that `hand` needs an A-restoration story.

The current row state shows why it should not be read that way. In the full trace, the row passes through `ARestoration` unchanged as `*x*a*n*d*u`; the successful derivation is then carried by ordinary final-segment loss and orthographic mapping, not by a special hand-only vowel repair [Germanic/docs/debug_snapshots/oe_full_trace_report_2026-03-11.txt:5906-5941]. So this fragment is best kept as diagnostic project history only: it proves that `hand` was present in an earlier pattern audit, but it is not controlling authority for current row analysis.

## Superseded or diagnostic material

- No hand-specific DEV_NOTES section survives that would justify a stronger lexeme-level narrative than the one above. The slice should state that plainly rather than reconstructing one from memory. The current row is regular, exact-match, and unflagged in `oe_known_problems.tsv`; the missing thing is a dedicated historical note, not a missing phonological fix [Germanic/data/oe_known_problems.tsv:1-8; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1990-2010].
- The `duru` note is useful but remains comparator material. Its quotations establish that `hand` belongs to the tiny surviving OE feminine u-stem set and that the project thinks of `hand` as an old noun in the same broad comparative space as `tooth` and `goose`, but it does not amount to a hand-specific derivation memo [Germanic/docs/DEV_NOTES.md:932-959].
- The February A-restoration mention is diagnostic only. Because the same debug cluster was later marked fixed and the present trace derives `hand` without any visible A-restoration change, that earlier citation should not be promoted into row authority [Germanic/docs/DEV_NOTES.md:1697-1724; Germanic/docs/debug_snapshots/oe_full_trace_report_2026-03-11.txt:5906-5941].
- The March `*nd`-cluster audit is the one place where DEV_NOTES gives a row-specific judgment that still matters. Even there, its scope is narrow: it confirms dental representation (`d`, not `ð`), not a whole lexeme dossier [Germanic/docs/DEV_NOTES.md:7538-7570].

## Open questions for later work

- If row 2054 later gets a full packet or memo, collect direct handbook support for PGmc `*handuz` / OE feminine u-stem `hand` instead of continuing to rely mainly on hand-as-comparator material embedded in the `duru` note.
- If future reporting normalizes proto accent notation, decide whether the live TSV's `*xánduz` and the snapshots' `*xanduz` should be explicitly harmonized in prose or simply treated as equivalent project spellings for the same input.
- If later lexeme reporting starts separating lexeme-level headword from active derivational input more aggressively, keep explicit that row 2054 currently has no alternate paradigm-cell solution in play: `PROTO` and `PROTOFORM` are the same, and no DEV_NOTES fragment proposes changing that.
