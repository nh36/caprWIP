# OE lexeme research memo skill

## Purpose

Use this skill when preparing an intermediate research memo for an Old English
lexeme row. A research memo is not the final `### Lexeme report`; it is the
stage between the evidence packet and the eventual publishable lexeme report.

## Core principle

The evidence packet is a **starting dossier, not the final evidence base**.
Treat it as a guide to likely issues, files, and prior discussion. Before making
recommendations, do additional repository research and record what was checked.

## Model requirement

For substantive memo drafting or revision, delegated agents must use
**GPT-5.4** (`gpt-5.4`), matching the supervising session model. Do not use a
cheaper or faster fallback model for Old English lexeme research memos; the
memo stage is part of the evidential workflow and needs the higher-quality
reasoning pass.

## Required workflow

1. Start from the aligned TSV row and the packet for the exact row ID.
2. Audit the packet:
   - what is authoritative/current;
   - what is useful background;
   - what is stale, superseded, or diagnostic only;
   - what is irrelevant or misleading.
3. Search beyond the packet:
   - `Germanic/docs/DEV_NOTES.md`
   - any dossier or analysis file named in the packet or TSV note
   - `Germanic/data/oe_known_problems.tsv` when relevant
   - lexical tables and other repo materials if they clarify attestation,
     paradigm cells, or headword issues
4. Distinguish clearly between:
   - the cognate-set headword / etymological proto;
   - the project input form used for derivation;
   - the Old English target form actually represented by the row.
5. End with recommendations, not final prose.

## Research memo index

Track memo progress in:

- `Germanic/docs/lexeme_reports/research_memo_index.tsv`

Use these columns:

- `ID`
- `CONCEPT`
- `COUNTERPART`
- `DERIVATION_CLASS`
- `PACKET_PATH`
- `MEMO_PATH`
- `STATUS`
- `NEEDS_PARADIGM_PROBE`
- `DATA_CHANGE_RECOMMENDED`
- `DATA_CHANGE_KIND`
- `READY_FOR_FINAL_REPORT`
- `NOTES`

For `DATA_CHANGE_KIND`, use only:

- `none`
- `tsv_note`
- `tsv_protoform`
- `tsv_counterpart`
- `derivation_class`
- `known_problems_refs`
- `dev_notes_cleanup`
- `dossier_cleanup`
- `multiple`

## Four-agent round workflow

The memo workflow runs in **four-agent rounds**, with at most four memos in a
round. Do not begin a new round until the previous round has been reviewed.

Use these lanes as a preference order:

1. **Lane 1: unresolved/unmodelled**
   - `unexplained_unmodelled`
   - `known_unmodelled`
2. **Lane 2: philological special cases**
   - `reconstructed_oe`
   - `attested_variant`
3. **Lane 3: paradigm-cell cases**
   - `late_analogy`
4. **Lane 4: lighter but still note-bearing**
   - `regular` rows with non-empty `NOTE`
   - `early_analogy`

Selection rule for each round:

1. First try to choose one row from each lane.
2. If one or more lanes are exhausted, refill the empty slots from the
   remaining required memo backlog.
3. When refilling, prefer higher-risk categories first:
   - unmodelled rows;
   - reconstructed or attested-variant rows;
   - late-analogy rows;
   - early-analogy rows;
   - regular rows with `NOTE`.
4. Avoid assigning four rows of the same narrow type in a single round unless
   the backlog has become mostly that type.
5. If the backlog is mostly one type, it is acceptable for a round to contain
   mostly or entirely that type, but the batch summary should say so explicitly.

For each memo in a round:

1. Start from the evidence packet.
2. Do additional repo research beyond the packet.
3. Distinguish current evidence from stale project history.
4. Identify whether a paradigm probe is required.
5. Make explicit data-change recommendations.
6. Update `research_memo_index.tsv`.

Before launching delegated memo agents for a round, generate or refresh the
starting evidence packets for the selected rows. Agents should begin from live
packet files, not from stale packet snapshots or from TSV-only context.

After each four-memo round, stop and write a batch summary under
`Germanic/docs/lexeme_reports/research_memos/` before any later round begins.

## Required memo structure

Use exactly these headings:

- `# Research memo — ID concept / counterpart`
- `## Starting point`
- `## Packet evidence assessment`
- `## Additional repo research`
- `## Reconstruction and early-stage forms`
- `## Old English philology`
- `## Project problem and solution`
- `## Paradigm probe`
- `## Recommended final report`
- `## Data-change recommendations`

## Memo content rules

1. In `## Starting point`, summarize:
   - `ID`
   - `CONCEPT`
   - `COUNTERPART`
   - `PROTO`
   - `PROTOFORM`
   - `DERIVATION_CLASS`
   - `NOTE`
2. In `## Packet evidence assessment`, say explicitly which packet material is:
   - authoritative/current;
   - useful background;
   - stale or superseded;
   - irrelevant or misleading.
3. In `## Additional repo research`, list the files checked beyond the packet,
   especially any full dossier named in the packet or TSV note.
4. In `## Reconstruction and early-stage forms`, explain any disagreement or
   choice involving `PROTO`, `PROTOFORM`, PGmc, PWGmc, NWGmc, Anglo-Frisian, or
   OE staging.
5. In `## Old English philology`, distinguish:
   - attested vs reconstructed;
   - citation form vs inflected form;
   - dialect or manuscript status, if actually supported;
   - dictionary/headword issues, if relevant.
6. In `## Project problem and solution`, explain the project-specific issue and
   what the current row is intended to represent.
7. In `## Paradigm probe`, say whether a probe is required; if missing, specify
   which cells should be probed.
8. In `## Recommended final report`, give only a concise recommendation for the
   eventual `### Lexeme report`. Do **not** draft the final report unless
   explicitly asked.
9. In `## Data-change recommendations`, say whether any of these should change:
   - TSV `PROTO`
   - TSV `PROTOFORM`
   - TSV `COUNTERPART`
   - TSV `DERIVATION_CLASS`
   - TSV `NOTE`
   - `oe_known_problems.tsv`
   - `DEV_NOTES` or dossier text

## Output expectations

Good research memos are:

- source-aware rather than packet-bound;
- explicit about uncertainty and project chronology;
- careful about stale evidence;
- suitable as the direct substrate for a later lexeme report.

Bad research memos:

- merely paraphrase the packet;
- treat stale project history as current evidence;
- collapse attested forms, reconstructed forms, and modelling inputs together;
- prematurely write polished `### Lexeme report` prose.
