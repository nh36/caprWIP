---
row_id: 2114
concept: lung
counterpart: lungen
proto: *lungō
protoform: *lúnganjō
derivation_class: early_analogy
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file: Germanic/docs/lexeme_reports/packets/2114-lung-lungen.md
linked_research_memo_file: Germanic/docs/lexeme_reports/research_memos/2114-lung-lungen.md
linked_dossier_or_analysis_files:
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2114 lung / lungen

## Current row state

- CONCEPT: `lung`
- COUNTERPART: `lungen`
- PROTO: `*lungō`
- PROTOFORM: `*lúnganjō`
- DERIVATION_CLASS: `early_analogy`
- Live TSV note: `*lunganjō (ō-stem feminine with *-anjō suffix; Wiktionary Reconstruction:Proto-Germanic/*lunganjō). OE lungen specifically reflects the *-anjō derivative.` The live history field also preserves that the row was previously kept at base `*lungō` and that the grammar was later extended to accept the derivative input [Germanic/data/germanic-aligned-final.tsv:713-713; Germanic/docs/lexeme_reports/packets/2114-lung-lungen.md:5-10].
- `oe_known_problems.tsv`: no row-specific entry is attached. The packet records `_None_`, and a direct row-id check likewise finds no row 2114 problem row [Germanic/docs/lexeme_reports/packets/2114-lung-lungen.md:44-46; Germanic/data/oe_known_problems.tsv:1-9].
- Packet status: the packet's compact derivation trace is current for the live modelling input, not for the comparative base noun. It records `PROTO: *lúnganjō`, `EXPECTED: lungen`, `OUTPUTS: lungen`, and traces `*lúnganjō` through gemination, final long-`ō` raising, i-umlaut, high-vowel apocope, j-loss after heavy syllable, and final geminate simplification before orthographic surface `lungen` [Germanic/docs/lexeme_reports/packets/2114-lung-lungen.md:15-41].
- Manifest/report status: no manifest entry is present for this row, so the packet and memo are still the working dossier rather than a vetted final report [Germanic/docs/lexeme_reports/packets/2114-lung-lungen.md:11-13; Germanic/docs/lexeme_reports/research_memos/2114-lung-lungen.md:13-18].
- Lexical-source baseline in repo references must stay split three ways. Kroonen gives the comparative headword `*lungōn- f. 'lung'` and then adds `Also cf. OE lungen, OFri. lungen(e), OS lungannia, OHG lungunna f. 'lung' <*lungunjō-`; Clark Hall has `lungen f. 'lung,'`; Bosworth-Toller preserves the headword `lungen` plus oblique forms `lungenne` and `lungene` [docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:18271-18280; docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:26618-26618; docs/references/bosworth_toller_anglo_saxon_dictionary.vision.txt:100241-100249].
- Supplementary lexical-table support exists but should stay secondary to the checked dictionaries: `old_english_wiktionary.tsv` has `lung\tlungen\tinh\ttemplate:inh\tlung` [Germanic/data/old_english_wiktionary.tsv:175-175; Germanic/docs/lexeme_reports/packets/2114-lung-lungen.md:146-153].
- Current DEV_NOTES authority status: there is **no securely attachable current row-specific DEV_NOTES decision block** for row 2114. The March 2026 row-specific note preserves useful history and one still-accurate attestation fragment, but the only clearly current DEV_NOTES support for the live modelling solution is the later shared implementation note at lines 17910-17929 showing that the transducer now handles `*lunganjō → lungen` [Germanic/docs/DEV_NOTES.md:13401-13504; Germanic/docs/DEV_NOTES.md:17910-17929; Germanic/docs/lexeme_reports/research_memos/2114-lung-lungen.md:17-20,36-41,61-67].

## Development-note summary

Row 2114 is an `early_analogy` / pre-OE derivational-selection case, not a late-paradigm-cell workaround. The checked materials all agree on the basic problem shape: the comparative base noun and the OE target are not the same thing. The live TSV row keeps `PROTO = *lungō` as the cognate-set headword, but it now feeds the generator with `PROTOFORM = *lúnganjō` in order to model the attested OE noun `lungen` [Germanic/data/germanic-aligned-final.tsv:713-713; Germanic/docs/lexeme_reports/research_memos/2114-lung-lungen.md:43-51,61-67]. The packet confirms that this live project input currently generates the target form successfully, while the March DEV_NOTES mismatch note preserves why the split became necessary in the first place: `*lungō -> lung (expected lungen)` [Germanic/docs/lexeme_reports/packets/2114-lung-lungen.md:17-41; Germanic/docs/DEV_NOTES.md:13405-13415].

The philology is more secure on the OE side than on the exact derivative reconstruction. `lungen` is an attested Old English noun and should not be replaced by unattested bare `lung`. Bosworth-Toller's row-local evidence preserves `lungen`, `lungenne`, and `lungene`; Clark Hall has the citation form `lungen f. 'lung,'`; and the memo is right to insist that this row targets the attested lemma rather than a ghost abstraction [docs/references/bosworth_toller_anglo_saxon_dictionary.vision.txt:100241-100249; docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:26618-26618; Germanic/docs/lexeme_reports/research_memos/2114-lung-lungen.md:53-60,69-73]. The row's OE target is therefore secure.

The unstable part is the exact pre-OE derivative label. The packet and March DEV_NOTES note foreground a Wiktionary-style account `OE lungen < PGmc *lunganjō`, treating `*-anjō` as the key suffixal explanation for the OE `-en-` stem [Germanic/docs/lexeme_reports/packets/2114-lung-lungen.md:39-41,106-140; Germanic/docs/DEV_NOTES.md:13418-13427]. But the strongest repo-local lexicographic source is Kroonen, not Wiktionary, and Kroonen does **not** present that same derivative as settled. Instead the reference extract gives base `*lungōn- f. 'lung'` and then specifically says `OE lungen ... <*lungunjō-` [docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:18271-18280; Germanic/docs/lexeme_reports/research_memos/2114-lung-lungen.md:38-41,45-52]. That means the live `PROTOFORM = *lúnganjō` is best treated as the project's current modelling transponent, not as an uncontested philological endpoint.

The current DEV_NOTES picture must therefore be read asymmetrically. The old March 2026 `lungen` note is still useful for checked chronology: it recorded the real mismatch, rejected the earlier confusion of base `*lungō` with the OE derivative, and preserved attestation snippets from Bosworth-Toller [Germanic/docs/DEV_NOTES.md:13405-13431]. But that same note also framed the derivative too narrowly around `*lunganjō`, and in its original context it still assumed that the grammar lacked the suffix and might have to leave the row as an exception [Germanic/docs/DEV_NOTES.md:13454-13504; Germanic/docs/lexeme_reports/research_memos/2114-lung-lungen.md:17-20,63-67,85-87]. Later DEV_NOTES work changed the computational state: the 2026-04-12 inter-stress-raising repair explicitly says that in derivational suffixes like `*-anjō`, `*j` blocks the raising environment, and it lists `*lunganjō → lungen` among the correctly handled outcomes with no mismatch regression [Germanic/docs/DEV_NOTES.md:17910-17929].

The replacement working note therefore has to preserve four distinctions explicitly. First, `PROTO = *lungō` is current row metadata, but it is only the simplified comparative headword for Kroonen's fuller `*lungōn-` [Germanic/data/germanic-aligned-final.tsv:713-713; docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:18271-18280]. Second, `PROTOFORM = *lúnganjō` is the row's live FST input because that is what the current packet trace models successfully [Germanic/docs/lexeme_reports/packets/2114-lung-lungen.md:17-41]. Third, `COUNTERPART = lungen` is the secure OE target and must remain distinct from both proto labels [docs/references/bosworth_toller_anglo_saxon_dictionary.vision.txt:100241-100249; Germanic/docs/lexeme_reports/research_memos/2114-lung-lungen.md:53-60]. Fourth, Kroonen's `*lungunjō-` evidence is not the same as the row's live project input and should be carried forward as an unresolved source-tension, not silently flattened into the packet's `*lunganjō` wording [docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:18279-18280; Germanic/docs/lexeme_reports/research_memos/2114-lung-lungen.md:77-87].

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-17910-17929

- Source heading: `14.6 Implementing Inter-Stress Raising: *a → *u (2026-04-12)`
- Source line or section hint: `lines 17910-17929`
- Fragment type: `copied_shared_lexeme_fragment`
- Status: `current`
- Issue tags: `inter_stress_raising`; `derivational_suffix`; `implementation`; `verification`; `protoform_vs_proto`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This is the only securely current DEV_NOTES fragment that directly supports the live modelling solution for row 2114. It does not settle whether the best comparative derivative is `*lunganjō` or Kroonen's `*lungunjō-`; instead it records the transducer-side repair that now makes the row work. DEV_NOTES says that inter-stress raising applies only when the consonant cluster before `*u` does not include `*j`, and therefore in derivational suffixes like `*-anjō` the immediately preceding `*j` blocks the rule. The explicit verification list then includes ``*lunganjō → lungen`` alongside non-row comparators such as ``*wer-aldu → *wer-uldu → weorold`` and ``*xamaras → hameres``, with mismatch count unchanged at 40 [Germanic/docs/DEV_NOTES.md:17910-17929]. For row 2114, this fragment is current implementation authority only: it justifies the live packet trace and the current `PROTOFORM` as an accepted project input, but it does not erase the separate lexicographic tension preserved in Kroonen and the memo [Germanic/docs/lexeme_reports/packets/2114-lung-lungen.md:17-41; Germanic/docs/lexeme_reports/research_memos/2114-lung-lungen.md:38-41,61-67,77-87].

### DEV_NOTES:line-13428-13431

- Source heading: `OE lungen 'lung': The *-anjō Suffix Problem (2026-03-21)`
- Source line or section hint: `lines 13428-13431`
- Fragment type: `bibliography_or_source_audit_for_lexeme`
- Status: `current`
- Issue tags: `attestation`; `oe_philology`; `dictionary_evidence`; `paradigm_background`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This short attestation block remains current even though it sits inside an otherwise outdated March discussion. DEV_NOTES preserves the Bosworth-Toller forms directly: ``lungen`` “nominative singular (glossed as *pulmo*),” ``lungenne`` “dative singular,” and ``lungena`` “genitive plural” [Germanic/docs/DEV_NOTES.md:13428-13431]. Those forms line up with the Bosworth-Toller extract under the dictionary headword `lungen`, which gives `foxes lungen`, `rammes lungenne (-ene, v. l.)`, and `betwux pære lungene` [docs/references/bosworth_toller_anglo_saxon_dictionary.vision.txt:100241-100244]. For this row the fragment is not a claim about which proto derivative must be reconstructed; it is current row-specific source audit showing that the OE target really is attested and that oblique `-en-` forms belong to the same lexeme.

### DEV_NOTES:line-13405-13415

- Source heading: `OE lungen 'lung': The *-anjō Suffix Problem (2026-03-21)`
- Source line or section hint: `lines 13405-13415`
- Fragment type: `superseded_or_diagnostic_for_lexeme`
- Status: `diagnostic_only`
- Issue tags: `mismatch_history`; `old_row_state`; `proto_vs_protoform`; `project_history`
- Recommended next use: `use_to_explain_superseded_analysis`
- Shared with row IDs:

This opening mismatch note should be preserved because it captures the real comparator that forced the later row split. DEV_NOTES records the exact old failure ``*lungō -> lung (expected lungen)`` and immediately states that the earlier TSV note was “**incorrect** — it confused the base form `*lungô` with the derived OE form” [Germanic/docs/DEV_NOTES.md:13407-13415]. That diagnosis is no longer the row's full current state, because the project now uses a derivative modelling input and the packet already derives `lungen` successfully [Germanic/docs/lexeme_reports/packets/2114-lung-lungen.md:17-41]. It remains diagnostically important, however, because later work still needs the regular comparator `*lungō > lung` in view when explaining why row 2114 is an upstream derivational-selection problem rather than a simple regular noun row [Germanic/docs/lexeme_reports/research_memos/2114-lung-lungen.md:61-67].

### DEV_NOTES:line-13418-13427

- Source heading: `OE lungen 'lung': The *-anjō Suffix Problem (2026-03-21)`
- Source line or section hint: `lines 13418-13427`
- Fragment type: `bibliography_or_source_audit_for_lexeme`
- Status: `misleading_if_uncontextualized`
- Issue tags: `suffix_analysis`; `reconstruction_disagreement`; `wiktionary_dependence`; `protoform_review`
- Recommended next use: `use_to_explain_superseded_analysis`
- Shared with row IDs:

This March source-audit fragment preserves real project history but should not be reused without explicit context. DEV_NOTES quotes a “**Wiktionary reconstruction**” that gives ``OE lungen < PGmc *lunganjō`` and describes `*-anjō` as the derivational mechanism behind OE `-en-`, adding cognates such as OFris `lungen(e)`, OS `lungannia`, and OHG `lungunna` [Germanic/docs/DEV_NOTES.md:13418-13427]. The cognate grouping and the emphasis on a derived feminine lexeme are still useful, but the exact reconstruction is not securely current on its own. Kroonen's repo-local dictionary extract instead gives base `*lungōn-` and explicitly derives the OE/Germanic `lungen` group from `*lungunjō-`, which is why the memo treats the live `*lúnganjō` as a modelling choice rather than settled comparative authority [docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:18271-18280; Germanic/docs/lexeme_reports/research_memos/2114-lung-lungen.md:38-41,51-60,77-85].

## Superseded or diagnostic material

- The March 2026 `lungen` note as a whole is not current row policy. Its mismatch framing is valuable history, and its Bosworth-Toller attestation excerpt remains usable, but its original discussion still belonged to the phase where the grammar rejected `*lunganjō` and the row was being weighed as a possible documented exception rather than a solved derivation [Germanic/docs/DEV_NOTES.md:13454-13504; Germanic/docs/lexeme_reports/research_memos/2114-lung-lungen.md:17-20,63-67,85-87].
- The packet's sentence `OE lungen specifically reflects the *-anjō derivative` should also be treated as narrower than the current source picture. It matches the live project input and the post-fix packet trace, but it does not reflect Kroonen's stronger repo-local `*lungunjō-` evidence and therefore should not be quoted as if it settled the comparative reconstruction by itself [Germanic/docs/lexeme_reports/packets/2114-lung-lungen.md:39-41; docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:18279-18280; Germanic/docs/lexeme_reports/research_memos/2114-lung-lungen.md:77-85].
- `old_english_wiktionary.tsv` is supportive but secondary here. Its `lung -> lungen` line agrees with the row target, yet it adds no philological discrimination beyond the checked dictionary extracts and should not outweigh Kroonen, Clark Hall, or Bosworth-Toller on the derivative question [Germanic/data/old_english_wiktionary.tsv:175-175; Germanic/docs/lexeme_reports/packets/2114-lung-lungen.md:146-153].
- The absence of any `oe_known_problems.tsv` row is itself current-state information. Row 2114 is no longer managed as an open OE mismatch in the present project state; the unresolved issue is source framing around `*lúnganjō` versus `*lungunjō-`, not failure to produce `lungen` [Germanic/docs/lexeme_reports/packets/2114-lung-lungen.md:44-46; Germanic/docs/lexeme_reports/research_memos/2114-lung-lungen.md:79-87].

## Open questions for later work

- Decide whether later row curation should review `PROTOFORM = *lúnganjō` against Kroonen's explicit `*lungunjō-` evidence, or whether the project will continue to keep `*lúnganjō` as a consciously transponent modelling input while documenting the disagreement directly [docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:18279-18280; Germanic/docs/lexeme_reports/research_memos/2114-lung-lungen.md:77-85].
- If a final lexeme report is drafted later, keep the three-way distinction explicit: comparative headword `*lungō` / Kroonen `*lungōn-`, live FST input `*lúnganjō`, and attested OE target `lungen` [Germanic/data/germanic-aligned-final.tsv:713-713; docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:18271-18280; Germanic/docs/lexeme_reports/packets/2114-lung-lungen.md:17-41].
- If `DEV_NOTES` is ever curated further, annotate the March 2026 `lungen` entry so the still-usable attestation material is separated more clearly from the now-misleading Wiktionary-based reconstruction framing [Germanic/docs/DEV_NOTES.md:13418-13431; Germanic/docs/lexeme_reports/research_memos/2114-lung-lungen.md:85-87].
- If `dev_notes_slices/index.tsv` is updated later, record row 2114 as having one current shared implementation fragment (`17910-17929`), one current row-specific attestation/source-audit fragment (`13428-13431`), one diagnostic mismatch-history fragment (`13405-13415`), and one misleading-if-uncontextualized March reconstruction fragment (`13418-13427`).
