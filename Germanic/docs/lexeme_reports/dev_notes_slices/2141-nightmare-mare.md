---
row_id: 2141
concept: nightmare
counterpart: mare
proto: *márōn
protoform: *márōn
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file: Germanic/docs/lexeme_reports/packets/2141-nightmare-mare.md
linked_research_memo_file: Germanic/docs/lexeme_reports/research_memos/2141-nightmare-mare.md
linked_dossier_or_analysis_files: Germanic/docs/analysis/arestoration_r_l_research.md
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2141 nightmare / mare

## Current row state

- CONCEPT: `nightmare`
- COUNTERPART: `mare`
- PROTO: `*márōn`
- PROTOFORM: `*márōn`
- DERIVATION_CLASS: `regular`
- Live TSV note: the row now treats OE `mare` as the attested simplex target and keeps `*nihtmare` only as an unattested compound-level background note: “second element is OE mare 'nightmare' (n-stem fem., < PWGmc *mara, *marōn-, cf. ON mara, OHG mara). Per Ringe & Taylor ... the attested OE forms are mare (nom.sg.), maran (obl.), and variant mere. Earlier target mære reflected Wiktionary headword (Orel-style spelling) and was conflated with the unrelated OE adjective mǣre 'famous'” [Germanic/data/germanic-aligned-final.tsv:819-819].
- PROTO and PROTOFORM are identical in the live row, but the slice still has to keep levels separate: the active OE derivational input is simplex `*márōn`, while the concept-side compound `*nihtmare` is explicitly unattested and survives only in note/tokens context; the row does **not** claim an attested OE compound citation form [Germanic/data/germanic-aligned-final.tsv:819-819; Germanic/docs/lexeme_reports/packets/2141-nightmare-mare.md:17-41; Germanic/docs/lexeme_reports/research_memos/2141-nightmare-mare.md:41-59].
- `oe_known_problems.tsv`: no row-local problem entry for `2141`, `*márōn`, `mare`, or `mære` [Germanic/data/oe_known_problems.tsv:1-8; Germanic/docs/lexeme_reports/packets/2141-nightmare-mare.md:44-46].
- Packet and memo status: both row-local helper files already treat the live row as a corrected simplex-target case rather than an unresolved phonological problem; both identify `DEV_NOTES` §17.28 and the repo-local Ringe-Taylor extract as the controlling current authority, while flagging older `mære` material as stale project history only [Germanic/docs/lexeme_reports/packets/2141-nightmare-mare.md:15-41,150-236; Germanic/docs/lexeme_reports/research_memos/2141-nightmare-mare.md:15-23,61-72,86-99].
- Repo-local reference extracts checked for this slice confirm the hierarchy stated in the live TSV note: Ringe-Taylor gives “OE mare, maran, and mere”; Orel gives comparative `*marōn` but cites OE `mære`; Clark Hall directly records `mare ... nightmare, monster` and separately `mera m. incubus`, with `mere II. = mare`, which supports the `mere/mera` variant tradition but not the long-vowel target `mære` [docs/references/ringe_taylor_linguistic_history_vol2.txt:11146-11147; docs/references/orel_handbook_germanic_etymology.vision.txt:29678-29680; docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:27553-27554,27957-27964].

## Development-note summary

Current row-specific DEV_NOTES authority survives strongly for row 2141. The decisive current material is the dedicated correction cluster at `DEV_NOTES` §17.28, not the earlier mismatch log alone. That section says explicitly that `*márōn -> mare` is “the expected lautgesetzlich result,” that the reconstruction `PGmc / PNWGmc *marōn- 'nightmare'` is standard, and that the OE evidence to prefer is Ringe & Taylor's paradigm line with `mare`, `maran`, and `mere`, not the stale target `mære` [Germanic/docs/DEV_NOTES.md:36990-37055].

The key distinction is not between two surviving row-level protoforms but between three descriptive levels. At the comparative-lexeme level, DEV_NOTES and Ringe-Taylor frame the noun as `PGmc / PNWGmc *marōn-`, with PWGmc paradigm material `*mara, *marōn-` behind the OE outcomes [Germanic/docs/DEV_NOTES.md:37009-37032; docs/references/ringe_taylor_linguistic_history_vol2.txt:11146-11147]. At the row-input level, `PROTO = PROTOFORM = *márōn`, so the FST is intentionally being asked for a simplex n-stem outcome, not for an unattested compound [Germanic/data/germanic-aligned-final.tsv:819-819]. At the OE-target level, the row now selects attested simplex `mare`; reconstructed `*nihtmare` remains concept-side background only, and the live row should not be rewritten as if the compound itself were the attested citation form [Germanic/data/germanic-aligned-final.tsv:819-819; Germanic/docs/lexeme_reports/research_memos/2141-nightmare-mare.md:41-49].

Philologically, the current hierarchy is also clear enough to be self-sufficient here. DEV_NOTES preserves the contrast between Orel and Ringe-Taylor: Orel's lemma reads “OE mære 'nightmare',” but DEV_NOTES immediately notes that Orel gives “no philological evidence for a long-front-vowel form,” whereas Ringe-Taylor explicitly give `mare (nom.sg.), maran (oblique), and a variant mere`, with “no `mære` anywhere in the paradigm” [Germanic/docs/DEV_NOTES.md:37018-37032; docs/references/orel_handbook_germanic_etymology.vision.txt:29678-29680; docs/references/ringe_taylor_linguistic_history_vol2.txt:11146-11147]. Clark Hall strengthens the same conclusion inside the repo: `mare` is entered as the nightmare noun, while `mera m. incubus` and `mere II. = mare` show the short-vowel variant tradition that DEV_NOTES identifies with Ringe-Taylor's `mere`; those entries do not provide evidence for `mære` as the row target [docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:27553-27554,27957-27964].

The main historical caution is that older project materials did temporarily treat row 2141 as if it still targeted `mære`. That history survives in the initial post-fix mismatch table and in the stale affected-rows snapshot inside `arestoration_r_l_research.md`, where row 2141 is still listed as `mære` and “out of scope of short A-restoration” [Germanic/docs/DEV_NOTES.md:36666-36674,36786-36789; Germanic/docs/analysis/arestoration_r_l_research.md:717-717]. Those are useful diagnostics for how the row surfaced during the A-restoration repair, but they are no longer current authority. The replacement working note for row 2141 should therefore treat the live row as a corrected regular simplex-target row whose current authority is secure, while keeping `mære` only as superseded headword history [Germanic/docs/DEV_NOTES.md:37035-37090].

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-36757-36804

- Source heading: `§17.25.8 Post-fix verification`
- Source line or section hint: `lines 36757-36804`
- Fragment type: `superseded_or_diagnostic_for_lexeme`
- Status: `diagnostic_only`
- Issue tags: `a_restoration_fix`; `mismatch_exposure`; `target_side_issue`; `project_chronology`
- Recommended next use: `use_as_project_history_only`
- Shared with row IDs: `2003,2090,2240`

This is the key exposure-history fragment, but not the controlling current philology. After the A-restoration repair, DEV_NOTES logs `*márōn -> mare` as “lautgesetzlich-correct” while the TSV still had target `mære`, and it explicitly groups row 2141 with other rows whose mismatch surfaced because the phonology was fixed, not because the phonology had broken [Germanic/docs/DEV_NOTES.md:36770-36789]. The important preserved wording is that “FST output `mare` is regular; target `mære` likely reflects analogical i-umlaut or a different protoform,” followed immediately by the decision to defer the row into its own loop rather than treat it as a regression [Germanic/docs/DEV_NOTES.md:36786-36789]. For the replacement slice this fragment should be kept as project chronology only: it explains **when** row 2141 reappeared and why `mare` first became visibly mismatched, but the later §17.28 note supersedes its tentative framing of the problem [Germanic/docs/DEV_NOTES.md:36990-37005].

### DEV_NOTES:line-36990-37032

- Source heading: `§17.28 *márōn / *nihtmare row 2141: TSV target correction (mære → mare)` / `§17.28.2 The reconstruction is uncontroversial`
- Source line or section hint: `lines 36990-37032`
- Fragment type: `bibliography_or_source_audit_for_lexeme`
- Status: `current`
- Issue tags: `target_correction`; `source_hierarchy`; `attested_forms`; `proto_vs_protoform`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This is the controlling row-level source-audit fragment. DEV_NOTES first restates the crucial verdict from the earlier loop — “`*márōn -> mare` is not a bug in our rule” — and then gives the source hierarchy in usable form [Germanic/docs/DEV_NOTES.md:36999-37005]. It labels `PGmc / PNWGmc *marōn- 'nightmare' (n-stem fem.)` the standard reconstruction and juxtaposes two authorities: Orel, “`*marōn sb.f.`: `ON mara ... OE mære ... MLG mare, OHG mara`,” versus Ringe & Taylor, who give `PNWGmc *maron- ... > PWGmc *mara, *marōn- ... >— OE mare, maran, and mere` [Germanic/docs/DEV_NOTES.md:37009-37029; docs/references/orel_handbook_germanic_etymology.vision.txt:29678-29680; docs/references/ringe_taylor_linguistic_history_vol2.txt:11146-11147]. DEV_NOTES then draws the row-local conclusion explicitly: “Ringe-Taylor explicitly attest `mare` (nom.sg.), `maran` (oblique), and a variant `mere`, with no `mære` anywhere in the paradigm” [Germanic/docs/DEV_NOTES.md:37031-37032]. For this slice, that sentence is the safest current authority for why the OE target is `mare`.

### DEV_NOTES:line-37035-37053

- Source heading: `§17.28.3 Why the FST output mare is correct`
- Source line or section hint: `lines 37035-37053`
- Fragment type: `lexeme_specific`
- Status: `current`
- Issue tags: `a_restoration`; `fst_verification`; `regular_derivation`; `protoform_vs_proto`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This fragment is the clearest row-policy statement about the active derivation itself. DEV_NOTES identifies the FST input `*márōn` explicitly as “`PROTOFORM` (= paradigm-cell-specific)” and says it follows the ordinary n-stem feminine path: short PGmc `*a`, intervening single `*r`, back-vocalic `*-ō`, and A-restoration before that back vowel [Germanic/docs/DEV_NOTES.md:37037-37048]. The note then gives the operative conclusion in one line: “→ output: **`mare`** ✓ (matches RT vol. 2 p. 192 attested form). The FST output coincides with the reconstructed PWGmc `*mara` form ... everything is regular” [Germanic/docs/DEV_NOTES.md:37050-37053]. This is current row-specific authority that the live `PROTOFORM` is already appropriate and that no special exception handling, paradigm rescue, or rule change is needed.

### DEV_NOTES:line-37055-37077

- Source heading: `§17.28.4 Why the TSV target mære is wrong`
- Source line or section hint: `lines 37055-37077`
- Fragment type: `lexeme_specific`
- Status: `current`
- Issue tags: `wrong_target_source`; `wiktionary_contamination`; `headword_conflation`; `variant_mere`
- Recommended next use: `use_to_explain_superseded_analysis`
- Shared with row IDs:

This fragment is current because it explains the stale `mære` tradition without asking the slice reader to reconstruct that history independently. DEV_NOTES lists three plausible sources of the wrong target: “Wiktionary contamination,” conflation with the unrelated adjective `mǣre 'famous, renowned' (< PGmc *mēriz)`, and a weaker possibility that some earlier contributor may have tuned the target to an older buggy FST state [Germanic/docs/DEV_NOTES.md:37057-37072]. The note then adds a philologically important warning: Clark Hall's glossary form `mera m. incubus` is the same short-vowel variant tradition as Ringe-Taylor's `mere`, “It is *not* evidence for `mære`” [Germanic/docs/DEV_NOTES.md:37074-37077; docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:27957-27964]. For row 2141 this fragment should be preserved as the preferred explanation of how the project drifted toward `mære` and why that drift should not be revived.

## Superseded or diagnostic material

- The early post-fix mismatch framing — “row 2141 `*nihtmare` PROTO `*marōn` → `mære` ... target `mære` likely reflects analogical i-umlaut or a different protoform” — is preserved history, not current policy. §17.28 resolved the row more narrowly and more securely: the live target was simply wrong, while `*márōn -> mare` was already regular [Germanic/docs/DEV_NOTES.md:36786-36789,36999-37005].
- Orel's comparative entry `*marōn sb.f.: ... OE mære 'nightmare'` remains useful only as background for the stale headword tradition. It is not the best row-level OE authority, because DEV_NOTES itself marks the absence of philological support for that long-front-vowel citation and prefers Ringe-Taylor's `mare, maran, and mere` instead [Germanic/docs/DEV_NOTES.md:37018-37032; docs/references/orel_handbook_germanic_etymology.vision.txt:29678-29680].
- The checked analysis file preserves both current support and stale residue. Its quotation of Ringe-Taylor correctly gives `OE mare, maran, and *mere*`, but its affected-rows table still lists row 2141 as `mære` and “out of scope of short A-restoration”; that table should therefore be treated only as a pre-correction project snapshot [Germanic/docs/analysis/arestoration_r_l_research.md:141-141,717-717].
- Generic `mære` or `mare` hits elsewhere in repo-local dictionaries must stay contextually separated: the nightmare noun `mare`, the short-vowel variant tradition `mere/mera`, the adjective `mǣre`, and the unrelated equine noun `mare/miere` are all distinct items in the reference material and should not be collapsed in later report prose [docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:27090-27091,27553-27554,27957-27964,28294-28294].

## Open questions for later work

- If a full lexeme report is written later, it may be worth citing Clark Hall directly alongside Ringe-Taylor so that `mere/mera` can be described positively as a real variant tradition, while still excluding `mære` as the row target [docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:27553-27554,27957-27964; docs/references/ringe_taylor_linguistic_history_vol2.txt:11146-11147].
- If concept-side editorial policy ever changes, decide whether unattested compound `*nihtmare` deserves its own separately labelled reconstructed-compound treatment. Nothing in the current row authority requires changing `PROTO`, `PROTOFORM`, or `COUNTERPART`; the present row is already correctly modeling the simplex noun only [Germanic/data/germanic-aligned-final.tsv:819-819; Germanic/docs/lexeme_reports/research_memos/2141-nightmare-mare.md:65-72,90-99].
- If supporting analysis files are later cleaned up, `Germanic/docs/analysis/arestoration_r_l_research.md` line 717 should be explicitly marked stale or updated, since it still preserves the superseded `mære` target even though the same repo-local evidence base already supports `mare` [Germanic/docs/analysis/arestoration_r_l_research.md:141-141,717-717].
