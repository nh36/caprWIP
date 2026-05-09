---
row_id: 2244
concept: thanks
counterpart: þanc
proto: *θánkaz
protoform: *θánkaz
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files: Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2244 thanks / þanc

## Current row state

- The live OE row is `2244`, `CONCEPT thanks`, `COUNTERPART þanc`, `PROTO *θánkaz`, `PROTOFORM *θánkaz`, `DERIVATION_CLASS regular` [Germanic/data/germanic-aligned-final.tsv:1217-1217].
- The live TSV note is already the most important row-level correction: `TSV: þancas (nom.pl.) → þanc (nom.sg.); *θankăz is masc. a-stem nom.sg.` [Germanic/data/germanic-aligned-final.tsv:1217-1217]. This means the current row is a singular noun row, not a plural-paradigm row.
- `PROTO` and `PROTOFORM` are the same here. The row is not using a substitute preform, an oblique paradigm cell, or the related verbal derivative `*θánkijaną`; it is simply the noun `*θánkaz -> þanc` [Germanic/data/germanic-aligned-final.tsv:1217-1217; @Kroonen2013, s.v. "*þanka-"; @Orel2003, s.v. "*þankaz"].
- `oe_known_problems.tsv` has no row-specific entry for `2244`, `*θánkaz`, or `þanc`, so the project is not currently treating this item as an unresolved OE exception [Germanic/data/oe_known_problems.tsv:1-8].
- `coverage_audit.md` still lists `| 2244 | thanks | þanc | regular | no | - | - | - | none |`, and no row-specific packet or research memo stem was found, so the slice uses the canonical row-based filename [Germanic/docs/lexeme_reports/coverage_audit.md:388-388].
- The current published derivation trace is an exact match: `PROTO: *θánkaz`, `EXPECTED: þanc`, `OUTPUTS: þanc`, with the visible chain `PGmc Final Z Deletion: *θánka` and `PWGmc Final Bare A Loss: *θánk`, then orthographic `þanc` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:5131-5150].

## Detailed development-note summary

The live row is now a straightforward noun derivation and the slice should preserve that simplicity rather than re-importing older debugging noise. Comparative lexicography supports a masculine noun meaning ‘thanks’: Kroonen gives `*þanka- m. 'thanks'` with OE `þanc`, and Orel likewise gives `*þankaz sb.m.` with OE `ðanc`/`þanc` among the reflexes [@Kroonen2013, s.v. "*þanka-"; @Orel2003, s.v. "*þankaz"]. The live TSV note makes the row-level consequence explicit: this slice is about nominative-singular `þanc`, not about plural `þancas`, and not about a different member of the `þank-` word-family [Germanic/data/germanic-aligned-final.tsv:1217-1217].

Surviving DEV_NOTES support is thin and mostly diagnostic rather than lexeme-dossier material. The only explicit DEV_NOTES mention of this noun is the 2025-12-23 fronting/palatalization audit, which says: “prioritize fronting/breaking changes that create front‑vowel contexts (esp. for *bōkō, *θankăz, *dranką, *fleugăną, *xunăgą), then re‑check palatalization buckets” [Germanic/docs/DEV_NOTES.md:2593-2593]. In context, that note belongs to an older debugging phase where `*θankăz` was grouped with rows whose expected outputs were being over-read as requiring an upstream front-vowel trigger [Germanic/docs/DEV_NOTES.md:2588-2593]. For row `2244`, that is no longer current row policy. The live row now targets the regular singular noun `þanc`, and the published trace already derives that target exactly [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:5131-5150].

The crucial replacement-note conclusion is therefore negative as much as positive. DEV_NOTES does **not** currently preserve a dense row-local argument that `þanc` needed a special OE repair, a fronted vowel, or a palatalized outcome. What it preserves is evidence that the lexeme once sat inside a broader upstream-context bucket. The live repository state has since narrowed the row to the nominative singular and removed any present need for that bucket diagnosis [Germanic/data/germanic-aligned-final.tsv:1217-1217]. Later writers should therefore treat the DEV_NOTES line as project chronology, not as current authority against the exact-match noun row.

One distinction is worth spelling out because the repo contains nearby `þank-` material. The related verb row `2248 think / þenċan` uses `*θánkijaną` and treats noun `*θankăz` only as etymological background, not as its direct row input [Germanic/docs/lexeme_reports/research_memos/2248-think-þenċan.md:32-40]. That separation should remain firm here as well: row `2244` is the noun `*θánkaz -> þanc`; row `2248` is the weak verb `*θánkijaną -> þenċan`. Collapsing those rows would blur exactly the `PROTO` / `PROTOFORM` / `COUNTERPART` distinctions that the live TSV now keeps clear.

Given that profile, this slice is a valid replacement working note but not yet a strong indexing candidate. The current row is well behaved, but the DEV_NOTES attachment is only one short shared diagnostic fragment plus current trace/TSV confirmation. That is enough for careful documentation and probably not enough for a useful `index.tsv` entry yet.

## Relevant DEV_NOTES fragments with line-based refs

### DEV_NOTES:line-2588-2593

- Source heading: `OE palatalization vs fronting/umlaut split (2025-12-23)`
- Source line or section hint: `lines 2588-2593`
- Fragment type: `shared_diagnostic_fragment`
- Status: `diagnostic_only`
- Issue tags: `fronting_context`; `palatalization_bucket`; `project_history`
- Recommended next use: `use_as_project_history_only`

This is the only explicit DEV_NOTES fragment currently attachable to row `2244`. It says the remaining “palatalization missing” cases were not true palatalization-rule failures because the required front-vowel environment never arose, then names `*θankăz` among the rows to prioritize for upstream fronting/breaking work [Germanic/docs/DEV_NOTES.md:2590-2593].

> “prioritize fronting/breaking changes that create front‑vowel contexts (esp. for *bōkō, *θankăz, *dranką, *fleugăną, *xunăgą), then re‑check palatalization buckets.” [Germanic/docs/DEV_NOTES.md:2593-2593]

For the present row, the fragment is useful only as chronology. It records that `*θankăz` once sat in a broad upstream-context diagnostic bucket; it does **not** now override the live singular-noun row `*θánkaz -> þanc`, which already derives correctly and no longer depends on a front-vowel rescue [Germanic/data/germanic-aligned-final.tsv:1217-1217; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:5131-5150].

## Superseded or diagnostic material

- A nearby older diagnostic outside DEV_NOTES shows why the row needed the TSV clarification. `non_firing_rules_analysis.md` once listed `*θankăz -> þænc (expected þancas)`, i.e. both a fronted singular output and a plural target [Germanic/docs/non_firing_rules_analysis.md:517-520]. The live row note explicitly supersedes that state by converting the row from plural `þancas` to nominative singular `þanc` and by noting that `*θankăz` is a masculine a-stem nominative singular [Germanic/data/germanic-aligned-final.tsv:1217-1217].
- The related verbal derivation `*θankăz -> *θankijăną` belongs to row `2248 think / þenċan`, not to this noun row. The research memo for `2248` is useful background because it explicitly says the noun is only etymological background there, but that memo should not be mined as if it were direct lexical authority for row `2244` [Germanic/docs/lexeme_reports/research_memos/2248-think-þenċan.md:35-40].
- No surviving material was found that argues for a different current `PROTOFORM`, a different `COUNTERPART`, or a non-regular derivation class for row `2244`. The live exact-match trace and the absence of an `oe_known_problems.tsv` entry are therefore meaningful, not accidental [Germanic/data/oe_known_problems.tsv:1-8; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:5131-5150].

## Open questions for later work

- If a later final report is written, add a direct OE dictionary citation for the singular/plural contrast (`þanc` vs. `þancas`) so the row does not rely mainly on the TSV note for that paradigm-cell decision.
- If more DEV_NOTES material for `*θankăz` turns up, check whether it reflects the old plural-target/fronting diagnostics or genuinely bears on the now-live singular noun row.
- Keep row `2244` noun `þanc` and row `2248` verb `þenċan` explicitly separate in any later report or index proposal; the etymological relation is real, but the row inputs and targets are different.
