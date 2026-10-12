---
row_id: 2210
concept: spread
counterpart: sprǣdan
proto: *spráidijaną
protoform: *spráidijaną
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2210 spread / sprǣdan

## Current row state

- Live `Germanic/data/germanic-aligned-final.tsv` line `1086` gives row `2210` as `CONCEPT spread`, `COUNTERPART sprǣdan`, `PROTO *spráidijaną`, `PROTOFORM *spráidijaną`, and `DERIVATION_CLASS regular`; the row has no custom note beyond duplicated Wiktionary inheritance history [Germanic/data/germanic-aligned-final.tsv:1086-1086].
- For this row the live table currently uses the same string for `PROTO` and `PROTOFORM`, but the slice still needs to keep their functions distinct: `PROTO` is the comparative/cognate-set headword slot, while `PROTOFORM` is the row-level FST input. The surviving DEV_NOTES material only comments on the input notation, not on any need to split the two fields for this row [Germanic/data/germanic-aligned-final.tsv:1086-1086; DEV_NOTES:line-8911-8934].
- `Germanic/data/oe_known_problems.tsv` has no entry for row `2210`, `sprǣdan`, or `*spráidijaną`; that absence is only bookkeeping, but it does align with the live row's `regular` classification [Germanic/data/oe_known_problems.tsv:1-8].
- `Germanic/docs/lexeme_reports/coverage_audit.md` lists row `2210 spread / sprǣdan` with packet, memo, and report coverage all `none`, so there is no existing packet or research-memo stem to reuse; the canonical row-based filename is therefore the correct slice filename here [Germanic/docs/lexeme_reports/coverage_audit.md:366-366].

## Detailed development-note summary

No long row-dedicated DEV_NOTES argument survives for `sprǣdan`. The useful material is thin and mostly shared, but it is still enough to replace a fresh search through DEV_NOTES for the present row. The main current point is that DEV_NOTES treats this lexeme as an ordinary **heavy-stem class I weak verb** whose proto input should be written with `-ij-`, not as a special OE problem demanding an analogical repair or a known-problems exception [DEV_NOTES:line-8911-8934; DEV_NOTES:line-8991-9043].

The one direct row-local DEV_NOTES hit is the March 2026 heavy-stem notation update table. There the project explicitly changes `*spraidjăną` to `*spraidijăną` and labels the stem as heavy by shape: `by analogy (CCVVC heavy)` [DEV_NOTES:line-8917-8934]. That note matters because it is the surviving project decision most closely tied to row `2210`: the row's live accented form `*spráidijaną` corresponds to DEV_NOTES unaccented `*spraidijăną`, so the current row is aligned with the later PGmc-style `-ij-` policy rather than with the older reduced `-j-` convention [DEV_NOTES:line-8911-8934].

The later analytical block makes the policy explicit in prose: “**Criterion:** A heavy-stem Class I weak verb should have `-ijăną` (Sievers' Law)” [DEV_NOTES:line-8991-8995]. The same block then includes `*spraidijăną | spraid- (CCVVC) | heavy | (by analogy)` in the list of forms now treated that way, and closes by stating that “All heavy-stem Class I weak verbs have been updated to use `-ijăną` notation” because that is etymologically correct and because “The SieversLawSyncope rule correctly handles them anyway” [DEV_NOTES:line-8997-9043]. For row `2210`, this is the closest thing DEV_NOTES preserves to a current project verdict: `sprǣdan` is being left in the regular system, with a heavy-stem `-ij-` proto input, rather than moved into a bespoke exception class.

Although DEV_NOTES does not spell out a full row-specific derivation for `sprǣdan`, the same notation dossier preserves directly comparable `*ai`-grade heavy-stem weak verbs whose OE reflexes show `ǣ`, especially `*laidijăną` → `lǣdan` and `*xailijăną` → `hǣlan` from Ringe & Taylor's cited forms [DEV_NOTES:line-8972-8987; @RingeTaylor2014, pp. 229, 234]. In other words, the surviving DEV_NOTES evidence does not merely say “the string was updated”; it places `*spraidijăną` in the same phonological/morphological type as other heavy `-ij-` verbs where PGmc `*ai` surfaces as OE `ǣ` before the weak suffix. That is enough support for keeping row `2210` as a routine regular derivation, even though the row still lacks a dedicated lexeme memo or handbook quotation aimed specifically at the lexeme ‘spread’ itself [DEV_NOTES:line-8976-8985; DEV_NOTES:line-8991-9043].

The thinness of the support needs to stay visible. DEV_NOTES does **not** preserve a row-local discussion of attestation, stem-class controversy, or any philological reason to distinguish `COUNTERPART sprǣdan` from the regular outcome expected from the live proto input. The slice should therefore stand as a conservative replacement note: the current project has one explicit notation/update decision for `*spraidijăną`, no surviving evidence of a row-local problem, and no reason at present to rewrite the row away from `regular`; but the row is still underdocumented compared with items that have packets or dedicated research sections [Germanic/docs/lexeme_reports/coverage_audit.md:366-366; DEV_NOTES:line-8911-8934; DEV_NOTES:line-8991-9043].

## Relevant DEV_NOTES fragments with line-based refs

### DEV_NOTES:line-8911-8934

- Source heading: `TSV Updates (server/data/germanic-aligned-final.tsv)`
- Source line or section hint: `lines 8911-8934`
- Fragment type: `row_local_notation_update`
- Status: `current`
- Issue tags: `heavy_stem_class_i`; `protoform_notation`; `row_specific_string_update`
- Recommended next use: `cite_in_final_report`

This is the most directly row-relevant surviving DEV_NOTES fragment because it names the lexeme's proto spelling explicitly. The table entry reads `*spraidjăną` → `*spraidijăną` with reason `by analogy (CCVVC heavy)` [Germanic/docs/DEV_NOTES.md:8931-8931]. For row `2210`, that fragment is the clearest statement that the project deliberately regularized the row into the heavy-stem `-ij-` class rather than treating the form as exceptional.

### DEV_NOTES:line-8972-8987

- Source heading: `Evidence from Ringe & Taylor (2014) Vol.2`
- Source line or section hint: `lines 8972-8987`
- Fragment type: `shared_comparator_fragment`
- Status: `current`
- Issue tags: `ringe_taylor`; `ai_to_oe_ae_long`; `heavy_stem_class_i`; `direct_quotation`
- Recommended next use: `cite_in_final_report`

This fragment does not mention `spread` directly, but it supplies the best preserved source-backed comparators for the row's phonological type. DEV_NOTES quotes Ringe & Taylor forms including `*laidijană 'to make go'` → `lǣdan` and `*hailijană 'to heal, to cure'` → `hǣlan` [Germanic/docs/DEV_NOTES.md:8982-8984; @RingeTaylor2014, pp. 229, 234]. For row `2210`, the value of this block is that it shows the project already treats heavy `*ai + ij` weak verbs as a normal route to OE `ǣ` outcomes, so `sprǣdan` sits in an ordinary comparative pattern rather than an ad hoc one.

### DEV_NOTES:line-8991-9043

- Source heading: `Analysis: Which Forms Are Etymologically Correct?`
- Source line or section hint: `lines 8991-9043`
- Fragment type: `shared_current_policy`
- Status: `current`
- Issue tags: `sievers_law`; `heavy_stem_class_i`; `regularity_policy`; `row_enabling_context`
- Recommended next use: `cite_in_final_report`

This is the controlling shared-policy fragment for the row. It states, “A heavy-stem Class I weak verb should have `-ijăną` (Sievers' Law),” includes `*spraidijăną | spraid- (CCVVC) | heavy | (by analogy)` in the heavy-stem inventory, and closes with the rationale that the system now uses `-ijăną` because it is etymologically correct and because “The SieversLawSyncope rule correctly handles them anyway” [Germanic/docs/DEV_NOTES.md:8991-8995, 9013-9013, 9037-9043]. For row `2210`, this is the best surviving DEV_NOTES authority for leaving the row in the ordinary regular derivational pipeline.

> “Criterion: A heavy-stem Class I weak verb should have `-ijăną` (Sievers' Law).” [Germanic/docs/DEV_NOTES.md:8991-8991]

> “All heavy-stem Class I weak verbs have been updated to use `-ijăną` notation.” [Germanic/docs/DEV_NOTES.md:9037-9037]

### DEV_NOTES:line-8719-8747

- Source heading: `Empirical Confirmation from Our TSV`
- Source line or section hint: `lines 8719-8747`
- Fragment type: `superseded_shared_policy`
- Status: `superseded`
- Issue tags: `older_notation_policy`; `post_sievers_leveling`; `project_history`
- Recommended next use: `use_to_explain_superseded_analysis`

This fragment is not row-local, but it preserves the superseded policy that the March 2026 update overturned. It had argued that heavy-stem class I weak verbs should be written with `-jăną`, not `-ijăną`, and then immediately marks that conclusion as `SUPERSEDED` once the project switches to PGmc-style input notation [Germanic/docs/DEV_NOTES.md:8719-8747]. For row `2210`, the fragment matters only as chronology: if older notes or searches surface `*spraidjăną`, that is the abandoned notation layer, not the current row policy.

## Superseded or diagnostic material

- The only clearly superseded row-adjacent material is the older general heavy-stem `-jăną` convention. DEV_NOTES no longer wants forms of the `*spraidjăną` type, and the later update table explicitly replaces that spelling with `*spraidijăną` [DEV_NOTES:line-8719-8747; DEV_NOTES:line-8911-8934].
- A separate diagnostic caution is orthographic rather than etymological: DEV_NOTES writes the row's protoform as unaccented `*spraidijăną`, while the live TSV writes accented `*spráidijaną`. Nothing in the surviving DEV_NOTES material treats these as different lexical reconstructions; they are notation-layer variants of the same row-level input, and the slice should not turn that graphic mismatch into a false PROTO versus PROTOFORM distinction [Germanic/data/germanic-aligned-final.tsv:1086-1086; DEV_NOTES:line-8911-8934].
- What is missing is as important as what survives. No current DEV_NOTES block gives a row-specific attestation discussion for `sprǣdan`, no fragment argues for irregular analogy, and no known-problems entry flags the row as unstable. That absence supports keeping the row regular, but it also means later index/report work should remain conservative about treating this slice as richly evidenced [Germanic/data/oe_known_problems.tsv:1-8; Germanic/docs/lexeme_reports/coverage_audit.md:366-366].

## Open questions for later work

- Check a future lexeme packet or literature pass for direct dictionary coverage of `*spráidijaną` / `sprǣdan`, so the slice can carry row-specific handbook or etymological citations instead of relying mostly on shared heavy-stem policy material.
- Decide whether later report prose should cite the row through the live accented `*spráidijaną`, the DEV_NOTES transliteration `*spraidijăną`, or both in parallel; the present slice keeps them aligned but does not try to normalize the notation.
- If `index.tsv` is revisited later, decide whether this row deserves indexing at all before a dedicated row-local source note exists. At present the best candidate fragments would be `DEV_NOTES:line-8911-8934` and `DEV_NOTES:line-8991-9043`, but both are mostly shared-policy material rather than a true lexeme dossier.
