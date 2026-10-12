---
row_id: 1950
concept: bind
counterpart: bindan
proto: "*bíndaną"
protoform: "*bíndaną"
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files: []
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 1950 bind / bindan

## Current row state

- The live OE row currently reads `CONCEPT = bind`, `COUNTERPART = bindan`, `PROTO = *bíndaną`, `PROTOFORM = *bíndaną`, `DERIVATION_CLASS = regular` [Germanic/data/germanic-aligned-final.tsv:1950-1950].
- The published derivation snapshot is already exact for the live row: `PROTO: *bíndaną`, `EXPECTED: bindan`, `OUTPUTS: bindan`, with OE-side steps `OE Heavy Syllable Nasal Apocope: *bíndan`, `OE Secondary Nasalization: *bíndąn`, and `OE Weak Tail Reduction: *bíndan` before surface `bindan` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:249-262].
- `coverage_audit.md` still treats row `1950` as a regular row with no pre-existing report infrastructure (`| 1950 | bind | bindan | regular | no | - | - | - | none |`), so there is no row-specific packet or research memo file to link from this slice at present [Germanic/docs/lexeme_reports/coverage_audit.md:200-200].
- `oe_known_problems.tsv` currently contains only unrelated exception rows and no entry for `*bíndaną` / `bindan`, so the row is not being managed as an open OE exception bucket [Germanic/data/oe_known_problems.tsv:1-8].

## Development-note summary

The surviving DEV_NOTES support for row `1950` is real, but it is mostly **shared bindan-family material** rather than a standalone row dossier. The important point is that this shared material is still materially relevant to the live row, because it fixes two interpretive risks that later reporting could otherwise reintroduce: (i) treating `bindan` as if it were a Verner-style `*nþ/*nð` item, and (ii) confusing the infinitive's regular `-an` outcome with the fronted `-en` seen in related participial formations [Germanic/docs/DEV_NOTES.md:7538-7556,7879-7885,10320-10343,10692-10902].

First, later March 2026 DEV_NOTES are explicit that `bindan` is **not** a hidden `*þ/*ð` row. The audit table classifies `bindan` as `| bindan | *bindăną | *bhendh- "to bind" | original *dh | No |`, and the prose conclusion states: “`bindan, windan`: PIE roots `*bhendh-, *wendh-` with aspirated `*dh` → PGmc `*d`. No Grimm `*þ` ever existed” [Germanic/docs/DEV_NOTES.md:7542-7556]. A later decision block makes the same policy sharper still: “Other `*nd` forms (bindan, windan, hund, etc.) have ORIGINAL `*d` from PIE `*dh` ... They were never `*þ` or `*ð` at any stage” [Germanic/docs/DEV_NOTES.md:7879-7882]. For this row, that means the live `PROTO = PROTOFORM = *bíndaną` is already the correct type of input; DEV_NOTES does not support rewriting it as an `*nþ/*nð` alternation case.

Second, the row's `-an` ending is defended by the same nasalization/fronting discussion that DEV_NOTES uses for the broader infinitive-versus-participle contrast. Ringe-Taylor are quoted as saying that unstressed `*a` was nasalized only when followed by a nasal in the **syllable coda**, not when followed by an **intervocalic nasal**; the worked example then gives exactly the row-relevant pair: `PGmc *bindana 'to tie' > PWGmc *bindan > OE bindan` versus `PGmc *bindand- 'tying' > PWGmc *bindandi > OE bindende` [Germanic/docs/DEV_NOTES.md:10322-10343]. Later source canvass and implementation notes keep the same distinction in more explicit phonological terms: Luick lists `bindan 'binden'` under the development of backed/nasalized infinitival `-an`, Fulk is quoted on fronting only before **heterosyllabic** `n`, and the chronology fix then verifies `bindaną  → bindan   ✓ (infinitive: nasalization blocks fronting)` [Germanic/docs/DEV_NOTES.md:10692-10703,10715-10721,10843-10902]. For row `1950`, this is the core current derivational support: the infinitive stays `bindan` precisely because the relevant `a` is in the coda-nasal environment, whereas forms with onset `n` in the following syllable are the ones that front to `-en`.

Third, DEV_NOTES also contains a smaller but useful encoding check showing that the row does **not** depend on a special breve-marked infinitive notation. In a later probe table, `| *bíndăną vs *bíndaną | bindan | none |` is given as a case where breve versus plain suffix marking makes no difference to the output [Germanic/docs/DEV_NOTES.md:21768-21776]. That matters because the live TSV row currently uses plain `*bíndaną`; DEV_NOTES does not preserve any current argument that row `1950` needs a different `PROTOFORM` encoding to derive `bindan`.

There is also older family-level discussion worth preserving, but it should be handled carefully. DEV_NOTES quotes Campbell's Class III paradigm as `"bindan, bind — band, bond — bundon — bunden"`, explicitly noting that Old English shows `d` throughout the paradigm [Germanic/docs/DEV_NOTES.md:7074-7082]. That is useful background for the lexeme family, but it is not a competing target analysis for the live row. Likewise, later DEV_NOTES discussions of `bunden` / `funden` and the analogical status of strong past-participle `-en` are real philological context, yet they concern the participial side of the paradigm and should not be back-projected onto the infinitive row `bindan` without saying so [Germanic/docs/DEV_NOTES.md:24893-24925,25466-25536].

The safest replacement-note conclusion is therefore conservative. Current DEV_NOTES support is **present but shared**: it is strong enough to justify the live regular row and to preserve why `bindan` is neither a Verner problem nor a fronted `-en` form, but it is not a dense row-local controversy dossier. That makes the slice useful as working documentation, while also suggesting that the row is probably weaker as an index anchor than note-bearing rows with dedicated packet or memo infrastructure [Germanic/docs/DEV_NOTES.md:7538-7556,7879-7885,10320-10343,21768-21776; Germanic/docs/lexeme_reports/coverage_audit.md:200-200].

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-7538-7556 and line-7879-7882

- Source heading: `Systematic Check: TSV Forms with *nd Clusters (2026-03-11)` / later decision block on `*d/*ð`
- Source line or section hint: `lines 7538-7556; 7879-7882`
- Fragment type: `lexeme_specific_shared_decision`
- Status: `current`
- Issue tags: `original_d_not_verner`; `nd_cluster`; `bindan_not_nþ_case`
- Recommended next use: `cite_if_explaining_consonant_history`
- Shared with row IDs: `2294`

This is the controlling current DEV_NOTES evidence for the row's consonant history. The table names `bindan` directly as a form with original `*d`, not a Verner alternant: `| bindan | *bindăną | *bhendh- "to bind" | original *dh | No |` [Germanic/docs/DEV_NOTES.md:7542-7544]. The prose conclusion then states: `"bindan, windan": PIE roots *bhendh-, *wendh- with aspirated *dh → PGmc *d. No Grimm *þ ever existed` [Germanic/docs/DEV_NOTES.md:7555-7556]. The later decision block sharpens the same point into project policy: `Other *nd forms (bindan, windan, hund, etc.) have ORIGINAL *d from PIE *dh ... They were never *þ or *ð at any stage` [Germanic/docs/DEV_NOTES.md:7879-7882].

For row `1950`, this fragment is materially relevant even though the row has no mismatch. It prevents later note-writing from reviving a false `*nþ/*nð` narrative just because the verb family contains `nd`.

### DEV_NOTES:line-10320-10343 and line-10692-10902

- Source heading: `R/T vol.2 §5.1.2 (p.142)` / `R/T vol.2 p.153` / later source canvass and implementation results
- Source line or section hint: `lines 10320-10343; 10692-10902`
- Fragment type: `shared_derivational_support`
- Status: `current`
- Issue tags: `infinitive_vs_participle`; `coda_nasalization`; `fronting_blocked`; `verification_history`
- Recommended next use: `cite_if_explaining_why_bindan_stays_an`
- Shared with row IDs: `1934`

This is the main current derivational support for the row. DEV_NOTES quotes Ringe-Taylor's rule in a form that directly governs `bindan`: `"unstressed *a was apparently nasalized when immediately followed by a nasal in the syllable coda, but not when immediately followed by an intervocalic nasal"` [Germanic/docs/DEV_NOTES.md:10322-10325]. The worked pair then uses the lexeme itself: `PGmc *bindana 'to tie' > PWGmc *bindan > OE bindan` but `PGmc *bindand- 'tying' > PWGmc *bindandi > OE bindende` [Germanic/docs/DEV_NOTES.md:10335-10340]. Later notes add Luick's `bindan 'binden'` evidence for backed/nasalized infinitival `-an` and then record the implementation check `bindaną  → bindan   ✓ (infinitive: nasalization blocks fronting)` [Germanic/docs/DEV_NOTES.md:10692-10695,10843-10848,10890-10902].

For this row, the practical force of the fragment is straightforward: `bindan` is the expected infinitive outcome under the current chronology, while fronted `-en` belongs to other paradigm environments and should not be silently imported into the row target.

### DEV_NOTES:line-21768-21776

- Source heading: `C. Probes confirming breve is inert outside AFB contexts`
- Source line or section hint: `lines 21768-21776`
- Fragment type: `shared_encoding_probe`
- Status: `current`
- Issue tags: `protoform_encoding`; `breve_inertness`; `no_row_specific_workaround`
- Recommended next use: `cite_if_questioned_about_plain_vs_breve_suffix_notation`
- Shared with row IDs:

This fragment is narrower than the first two, but it bears directly on the live row state because it checks the exact lexeme. The probe table says `| *bíndăną vs *bíndaną | bindan | none |` [Germanic/docs/DEV_NOTES.md:21774-21776]. That means current DEV_NOTES do not preserve any row-local need for a special breve-marked `PROTOFORM`; plain `*bíndaną` is sufficient for the present output.

### DEV_NOTES:line-7074-7082

- Source heading: `The Levelling Chronology`
- Source line or section hint: `lines 7074-7082`
- Fragment type: `shared_family_background`
- Status: `current_but_background`
- Issue tags: `class_iii_paradigm`; `generalized_d`; `family_context`
- Recommended next use: `use_as_background_only`
- Shared with row IDs:

This is not a row-local derivation argument, but it is still materially relevant family context. DEV_NOTES quotes Campbell's Class III pattern: `"bindan, bind — band, bond — bundon — bunden"` and then notes that Old English shows `d` throughout the paradigm [Germanic/docs/DEV_NOTES.md:7074-7082]. For row `1950`, the fragment helps keep the infinitive inside its wider OE verb family, but it should remain secondary to the later explicit `*d` audit and nasalization/fronting notes.

## Superseded or diagnostic material

- No dedicated superseded row-local target was located. Surviving DEV_NOTES do not argue that row `1950` once needed a different `COUNTERPART`, a different derivation class, or a special exception status; the note material is mainly about keeping the regular analysis from being misdescribed [Germanic/docs/DEV_NOTES.md:7538-7556,10320-10343,21768-21776].
- Later DEV_NOTES discussion of strong past-participle `-en` is relevant only as **family-level diagnostic context**. The notes explicitly contrast infinitive `bindan` with present participle `bindende`, and later family analysis argues over whether strong past participles like `bunden/funden` are regular or analogical; that material should not be read as changing the infinitive row itself [Germanic/docs/DEV_NOTES.md:10335-10343,24893-24925,25466-25536].
- The exact trace already lands on `bindan`, so this slice is not preserving a live mismatch-repair narrative. Its main value is documentary: preventing future conflation of `bindan` with Verner `*nþ/*nð` cases or with fronted participial `-en` material [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:249-262; Germanic/docs/DEV_NOTES.md:7879-7882,10890-10902].

## Open questions for later work

- Decide whether row `1950` should remain a no-index background slice. The current DEV_NOTES support is genuine and reusable, but it is mostly shared-rule material rather than a dense row-local dossier [Germanic/docs/lexeme_reports/coverage_audit.md:200-200; Germanic/docs/DEV_NOTES.md:7538-7556,10320-10343].
- If a future packet or memo is ever created for Class III strong infinitives, keep `bindan`, `bindende`, and `bunden` explicitly separated by paradigm function; the present notes show that the row's main documentary risk is paradigm conflation rather than target uncertainty [Germanic/docs/DEV_NOTES.md:10335-10343,24893-24925,25466-25536].
- If later reporting wants one short source-backed sentence for the row, the safest one is that `bindan` continues a PGmc verb with original `*d` and keeps infinitival `-an` because nasalization blocks fronting in the coda-nasal environment [Germanic/docs/DEV_NOTES.md:7555-7556,10322-10340,10890-10902].
