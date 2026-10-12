---
row_id: 2257
concept: tide
counterpart: tīd
proto: *tī́diz
protoform: *tḯdiz
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file: Germanic/docs/lexeme_reports/packets/2257-tide-tīd.md
linked_research_memo_file: Germanic/docs/lexeme_reports/research_memos/2257-tide-tīd.md
linked_dossier_or_analysis_files:
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2257 tide / tīd

## Current row state

- Live OE row `2257` currently stands as `PROTO = *tī́diz`, `PROTOFORM = *tḯdiz`, `COUNTERPART = tīd`, `DERIVATION_CLASS = regular`, with the live note `Kroonen *tīdiz f. i-stem 'time, hour' → OE tīd f.; tīdan is the verb 'to happen'` [Germanic/data/germanic-aligned-final.tsv:2257-2257].
- The row therefore already encodes the three-way distinction that later report work must keep explicit: `PROTO` is the comparative cognate-set headword, `PROTOFORM` is the OE-facing derivational input used by the transducer, and `COUNTERPART` is the OE noun target `tīd`, not the separate verb `tīdan` [Germanic/data/germanic-aligned-final.tsv:2257-2257].
- Existing packet and memo infrastructure already uses the stem `2257-tide-tīd`, so this slice reuses that filename rather than inventing a new one [Germanic/docs/lexeme_reports/packets/2257-tide-tīd.md:1-125; Germanic/docs/lexeme_reports/research_memos/2257-tide-tīd.md:1-107].
- Kroonen's lexical distinction is exactly the one preserved in the TSV note: `*tīdi- f. 'time' ... OE tid f. 'time, season, hour' ... tidan w.v. 'to betide, happen'` [@Kroonen2013]. That is the philological reason the row keeps the noun `tīd` and treats `tīdan` only as a confusable but separate lexeme.

## Development-note summary

The surviving `DEV_NOTES.md` support for row 2257 is real but thin. It does **not** preserve a row-local etymological dispute about whether OE should have the noun `tīd`, nor does it argue for a non-regular derivation. What survives is mainly the stressed-long-`ī` notation migration that affected this row together with other OE items whose root vowel had to be distinguished from the unstressed in-stem suffix `*-īn` handled elsewhere in the cascade [Germanic/docs/DEV_NOTES.md:41893-42041].

That distinction matters because row 2257 sits exactly at the boundary between comparative notation and OE-cascade input notation. `PROTO = *tī́diz` is the comparative headword spelling used for the cognate set; `PROTOFORM = *tḯdiz` is the machine-safe OE-facing input adopted after the migration to a dedicated stressed-long-`ī` tier; `COUNTERPART = tīd` is the ordinary OE surface noun after the special tier has been stripped away again [Germanic/data/germanic-aligned-final.tsv:2257-2257; Germanic/docs/DEV_NOTES.md:41923-41957]. The row should therefore **not** be read as if `*tī́diz` and `*tḯdiz` were competing proto-stages. In current project usage they are two notation layers for the same lexical item, with `*ḯ` introduced only so the OE machinery can tell stressed root long `ī` apart from unstressed suffixal long `ī`.

`DEV_NOTES` is explicit on that point. In the stressed-long-`ī` repair, it rejects the earlier context hack because “Words like `*tīdiz` or `*lībą` happen to satisfy the V+C+ context by accident of having an inflectional ending; the principle is unrelated” [Germanic/docs/DEV_NOTES.md:41913-41915]. The row is thus valuable as a reminder that the correct generalization is stress-based, not lexeme-specific and not dependent on the mere presence of final `-iz`. The same note then gives the key interpretive sentence: “The diaeresis is purely notational. Semantically `*ḯ` = stressed long *ī” [Germanic/docs/DEV_NOTES.md:41938-41940]. For row 2257, that is the controlling explanation of why the live OE-facing input is `*tḯdiz` while the comparative `PROTO` remains `*tī́diz`.

The row's only direct appearance in `DEV_NOTES` is accordingly a migration-and-verification appearance, not a lexical crisis. Batch 4 of the stressed-long-`ī` TSV migration names rows `2197, 2257, 2285 | slīm, tīd, hwīl`, with `tīd` glossed as “i-umlaut trigger w/ *ḯ no-op ✓” [Germanic/docs/DEV_NOTES.md:42020-42025]. The phrasing is important. It records that the suffix still counts as an i-umlaut trigger structurally, but there is no visible vowel-quality change in the output because the root already contains long `ī`; the row is therefore a **verification case**, not an exception case. The follow-up probe confirms exactly that: `tḯdiz   → tīd       (i-umlaut trigger present, *ḯ output ✓)` [Germanic/docs/DEV_NOTES.md:42031-42040].

The lexical identity of the row remains the noun throughout. The live TSV note and Kroonen both warn against confusion with the verb `tīdan`, and nothing in the migration note suggests otherwise [Germanic/data/germanic-aligned-final.tsv:2257-2257; @Kroonen2013]. If anything, the packet/memo trail shows that the real practical risk is lexical-table noise, because English `tide` can attract the verb `tīdan` unless the noun/verb split is kept explicit [Germanic/docs/lexeme_reports/packets/2257-tide-tīd.md:88-95; Germanic/docs/lexeme_reports/research_memos/2257-tide-tīd.md:78-85]. That warning belongs in the slice because it is exactly the kind of rediscovery later writers should not have to repeat.

The safest present reading is therefore conservative. Row 2257 is presently a regular noun row with a useful note, but its surviving `DEV_NOTES` value is mostly implementation history: stressed long `*ī` had to migrate from older combining-acute notation to single-codepoint `*ḯ`, and row 2257 was one of the checked noun cases showing that the migration left a regular output `tīd` intact [Germanic/docs/DEV_NOTES.md:41925-41939,42020-42040]. That is enough for a replacement working note, but it is still weaker than a dedicated lexical controversy dossier. On present evidence the row is better treated as a **no-index slice for now** than as a central indexed note.

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-41893-41957

- Source heading: `§17.46 Stressed long-ī tier (*ḯ) — principled fix for the *swīn regression`
- Source line or section hint: `lines 41893-41957`
- Fragment type: `phenomenon_context_for_lexeme`
- Status: `current`
- Issue tags: `stressed_long_i`; `notation_policy`; `proto_vs_protoform`; `stress_not_syllable_count`
- Recommended next use: `cite_if_explaining_row_notation`
- Shared with row IDs: `2101`; `2103`; `2105`; `2106`; `2153`; `2182`; `2188`; `2197`; `2285`; `2286`; `2290`; `2296`

This is the controlling current fragment for row 2257 even though the fragment is mostly about project notation policy rather than the noun `tīd` in isolation. It says that the previous context restriction was not principled because “Words like `*tīdiz` ... happen to satisfy the V+C+ context by accident,” and it replaces that hack with a stress-sensitive tier [Germanic/docs/DEV_NOTES.md:41913-41915]. It also states the interpretation that later writing must preserve verbatim: “The diaeresis is purely notational. Semantically `*ḯ` = stressed long *ī” [Germanic/docs/DEV_NOTES.md:41938-41940].

For row 2257, the practical consequence is that `PROTOFORM = *tḯdiz` should be treated as the live OE-facing encoding, while `PROTO = *tī́diz` remains the comparative headword spelling. The fragment does **not** authorize collapsing those fields into one label, but it does explain why they denote the same lexical base for current project purposes [Germanic/docs/DEV_NOTES.md:41923-41957].

### DEV_NOTES:line-42006-42026

- Source heading: `§17.46 ... E. TSV migration (Phase 4)`
- Source line or section hint: `lines 42006-42026`
- Fragment type: `lexeme_specific`
- Status: `current`
- Issue tags: `tsv_migration`; `row_explicit`; `stressed_long_i`; `i_umlaut_trigger_no_op`
- Recommended next use: `cite_if_documenting_row_history`
- Shared with row IDs: `2197`; `2285`

This is the one securely attachable fragment that names row 2257 directly. Batch 4 lists `tīd` among the rows migrated into the stressed-long-`ī` cohort and glosses it as “i-umlaut trigger w/ *ḯ no-op ✓” [Germanic/docs/DEV_NOTES.md:42020-42025]. That wording should be preserved because it captures the row's real project significance: the suffixal trigger is still structurally present, but the noun remains surface `tīd`.

The fragment should still be read narrowly. It records successful migration history, not a need to change `COUNTERPART`, not a dispute over noun versus verb, and not an exception label. It is useful because it ties row 2257 explicitly to the notation migration; it is not evidence for any broader lexical instability.

### DEV_NOTES:line-42031-42040

- Source heading: `§17.46 ... F. Verification`
- Source line or section hint: `lines 42031-42040`
- Fragment type: `diagnostic_project_history_for_lexeme`
- Status: `current`
- Issue tags: `verification`; `probe`; `regular_output`; `diagnostic_only`
- Recommended next use: `use_as_supporting_history_only`
- Shared with row IDs: migrated `*ḯ` rows

The verification probe `tḯdiz   → tīd       (i-umlaut trigger present, *ḯ output ✓)` is the strongest short-form project confirmation that the migrated OE-facing input still yields the correct noun output [Germanic/docs/DEV_NOTES.md:42031-42040]. It is worth carrying into the slice because later writers would otherwise have to rediscover whether row 2257 was merely listed in the migration table or actually tested afterward.

Even so, this remains diagnostic history rather than a stand-alone lexical argument. It supports the live `regular` classification; it does not by itself justify indexing the row as if a substantial lexeme-specific note survived in `DEV_NOTES`.

## Superseded or diagnostic material

- Older project spelling with combining acute, i.e. `*tī́diz` as OE-facing input, should remain visible in this slice because the live row still preserves that notation in the `PROTO` field [Germanic/data/germanic-aligned-final.tsv:2257-2257]. But `DEV_NOTES` makes clear that the move to `*tḯdiz` was an encoding repair forced by input-tokenization behavior, not a change in lexical reconstruction or in the intended OE outcome [Germanic/docs/DEV_NOTES.md:41925-41939]. For this slice, older `*tī́diz` is therefore diagnostic of an earlier notation layer, not superseding evidence against the current row.
- The noun/verb contrast should also be preserved as a diagnostic warning. Kroonen distinguishes noun `*tīdi-` / OE `tid` from verb `tidan`, and the row note correctly follows that distinction [@Kroonen2013; Germanic/data/germanic-aligned-final.tsv:2257-2257]. Any lexical-table hit that points from English `tide` to verb `tīdan` is therefore noise for this row, not rival evidence.
- No surviving `DEV_NOTES` fragment argues that row 2257 is morphologically irregular, dialectally aberrant, or dependent on a substitute paradigm cell. The slice's main weakness is lack of rich row-local prose, not the presence of a competing analysis.

## Open questions for later work

- If a final lexeme report is later written, decide whether to quote Kroonen's noun/verb split directly in the main report text so the row's warning note is fully sourced rather than merely inherited from the TSV [@Kroonen2013].
- If later report work wants fuller OE philology, add direct noun-paradigm support for `tīd` and keep it separate from any attestations of verb `tīdan`; the current slice only needs the distinction, not a full paradigm discussion.
- If `dev_notes_slices/index.tsv` is revisited later, row 2257 should probably remain unindexed unless the project decides that notation-migration fragments alone are sufficient for indexing. At present the surviving `DEV_NOTES` evidence is mostly shared migration history plus one short verification probe, which is useful but still too thin for a strong index entry.
