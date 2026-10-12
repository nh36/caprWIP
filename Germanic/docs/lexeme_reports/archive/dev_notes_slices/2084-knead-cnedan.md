---
row_id: 2084
concept: knead
counterpart: cnedan
proto: *knédaną
protoform: *knédaną
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
  - Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2084 knead / cnedan

## Current row state

- Live OE row: `ID 2084 | CONCEPT knead | COUNTERPART cnedan | PROTO *knédaną | PROTOFORM *knédaną | DERIVATION_CLASS regular`; there is no row-local explanatory `NOTE`, only inherited-etymology source placeholders in the provenance columns [Germanic/data/germanic-aligned-final.tsv:597-597].
- Coverage state: `coverage_audit.md` still lists row `2084` as `| 2084 | knead | cnedan | regular | no | - | - | - | none |`, so this slice is replacing an otherwise uncovered row rather than summarizing an existing packet/memo workflow [Germanic/docs/lexeme_reports/coverage_audit.md:284-284].
- Known-problems state: `oe_known_problems.tsv` has no row-specific exception entry for this lexeme; nothing in the current repo tracks `*knédaną > cnedan` as a mismatch bucket or accepted anomaly [Germanic/data/oe_known_problems.tsv:1-8].
- Current derivation trace is fully successful and minimal: `PROTO: *knédaną`, `EXPECTED: cnedan`, `OUTPUTS: cnedan`, with only `OE Heavy Syllable Nasal Apocope: *knédan`, `OE Secondary Nasalization: *knédąn`, and `OE Weak Tail Reduction: *knédan` before `Outcome: cnedan` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2579-2598].
- Basic lexical support for the OE target survives in repo reference files independently of DEV_NOTES: `old_english_wiktionary.tsv` lists `knead	cnedan`, and Clark Hall has the exact headword `cnedan³ to knead` [Germanic/data/old_english_wiktionary.tsv:147-147; docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:9276-9276].

## Development-note summary

No row-specific DEV_NOTES block for `knead / cnedan` survives in the live `DEV_NOTES.md`. The only attachable DEV_NOTES material is **shared-background-only** and also partly **diagnostic**: a Class III strong-verb discussion written to show that certain OE verbs with `*d` are **not** Verner-law repair cases includes `*knedaną` among the verbs whose present stem already has inherited/default `*d` [Germanic/docs/DEV_NOTES.md:7349-7381].

That narrow point is still relevant for row `2084`. DEV_NOTES quotes Ringe-Taylor on the West Germanic regularization: `"'to knead' are reflected in PWGmc *tredan and *knedan"` [Germanic/docs/DEV_NOTES.md:7362-7363]. In other words, the surviving note does **not** present `cnedan` as a problematic OE target needing a substituted paradigm cell, analogical rescue, or exception label. It uses `*knedan` as one of the positive control cases contrasted with `*finþaną`, where a voiced alternant really does matter [Germanic/docs/DEV_NOTES.md:7368-7381].

For this row, that means the current project distinction remains simple and should stay explicit: `PROTO = *knédaną` and `PROTOFORM = *knédaną` are the same live input because no alternate probe form is currently in play, while the attested/target OE form is `cnedan` [Germanic/data/germanic-aligned-final.tsv:597-597]. The debug trace agrees: the row already derives straight to `cnedan` with no repair logic [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2579-2598].

External reference files support that conservative reading but should be classified carefully. Ringe-Taylor's source text says that PGmc zero-grade `*knudana` was regularized in PWGmc as `*knedan`; Kroonen gives the lexeme as `*knedan- ~ *knudan-`; Orel gives `*kneđanan` with OE `cnedan`, OS `gi-knedan`, and OHG `knetan` [docs/references/ringe_taylor_linguistic_history_vol2.txt:5030-5035; docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:15995-16000; docs/references/orel_handbook_germanic_etymology.vision.txt:24955-24958]. Those are useful corroborations for the lexeme family and for the historical background behind DEV_NOTES' quotation, but in the current row they are still **shared philological background**, not evidence that the live row needs a different `PROTOFORM` or a non-regular derivation class.

## Relevant DEV_NOTES fragments

No lexeme-dedicated `knead / cnedan` DEV_NOTES dossier survives. The usable fragment below is therefore shared background whose relevance has to be stated explicitly.

### DEV_NOTES:7349-7381

- Source heading: `Verification: Other Class III Verbs with *d Are NOT Verner Cases`
- Source line hint: `lines 7349-7381`
- Fragment type: `shared_background_only`
- Status: `current`
- Issue tags: `class_iii_present_regularization`; `original_d_not_verner`; `no_paradigm_probe`
- Recommended next use: `cite only if someone treats cnedan as a Verner-type repair case`
- Shared-with rows if relevant: `other Class III *d verbs discussed in the same note, especially bindan / tredan / waldan families`

This is the only surviving DEV_NOTES passage that materially touches row `2084`, and its scope is narrow. The note is working through whether verbs with OE `d` should be handled like true Verner-alternation cases. After citing `*bindaną` and `*tredaną`, it gives the relevant quotation for this row: `"'to knead' are reflected in PWGmc *tredan and *knedan"` [Germanic/docs/DEV_NOTES.md:7357-7363]. DEV_NOTES then contrasts those verbs with `*finþaną`, where the text explicitly says that `findan` has a “voiced VL alternant levelled” and therefore really is a Verner case [Germanic/docs/DEV_NOTES.md:7368-7381].

For row `2084`, the substance to preserve is therefore not “special knead note” but a negative classification: `*knédaną > cnedan` is being treated as an ordinary inherited/regularized Class III verb with `*d`, not as a row requiring analogical target selection from some special paradigm cell. The same point is visible in the source text behind the DEV_NOTES quotation, where Ringe-Taylor says that PGmc zero-grade `*knudana` and `*trudang` are reflected in PWGmc `*knedan` and `*tredan` “with the default present-stem vocalism” [docs/references/ringe_taylor_linguistic_history_vol2.txt:5030-5035]. In present project terms, that shared background supports keeping `PROTO` and `PROTOFORM` unified and keeping the row in the ordinary successful-trace bucket [Germanic/data/germanic-aligned-final.tsv:597-597; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2579-2598].

## Superseded or diagnostic material

- No superseded row-specific DEV_NOTES block was located for `2084`. The absence is real and should be stated plainly: current row support comes from shared Class III-verb background plus the live successful derivation trace, not from a lost lexeme-local troubleshooting note [Germanic/docs/DEV_NOTES.md:7349-7381; Germanic/docs/lexeme_reports/coverage_audit.md:284-284].
- The surviving DEV_NOTES fragment is partly **diagnostic** because it was written to settle a different question—whether certain `*d` verbs are Verner cases—not to document `cnedan` as an individual lexeme report. Its main value is therefore boundary-setting: do **not** overread row `2084` as another `findan`-type alternation problem [Germanic/docs/DEV_NOTES.md:7368-7381].
- Literature notation is not fully uniform across repo references. DEV_NOTES/Ringe-Taylor foreground PWGmc `*knedan`; Kroonen gives `*knedan- ~ *knudan-`; Orel gives `*kneđanan`; Streitberg likewise groups OE `cnedan` with OHG `knetan` and ON `knoða` as verbs remodeled like `tredan` [docs/references/ringe_taylor_linguistic_history_vol2.txt:5030-5035; docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:15995-16000; docs/references/orel_handbook_germanic_etymology.vision.txt:24955-24958; docs/references/streitberg_urgermanische_grammatik.vision.txt:15517-15522]. For this slice those differences are diagnostic/background only; they do not by themselves show that the live row's `*knédaną` is in active need of replacement.
- Bosworth-Toller evidence in the repo is indirect here: searches hit prefixed forms such as `be-cnedan` and `ge-cnedan`, while Clark Hall and the OE Wiktionary export give the simplex headword directly [docs/references/bosworth_toller_anglo_saxon_dictionary.vision.txt:10936-10937,50180-50180; docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:9276-9276; Germanic/data/old_english_wiktionary.tsv:147-147]. That is useful source-audit context, not a derivational problem.

## Open questions for later work

- If a later lexeme packet is created, decide whether the report should normalize the comparative headword discussion explicitly: live project `*knédaną` versus Ringe-Taylor `*knedan`, Kroonen `*knedan- ~ *knudan-`, and Orel `*kneđanan` [Germanic/data/germanic-aligned-final.tsv:597-597; docs/references/ringe_taylor_linguistic_history_vol2.txt:5030-5035; docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:15995-16000; docs/references/orel_handbook_germanic_etymology.vision.txt:24955-24958].
- If later indexing work requires genuinely row-local DEV_NOTES authority before a row is promoted, note that row `2084` currently does **not** have that kind of surviving block; any fuller report would have to be built from shared Class III literature plus the live trace, not from a dedicated old DEV_NOTES section [Germanic/docs/DEV_NOTES.md:7349-7381; Germanic/docs/lexeme_reports/coverage_audit.md:284-284].
- If stronger OE attestation support is wanted later, add an exact simplex Bosworth-Toller citation if one can be located in the repo sources; at present the cleanest direct headword support inside the repo is Clark Hall plus the OE Wiktionary export, while Bosworth-Toller search hits are prefixed derivatives [docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:9276-9276; Germanic/data/old_english_wiktionary.tsv:147-147; docs/references/bosworth_toller_anglo_saxon_dictionary.vision.txt:10936-10937,50180-50180].
