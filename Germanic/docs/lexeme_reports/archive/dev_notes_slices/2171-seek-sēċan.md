---
row_id: 2171
concept: seek
counterpart: sēċan
proto: *sōkijaną
protoform: *sōkijaną
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2171 seek / sēċan

## Current row state

- CONCEPT: `seek` [Germanic/data/germanic-aligned-final.tsv:935-935]
- COUNTERPART: `sēċan` [Germanic/data/germanic-aligned-final.tsv:935-935]
- PROTO: `*sōkijaną` [Germanic/data/germanic-aligned-final.tsv:935-935]
- PROTOFORM: `*sōkijaną` [Germanic/data/germanic-aligned-final.tsv:935-935]
- DERIVATION_CLASS: `regular` [Germanic/data/germanic-aligned-final.tsv:935-935]
- `oe_known_problems.tsv` has no row-local entry for row `2171`, for `seek`, for `sēċan`, or for `*sōkijaną`; the file currently lists unrelated exception and wontfix items only [Germanic/data/oe_known_problems.tsv:1-8].
- Coverage infrastructure still shows no linked packet, research memo, or dossier for this row; row `2171` appears in the coverage audit as `regular` with all linked-report fields blank and issue status `none` [Germanic/docs/lexeme_reports/coverage_audit.md:339-339].
- The current published derivation trace is an exact match: `PROTO: *sōkijaną`, `EXPECTED: sēċan`, `OUTPUTS: sēċan`. The OE-side stages now shown for the live row are `OE Heavy Syllable Nasal Apocope: *sōkijan`, `OE Secondary Nasalization: *sōkijąn`, `Sievers Law Syncope: *sōkjąn`, `OE Velar Palatalization: *sōʧjąn`, `OE I Umlaut: *sēʧjąn`, `OE Weak Tail Reduction: *sēʧjan`, and `OE J Loss After Heavy: *sēʧan`, followed by orthographic `*sēċan` and surface `sēċan` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3893-3913].

## Development-note summary

No long row-numbered `seek / sēċan` mini-dossier currently survives in `Germanic/docs/DEV_NOTES.md`, but the current shared notes are unusually explicit about this lexeme's derivational pathway. DEV_NOTES preserves the key handbook wording for the stem: Ringe & Taylor's `PGmc *sōkijană 'to look for, to seek' > PWGmc *sōkijan > *sōkjan > OE sēċan` and Fulk's `*sōkijanan > sēcan 'seek'` [@RingeTaylor2014, p. 157; @Fulk2018, §4.7]. Those exact quotations survive in the current note clusters that discuss PGmc input notation and source attestation [Germanic/docs/DEV_NOTES.md:8795-8805,8954-8979].

For this row, the most important distinction is between notation layers and chronological stages. The live TSV keeps `PROTO = PROTOFORM = *sōkijaną`, so the stored OE-facing input is the unsyncopated PGmc-form label [Germanic/data/germanic-aligned-final.tsv:935-935]. Current DEV_NOTES material, however, also preserves two other forms that must not be confused with competing row targets: `(1)` the handbook-style PGmc `*sōkijăną/*sōkijană`, which spells out the heavy-stem `-ij-` infinitive more explicitly, and `(2)` the later PWGmc stage `*sōkjăną`, which is the post-syncope form after `*-CijV- > *-CjV-` [@RingeTaylor2014, p. 157; @Fulk2018, §4.7]. DEV_NOTES keeps both stages visible [Germanic/docs/DEV_NOTES.md:8831-8836,8930-8930,8961-8979]. These are not rival reconstructions for the row. They are the same lexeme seen at different analytical resolutions, and the current exact-match trace confirms that the project can already derive OE `sēċan` from the stored live input without any workaround [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3893-3913].

The concrete sound-law content that matters for the row is also well preserved. DEV_NOTES' Sievers-law update says heavy-stem Class I weak verbs keep `*-ij-` at the PGmc input stage, then undergo a regular PWGmc syncope `*-CijV- > *-CjV-`, with `*sōkijăną → *sōkjăną` as the explicit example, and then proceed to OE `sēċan` [@RingeTaylor2014, p. 157; Germanic/docs/DEV_NOTES.md:8795-8836]. The live derivation trace shows exactly the OE-side continuation of that story: after syncope, `kj` palatalizes (`*sōkjąn > *sōʧjąn`), then the following `j` triggers i-umlaut (`*sōʧjąn > *sēʧjąn`), and only afterward do weak-tail reduction and `j`-loss produce `*sēʧan > sēċan` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3900-3913].

A second current DEV_NOTES passage matters because it confirms that `sēċan` is not some ad hoc umlaut rescue. In the long-vowel i-umlaut discussion, `*sōkjan → sēċan` is listed alongside `*dōmjan → dēman`, `*fōdjan → fēdan`, and `*kōpjan → cēpan` as a canonical example of the standard long-vowel umlaut pathway, i.e. the same rule family described in the handbooks for long-vowel umlaut before `j` [@Campbell1959, §198; @RingeTaylor2014, pp. 189-190]. DEV_NOTES preserves that comparator list explicitly [Germanic/docs/DEV_NOTES.md:37268-37273]. At row level, the exact-match trace shows the same order of events: palatalization first, then i-umlaut of internal `ō` to `ē`, not a special lexeme-specific vowel substitution [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3900-3913].

The only strong caution to preserve is historical rather than current. Earlier DEV_NOTES diagnostics caught this lexeme as a real failure case: `*sōkjăną` was reported as giving `suscġan` instead of expected `sēċan`, and the note warned that apparent `sc` outputs in such cases reflected upstream fronting or umlaut failure, not a harmless spelling preference [Germanic/docs/DEV_NOTES.md:2581-2586]. That older diagnostic is still useful because it explains what used to be wrong and why the row once exposed both missing front-vowel conditioning and masked palatalization. But it is no longer current row status. The live published trace now lands exactly on `sēċan`, so the replacement working note for row `2171` should treat the old `suscġan` note as resolved project history rather than as present row policy [Germanic/docs/DEV_NOTES.md:2581-2586; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3893-3913].

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-8795-8836

- Source heading: `DECISION UPDATE (2026-03-13): Adopting PGmc Input Notation`
- Source line or section hint: `lines 8795-8836`
- fragment_type: `lexeme_specific`
- current_status: `current`
- Issue tags: `heavy_stem_class_i`; `sievers_law_syncope`; `protoform_vs_proto`; `palatalization`
- recommended_next_use: `cite_in_final_report`
- Shared with row IDs:

This is the controlling current fragment for how the row's PGmc and PWGmc stages should be read. DEV_NOTES distinguishes the ordinary heavy-stem infinitive in `*-ij-` from the later PWGmc syncopated outcome and gives `seek` as the explicit example. The preserved handbook chain is `PGmc *sōkijană 'to look for, to seek' … > PWGmc *sōkijan > *sōkjan > OE sēċan` [@RingeTaylor2014, p. 157]. DEV_NOTES then restates the same chronology in project notation as `*sōkijăną → *sōkjăną` (syncope) and finally `*sōkjăną → OE sēċan` [Germanic/docs/DEV_NOTES.md:8795-8836]. For row `2171`, that establishes that the live stored form `*sōkijaną` is the pre-syncope comparator, not an error, and that the shorter `*sōkj-` form belongs to the subsequent PWGmc stage rather than to the TSV's top-line `PROTO/PROTOFORM` fields [Germanic/data/germanic-aligned-final.tsv:935-935].

It also explains why the row should remain regular after syncope. DEV_NOTES states that heavy stems do not undergo j-gemination because the `i` intervenes (`*k-i-j`, not `*k-j`), so syncope must be ordered after gemination and before later palatalization [Germanic/docs/DEV_NOTES.md:8838-8867]. The current derivation trace shows exactly that downstream result for this row: once the `i` is removed, `kj` becomes the palatalizable cluster that yields OE `ċ`, and the surviving `j` still triggers the `ō > ē` umlaut before being lost later [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3900-3913].

### DEV_NOTES:line-8954-8979

- Source heading: `Source Attestation of *-ijăną Forms (2026-03-13)`
- Source line or section hint: `lines 8954-8979`
- fragment_type: `lexeme_specific`
- current_status: `current`
- Issue tags: `source_attestation`; `heavy_stem_class_i`; `pgmc_input_notation`; `literature_support`
- recommended_next_use: `cite_in_final_report`
- Shared with row IDs:

This is the strongest direct literature-attestation fragment for the lexeme. DEV_NOTES' source table names `seek` twice: Fulk §4.7 with `*sōkijanan > sēcan 'seek'` and Ringe & Taylor p.157 with `PGmc *sōkijană 'to look for, to seek'` [@Fulk2018, §4.7; @RingeTaylor2014, p. 157]. DEV_NOTES preserves those entries explicitly [Germanic/docs/DEV_NOTES.md:8961-8979]. That makes the row more secure than a generic heavy-stem analogy case, because the same lexeme is directly attested in both handbook traditions as a `*-ij-` infinitive with OE reflex `sēċan/sēcan`.

For row `2171`, the fragment is useful both positively and cautiously. Positively, it confirms that a PGmc input with `-ij-` is the literature-backed starting point for the OE infinitive. Cautiously, it shows why the slice should keep `PROTO`, `PROTOFORM`, and later syncopated forms distinct in prose: the live TSV's `*sōkijaną` is aligned with the same structural form as DEV_NOTES' `*sōkijăną/*sōkijană`, while the shorter `*sōkjăną` belongs to the later derivational stage and should not be mistaken for the stored row header [Germanic/data/germanic-aligned-final.tsv:935-935; Germanic/docs/DEV_NOTES.md:8930-8930,8961-8979].

### DEV_NOTES:line-37268-37273

- Source heading: `.1.c Sound-change pathway from *bōjenō (the Sievers/Brunner/Orel pathway)`
- Source line or section hint: `lines 37268-37273`
- fragment_type: `phenomenon_context_for_lexeme`
- current_status: `current`
- Issue tags: `long_vowel_i_umlaut`; `canonical_example`; `shared_row_support`; `oe_sound_change_context`
- recommended_next_use: `cite_in_final_report`
- Shared with row IDs:

This is the clearest current shared DEV_NOTES statement that the vowel development in `sēċan` is ordinary rule-governed phonology. In giving the standard chronology for another lexeme, DEV_NOTES explicitly identifies long-vowel i-umlaut as the “canonical rule” and names the same comparator set: `*sōkjan → sēċan`, `*dōmjan → dēman`, `*fōdjan → fēdan`, `*kōpjan → cēpan` [Germanic/docs/DEV_NOTES.md:37268-37273]. The rule context is the ordinary long-vowel umlaut pathway described in the standard handbooks [@Campbell1959, §198; @RingeTaylor2014, pp. 189-190]. For row `2171`, that directly supports the central middle step of the current trace, `*sōʧjąn → *sēʧjąn`, and shows that the OE `ē` is not some row-local special pleading.

This fragment should be cited together with the exact-match derivation trace, not instead of it. The DEV_NOTES line supplies the high-level rule identity; the trace supplies the row-specific stage ordering, including the fact that palatalization precedes umlaut in the current implementation [Germanic/docs/DEV_NOTES.md:37268-37273; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3900-3913]. Used together, they make the slice self-sufficient on why `seek` is now a regular-control lexeme.

## Superseded or diagnostic material

### DEV_NOTES:line-2581-2586

- Source heading: `OE i-umlaut deep dive (2025-12-23)`
- Source line or section hint: `lines 2581-2586`
- fragment_type: `superseded_or_diagnostic_for_lexeme`
- current_status: `diagnostic_only`
- Issue tags: `old_umlaut_failure`; `palatalization_masking`; `resolved_regression`; `project_history`
- recommended_next_use: `use_as_project_history_only`
- Shared with row IDs:

This older diagnostic is still worth preserving because it records the exact failure mode the row used to expose. DEV_NOTES flagged `*sōkjăną` among the “Targeted umlaut misses” with expected `sēċan` but output `suscġan`, then warned that apparent `ċ/sc` mismatches in such outputs were not mere orthographic variation but visible evidence that the front-vowel context for palatalization was missing upstream [Germanic/docs/DEV_NOTES.md:2581-2586].

For current row work, though, this fragment is historical only. The live published derivation now reaches `sēċan` exactly, with explicit palatalization and i-umlaut stages present in the trace [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3893-3913]. Later reviewers should therefore use `2581-2586` only to explain the resolved bug history behind the row, not to characterize the current state of row `2171`.

- A second search caution is textual rather than phonological: DEV_NOTES still contains an older pre-update heavy-stem table with `*sōkjăną | ... | sēċan`, but that table belongs to the superseded post-Sievers-leveling notation discussion immediately overridden by the later “DECISION UPDATE” adopting PGmc `*-ij-` input notation [Germanic/docs/DEV_NOTES.md:8722-8739,8763-8773]. For current row documentation, the later `*-ij-` policy and the exact-match live trace should control.
- DEV_NOTES line `42004` is not row authority for `2171`; it is merely an English-bin file-line reference (`OEUnstressedLongVowelShortening3`) inside a deferred ModE-stage audit [Germanic/docs/DEV_NOTES.md:41999-42005]. It should not be indexed as if it were a lexeme note for `seek`.

## Open questions for later work

- If the row is ever indexed centrally, keep the stage distinction explicit in the one-line summaries: live TSV `PROTO = PROTOFORM = *sōkijaną`, current literature-attested PGmc heavy-stem notation `*sōkijăną/*sōkijană`, later PWGmc syncope stage `*sōkjăną`, and OE target `sēċan` [Germanic/data/germanic-aligned-final.tsv:935-935; Germanic/docs/DEV_NOTES.md:8795-8836,8954-8979].
- If a later packet or memo is created, quote the exact handbook wording already preserved in DEV_NOTES rather than paraphrasing it away; for this row the strongest surviving lexeme-specific authority is the direct Fulk and Ringe-Taylor attestation of `*sōkijanan/*sōkijană > sēcan/sēċan` [@Fulk2018, §4.7; @RingeTaylor2014, p. 157; Germanic/docs/DEV_NOTES.md:8961-8979].
- No literature-agent pass is required for the present slice, but a future reviewer could still tighten notation policy by deciding whether live TSV `*sōkijaną` should remain the house form or be normalized to the more explicit DEV_NOTES-style `*sōkijăną`; the current slice preserves the distinction without asserting that a row rewrite is presently required [Germanic/data/germanic-aligned-final.tsv:935-935; Germanic/docs/DEV_NOTES.md:8930-8930,8961-8979].
