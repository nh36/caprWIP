---
row_id: 2235
concept: swan
counterpart: swanes
proto: *swánaz
protoform: *swánas
derivation_class: early_analogy
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file: Germanic/docs/lexeme_reports/packets/2235-swan-swanes.md
linked_research_memo_file: Germanic/docs/lexeme_reports/research_memos/2235-swan-swanes.md
linked_dossier_or_analysis_files:
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2235 swan / swanes

## Current row state

- CONCEPT: `swan`
- COUNTERPART: `swanes`
- PROTO: `*swánaz`
- PROTOFORM: `*swánas`
- DERIVATION_CLASS: `early_analogy`
- Live TSV note/status: `using gen.sg. *swanas (> swanes)` [Germanic/data/germanic-aligned-final.tsv:1183]
- The live row is explicitly a **paradigm-cell** row rather than a citation-lemma row: lexeme-level `PROTO` stays nom.sg. `*swánaz`, but row-level `PROTOFORM` is gen.sg. `*swánas`, and the OE comparator is likewise gen.sg. `swanes` [Germanic/data/germanic-aligned-final.tsv:1183].
- The packet's compact derivation trace already matches the live row exactly: `PROTO: *swánas`, `EXPECTED: swanes`, `OUTPUTS: swanes`, with OE-side stages `*swánæs` and `*swánes` before surface `swanes` [Germanic/docs/lexeme_reports/packets/2235-swan-swanes.md:17-40].
- `oe_known_problems.tsv`: no entry was found for row `2235`, `swan`, `swanes`, `*swánaz`, `*swánas`, or normalized `*swanas`; the packet and memo both record no matching known-problem entry [Germanic/docs/lexeme_reports/packets/2235-swan-swanes.md:42-44; Germanic/docs/lexeme_reports/research_memos/2235-swan-swanes.md:33-39].
- Repo-local philological support keeps lemma and inflected cell distinct rather than collapsing them. Orel gives `*swanaz sb.m.: ON svanr 'swan', OE swan id.` [@Orel2003, s.v. "*swanaz"], Clark Hall gives `swan (o) m. 'swan.'` [@ClarkHall1960, s.v. "swan"], and Bright's glossary gives the exact paradigm-cell linkage `swan, m., swan: gs. swanes`, with commentary on the phrase `swanes feðre` [@BrightCassidyRingler1971, s.v. "swan"].

## Detailed development-note summary

The live row has to be described with the three-way distinction kept fully explicit. `PROTO` `*swánaz` is the cognate-set or etymological headword; `PROTOFORM` `*swánas` is the row-specific PGmc **gen.sg.** input; and OE `swanes` is the corresponding **gen.sg.** output chosen as the comparator for this row [Germanic/data/germanic-aligned-final.tsv:1183; Germanic/docs/lexeme_reports/research_memos/2235-swan-swanes.md:49-57]. The packet confirms that the current cascade handles that comparator regularly: `*swánas -> *swánæs -> swanes` [Germanic/docs/lexeme_reports/packets/2235-swan-swanes.md:17-40]. Any later prose that simply says "PGmc `*swánaz` became OE `swanes`" would therefore be misleading, because it would erase the paradigm-cell substitution that the live TSV is actually making.

Philological support is real but split across lemma and inflected cell. Citation-form evidence is straightforward: Orel gives OE `swan`, and Clark Hall likewise indexes the word as `swan` [@Orel2003, s.v. "*swanaz"; @ClarkHall1960, s.v. "swan"]. The exact row target is also directly supported, but only as an inflected form: Bright's glossary has `swan, m., swan: gs. swanes`, and the commentary specifically quotes `swanes feðre` [@BrightCassidyRingler1971, s.v. "swan"]. The safe formulation is therefore not "the OE word is swanes," but rather: citation lemma `swan`, selected and source-backed gen.sg. `swanes`.

Surviving DEV_NOTES support is thin and should be described conservatively. No dedicated row-specific current DEV_NOTES dossier survives for row 2235. The strongest **current** DEV_NOTES material is only a shared precedent note from the `ræst` discussion: it says the project could use gen.sg. `*rastas -> ræstes`, "parallel to hammer, swan, brand," but immediately warns that such an encoding "gives the correct phonological result but misrepresents the morphological class" [Germanic/docs/DEV_NOTES.md:3216-3218]. That warning is exactly the right working-note takeaway for row 2235: the live row's `*swánas -> swanes` pairing may be methodologically legitimate as a chosen paradigm cell, but it must not be mistaken for the lexeme's nominative headword pathway.

The only lexeme-specific DEV_NOTES hit currently recoverable is older and diagnostic rather than authoritative. In a 2025 tail-bucket debugging note, DEV_NOTES says: `the tail bucket still contains swan (*swanăz → sʋana), which is not from *‑aną; flag for later review of *‑ăz handling` [Germanic/docs/DEV_NOTES.md:2539]. That note is worth preserving because it shows earlier project trouble around nominative-style `*swanăz`, but it is not current row authority for `swanes`: it predates the present gen.sg. row framing, uses a different proto spelling, and records a debugging symptom rather than a row-policy decision [Germanic/docs/DEV_NOTES.md:2539; Germanic/docs/lexeme_reports/packets/2235-swan-swanes.md:76-102].

Because the DEV_NOTES evidence is so limited, packet and memo context have to carry more of the replacement-note burden than usual. The memo is especially important because it states plainly that the live workaround explanation survives only as note-like structure text, not as a fully argued TSV `NOTE`, and because it distinguishes exact gen.sg. support from citation-form support instead of pretending the row is self-evident [Germanic/docs/lexeme_reports/research_memos/2235-swan-swanes.md:11-23, 61-74]. For this row, the replacement working note should therefore preserve two separate propositions: (1) `swanes` is a real and source-backed OE gen.sg.; (2) current DEV_NOTES do **not** provide a robust row-specific argument that this inflected cell should outrank citation-form `swan` as the indexed lexeme target.

## Relevant DEV_NOTES fragments with line-based refs

### DEV_NOTES:line-3216-3218

- Source heading: `Decision note in the ræst discussion`
- Source line or section hint: `lines 3216-3218`
- Fragment type: `copied_shared_lexeme_fragment`
- Status: `current`
- Issue tags: `paradigm_cell`; `proto_vs_protoform`; `morphological_class`; `row_policy`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs: `1965; 2053; 2152`

DEV_NOTES says the project could use gen.sg. `*rastas -> ræstes`, "parallel to hammer, swan, brand," but warns that this kind of encoding "gives the correct phonological result but misrepresents the morphological class" [Germanic/docs/DEV_NOTES.md:3216-3218]. For row 2235, that is the most useful current methodological witness. It does not prove the row by itself, but it does justify keeping `PROTO` `*swánaz` separate from row-level `PROTOFORM` `*swánas`, and it warns later writers not to describe `swanes` as if it were simply the lemma.

### DEV_NOTES:line-2539-2539

- Source heading: `Tail-bucket diagnostic after nasal-vowel loss audit`
- Source line or section hint: `line 2539`
- Fragment type: `lexeme_specific`
- Status: `diagnostic_only`
- Issue tags: `older_debugging_state`; `nominative_vs_oblique`; `*-az_handling`; `project_history`
- Recommended next use: `use_to_explain_superseded_analysis`
- Shared with row IDs:

DEV_NOTES records an earlier debugging symptom: `the tail bucket still contains swan (*swanăz → sʋana), which is not from *‑aną; flag for later review of *‑ăz handling` [Germanic/docs/DEV_NOTES.md:2539]. This is useful because it preserves a concrete reason why `swan` entered project diagnostics. It is not current authority for the live `*swánas -> swanes` row, because it describes an older nominative-style problem state and never records the later paradigm-cell decision in row-specific terms.

## Superseded or diagnostic material

The main superseded material is the older nominative-style debugging context around `*swanăz`, not the live gen.sg. row itself. The 2025 DEV_NOTES tail-bucket line and the packet's reuse of it belong to project chronology: they show that `swan` once appeared in an `*‑ăz` diagnostic bucket, but they do not explain or authorize the present `*swánas -> swanes` row policy [Germanic/docs/DEV_NOTES.md:2539; Germanic/docs/lexeme_reports/packets/2235-swan-swanes.md:76-102].

The other material that needs controlled handling is the shared `ræst` comparison. Its value is methodological, not row-specific. It shows that `swan` had become one of the stock precedents for a gen.sg. workaround, but the same note also warns that the workaround can misstate morphological class [Germanic/docs/DEV_NOTES.md:3216-3218]. That means the fragment should not be over-read as if DEV_NOTES had fully re-argued row 2235 on its own merits.

Philological support likewise has to stay sorted by paradigm cell. Orel and Clark Hall support citation-form `swan`; Bright supports exact gen.sg. `swanes` [@Orel2003, s.v. "*swanaz"; @ClarkHall1960, s.v. "swan"; @BrightCassidyRingler1971, s.v. "swan"]. None of those sources licenses collapsing lemma and inflected form into one undifferentiated target. For this row the useful diagnostic contrast is exactly that both forms are real, but only one is the citation headword.

## Open questions for later work

- If row 2235 is later indexed or turned into a full lexeme report, state explicitly that current DEV_NOTES support is **shared and thin**, not a dedicated row-specific argument; pair any citation of DEV_NOTES with the exact Bright evidence for gen.sg. `swanes` [@BrightCassidyRingler1971, s.v. "swan"].
- If the row is later normalized, keep the levels distinct: `PROTO` `*swánaz` as lexeme headword, `PROTOFORM` `*swánas` as selected gen.sg. input, and `COUNTERPART` `swanes` as the surface form of that chosen cell, rather than rewriting the row history as though `swanes` were the ordinary lemma.
- If later project notes recover a concrete row-update decision for `swanes`, that material would materially strengthen indexability. As the repository stands now, the slice rests on a real inflected form plus only sparse DEV_NOTES precedent, not on a robust row-specific DEV_NOTES dossier.
