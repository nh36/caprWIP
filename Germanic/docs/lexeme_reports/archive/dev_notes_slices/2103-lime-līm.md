---
row_id: 2103
concept: lime
counterpart: līm
proto: *lī́mą
protoform: *lḯmą
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files: []
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2103 lime / līm

## Current row state

- The live OE row now reads `ID 2103 | CONCEPT lime | COUNTERPART līm | PROTOFORM *lḯmą | DERIVATION_CLASS regular | PROTO *lī́mą`, and it carries no row-local explanatory NOTE beyond duplicated inherited-etymology placeholders in `HISTORY` [Germanic/data/germanic-aligned-final.tsv:670-670].
- The row therefore already encodes a three-way distinction that later writing must keep explicit: comparative `PROTO = *lī́mą`, OE-facing derivational `PROTOFORM = *lḯmą`, and attested/project target `COUNTERPART = līm` [Germanic/data/germanic-aligned-final.tsv:670-670].
- `coverage_audit.md` currently treats the row as uncovered but unproblematic: `| 2103 | lime | līm | regular | no | - | - | - | none |`. There is no linked packet, research memo, manifest entry, or prior lexeme-report path to inherit for this row [Germanic/docs/lexeme_reports/coverage_audit.md:294-294; Germanic/docs/lexeme_reports/report_manifest.tsv:1-14].
- `oe_known_problems.tsv` has no entry for row `2103`, for `lime`, for `līm`, or for either long-`ī` proto spelling; the active OE known-problem list presently contains only unrelated exception buckets [Germanic/data/oe_known_problems.tsv:1-8].
- The authoritative published derivation snapshot is an exact match and already uses the migrated stressed-long-`ī` notation: `PROTO: *lḯmą`, `EXPECTED: līm`, `OUTPUTS: līm`, with no PWGmc or NWGmc change and only `OE Heavy Syllable Nasal Apocope: *lḯm` before surface `Outcome: līm` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2863-2882].
- A separate local sandbox JSON still shows the older plain-`*ī` input spelling `*līmą` and a broader output bundle `līm / līmu / līmuz / līmiz`; its staged dump even records a failing intermediate runner and terminal `Surface` value `līma`, so it should be treated as diagnostic scratch evidence rather than as the governing row trace [Germanic/tmp/old_english_sandbox_results_current.json:1632-1640; Germanic/tmp/old_english_sandbox_results_with_stages.json:24582-24726].

## Development-note summary

No dedicated lexeme dossier for `lime / līm` survives in `Germanic/docs/DEV_NOTES.md`. The only securely attachable direct row mention is the stressed-long-`ī` migration table entry `| 2 | 2103, 2105, 2106 | līm, līne, līste |`, so the replacement slice has to be built conservatively from that migration note plus the shared notation-policy section and the current published derivation trace [Germanic/docs/DEV_NOTES.md:42020-42026; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2863-2882].

That surviving material is still enough to explain the row's present logic in detail. `DEV_NOTES` says the old fix was unprincipled because “Words like `*tīdiz` or `*lībą` happen to satisfy the V+C+ context by accident of having an inflectional ending; the principle is unrelated,” and it replaces that hack with a distinct stressed-long-`ī` tier [Germanic/docs/DEV_NOTES.md:41913-41915]. The same note then states the key interpretive sentence that governs this row too: “The diaeresis is purely notational. Semantically `*ḯ` = stressed long *ī” [Germanic/docs/DEV_NOTES.md:41938-41940]. For row 2103, that means `*lī́mą` and `*lḯmą` are not rival reconstructions or rival chronology layers; the first is the comparative cognate-set spelling retained in `PROTO`, and the second is the machine-safe OE-facing input now retained in `PROTOFORM` [Germanic/data/germanic-aligned-final.tsv:670-670; Germanic/docs/DEV_NOTES.md:41925-41940].

The row's practical significance inside `DEV_NOTES` is therefore implementation history, not lexical controversy. Batch 2 of the TSV migration names `līm` together with `līne` and `līste`, which means row 2103 was one of the OE items deliberately moved from plain long `*ī` notation into the stressed `*ḯ` cohort [Germanic/docs/DEV_NOTES.md:42020-42023]. Nothing in the surviving note suggests that `līm` needed a substitute paradigm cell, an analogical repair, an exception label, or a different OE target. The published exact-match trace confirms the narrow reading: the live grammar now derives `līm` regularly from `*lḯmą` with a minimal chain and no special rescue step [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2863-2882].

Accordingly, support here should be classified carefully. The notation-policy discussion is **shared-background-only** support that explains why the row shows `*ḯ` at all; the migration table is the one piece of **row-specific** surviving DEV_NOTES evidence; the published trace is **current row-state** evidence rather than DEV_NOTES authority; and the sandbox JSONs are merely **diagnostic** because they still preserve older input spelling and non-authoritative scratch outputs [Germanic/docs/DEV_NOTES.md:41893-42026; Germanic/tmp/old_english_sandbox_results_current.json:1632-1640].

## Relevant DEV_NOTES fragments

No dedicated row-specific prose block survives for `2103`. The fragments below are the surviving material that actually governs the row.

### DEV_NOTES:line-41893-41957

- Source heading: `§17.46 Stressed long-ī tier (*ḯ) — principled fix for the *swīn regression`
- Source line or section hint: `lines 41893-41957`
- Fragment type: `phenomenon_context_for_lexeme`
- Status: `current`
- Issue tags: `stressed_long_i`; `notation_policy`; `proto_vs_protoform`; `shared_background_only`
- Recommended next use: `cite_when_explaining_why_row_2103_has_*lḯmą_in_PROTOFORM_but_not_as_a_new_reconstruction`
- Shared with rows if relevant: `2101`; `2105`; `2106`; `2153`; `2182`; `2188`; `2197`; `2257`; `2285`; `2286`; `2290`; `2296`

This is the controlling shared background for the row even though it does not name `līm` directly. DEV_NOTES rejects the earlier context hack because the in-stem rule is stress-conditioned, not syllable-count-conditioned, and warns that “Words like `*tīdiz` or `*lībą` happen to satisfy the V+C+ context by accident of having an inflectional ending; the principle is unrelated” [Germanic/docs/DEV_NOTES.md:41908-41915]. The row-level force of that sentence is methodological: forms with long stressed root `*ī` should not be treated as safe merely because an ending happens to create the right local context. Instead, the stressed vowel must be encoded distinctly inside the OE machinery.

The same fragment then preserves the exact wording that should be carried forward for row 2103: “The diaeresis is purely notational. Semantically `*ḯ` = stressed long *ī” and `{*ḯ} -> ī` at surface level because “OE orthography does **not** distinguish stressed-root from unstressed-suffix long ī” [Germanic/docs/DEV_NOTES.md:41925-41940,41952-41957]. Applied to this row, that means `PROTO *lī́mą` and `PROTOFORM *lḯmą` are two notation layers for the same inherited long-`ī` noun, while the target remains ordinary OE `līm` [Germanic/data/germanic-aligned-final.tsv:670-670]. This fragment is therefore indispensable, but it is **shared-background-only** support rather than a row-local lexical memorandum.

### DEV_NOTES:line-42006-42026

- Source heading: `§17.46 ... E. TSV migration (Phase 4)`
- Source line or section hint: `lines 42006-42026`
- Fragment type: `lexeme_specific`
- Status: `current`
- Issue tags: `tsv_migration`; `row_explicit`; `stressed_long_i`; `row_specific_surviving_note`
- Recommended next use: `cite_if_documenting_the_only_direct_DEV_NOTES_hit_for_row_2103`
- Shared with rows if relevant: `2105`; `2106`

This is the one securely attachable fragment that names the row directly. DEV_NOTES inventories the migrated OE rows and gives Batch 2 as `| 2 | 2103, 2105, 2106 | līm, līne, līste |` [Germanic/docs/DEV_NOTES.md:42020-42023]. The narrow but important substance is that `līm` belongs to the stressed-root long-`ī` cohort that was deliberately rewritten into `*ḯ` notation during the TSV migration.

The fragment should be read narrowly and literally. It records migration history, not etymological instability. It does **not** say that `līm` was a mismatch, not that the target had to be changed, and not that some competing OE form survived in DEV_NOTES. Its value is that it is the only current DEV_NOTES place where row 2103 survives as a named lexeme at all; beyond that, interpretation must come from the shared notation section and the published exact-match trace [Germanic/docs/DEV_NOTES.md:41893-41957; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2863-2882].

### DEV_NOTES:line-42031-42051

- Source heading: `§17.46 ... F. Verification`
- Source line or section hint: `lines 42031-42051`
- Fragment type: `diagnostic_project_history_for_lexeme`
- Status: `current_but_aggregate`
- Issue tags: `verification`; `migration_regression_check`; `diagnostic`; `shared_background_only`
- Recommended next use: `use_only_as_supporting_project_history`
- Shared with rows if relevant: `all migrated_*ḯ_rows`

This verification block does not mention `līm` by name, but it documents the post-migration check regime under which row 2103 was kept. DEV_NOTES lists representative probes such as `swḯną → swīn` and `tḯdiz → tīd`, then reports mismatch totals holding at `13` through Phase 4 batches 1–5 [Germanic/docs/DEV_NOTES.md:42031-42051]. For row 2103, the practical use of the fragment is limited but real: it supports the conservative reading that the migration table was not merely aspirational bookkeeping but part of a verified, non-regressing `*ḯ` rollout.

Because the fragment is aggregate and not row-local, it should stay secondary. It can support statements about project history and about why the migration table can be trusted as current, but it should not be cited as if it were itself a lexeme-specific discussion of `līm`.

## Superseded or diagnostic material

- No superseded row-specific `līm` memorandum has been located in `DEV_NOTES.md`. The current replacement slice therefore has to say plainly that the surviving DEV_NOTES support is thin: one direct migration-table hit plus shared stressed-long-`ī` policy, not a lost lexical controversy dossier [Germanic/docs/DEV_NOTES.md:41893-42051].
- Older combining-acute spelling remains visible in the row as comparative `PROTO *lī́mą`, but DEV_NOTES is explicit that the move to single-codepoint `*ḯ` was an input-tokenization repair, not a new reconstruction: combining acute compiled yet failed under `apply down`, while `ḯ` “works, single codepoint. **Adopted.**” [Germanic/docs/DEV_NOTES.md:41925-41936]. For this row, older `*lī́mą` is therefore superseded only as OE-cascade input notation; it remains current as the comparative proto label in the TSV [Germanic/data/germanic-aligned-final.tsv:670-670].
- The local sandbox JSON files are diagnostic but should not be treated as row authority. They still expose plain `*līmą` rather than migrated `*lḯmą`, return bundled exploratory outputs (`līm`, `līmu`, `līmuz`, `līmiz`), and in the staged dump even end at `Surface: līma` after a flagged failing stage [Germanic/tmp/old_english_sandbox_results_current.json:1632-1640; Germanic/tmp/old_english_sandbox_results_with_stages.json:24582-24726]. Those files illuminate project history and runner state, but the published derivation snapshot is the authoritative current row trace [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2863-2882].

## Open questions for later work

- If a future packet or memo is created for row 2103, keep the notation bridge explicit near the top: comparative `PROTO *lī́mą`, OE-facing `PROTOFORM *lḯmą`, and ordinary OE target `līm`. The surviving DEV_NOTES material is thin enough that later writers could otherwise collapse those layers by mistake [Germanic/data/germanic-aligned-final.tsv:670-670; Germanic/docs/DEV_NOTES.md:41938-41957].
- If later philological enrichment is wanted, fresh literature canvassing may be useful on dictionary lemma format (`*līma-` / `*līman`) and lexical gender, but that is outside what the surviving DEV_NOTES block currently settles. The present slice should not pretend that DEV_NOTES already resolved those comparative-dictionary presentation issues.
- If sandbox diagnostics are refreshed later, it would be useful to regenerate or retire the stale `old_english_sandbox_results_*` entries for `lime` so that local scratch outputs no longer compete with the published exact-match trace. That is workflow hygiene, not evidence that row 2103 itself is unstable [Germanic/tmp/old_english_sandbox_results_current.json:1632-1640; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2863-2882].
