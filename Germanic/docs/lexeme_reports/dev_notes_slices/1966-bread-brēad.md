---
row_id: 1966
concept: bread
counterpart: brēad
proto: *bráudą
protoform: *bráudą
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files: []
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 1966 bread / brēad

## Current row state

- The live OE row is `1966 bread / brēad`, with `PROTO = *bráudą`, `PROTOFORM = *bráudą`, and `DERIVATION_CLASS = regular` [Germanic/data/germanic-aligned-final.tsv:135-135].
- The published derivation snapshot already returns the live target without repair. It spells the pathway out as `OE Au Fronting: *bráeudą`, `OE Diphthong Leveling: *brēadą`, and `OE Heavy Syllable Nasal Apocope: *brēad`, with final outcome `brēad` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:510-529].
- Existing row infrastructure is still empty: the coverage audit records row `1966 | bread | brēad | regular | no | - | - | - | none`, i.e. no packet, no memo, no attached analysis file, and no pre-existing DEV_NOTES fragment assignment [Germanic/docs/lexeme_reports/coverage_audit.md:209-209].

## Development-note summary

Current DEV_NOTES support for `bread / brēad` is **thin but real**. There is no preserved lexeme-specific bread note in the live infrastructure, and the coverage audit still marks the row as having `none` for attached report material [Germanic/docs/lexeme_reports/coverage_audit.md:209-209]. What does exist is shared phonological discussion that directly bears on the row's regularity.

The earliest directly relevant DEV_NOTES material is implementation history. In the January long-vowel-missing review, DEV_NOTES identified one of the main OE problems as “**PGmc *au not lengthened**” and proposed the concrete repair “change `*aeu -> *ēa`” [Germanic/docs/DEV_NOTES.md:1760-1765]. That note is not about `brēad` by name, but it is exactly the kind of issue that would have blocked a regular derivation from `*bráudą` to an OE `ēa` outcome. In other words, the project once treated PGmc `*au` > OE long diphthong as an implementation gap, not as a lexical problem specific to bread.

Later DEV_NOTES material gives the current shared rule in explicit phonological terms. In the `rēc` dossier, DEV_NOTES states: “**PGmc diphthong *au undergoes fronting and lengthening in all OE dialects**,” gives the sequence `*au → *aeu → ēa`, and illustrates it with forms such as `*haub-udą → OE hēafod`, `*raup-az → OE rēad`, and `*laub-az → OE lēaf` [Germanic/docs/DEV_NOTES.md:34305-34318]. That shared rule is the main current DEV_NOTES authority for row 1966. Applied to `*bráudą`, it predicts the exact pre-apocope stage seen in the published trace, namely `*brēadą` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:523-529].

One additional shared DEV_NOTES caution matters for the row's surface shape. While discussing another lexeme, DEV_NOTES asks whether `ēa` might later smooth to `ē`, but then warns that such smoothing should not simply be assumed: “**smoothing of ēa → ē before -c is NOT universally attested in WS**,” and the note immediately points to `dēad` and `rēad` as counterexamples showing preserved `ēa` [Germanic/docs/DEV_NOTES.md:35583-35587]. For `brēad`, this is useful negative evidence. The row ends in a dental and already surfaces with `ēa`; current DEV_NOTES therefore supports leaving `brēad` as an ordinary preserved-`ēa` outcome, not inventing any further monophthongizing repair.

So the replacement note should stay conservative. DEV_NOTES does support the live row, but only through **shared sound-change discussion** and **old implementation history**, not through a dedicated bread dossier, not through an attestation audit, and not through any row-local controversy over protoform or target choice [Germanic/docs/DEV_NOTES.md:1760-1765,34305-34318,35583-35587; Germanic/docs/lexeme_reports/coverage_audit.md:209-209].

## Relevant DEV_NOTES fragments

### [Germanic/docs/DEV_NOTES.md:1760-1765]

- Source heading: long-vowel-missing deep dive / actionable sources
- Fragment type: `superseded_or_diagnostic_for_lexeme`
- Status: `superseded`
- Issue tags: `pgmc_au_to_oe_ea`; `long_diphthong`; `implementation_history`
- Recommended next use: `use_to_explain_early_rule_gap`
- Shared with row IDs:

This is the clearest early implementation fragment directly relevant to `brēad`. DEV_NOTES says one of the “Biggest actionable sources” was “**PGmc *au not lengthened**” and recommends “**change `*aeu -> *ēa`**” [Germanic/docs/DEV_NOTES.md:1763-1765]. The fragment is superseded because the published trace now reaches `brēad` cleanly, but it preserves important project history: OE `*au` rows were once being handled as a systemic long-diphthong problem rather than as isolated lexeme exceptions.

### [Germanic/docs/DEV_NOTES.md:34305-34318]

- Source heading: `§17.22.3  Vowel discrepancy: īe (WS) vs. ē (Anglian) as i-umlaut of *au`
- Fragment type: `copied_shared_lexeme_fragment`
- Status: `current`
- Issue tags: `shared_sound_change`; `pgmc_au_to_oe_ea`; `regular_reflex`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This is the main current DEV_NOTES authority for the row. DEV_NOTES states that “**PGmc diphthong *au undergoes fronting and lengthening in all OE dialects**” and gives the pathway `*au → *aeu → ēa`, with comparator examples `*haub-udą → OE hēafod`, `*raup-az → OE rēad`, and `*laub-az → OE lēaf` [Germanic/docs/DEV_NOTES.md:34309-34318]. For row 1966, that shared discussion is enough to justify the vowel history of `*bráudą > *brēadą > brēad` as regular. It also aligns exactly with the published derivation trace's `OE Au Fronting` plus `OE Diphthong Leveling` sequence [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:523-529].

### [Germanic/docs/DEV_NOTES.md:35583-35587]

- Source heading: follow-up question on smoothing in the `rēc` analysis
- Fragment type: `copied_shared_lexeme_fragment`
- Status: `current`
- Issue tags: `no_assumed_smoothing`; `preserved_ea`; `shared_negative_evidence`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This fragment matters because it tells later note-writers what **not** to do with forms like `brēad`. DEV_NOTES asks whether `rēac` could smooth to `rēc`, but then immediately cautions that “**smoothing of ēa → ē before -c is NOT universally attested in WS**” and adds that forms such as `**dēad**` and `**rēad**` show `ēa` preserved [Germanic/docs/DEV_NOTES.md:35583-35585]. For row 1966, the transferable point is that preserved `ēa` before a dental is entirely compatible with current project reasoning; there is no basis in DEV_NOTES for treating `brēad` as an over-diphthongized form needing later reduction.

## Superseded or diagnostic material

- The January “long-vowel-missing” note is diagnostic history only. It shows that PGmc `*au` > OE `ēa` once needed implementation repair, but that issue is no longer live for row 1966 now that the published trace already returns `brēad` [Germanic/docs/DEV_NOTES.md:1760-1765; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:510-529].
- The infrastructure absence is itself diagnostic. Coverage audit still lists row 1966 as `none`, so later reporting should not imply that a row-local bread dossier, memo, or packet already exists when it does not [Germanic/docs/lexeme_reports/coverage_audit.md:209-209].
- A likely search false positive is Campbell's quotation listing `brǣdu breadth` among abstract nouns in `-u` [Germanic/docs/DEV_NOTES.md:40720-40730]. That passage is about the inflectional history of abstract nouns such as `brǣdu`, not about the lexeme `bread / brēad`, and it should not be recycled as row-1966 evidence.

## Open questions for later work

- If row 1966 is ever considered for `index.tsv`, decide whether shared-rule-only support is enough. On present evidence, the slice looks more like a **useful no-index replacement note** than an index-worthy lexeme dossier, because the DEV_NOTES support is real but not bread-specific [Germanic/docs/lexeme_reports/coverage_audit.md:209-209; Germanic/docs/DEV_NOTES.md:34305-34318].
- If later literature work wants a fuller report, add a proper OE attestation/source audit for `brēad`. The current slice rests on the live TSV row, the published derivation trace, and shared DEV_NOTES phonology, not on a preserved bread-specific bibliography [Germanic/data/germanic-aligned-final.tsv:135-135; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:510-529].
- If DEV_NOTES eventually gets a consolidated shared note on PGmc `*au > OE ēa`, row 1966 would be a natural straightforward example to attach there alongside comparator forms like `hēafod`, `rēad`, and `lēaf` [Germanic/docs/DEV_NOTES.md:34309-34318].
