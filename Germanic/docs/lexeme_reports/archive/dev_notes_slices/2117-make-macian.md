---
row_id: 2117
concept: make
counterpart: macian
proto: "*mákōjaną"
protoform: "*mákōjaną"
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
  - Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md
  - Germanic/docs/debug_snapshots/oe_full_trace_report_2026-03-11.txt
current_status: current_shared_background_plus_live_trace
needs_literature_agent: no
---

# DEV_NOTES material — 2117 make / macian

## Current row state

- CONCEPT: `make`
- COUNTERPART: `macian`
- PROTO: `*mákōjaną`
- PROTOFORM: `*mákōjaną`
- DERIVATION_CLASS: `regular`
- Live TSV row: row 2117 currently keeps the lemma-level verbal input and target aligned at the lexeme level: `PROTO = *mákōjaną`, `PROTOFORM = *mákōjaną`, `COUNTERPART = macian`, `DERIVATION_CLASS = regular`. The source field carries only generic Wiktionary-etymology placeholders; there is no row-local explanatory NOTE or HISTORY text to preserve from the TSV itself [Germanic/data/germanic-aligned-final.tsv:725-725].
- Coverage / manifest / known-problems state: `coverage_audit.md` marks row 2117 as `regular`, with no packet, no memo, no prior attached fragment, and `none` in the notes column; `report_manifest.tsv` still lists only a small pilot set and has no row-2117 entry; `oe_known_problems.tsv` currently contains unrelated exception rows only, so row 2117 is not being tracked as a live unresolved problem [Germanic/docs/lexeme_reports/coverage_audit.md:304-304; Germanic/docs/lexeme_reports/report_manifest.tsv:1-14; Germanic/data/oe_known_problems.tsv:1-8].
- Current implementation traces: both current debug snapshots already derive the expected target. The publish snapshot gives `*mákōjaną > *mækōjaną > *makōjaną > *makējąn > *makejąn > *makejan > *makeian > *makian > macian`, while the full trace snapshot likewise ends at `Orthography: macian / Surface: macian` from the same proto input, just with more granular starred-segment notation [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3084-3103; Germanic/docs/debug_snapshots/oe_full_trace_report_2026-03-11.txt:8638-8691].
- PROTO / PROTOFORM / OE-target distinction: for this row, unlike the companion paradigm-cell rows `2309 maca` and `2310 macaþ`, the live data do **not** separate lexeme-level proto from selected paradigm-cell protoform. `PROTO` and `PROTOFORM` are the same comparative lexical form here, and `macian` is the attested/target Old English infinitive counterpart, not an imperative or finite-cell substitute [Germanic/data/germanic-aligned-final.tsv:725-725].

## Development-note summary

No dedicated row-2117 DEV_NOTES block survives. The usable material is a layered mix of (a) **shared-background-only** class-II weak-verb discussion, where `*makōjăną` was originally treated as part of the `-eian`/`-ian` mismatch problem; (b) **current shared literature support** on A-restoration in class-II weak verbs, explicitly naming `macian` as a canonical retracted-`a` example; and (c) **current diagnostic verification**, where the post-fix probe list explicitly includes `*mákōjaną → macian` as a successful derivation [Germanic/docs/DEV_NOTES.md:2761-2861; Germanic/docs/DEV_NOTES.md:36529-36534; Germanic/docs/DEV_NOTES.md:36757-36767].

The conservative reading is therefore two-track. Historically, DEV_NOTES did preserve a real warning that OE class-II `-ian` has been treated in the literature as morphologized rather than as a simple phonological reflex of PGmc `*-ōja-`; that warning remains relevant as background and should not be erased [Germanic/docs/DEV_NOTES.md:2901-2903]. But for the **current row state**, the repo no longer treats `macian` as an active mismatch: the live row is `regular`, no known-problems entry exists, the coverage audit records no exception handling, and the current snapshots produce the target directly [Germanic/data/germanic-aligned-final.tsv:725-725; Germanic/docs/lexeme_reports/coverage_audit.md:304-304; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3084-3103].

What should be carried forward for row 2117 is not a claim that the whole historical suffix story has been solved once and for all, but a more limited working note: the present project state accepts `*mákōjaną > macian`, and the live explanatory support centers on the class-II retracted-`a` behavior of the stem (`mac-`, not `məc-/mæc-`) plus the trace-confirmed later weak-tail developments to `-ian` [Germanic/docs/DEV_NOTES.md:36531-36534; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3091-3103].

## Relevant DEV_NOTES fragments

### DEV_NOTES fragment 1

- Source heading: `### Implications for Class II Weak Verbs` / `## Class II Weak Verb Exploration (class2-weak-exploration branch)`
- Source line hint: `Germanic/docs/DEV_NOTES.md:2761-2861, 2899-2904`
- Fragment type: `shared_background_only_with_superseded_diagnostic_history`
- Status: `partly superseded, still relevant as background`
- Issue tags: `class_ii_weak_verbs`; `suffix_form__eian_vs_ian`; `citation_form_strategy`; `make_family`
- Recommended next use: `use only to explain earlier project hesitation about the infinitive row and the creation of companion paradigm-cell probes; do not cite as the current live verdict for row 2117`
- Shared-with rows if relevant: `2309 make (iptv.2sg) / maca`; `2310 make (3sg) / macaþ`; other class-II weak-verb explorations

This is the oldest surviving make-relevant DEV_NOTES material, and it matters mostly as project history. DEV_NOTES first grouped `*makōjăną` with other class-II weak verbs in a mismatch bucket: “The three Class II weak verbs in the mismatch report (suffix_form__eian_vs_ian): … `*makōjăną → maceian (expected macian)`” [Germanic/docs/DEV_NOTES.md:2761-2764]. The surrounding analysis then argued that the infinitive suffix `*-ōja-` was not a straightforward sound-law problem but a morphological one: “OE -ian does not derive by regular phonology from `*-ōjanan`” and, quoting Ringe/Taylor, “The Class 2 weak verbs are characterized in NWGmc by the stem-forming suffix `*-ō(ja)-` ... but the actual OE suffix `-i(g)an` is the result of a complex of analogical changes” [Germanic/docs/DEV_NOTES.md:2766-2769; Germanic/docs/DEV_NOTES.md:2901-2903]. For row 2117, this fragment remains useful only as a warning not to flatten the suffix history.

The same exploratory block then proposed paradigm-cell workarounds (`*makō > maca`, `*makōθi > maceþ / macaþ`) because the infinitive looked unreliable at that stage [Germanic/docs/DEV_NOTES.md:2840-2861; Germanic/docs/DEV_NOTES.md:2905-2917]. That proposal is **not** the current row state for 2117, but it explains why related make-family rows later appeared for `maca` and `macaþ`. For the present slice, the fragment should therefore be treated as **shared-background-only** and partly superseded implementation history, not as evidence that row 2117 still fails.

### DEV_NOTES fragment 2

- Source heading: `table of literature support inside the A-restoration/class-II discussion`
- Source line hint: `Germanic/docs/DEV_NOTES.md:36529-36534`
- Fragment type: `shared_background_literature_digest`
- Status: `current`
- Issue tags: `a_restoration`; `class_ii_weak_verbs`; `retracted_a`; `single_consonant_environment`
- Recommended next use: `cite as the main surviving philological support for why the OE stem should be mac- rather than fronted/palatalized mæc-`
- Shared-with rows if relevant: `2309 make (iptv.2sg) / maca`; `2310 make (3sg) / macaþ`; `2205 spare / sparian`; wider class-II rows such as `talian`, `lapian`, `bacian`

This is the strongest surviving DEV_NOTES support for row 2117, but it is still **shared** rather than lexeme-local. The literature table preserves two directly row-relevant quotations. Campbell §159 is quoted as listing “[…] weak verbs in `*-i-* (< *-ói-*), `lapian, macian, hnappian`, &c.” [Germanic/docs/DEV_NOTES.md:36531-36532]. Ringe/Taylor §6.3.1 is then quoted even more explicitly: “Weak verbs of class II always exhibit retracted `a` rather than `æ` before a non-nasal consonant in a monosyllabic root syllable […]. There are more than fifty examples; the following are typical: `carian, talian, macian, bacian, bapian, lapian, nacod, nafola, gafol, sadol, stapol, manslaga, hara, mara` […]” [Germanic/docs/DEV_NOTES.md:36533-36534].

For row 2117, the value of these quotations is precise. They do **not** by themselves prove every later `-ian` detail, but they do preserve the project's best surviving philological basis for the stem vowel: after Anglo-Frisian brightening would have created `*mæk-`, class-II A-restoration is exactly what brings the form back to `mak-`, matching the attested target `macian` and preventing a false palatalized `mæc-` path [Germanic/docs/DEV_NOTES.md:36531-36534; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3091-3103]. This fragment is therefore **current shared-background support**, not superseded material.

### DEV_NOTES fragment 3

- Source heading: `### §17.25.8 Post-fix verification`
- Source line hint: `Germanic/docs/DEV_NOTES.md:36757-36767`
- Fragment type: `diagnostic_verification_fragment`
- Status: `current`
- Issue tags: `post_fix_verification`; `class_ii_pathway`; `regression_check`; `make_family`
- Recommended next use: `cite when documenting that row 2117 is currently implemented successfully, not when making a purely literature-based claim`
- Shared-with rows if relevant: `2205 spare / sparian`; `2309 make (iptv.2sg) / maca`; other post-fix probe words in the same verification list

This fragment is implementation-facing rather than philological, but for row 2117 it is too direct to omit. After the A-restoration fixes, DEV_NOTES records the verification probes and explicitly includes “`*sákōjaną → sacian`, `*mákōjaną → macian` ✓” [Germanic/docs/DEV_NOTES.md:36762-36767]. That line matters because it reverses the practical situation found in the earlier exploration block: `macian` is no longer merely an expected target contrasted with a failing `maceian`; it is a checked successful outcome in the post-fix state.

The fragment should still be classified as **diagnostic**, not as primary-source literature support. Its value is that it anchors the slice to current project reality: as of the post-fix verification stage, the repo regarded `*mákōjaną > macian` as a successful derivation alongside other repaired class-II/A-restoration forms [Germanic/docs/DEV_NOTES.md:36757-36767]. For replacement-slice purposes, this is the closest surviving thing to a row-local implementation verdict.

## Superseded or diagnostic material

- The exploratory mismatch framing `*makōjăną → maceian (expected macian)` is superseded as a statement of the **current** row status. It should be preserved only as evidence of an earlier project stage in which class-II infinitives were thought to require alternative paradigm-cell handling [Germanic/docs/DEV_NOTES.md:2761-2764; Germanic/docs/DEV_NOTES.md:2840-2861].
- DEV_NOTES later says that, for the wider class-II weak-verb space (`carian, talian, lapian, macian, …`), “none of these are individual rows in our 386-OE TSV currently” [Germanic/docs/DEV_NOTES.md:36631-36633]. That statement is now plainly superseded by the live data: row 2117 exists and `coverage_audit.md` records it directly [Germanic/data/germanic-aligned-final.tsv:725-725; Germanic/docs/lexeme_reports/coverage_audit.md:304-304].
- The two current debug snapshots agree on the surface result `macian`, but they present the late suffix mechanics slightly differently. The publish derivation-class snapshot names “OE Unstressed EI Contraction: `*makian`,” while the full 2026-03-11 trace leaves the `Contraction` line inert and instead reaches `*makian` at `ProtoToOEWeightCleanup` before orthography [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3097-3103; Germanic/docs/debug_snapshots/oe_full_trace_report_2026-03-11.txt:8675-8690]. This looks diagnostic/reporting-level rather than lexical disagreement, but the distinction should be remembered if a future dossier tries to quote a single canonical named rule.
- The full trace snapshot also prints the proto header as `*makōjăną` rather than the accented TSV/publish-snapshot form `*mákōjaną` [Germanic/docs/debug_snapshots/oe_full_trace_report_2026-03-11.txt:8638-8643; Germanic/data/germanic-aligned-final.tsv:725-725]. Treat that as notation variance unless later work uncovers a substantive difference in encoded vowel quantity or accent placement.

## Open questions for later work

- Should row 2117 remain simply `regular` in the project taxonomy, or should the slice eventually say more explicitly that the OE class-II `-ian` ending still carries the historical/morphological warning preserved in the older DEV_NOTES exploration [Germanic/docs/DEV_NOTES.md:2901-2903]?
- If the make-family documentation is ever consolidated, should row 2117 be cross-linked more explicitly with rows 2309 (`maca`) and 2310 (`macaþ`) so that lemma-level `macian` evidence and paradigm-cell evidence are not conflated?
- When debug snapshots are regenerated, normalize the displayed proto notation and clarify which named late rule the project wants to foreground for the `*makeian`/`*makēian > *makian` step, since the current published snapshots do not label that step identically [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3097-3103; Germanic/docs/debug_snapshots/oe_full_trace_report_2026-03-11.txt:8675-8690].
