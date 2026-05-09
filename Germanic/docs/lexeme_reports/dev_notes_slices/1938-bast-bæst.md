---
row_id: 1938
concept: bast
counterpart: bæst
proto: *bástą
protoform: *bástą
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
  - Germanic/docs/analysis/arestoration_r_l_research.md
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 1938 bast / bæst

## Current row state

- The live OE row is a regular exact-match row: `CONCEPT = bast`, `COUNTERPART = bæst`, `PROTO = *bástą`, `PROTOFORM = *bástą`, `DERIVATION_CLASS = regular` [Germanic/data/germanic-aligned-final.tsv:1938-1938].
- The published derivation trace is currently exact and minimal: `PROTO: *bástą`, `EXPECTED: bæst`, `OUTPUTS: bæst`, with OE-side stages `Anglo Frisian Brightening: *bæstą`, `OE Heavy Syllable Nasal Apocope: *bæst`, `Outcome: bæst` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:65-84].
- `coverage_audit.md` still classifies row `1938` as a regular row with no inherited report requirement (`Requirement basis = none`), so this slice is replacement working documentation rather than continuation of an older row-specific report chain [Germanic/docs/lexeme_reports/coverage_audit.md:189-194].
- The only directly attachable non-DEV_NOTES support file found during this pass is the shared A-restoration analysis `Germanic/docs/analysis/arestoration_r_l_research.md`, whose `### 6.2 bæst` subsection restates the same weak-tail diagnosis later adopted in DEV_NOTES: `*st` is transparent, and singular `*bastą` stays fronted because final `*ą` is not a real restoration trigger [Germanic/docs/analysis/arestoration_r_l_research.md:441-448].

## Development-note summary

The surviving DEV_NOTES material for row 1938 is real but mostly shared-rule material rather than a standalone `bast / bæst` dossier. The project first encountered the row in an early A-restoration sandbox audit, where `*bastą -> bæst` was counted among the apparent “false positives” and used as part of the motivation for tightening restoration conditioning [Germanic/docs/DEV_NOTES.md:1719-1724]. That early mention should be preserved, but not treated as the current explanation.

The later §17.25 rewrite explicitly corrects the earlier framing. DEV_NOTES says the exclusion of liquids from `OEARestorationIntervening` was an “over-correction”: it had been added to defeat false positives like ``*nadrō → *nadre`` and ``*bastą → *bast``, but those cases are not actually blocked by liquids themselves [Germanic/docs/DEV_NOTES.md:36517-36523]. The same passage then preserves the literature-based conditioning that matters for this row. Campbell is quoted that “The restoration of *a* is common before all single consonants and geminates” and is “commonly restored also before groups consisting of *f* or *s* followed by another consonant”; Ringe-Taylor are quoted that stressed `*æ` retracts when followed by “a single or geminate consonant or **sC-cluster**” plus a back vowel; Luick is quoted that restoration is “unabhängig von der Art der dazwischen stehenden Konsonanten” [Germanic/docs/DEV_NOTES.md:36524-36536]. For row 1938, that means `*st` is not a blocker at all; it is exactly the kind of `sC` cluster under which restoration would be compatible with the literature.

DEV_NOTES is equally explicit about why the row still surfaces as `bæst`. The key sentence is that “The current FST handles `*bastą → bæst` correctly for **independent** reasons”: the trigger candidate `*ą` is in the weak-tail exclusion list, while the intervening `*st` cluster remains part of the proposed allowed set [Germanic/docs/DEV_NOTES.md:36543-36552]. In other words, the row is now treated as a control example showing that the grammar must distinguish two questions that earlier notes blurred together: whether a consonant cluster permits restoration, and whether the following vowel is a strong enough back-vowel trigger to cause it.

The implementation history preserved in DEV_NOTES confirms that this was not just a theoretical cleanup. The §17.25 probe plan explicitly included ``echo 'bastą' | flookup -i backend/old_english.bin`` with expected `bæst`, and the post-fix verification later records `*bastą → bæst` ✓ with the gloss “no regression — weak-tail *ą correctly blocks” [Germanic/docs/DEV_NOTES.md:36649-36657,36757-36769]. Row 1938 is therefore current project evidence that the literature-grounded A-restoration rewrite did **not** damage singular `bæst`; the form stayed correct precisely because the weak-tail exclusion, not cluster blocking, is doing the work.

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-1719-1724

- Source heading: `Measured ARestoration intervening segments (2026-02-05, OE sandbox)`
- Source line or section hint: `lines 1719-1724`
- Fragment type: `early_diagnostic_snapshot`
- Status: `diagnostic_only`
- Issue tags: `a_restoration`; `false_positive_bucket`; `cluster_conditioning`; `project_history`
- Recommended next use: `cite_only_if_explaining_why_the_later_note_had_to_correct_the_record`
- Shared with row IDs: `1934`, `2003`, `2205`

This is the earliest row-explicit DEV_NOTES attachment. It records that the sandbox measured `*bastą -> bæst` among the “False positives (16 items)” with intervening segment `st` [Germanic/docs/DEV_NOTES.md:1719-1721]. That is worth preserving because it explains the project chronology: `bæst` initially looked like evidence that the restoration rule was overfiring or underconstrained. But the fragment is no longer a safe current explanation. Later DEV_NOTES reclassifies the case and shows that `bæst` was not a genuine cluster-blocking counterexample in the first place [Germanic/docs/DEV_NOTES.md:36517-36523,36548-36552].

### DEV_NOTES:line-36517-36552

- Source heading: `§17.25.1 Why the current *r/*l exclusion is wrong` plus `§17.25.2 The canonical conditioning of A-restoration (literature consensus)`
- Source line or section hint: `lines 36517-36552`
- Fragment type: `shared_rule_reanalysis`
- Status: `current`
- Issue tags: `a_restoration`; `sC_cluster`; `weak_tail_trigger`; `literature_grounding`
- Recommended next use: `cite_if_explaining_why_bæst_is_not_a_counterexample_to_sC_transparency`
- Shared with row IDs: `1934`, `2003`, `2090`, `2141`, `2205`

This is the controlling current DEV_NOTES material for row 1938. It first preserves the correction to the earlier false-positive logic: the liquid exclusion was an “over-correction,” because forms such as ``*bastą → *bast`` were not being blocked by liquids “per se” [Germanic/docs/DEV_NOTES.md:36517-36523]. It then copies the literature consensus that matters here. Campbell is quoted that restoration is common “before all single consonants and geminates” and is “commonly restored also before groups consisting of *f* or *s* followed by another consonant”; Ringe-Taylor are quoted that retraction applies before “a single or geminate consonant or **sC-cluster**”; Luick is quoted that the process is “unabhängig von der Art der dazwischen stehenden Konsonanten” [Germanic/docs/DEV_NOTES.md:36524-36536]. For `*bastą`, those quotations matter because they make `*st` the **wrong** place to locate the explanation.

DEV_NOTES then states the row-specific conclusion in current project language: “The current FST handles `*bastą → bæst` correctly for **independent** reasons: trigger `*ą` is in the weak-tail exclusion list … The intervening `*st` cluster is `sC`, in our proposed set. Removing the *r exclusion does not regress this case” [Germanic/docs/DEV_NOTES.md:36548-36552]. This is the sentence later work should quote when the row is used as evidence. It preserves both halves of the argument: `*st` is transparent under the accepted rule, and singular `bæst` survives because final `*ą` is not a genuine restoration trigger.

### DEV_NOTES:line-36649-36657 and line-36757-36769

- Source heading: `Implementation plan / probes` and `§17.25.8 Post-fix verification`
- Source line or section hint: `lines 36649-36657; 36757-36769`
- Fragment type: `verification_probe`
- Status: `current`
- Issue tags: `regression_check`; `flookup_probe`; `weak_tail_guardrail`; `control_case`
- Recommended next use: `cite_if_showing_that_the_reanalysis_was_tested_not_just_asserted`
- Shared with row IDs: `1934`, `2003`, `2090`, `2141`, `2205`

These lines show that row 1938 remained an active regression check after the literature rewrite. DEV_NOTES requires the explicit probe ``echo 'bastą' | flookup -i backend/old_english.bin`` with expected `bæst` [Germanic/docs/DEV_NOTES.md:36651-36656]. The later post-fix checklist then records the successful outcome as `*bastą → bæst` ✓ and labels the reason directly: “no regression — weak-tail *ą correctly blocks” [Germanic/docs/DEV_NOTES.md:36757-36769]. For this slice, that matters because it turns the shared theoretical claim into tested project state.

## Superseded or diagnostic material

- The February 2026 “false positives” bucket is retained here only as project history. It should not be reused as though it were the current phonological account of `bæst`, because later DEV_NOTES explicitly revises the causal explanation away from cluster blocking and toward weak-tail trigger suppression [Germanic/docs/DEV_NOTES.md:1719-1724,36517-36523,36548-36552].
- The shared analysis file `Germanic/docs/analysis/arestoration_r_l_research.md` is useful background, but it is not a row-specific replacement note and should not be mistaken for a packet or memo. Its value is diagnostic: it preserves the same conclusion in expanded form, including the formulation “`*bastą → bæst` is fully accounted for by the weak-tail exclusion” and the reminder that `*st` would permit restoration in forms with a genuine following back-vowel trigger [Germanic/docs/analysis/arestoration_r_l_research.md:443-448].
- Because `coverage_audit.md` marked row `1938` as a regular row with `Requirement basis = none`, the evidentiary state here is inherently lighter than in rows with dedicated packet/memo chains. The slice should therefore stay conservative and avoid implying that a rich lexeme-specific DEV_NOTES dossier survives when the actual support is mostly shared A-restoration discussion [Germanic/docs/lexeme_reports/coverage_audit.md:189-194].

## Open questions for later work

- If a final lexeme report is ever wanted, add direct comparative-source quotations for the noun paradigm itself; current DEV_NOTES support is strong on the rule interaction, but thin on row-local lexicographic discussion beyond the shared A-restoration material [Germanic/docs/DEV_NOTES.md:36524-36552; Germanic/docs/analysis/arestoration_r_l_research.md:443-448].
- If later work starts citing inflected forms, keep singular `*bastą` separate from hypothetical forms with full back-vowel endings. The current note only establishes why nominative/accusative singular `bæst` stays fronted; it does not license flattening the entire paradigm into the same trigger behavior [Germanic/docs/analysis/arestoration_r_l_research.md:444-448].
- If `index.tsv` is reconsidered later, decide whether the present evidence is strong enough for indexing. The row now has explicit, current DEV_NOTES support, but most of that support is shared rule-scope analysis plus regression verification rather than a bespoke lexeme dossier [Germanic/docs/DEV_NOTES.md:36517-36552,36757-36769; Germanic/docs/lexeme_reports/coverage_audit.md:189-194].
