# OE DEV_NOTES slicing skill

Use this skill when turning `Germanic/docs/DEV_NOTES.md` into lexeme-addressable slice files for Old English rows.

## Model requirement

Use **GPT-5.4** for substantive slicing work. The point of this pass is not cheap summarization but careful separation of current row policy, superseded project history, and cross-lexeme sound-change material.

## Purpose

Create a derived working layer under `Germanic/docs/lexeme_reports/dev_notes_slices/` without editing:

- `Germanic/docs/DEV_NOTES.md`
- `Germanic/data/germanic-aligned-final.tsv`
- `Germanic/data/oe_known_problems.tsv`
- `Germanic/fsts/germanic.txt`
- existing packets, research memos, dossiers, analysis files, or reports

The unit of organization is the **lexical row**, not the DEV_NOTES heading.

## Core workflow

1. Work **top-down through DEV_NOTES**.
2. Map each usable passage to the current OE row state in `Germanic/data/germanic-aligned-final.tsv`.
3. Reuse existing packet or research-memo filename stems where possible.
4. Gather all clearly relevant DEV_NOTES material for that lexical item into one file.
5. If the same DEV_NOTES passage matters for multiple rows, copy it into each relevant row file and record the sharing in `index.tsv`.
6. If a passage is mainly about sound-change behavior or chronology and cannot yet be attached cleanly to a row, move it to `deferred_sound_change_material.md`.
7. If a passage looks lexeme-relevant but cannot yet be attached confidently to a row, move it to `orphan_fragments.md`.

## Evidence policy

- Treat DEV_NOTES as project history, not automatically as current truth.
- Treat evidence packets and research memos as **starting points**, not final authority.
- Always privilege the **live TSV row** for current `PROTO`, `PROTOFORM`, `COUNTERPART`, and `DERIVATION_CLASS`.
- Distinguish carefully between:
  - `PROTO` = cognate-set / etymological headword
  - `PROTOFORM` = row-specific FST input
  - `COUNTERPART` = OE target form for the row
- Mark superseded proposals explicitly instead of silently normalizing them away.

## Output expectations

Each lexeme slice file should include:

- YAML-style metadata
- current row state
- a **detailed** development-note summary that is rich enough to replace repeated return visits to `DEV_NOTES.md` for the basic argument
- source-based fragment references such as `DEV_NOTES:line-63-166`
- explicit status labels (`current`, `superseded`, `diagnostic_only`, etc.)
- concrete open questions for later report work

`index.tsv` should track one row per attached fragment, not just one row per lexeme file.

## Citation and detail requirements

- Default to **more detail, not less**. If a slice still feels like a high-level recap, it is not finished.
- The development-note summary should normally preserve:
  - the regular comparator or expected outcome;
  - the attested or row-target outcome;
  - the philological or morphological issue at stake;
  - the main handbook or source positions;
  - the current project decision;
  - any important superseded detour that later report writers would otherwise have to rediscover.
- Any paragraph that makes a concrete source-based claim should normally carry an explicit citation.
- When DEV_NOTES preserves a useful direct quotation from a handbook, dictionary, or primary-source discussion, prefer carrying that quotation over replacing it with a bare paraphrase.
- Do not collapse several distinct source claims into one vague sentence with a single trailing citation if the note can reasonably preserve who says what.
- If the current row policy depends on a later correction, probe, or reversal in DEV_NOTES, state that explicitly and cite the correcting note.
- If a fragment is mainly valuable because it preserves project chronology, say what the abandoned proposal was and why it is no longer current.
- Prefer explicit contrastive formulations such as `regular X`, `attested Y`, `superseded proposal Z`, rather than implicit summary language.

## Reference and index hygiene

- Use **line-based fragment refs** in slice files and `index.tsv`, e.g. `DEV_NOTES:line-25940-26067`.
- Do not leave final fragment refs in `DEV_NOTES:section-...` form unless a line-based ref is genuinely impossible.
- Source headings may be descriptive, but the prose should stand alone and not depend on section-number shorthand.
- Keep `index.tsv` rows structurally valid:
  - preserve the exact column order;
  - keep controlled-value fields such as `recommended_next_use` to their allowed values;
  - do not accidentally spill an expanded summary into the wrong column.
- When a slice file is rewritten, update the matching `index.tsv` rows in the same pass so fragment refs, source headings, and summaries stay synchronized.

## Style

- Do not write autobiographically.
- Do not turn this into the final lexeme report.
- Keep project chronology, but label it as chronology.
- Be conservative: when attachment is doubtful, defer or orphan rather than force.
- Treat the slice file as a **replacement working note**, not as a pointer back to the old note.
- Do **not** rely on phrases like "this section argues" or "the subsection below says". Preserve source line hints in metadata, but write the prose so it stands on its own.
- When DEV_NOTES already contains direct quotations from primary sources or handbook sources and those quotations remain current, **carry them over** into the fragment text instead of reducing everything to high-level paraphrase.
- Fragment text should normally include:
  - the concrete problem being discussed;
  - the specific source claims and quotations that matter;
  - the project decision or later correction;
  - whether the material is current, superseded, or diagnostic only.
- Use the repo's pandoc/LaTeX-friendly citation keys from `docs/refs.bib`, e.g. `[@Campbell1959, §210.1]`, `[@Kroonen2013, p. 220]`, `[@RingeTaylor2014, p. 322]`.
- When a page, section, or note number is available in DEV_NOTES or the dossier material, include it in the citation rather than citing the work bare.
- For dense or philologically messy items, work in small batches of **3-4 rows at a time** so the slice files stay careful and specific rather than schematic.
