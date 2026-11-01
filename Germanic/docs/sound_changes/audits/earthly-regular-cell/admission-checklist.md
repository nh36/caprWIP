# Earthly: future admission and publication

This is an implementation specification for a separately authorised adoption,
not permission to carry it out. The present branch adds research only. The
preferred target and its qualifications are governed by `assessment.md` and
`morphology.md`, not by the fact that an experimental spelling succeeds.

## Proposed selected cell

For the regular Genesis weak-neuter accusative singular hypothesis:

| Field | Proposed value or obligation |
| --- | --- |
| Stable identity | `2336` is presently unallocated; recheck the entire live TSV and sidecars immediately before adoption. It is not reserved by this report. `2335` is filth. |
| Modern English headword | earthly |
| PGmc citation, `PROTO` | CAPR-assembled `*érθa-kùnðaz`; preserve the difference between Orel's printed formation and this accented serialization. |
| Selected `PROTOFORM` | `*érθa-kùnðǭ`, weak neuter accusative singular with the source-supported bimoric nasal ending, not the citation nominative. |
| OE `COUNTERPART` | `eorþcunde`, the normalized attested Genesis A 1627 form; distinguish dictionary/edition OCR from an unchecked manuscript reading. |
| Documentary class | Proposed `attested_variant`, under `report_schema.md`'s genuine non-headword OE target policy: an attested poetic inflected cell, not an analogy or dialectal anomaly. Historical regularity is a separate assessment. |
| Historical assessment | A source-supported regular-cell hypothesis requiring independently computed medial prominence; not an already passing production derivation. |
| Stage | `PROTO` and `PROTOFORM` are both PGmc. Since the strings differ, add explicit `entry_stage_metadata.tsv` evidence and the existing `same_stage_pgmc_paradigm_cell` decision, rather than silently inferring a later input stage. |
| Context | Use the existing input-context authority and independently justify the selected citation context. A grammatical-cell choice does not license a suffix-, case- or lexeme-conditioned sound law. |
| Parser | The preferred complete bimoric nasal-ending input is already accepted by the production parser. No parser expansion is required. Private ending diagnostics are not proposals for production coverage. |

The NOTE and lexical apparatus must distinguish the attested inflected cell
from the citation lemma, and distinguish assembled
accent/cell notation from an author's verbatim whole-word reconstruction.
Do not use `late_analogy` merely because an oblique cell was selected: that
class requires an independently supported levelling history.

The regular, unattested genitive fallback would instead use
`PROTOFORM=*érθa-kùnðas`, `COUNTERPART=eorþcundes` and `reconstructed_oe`,
with reconstructed OE typography in prose. That class marks documentary
status, not phonological irregularity. It is not the preferred record.

## Scientific authorisation before inserting a row

The live rule owner is `Germanic/fsts/germanic.txt`; the decision owner is
`Germanic/docs/sound_changes/registry/sc_registry.tsv`. SC040's reader-facing
authority is `Germanic/docs/sound_changes/040-medial-unstressed-u-lowering.md`,
with the existing conditioning dossier and accepted post-migration chronology
reconciliation cited there. A separately authorised ordinary adjudication
would supply `Germanic/docs/sound_changes/audits/sc040-adjudication.md`;
that file and verdict do not exist as a completed decision in this research.

1. Obtain explicit authorisation for the SC040 investigation and the lexical
   admission. Use the real `adjudicate.py SC040 --prepare`, investigation
   preflight and logged controller stages. This lexical research is not a
   fictitious completed SC040 adjudication.
2. Read the current SC040 registry, its cited source authorities and accepted
   post-migration chronology reconciliation. Write the real template-based
   SC040 memorandum if a general prominence correction is approved. Specify
   weight, onset, foot-domain and final-syllable assumptions and test the
   proposed domain, rather than adopting the entire research sensitivity
   suite. The present projection is not a complete OE stress grammar.
3. Retain the inherited-accent stripping operation at its accepted position.
   Temporary computed prominence must remain distinct from inherited accent.
   Do not reopen the accepted histories of world, rainbow or soul.
4. Keep SC065, SC066 and SC068 unchanged. The preferred weak-neuter does not
   require the Oxford ending's experimental r-syncope or the extra final-
   overheavy sensitivity. Those are separate research findings, not a
   prerequisite to deriving this one regular cell.
5. Before changing SOURCE, pin the then-current immutable snapshot and run the
   complete selected population, original 380 inputs, candidate and negative
   controls, intermediate-state comparisons and forward-functionality checks.
   Repeat against the exact intended production definition, not just this
   earlier private projection.
6. Declare the intended source paths and before/after hashes in controlled
   propagation, including the registry, real SC040 memorandum, Foma source,
   lexical data, source apparatus and promised reader-facing documents.
   New SOURCE documents need the controller's explicit new-file declaration.
   Generated, protected and frozen files are not ordinary SOURCE permissions.
   Execute the genuine finalisation entry point and satisfy the fresh
   finalisation preflight and its source-bound receipt.

## Corpus and protected-baseline transition

Only after scientific approval, add the selected cell and its stage/context
evidence through the existing SOURCE owners. Establish an explicitly approved
390-to-391 population extension, preserving all old 390 records, outputs,
standing mismatches and relevant intermediate states. If there is exactly one
new correct witness, the expected result is 391 selected, 383 correct and the
same eight mismatches, not an improvement obtained by removing old rows.

Archive the preceding active baseline through the authorised baseline
procedure, record the exact additional row and fresh evaluator/lexical hashes,
and preserve the immutable original-380 archive and approved selected-input
migrations byte-for-byte. Test both the original-input population and the
active selected-input 380 population; they are not interchangeable.

`--adopt-cell-baseline` validates changes within the same identity population;
it is not permission to append a 391st identity. The population extension
therefore needs its own explicit authorisation and the established baseline
writer's before/after evidence, following the approved filth-extension
precedent. Do not invent a population-adoption CLI option, silently run the
generic writer against protected files, or treat a routine refresh/finalize
as baseline approval. Resolve the exact authorised enrolment procedure before
claiming implementation readiness.

## Scholarly SOURCE and actual publication

1. Extend the reconstruction survey's SOURCE bibliography, diplomatic
   forms/process evidence, consultations, analyses, scoped comparisons and
   rationales. Record printed pages and the source's own notation. Preserve
   the six-token report, recovered passages, unresolved census/access limits,
   preferred Genesis cell, unattested genitive fallback and the alternative
   n-stem-ending prehistory.
2. Use the present census and morphological study as evidence, not as a
   substitute for the required lexical source ledger. Provide a complete
   lexical report with the selected full cell, regular chain, alternative
   attested cells, controls and a companion ledger.
3. The formation, inflection and documentary uncertainty warrant extended
   discussion if publication is promised. First commit an editorial case in
   `pgmc_integration/editorial_cases.tsv`, with actual evidence IDs,
   `requires_extended_discussion=1` and an exact publication path, for example
   `model_entries/2336-earthly-eorþcunde.model.md` if 2336 remains available.
   Do not promise a mature article without that binding SOURCE case.
4. Write and editorially certify the mature model and its
   `model_entries/2336-earthly-eorþcunde.source_ledger.md` companion if that
   identity and target remain selected. Preserve existing literature, distinguish hypothetical forms with
   the book's reconstruction typography, and use the existing report/index
   authorities instead of changing prose to trigger a checker.
5. Regenerate only through `python3 Germanic/tools/adjudicate.py --refresh`;
   `--status` must then report freshness and the promised model publication
   and ledger. Never hand-edit generated indexes, manifests, inventories,
   fingerprints, class volumes or the combined book.
6. Complete genuine Level A focused checks and the prescribed Level B
   integrated refresh/status checks, then both applicable Level C lanes under
   the current `docs/CI_VALIDATION.md` commands and exclusive runtime contract.
   Preserve logs, JUnit evidence, source identity and verified receipts.
7. Build the complete lexical publication, mature class volume and combined
   book through the existing assembly entry point. Verify that the approved
   article and its ledger are present in the actual generated volume, and
   complete the current publication checks. A source file's existence or a
   portable test pass does not certify the finished publication.

No item in this checklist has been performed as production adoption on this
research branch. Research success is grounds for the next controlled decision,
not a bypass around its scientific, baseline or publication gates.
