---
row_id: 2258
concept: timber
counterpart: timber
proto: *tímrą
protoform: *tímbrą
derivation_class: early_analogy
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file: Germanic/docs/lexeme_reports/packets/2258-timber-timber.md
linked_research_memo_file: Germanic/docs/lexeme_reports/research_memos/2258-timber-timber.md
linked_dossier_or_analysis_files: []
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2258 timber / timber

## Current row state

- CONCEPT: `timber`
- COUNTERPART: `timber`
- PROTO: `*tímrą`
- PROTOFORM: `*tímbrą`
- DERIVATION_CLASS: `early_analogy`
- Live TSV note: `Kroonen *timbra- with *b; OE timber.` The live row therefore already distinguishes the comparative cognate-set headword from the OE-facing derivational input, and the row history explicitly records the correction `proto *timrą → *timbrą` at the `PROTOFORM` level rather than as a replacement of `PROTO` [Germanic/data/germanic-aligned-final.tsv:1272-1272].
- Packet and memo status: the existing row packet and memo both treat `*tímbrą -> timber` as the current working derivation and treat the older `*timrą`-based path as superseded project history rather than current row policy [Germanic/docs/lexeme_reports/packets/2258-timber-timber.md:7-9,17-42,124-149; Germanic/docs/lexeme_reports/research_memos/2258-timber-timber.md:5-19,41-57].
- `oe_known_problems.tsv` has no entry for this row or protoform, which matches the packet's assessment that the present row is not being tracked as an unresolved OE exception [Germanic/data/oe_known_problems.tsv:1-9; Germanic/docs/lexeme_reports/packets/2258-timber-timber.md:44-46].

## Development-note summary

The surviving DEV_NOTES support for row 2258 is usable but thin. There is no dedicated `timber` mini-dossier in `DEV_NOTES.md`; the current evidence comes from a shared phonology note on OE epenthetic vowel insertion plus one unrelated Modern English diagnostic mention. That means this slice has to preserve the current row policy explicitly instead of pretending DEV_NOTES already contains a row-specific final note [Germanic/docs/DEV_NOTES.md:16671-16711,2322-2324].

The row's core distinction is the one the live TSV now makes overt: `PROTO = *tímrą` remains the comparative proto headword, while `PROTOFORM = *tímbrą` is the row-specific OE derivational input. Those are not interchangeable fields. The reason for the split is the standing project correction that the OE row must carry the `b` seen in Kroonen's `*timbra-`; without that correction the older project input `*timrą` belongs to superseded history, whereas the current working input is the `b`-bearing form `*tímbrą` [Germanic/data/germanic-aligned-final.tsv:1272-1272; Germanic/docs/lexeme_reports/research_memos/2258-timber-timber.md:41-57,67-77]. In other words, the analogy/protoform intervention happens **before** ordinary OE phonology. That is why `early_analogy` remains the right derivation class for this row.

Once the corrected `PROTOFORM` is chosen, the surviving DEV_NOTES treat the rest of the derivation as ordinary OE phonology rather than as an ad hoc lexical repair. The relevant note lists `PGmc *timbrą → OE timber (via *timbr → *timbEr → *timber)` among the examples for `OEEpentheticInsertion` [Germanic/docs/DEV_NOTES.md:16671-16675]. It then states explicitly that this is a “**real phonological rule** representing ‘parasitic vowel insertion’ (also called ‘anaptyxis’ or ‘svarabhakti vowel’)” and anchors that claim to Campbell's discussion of medial vowels in unstressed syllables and to Ringe-Taylor's chronology for epenthesis [Germanic/docs/DEV_NOTES.md:16677-16691]. See also [@Campbell1959, §§463-464; @RingeTaylor2014, §6.9.5]. The same note also preserves the front/back conditioning needed for this lexeme: “After front vowels: `*E → *e` (e.g., `finger`, `timber`)” [Germanic/docs/DEV_NOTES.md:16687-16691]. For row 2258, then, the project decision is not that OE `timber` itself is dubious; the project decision is that the derivation should start from `*tímbrą`, after which the `-mbr` cluster behaves like the other epenthesis cases.

That division of labor should remain explicit in later work. `PROTO` is the etymological cognate-set label; `PROTOFORM` is the row-specific pre-OE input; `COUNTERPART` is the attested OE target `timber`. The note “Kroonen *timbra- with *b; OE timber” should therefore be read as justification for the row-specific `PROTOFORM`, not as grounds for silently rewriting the comparative `PROTO` field [Germanic/data/germanic-aligned-final.tsv:1272-1272; Germanic/docs/lexeme_reports/research_memos/2258-timber-timber.md:41-57,67-77]. For the comparative etymological background, see [@Kroonen2013].

The only other DEV_NOTES occurrence of `timber` is not OE-row authority. In the English attested-form harness, `timber` appears inside the Modern English diagnostic list `sieve/singe/timber` under “suffixal analogies” still missing from an English KIT-bucket sweep [Germanic/docs/DEV_NOTES.md:2322-2324]. That note is worth preserving only so later readers do not mistake the string hit for row-level OE evidence. It does **not** show that OE row 2258 itself is currently broken or in need of a late analogical rescue.

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-16671-16711

- Source heading: `OEEpentheticInsertion: Parasitic Vowel in Final Consonant Clusters (2026-04-10)`
- Source line or section hint: `lines 16671-16711`
- Fragment type: `shared_row_verification`
- Status: `current`
- Issue tags: `epenthetic_vowel`; `front_vowel_conditioning`; `protoform_with_b`; `ordinary_oe_phonology`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This is the fragment that currently matters most for row 2258. It explicitly includes `PGmc *timbrą → OE timber (via *timbr → *timbEr → *timber)` in the rule examples, then says the insertion rule is a “real phonological rule” rather than a patch, and adds the exact vowel-quality condition “After front vowels: `*E → *e` (e.g., `finger`, `timber`)” [Germanic/docs/DEV_NOTES.md:16671-16691]. For this row, the fragment's force is limited but clear: it does not argue for changing the comparative proto, but it does show that once the row-specific `PROTOFORM` has been corrected to `*tímbrą`, the `timber` outcome belongs to the ordinary OE epenthesis pathway described with reference to Campbell and Ringe-Taylor [Germanic/docs/DEV_NOTES.md:16679-16681,16708-16711]. Compare [@Campbell1959, §§463-464; @RingeTaylor2014, §6.9.5].

### DEV_NOTES:line-2322-2324

- Source heading: `KIT sweep (WIP)`
- Source line or section hint: `lines 2322-2324`
- Fragment type: `superseded_or_diagnostic_for_lexeme`
- Status: `diagnostic_only`
- Issue tags: `english_attested_form_project`; `cross_project_name_collision`; `suffixal_analogy`
- Recommended next use: `exclude_from_oe_indexing`
- Shared with row IDs:

This fragment mentions `timber`, but only as part of a Modern English attested-form cleanup list: “suffixal analogies (`sieve/singe/timber`)” [Germanic/docs/DEV_NOTES.md:2324-2324]. It should be preserved because searchers looking for `timber` in DEV_NOTES will find it. For the OE row, however, it is diagnostic noise rather than row authority. It does not discuss `PROTO`, `PROTOFORM`, OE epenthesis, or the live row target.

## Superseded or diagnostic material

- The important superseded material is the older project state in which `*timrą` functioned as the effective OE input. The live row history and both row-level support files now treat that as outdated, because the OE row requires the `b`-bearing `PROTOFORM = *tímbrą` while keeping `PROTO = *tímrą` distinct as the comparative headword [Germanic/data/germanic-aligned-final.tsv:1272-1272; Germanic/docs/lexeme_reports/packets/2258-timber-timber.md:7-9,124-149; Germanic/docs/lexeme_reports/research_memos/2258-timber-timber.md:17-19,35-57].
- The DEV_NOTES epenthesis section is current but shared. It proves the phonological pathway and preserves good handbook anchoring, yet it is still a general implementation note rather than a timber-only argument. Any future index entry should remember that this row's DEV_NOTES support is structurally thinner than a bespoke lexeme note [Germanic/docs/DEV_NOTES.md:16671-16711].
- The Modern English KIT-sweep mention is cross-project diagnostic material only and should stay outside any claim that the OE row itself is unstable or unresolved [Germanic/docs/DEV_NOTES.md:2322-2324].

## Open questions for later work

- If a later report wants a firmer literature-facing citation for the `b`-bearing input, add the exact Kroonen page/entry for `*timbra-` rather than relying only on the TSV note and memo-level paraphrase [Germanic/data/germanic-aligned-final.tsv:1272-1272]. Compare [@Kroonen2013].
- If this row is ever indexed from DEV_NOTES material alone, decide whether the shared epenthesis fragment is considered sufficient row authority, or whether the row should remain memo-backed/no-index until a more lexeme-specific note exists.
- If later cleanup revisits the row note, keep the field distinction explicit: `PROTO = *tímrą` is not the same object as row-specific `PROTOFORM = *tímbrą`, and the correction applies to the latter.
