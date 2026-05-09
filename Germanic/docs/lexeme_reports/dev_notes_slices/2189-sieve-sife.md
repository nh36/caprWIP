---
row_id: 2189
concept: sieve
counterpart: sife
proto: *síbaz
protoform: *síbi
derivation_class: early_analogy
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file: Germanic/docs/lexeme_reports/packets/2189-sieve-sife.md
linked_research_memo_file: Germanic/docs/lexeme_reports/research_memos/2189-sieve-sife.md
linked_dossier_or_analysis_files:
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2189 sieve / sife

## Current row state

- CONCEPT: `sieve`; COUNTERPART: `sife`; live TSV currently keeps `PROTO = *síbaz`, `PROTOFORM = *síbi`, `DERIVATION_CLASS = early_analogy` [Germanic/data/germanic-aligned-final.tsv:1003; Germanic/docs/lexeme_reports/packets/2189-sieve-sife.md:7-9].
- The live TSV note is already unusually dense and materially correct about the OE-facing derivation: Kroonen lacks a `sieve` headword here; the working reconstruction is PGmc/WGmc `*sibi-`, short neuter i-stem from older s-stem `*sib-iz`; Campbell's Corpus Glossary `sibi` confirms the `*-i`; `*sibja-` would give OE `**sibb`; `*sibaz` would give OE `**sif`; and the OE row's `PROTOFORM` was therefore corrected from `*síbaz` to `*síbi` on 2026-04-24 [Germanic/data/germanic-aligned-final.tsv:1003].
- The packet's compact derivation trace is fully aligned with the live OE input: `PROTO: *síbi`, `EXPECTED: sife`, `OUTPUTS: sife`, with the explicit path `*síbi -> *síβi -> *síβe -> sife` via PGmc `*b` allophony and OE medial unstressed `i > e` [Germanic/docs/lexeme_reports/packets/2189-sieve-sife.md:17-40].
- The research memo records the same live probe distinction more explicitly: `*síbi` and `*síbiz` yield `sife`, while `*síbaz` yields `sif` and `*sibja` yields `sibb`; accordingly, the row problem is not a missing OE rule but choosing the right inherited stem-class input [Germanic/docs/lexeme_reports/research_memos/2189-sieve-sife.md:36-40, 63-73].
- `oe_known_problems.tsv` has no separate row-level exception entry for 2189, which is consistent with the current understanding that the FST is behaving correctly once the input is `*síbi` rather than `*síbaz` [Germanic/docs/lexeme_reports/packets/2189-sieve-sife.md:42-45].
- Coverage infrastructure still treats the row as lacking a finished report: `coverage_audit.md` lists `2189 | sieve | sife | early_analogy | no report`, and the packet says `_No manifest entry_`; this slice therefore has to function as the row's replacement working dossier rather than as a summary of already-stabilized report output [Germanic/docs/lexeme_reports/coverage_audit.md:133-135; Germanic/docs/lexeme_reports/packets/2189-sieve-sife.md:11-14].
- Batch-27 rollout notes also still mark the row as `Not ready` and explicitly flag pending cleanup of TSV `PROTO`, TSV `NOTE`, and DEV_NOTES §17.15 wording, so the row is documented but not yet clean enough for effortless index extraction [Germanic/docs/lexeme_reports/research_memos/batch_27_summary.md:10-13, 20-30].

## Development-note summary

The controlling DEV_NOTES material does **not** support treating `*síbaz`, `*síbi`, and attested OE `sife` as interchangeable labels for the same thing. The live row presently preserves a three-layer situation that has to be kept explicit. First, the comparative/cognate-set **PROTO** column still carries legacy `*síbaz`. Second, the OE derivational **PROTOFORM** actually fed to the FST is now `*síbi`. Third, the attested OE target is `sife` [Germanic/data/germanic-aligned-final.tsv:1003; Germanic/docs/lexeme_reports/research_memos/2189-sieve-sife.md:42-50]. DEV_NOTES §17.15 was written precisely because the older OE row had collapsed the first two levels and thereby forced the transducer to derive the wrong morphological class.

The row-specific philological conclusion preserved in DEV_NOTES is narrower, and more useful, than the live `PROTO` field suggests. The section says three parallel research passes converged on `PGmc *sibi-` as a **short-stem neuter i-stem**, historically continuing an older neuter s-stem `*sib-iz` [Germanic/docs/DEV_NOTES.md:28532-28548]. The comparison table there is worth preserving almost verbatim because it encodes the repo's present source hierarchy: Kluge/Seebold gives `WGmc *sibi- n.` and explicitly links the noun to the `seihen` family; Brunner explains original `*sib-iz` as an old s-stem absorbed into the i-declension; Campbell §§608–609 groups `sife` with short neuter i-stems such as `spere`, `gedyre`, and `orlege`; and Kroonen is cited not for a positive `sieve` reconstruction but for the negative fact that his entry at p. 429 is only `*sebjō-` 'kinship' > OE `sibb`, i.e. a different lexeme entirely [Germanic/docs/DEV_NOTES.md:28551-28557; docs/references/kluge_seebold_etymologisches_woerterbuch.txt:85009-85013; docs/references/campbell_old_english_grammar.txt:15781-15784]. Orel's `*sibaz` entry remains in the note, but DEV_NOTES already demotes it to ambiguous cover notation rather than decisive evidence for an OE-relevant a-stem [Germanic/docs/DEV_NOTES.md:28553-28556; docs/references/orel_handbook_germanic_etymology.vision.txt:36662-36668].

The OE evidence retained in DEV_NOTES is likewise specific and should not be reduced to a generic “attested with final `-e`” statement. Campbell's quoted Corpus Glossary note, `"Cp. sibi sieve"`, is used in §17.15 not as a spelling curiosity but as direct evidence that the older OE form still showed `-i` and archaic `⟨b⟩` before the later normalized spelling `sife` [Germanic/docs/DEV_NOTES.md:28586-28590, 28600-28601; docs/references/campbell_old_english_grammar.txt:11553-11554]. Clark Hall independently aligns with that distinction, listing both `sibi (GL) ... = sife` and `sife (y) n. 'sieve'`; Bosworth-Toller gives the secure lexical citation `Āsifte þurh sife`; and Bright's Reader prints `sife` in a neuter paradigm with genitive `sifes` and dative/instrumental `sife`, which is exactly the kind of inflection Campbell's i-stem discussion implies [docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:36200-36200, 36320-36324; docs/references/bosworth_toller_anglo_saxon_dictionary.vision.txt:8175-8175; docs/references/bright_anglo_saxon_reader.txt:1270-1277].

DEV_NOTES is also explicit about what the row **cannot** be. The rejected `*sibja-` analysis is not merely less elegant; it is phonologically wrong for the attested OE word. The section states that a light ja-stem neuter `*sibja-`, parallel to forms like `*wabja-` and `*kunja-`, would feed West Germanic Consonant Gemination and produce OE `*sibb(e)`, not `sife`; the homophonous-root kinship lexeme `*sibjō-` is cited as the positive control, because that is exactly how OE `sibb` arose [Germanic/docs/DEV_NOTES.md:28564-28580]. The minimal pair `sibb` 'kinship' versus `sife` 'sieve' is therefore not incidental lexical trivia but one of the row's strongest diagnostics.

The same section is just as clear that an a-stem `*sibaz` is wrong for the OE target, even if it survives as legacy project bookkeeping. DEV_NOTES says outright that a masc./neut. a-stem `*sibaz` would give OE `**sif` after ordinary loss of final `*-az/*-ą`, “exactly what the FST currently produces” under that old input [Germanic/docs/DEV_NOTES.md:28582-28590]. The memo's live re-check makes the same contrast operationally explicit: `*síbi/*síbiz -> sife`, but `*síbaz -> sif` and `*sibja -> sibb` [Germanic/docs/lexeme_reports/research_memos/2189-sieve-sife.md:36-40, 69-73]. For row work, that means `*síbaz` and `*síbi` are **not** merely alternate spellings or different notation layers for the same chosen input; they represent genuinely different morphological analyses with different OE outcomes.

Once the i-/s-stem analysis is chosen, however, DEV_NOTES' several stage forms are mostly notation variants or chronological checkpoints rather than competing policies. `*sib-iz` is the older morphological reconstruction; `*sibi`/`*sibiz` are unaccented probe forms; `*síbi`/`*síbiz` are the same forms with project stress marking; and WGmc/early OE `sibi` is the post-`*-z` stage directly reflected by Corpus Glossary spelling [Germanic/docs/DEV_NOTES.md:28592-28618]. Those should be read as one derivational family, not as four rival candidate row settings. By contrast, `*sibja-` and `*sibaz` are true rejected alternatives. This distinction matters for later indexing, because the note already mixes harmless notation shifts with live policy disagreement over what the comparative proto column should say.

The actual sound-law pathway in DEV_NOTES is fully regular once the correct stem class is selected. The section writes it out: PIE/PGmc `*sib-iz` > WGmc `*sibi` by final `*-z` loss; pre-OE still keeps `*-i` after a light stem; early OE gloss spelling gives `sibi`; and classical OE gives `sife`, with medial `b` represented later by `⟨f⟩` for a voiced spirant and final `-i` lowered to `-e` [Germanic/docs/DEV_NOTES.md:28592-28605]. The packet's compact derivation trace compresses the same path as `*síbi -> *síβi -> *síβe -> sife` [Germanic/docs/lexeme_reports/packets/2189-sieve-sife.md:21-40]. Nothing in the surviving row-specific note argues for a late OE analogical cell, a repaired ending, or a reconstructed unattested West-Saxon target. The row remains labelled `early_analogy` only in project metadata, because the practical fix was to choose the right inherited stem-class input upstream of OE, not to posit a late surface reshaping inside OE.

What is still unstable is not the OE derivation but the comparative bookkeeping surrounding it. DEV_NOTES §17.15.8 records only a `PROTOFORM` change, not a `PROTO` change, and even says the cognate-set English/Dutch/German rows retain their `*síbaz` encoding while the OE row alone was audited for FST derivation [Germanic/docs/DEV_NOTES.md:28621-28632]. The research memo and batch summary both treat that compromise as unfinished business rather than a final resolution: they explicitly recommend later cleanup of the surviving legacy `PROTO *síbaz` wording and say the row is still “not ready” in that sense [Germanic/docs/lexeme_reports/research_memos/2189-sieve-sife.md:79-87; Germanic/docs/lexeme_reports/research_memos/batch_27_summary.md:12-13, 24-30]. For present purposes, the safe dossier-level conclusion is therefore: OE `sife` is securely derivable from `PROTOFORM *síbi`; `*sibja-` and `*sibaz` are rejected for the OE row; but live row metadata still preserves an older comparative proto label that should not yet be indexed as if DEV_NOTES had fully stabilized it.

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-28521-28561

- Source heading: `§17.15 sife PROTOFORM research (row 1003 fix)`
- Source line or section hint: `§17.15.1-3, lines 28521-28561`
- Fragment type: `lexeme_specific`
- Status: `current`
- Issue tags: `protoform_vs_proto`; `stem_class`; `source_audit`; `reconstruction_disagreement`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This is the core row-specific research fragment. It preserves the exact problem statement (`*síbaz` derives `sif`, not `sife`) and the exact positive conclusion: the three-agent literature pass converged on `PGmc *sibi-`, “short-stem neuter i-stem, historically from a PGmc/PIE neuter s-stem `*sib-iz`” [Germanic/docs/DEV_NOTES.md:28525-28548]. It also keeps the most important source-by-source distinctions: Kluge/Seebold `WGmc *sibi- n.`, Brunner's old s-stem absorbed into i-declension, Campbell's short neuter i-stem grouping, and Kroonen's failure to supply a `sieve` headword here at all, only `*sebjō-` 'kinship' and unrelated `*sēdla-` [Germanic/docs/DEV_NOTES.md:28551-28557]. This fragment is presently attachable and should anchor any later report that needs to explain why the live OE row uses `PROTOFORM = *síbi` even though the comparative `PROTO` field still lags behind.

### DEV_NOTES:line-28564-28618

- Source heading: `Why NOT *sibja-`; `Why NOT *sibaz`; `Lautgesetzlich derivation of OE sife`; `FST probe (pre-change)`
- Source line or section hint: `§17.15.4-7, lines 28564-28618`
- Fragment type: `lexeme_specific`
- Status: `current`
- Issue tags: `rejected_etymon`; `wgmc_gemination`; `oe_attestation`; `fst_probe`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This is the fragment that most clearly separates rejected analyses from accepted notation variants. DEV_NOTES states that `*sibja-` would produce OE `*sibb(e)` by West Germanic gemination, exactly like kinship `sibb`, so it cannot underlie `sife` [Germanic/docs/DEV_NOTES.md:28564-28580]. It then says just as explicitly that a-stem `*sibaz` would give OE `**sif`, whereas the glossary spelling `sibi` and the normalized form `sife` require the i-/s-stem line [Germanic/docs/DEV_NOTES.md:28582-28605]. The short probe block then shows that `sibi`, `sibiz`, `síbi`, and `síbiz` all yield `sife`, and concludes that under project notation conventions the canonical row input is `*síbi` [Germanic/docs/DEV_NOTES.md:28607-28618]. That makes this fragment the best surviving authority for distinguishing: notation variants of the accepted i-stem analysis versus genuinely different, rejected row policies.

### DEV_NOTES:line-28621-28632

- Source heading: `TSV change`
- Source line or section hint: `§17.15.8, lines 28621-28632`
- Fragment type: `superseded_or_diagnostic_for_lexeme`
- Status: `diagnostic_only`
- Issue tags: `row_policy`; `metadata_drift`; `protoform_vs_proto`; `project_history`
- Recommended next use: `use_to_explain_no_index_status`
- Shared with row IDs:

This fragment is important but should not be indexed unqualified. It records the concrete row repair—`PROTOFORM: *síbaz -> *síbi` and alignment shortening—but it also freezes the compromise that now makes the row awkward for index ingestion: only the OE row was audited for derivation, while the cognate-set sister rows were left with `*síbaz` under an earlier bookkeeping precedent [Germanic/docs/DEV_NOTES.md:28621-28632]. That was a practical fix for the mismatch, not a fully harmonized reconstruction policy. The fragment therefore remains valuable as project history and explanation of current metadata drift, but not as a clean final statement that the row's comparative proto analysis is settled.

### DEV_NOTES:line-5371-5414; DEV_NOTES:line-17455-17472

- Source heading: `Applying the Theory to Our Data`; `Fulk vs. Our Implementation of *i → *e`
- Source line or section hint: `lines 5371-5414; 17455-17472`
- Fragment type: `phenomenon_context_for_lexeme`
- Status: `background`
- Issue tags: `i_lowering`; `labial_blocking`; `diagnostic_history`; `stale_input`
- Recommended next use: `keep_as_general_background`
- Shared with row IDs: `2058; 2107`

These earlier notes are useful only for the rule-side background behind `sife`, not for the row's stem-class decision. They cite `sieve` among forms where coda labials appear to block NWGmc/early-OE `*i > *e` lowering, contrasting `*sibăz` with expected `sef` or `sif`-type outputs under overbroad implementations [Germanic/docs/DEV_NOTES.md:5371-5414, 17455-17472]. The rule-side observation may still be helpful when explaining why accepted `*síbi` can pass to `sife` without unwanted earlier lowering, but the lexical input cited there is the old `*sibaz` framing. These fragments are therefore background phenomenon notes, not row-defining authority for the current OE reconstruction.

## Superseded or diagnostic material

The main diagnostic problem is that some repo-local artifacts still preserve pre-fix or partially normalized `*sibaz` workflows. DEV_NOTES' earlier i-lowering notes list `sieve` under `*sibaz/*sibăz` and use it as evidence for labial blocking; that remains potentially useful for the rule discussion, but it is not reliable row-level proto evidence after §17.15 [Germanic/docs/DEV_NOTES.md:5374, 5413, 17459-17472].

The live sandbox snapshot is even more obviously stale for row purposes. `Germanic/tmp/old_english_sandbox_results_current.json` still records the OE `sieve` entry with `proto: "*sibăz"` and output `sifez` [Germanic/tmp/old_english_sandbox_results_current.json:2440-2445]. That is diagnostic of an older harness/normalization layer, not of the live audited row in `germanic-aligned-final.tsv`, which now uses `PROTOFORM = *síbi` and whose packet trace yields plain `sife` [Germanic/data/germanic-aligned-final.tsv:1003; Germanic/docs/lexeme_reports/packets/2189-sieve-sife.md:17-40].

The research-memo infrastructure also preserves a deliberate “not ready” warning that should not be mistaken for uncertainty about the OE derivation itself. The memo is confident that `*síbi -> sife` is the correct OE-facing analysis, but it still recommends future cleanup of the surviving `PROTO *síbaz` and of DEV_NOTES wording that can make the legacy comparative label look more secure than it is [Germanic/docs/lexeme_reports/research_memos/2189-sieve-sife.md:75-87; Germanic/docs/lexeme_reports/research_memos/batch_27_summary.md:12-13, 24-30]. For this slice, that means the row is well enough understood to document, but not clean enough to index as if the note had no stale layers left.

## Open questions for later work

- Decide whether the live comparative `PROTO` field should remain legacy `*síbaz` or be brought into line with the stem-class analysis already accepted for the OE row (`*síbiz` or explicitly stem-form `*sibi-`); the slice should not prejudge the exact normalization, only the inadequacy of a true a-stem reading for OE `sife`.
- Reassess whether `DERIVATION_CLASS = early_analogy` is still the best label once the comparative proto column is cleaned. The surviving row argument is really about inherited stem selection upstream of OE, not about a late OE analogical cell.
- If DEV_NOTES §17.15 is ever indexed, split the core lexical findings (`*sibi-`, rejection of `*sibja-` and `*sibaz`, `sibi > sife`) from the narrower 2026-04-24 row-maintenance block, so the index can keep the durable analysis without inheriting the stale “OE row fixed, sister rows still legacy” compromise.
- If later report writing cites Orel, keep the qualification explicit that his `*sibaz` is being used here only as broad handbook cover notation; the row's accepted OE derivation depends on the i-/s-stem analysis preserved by Kluge/Seebold, Brunner, Campbell, and the OE attestation.
