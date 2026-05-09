---
row_id: 2065
concept: heart
counterpart: heorte
proto: *xértōn
protoform: *xértōn
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
  - Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md
  - Germanic/docs/debug_snapshots/oe_full_trace_report_2026-03-11.txt
current_status: "No surviving row-specific DEV_NOTES block; published trace still reaches heorte, but current sandbox snapshots regress after ProtoRhoticFronting/PostVocalicRLoss."
needs_literature_agent: no
---

# DEV_NOTES material — 2065 heart / heorte

## Current row state

- The live TSV row is stable and bare: `ID 2065`, `CONCEPT heart`, `COUNTERPART heorte`, `PROTO *xértōn`, `PROTOFORM *xértōn`, `DERIVATION_CLASS regular`, with only source-history strings in `HISTORY` and no row-local explanatory note. `PROTO` and `PROTOFORM` are still identical here; there is no live OE-specific substitute input for the row [Germanic/data/germanic-aligned-final.tsv:525-525].
- Coverage infrastructure is still empty for this row. `coverage_audit.md` marks row `2065` as `regular | no | - | - | - | none`, and `report_manifest.tsv` still contains only the older pilot subset, with no entry for row `2065` or for `heart/heorte` [Germanic/docs/lexeme_reports/coverage_audit.md:272-272; Germanic/docs/lexeme_reports/report_manifest.tsv:1-13].
- `oe_known_problems.tsv` has no surviving entry for row `2065`, for `heart`, for `heorte`, or for `*xértōn`, so the row is not currently being tracked as an acknowledged OE exception bucket [Germanic/data/oe_known_problems.tsv:1-8].
- Repo-local lexical confirmation is straightforward: `old_english_wiktionary.tsv` has `heart	heorte	inh	template:inh	heart`, which matches the live counterpart exactly [Germanic/data/old_english_wiktionary.tsv:129-129].
- The published derivation snapshot is clean and fully regular. The compact published report gives `PROTO: *xértōn`, `EXPECTED: heorte`, `OUTPUTS: heorte`, and the stated OE side of the chain is `OE Breaking: *xéortǭ`, `OE Velar Fricative Palatalization: *çéortǭ`, `OE Unstressed Long Vowel Shortening: *çéortæ`, `OE Unstressed AE Merger: *çéorte`, followed by orthographic `h*éorte` and surface `heorte` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2200-2220]. The fuller trace shows the same path in more granular rule order, with Northwest Germanic n-stem `n` loss first creating `*x*e*r*t*ǭ`, then breaking, palatalization of initial velar fricative to `ç`, shortening of unstressed long `ǭ` to `æ`, and final cleanup to `*ç*eo*r*t*e > heorte` [Germanic/docs/debug_snapshots/oe_full_trace_report_2026-03-11.txt:6400-6436].
- Current sandbox diagnostics are worse than the published trace and should be labeled as such. `old_english_sandbox_results_current.json` records row-local metadata for `heart / *xertōn / heorte` but gives `"outputs": []`, and the staged sandbox file marks `"first_failing_stage": "ProtoRhoticFronting"` before drifting into a bad path where `PostVocalicRLoss` deletes the `r`, orthography shows `hæ*t*əʊ*n`, and the fallback surface ends at `hertōn` [Germanic/tmp/old_english_sandbox_results_current.json:1216-1220; Germanic/tmp/old_english_sandbox_results_with_stages.json:19036-19175]. That material is diagnostic for current debugging only; it is not evidence that the live row target should move away from `heorte`.

## Development-note summary

No dedicated `heart / heorte` DEV_NOTES dossier survives. That should be stated plainly. The surviving DEV_NOTES support for row `2065` is limited to two small but useful fragments, both embedded inside broader A-restoration work on feminine `*-ōn` material rather than a heart-specific note [Germanic/docs/DEV_NOTES.md:2863-2889; Germanic/docs/DEV_NOTES.md:3799-3854].

Those fragments do not propose any row rewrite. Instead, they preserve a narrow but important claim: `*xertōn > heorte` sits **outside** the A-fronting/A-restoration problem set because its root vowel at the relevant stage is already `*e`/`eo`, not an `*a` that would need restoration. DEV_NOTES first says this explicitly in prose — “`*xertōn → heorte has {*e} from breaking, not {*a}, so no AFB issue. Will monitor.`” — and later repeats the same conclusion in the fem. `ōn`-stem regression table: `| *xertōn | heorte | heorte | heorte | unchanged (*e root) |` [Germanic/docs/DEV_NOTES.md:2884-2889; Germanic/docs/DEV_NOTES.md:3844-3853].

So the conservative working reading for row `2065` is: there is **no surviving row-specific DEV_NOTES block**, but there is surviving row-specific **negative evidence** that the lexeme does not belong to the A-restoration failure bucket being discussed nearby. The live dataset therefore keeps `PROTO = PROTOFORM = *xértōn` and target `heorte`, and the published trace still supports that regular pathway [Germanic/data/germanic-aligned-final.tsv:525-525; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2200-2220].

## Relevant DEV_NOTES fragments

### Germanic/docs/DEV_NOTES.md:2863-2889

- Source heading: `### A-Restoration Gap for {*ô}`
- Source line hint: `lines 2863-2889`
- Fragment type: `row_named_negative_evidence_with_shared_background`
- Status: `current_background`
- Issue tags: `a_restoration`; `afb_scope`; `fem_ōn_stems`; `breaking`; `e_root`
- Recommended next use: `cite when explaining that heart/heorte was explicitly checked and excluded from the A-restoration bug class`
- Shared-with rows if relevant: `same broader fem. ōn / ōn-stem A-restoration discussion; directly adjacent to makô and tungōn examples`

This is the nearest thing to an explicit row mention in surviving DEV_NOTES prose. The section is not about `heart` as such; it is about an A-restoration trigger gap for trimoric `*ô`. But when DEV_NOTES asks whether related nasalized `*ǭ` cases could create similar trouble, it names this row directly and says: “`other fem. n-stems with {*a} in root: *xertōn → heorte has {*e} from breaking, not {*a}, so no AFB issue. Will monitor.`” [Germanic/docs/DEV_NOTES.md:2884-2889]. That sentence should be preserved almost verbatim because it is the clearest surviving statement of row scope.

Its evidential status is limited but real. This is **row-specific support only in a negative/scoping sense**: it does not narrate the whole derivation, discuss manuscript forms, or argue about lemma choice. What it does do is rule out one specific class of false diagnosis. For row `2065`, the point is that the troublesome `*a > *æ > *a` restoration cycle under discussion elsewhere is irrelevant because the heart-word’s vowel at the crucial OE stage is already the broken `e/eo` outcome, not a fronted `a` needing restoration [Germanic/docs/DEV_NOTES.md:2867-2889].

### Germanic/docs/DEV_NOTES.md:3799-3854

- Source heading: `### Case 3: *flaskō → *flaskōn (OE flasce 'flask, bottle')`
- Source line hint: `lines 3799-3854`
- Fragment type: `shared_regression_table_with_row_entry`
- Status: `current`
- Issue tags: `regression_check`; `a_restoration_fix`; `fem_ōn_stems`; `unchanged_e_root`
- Recommended next use: `cite when documenting that heart/heorte remained stable after the *ǭ trigger fix`
- Shared-with rows if relevant: `*wartōn`; `*swalwōn`; `*sapōn`; `*laimōn`; `*marōn`

This fragment is still not a heart dossier, but it is the strongest later confirmation that the row stayed correct after the `*ǭ` A-restoration repair. The surrounding section explains the `flaskōn` fix and then runs a regression table over “all other fem. ōn-stems verified” [Germanic/docs/DEV_NOTES.md:3830-3845]. In that table the heart row appears exactly as `| *xertōn | heorte | heorte | heorte | unchanged (*e root) |` [Germanic/docs/DEV_NOTES.md:3846-3853].

For slicing purposes, that table line matters in two ways. First, it is a direct statement that the row already matched before the fix and still matched after it; no hidden repair logic was introduced for `heorte`. Second, the parenthetical “`(*e root)`” is the compressed explanation for why: the row belongs to the same broad feminine weak-noun neighborhood as the other checked forms, but unlike the `*a`-root cases that motivated the repair, it is insulated by its `e`-root/broken-vowel history [Germanic/docs/DEV_NOTES.md:3844-3853]. Treat this as **shared-background support with an explicit row entry**, not as an autonomous lexeme note.

## Superseded or diagnostic material

- The conspicuous DEV_NOTES hits at `10805`, `10823`, `10886`, `11204`, and `11274` are **not row-2065 lexeme notes at all**. They refer to pipeline line numbers near `2065` inside `germanic.txt` during nasalization and i-umlaut rule-order debugging [Germanic/docs/DEV_NOTES.md:10798-10825; Germanic/docs/DEV_NOTES.md:11202-11227,11272-11274]. They should not be cited as evidence about `heart / heorte`.
- The published trace files are **diagnostic/current-state support**, not DEV_NOTES replacements by themselves. They confirm that the intended regular derivation still lands on `heorte`, but they do not add philological argument beyond the limited DEV_NOTES scoping notes above [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2200-2220; Germanic/docs/debug_snapshots/oe_full_trace_report_2026-03-11.txt:6400-6436].
- The current sandbox `[]` / `ProtoRhoticFronting` / `hertōn` material is likewise **diagnostic only**. It is useful because it shows a present implementation regression affecting this row’s debug pipeline, but it is not a reason to alter the row target, the proto columns, or the interpretation of the surviving DEV_NOTES evidence [Germanic/tmp/old_english_sandbox_results_current.json:1216-1220; Germanic/tmp/old_english_sandbox_results_with_stages.json:19036-19175].
- Because no true row-specific DEV_NOTES block survives, there is also no superseded row-local alternative target to preserve here. The surviving notes do **not** argue for changing `heorte` to another paradigm cell or for splitting `PROTO` from `PROTOFORM`; they only preserve that the row was checked and left unchanged under A-restoration work [Germanic/docs/DEV_NOTES.md:2863-2889; Germanic/docs/DEV_NOTES.md:3844-3853].

## Open questions for later work

- The main technical question is implementation, not philology: why do current sandbox pipelines fail at `ProtoRhoticFronting` and then lose `r` under `PostVocalicRLoss` for a row whose published OE trace still cleanly yields `heorte`? That regression should be investigated together with nearby `r`-breaking rows rather than by changing this slice’s lexical conclusions [Germanic/tmp/old_english_sandbox_results_with_stages.json:19090-19175; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2207-2220].
- If a later packet or research memo is commissioned for this row, it should add genuine row-local literature on the `*xertōn > heorte` derivation and weak-feminine morphology. The present slice is intentionally conservative because the surviving DEV_NOTES material is mostly scoping evidence, not a dedicated heart dossier [Germanic/docs/lexeme_reports/coverage_audit.md:272-272; Germanic/docs/DEV_NOTES.md:2863-2889,3844-3853].
- If future editorial work starts distinguishing published-trace state from sandbox-current state in metadata, row `2065` may need a more explicit status vocabulary. Right now the row is philologically regular and published-trace-correct, but procedurally diagnostic snapshots are signaling a live implementation problem that this file can only annotate, not resolve [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2200-2220; Germanic/tmp/old_english_sandbox_results_current.json:1216-1220].
