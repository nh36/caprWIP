---
row_id: 2305
concept: yarn
counterpart: ġearn
proto: "*gárną"
protoform: "*gárną"
derivation_class: regular
source_file: Germanic/data/germanic-aligned-final.tsv
linked_packet_file: Germanic/docs/lexeme_reports/packets/2305-yarn-ġearn.md
linked_research_memo_file: Germanic/docs/lexeme_reports/research_memos/2305-yarn-ġearn.md
linked_dossier_or_analysis_files: []
current_status: "Note-bearing regular OE row; live trace reaches ġearn; no dedicated row-specific DEV_NOTES block located."
needs_literature_agent: false
---

# DEV_NOTES material — 2305 yarn / ġearn

## Current row state
The live row is `2305 | yarn | ġearn | *gárną | *gárną | regular`, with the only live row note reading `Proto: oblique *garnăn→*garną (n. a-stem nom.sg.; Kroonen)` [Germanic/data/germanic-aligned-final.tsv:1454-1457]. `coverage_audit.md` flags the row for report coverage because `NOTE` is present, not because of a derivational failure [Germanic/docs/lexeme_reports/coverage_audit.md:169-177]. There is no current manifest entry for 2305 in `report_manifest.tsv` [Germanic/docs/lexeme_reports/report_manifest.tsv:1-13], and `oe_known_problems.tsv` does not list this proto or row among the standing OE exceptions [Germanic/data/oe_known_problems.tsv:1-8].

The current generated OE trace is successful and should be treated as the present pipeline state, not as independent lexical authority: `PROTO: *garną`, `EXPECTED: ġearn`, `OUTPUTS: ġearn`; the traced sequence is `AngloFrisianBrightening: *g*æ*r*n*ą`, `BreakingLengthening: *g*ea*r*n*ą`, `VelarPalatalization: *ʤ*ea*r*n*ą`, then orthographic/surface `ġearn` [docs/debug_snapshots/oe_full_trace_report.txt:16998-17018; docs/debug_snapshots/oe_full_trace_report.txt:17023-17024; docs/debug_snapshots/oe_full_trace_report.txt:17041-17051]. The packet matches that state and also records no row-level `DEV_NOTES`, dossier, or analysis hits [Germanic/docs/lexeme_reports/packets/2305-yarn-ġearn.md:17-23; Germanic/docs/lexeme_reports/packets/2305-yarn-ġearn.md:45-65].

## Development-note summary
No row-specific DEV_NOTES block currently survives for row 2305. The packet explicitly records `_None_` under both row-level and background `DEV_NOTES` hits, so this slice must be built conservatively from the live row, the current trace, the packet, the research memo, and shared-background DEV_NOTES material rather than from a dedicated 2305 note block [Germanic/docs/lexeme_reports/packets/2305-yarn-ġearn.md:45-61].

The main working distinction is three-way and should stay explicit. Comparative literature may cite lemma/stem-style `*garna-`, and the TSV note mentions oblique `*garnăn`, but the project’s actual derivational input is `PROTO = PROTOFORM = *gárną`; the OE target is the attested noun `ġearn`, corresponding to dictionary `gearn` [Germanic/data/germanic-aligned-final.tsv:1454-1457; Germanic/docs/lexeme_reports/research_memos/2305-yarn-ġearn.md:44-50]. On current evidence this is a representational caution, not a modelling failure: the row is still a regular derivation, not an `oe_known_problems.tsv` exception and not a paradigm-cell workaround [Germanic/docs/lexeme_reports/research_memos/2305-yarn-ġearn.md:60-70].

Shared DEV_NOTES background remains relevant because the live trace uses exactly the chronology those notes describe: front-vowel creation before `rC`/`lC` breaking environments, then velar palatalization before front vowels, then OE orthographic marking of palatal outcomes [Germanic/docs/DEV_NOTES.md:2439-2446; Germanic/docs/DEV_NOTES.md:2630-2632]. That background explains why the current pipeline reaches `ġearn` from `*gárną/*garną` without needing any row-specific exception [docs/debug_snapshots/oe_full_trace_report.txt:17016-17024; Germanic/docs/lexeme_reports/research_memos/2305-yarn-ġearn.md:50-58].

## Relevant DEV_NOTES fragments

### Fragment 1
- **Source heading:** `PGmc→OE TODOs (consolidated)` / `PGmc→OE chronology audit (2025-12-21)`
- **Source line hint:** `Germanic/docs/DEV_NOTES.md:2422-2446`
- **Fragment type:** shared-background-only
- **Status:** active background
- **Issue tags:** `oe-chronology`, `breaking`, `velar-palatalization`, `oe-stack-separation`
- **Recommended next use:** Use this fragment to justify the live order of operations for the row (`*a > *æ > *ea` before `rn`, then palatal `g > ġ` before the front-vocalic outcome), not as row-specific lexical evidence.
- **Shared-with rows if relevant:** OE rows whose successful outcomes depend on breaking before `rC/lC` plus front-vowel-triggered palatalization.

DEV_NOTES states, in the condensed chronology, that “Breaking/retraction of front vowels before h, rC, lC (and some w contexts) is dialect-conditioned and not uniform across OE” and that “Palatalization of velars (k/g, and sc) before front vowels yields ċ/ġ alternations and later phonemic splits” [Germanic/docs/DEV_NOTES.md:2440-2446]. It also insists on the OE-specific stack as a separate PGmc→OE pipeline rather than borrowing later English rules [Germanic/docs/DEV_NOTES.md:2422-2430]. For row 2305 this is shared background only, but it maps cleanly onto the live trace: brightening creates `*æ`, breaking before `rn` yields `*ea`, and only then does the initial velar palatalize to `*ʤ`, giving the pre-orthographic basis of `ġearn` [docs/debug_snapshots/oe_full_trace_report.txt:17016-17024].

### Fragment 2
- **Source heading:** discussion of initial palatalization chronology (`gift` / `giefan` comparison)
- **Source line hint:** `Germanic/docs/DEV_NOTES.md:6484-6518`
- **Fragment type:** shared-background-only with embedded primary-source quotation
- **Status:** active background
- **Issue tags:** `initial-g-palatalization`, `campbell-quotation`, `front-vowel-conditioning`
- **Recommended next use:** Use when the row file needs explicit justification for dotted initial `ġ-` as a palatal outcome rather than a separate lexeme spelling.
- **Shared-with rows if relevant:** OE rows with initial `ġ-` derived from front-vowel-conditioned palatalization.

This DEV_NOTES discussion is not about `ġearn`, but it preserves a directly relevant palatalization principle and a useful embedded citation. The notes summarize the chronology as “Initial `*g` palatalizes before front vowel” and quote Campbell: “Examples of initial palatal sounds are: ... **gift gift**, gifre greedy, ginnan begin, gefan (W-S giefan) give...” [Germanic/docs/DEV_NOTES.md:6490-6501; Germanic/docs/DEV_NOTES.md:6516-6518]. For row 2305, the front-vowel trigger is not inherited unchanged from the proto spelling but created in the OE chain represented by brightening plus breaking; once the trace has `*ʤ*ea...`, the palatalized onset is expected, and the memo is right to treat dictionary `gearn` and project `ġearn` as the same noun under different editorial normalization [docs/debug_snapshots/oe_full_trace_report.txt:17016-17024; Germanic/docs/lexeme_reports/research_memos/2305-yarn-ġearn.md:54-58].

### Fragment 3
- **Source heading:** `OE orthography cleanup + reports (2026-01-18)`
- **Source line hint:** `Germanic/docs/DEV_NOTES.md:2630-2632`
- **Fragment type:** shared-background-only
- **Status:** active background
- **Issue tags:** `orthography`, `palatal-marking`, `editorial-normalization`
- **Recommended next use:** Use this only to interpret project spelling conventions; it does not independently prove the lexeme or its semantics.
- **Shared-with rows if relevant:** All OE rows whose outputs use dotted palatal markers (`ġ`, `ċ`, `sċ`).

The orthography note says that `OldEnglishOrthography` now handles dotted palatal outcomes explicitly, including mappings where `{ʤ}` still surfaces as `ġ` [Germanic/docs/DEV_NOTES.md:2630-2632]. For this row, that matters because lexical sources in the memo are cited as `gearn`, while the project counterpart is `ġearn`; the difference should be read as project orthographic normalization of a palatal initial, not as evidence for a separate target form [Germanic/docs/lexeme_reports/research_memos/2305-yarn-ġearn.md:54-58]. This fragment is therefore shared background only, but it is the best surviving DEV_NOTES material for explaining why the trace’s `*ʤ...` ends as orthographic `ġearn` [docs/debug_snapshots/oe_full_trace_report.txt:17023-17024; docs/debug_snapshots/oe_full_trace_report.txt:17050-17051].

## Superseded or diagnostic material
There is no surviving row-specific DEV_NOTES fragment to preserve here; that absence itself is diagnostic and should be stated plainly. The packet records `_None_` for row-level `DEV_NOTES` hits and `_None_` again for supporting/background `DEV_NOTES` hits, so any attempt to reconstruct a dedicated 2305 DEV_NOTES block would be speculative [Germanic/docs/lexeme_reports/packets/2305-yarn-ġearn.md:49-61].

The live row note is still important but should be classed as diagnostic/shared background rather than as a replacement for row-specific DEV_NOTES prose: `Proto: oblique *garnăn→*garną (n. a-stem nom.sg.; Kroonen)` captures comparative morphology, yet the memo correctly warns that this wording can mislead a reader into treating oblique `*garnăn` as the derivational input when the live row actually runs on `*gárną` [Germanic/data/germanic-aligned-final.tsv:1454-1457; Germanic/docs/lexeme_reports/research_memos/2305-yarn-ġearn.md:17-24; Germanic/docs/lexeme_reports/research_memos/2305-yarn-ġearn.md:62-64]. The current debug trace is likewise diagnostic only: it confirms that the pipeline presently succeeds, but it does not settle lexicographic questions by itself [docs/debug_snapshots/oe_full_trace_report.txt:16998-17001; Germanic/docs/lexeme_reports/research_memos/2305-yarn-ġearn.md:27-40].

## Open questions for later work
1. The live row is stable, but the TSV note is still compressive. Later cleanup should decide whether to rewrite it so that `*gárną` remains the explicit project input while `*garna-` / oblique `*garnăn` are labelled comparative background only [Germanic/docs/lexeme_reports/research_memos/2305-yarn-ġearn.md:62-64; Germanic/docs/lexeme_reports/research_memos/2305-yarn-ġearn.md:78-84].
2. If a future full report or dossier is built, it may be worth importing direct noun-only lexical support (`gearn (e) n.`, `Filatum, gearn`) into row-local documentation so the noun is insulated from homographic verbal `gearn` material; for the present slice that evidence survives only through the memo [Germanic/docs/lexeme_reports/research_memos/2305-yarn-ġearn.md:32-38; Germanic/docs/lexeme_reports/research_memos/2305-yarn-ġearn.md:52-58].
3. The live TSV keeps accented `*gárną`, while the generated trace shows unaccented internal `*garną`. That normalization difference is not currently a blocker, but if future tooling compares row text directly against trace text, the distinction should be documented rather than mistaken for a proto mismatch [Germanic/data/germanic-aligned-final.tsv:1454-1457; docs/debug_snapshots/oe_full_trace_report.txt:16998-17003].
