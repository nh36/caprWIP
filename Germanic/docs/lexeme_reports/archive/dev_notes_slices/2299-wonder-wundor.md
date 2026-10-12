---
row_id: 2299
concept: wonder
counterpart: wundor
proto: "*wúndrą"
protoform: "*wúndrą"
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file: ""
linked_research_memo_file: ""
linked_dossier_or_analysis_files:
  - Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md
  - Germanic/docs/debug_snapshots/oe_full_trace_report.txt
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2299 wonder / wundor

## Current row state

- The live TSV row is `2299 | wonder | wundor | *wúndrą | *wúndrą | regular`. The row still carries the inherited placeholder note `MT | TODO: replace with attested Old English form | Source: Wiktionary etymology (template:inh) | Source: Wiktionary etymology (template:inh)`, so the TSV itself does **not** preserve the real reasoning behind the current classification [Germanic/data/germanic-aligned-final.tsv:1432-1432].
- `PROTO` and `PROTOFORM` are currently identical in the live row, but the distinction still matters here. `PROTO = *wúndrą` is the comparative Germanic headword published in the row; `PROTOFORM = *wúndrą` is also the actual OE derivational input currently chosen by the project; `COUNTERPART = wundor` is the targeted Old English reflex, not another proto-level label [Germanic/data/germanic-aligned-final.tsv:1432-1432].
- The lexical target itself is attested and not merely a spreadsheet invention: `old_english_wiktionary.tsv` has the direct entry `wonder\twundor\tinh\ttemplate:inh\twonder` [Germanic/data/old_english_wiktionary.tsv:355-355]. That makes the TSV's lingering `TODO: replace with attested Old English form` diagnostic metadata rather than a sign that the row lacks an OE target [Germanic/data/germanic-aligned-final.tsv:1432-1432; Germanic/data/old_english_wiktionary.tsv:355-355].
- No row-specific problem entry is currently tracked in `oe_known_problems.tsv`; the file only lists other protoforms such as `*búkkaz`, `*fúglaz`, `*wúlfaz`, `*wúllō`, `*rústō`, `*fūri`, and `*táppô`, not `*wúndrą` [Germanic/data/oe_known_problems.tsv:1-8].
- Coverage/report infrastructure is still empty for this row: `coverage_audit.md` records `| 2299 | wonder | wundor | regular | no | - | - | - | none |`, and no row-local packet or memo is linked from the current lexeme-report scaffolding [Germanic/docs/lexeme_reports/coverage_audit.md:418-418].
- The current published derivation snapshot already matches the live row exactly: `PROTO: *wúndrą`, `EXPECTED: wundor`, `OUTPUTS: wundor`, with the decisive OE stages `OE Heavy Syllable Nasal Apocope: *wúndr` and `OE Epenthetic Vowel: *wúndor`, then surface `Outcome: wundor` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:6025-6044].
- The full trace says the same thing at higher resolution: `OEHeavySyllableNasalApocope: *w*ú*n*d*r`, then `OEEpentheticVowel: *w*ú*n*d*o*r`, then `OldEnglishRemoveStars: wundor` [Germanic/docs/debug_snapshots/oe_full_trace_report.txt:41067-41180]. For the live row, that trace is stronger evidence than the inherited TSV note because it shows the present implementation already deriving the target without any workaround [Germanic/docs/debug_snapshots/oe_full_trace_report.txt:41067-41180].
- A separate temporary sandbox artifact is presently out of step with the live row: it uses accentless `*wundrą` and reports `outputs: []` for `wonder / wundor` [Germanic/tmp/old_english_sandbox_results_current.json:3513-3517; Germanic/tmp/old_english_sandbox_results_with_stages.json:52923-52927]. That should be treated as diagnostic/stale auxiliary output, not as the authority over the publish trace or the TSV.

## Development-note summary

No dedicated wonder-specific DEV_NOTES dossier survives. That needs to be said plainly. The row's current support is a mixture of (a) one **indirect but row-specific** precedent note embedded inside the later `shoulder / sċuldor` investigation, (b) several **shared-background-only** phonology/class notes that include `wundor` among ordinary OE parasite-vowel outcomes, and (c) a later **diagnostic** no-regression spot-check. There is no standalone `wonder / wundor` section comparable to the long lexeme-specific notes for harder rows [Germanic/docs/DEV_NOTES.md:22635-22643,29853-29866,30124-30132,39397-39406,39790-39830].

The most important surviving row-facing statement is the indirect precedent note in the `shoulder` dossier. DEV_NOTES there contrasts `shoulder` with this row and states that `*wúndrą` avoids u-lowering because of the “nasal+C blocker,” then later says explicitly: “TSV row 2299 (*wundor*) declares PROTOFORM `*wúndrą` (i.e., a non-NSg cell with high-vowel suffix), exactly parallel to the move recommended here” [Germanic/docs/DEV_NOTES.md:39403-39406,39818-39823]. Even though that passage is not a wonder dossier, it is still the nearest thing to a row-specific project rationale now preserved in DEV_NOTES: the project already treats `*wúndrą` as a legitimate cell-selected input whose high-vowel environment keeps `u` from lowering.

The broader class support is also substantial, but it is shared rather than bespoke. Campbell's quotation copied into DEV_NOTES lists `wundor` among the “Normal OE forms”: “þunor, wundor, winter ...” [Germanic/docs/DEV_NOTES.md:22639-22643]. Later DEV_NOTES class notes likewise include `wundor` among the ordinary back-vowel parasite-vowel outcomes: “*o* after back stressed vowels: *fugol, wuldor, wundor, māþum, bōsom*” [Germanic/docs/DEV_NOTES.md:29857-29866]. Those passages matter because they make `wundor` look like a normal member of an established OE outcome class, not an isolated spreadsheet exception.

The current row therefore looks regular for two separate reasons that should not be collapsed. First, the retained `u` is supported by the row's selected `PROTOFORM = *wúndrą` plus DEV_NOTES' explicit comparison with the nasal+C blocker in contrast to `shoulder` [Germanic/docs/DEV_NOTES.md:39403-39406,39818-39823]. Second, the surface `-or` is supported by the shared OE parasite-vowel class notes that explicitly name `wundor` [Germanic/docs/DEV_NOTES.md:22639-22643,29857-29866]. The publish/full traces then show that the current implementation already realizes exactly that combination: heavy-syllable apocope to `*wúndr`, then epenthesis to `*wúndor`, then surface `wundor` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:6032-6044; Germanic/docs/debug_snapshots/oe_full_trace_report.txt:41110-41180].

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-39403-39406; DEV_NOTES:line-39790-39823

- Source heading: `What's been established (still valid)` / `Q4 finding — lautgesetz status (cell-switch, not wontfix)`
- Source line hint: `lines 39403-39406, 39790-39823`
- Fragment type: `indirect_row_specific_project_precedent`
- Status: `current`
- Issue tags: `protoform_selection`; `u_retention`; `nasal_plus_consonant_blocker`; `cell_switch_precedent`
- Recommended next use: `best surviving row-specific anchor`
- Shared-with rows if relevant: `shoulder / sċuldor` comparison work; other cell-switch rows in the `wolf/wool/fugol` cluster

This is the nearest surviving thing to a row-local project rationale, even though it lives inside the `shoulder` investigation rather than a `wonder` section. First, DEV_NOTES distinguishes the two lexemes directly: “All NSg cells of shoulder ... u-lower → `sċoldor`; `*wúndrą`'s escape is via the nasal+C blocker (Campbell §§115–118), absent in shoulder” [Germanic/docs/DEV_NOTES.md:39403-39406]. Later, in the explicit recommendation block, it treats row 2299 as already-set project precedent: “TSV row 2299 (*wundor*) declares PROTOFORM `*wúndrą` (i.e., a non-NSg cell with high-vowel suffix), exactly parallel to the move recommended here” [Germanic/docs/DEV_NOTES.md:39818-39823].

For row 2299, this fragment should be used carefully but definitely. It is **not** a complete wonder dossier; it does **not** narrate the whole derivation; and its immediate target is another lexeme. But it does preserve two things that are otherwise easy to lose: (1) the row's retained `u` is not being treated as an unexplained exception, but as the expected result of a selected high-vowel cell plus the nasal+C environment; and (2) the project's use of `PROTOFORM = *wúndrą` is already recognized inside DEV_NOTES as an established precedent, not an ad hoc spreadsheet oddity [Germanic/docs/DEV_NOTES.md:39403-39406,39790-39823].

### DEV_NOTES:line-22635-22643

- Source heading: `Case 2 — *sáiwalō → sāwul (expected sāwol)`
- Source line hint: `lines 22635-22643`
- Fragment type: `shared_background_handbook_quote`
- Status: `current`
- Issue tags: `campbell_quote`; `normal_oe_forms`; `parasite_vowel_class`; `shared_background_only`
- Recommended next use: `secondary class anchor`
- Shared-with rows if relevant: `2255 thunder`; `2295 winter`; other `-or/-er` parasite-vowel rows

This fragment is shared background only, but it is still highly relevant because it preserves the exact handbook wording that classifies `wundor` as ordinary Old English. DEV_NOTES quotes Campbell §362: “Normal OE forms are fugol, tungol, cumbol, **sāwol**, nagel, æppel, segel, þunor, wundor, winter, fæger, æcer, hrefen, ofen, bēsum, māþum, westum” [Germanic/docs/DEV_NOTES.md:22639-22643]. For row 2299, the value of that quotation is not protoform selection and not u-retention; it is specifically the surface-side classification of `wundor` as a normal OE parasite-vowel outcome.

Because this quotation is embedded in a `sāwol` discussion, it should not be mislabelled as wonder-specific support. Its status is **shared-background-only**. But it is strong shared background: it shows that once the row reaches a final `wundr`-type cluster, `wundor` is exactly the sort of West Saxon output Campbell treats as ordinary rather than exceptional [Germanic/docs/DEV_NOTES.md:22635-22643].

### DEV_NOTES:line-29853-29866

- Source heading: `§17.18.1 The lautgesetzlich background (Campbell §§360–363; Hogg §§6.30–6.36; SB §§145–146)`
- Source line hint: `lines 29853-29866`
- Fragment type: `shared_background_phonology_note`
- Status: `current`
- Issue tags: `final_cluster_epenthesis`; `back_vowel_o`; `wundor_named`; `shared_background_only`
- Recommended next use: `main shared derivational background`
- Shared-with rows if relevant: `wuldor`; `fugol`; `māþum`; other final obstruent+sonorant rows

This later class note is the clearest shared phonological background for the final `-or` shape. DEV_NOTES explains that in nominative/accusative singular a-stems, the cluster falls word-finally and “late OE develops a parasite vowel,” then gives the back-vowel side explicitly: “*o* after back stressed vowels: *fugol, wuldor, wundor, māþum, bōsom*” [Germanic/docs/DEV_NOTES.md:29857-29861]. The immediate section is about a wider `-Cl/-Cr/-Cn/-Cm#` investigation, not specifically about `wonder`, so its status is again **shared-background-only**.

Even so, this fragment should carry real weight for row 2299 because it states the exact class behavior the live trace now implements. After the selected protoform loses final nasal vowel material in the heavy syllable, the project trace reaches `*wúndr`; the shared class note then explains why OE supplies back-vocalic `o`, yielding `wundor` rather than some other repair [Germanic/docs/DEV_NOTES.md:29857-29866; Germanic/docs/debug_snapshots/oe_full_trace_report.txt:41130-41180].

### DEV_NOTES:line-30124-30132

- Source heading: `§17.18.7.2 Implementation steps`
- Source line hint: `lines 30124-30132`
- Fragment type: `diagnostic_no_regression_probe`
- Status: `diagnostic_only`
- Issue tags: `spot_check`; `no_regression`; `wundor_named`; `diagnostic`
- Recommended next use: `background only`
- Shared-with rows if relevant: `wuldor`; `fæder`; the broader cluster-regression check set

This fragment is diagnostic rather than explanatory. In the verification checklist for another change, DEV_NOTES instructs the project to “Spot-check no regressions on -gl# (fugol, seġel) or -Cr# (wuldor, wundor, fæder)” [Germanic/docs/DEV_NOTES.md:30131-30132]. That does not explain why row 2299 works; it only shows that by this point `wundor` was already treated as a stability probe that later work was not supposed to break.

The fragment is therefore worth preserving, but only as implementation history. It supports the claim that `wundor` was already considered a correct, stable member of the regular cluster-output set; it does **not** replace the row's actual background support from the Campbell quotation, the class note, or the row-2299 precedent passage [Germanic/docs/DEV_NOTES.md:30124-30132].

## Superseded or diagnostic material

- No standalone wonder-specific DEV_NOTES block survives. The row-specific material that does survive is indirect: it appears only when the `shoulder` dossier points back to row 2299 as existing precedent [Germanic/docs/DEV_NOTES.md:39790-39823].
- The lingering TSV note `TODO: replace with attested Old English form` is superseded/diagnostic metadata, not a trustworthy statement of row status, because the row already targets attested `wundor` and the attested-form lookup file already contains that pairing [Germanic/data/germanic-aligned-final.tsv:1432-1432; Germanic/data/old_english_wiktionary.tsv:355-355].
- The temporary sandbox JSON files are also diagnostic only for this row at present. They use accentless `*wundrą` and show no outputs, whereas the publish trace and full trace both derive `wundor` cleanly from the live accented protoform `*wúndrą` [Germanic/tmp/old_english_sandbox_results_current.json:3513-3517; Germanic/tmp/old_english_sandbox_results_with_stages.json:52923-52927; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:6025-6044].
- The later no-regression spot-check naming `wundor` is useful diagnostic history but not primary explanatory support [Germanic/docs/DEV_NOTES.md:30124-30132].

## Open questions for later work

- If this row later receives a full packet or pilot report, the first task should be to turn the indirect `shoulder`-dossier precedent into a direct wonder-facing explanation, because the current evidence is good but scattered [Germanic/docs/DEV_NOTES.md:39403-39406,39790-39823].
- If the auxiliary sandbox artifacts are meant to be authoritative again, they need reconciliation with the live TSV/protoform spelling and the publish trace, since they currently record accentless `*wundrą` with no outputs while the canonical traces derive `wundor` successfully from `*wúndrą` [Germanic/tmp/old_english_sandbox_results_current.json:3513-3517; Germanic/docs/debug_snapshots/oe_full_trace_report.txt:41067-41180].
- If `index.tsv` is revisited later, the safest anchor is probably the indirect-but-row-specific precedent block at `DEV_NOTES:line-39790-39823`, with `DEV_NOTES:line-22635-22643` and `DEV_NOTES:line-29853-29866` as shared background anchors rather than primary row-local ones.
