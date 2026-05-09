---
row_id: 1947
concept: bid
counterpart: -
proto: *béudaną
protoform: *béudaną
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files: []
current_status: uncertain
needs_literature_agent: yes
---

# DEV_NOTES material — 1947 bid / bēodan (live counterpart blank)

## Current row state

- The live Old English row currently reads `CONCEPT = bid`, `COUNTERPART = -`, `PROTO = *béudaną`, `PROTOFORM = *béudaną`, `DERIVATION_CLASS = regular`, and has no live row-local explanatory note beyond source placeholders [Germanic/data/germanic-aligned-final.tsv:61-61].
- Immediate row context shows why a disambiguating filename matters. The same concept block also contains the English `bid` row from `*béudaną` and a separate Old English `bid` row `1948` from `*bídjaną`, but both OE rows still keep `COUNTERPART = -` in the live TSV [Germanic/data/germanic-aligned-final.tsv:58-64].
- Repo-local sources do nevertheless preserve a specific intended OE verb for the `*béudaną` branch. DEV_NOTES' infinitive-shape probe gives ``*béudăną`` and ``*béudaną`` with output `bēodan`; Bright lists `bēodan, bēad budon boden`; Clark Hall has `±beodan² to command, decree, summon`; and Hogg cites `beodan ~ bead ~ budon ~ boden` as the expected strong class II pattern. On that basis this slice uses filename stem `bēodan` while keeping metadata `counterpart: -` honest to the live row state [Germanic/docs/DEV_NOTES.md:21768-21785; docs/references/bright_anglo_saxon_reader.vision.txt:16416-16417; docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:5757-5759; docs/references/hogg_vol1.txt:7346-7348].
- `oe_known_problems.tsv` has no entry for `*béudaną` or for this row. That absence only means the row is not presently being managed as a known OE exception bucket; it does not by itself settle whether the dashed OE counterpart should later be promoted to explicit `bēodan` in the data table [Germanic/data/oe_known_problems.tsv:1-8].

## Development-note summary

Current DEV_NOTES support for row `1947` is real but thin. There is no dedicated lexeme dossier for this row, no row-local section headed `bid` or `bēodan`, and no explicit DEV_NOTES recommendation block saying “change row 1947 counterpart to `bēodan`.” The materially relevant evidence is instead shared implementation and phonology discussion that happens to preserve the OE form expected for the `*béudaną` branch [Germanic/data/germanic-aligned-final.tsv:61-61; Germanic/docs/DEV_NOTES.md:21768-21785,43943-43949].

The most direct DEV_NOTES passage is the infinitive-shape probe in the breve audit. There the project tests ``*béudăną`` against ``*béudaną`` and records output `bēodan` with `Difference = none` [Germanic/docs/DEV_NOTES.md:21774-21785]. That passage matters because it shows two things at once: first, current DEV_NOTES does in fact preserve `bēodan` as the OE reflex expected from this proto-verb; second, the immediate issue under discussion was not lexeme choice or attestation but whether reduced `*ă` versus plain `a` in the infinitive ending changes the OE result here. DEV_NOTES' answer for this lexeme is no: for `*béudaną`, the breve distinction is inert.

The other materially relevant DEV_NOTES passage is broader but still directly useful. In a later discussion of the `būgan/sċūfan` problem, DEV_NOTES says that inherited PGmc `*eu` “would regularly give OE *ēo — cf. *béuganą → bēogan attested in early Anglian” [Germanic/docs/DEV_NOTES.md:43943-43949]. That sentence is not about row `1947` by name, but it states the project's shared rule context for why a verb like `*béudaną` fitting the same inherited diphthong class would be expected to surface with OE `ēo`, not with a special analogical vowel. Hogg's handbook summary reinforces the same morphological slot by presenting `beodan ~ bead ~ budon ~ boden` as the ordinary strong class II paradigm [docs/references/hogg_vol1.txt:7346-7348].

The practical conclusion should stay conservative. The repo clearly preserves `bēodan` as the intended OE lexeme for the `*béudaną` row strongly enough to justify a `bēodan` filename and to distinguish row `1947` from the separate `*bídjaną` row `1948` [Germanic/data/germanic-aligned-final.tsv:58-64; Germanic/docs/DEV_NOTES.md:21774-21785]. But the live row still leaves `COUNTERPART = -`, and DEV_NOTES does not contain a row-local attestation audit or explicit data-change decision for this specific line. So the replacement note should preserve both facts together: intended `bēodan` is visible in shared repo sources, yet row `1947` remains underdocumented as a dashed OE slot rather than a fully ratified counterpart entry [Germanic/data/germanic-aligned-final.tsv:61-61; Germanic/docs/DEV_NOTES.md:21768-21785].

## Relevant DEV_NOTES fragments

### DEV_NOTES:no-dedicated-row-1947-section

- Source heading: no dedicated `1947` / `bid` / `bēodan` section survives in `Germanic/docs/DEV_NOTES.md`
- Source line or section hint: relevant support is limited to shared passages, not a row-local note
- Fragment type: `unclear_needs_human_review`
- Status: `uncertain`
- Issue tags: `missing_row_specific_authority`; `dashed_counterpart`; `thin_support`; `negative_result`
- Recommended next use: `check_against_literature`
- Shared with row IDs:

This negative result is itself materially relevant. Later reporting could easily overstate the case by noticing that DEV_NOTES contains `bēodan` somewhere and then treating row `1947` as if it already had a settled lexeme report. It does not. The current note base consists of shared passages that preserve the expected form, but not a row-local argument that explains why the live TSV still leaves the counterpart blank [Germanic/data/germanic-aligned-final.tsv:61-61; Germanic/docs/DEV_NOTES.md:21768-21785].

### DEV_NOTES:line-21768-21785

- Source heading: `C. Probes confirming breve is inert outside AFB contexts`
- Source line or section hint: `lines 21768-21785`
- Fragment type: `copied_shared_lexeme_fragment`
- Status: `current`
- Issue tags: `infinitive_shape`; `breve_inertness`; `intended_oe_target`; `implementation_probe`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs: `2003`; `2046`; `2071`

This is the clearest surviving DEV_NOTES fragment for row `1947`. The table explicitly records ``*béudăną`` vs ``*béudaną`` with output `bēodan` and `Difference = none` [Germanic/docs/DEV_NOTES.md:21774-21779]. Its importance is narrow but solid: the project was actively checking whether infinitive-end spelling with reduced `*ă` mattered here, and concluded that it did not. For this slice, that gives direct in-repo evidence that the `*béudaną` row belongs with OE `bēodan`, even though the passage is implementation-facing rather than a full lexeme dossier.

### DEV_NOTES:line-43943-43949

- Source heading: `Origin of the 3pl pret. choice`
- Source line or section hint: `lines 43943-43949`
- Fragment type: `phenomenon_context_for_lexeme`
- Status: `current`
- Issue tags: `inherited_eu_to_eo`; `strong_class_II`; `shared_phonology`; `comparator_bēogan`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs: `1961`; `1962`; `2184`; `2246`

This fragment is shared rather than row-specific, but it directly bears on why `bēodan` is structurally the right kind of OE target. DEV_NOTES states that PGmc `*eu` “would regularly give OE *ēo — cf. *béuganą → bēogan attested in early Anglian” [Germanic/docs/DEV_NOTES.md:43946-43949]. For row `1947`, the value of the fragment is phonological context: it does not prove the whole paradigm, but it does preserve the project's explicit expectation that inherited `*eu`-class verbal material maps to OE `ēo`, which aligns with the shared `bēodan` outcome seen in the breve probe and with handbook class-II paradigm citations [Germanic/docs/DEV_NOTES.md:21774-21779; docs/references/hogg_vol1.txt:7346-7348].

## Superseded or diagnostic material

- The line ``*béudăną`` vs ``*béudaną`` → `bēodan` is best treated as current but **diagnostic in scope**. It answers a spelling/shape question about the infinitive ending; it is not a dedicated attestation memo, semantic audit, or explicit row-policy note for why row `1947` still has `COUNTERPART = -` [Germanic/docs/DEV_NOTES.md:21768-21785].
- The live TSV distinction must therefore stay visible. Using `bēodan` in the filename is warranted by repo-local evidence, but it does **not** mean the dataset has already promoted `bēodan` into the OE counterpart field for row `1947`; the table still leaves that field blank, and row `1948` shows why conflation would be risky [Germanic/data/germanic-aligned-final.tsv:58-64].
- The lack of an `oe_known_problems.tsv` entry is also diagnostic only. It shows that the row is not presently triaged as a known FST exception, not that the row's documentation or counterpart selection is complete [Germanic/data/oe_known_problems.tsv:1-8].

## Open questions for later work

- Decide whether row `1947` should eventually promote `bēodan` into `COUNTERPART`, or whether the project wants to keep the OE field dashed until a dedicated row-local source audit is written.
- Review row pair `1947` (`*béudaną`) and `1948` (`*bídjaną`) together and add explicit note-level disambiguation if the live table continues to leave both OE counterparts blank [Germanic/data/germanic-aligned-final.tsv:58-64].
- Run a literature-focused pass if this row is later prepared for indexing or final reporting. The repo already contains enough local lexical evidence to point toward `bēodan`, but a dedicated memo should still gather the exact comparative and OE dictionary authorities in one place before treating the row as fully report-ready [docs/references/bright_anglo_saxon_reader.vision.txt:16416-16417; docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:5757-5759; docs/references/hogg_vol1.txt:7346-7348].
