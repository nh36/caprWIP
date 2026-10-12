---
row_id: 2175
concept: shaft
counterpart: sċeaft
proto: *skáftą
protoform: *skáftą
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2175 shaft / sċeaft

## Current row state

- The live OE row currently reads `CONCEPT = shaft`, `COUNTERPART = sċeaft`, `PROTO = *skáftą`, `PROTOFORM = *skáftą`, `DERIVATION_CLASS = regular` [Germanic/data/germanic-aligned-final.tsv:949-952].
- `PROTO` and `PROTOFORM` are identical in the live TSV. Nothing in the current row state suggests a surrogate modelling stem, a different paradigm cell, or an analogical repair input; the derivational input consumed by the OE cascade is the same `*skáftą` that labels the cognate set [Germanic/data/germanic-aligned-final.tsv:951-951].
- `oe_known_problems.tsv` has no row-specific entry for row `2175`, for `shaft`, for `sċeaft`, or for `*skáftą`; the file currently lists only unrelated exception buckets [Germanic/data/oe_known_problems.tsv:1-8].
- `coverage_audit.md` currently inventories row `2175` as `regular`, with no packet, memo, or other report artifact attached (`none`) [Germanic/docs/lexeme_reports/coverage_audit.md:338-345].
- The current published derivation trace is an exact match and shows the active pathway explicitly: `PROTO: *skáftą`, `EXPECTED: sċeaft`, `OUTPUTS: sċeaft`, with the OE-side stages `Anglo Frisian Brightening: *skæftą`, `OE Heavy Syllable Nasal Apocope: *skæft`, `OE Sk Palatalization: *ʃæft`, `OE Ws Palatal Diphthongization: *ʃeaft`, then surface `Outcome: sċeaft` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3974-3994].
- A separate diagnostic survey also still lists row `2175` only tersely as `*skáftą → sċeaft` with trigger inventory `á,ą`; that file is useful as a quick cross-check that no hidden `i`-umlaut or other front-vowel trigger is being invoked, but it is not a row analysis in its own right [Germanic/docs/debug_snapshots/retraction_trigger_survey.txt:90-90].
- No row-specific packet or research memo was found during slice preparation, so the YAML link fields are intentionally left blank and this slice stands as the replacement working note for the row.

## Development-note summary

No direct lexeme dossier for `shaft / sċeaft` survives in `DEV_NOTES.md`; what survives is a set of shared phonology notes plus the current exact-match trace. That means the secure row-level claim is narrower than for rows with dedicated literature audits. The live row is currently regular and exact, but the supporting DEV_NOTES evidence is mostly indirect: an archived project note for heavy-syllable loss of final `*-ą`, a neighboring-row note on West-Saxon palatal diphthongization after initial `ʃ`, and a diagnostic note explaining that the project's `sk` rule label should not be confused with ordinary OE velar palatalization or with manuscript spelling practice [Germanic/docs/DEV_NOTES.md:1591-1645,11180-11233,2991-2993; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3974-3994].

The distinction between `PROTO`, `PROTOFORM`, and the attested OE target is straightforward here and should be kept explicit. `PROTO = PROTOFORM = *skáftą` in the live TSV, so there is no row-policy split comparable to early-analogy rows where the comparative headword and modelling input diverge [Germanic/data/germanic-aligned-final.tsv:951-951]. The intermediate forms seen in the trace are therefore chronological derivational stages, not competing reconstruction layers: `*skáftą` is first brightened to `*skæftą`, then loses final `*-ą` after a heavy stem to give `*skæft`, then shifts initial `sk` to `ʃ`, then undergoes West-Saxon palatal diphthongization to `*ʃeaft`, and only after those steps is the form written as project-normalized `sċeaft` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3981-3994].

The notation layers matter. The trace names one stage `OE Sk Palatalization`, but DEV_NOTES elsewhere states more carefully that `sk → sc` is “not palatalization but a general OE shift of /sk/ → /ʃ/ spelled ⟨sc⟩” [Germanic/docs/DEV_NOTES.md:2991-2993]. In other words, the trace's rule name is project-internal shorthand for the phonological shift from `/sk/` to `/ʃ/`; it is not a claim that row 2175 behaves exactly like the `k/g` palatalization cases discussed under Campbell §§427–429. Likewise, the row's dotted `sċ-` is a project normalization layer, whereas manuscript-style spelling would ordinarily be plain `sc-`/`sceaft`. The slice should therefore keep phonological stage, rule label, and editorial spelling distinct instead of flattening them into a single statement.

The `ea` of `sċeaft` is best treated as a West-Saxon palatal-diphthongized surface stage, not as a signal that `PROTOFORM` should be rewritten. DEV_NOTES' nearest explicit discussion is the `sċēaþ` chronology note, where Campbell's `sċēaþ` is used to show that West-Saxon palatal diphthongization can convert a front vowel after initial `ʃ` into `ēa`, and a separate Campbell quotation says this diphthongization is “unknown to all Kt. and Merc. texts” [Germanic/docs/DEV_NOTES.md:11180-11233,6527-6529]. Row 2175 is not that long-vowel `ǣ → ēa` case; the live trace shows short `æ → ea` after initial `ʃ`. But the shared DEV_NOTES material still matters because it confirms the project's general interpretation of `ea` after an initial palatal as West-Saxon palatal diphthongization, not as a reason to split `PROTO` from `PROTOFORM` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3987-3994].

The weakest piece of the evidence chain is the final-vowel loss. DEV_NOTES explicitly labels heavy-syllable apocope of `*-ą` an “empirically-derived phonological finding” and says that neither Ringe-Taylor nor Hogg states this extension to `*-ą` outright [Germanic/docs/DEV_NOTES.md:1595-1615]. That does not make row 2175 wrong—the live trace currently uses the rule and matches exactly—but it does mean the row's best in-repo explanation partly rests on project-internal modelling history rather than a direct lexeme citation or a copied source statement about OE `sceaft`. For indexing purposes, that is a caution signal: the row is stable enough for a slice dossier, but the surviving DEV_NOTES support is still more diagnostic/shared than row-specific.

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-1591-1645

- Source heading: `Archived: Heavy Syllable Nasal Apocope (2026-02-06) — EMPIRICAL DISCOVERY`
- Source line or section hint: `lines 1591-1645`
- Fragment type: `archived_shared_rule_fragment`
- Status: `archived_but_still_live_in_trace`
- Issue tags: `heavy_syllable_apocope`; `*-ą`; `shared_phonology`; `project_internal_rule`
- Recommended next use: `use_with_caution_in_final_report`
- Shared with row IDs:

This is the only DEV_NOTES fragment that directly explains the trace step `*skæftą -> *skæft`, but it is also the fragment that most clearly advertises its own evidentiary limits. DEV_NOTES says the rule “deleting proto `*-ą` after heavy syllables” was an empirical discovery, notes that Ringe-Taylor and Hogg explicitly discuss only final short `*i/*u` after heavy syllables, and then states that “neither source explicitly extends this pattern to `*-ą`” [Germanic/docs/DEV_NOTES.md:1595-1615]. For row 2175 the fit is obvious: `*skáftą` has a heavy stem by virtue of the `-ft-` cluster, and the live trace uses exactly this deletion before the onset shift and diphthongization stages [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3983-3988].

What makes this fragment valuable is not that it proves `sċeaft` philologically from a primary source, but that it preserves the project history behind the current successful derivation. What makes it weak for indexing is the same thing: the note is openly modelling-driven and not a copied lexeme citation. Later reporting can cite it to explain why the current cascade drops final `*-ą`; it should not be treated as if it were direct handbook testimony specifically on `shaft`.

### DEV_NOTES:line-11180-11233

- Source heading: `I-Umlaut / WS Palatal Diphthongization Chronology (2026-03-17)`
- Source line or section hint: `lines 11180-11233`
- Fragment type: `phenomenon_context_for_lexeme`
- Status: `current`
- Issue tags: `west_saxon_palatal_diphthongization`; `shared_sk_rows`; `chronology`; `ea_outcome`
- Recommended next use: `cite_with_scope_note`
- Shared with row IDs: `2178`

This is the best current DEV_NOTES fragment for the row's final vowel shape, even though it is formally about `sċēaþ`, not `sċeaft`. DEV_NOTES quotes Campbell's note that there is “sǣǣþ sheath, beside sċēaþ,” then explains that the `ēa` form arises from West-Saxon palatal diphthongization after initial `ʃ` [Germanic/docs/DEV_NOTES.md:11180-11196]. The note then lays out an explicit chronology in which `*sk...` first becomes `*ʃ...` and only then feeds the WS palatal-diphthongization stage [Germanic/docs/DEV_NOTES.md:11190-11233].

For row 2175 the vowel source is not identical: `sċēaþ` is a long-vowel `ǣ → ēa` case created by i-umlaut, while the live `shaft` trace shows short `æ → ea` after Anglo-Frisian brightening and `sk > ʃ` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3987-3994]. But the fragment is still the clearest surviving DEV_NOTES authority for the project's broader claim that `ea` after initial `ʃ` belongs to West-Saxon palatal diphthongization chronology, not to an alternative `PROTOFORM`. It should therefore be cited as shared process support, with the explicit warning that it is analogical evidence from an adjacent row rather than a shaft-specific quotation.

### DEV_NOTES:line-6527-6529

- Source heading: `Campbell (1959) §187 via OE ġift 'gift'`
- Source line or section hint: `lines 6527-6529`
- Fragment type: `shared_scope_quote`
- Status: `current`
- Issue tags: `west_saxon_only`; `dialect_scope`; `palatal_diphthongization`
- Recommended next use: `cite_for_dialect_scope_only`
- Shared with row IDs: `2040`; `2178`

This short quotation is worth keeping separate because it is the clearest in-repo statement about dialect scope: Campbell §187 is quoted as saying, “The diphthongization of front vowels after palatals is unknown to all Kt. and Merc. texts” [Germanic/docs/DEV_NOTES.md:6527-6529]. For row 2175 that matters because the live target has the West-Saxon-looking `ea` outcome and the trace labels the responsible step explicitly as `OE Ws Palatal Diphthongization` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3987-3994].

This fragment should not be oversold. It does not attest `sceaft` or `sċeaft`; it only helps state that the final `ea` belongs to a specifically West-Saxon interpretive layer inside the current cascade. If row 2175 ever moves into a tighter index entry, this quote is useful for qualifying dialect scope, not for establishing the lexeme by itself.

### DEV_NOTES:line-2991-2993

- Source heading: `Missing ēa diphthong + sk/sc issue (*skawô → sċawa vs scēawa)`
- Source line or section hint: `lines 2991-2993`
- Fragment type: `notation_layer_fragment`
- Status: `diagnostic_but_reusable`
- Issue tags: `sk_shift`; `notation`; `rule_naming`; `orthography`
- Recommended next use: `cite_for_terminology_only`
- Shared with row IDs: `2181`

This fragment is crucial for preventing category mistakes in the row dossier. DEV_NOTES says, “The `sk -> sc` change is not palatalization but a general OE shift of `/sk/ -> /ʃ/` spelled ⟨sc⟩” [Germanic/docs/DEV_NOTES.md:2991-2993]. That sentence is the best in-repo explanation of why the trace label `OE Sk Palatalization` should be read as a pipeline name rather than as a fully theory-neutral description of the historical change.

For row 2175, the reusable part is the distinction between phonological shift and spelling layer. The local spelling claim in the source note—`scēawa` rather than project-normalized `sċēawa`—belongs to that other row's orthographic decision and should not override the current live target `sċeaft` [Germanic/data/germanic-aligned-final.tsv:951-951]. What should be preserved here is the narrower point: `*sk > ʃ` is the relevant historical stage, and manuscript-style `sc-` versus project-normalized dotted `sċ-` is a separate editorial question.

## Superseded or diagnostic material

The most important diagnostic residue is precisely the material that the current successful trace still depends on. The heavy-syllable `*-ą` note is archived and explicitly modelling-derived rather than literature-secured, so it remains a project-history explanation more than a philological argument [Germanic/docs/DEV_NOTES.md:1591-1645]. That is why row 2175 can be described as currently regular without yet being a strong candidate for central index integration.

The `sk/sc` note from the `scēawa` discussion is also partly diagnostic. Its terminological warning is reusable, but its local spelling expectation should not be copied mechanically into this row because the live dataset currently normalizes the row as `sċeaft`, not `sceaft` [Germanic/docs/DEV_NOTES.md:2991-2993; Germanic/data/germanic-aligned-final.tsv:951-951]. The diagnostic survey entry `2175    *skáftą    sċeaft    á,ą` is even thinner: it is useful only as a terse reminder that the row lives in the plain `á,ą` trigger space, not as evidence about attestation, dialect, or orthographic policy [Germanic/docs/debug_snapshots/retraction_trigger_survey.txt:90-90].

More broadly, the absence of a direct `shaft / sceaft` discussion in DEV_NOTES is itself part of the dossier. No surviving fragment copies a primary or secondary source directly on OE `sceaft`, and no row-specific packet or memo survives to bridge that gap. Later writers should therefore say plainly that the current row is supported mainly by a successful live derivation plus indirect shared notes, not by a preserved row-specific literature audit.

## Open questions for later work

- Verify a direct source citation for OE `sceaft`/`sċeaft` before treating the row as index-ready; the current slice has strong live-trace evidence but no preserved DEV_NOTES quotation specifically on the lexeme.
- Decide whether future row-level reporting should spell the attested target in manuscript-style `sceaft` or continue the project's normalized dotted `sċeaft`; DEV_NOTES preserves terminology about `/sk/ > /ʃ/`, but not a stable global spelling policy for this exact row.
- If a later index candidate is wanted, confirm whether the intended target is specifically West Saxon `ea` or a broader OE lemma abstraction, since the best explicit DEV_NOTES statement about after-palatal diphthongization says the process is not common to Kentish and Mercian [Germanic/docs/DEV_NOTES.md:6527-6529].
- Replace or supplement the archived heavy-syllable `*-ą` apocope note with a more source-secure explanation if possible; the current live cascade uses that rule successfully, but DEV_NOTES itself labels the extension to `*-ą` as a modelling discovery rather than an explicit handbook statement [Germanic/docs/DEV_NOTES.md:1604-1615].
