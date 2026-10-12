---
row_id: 1945
concept: belly
counterpart: bielġ
proto: "*bálgiz"
protoform: "*bálgiz"
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
  - Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md
  - Germanic/docs/dossiers/g-palatalisation-conditioning.md
current_status: uncertain
needs_literature_agent: yes
---

# DEV_NOTES material — 1945 belly / bielġ

## Current row state

- The live Old English row is stable at the table level: `ID 1945`, `CONCEPT belly`, `COUNTERPART bielġ`, `PROTO = PROTOFORM = *bálgiz`, `DERIVATION_CLASS regular` [Germanic/data/germanic-aligned-final.tsv:52-52].
- The row's source trail is already mixed and should be recorded as such. In `germanic-aligned-final.tsv`, the `HISTORY` field cites both the Old English Swadesh list and Wiktionary, while the row's `IPA` is `wɒmb`; the Swadesh source indeed has `belly = wamb`, but `old_english_wiktionary.tsv` gives `belly = bielġ` [Germanic/data/germanic-aligned-final.tsv:52-52; Germanic/data/old_english_swadesh.tsv:86-86; Germanic/data/old_english_wiktionary.tsv:14-14].
- No row-specific packet or research memo is currently present. The coverage audit still lists row `1945` as `none` across report infrastructure columns [Germanic/docs/lexeme_reports/coverage_audit.md:199-199].
- Repo diagnostics are internally split. The published derivation trace reaches the target cleanly via `*bálgiz > *bálgi > *bælgi > *bealgi > *bealʤi > *bielʤi > *bielʤ > bielġ` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:208-228]. But the current sandbox JSON reports `outputs: []` for `belly / bielġ`, and the staged sandbox trace collapses to surface `balg` with `first_failing_stage: "ProtoRhoticFronting"` [Germanic/tmp/old_english_sandbox_results_current.json:92-98; Germanic/tmp/old_english_sandbox_results_with_stages.json:1712-1852].
- `oe_known_problems.tsv` has no entry for `*bálgiz`. That absence means only that the row is not currently registered as a known exception or wontfix item; it does not settle the live conflict between the published trace and the current sandbox state [Germanic/data/oe_known_problems.tsv:1-8].

## Development-note summary

DEV_NOTES support for row `1945` is real but mostly **shared-rule** support rather than a dedicated belly dossier. The earliest material is an OE TODO/mismatch cluster from December 2025. There the row appears twice: once as an explicit mismatch, “`*balgiz -> balgi` vs `bielġ`,” and once in the implementation TODO list targeting stray final high vowels, which names `balgi` among the outputs to eliminate [Germanic/docs/DEV_NOTES.md:2422-2429,2473-2484]. That preserves the original problem statement clearly: at that stage the grammar was still stopping at something like `balgi`, not yet the attested/desired `bielġ`.

The same DEV_NOTES block also matters because it does not treat the row as a pure tail problem only. Right beside the `balgi` TODO, DEV_NOTES says OE work still needed “missing PGmc→OE consonant changes (palatalisation in OE contexts, rhotic prep, targeted lexical replacements)” so outputs could align with `COUNTERPART` values [Germanic/docs/DEV_NOTES.md:2428-2428]. For `bielġ`, that is materially relevant: the row needs not just deletion of final `-i`, but also the OE-side conditioning that can support final palatal `ġ` rather than plain velar `g` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:221-228].

A few lines later DEV_NOTES records a partial repair. The high-vowel-loss debug note says the H-marker rule had been nondeterministic and that `balluz/balgiz/bebruz` were then used as verification probes; after the fix they yielded “a **single** output at each stage, with apocope firing deterministically in heavy contexts” and the updated diagnostics showed “**0** final `-i/-u` outputs” [Germanic/docs/DEV_NOTES.md:2509-2520]. This is important current substance, but it is also limited substance. It documents that the row's visible `balgi` tail problem was intentionally fixed; it does **not** by itself explain the full vowel-and-palatal sequence needed for `bielġ`.

The most philologically substantive shared note comes much later in the handbook-backed audit of OE `*g` palatalisation. DEV_NOTES preserves the source claim that final /g/ palatalises after a front vowel and that medial /g/ does so “between any two front vowels, between front vowel and syllabic consonant, and always after a vowel which has suffered i-umlaut,” while remaining velar when a back vowel stands on one side in the relevant environment [Germanic/docs/DEV_NOTES.md:43224-43243]. DEV_NOTES then abstracts the consensus as: palatalisation after a front vowel happens iff the right context is “anything except a back vowel,” with explicit positive environments `_ #`, `_ front-V`, and `_ Consonant`, plus an umlaut-override row [Germanic/docs/DEV_NOTES.md:43273-43294]. That shared rule discussion directly bears row `1945`, because the target `bielġ` requires final palatal `ġ` after a fronted/umlauted vowel and no surviving back-vowel blocker.

What DEV_NOTES does **not** currently preserve is equally important. No row-specific passage walks through `*bálgiz` as a belly lexeme and explicitly defends the whole chain `a > æ > ea > ie` plus final `ġ`. The current published trace supplies such a chain operationally, but DEV_NOTES itself only securely documents two pieces of project history: first, `balgi` was an acknowledged bad OE output; second, the project later considered final-high-vowel apocope and `g`-palatalisation conditioning to be solved or at least source-backed shared problems [Germanic/docs/DEV_NOTES.md:2478-2484,2509-2520,43224-43294; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:208-228]. Because the repo's current sandbox no longer agrees with the published trace, the safest replacement note is therefore conservative: preserve the shared DEV_NOTES support, but do not overstate it as a row-specific closed case [Germanic/tmp/old_english_sandbox_results_current.json:92-98; Germanic/tmp/old_english_sandbox_results_with_stages.json:1712-1852].

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-2422-2429

- Source line or section hint: `lines 2422-2429`
- Fragment type: `superseded_or_diagnostic_for_lexeme`
- Status: `diagnostic_only`
- Issue tags: `balgi_output`; `high_vowel_apocope`; `missing_oe_consonant_innovations`
- Recommended next use: `use_to_explain_initial_problem_statement`
- Shared with row IDs: `1935`; `1941`; `1981`; `2107`

This is the first materially relevant setup note because it names both halves of the later repair space. DEV_NOTES explicitly says OE work should “broaden final `*i/*u` deletion” and names `balgi` among the outputs to target, while also stating that OE still lacked “palatalisation in OE contexts” among the consonant changes needed to align outputs with counterparts [Germanic/docs/DEV_NOTES.md:2426-2428]. For row `1945`, this fragment shows that the project already understood `balgi` as a two-part issue: the lingering final `-i` was wrong, and OE consonant conditioning still mattered too.

### DEV_NOTES:line-2473-2484

- Source line or section hint: `lines 2473-2484`
- Fragment type: `superseded_or_diagnostic_for_lexeme`
- Status: `superseded`
- Issue tags: `explicit_mismatch`; `balgi_output`; `ending_diagnostics`
- Recommended next use: `use_as_project_history_only`
- Shared with row IDs: `1935`; `1941`; `1981`; `2107`

This is the clearest early row-specific diagnostic record. DEV_NOTES first lists `*balgiz -> balgi` vs `bielġ` as a sample OE mismatch, then repeats `balgi` in the sample `-i/-u` outputs [Germanic/docs/DEV_NOTES.md:2478-2484]. That pair of statements is worth preserving verbatim in substance because it shows exactly what the grammar was emitting and exactly what the table expected. It also shows that, in late 2025, the row was still being encountered primarily through bulk mismatch diagnostics rather than through a dedicated lexeme memo.

### DEV_NOTES:line-2509-2520

- Source line or section hint: `lines 2509-2520`
- Fragment type: `copied_shared_lexeme_fragment`
- Status: `current`
- Issue tags: `high_vowel_apocope`; `deterministic_fix`; `shared_probe`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs: `1935`; `1941`; `1981`; `2107`

This is the most important current implementation-side fragment for the row's tail behaviour. DEV_NOTES says the H-marker rule had been “yielding both apocopated and non-apocopated outputs,” then records the fix and adds: “Verification (sample probes): `balluz/balgiz/bebruz` now yield a **single** output at each stage, with apocope firing deterministically in heavy contexts” [Germanic/docs/DEV_NOTES.md:2510-2517]. For `*bálgiz`, the narrow claim is solid: DEV_NOTES treats the old `balgi`-type ending as a repaired bug, not as a rival lexical analysis.

### DEV_NOTES:line-43224-43294

- Source line or section hint: `lines 43224-43294`
- Fragment type: `copied_shared_lexeme_fragment`
- Status: `current`
- Issue tags: `g_palatalisation`; `campbell_quote`; `right_context_conditioning`; `umlaut_override`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs: `782`; `940`; `1579`; `1882`

This is the strongest current shared philological support that bears directly on `bielġ`. DEV_NOTES preserves Campbell's claim that word-final /g/ palatalises after any front vowel and that medial /g/ palatalises “between any two front vowels, between front vowel and syllabic consonant, and always after a vowel which has suffered i-umlaut,” while forms like `wegas` and `nigon` remain velar in back-vowel contexts [Germanic/docs/DEV_NOTES.md:43229-43243]. It then abstracts the consensus as a rule that inherited `*g` after a front vowel palatalises iff the right context is anything except a back vowel, explicitly including `_ #`, `_ front-V`, and `_ Consonant` [Germanic/docs/DEV_NOTES.md:43275-43294]. That is not a belly-specific note, but it is exactly the kind of shared rule discussion that directly bears on row `1945`'s final `ġ`.

## Superseded or diagnostic material

- The mixed-source row metadata needs to stay visibly diagnostic. The aligned row currently combines `COUNTERPART bielġ` with `IPA wɒmb`, which reflects the coexistence of Wiktionary `bielġ` and Swadesh `wamb` in the underlying source trail rather than a single harmonized OE lexical decision [Germanic/data/germanic-aligned-final.tsv:52-52; Germanic/data/old_english_swadesh.tsv:86-86; Germanic/data/old_english_wiktionary.tsv:14-14].
- DEV_NOTES' early `balgi` material is superseded as output history, not as an alternative OE target. The note history shows a bad intermediate system state, first recognized as a mismatch and later addressed by high-vowel apocope work [Germanic/docs/DEV_NOTES.md:2478-2484,2509-2520].
- The current repo diagnostics are also only diagnostic. The published trace report already generates `bielġ`, but the current sandbox still gives no output and a stage trace ending in `balg` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:208-228; Germanic/tmp/old_english_sandbox_results_current.json:92-98; Germanic/tmp/old_english_sandbox_results_with_stages.json:1712-1852]. Until that split is reconciled, neither artifact should be silently treated as the sole authoritative state of the row.
- No packet, research memo, or `oe_known_problems.tsv` entry currently supersedes this slice. The row is documented enough to justify a replacement working note, but still underdocumented at the lexeme-specific level [Germanic/docs/lexeme_reports/coverage_audit.md:199-199; Germanic/data/oe_known_problems.tsv:1-8].

## Open questions for later work

- Reconcile the live row's mixed-source metadata: should the OE belly row continue to foreground `bielġ`, should `wamb` be segregated to a different lexeme/source track, or should the current row metadata be normalized so `IPA`, `COUNTERPART`, and source citations point to the same lexical item [Germanic/data/germanic-aligned-final.tsv:52-52; Germanic/data/old_english_swadesh.tsv:86-86; Germanic/data/old_english_wiktionary.tsv:14-14]?
- Reconcile the published success trace with the current failing sandbox run before treating this row as fully settled in report infrastructure [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:208-228; Germanic/tmp/old_english_sandbox_results_current.json:92-98].
- If a full memo is later written, make the vowel pathway explicit rather than assuming it from the trace alone: the replacement note still lacks a DEV_NOTES passage that directly argues through the full sequence behind `bielġ` rather than just its tail repair and final palatalisation environment [Germanic/docs/DEV_NOTES.md:2478-2484,2509-2520,43224-43294].
- This slice is probably useful as a no-index working note now, but it likely should not be treated as index-ready until the source-mixing issue and the trace-vs-sandbox conflict are resolved.
