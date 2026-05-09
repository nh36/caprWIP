---
row_id: 2296
concept: withy
counterpart: wīþiġ
proto: *wáiθiz
protoform: *wḯθagą
derivation_class: early_analogy
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file: Germanic/docs/lexeme_reports/packets/2296-withy-wīþiġ.md
linked_research_memo_file: Germanic/docs/lexeme_reports/research_memos/2296-withy-wīþiġ.md
linked_dossier_or_analysis_files:
  - Germanic/docs/analysis/notable_findings.md
  - Germanic/docs/analysis/fryhtu_investigation.md
  - Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2296 withy / wīþiġ

## Current row state

- The live OE row now explicitly separates the comparative cognate-set headword from the OE derivational input: `PROTO = *wáiθiz`, `PROTOFORM = *wḯθagą`, `COUNTERPART = wīþiġ`, `DERIVATION_CLASS = early_analogy`, with a row note stating that OE `-ig` continues PGmc `*-ag-` rather than a heavy ja-stem `*-ij-` [Germanic/data/germanic-aligned-final.tsv:1420-1420].
- This row still sits in the coverage audit as a note-bearing `early_analogy` item with no manifest-backed report, so the slice has to preserve the actual row-local reasoning rather than relying on pilot infrastructure [Germanic/docs/lexeme_reports/coverage_audit.md:171-171; Germanic/docs/lexeme_reports/report_manifest.tsv:1-13].
- `oe_known_problems.tsv` currently lists other accepted exceptions only; row 2296 is absent, which matches the fact that the current `PROTOFORM` already derives the target and no longer needs a known-problem ledger entry [Germanic/data/oe_known_problems.tsv:1-8].
- The current published derivation trace is fully aligned with the live row: `Proto Input: *wḯθagą`, `EXPECTED: wīþiġ`, `OUTPUTS: wīþiġ`, with the stages `*wḯθægą > *wḯθæg > *wḯθæʤ > *wḯθeʤ > *wḯθiʤ > wīþiġ` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:6863-6883].
- The packet and research memo already reflect the same settled state: the row is no longer being treated as a live Sievers-law bug, but as an OE-specific derivative where `PROTOFORM = *wḯθagą` is the sound-law-clean input and `PROTO = *wáiθiz` is kept as the comparative family label [Germanic/docs/lexeme_reports/packets/2296-withy-wīþiġ.md:5-10,17-43; Germanic/docs/lexeme_reports/research_memos/2296-withy-wīþiġ.md:4-18,64-73].

## Development-note summary

The surviving DEV_NOTES material for row 2296 divides cleanly into two layers. The **current row-specific authority** is the 2026-04-23 closure at §17.10.35, which says the old `*wīθijaz` analysis was not exposing a missing OE rule at all; it was the wrong morphology for the attested OE noun. In that section DEV_NOTES states flatly that OE `wiðiġ / wīðiġ` “does not contain a productive ja-stem adj. suffix; it contains the homophonous nominal/adjectival derivational suffix `-iġ`, whose source is PGmc `*-ag-` (short *a), NOT `*-ij-`,” and it anchors that claim in Campbell §275(7) and §376 [Germanic/docs/DEV_NOTES.md:26218-26310]. That is the controlling explanation for the live row.

The older 2026-03-19 withy note is still worth preserving, but only as **superseded row-specific diagnosis** plus **useful negative evidence**. It correctly observed that if one insists on `*wīþijaz` / `*wīθijăz` as a heavy ja-stem input, the FST’s output `wīþ` is phonologically plausible, not random noise; it also assembled the key handbook/literature point that heavy monosyllabic ja-stems should give OE `-e` or zero, not `-ig` [Germanic/docs/DEV_NOTES.md:12482-12530,12637-12647,12780-12803]. What it got wrong was the repair strategy: the note tried to save the ja-stem by restricting syncope, whereas the later closure concludes that the morphology itself must change.

The best conservative row reading is therefore: `PROTO` and `PROTOFORM` should not be collapsed. `PROTO = *wáiθiz` remains the comparative/cognate-set label attached to the broader family in the live TSV, while `PROTOFORM = *wḯθagą` is the OE modelling input actually justified by the project’s current sound-change and suffix analysis [Germanic/data/germanic-aligned-final.tsv:1420-1420]. Support for that distinction is partly **row-specific current** (§17.10.35), partly **shared-background-only** (Campbell on `-ig < -eg < -æg`), and partly **superseded/diagnostic** (the older Sievers-law framing and related test-battery mentions) [Germanic/docs/DEV_NOTES.md:26226-26233,26316-26344; Germanic/docs/analysis/notable_findings.md:1312-1395].

One project-history wrinkle should stay explicit. §17.10.35 originally proposed changing not only `PROTOFORM` but the TSV `PROTO` column “likewise” to `*wīθagą` [Germanic/docs/DEV_NOTES.md:26346-26355]. The live row did **not** follow that last step: it now keeps comparative `PROTO = *wáiθiz` while changing only `PROTOFORM`. For this slice, treat the live TSV distinction as current row policy and the broader PROTO-rewrite plan as superseded implementation history [Germanic/data/germanic-aligned-final.tsv:1420-1420; Germanic/docs/DEV_NOTES.md:26346-26355].

## Relevant DEV_NOTES fragments

### DEV_NOTES fragment 1

- Source heading: `OE wīþiġ 'withy': ja-stem Adjective vs Sievers' Law Syncope (2026-03-19)`
- Source line hint: `Germanic/docs/DEV_NOTES.md:12482-12530`
- Fragment type: `lexeme_specific`
- Status: `superseded`
- Issue tags: `heavy_ja_stem`; `sievers_law`; `suffix_loss`; `project_history`
- Recommended next use: `preserve_only_as_superseded_bug_history`
- Shared-with rows: `none`

This is the first row-local project diagnosis and it should survive because it records the exact bug state that later notes are answering. DEV_NOTES framed the row as `PROTOFORM: *wīθijăz` / `COUNTERPART: wīþiġ` and said: “FST produces `wīþ` instead of expected `wīþiġ`. The `-ij-` suffix is being incorrectly deleted.” It then traced the loss through `SieversLawSyncope` and `OEJLossAfterHeavy`, and explicitly claimed that `*wīþijaz` was “a **ja-stem adjective**, NOT a weak verb,” so the weak-verb-style syncope rule should not have applied here [Germanic/docs/DEV_NOTES.md:12487-12530]. Keep this fragment as project history, not current doctrine. Its lasting value is that it preserves the original wrong hypothesis in a form precise enough to explain later reversal.

### DEV_NOTES fragment 2

- Source heading: `same 2026-03-19 withy note: Comprehensive Source Research`
- Source line hint: `Germanic/docs/DEV_NOTES.md:12606-12617; 12637-12647; 12780-12803`
- Fragment type: `lexeme_specific_with_shared_background`
- Status: `diagnostic`
- Issue tags: `kluge_headword`; `campbell_ja_nouns`; `adamczyk`; `negative_control`
- Recommended next use: `reuse_only_as_negative_evidence_against_reviving_*wīþijaz`
- Shared-with rows: `none`

This older research block remains useful because it preserves both the comparative temptation and the phonological reason not to follow it. On the one hand it quotes Kluge-Seebold: “Aus g. `*wīþja/ō` m./f. 'Weide', auch in anord. `víðir` m., ae. `wīþig` m.; vielleicht ist eine ältere Form `*wīþw-` ...” — exactly the kind of tidy cognate-set reconstruction that led the project toward `*wīθijaz` in the first place [Germanic/docs/DEV_NOTES.md:12606-12617]. On the other hand the same note quotes Campbell §576 on the loss of ja-stem `*i/ī` after heavy syllables and then, after integrating Adamczyk 2001, states the crucial negative result: heavy monosyllabic ja-stems carry OE `-e`, and therefore “The attested form `wīþig` cannot derive regularly from a ja-stem with this proto-form” [Germanic/docs/DEV_NOTES.md:12637-12647,12780-12803]. That combination still matters. Use it as diagnostic evidence that the older ja-stem pathway fails even before the later `*-ag-` solution is adopted.

### DEV_NOTES fragment 3

- Source heading: `§17.10.35 *wīθijaz → wīþ (expected wīþiġ): wrong suffix etymology`
- Source line hint: `Germanic/docs/DEV_NOTES.md:26201-26310`
- Fragment type: `lexeme_specific`
- Status: `current`
- Issue tags: `wrong_suffix_etymology`; `ag_suffix`; `protoform_reanalysis`; `row_closure`
- Recommended next use: `treat_as_primary_row_authority`
- Shared-with rows: `2079 huniġ` (suffix comparison only)

This is the decisive row-specific replacement note. DEV_NOTES now says the FST was not failing on `*wīθijaz`; rather, “The FST actually does what that morphology says,” because a heavy ja-stem in `*-ijaz` should collapse to bare `wīþ` [Germanic/docs/DEV_NOTES.md:26213-26216]. The note then reverses the older premise: the Wiktionary/Kluge-style `*-ijaz` reconstruction is “the wrong etymology for OE `wiðiġ / wīðiġ` 'willow, withy'.” Instead, the noun “does not contain a productive ja-stem adj. suffix; it contains the homophonous nominal/adjectival derivational suffix `-iġ`, whose source is PGmc `*-ag-` (short *a), NOT `*-ij-`” [Germanic/docs/DEV_NOTES.md:26218-26223].

The same fragment also preserves the source stack that now carries real row weight. Campbell §275(7) is quoted for the claim that the suffix `-ig` represents Primitive OE `-æg`, with examples including `hunig`, `wiðig`, and `bodig`; Campbell §376 is quoted for the later raising sequence `-ig < -eg < -æg` before palatal `g`; Hall is cited for OE `wiþig. wiðiġe m.`; Orel is used to distinguish related feminine formations `*wiþiz` and `*wiþjōn`; Kluge is kept, but only as a comparative headword source whose ja-/jō-stem shorthand “fails lautgesetzlich verification”; and Kroonen’s silence is treated as consistent with the idea that the OE masculine is a transparent derivative rather than a direct reflex of one inherited PGmc lemma [Germanic/docs/DEV_NOTES.md:26224-26310]. That combination of quotations and synthesis is the material that should actually replace consulting DEV_NOTES for this row.

### DEV_NOTES fragment 4

- Source heading: `same §17.10.35 note: probe of proposed PROTOFORM`
- Source line hint: `Germanic/docs/DEV_NOTES.md:26311-26344`
- Fragment type: `lexeme_specific`
- Status: `current`
- Issue tags: `probe_success`; `derivation_chain`; `long_i`; `current_input_form`
- Recommended next use: `cite_when_justifying_live_PROTOFORM`
- Shared-with rows: `2079 huniġ` (formal suffix parallel only)

This fragment is the current implementation-facing proof. DEV_NOTES explicitly compares row 2296 with `*xúnagą → huniġ`, notes that the required `*-ag-` shape is already supported by the existing allow-list, and then runs the crucial probe: ``$ echo wīθagą | flookup -i old_english.bin`` → `wīθagą    wīþiġ` [Germanic/docs/DEV_NOTES.md:26311-26322]. It then writes out the full sound-law chain: `*wīθ-agą → *wīþ-agą → *wīþ-egą → *wīþ-igą → wīþ-iġ`, i.e. no ja-stem rescue is needed once the suffix is corrected [Germanic/docs/DEV_NOTES.md:26324-26331].

The tail end of the fragment also matters because it keeps the vowel-length issue subordinate to the suffix issue. DEV_NOTES notes Hall’s unmacronized `wiþig`, but keeps long `ī` because Kluge supports it, the current TSV target already uses it, and `*wīθagą` derives it cleanly; if the row were forced to short `*i`, the output would be `weþiġ`, reopening a different vowel-quality problem [Germanic/docs/DEV_NOTES.md:26333-26344]. For present purposes, preserve that hierarchy: suffix etymology is settled; root-vowel length is a later audit question.

### DEV_NOTES fragment 5

- Source heading: `Mismatch Progress Log (2026-03-14)`
- Source line hint: `Germanic/docs/DEV_NOTES.md:10407-10410`
- Fragment type: `diagnostic_project_log`
- Status: `diagnostic`
- Issue tags: `mismatch_count`; `change_date`; `project_history`
- Recommended next use: `use_only_to_date_the_row_closure`
- Shared-with rows: `none`

This log line is not philological evidence, but it is useful project-history scaffolding. It records that on `2026-04-23` the mismatch count dropped to `35` and glosses the row-level action as “wīþiġ: PROTOFORM `*wīθijaz` → `*wīθagą` (§17.10.35, Campbell -ag- suffix)” [Germanic/docs/DEV_NOTES.md:10407-10410]. Use it only to date the moment when row 2296 left the active mismatch list; for substance, rely on §17.10.35 itself.

## Superseded or diagnostic material

- The entire 2026-03-19 withy section remains superseded as a **repair proposal**, even though parts of its source collection remain valuable as negative evidence. Its operational thesis was “Sievers-law syncope is overapplying to a ja-stem”; the live row and the later closure instead treat `*wīθijaz` as the wrong OE input altogether [Germanic/docs/DEV_NOTES.md:12482-12530; 26213-26310].
- `Germanic/docs/analysis/notable_findings.md` §9 preserves the same pre-closure state in compressed form: it says no authoritative proto-form was then known that could derive `wīþig` regularly, lists the ja-stem reconstructions, and labels the row a known exception awaiting better evidence [Germanic/docs/analysis/notable_findings.md:1312-1395]. That is now background-only, because §17.10.35 supplies a working protoform and the live row no longer behaves as an open exception.
- `Germanic/docs/analysis/fryhtu_investigation.md` uses withy only as a syncope diagnostic. The file notes “Before `*j`: `wīþiġ` preserves the vowel” and includes a test-battery line `wīθijăz | wīþeġ | wīþiġ | — (pre-existing mismatch)` [Germanic/docs/analysis/fryhtu_investigation.md:226-226,294-306]. That material is helpful for reconstructing why the row once kept surfacing in syncope work, but it is not current row authority.
- The plan at the end of §17.10.35 is partly superseded by the live TSV. DEV_NOTES proposed changing the `PROTO` column “likewise” to `*wīθagą`, whereas the current row keeps `PROTO = *wáiθiz` and only changes `PROTOFORM` [Germanic/docs/DEV_NOTES.md:26346-26355; Germanic/data/germanic-aligned-final.tsv:1420-1420]. For this slice, treat that as a settled distinction between comparative headword and OE modelling input, not as an unresolved bug.

## Open questions for later work

- If a later metadata audit wants stricter harmony between comparative and OE-specific fields, decide whether live `PROTO = *wáiθiz` should stay as the cognate-set label or be replaced by a more explicitly long-vowel comparative form. The current slice should not collapse `PROTO` into `PROTOFORM`, but the relation between them is still only partly explicit in row-local notes [Germanic/data/germanic-aligned-final.tsv:1420-1420; Germanic/docs/DEV_NOTES.md:26333-26344].
- If anyone tries to revive a ja-stem derivation for the OE noun, the burden of proof is now very high: they would need to answer the preserved Campbell/Adamczyk-style objection that a heavy monosyllabic `*-ijaz` should yield OE `-e` or zero rather than `-ig` [Germanic/docs/DEV_NOTES.md:12637-12647,12780-12803].
- If later report prose wants a stronger external etymological narrative for the whole lexeme family, the remaining unresolved point is not the OE suffix anymore but the comparative-family reconstruction around long `ī`, Kluge’s `*wīþja/ō`, and possible older `*wīþw-` background. That is a literature/etymology audit question, not a current row-state blocker [Germanic/docs/DEV_NOTES.md:12606-12617,26333-26344].
