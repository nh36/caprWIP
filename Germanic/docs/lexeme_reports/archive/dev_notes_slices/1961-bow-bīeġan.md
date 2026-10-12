---
row_id: 1961
concept: bow
counterpart: bīeġan
proto: *báugijaną
protoform: *báugijaną
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file: Germanic/docs/lexeme_reports/packets/1961-bow-bīeġan.md
linked_research_memo_file: Germanic/docs/lexeme_reports/research_memos/1961-bow-bīeġan.md
linked_dossier_or_analysis_files:
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 1961 bow / bīeġan

## Current row state

- CONCEPT: `bow`
- COUNTERPART: `bīeġan`
- PROTO: `*báugijaną`
- PROTOFORM: `*báugijaną`
- DERIVATION_CLASS: `regular`
- Live TSV note: `Kroonen *baugjan- wv. 'to (make) bend' → OE bīeġan; boga is the noun *bugan-`
- `oe_known_problems.tsv`: no row-specific entry.
- `report_manifest.tsv`: no manifest entry for this lexeme file.
- Working distinction that must stay explicit: row 1961 is the weak causative verb 'to bend, make bend', not the strong verb row `1962 *béuganą / *báug -> bēag` and not the noun row `1963 *búgô -> boga`.

## Development-note summary

No dedicated long-form DEV_NOTES subsection survives for row 1961 alone. The usable authority is scattered across short row-explicit checks, a notation/source table, and broader sound-change notes on `*au + i` and CVVC weak-verb structure. That scattered pattern is itself the main row-level fact: `1961 *báugijaną -> bīeġan` is current because the row is now ordinary and already correct, not because DEV_NOTES had to build a special rescue argument for it [DEV_NOTES:line-26619-26623].

The live row remains a regular Class-I weak causative. DEV_NOTES' notation audit aligns the project's PGmc input notation with Ringe & Taylor and gives the row as a direct comparator: ``*baugijăną`` in project notation corresponds to R/T `*baugijana`, with OE reflex `bīeġan` and citation `"PNWGmc *baugijana 'to bend (it)'"` [DEV_NOTES:line-8974-8980; @RingeTaylor2014, p. 158]. That fragment matters because it secures two otherwise easy-to-blur points at once: the live `PROTOFORM` is not an ad hoc project invention, and the row belongs to the causative `*baugjan-` lexeme distinguished from noun `*bugan-` and strong-verb `*beugan- ~ *būgan-` comparators.

The structural note on CVVC stems is the closest thing DEV_NOTES has to a row-specific derivational explanation. It explicitly contrasts `*baug-` with `*straw-` and says the distinction turns on stem structure, not on superficial similarity: `*baug-` is a true diphthong-plus-coda-consonant heavy stem and therefore takes `*-ijăną`, while `*straw-` is a vowel-plus-glide sequence with different WGmc behavior [DEV_NOTES:line-9057-9075]. DEV_NOTES preserves the crucial R/T quotation in full: `"PNWGmc *baugijana 'to bend (it)' ... → *béagjan → WS OE bīegan"` [DEV_NOTES:line-9073-9075; @RingeTaylor2014, p. 158]. For this slice that is the core replacement-note claim: the row's `*báugijaną` is the expected heavy-stem weak causative input, not a malformed repair after the fact.

Later shared handbook audits make the OE side equally explicit. DEV_NOTES quotes Ringe & Taylor's general rule that long `*éa` from PGmc `*au` undergoes i-umlaut to West Saxon `ie`, and then immediately gives `PNWGmc *baugijan -> *béagjan -> WS biegan` as one of the model examples [DEV_NOTES:line-35061-35070; @RingeTaylor2014, §6.6.3]. A second handbook fragment keeps Campbell's evidence side by side with the same lexeme: `Campbell §200(5)` lists `biegan` among the standard West Saxon `ie` outcomes from `*éa + i-umlaut`, together with `biécnan`, `ciegan`, `hieran`, and `liefan` [DEV_NOTES:line-35481-35493; @Campbell1959, §200(5)]. These notes are important because they show that project `bīeġan` is just normalized OE spelling layered onto handbook `biegan`/`bīegan`; there is no surviving DEV_NOTES authority for treating the row as irregular or for swapping in another OE target.

Project chronology survives in one short superseded note. During the 2026-01-22 `*-gj-` chronology check, DEV_NOTES still reported that ``*baugjăną`` mispredicted `bīeġan`, even after related items such as `*xagjăz -> heġġ` and `*sangjăną -> senġan` had improved [DEV_NOTES:line-1750-1753]. That note is worth preserving, but only as implementation history. The later safety audit explicitly reverses its practical significance: row 1961 is listed as `✓ already correct` and already handled `via existing *gj→ʤ`, while the proposed `*aw+j` rule is marked as having `NONE` risk for this row because `*báugijaną` is a different input shape [DEV_NOTES:line-26619-26623]. So the only securely attachable DEV_NOTES dispute here is an old pipeline-stage mismatch report, not an active lexical or philological controversy.

The replacement working note should therefore stay narrow and explicit. Current row policy is simply to keep `PROTO = PROTOFORM = *báugijaną`, keep counterpart `bīeġan`, cite the row as a regular weak causative, and preserve the noun/strong-verb distinction every time the wider bow cogset is discussed. DEV_NOTES does not support any row-specific retargeting, analogical workaround, or exception label for 1961; when the row reappears in later notes, it reappears as a control case that is already behaving correctly [DEV_NOTES:line-26619-26623].

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-8974-8980

- Source heading: `Source attestation of *-ijăną forms / Ringe & Taylor notation table`
- Source line or section hint: `lines 8974-8980`
- Fragment type: `bibliography_or_source_audit_for_lexeme`
- Status: `current`
- Issue tags: `source_quote`; `protoform_notation`; `lexeme_disambiguation`; `weak_causative`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

DEV_NOTES aligns the project's `*-ijăną` notation with Ringe & Taylor's published reconstructions and includes the row explicitly: ``*baugijăną`` / `*baugijana` / `bīeġan`. This is current row authority because it ties the live `PROTOFORM` directly to handbook reconstruction and to the correct OE verb, rather than to the noun `boga` or the strong verb `būgan` [@RingeTaylor2014, p. 158].

### DEV_NOTES:line-9057-9075

- Source heading: `CVVC Stems and Sievers' Law: The *baug- vs *straw- Distinction`
- Source line or section hint: `lines 9057-9075`
- Fragment type: `phenomenon_context_for_lexeme`
- Status: `current`
- Issue tags: `sievers_law`; `stem_weight`; `weak_verb_class`; `row_input`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This shared note gives the best surviving explanation for why row 1961 has the shape it does. DEV_NOTES says `*baug-` is structurally `diphthong + consonant`, therefore a heavy stem with `*-ijăną`, and quotes R/T's chain `"PNWGmc *baugijana 'to bend (it)' ... → *béagjan → WS OE bīegan"` [@RingeTaylor2014, p. 158]. For row 1961, that means the live `*báugijaną` is the expected causative input, not a patched form introduced only to force the OE output.

### DEV_NOTES:line-35061-35070

- Source heading: `Ringe & Taylor (2014) §6.6.3 i-umlaut of diphthongs`
- Source line or section hint: `lines 35061-35070`
- Fragment type: `phenomenon_context_for_lexeme`
- Status: `current`
- Issue tags: `au_plus_i_umlaut`; `ws_ie`; `handbook_rule`; `shared_sound_change`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

DEV_NOTES preserves the general handbook rule behind the OE outcome: long `*éa` from PGmc `*au` gives West Saxon `ie` under i-umlaut, and `*baugijan -> *béagjan -> WS biegan` is one of the model examples. This fragment is the cleanest statement that `bīeġan` is the regular West Saxon development once the causative `*baugijan-` analysis is accepted [@RingeTaylor2014, §6.6.3].

### DEV_NOTES:line-35481-35493

- Source heading: `Attested OE lexemes with *au + i: handbook evidence`
- Source line or section hint: `lines 35481-35493`
- Fragment type: `copied_shared_lexeme_fragment`
- Status: `current`
- Issue tags: `handbook_attestation`; `ie_spelling`; `lexeme_support`; `shared_sound_change`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

Campbell's lexeme list is worth keeping because it names `biegan` directly among ordinary West Saxon `ie` outcomes from `*éa + i-umlaut` [@Campbell1959, §200(5)]. The fragment confirms that the row's OE target is not only reconstructable by rule but also handbook-normal as a lexical example.

### DEV_NOTES:line-26619-26623

- Source heading: `probe table for rows containing *Vw+j or related sequences`
- Source line or section hint: `lines 26619-26623`
- Fragment type: `verification_snapshot`
- Status: `current`
- Issue tags: `current_output`; `rule_scope`; `already_correct`; `closure`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This is the decisive current-state fragment. DEV_NOTES lists row 1961 as `*báugijaną  bīeġan  bīeġan  ✓ already correct`, with the note `via existing *gj→ʤ`. Any later report that treats the row as unsettled would therefore be out of date.

### DEV_NOTES:line-1750-1753

- Source heading: `OE *-gj- chronology check (2026-01-22)`
- Source line or section hint: `lines 1750-1753`
- Fragment type: `superseded_or_diagnostic_for_lexeme`
- Status: `diagnostic_only`
- Issue tags: `old_mismatch_snapshot`; `implementation_history`; `gj_chronology`; `project_history`
- Recommended next use: `use_as_project_history_only`
- Shared with row IDs:

This short note is the only securely attachable row-specific mismatch history inside DEV_NOTES proper. It records that `*baugjăną` still mispredicted `bīeġan` during an early `*-gj-` chronology pass. The fragment should be preserved so later writers can see that the row once participated in implementation debugging, but it should not be inflated into an enduring philological problem, because later DEV_NOTES material already marks the row as correct.

## Superseded or diagnostic material

The only row-specific DEV_NOTES material that is clearly superseded is the early 2026-01-22 mismatch note. No later DEV_NOTES passage preserves a rival current etymology, a paradigm-cell retargeting, or an exception label for row 1961. The more substantial noun/verb conflation history belongs mainly to packet- and memo-level repo history, not to a surviving DEV_NOTES argument. For normal workflow, the safe replacement-note stance is therefore: keep the old mismatch note as chronology, but do not pretend DEV_NOTES contains a still-live controversy once the row has been separated from `boga` and `būgan`.

## Open questions for later work

- If a final lexeme report covers rows 1961-1963 together, keep the wording explicit that `*báugijaną -> bīeġan` is the weak causative, `*béuganą / *báug -> bēag` is the strong-verb row, and `*búgô -> boga` is the noun row.
- Decide whether the final report should normalize all OE citations to `bīeġan` in project spelling while still quoting handbook spellings such as `biegan` or `bīegan` exactly as printed.
- If later rule audits revisit `*Vw+j` environments, keep row 1961 in the control set of forms already handled by existing `*gj` palatalization rather than reopening the superseded 2026-01-22 mismatch note as if it were current evidence.
