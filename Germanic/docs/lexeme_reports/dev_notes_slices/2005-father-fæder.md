---
row_id: 2005
concept: father
counterpart: fæder
proto: *fádēr
protoform: *fádēr
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
  - Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2005 father / fæder

## Current row state

- The live TSV row is `ID 2005`, `CONCEPT father`, `COUNTERPART fæder`, `PROTO *fádēr`, `PROTOFORM *fádēr`, `DERIVATION_CLASS regular`. `PROTO` and `PROTOFORM` are identical here, so the row is not currently using a separate repaired OE-targeting protoform [Germanic/data/germanic-aligned-final.tsv:290-290].
- The row is presently stable in the published compact trace. The debug snapshot gives `PROTO: *fádēr`, `EXPECTED: fæder`, `OUTPUTS: fæder`, with the visible derivational path `*fádēr > *fádǣr > *fædǣr > *fædær > *fæder > fæder` via Northwest Germanic long-`ē` lowering, Anglo-Frisian brightening, unstressed long-vowel shortening, and unstressed `æ > e` merger [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1158-1177].
- `coverage_audit.md` still marks the row as lacking harvested support material — `| 2005 | father | fæder | regular | no | - | - | - | none |` — and `report_manifest.tsv` still contains only the pilot report set, with no row-2005 entry [Germanic/docs/lexeme_reports/coverage_audit.md:234-234; Germanic/docs/lexeme_reports/report_manifest.tsv:1-13].
- `oe_known_problems.tsv` has no surviving entry for `*fádēr`, so row 2005 is not currently tracked as a live OE exception case in that file [Germanic/data/oe_known_problems.tsv:1-8].
- No row-specific packet, research memo, or dedicated dossier for `father / fæder` was found under `Germanic/docs/lexeme_reports/`. This replacement slice therefore has to preserve mainly shared DEV_NOTES material plus the one directly row-relevant regression note, and it should not pretend that a dedicated lexeme memo survives.

## Development-note summary

No clearly row-dedicated DEV_NOTES section for `father / fæder` survives. What does survive is still useful, but most of it is shared infrastructure rather than a bespoke lexeme dossier. The most directly row-relevant note is the 2026 unstressed-vowel chronology research that explicitly records a bad intermediate/output pair `*fádēr → fædær`; that note matters because it shows that the project once had the correct lexeme but the wrong final unstressed vowel, and that the intended repair was rule-ordering, not a change of target form [Germanic/docs/DEV_NOTES.md:20555-20559].

The next most important surviving material is classificatory. DEV_NOTES explicitly uses `PIE *pəter- → Gmc *faðer (OE fæder)` as a standard illustration of Verner’s Law, and elsewhere treats `fæder` as one of the canonical OE r-declension kinship terms alongside `mōdor`, `brōþor`, and `dohtor` [Germanic/docs/DEV_NOTES.md:6971-6984; Germanic/docs/DEV_NOTES.md:33106-33110,33404-33410]. Those passages are shared, but they help keep several distinctions clear: the row’s stored `PROTO`/`PROTOFORM` is the project’s Germanic-stage `*fádēr`; the inherited consonant history behind medial `ð/d` is older than that; and the OE counterpart `fæder` is being treated as an attested member of the kinship r-stem set, not as a speculative reconstructed placeholder.

There is also one later diagnostic mention from implementation work: when DEV_NOTES documents the `-Cl/-Cn/-Cm#` handling change for `þistles`, it says to “Spot-check no regressions on ... `-Cr#` (`wuldor, wundor, fæder`)” [Germanic/docs/DEV_NOTES.md:30124-30132]. That is not philological evidence in itself, but it does show that `fæder` was being used as a stable control item whose expected surface shape should not move while adjacent phonotactic work was done elsewhere.

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-6971-6984

- Source heading: `### Forschungsgeschichte: Comprehensive Literature Review` / `#### 1. Verner's Law: Discovery and Formulation`
- Source line or section hint: `lines 6971-6984`
- Fragment type: `shared_historical_phonology_anchor`
- Status: `current_but_shared`
- Issue tags: `Verner_law`; `PIE_to_Germanic`; `medial_ð`; `father_brother_contrast`
- Recommended next use: `cite when explaining why father belongs to the voiced-fricative/stop outcome class and why the OE medial consonant is not an ad hoc spelling accident`
- Shared with row IDs: `2005; 1954? brother-row equivalent; other Verner-law examples`

This is the clearest surviving DEV_NOTES passage that names `fæder` directly in a historical explanation rather than only in diagnostics. DEV_NOTES says that Karl Verner’s 1877 result explains “why PIE `*pəter-` → Gmc `*faðer` (OE `fæder`) but PIE `*bhrāter-` → Gmc `*brōþer` (OE `brōþor`)” [Germanic/docs/DEV_NOTES.md:6971-6975]. For row 2005, that matters because it preserves the older comparative background behind the medial consonant: the row’s stored project input is `*fádēr`, but DEV_NOTES still explicitly anchors the lexeme in the standard PIE→Germanic Verner-law pathway.

This fragment should be used conservatively. It is not a row-2005 packet, and it does not itself adjudicate every detail of the project’s accent-marked `PROTOFORM` notation. Still, it is the best surviving direct statement that `father / fæder` is not being handled as a one-off OE irregularity; rather, it belongs to a textbook inherited contrast where the Germanic reflex shows voiced medial frication because “the accent in Indo-European was not on the immediately preceding syllable” [Germanic/docs/DEV_NOTES.md:6980-6983].

### DEV_NOTES:line-20555-20559

- Source heading: `§15.8 Two-Stage *ō Shortening: Early vs Late (Research)` / `#### Regressions Identified (56 vs 43 mismatches)`
- Source line or section hint: `lines 20555-20559`
- Fragment type: `explicit_row_regression_note`
- Status: `diagnostic_but_still_material`
- Issue tags: `fædær_regression`; `unstressed_vowel_chronology`; `late_vs_early_shortening`; `AE_merger`
- Recommended next use: `primary preserved note for explaining the specific bad output once seen for row 2005`
- Shared with row IDs: `1999; 2005; 2014?; other rows listed in the same regression cluster`

This is the only surviving DEV_NOTES fragment that appears to touch row 2005’s exact output state directly. In the regression list, DEV_NOTES records a `-æ` vs `-e` problem and explicitly includes ``*fádēr → fædær`` [Germanic/docs/DEV_NOTES.md:20555-20559]. That is important because it distinguishes the live target from the superseded bad form very plainly: the row was not being reconsidered as some alternate OE lexeme; the system was briefly producing the wrong unstressed ending.

The surrounding §15.8 note is about chronology of unstressed-vowel shortening and the timing of `æ > e` reduction. Even though `fæder` is only named in the regression list itself, the point of preserving this fragment is that it ties row 2005 to a concrete implementation-era failure mode. The current published trace now lands on `fæder` again, but the slice should keep the bad output visible so later work does not mistake `fædær` for a live rival target or for philological evidence [Germanic/docs/DEV_NOTES.md:20555-20559; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1158-1177].

### DEV_NOTES:line-33106-33110 and line-33407-33410

- Source heading: `§17.21.2.1 The basic shape: consonant-stem r-declension` / `§17.21.4.4 Hogg 1992 Phonology: no specific discussion`
- Source line or section hint: `lines 33106-33110; 33407-33410`
- Fragment type: `shared_morphological_classification_note`
- Status: `current_but_indirect`
- Issue tags: `r_declension`; `kinship_terms`; `morphological_class`; `citation_form_fæder`
- Recommended next use: `use to justify treating fæder as part of the canonical OE kinship r-stem set when later packets discuss paradigm behaviour`
- Shared with row IDs: `2005; mother; brother; daughter; sister`

Although this material occurs inside the long `sister` dossier, it preserves a useful classification statement for `father`. DEV_NOTES describes the OE reflexes of the kinship terms as the “r-stem minor declension,” giving `*fæder, *mōdor, *brōþor, *dohtor` as the comparison set [Germanic/docs/DEV_NOTES.md:33106-33110]. Later in the same dossier it quotes Hogg’s summary that “the kinship terms fæder 'father', modor 'mother', brodor 'brother', dohtor 'daughter', sweostor 'sister' constituted the r-declension” [Germanic/docs/DEV_NOTES.md:33404-33410].

For row 2005 this is shared rather than row-local evidence, but it is still worth preserving because no dedicated `father` memo survives. The fragment does not by itself solve any output mismatch, nor does it give paradigm-cell citations for `fæder`; what it does do is record the project’s morphological framing of the lexeme. That is a real working-note function: if a later packet asks whether `fæder` should be treated as an ordinary noun with a mechanically predictable weak ending history, this shared note says no — it sits in the special inherited kinship r-declension class.

### DEV_NOTES:line-30124-30132

- Source heading: `§17.18.7.2 Implementation steps`
- Source line or section hint: `lines 30124-30132`
- Fragment type: `shared_control_row_diagnostic`
- Status: `diagnostic_only`
- Issue tags: `control_lexeme`; `regression_check`; `Cr_cluster`; `stable_output`
- Recommended next use: `use only as evidence that fæder served as a no-regression control during neighboring phonotactic work`
- Shared with row IDs: `2005; wuldor; wundor`

This is not linguistic argumentation, but it is still useful project memory. When DEV_NOTES records how the `þistles` decision should be verified, it instructs the reader to “Spot-check no regressions on `-gl#` (`fugol, seġel`) or `-Cr#` (`wuldor, wundor, fæder`)” [Germanic/docs/DEV_NOTES.md:30124-30132]. In practice that means `fæder` was being treated as a stable comparator whose derivation should remain unchanged while unrelated final-cluster logic was adjusted elsewhere.

Because this is only a diagnostic control note, it should not be promoted into lexical proof. It does, however, support a modest inference about row state at that moment in the project: `fæder` was expected to continue matching cleanly, and any movement away from that outcome would have counted as collateral damage rather than as a desired revision [Germanic/docs/DEV_NOTES.md:30124-30132].

## Superseded or diagnostic material

- The most explicit superseded row-local bad state is `*fádēr → fædær`. DEV_NOTES preserves it only as a regression in the `-æ` vs `-e` bucket, not as an alternate target that should remain live [Germanic/docs/DEV_NOTES.md:20555-20559].
- The current compact trace already shows the corrected path ending in `fæder`, so any future reuse of the regression note should keep the chronology clear: `fædær` is diagnostic history, while `fæder` is the live published output [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1158-1177].
- The Verner-law note is historically important but still shared background, not a row-2005 implementation memo. It explains inherited consonant history; it does not by itself document every stage of the project’s accent-marked `*fádēr` notation or every OE paradigm form [Germanic/docs/DEV_NOTES.md:6971-6984].
- The r-declension material is likewise shared and classificatory. It is useful because no dedicated `father` dossier survives, but it should not be overstated into a row-specific attestation packet [Germanic/docs/DEV_NOTES.md:33106-33110,33404-33410].
- The `-Cr#` spot-check note is purely diagnostic. It shows `fæder` functioning as a stable control lexeme during unrelated implementation work, not as a fresh philological argument [Germanic/docs/DEV_NOTES.md:30124-30132].

## Open questions for later work

- No surviving row-specific memo here quotes a dictionary or edition directly for OE `fæder`. If a later literature pass is commissioned, the first task should be simple attestation support and paradigm confirmation rather than more rule-order debugging.
- DEV_NOTES preserves PIE→Germanic `*faðer` in the Verner-law discussion, while the live row stores `*fádēr` as both `PROTO` and `PROTOFORM`. A later packet should explain that notation bridge explicitly so the row’s comparative background and the project’s working proto layer are not conflated [Germanic/docs/DEV_NOTES.md:6971-6984; Germanic/data/germanic-aligned-final.tsv:290-290].
- The current trace reaches `fæder` through unstressed long-vowel shortening plus `æ > e` merger, and the regression note shows that that chronology once slipped. If row 2005 ever regresses again, the first check should be whether the bad state is another `fædær`-type ending problem rather than a deeper disagreement about the lexeme itself [Germanic/docs/DEV_NOTES.md:20555-20559; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1171-1177].
