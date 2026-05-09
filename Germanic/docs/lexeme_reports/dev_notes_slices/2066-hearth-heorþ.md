---
row_id: 2066
concept: hearth
counterpart: heorþ
proto: "*xérθaz"
protoform: "*xérθaz"
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
  - Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md
  - Germanic/docs/debug_snapshots/oe_full_trace_report.txt
  - Germanic/docs/germanic_transducer_report.md
current_status: exact_match_no_row_specific_dev_notes_block
needs_literature_agent: no
---

# DEV_NOTES material — 2066 hearth / heorþ

## Current row state

- The live OE row is `ID 2066`, `CONCEPT hearth`, `COUNTERPART heorþ`, `PROTO *xérθaz`, `DERIVATION_CLASS regular`. No row-relevant file consulted here preserves a distinct alternative `PROTOFORM`, so this slice keeps `PROTO` and `PROTOFORM` identical rather than inventing a second reconstruction layer [Germanic/data/germanic-aligned-final.tsv:529-529].
- `coverage_audit.md` still marks the row as uncovered — `| 2066 | hearth | heorþ | regular | no | - | - | - | none |` — and `report_manifest.tsv` still contains only the pilot set, with no row-2066 report entry. There is therefore no surviving packet or manifest-linked lexeme report to supersede DEV_NOTES for this row [Germanic/docs/lexeme_reports/coverage_audit.md:273-273; Germanic/docs/lexeme_reports/report_manifest.tsv:1-13].
- `oe_known_problems.tsv` has no entry for row `2066`, for `hearth`, for `heorþ`, or for `*xérθaz`, so the row is not currently tracked as a live OE exception or wontfix bucket [Germanic/data/oe_known_problems.tsv:1-8].
- The row does have a lightweight attestation breadcrumb outside DEV_NOTES: `old_english_wiktionary.tsv` lists `hearth	heorþ	inh	template:inh	hearth` [Germanic/data/old_english_wiktionary.tsv:130-130].
- The current derivation is exact in both the compact/publish trace and the full trace. The visible route is `*xérθaz` → `PGmc Final Z Deletion: *xérθa` → `PWGmc Final Bare A Loss: *xérθ` → `OEBreaking: *xéorθ` → `OEVelarFricativePalatalization: *çéorθ` → orthographic `h*éorþ` / `heorþ` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2221-2241; Germanic/docs/debug_snapshots/oe_full_trace_report.txt:14620-14733].
- A separate analysis note also still groups this lexeme with the front-vowel `*x` cluster and explicitly lists `*xerθăz → heorþ` among the OE items relevant to velar-fricative palatalization diagnostics. That support is current-state analysis, not DEV_NOTES, but it helps explain why the row’s post-breaking `*x` stage matters [Germanic/docs/germanic_transducer_report.md:54-57].

## Development-note summary

No dedicated row-2066 DEV_NOTES block survives. Nothing in `Germanic/docs/DEV_NOTES.md` reads like a hearth-specific lexeme dossier with attestation, literature review, or a bespoke repair decision. The best surviving material is shared and should be labeled that way: one still-useful OE-side diagnostic about breaking in `*erC/*rθ` environments, plus one later OE→Modern classification note that groups `earth/hearth` together as inherited `*rθ` material [Germanic/docs/DEV_NOTES.md:2354-2374,2575-2578].

That means the row now has to be reconstructed conservatively from two things: (1) current exact row state and live traces, and (2) shared DEV_NOTES material that illuminates the same phonological corridor without pretending to be row-local proof. The row-specific facts that remain strongest are current, not archival: `heorþ` is the exact present output, the row is not in `oe_known_problems.tsv`, and the surviving analysis trail treats the development as regular `*e > eo` breaking plus expected orthographic `h`/`þ` surface resolution, not as an unresolved exception [Germanic/data/oe_known_problems.tsv:1-8; Germanic/docs/debug_snapshots/oe_full_trace_report.txt:14620-14733].

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-2575-2578

- Source heading: `OE breaking reorder + diagnostics (2025-12-22)`
- Source line hint: `2575-2578`
- Fragment type: `shared_background_diagnostic`
- Status: `current_for_rule_history_but_not_row_specific`
- Issue tags: `oe_breaking`; `erC_cluster`; `rθ_environment`; `heorþ_via_eo`
- Recommended next use: `use as the main surviving DEV_NOTES anchor for why this row belongs to the regular OE breaking pipeline`
- Shared-with rows if relevant: `1999 earth / eorþe; 2065 heart / heorte; 2073 herd / heord; other *erC rows`

This is the most useful surviving DEV_NOTES material for row 2066 even though it is not lexeme-specific. DEV_NOTES records that “**Breaking now precedes GH-marking and W-glide** so the conditioning consonants are still visible when OE breaking applies,” and then preserves the tracer result that the rebuilt probe “shows `*bergą → *eo`, `*bardăz → *ea`, `*erθo → *eo`, `*fextăną → *eo` at `BreakingLengthening`” [Germanic/docs/DEV_NOTES.md:2575-2578]. For `heorþ`, that is shared-background-only support, but it is genuinely material: it tells us the project’s intended analysis of the `*erθ` corridor is ordinary OE breaking before later cleanup, not a row-specific exception mechanism.

The current full trace matches that shared diagnostic cleanly. After `PGmc Final Z Deletion` and `PWGmc Final Bare A Loss`, the row reaches bare `*xérθ`; then `OEBreaking` gives `*xéorθ`, and only afterward does `OEVelarFricativePalatalization` produce `*çéorθ`, which surfaces orthographically as `heorþ` [Germanic/docs/debug_snapshots/oe_full_trace_report.txt:14652-14733]. So the DEV_NOTES fragment survives as diagnostic support for the regular vowel-development side of the row. It should not be oversold as direct attestation evidence, but it does preserve the exact kind of rule-order memory that would matter if this row ever regressed to non-breaking `herþ`-type output.

### DEV_NOTES:line-2354-2374

- Source heading: `Modern English (OE→Modern) roadmap — paused` / `Detailed blueprint` / `Consonant outcomes`
- Source line hint: `2354-2374`
- Fragment type: `shared_background_only_downstream_note`
- Status: `current_but_downstream`
- Issue tags: `earth_hearth_bucket`; `native_rθ`; `theta_retention`; `not_primary_oe_support`
- Recommended next use: `preserve only as downstream bucket memory separating inherited *rθ from later *rd analogical outcomes`
- Shared-with rows if relevant: `1999 earth / eorþe; 2073 herd / heord; later English reflex rows if added`

This fragment is explicit about `hearth`, but it is explicit in a downstream way. DEV_NOTES says the paused OE→Modern roadmap should “**Note explicitly why RP keeps /θ/ in `earth/hearth` but /d/ in `herd/word/sword` (OE retention vs. later analogical leveling)**,” then restates the same split more formally: “**native `{*rθ/ð}` clusters retain /θ/ in RP (`earth/hearth`), while `{*rd}` words level to /d/ in late ME (`herd/word/sword/bird`)**” [Germanic/docs/DEV_NOTES.md:2357-2358,2373-2374].

For row 2066, that is useful but only as shared-background-only support. It does not establish the OE target `heorþ`; it does not quote a primary source for this lexeme; and it belongs to a section DEV_NOTES itself labels as intentionally separated from PGmc→OE work [Germanic/docs/DEV_NOTES.md:2354-2355]. What it does preserve is an important project distinction: `hearth` is to remain grouped with inherited `*rθ` material, not with the quite different later `*rd > d` bucket. If later documentation rebuilds consonant-family links across rows, this fragment should be cited for that classification and not treated as the main philological warrant for the OE row.

## Superseded or diagnostic material

- No row-specific `hearth / heorþ / *xérθaz` DEV_NOTES dossier was found. That absence needs to stay explicit: the present slice is necessarily conservative because the surviving DEV_NOTES evidence is shared-background and diagnostic rather than lexeme-local [Germanic/docs/DEV_NOTES.md:2354-2374,2575-2578].
- The 2025-12-11 and 2025-12-06 English sandbox notes are relevant only as superseded downstream diagnostics. DEV_NOTES there admits that `EnglishSandboxRhoticBreaking` was “**a grab-bag of lexeme-specific rewrites**” and even floated a special case `{*erθo → {*erθ}}` for the OE→Modern sandbox [Germanic/docs/DEV_NOTES.md:1792-1800]. That material should not be reused as evidence for the PGmc→OE row; it records an abandoned ad hoc downstream strategy, not a stable analysis of OE `heorþ`.
- The 2025-12-22 breaking fragment above remains useful, but it is still diagnostic in genre. It shows the relevant pathway is behaving and preserves the probe quotation, yet it never names row 2066 directly and should therefore be cited as shared rule-history support rather than as a row-specific note [Germanic/docs/DEV_NOTES.md:2575-2578].
- Current row state strongly suggests that no live repair is needed: the row is exact in the published derivation trace and absent from `oe_known_problems.tsv`. Any future attempt to turn this slice into an exception memo would therefore need stronger evidence than the surviving DEV_NOTES material currently provides [Germanic/data/oe_known_problems.tsv:1-8; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2221-2241].

## Open questions for later work

- If a later lexeme packet is commissioned for row 2066, the first literature task should be attestation-focused rather than rule-fix-focused: replace the present Wiktionary breadcrumb with direct lexicographic or handbook support for OE `heorþ`, because the surviving DEV_NOTES material is not a lexeme dossier [Germanic/data/old_english_wiktionary.tsv:130-130].
- If future indexing links rows by shared DEV_NOTES material, row 2066 should probably be grouped first with regular OE `*erC/*rθ` breaking rows and only secondarily with the downstream `earth/hearth` vs. `herd/word/sword` consonant bucket. Those are different kinds of evidence and should not be collapsed [Germanic/docs/DEV_NOTES.md:2357-2374,2575-2578].
- If the OE pipeline ever regresses on this row, the first check should be rule order around `PWGmc Final Bare A Loss`, `OEBreaking`, and `OEVelarFricativePalatalization`, because the current exact trace shows that sequence doing essentially all the work [Germanic/docs/debug_snapshots/oe_full_trace_report.txt:14676-14733].
