---
row_id: 2264
concept: tread
counterpart: tredan
proto: *trédaną
protoform: *trédaną
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
current_status: current
needs_literature_agent: no
filename_basis: canonical_row_based_filename
---

# DEV_NOTES material — 2264 tread / tredan

## Current row state

- The live OE row reads `CONCEPT = tread`, `COUNTERPART = tredan`, `PROTO = *trédaną`, `PROTOFORM = *trédaną`, `DERIVATION_CLASS = regular`, with duplicated provenance text in `NOTE`: `Source: Wiktionary etymology (template:inh) | Source: Wiktionary etymology (template:inh)` [Germanic/data/germanic-aligned-final.tsv:1296-1296].
- `PROTO` and `PROTOFORM` are currently identical in the live TSV. That means the project is feeding the OE derivation from `*trédaną` as its active proto input; `COUNTERPART = tredan` is a separate OE output layer, not an alternate proto citation form and not a dictionary headword spelling [Germanic/data/germanic-aligned-final.tsv:1296-1296].
- Coverage tracking still records no attached row-local support material: `| 2264 | tread | tredan | regular | no | - | - | - | none |` [Germanic/docs/lexeme_reports/coverage_audit.md:399-399]. No packet, research memo, or pilot file is currently linked for reuse.
- `oe_known_problems.tsv` has no row-local entry for `2264`, `tredan`, or `*trédaną`; the current exception ledger is therefore not treating this lexeme as an active OE problem case [Germanic/data/oe_known_problems.tsv:1-8].
- The published derivation traces are exact matches. The compact report gives `PROTO: *trédaną`, `EXPECTED: tredan`, `OUTPUTS: tredan`, and the OE-side path consists only of `OE Heavy Syllable Nasal Apocope`, `OE Secondary Nasalization`, `OE Weak Tail Reduction`, and final star removal [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:5459-5478]. The full trace confirms that every earlier Germanic and Northwest Germanic stage is `[no-change]`, then runs `*trédaną -> *trédan -> *trédąn -> *trédan -> tredan` [Germanic/docs/debug_snapshots/oe_full_trace_report.txt:37124-37237].
- Repo-local reference works support the lexical identification while also showing that the row's notation layers should not be collapsed. Bright gives the principal parts `tredan, tread; træd, trædon; treden` [docs/references/bright_anglo_saxon_reader.vision.txt:2904-2907; @BrightCassidyRingler1971]. Clark Hall glosses `tredan³ (eo)` as `to ‘tread,' step on` [docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:41384-41384; @ClarkHall1960]. Kroonen places OE `tredan` under an alternation `*trudan-` / `*tredan-` and remarks that “The alternation *tredan- *trudan- points to an original root aorist” [docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:26624-26639; @Kroonen2013, p. 521]. Orel cites `*trudanan str.vb.` with Gothic `trudan` and Old Norse `troða` [docs/references/orel_handbook_germanic_etymology.vision.txt:45391-45399; @Orel2003, p. 410]. Fulk likewise treats Gothic `trudan` as an aorist-present comparandum and warns that WGmc forms such as `OE tredan, OHG tretan` are innovative within the paradigm [docs/references/fulk_comparative_grammar_early_germanic.vision.txt:16521-16524,16562-16565; @Fulk2018, §12.18].
- There is also a small but relevant piece of project-internal normalization history: `germanic_nan_normalization.csv` still records the broader cognate-set normalization `*tredanan,*tredaną,...,tread,...,*tredanan,3` [Germanic/docs/germanic_nan_normalization.csv:85-85]. That file documents an older cross-Germanic `-anan > -aną` normalization layer without accent marks; it is useful diagnostically, but it is not itself a reason to rewrite the live OE row away from `*trédaną` / `tredan`.

## Detailed development-note summary

The surviving `DEV_NOTES.md` material for row `2264` is real but thin, and it is not a full lexeme dossier. The only directly attachable row-relevant note is a shared verification block about strong verbs with medial `*d`, written to distinguish true Verner alternation cases from verbs whose `*d` belongs to the inherited paradigm. In that block the project quotes Ringe & Taylor: `"PGmc *trudaŋ 'to step on' (Goth. trudan, ON troða) > PWGmc *tredan"`, followed by the explicit conclusion: `The *d is original, not from Verner levelling` [Germanic/docs/DEV_NOTES.md:7357-7360; docs/references/ringe_taylor_linguistic_history_vol2.txt:18639-18640; @RingeTaylor2014, pp. 78, 325]. That is the strongest surviving DEV_NOTES point for this row, and it should be preserved verbatim because it protects later work from misclassifying `tredan` as a `findan`-type voiced-alternant rescue.

That conclusion matters because the row's three main labels point to three different descriptive layers. `PROTO` is the project's active proto input; `PROTOFORM` is the project field for any distinct rescued or citation protoform, but here it is identical to `PROTO`; and `COUNTERPART` is the Old English outcome the row is trying to derive [Germanic/data/germanic-aligned-final.tsv:1296-1296]. Comparative sources do not all cite the lexeme in the same shape. Ringe & Taylor's developmental narrative moves from `PGmc *trudaŋ` to `PWGmc *tredan` and then to OE `tredan` [docs/references/ringe_taylor_linguistic_history_vol2.txt:18639-18640; @RingeTaylor2014, p. 325]. Orel keeps the infinitive-like citation form `*trudanan` [docs/references/orel_handbook_germanic_etymology.vision.txt:45391-45399; @Orel2003, p. 410]. Kroonen organizes the entry under the alternation `*trudan-` / `*tredan-` [docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:26624-26639; @Kroonen2013, p. 521]. None of those citation-format differences, by themselves, requires a distinct live `PROTOFORM` field or a change to the OE `COUNTERPART`.

The live trace supports that conservative reading. There is no hidden consonant alternation fix, no special vowel rescue, and no West-Saxon-only diphthongization step required to reach the current target. Every pre-OE stage is stable in the full trace, and the only active OE operations are the project's standard heavy-syllable `*-ą` loss, secondary/contact nasalization notation, and weak-tail reduction before orthographic cleanup [Germanic/docs/debug_snapshots/oe_full_trace_report.txt:37131-37237]. In other words, the current row is not merely plausible in the abstract; it is already an exact live derivation. That is important because the DEV_NOTES prose is thinner than the trace evidence here.

The lexical support also needs to stay explicit about normalization versus source spelling. Bright's paradigm `tredan ... træd ... trædon ... treden` confirms that the row target is the infinitive of a strong verb, not a participle or a back-formed stem [docs/references/bright_anglo_saxon_reader.vision.txt:2904-2907; @BrightCassidyRingler1971]. Clark Hall's `tredan³ (eo)` shows manuscript or editorial variation without displacing the normalized row spelling `tredan` [docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:41384-41384; @ClarkHall1960]. Fulk's caution is also useful here: if `OE tredan, OHG tretan` are WGmc innovations relative to Gothic `trudan`, then the row's project input `*trédaną` should be read as the model's aligned proto-stage for the OE derivation, not as a claim that every dictionary must cite the verb in that exact form [docs/references/fulk_comparative_grammar_early_germanic.vision.txt:16562-16565; @Fulk2018, §12.18].

The best conservative summary, then, is narrow. Row `2264` is currently regular and exact; the live project distinguishes `PROTO = PROTOFORM = *trédaną` from `COUNTERPART = tredan`; and the only strong DEV_NOTES anchor is a shared comparative note saying that the row's `*d` is not a Verner-law repair [Germanic/data/germanic-aligned-final.tsv:1296-1296; Germanic/docs/DEV_NOTES.md:7341-7375; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:5459-5478]. That is enough to support a working-note slice, but not enough to pretend that a row-specific historical memorandum survives.

## Relevant DEV_NOTES fragments with line-based refs

### DEV_NOTES:line-7341-7375

- Source heading: `Verification: Other Class III Verbs with *d Are NOT Verner Cases`
- Source line or section hint: `lines 7341-7375`
- Fragment type: `shared_comparative_verification_fragment`
- Status: `row_relevant_but_not_row_exhaustive`
- Issue tags: `verner_law`; `original_d`; `class_iv_or_aorist_present_history`; `comparative_reconstruction`
- Recommended next use: `retain_as_primary_dev_notes_anchor`

This is the clearest surviving DEV_NOTES anchor for `tredan`. The fragment was written to answer whether several strong verbs with `*d` should be handled like Verner alternation cases, and it answers no. For this row it preserves the exact quotation `"PGmc *trudaŋ 'to step on' (Goth. trudan, ON troða) > PWGmc *tredan"` and then adds the interpretive sentence `The *d is original, not from Verner levelling` [Germanic/docs/DEV_NOTES.md:7357-7360]. The immediately following contrast with `*finþaną` matters just as much: DEV_NOTES treats `findan` as a genuine case of a voiced alternant being levelled, but does **not** put `tredan` in that bucket [Germanic/docs/DEV_NOTES.md:7368-7375]. For later row work, the safe takeaway is not a full etymology but a boundary condition: do not build a `Verner-repair` narrative around the OE `d` here.

The reference support behind the DEV_NOTES quote is strong enough to keep. Ringe & Taylor separately state that `PGmc *trudang ‘to step on’ ... > PWGmc *tredan ... > OE tredan`, and elsewhere note that zero-grade `*trudang` is reflected in PWGmc `*tredan` [docs/references/ringe_taylor_linguistic_history_vol2.txt:18639-18640,5031-5033; @RingeTaylor2014, pp. 78, 325]. Kroonen's `*trudan-` / `*tredan-` alternation and Fulk's discussion of Gothic `trudan` versus WGmc `tredan/tretan` are consistent with that comparative picture even though they frame it differently [docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:26624-26639; docs/references/fulk_comparative_grammar_early_germanic.vision.txt:16521-16524,16562-16565; @Kroonen2013, p. 521; @Fulk2018, §12.18].

### DEV_NOTES:line-1591-1618

- Source heading: `Archived: Heavy Syllable Nasal Apocope (2026-02-06) — EMPIRICAL DISCOVERY`
- Source line or section hint: `lines 1591-1618`
- Fragment type: `archived_shared_rule_fragment`
- Status: `shared_trace_background`
- Issue tags: `heavy_syllable_apocope`; `*-ą`; `oe_tail_rules`; `project_internal_model`
- Recommended next use: `use_for_trace_explanation_only`

This fragment is not about `tredan` by name, but it directly explains the first active OE step in the row's published trace: `OE Heavy Syllable Nasal Apocope: *trédaną -> *trédan` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:5472-5472; Germanic/docs/debug_snapshots/oe_full_trace_report.txt:37186-37187]. DEV_NOTES describes that rule as an `empirically-derived phonological finding` and says explicitly that the literature did not straightforwardly state the extension from final `*-i/*-u` loss to final `*-ą` [Germanic/docs/DEV_NOTES.md:1595-1615]. For row `2264`, that means the fragment is useful as project-history context for the live derivation, but it is weaker than a lexeme-specific note and should not be oversold as direct philological evidence about the verb itself.

The practical value of keeping this fragment is modest but real. Without it, a later writer could see `*trédaną -> *trédan` in the trace and incorrectly assume that the deletion rule was an uncomplicated handbook citation. DEV_NOTES makes clear that this was a learned modeling generalization, not a verb-specific repair [Germanic/docs/DEV_NOTES.md:1599-1618]. That helps explain why the row derives cleanly while still leaving the DEV_NOTES support base relatively thin.

### DEV_NOTES:line-9592-9638

- Source heading: `Primary vs Secondary Nasalization: The Correct Solution`
- Source line or section hint: `lines 9592-9638`
- Fragment type: `notation_history_fragment`
- Status: `diagnostic_only`
- Issue tags: `secondary_nasalization`; `coda_nasal`; `notation`; `trace_intermediate`
- Recommended next use: `use_with_caution_as_project_history`

This fragment survives because the current `tredan` trace still includes `OE Secondary Nasalization: *trédąn` after heavy-syllable apocope [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:5472-5472; Germanic/docs/debug_snapshots/oe_full_trace_report.txt:37186-37188]. DEV_NOTES distinguishes primary nasalization from a second kind of nasalization before retained coda nasals and originally proposed a separate symbol `{*ã}` for that secondary type, stressing that it was `NOT yet in FST` at the time [Germanic/docs/DEV_NOTES.md:9610-9636]. The live trace now writes the intermediate with ogonek `*trédąn`, not with a separate tilde symbol, so this fragment is mainly notation chronology rather than current row policy.

For row `2264`, the safest use is diagnostic: it explains why the trace contains a nasalization stage even though the final surface form simply ends in `-an`. It should not be converted into a claim that `tredan` itself underwent some unusual lexeme-specific exception process. The trace and row both remain regular; the fragment only documents how the project talked about that regular coda-nasal environment at one stage of development [Germanic/docs/DEV_NOTES.md:9617-9638; Germanic/docs/debug_snapshots/oe_full_trace_report.txt:37187-37217].

## Superseded or diagnostic material

- No row-specific packet, research memo, or pilot note is currently attached for `2264`; coverage still marks the row as `none` in every support column [Germanic/docs/lexeme_reports/coverage_audit.md:399-399]. The present slice therefore replaces missing row-local notes rather than summarizing a fuller dossier.
- The duplicated Wiktionary provenance string in the live `NOTE` field is diagnostic rather than explanatory. It records source provenance, but it does not say why the row uses `*trédaną` rather than a citation form such as Kroonen's `*trudan-` / `*tredan-` or Orel's `*trudanan` [Germanic/data/germanic-aligned-final.tsv:1296-1296; docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:26624-26639; docs/references/orel_handbook_germanic_etymology.vision.txt:45391-45399; @Kroonen2013, p. 521; @Orel2003, p. 410].
- `germanic_nan_normalization.csv` preserves an older unaccented normalization pair `*tredanan,*tredaną` for the broader Dutch/English/German cognate set [Germanic/docs/germanic_nan_normalization.csv:85-85]. That is useful as project history, but it is not a row-local instruction and should not override the live OE row's accented `PROTO` / `PROTOFORM` or its `COUNTERPART tredan`.
- The secondary-nasalization notation proposal is superseded as live descriptive practice. DEV_NOTES proposed a separate `{*ã}` symbol for contact nasalization, whereas the current trace simply writes `*trédąn` under `OE Secondary Nasalization` [Germanic/docs/DEV_NOTES.md:9627-9636; Germanic/docs/debug_snapshots/oe_full_trace_report.txt:37187-37188]. That discrepancy belongs to project chronology, not to the lexical identity of `tredan`.

## Open questions for later work

- If a later lexeme report is written, it should keep the citation-layer distinction explicit: live project `PROTO = PROTOFORM = *trédaną`, comparative developmental narrative `PGmc *trudaŋ > PWGmc *tredan`, dictionary headword `*trudanan` or `*trudan- / *tredan-`, and OE `COUNTERPART = tredan` are related but not interchangeable labels [Germanic/data/germanic-aligned-final.tsv:1296-1296; docs/references/ringe_taylor_linguistic_history_vol2.txt:18639-18640; docs/references/orel_handbook_germanic_etymology.vision.txt:45391-45399; docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:26624-26639; @RingeTaylor2014, p. 325; @Orel2003, p. 410; @Kroonen2013, p. 521].
- If future indexing work wants an attachable DEV_NOTES anchor, the only genuinely strong one at present is the shared non-Verner note at `Germanic/docs/DEV_NOTES.md:7341-7375`; the heavy-syllable and nasalization fragments are better treated as shared trace background than as row-local content.
- `index.tsv` should probably remain untouched unless stronger row-specific DEV_NOTES or packet-level material is added. The row looks stable and well supported, but the surviving DEV_NOTES evidence is mostly shared background plus one comparative diagnostic note rather than a dedicated lexeme memorandum.
