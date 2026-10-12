---
row_id: 2162
concept: rust
counterpart: rust
proto: *rústō
protoform: *rústō
derivation_class: unexplained_unmodelled
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file: Germanic/docs/lexeme_reports/packets/2162-rust-rust.md
linked_research_memo_file: Germanic/docs/lexeme_reports/research_memos/2162-rust-rust.md
linked_dossier_or_analysis_files:
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2162 rust / rust

## Current row state

- CONCEPT: `rust`
- COUNTERPART: `rust`
- PROTO: `*rústō`
- PROTOFORM: `*rústō`
- DERIVATION_CLASS: `unexplained_unmodelled`
- Live row note: regular citation-form development gives `**rost`; the row is kept as a documented OE `u`-retention exception, and the note explicitly rejects a clean high-vowel escape cell because the obvious `i`-triggered comparators would give `**ryst`, not citation-form `rust`.

## Development-note summary

The live TSV already encodes the central conclusion, and DEV_NOTES mostly reinforces it rather than replacing it. `rust` belongs to the same exception dossier as `full`, `wulf`, `fugol`, `bucc`, `wull`, and `lufu`: regular NWGmc/OE lowering turns stressed `*u` into `o` before a non-high vowel in the next syllable, so citation-form `*rústō` should surface as `rost`, not `rust` [@RingeTaylor2014, §2.3.1; @Campbell1959, §115]. The February exception survey keeps the old handbook discussion on record but ends by refusing to force a rule. Bülbring's classic description is quoted with its cautious wording that OE `u` appears "namentlich zwischen Labial und langem oder gedecktem l" but that "meist steht jedoch der Hauptregel gemäß o"; Luick is then used to show why a labial-environment blocker fails as a general explanation; and Ringe-Taylor's verdict is preserved without softening: "We do not really know why *u failed to lower in these forms" [@Bulbring1902, §116; @Luick1914, §78 Anm. 3; @RingeTaylor2014, pp. 32--33]. For row 2162, that is the current project position.

Later DEV_NOTES material matters because it records two different attempts to stop the row from looking like a simple phonological failure. One late audit says explicitly that `rust` was misread as a chronology regression: the mismatch report and the row note already classified it as a `u`-lowering exception, so the chronology pass had not broken anything. A different later cluster tried to regularize the row by separating the cognate-set headword from a cell-specific input and by correcting the noun class from feminine `*rústō` to masculine `*rústaz`; that move relied on Bosworth-Toller's masculine entry `m. (-es; pl. -as) RUST` and proposed the gen.sg. target `*rústis → rustes` [@BosworthToller1898, s.v. "rust"]. That proposal is not current row policy. The live TSV did not adopt `*rústaz/*rústis`, and the present row note does not treat `rustes` as a rescue path.

A third strand has to be kept separate from both of those. For part of the project, the FST was producing `orst`, not `rost`, because `OERMetathesis` was wrongly firing on word-initial `rVst`. DEV_NOTES preserves Campbell's statement that metathesis applies when `*sk, *sp, *st` are preceded by a short vowel and followed by `r` in the same syllable, i.e. the classic word-medial `CrVst > CVrst` cases, not word-initial `rust` [@Campbell1959, §459(1)]. That bug history matters when older packet material mentions `orst`, but it is diagnostic only. Once the metathesis bug was fixed, row 2162 returned to the real problem: regular `rost` versus attested `rust`.

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-63-166

Source heading: NWGmc u-lowering Exceptions Near Labials  
Source line or section hint: lines 63-166  
Status: current  
Issue tags: u_lowering;known_exception;reconstruction_disagreement  
Recommended use: cite_in_final_report  
Shared with row IDs: 2030, 2298, 2300  
Text or paraphrase:
The shared survey begins from the regular law, not from the exception: stressed `*u` lowers to `*o` before a following non-high vowel, so `*rustō` belongs with the forms for which the FST's regular output is expected [@RingeTaylor2014, §2.3.1]. The lexeme is then named directly in the exception list as `*rustō → rust (not ×rost)`. Bülbring's older description is copied with both its attraction and its weakness intact: OE `u` appears "namentlich zwischen Labial und langem oder gedecktem l", but "meist steht jedoch der Hauptregel gemäß o", and he finally says that it cannot be determined with certainty whether these forms preserve WGmc `u` or undo an earlier lowering [@Bulbring1902, §116]. Luick's response is also preserved in substance: the same labial and velar surroundings often show ordinary lowering (`folc, folġian, bolt, bolster, molde, molcen, smolt`), so no categorical blocker can be extracted from the pattern [@Luick1914, §78 Anm. 3]. The fragment ends with the project decision that controls row 2162 now: "Accept the mismatches. The FST correctly models the regular NWGmc u-lowering as a phonological rule. The u-preserving forms are genuine lexical exceptions for which no phonological conditioning has been established" [@Campbell1959, §115; @RingeTaylor2014, pp. 32--33; @SieversBrunner1965, §68].

### DEV_NOTES:line-24574-24599

Source heading: chronology-regression audit around §17.10.24/25  
Source line or section hint: lines 24574-24599  
Status: current  
Issue tags: known_exception;source_conflict  
Recommended use: cite_in_final_report  
Shared with row IDs: 2300  
Text or paraphrase:
This audit exists to stop `rust` from being misclassified as a new chronology bug. The note says that `*rústō → orst (expected rust)` and `*wúllō → woll (expected wull)` were reported as regressions after §17.10.24/25, but "are not actually regressions of our chronology work." The three checks it lists are all classificatory rather than speculative: the mismatch report already files `rust/rost` under `vowel_quality__u_lowering_exception`; row 2162 already carries the note "OE rust retains u; cf. R/T §2.3.1 for general u-lowering exceptions"; and the February survey had already decided to "Accept the mismatches" because no phonological conditioning had been established for these forms [@RingeTaylor2014, §2.3.1]. The practical consequence is that later chronology work is not the reason row 2162 remains mismatched. `rust` belongs in the documented-exception bucket.

### DEV_NOTES:line-25940-26067

Source heading: attempted paradigm-cell and stem-class rescue for rust  
Source line or section hint: lines 25940-26067  
Status: superseded  
Issue tags: paradigm_cell;protoform_vs_proto;stem_class;source_conflict  
Recommended use: use_to_explain_superseded_analysis  
Shared with row IDs: 2030, 2298  
Text or paraphrase:
This cluster is the most substantial superseded attempt to regularize `rust`, and it contains both useful source work and an abandoned row policy. The source audit restates the current consensus first. Stiles's environment table allows blocking only when the consonantism after `*u` begins with a nasal, so `-st-` gives no exemption for `rust` [@Stiles2012, §4.1.1.2]. Campbell §115 is quoted directly: "There are, however, many exceptions in OE, which have preserved u, very often where other West Gmc. languages, especially OHG, have o," followed by examples such as `full, fugol, bucca, wulf, ufan` and the corresponding regular OHG forms [@Campbell1959, §115]. Brunner is then quoted on the oblique high-vowel cells, "Instr. der mask. und neutr. o-Stämme wulfe aus wulfi ...", which the note uses as the model for a genitive-based rescue [@SieversBrunner1965, §§68, 239]. On that basis the project briefly proposed to correct row 2162 from feminine `*rústō` to masculine `*rústaz`, citing Bosworth-Toller `m. (-es; pl. -as) RUST`, and to retarget the OE row to gen.sg. `*rústis → rustes` as a regular outcome [@BosworthToller1898, s.v. "rust"]. That move is now superseded. The live TSV did not adopt the `*rústaz/*rústis` split, and the current row note no longer treats a high-vowel paradigm cell as an acceptable citation-form solution. This fragment should therefore be cited, if at all, as project history plus a warning that the row's inherited stem class may still be philologically unstable.

### DEV_NOTES:line-39972-40033

Source heading: diagnostic metathesis bug that produced orst  
Source line or section hint: lines 39972-40033  
Status: diagnostic_only  
Issue tags: metathesis;transducer_limitation;old_target_superseded  
Recommended use: use_as_project_history_only  
Shared with row IDs:  
Text or paraphrase:
This note isolates an implementation bug that once hid the real `rust` problem behind the wrong surface form `orst`. DEV_NOTES traces the bad derivation as `*rústō` → `*róstō` after regular `u`-lowering, then `*órst` after an overbroad metathesis rule, and finally orthographic `orst`. The quoted rule environment is Campbell's: "When [the cluster] *sk*, *sp* or *st* preceded by a short vowel followed *r* in the same syllable, the *r* and the short vowel were transposed" [@Campbell1959, §459(1)]. DEV_NOTES then makes the decisive point explicit: the rule examples `berstan` and `forst` all have a consonant before the metathesizing `r`, whereas word-initial `rust` does not. The fragment is therefore diagnostic only. Once `OERMetathesis` was restricted to word-medial `CrVst`, row 2162 stopped being an `orst` bug and went back to being what the live TSV says it is: a documented `u`-retention exception whose regular citation-form comparator is `rost`.

## Superseded or diagnostic material

Two older stories must stay separate in any later report. The `orst` episode is pure implementation history and should only be used to explain why older traces or packets may show the wrong surface form. The abandoned `*rústis → rustes` proposal is more serious philological history: it records a real attempt to separate cognate-set headword from row-specific protoform and a real source-based objection to feminine `*rústō`, but it is still superseded as row policy because the project chose to keep `rust` in the documented-exception bucket instead of rewriting the row around the genitive.

## Open questions for later work

- compare the live row note against the packet and research memo before quoting the stem-class issue in a final report;
- if the late rescue note is cited, separate the still-useful Bosworth-Toller masculine evidence from the abandoned `*rústis → rustes` retargeting;
- cite the metathesis bug note only as bug history, not as the current explanation of the mismatch;
- decide whether a final lexeme report should foreground the exception consensus or the unresolved `*rústō` versus `*rústaz` philology first.
