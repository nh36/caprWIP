---
row_id: 2300
concept: wool
counterpart: wull
proto: *wúllō
protoform: *wúllō
derivation_class: unexplained_unmodelled
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file: Germanic/docs/lexeme_reports/packets/2300-wool-wull.md
linked_research_memo_file: Germanic/docs/lexeme_reports/research_memos/2300-wool-wull.md
linked_dossier_or_analysis_files:
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2300 wool / wull

## Current row state

- CONCEPT: `wool`
- COUNTERPART: `wull`
- PROTO: `*wúllō`
- PROTOFORM: `*wúllō`
- DERIVATION_CLASS: `unexplained_unmodelled`
- Live project stance: the regular derivation of `*wúllō` is `*wóllō > *wóllu > woll`, so the FST's `woll` output is being treated as the correct regular result rather than as a rule bug [@Stiles2012, §4.1.1.2; @RingeTaylor2014, §2.3.1].
- The row remains in the lexically exceptional bucket because attested OE keeps `u`; the row note and later DEV_NOTES audits both treat that mismatch as documented and non-derivable in the present FST.
- Philological caution for later reporting: handbook prose often cites the weak-feminine form `wulle`, while the row itself uses normalized `wull`; the real issue is the retained root vowel, not whether the citation form ends in `-e`.

## Development-note summary

The current note tradition for wool is unusually consistent on the rule side. NWGmc/pre-OE lowering of stressed `*u` before non-high vocalism in the next syllable is accepted as regular, and `*wúllō` falls squarely into that environment because long `ō` is one of the standard triggers for lowering [@Stiles2012, §4.1.1.2]. On the project's chronology, that gives `*wóllō`, then `*wóllu`, then `woll`; the modeled form is therefore exactly what the sound laws predict, not an artifact of a mistaken rule ordering [@RingeTaylor2014, §2.3.1].

The literature survey preserved in DEV_NOTES also makes clear why wool stays exceptional even though the cluster has obvious phonetic temptations. Bülbring explicitly names `wulle` among words where OE `u` appears instead of expected `o`, especially "namentlich zwischen Labial und langem oder gedecktem l", but he also concedes that "meist steht jedoch der Hauptregel gemäß o" and lists counterexamples such as `wolcen`, `folgian`, `bolt`, and `folc` [@Bulbring1902, §116, pp. 45--46]. That is already enough to block a categorical labial + `l` rule. Luick rejects Bülbring's phonological account and prefers analogical doublets; Ringe and Taylor still end up with the negative conclusion that "We do not really know why *u failed to lower in these forms" [@Luick1914, §78 Anm. 3; @RingeTaylor2014, §2.3.1, pp. 32--33]. Campbell and Brunner preserve the same basic picture: many OE forms keep `u` where regular development and OHG comparison point to `o`, but no additional sound law is licensed by the evidence [@Campbell1959, §§115--116; @SieversBrunner1965, §68].

What later project history adds is not a different diagnosis of wool, but a better explanation of why wool cannot be regularized by paradigm-cell retargeting. DEV_NOTES briefly explored that kind of rescue for neighboring `wulf`, `fugol`, `bucc`, and `rust`, but it left row 2300 untouched because wool is a feminine ō-stem whose available endings are all back- or low-vocalic: `-ō, -ai, -ǭ, -ōz, -ǭ, -ōmaz, -ōz, -ōmiz`. No inherited cell supplies following `*i/*ī/*j`, so there is no high-vowel environment that would block lowering without creating a different problem [@Stiles2012, §4.1.1.2]. Wool therefore functions as the control case in the cluster: its exception status survived both the failed attempt to rescue the other rows and the later correction that reclassified all five lexemes as documented exceptions.

A second late clarification is also current and should stay with the slice. When chronology work made `*wúllō → woll (expected wull)` more visible in the mismatch report, DEV_NOTES explicitly ruled out reading that as a new regression. The row was already in the `vowel_quality__u_lowering_exception` bucket; the row note already described `wull` as a lexical exception; and the older survey had already reached the project decision to accept the mismatch rather than weaken the lowering rule. For final-report work, that means wool should be presented as a long-recognized exception sharpened by later auditing, not as a row destabilized by recent model changes.

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-63-166

Source heading: NWGmc u-lowering Exceptions Near Labials  
Source line or section hint: lines 63-166  
Status: current  
Issue tags: u_lowering;known_exception;literature_survey;reconstruction_disagreement  
Recommended use: cite_in_final_report  
Shared with row IDs: 2030, 2162, 2298  
Text or paraphrase:
Bülbring's discussion already captures the wool problem in nearly final form. He lists `wulle` with `full` and `wulf` as words showing OE `u` instead of the expected lowered vowel, especially "namentlich zwischen Labial und langem oder gedecktem l", and he treats the agreement with Old Frisian and Old Saxon as evidence that the phenomenon is "sehr alt" [@Bulbring1902, §116, pp. 45--46]. Yet the same passage immediately warns that "meist steht jedoch der Hauptregel gemäß o" and adduces `wolcen`, `folgian`, `bolt`, and `folc`, so the labial environment is only a clustering tendency, not a rule. Bülbring even leaves the mechanism unresolved: "Ob wir darin Erhaltung des wg. u oder Wiederaufhebung der durch a-Umlaut herbeigeführten Veränderung erblicken müssen, läßt sich nicht mit Sicherheit entscheiden." Luick answers that uncertainty by rejecting the phonological proposal and preferring analogical doublets, but his own counterexample list confirms that no clean blocker can be added to the sound law [@Luick1914, §78 Anm. 3]. Ringe and Taylor accept genuine exceptions and conclude, in words DEV_NOTES preserves because they remain current, "We do not really know why *u failed to lower in these forms" [@RingeTaylor2014, §2.3.1, pp. 32--33]. The row therefore inherits a literature-backed exception diagnosis rather than an invitation to modify the lowering rule.

### DEV_NOTES:line-24574-24599

Source heading: chronology-regression audit around §17.10.24/25  
Source line or section hint: lines 24574-24599  
Status: current  
Issue tags: known_exception;project_history;mismatch_bucket  
Recommended use: cite_in_final_report  
Shared with row IDs: 2162  
Text or paraphrase:
When later chronology work made `*wúllō → woll (expected wull)` newly conspicuous, DEV_NOTES explicitly recorded that the row was "not actually" a regression of the chronology changes. Three pieces of project evidence are named together: the mismatch report already buckets wool under `vowel_quality__u_lowering_exception`; the TSV row already states that "FST outputs regular woll; attested wull is genuine lexical exception"; and the older u-lowering survey had already reached the decision to "Accept the mismatches. The FST correctly models the regular NWGmc u-lowering as a phonological rule. The u-preserving forms are genuine lexical exceptions for which no phonological conditioning has been established." That audit is important current context because it fixes the row's place in project history: later debugging exposed the exception more sharply, but it did not create the exception.

### DEV_NOTES:line-25955-26023

Source heading: cluster-wide rule-side audit for the u-lowering exception set  
Source line or section hint: lines 25955-26023  
Status: background  
Issue tags: u_lowering;source_audit;cross_lexeme_context  
Recommended use: keep_as_general_background  
Shared with row IDs: 1973, 2030, 2162, 2298  
Text or paraphrase:
The cluster-wide source audit preserves the rule-side evidence that makes `woll` the correct regular output for wool. Stiles distinguishes three environments for lowering and defines environment (b) as the case "before short a, long ō (and long ā ...)"; he also states that the special blocking environment is a following high vowel or a nasal-initial intervening cluster [@Stiles2012, §4.1.1.2]. `*wúllō` has neither a following high vowel nor a nasal cluster, so nothing in Stiles licenses retention of `u`. Campbell is quoted even more starkly: "There are, however, many exceptions in OE, which have preserved u," and he illustrates the regular/exceptional split with OE forms versus regular OHG `foll, fogal, boch, wolf, obana` [@Campbell1959, §115]. Brunner likewise notes the exception cluster and discusses preservation in inflected high-vowel cells, but those remarks serve better for the masculine comparison lexemes than for wool [@SieversBrunner1965, §§68, 239]. The source audit is therefore useful as cross-lexeme context for the sound law and the handbook consensus, while the wool-specific ō-stem discussion below supplies the decisive row-level restriction.

### DEV_NOTES:line-26069-26094

Source heading: wool-specific o-stem argument against paradigm-cell rescue  
Source line or section hint: lines 26069-26094  
Status: current  
Issue tags: paradigm_cell;stem_class;known_exception;protoform_vs_proto  
Recommended use: cite_in_final_report  
Shared with row IDs:  
Text or paraphrase:
The row-specific argument for wool is morphological rather than phonetic. OE `wull` is identified as a feminine ō-stem, and DEV_NOTES writes out the relevant paradigm vocalism in full: `-ō, -ai, -ǭ, -ōz, -ǭ, -ōmaz, -ōz, -ōmiz`. That inventory matters because it eliminates the usual project escape hatch. There is, in DEV_NOTES' own wording, "no cell with high *i/*ī/*j in the next syllable that we could use as a regular-sound-change escape hatch" [@Stiles2012, §4.1.1.2]. Every available inherited form either sits in the lowering environment or in a back-vowel environment that still does not produce the attested `u`. The note then sharpens the consequence with the right comparison point: Campbell §115 explicitly lists `full` as an exception and gives OHG `foll` as the regular cognate outcome, so the project's `woll` is exactly the sort of regular form that the handbooks lead one to expect [@Campbell1959, §115]. `wull` is therefore not an underexplored paradigm cell but a genuine non-derivable lexeme in the current FST.

### DEV_NOTES:line-26167-26185

Source heading: wool retained as the benchmark documented exception  
Source line or section hint: lines 26167-26185  
Status: current  
Issue tags: known_exception;project_history;paradigm_cell  
Recommended use: cite_in_final_report  
Shared with row IDs: 1973, 2030, 2162, 2298  
Text or paraphrase:
The later revision makes wool the benchmark for the whole cluster. After the attempted paradigm-cell rescue for four neighboring lexemes failed, DEV_NOTES rereads Campbell's exception list and concludes that "all five cases are genuine, non-derivable documented exceptions — same status as wull." The action note is equally important: the neighboring rows were reverted to their committed values, while row 2300 kept its existing exception treatment. Wool's status therefore did not weaken under later scrutiny; the rest of the exception set was brought into line with wool's already-established treatment as a mismatch that must be documented, not regularized away.

## Superseded or diagnostic material

The main superseded history near this lexeme is comparative rather than wool-specific. A late cluster note temporarily tried to rescue `wulf`, `fugol`, `bucc`, and `rust` by retargeting them to high-vowel paradigm cells, but row 2300 was already excluded from that move because the ō-stem paradigm offered no comparable cell. The later rollback then withdrew the rescue attempt and generalized wool's exception status to the whole cluster.

That means the slice should not imply a discarded wool-specific PROTOFORM proposal or an abandoned wool-specific sound law. The important project-history fact is narrower: wool was the lexeme that most clearly exposed the limits of the paradigm-cell workaround.

## Open questions for later work

- Decide whether the final report should mention both normalized `wull` and handbook `wulle`, so readers do not mistake the row's headword choice for a claim that only the bare form is philologically legitimate.
- If the final report cites Campbell's `full` comparison, keep the point precise: it is an exact morphological parallel for the exception pattern, not direct attestation evidence for wool.
- Keep any future paradigm discussion explicitly negative. For this ō-stem, the useful result is that no inherited high-vowel rescue cell exists.
