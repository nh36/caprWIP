# Production batch 06 report

## Whether any eligible P1 rows remained

- Yes. A pre-selection pass over
  `Germanic/docs/lexeme_reports/production_backlog.tsv` found **9** remaining
  eligible rows with:
  - `PRIORITY_TIER = P1_nonregular_missing_production`
  - `PRODUCTION_STATUS = none`
  - `SOURCE_MATERIAL_STATUS = source_material_available`
  - no pre-existing `.model.md` entry in
    `Germanic/docs/lexeme_reports/model_entries/`
- Batch 06 therefore absorbs those 9 P1 rows first, then adds the first
  eligible P2 regular-with-note row to reach a total batch size of 10.

## Entries selected

The following 10 entries were selected from
`Germanic/docs/lexeme_reports/production_backlog.tsv` using these criteria:

- pre-selection check for any remaining eligible P1 rows;
- if eligible P1 rows remained, select them first;
- otherwise use `PRIORITY_TIER = P2_regular_with_note_missing_production`;
- `PRODUCTION_STATUS = none`;
- `SOURCE_MATERIAL_STATUS = source_material_available`;
- no pre-existing `.model.md` entry in
  `Germanic/docs/lexeme_reports/model_entries/`;
- source-material paths verified before drafting.

Selected entries:

1. `2310 make (3sg) / macaþ` — `PROTOFORM *mákōθi` —
   `late_analogy` — `NOTE_PRESENT yes` — source paths:
   `dev_notes_slices/2310-make-(3sg)-macaþ.md`,
   `packets/2310-make-(3sg)-macaþ.md`,
   `research_memos/2310-make-(3sg)-macaþ.md`
2. `2311 bore (iptv.2sg) / bora` — `PROTOFORM *búrô` —
   `late_analogy` — `NOTE_PRESENT yes` — source paths:
   `dev_notes_slices/2311-bore-(iptv.2sg)-bora.md`,
   `packets/2311-bore-(iptv.2sg)-bora.md`,
   `research_memos/2311-bore-(iptv.2sg)-bora.md`
3. `2312 bore (3sg) / boraþ` — `PROTOFORM *búrōθi` —
   `late_analogy` — `NOTE_PRESENT yes` — source paths:
   `dev_notes_slices/2312-bore-(3sg)-boraþ.md`,
   `research_memos/2312-bore-(3sg)-boraþ.md`
4. `2313 learn (iptv.2sg) / liorna` — `PROTOFORM *líznô` —
   `late_analogy` — `NOTE_PRESENT yes` — source paths:
   `dev_notes_slices/2313-learn-iptv-2sg-liorna.md`,
   `research_memos/2313-learn-(iptv.2sg)-liorna.md`,
   `research_memos/batch_12_summary.md`
5. `2314 learn (3sg) / liornaþ` — `PROTOFORM *líznōθi` —
   `late_analogy` — `NOTE_PRESENT yes` — source paths:
   `dev_notes_slices/2314-learn-(3sg)-liornaþ.md`,
   `research_memos/2314-learn-(3sg)-liornaþ.md`
6. `2315 lick (iptv.2sg) / licca` — `PROTOFORM *líkkô` —
   `late_analogy` — `NOTE_PRESENT yes` — source paths:
   `dev_notes_slices/2315-lick-iptv-2sg-licca.md`,
   `packets/2315-lick-(iptv.2sg)-licca.md`,
   `research_memos/2315-lick-(iptv.2sg)-licca.md`,
   `research_memos/batch_13_summary.md`
7. `2316 lick (3sg) / liccaþ` — `PROTOFORM *líkkōθi` —
   `late_analogy` — `NOTE_PRESENT yes` — source paths:
   `dev_notes_slices/2316-lick-(3sg)-liccaþ.md`,
   `research_memos/2316-lick-(3sg)-liccaþ.md`
8. `2317 show (iptv.2sg) / sċēawa` — `PROTOFORM *skáwô` —
   `late_analogy` — `NOTE_PRESENT yes` — source paths:
   `dev_notes_slices/2317-show-(iptv.2sg)-sċēawa.md`,
   `packets/2317-show-(iptv.2sg)-sċēawa.md`,
   `research_memos/2317-show-(iptv.2sg)-sċēawa.md`
9. `2318 show (3sg) / sċēawaþ` — `PROTOFORM *skáwōθi` —
   `late_analogy` — `NOTE_PRESENT yes` — source paths:
   `dev_notes_slices/2318-show-(3sg)-sċēawaþ.md`,
   `research_memos/2318-show-(3sg)-sċēawaþ.md`,
   `research_memos/batch_14_summary.md`
10. `1934 bake / bacan` — `PROTOFORM *bákaną` — `regular` —
    `NOTE_PRESENT yes` — source paths:
    `dev_notes_slices/1934-bake-bacan.md`,
    `packets/1934-bake-bacan.md`,
    `research_memos/1934-bake-bacan.md`

## Entries skipped and why

- None. The 9 remaining eligible P1 rows were all drafted, and the first
  eligible P2 row (`1934 bake / bacan`) was then used to bring the batch to 10.

## Files created

- `2310 make (3sg) / macaþ`
  - `Germanic/docs/lexeme_reports/model_entries/2310-make-(3sg)-macaþ.source_ledger.md`
  - `Germanic/docs/lexeme_reports/model_entries/2310-make-(3sg)-macaþ.model.md`
  - `Germanic/docs/lexeme_reports/model_entries/2310-make-(3sg)-macaþ.reviewer_checklist.md`
  - `Germanic/docs/lexeme_reports/model_entries/2310-make-(3sg)-macaþ.model_implementation_report.md`
- `2311 bore (iptv.2sg) / bora`
  - `Germanic/docs/lexeme_reports/model_entries/2311-bore-(iptv.2sg)-bora.source_ledger.md`
  - `Germanic/docs/lexeme_reports/model_entries/2311-bore-(iptv.2sg)-bora.model.md`
  - `Germanic/docs/lexeme_reports/model_entries/2311-bore-(iptv.2sg)-bora.reviewer_checklist.md`
  - `Germanic/docs/lexeme_reports/model_entries/2311-bore-(iptv.2sg)-bora.model_implementation_report.md`
- `2312 bore (3sg) / boraþ`
  - `Germanic/docs/lexeme_reports/model_entries/2312-bore-(3sg)-boraþ.source_ledger.md`
  - `Germanic/docs/lexeme_reports/model_entries/2312-bore-(3sg)-boraþ.model.md`
  - `Germanic/docs/lexeme_reports/model_entries/2312-bore-(3sg)-boraþ.reviewer_checklist.md`
  - `Germanic/docs/lexeme_reports/model_entries/2312-bore-(3sg)-boraþ.model_implementation_report.md`
- `2313 learn (iptv.2sg) / liorna`
  - `Germanic/docs/lexeme_reports/model_entries/2313-learn-(iptv.2sg)-liorna.source_ledger.md`
  - `Germanic/docs/lexeme_reports/model_entries/2313-learn-(iptv.2sg)-liorna.model.md`
  - `Germanic/docs/lexeme_reports/model_entries/2313-learn-(iptv.2sg)-liorna.reviewer_checklist.md`
  - `Germanic/docs/lexeme_reports/model_entries/2313-learn-(iptv.2sg)-liorna.model_implementation_report.md`
- `2314 learn (3sg) / liornaþ`
  - `Germanic/docs/lexeme_reports/model_entries/2314-learn-(3sg)-liornaþ.source_ledger.md`
  - `Germanic/docs/lexeme_reports/model_entries/2314-learn-(3sg)-liornaþ.model.md`
  - `Germanic/docs/lexeme_reports/model_entries/2314-learn-(3sg)-liornaþ.reviewer_checklist.md`
  - `Germanic/docs/lexeme_reports/model_entries/2314-learn-(3sg)-liornaþ.model_implementation_report.md`
- `2315 lick (iptv.2sg) / licca`
  - `Germanic/docs/lexeme_reports/model_entries/2315-lick-(iptv.2sg)-licca.source_ledger.md`
  - `Germanic/docs/lexeme_reports/model_entries/2315-lick-(iptv.2sg)-licca.model.md`
  - `Germanic/docs/lexeme_reports/model_entries/2315-lick-(iptv.2sg)-licca.reviewer_checklist.md`
  - `Germanic/docs/lexeme_reports/model_entries/2315-lick-(iptv.2sg)-licca.model_implementation_report.md`
- `2316 lick (3sg) / liccaþ`
  - `Germanic/docs/lexeme_reports/model_entries/2316-lick-(3sg)-liccaþ.source_ledger.md`
  - `Germanic/docs/lexeme_reports/model_entries/2316-lick-(3sg)-liccaþ.model.md`
  - `Germanic/docs/lexeme_reports/model_entries/2316-lick-(3sg)-liccaþ.reviewer_checklist.md`
  - `Germanic/docs/lexeme_reports/model_entries/2316-lick-(3sg)-liccaþ.model_implementation_report.md`
- `2317 show (iptv.2sg) / sċēawa`
  - `Germanic/docs/lexeme_reports/model_entries/2317-show-(iptv.2sg)-sċēawa.source_ledger.md`
  - `Germanic/docs/lexeme_reports/model_entries/2317-show-(iptv.2sg)-sċēawa.model.md`
  - `Germanic/docs/lexeme_reports/model_entries/2317-show-(iptv.2sg)-sċēawa.reviewer_checklist.md`
  - `Germanic/docs/lexeme_reports/model_entries/2317-show-(iptv.2sg)-sċēawa.model_implementation_report.md`
- `2318 show (3sg) / sċēawaþ`
  - `Germanic/docs/lexeme_reports/model_entries/2318-show-(3sg)-sċēawaþ.source_ledger.md`
  - `Germanic/docs/lexeme_reports/model_entries/2318-show-(3sg)-sċēawaþ.model.md`
  - `Germanic/docs/lexeme_reports/model_entries/2318-show-(3sg)-sċēawaþ.reviewer_checklist.md`
  - `Germanic/docs/lexeme_reports/model_entries/2318-show-(3sg)-sċēawaþ.model_implementation_report.md`
- `1934 bake / bacan`
  - `Germanic/docs/lexeme_reports/model_entries/1934-bake-bacan.source_ledger.md`
  - `Germanic/docs/lexeme_reports/model_entries/1934-bake-bacan.model.md`
  - `Germanic/docs/lexeme_reports/model_entries/1934-bake-bacan.reviewer_checklist.md`
  - `Germanic/docs/lexeme_reports/model_entries/1934-bake-bacan.model_implementation_report.md`
- Batch report
  - `Germanic/docs/lexeme_reports/model_entries/production_batch_06_report.md`

## Checklist results

| Entry | Result |
| :--- | :--- |
| `2310 make (3sg) / macaþ` | pass with caveat |
| `2311 bore (iptv.2sg) / bora` | pass with caveat |
| `2312 bore (3sg) / boraþ` | pass with caveat |
| `2313 learn (iptv.2sg) / liorna` | pass with caveat |
| `2314 learn (3sg) / liornaþ` | pass with caveat |
| `2315 lick (iptv.2sg) / licca` | pass with caveat |
| `2316 lick (3sg) / liccaþ` | pass with caveat |
| `2317 show (iptv.2sg) / sċēawa` | pass with caveat |
| `2318 show (3sg) / sċēawaþ` | pass with caveat |
| `1934 bake / bacan` | pass |

## Significant human-review issues

1. `2310 make (3sg) / macaþ` — `macaþ` is a normalized finite paradigm form,
   while the ordinary dictionary headword is `macian`.
2. `2311 bore (iptv.2sg) / bora` — `bora` is a normalized imperative paradigm
   form, not the ordinary lemma; later promotion should keep it distinct from
   `borian`.
3. `2312 bore (3sg) / boraþ` — `boraþ` is a normalized 3sg form, not a
   headword, and should stay distinct from the bore-family lemma row.
4. `2313 learn (iptv.2sg) / liorna` — the entry intentionally privileges an
   attested Northumbrian finite form over the more familiar dictionary headword
   `leornian`.
5. `2314 learn (3sg) / liornaþ` — the selected 3sg form is normalized from
   attested `liorn-` evidence and should remain carefully labeled as such.
6. `2315 lick (iptv.2sg) / licca` — `licca` remains a selected imperative form
   beside the headword `liccian`, and the finite-cell comparison is manual.
7. `2316 lick (3sg) / liccaþ` — `liccaþ` remains a selected 3sg form beside
   the headword `liccian`, and the row metadata still needs the finite-cell vs
   lexeme-level distinction kept explicit.
8. `2317 show (iptv.2sg) / sċēawa` — the final prose must keep attested source
   spelling `scēawa` distinct from normalized `sċēawa`.
9. `2318 show (3sg) / sċēawaþ` — the strongest local 3sg evidence is prefixed
   `-sceawað`, so the normalized simplex comparator `sċēawaþ` must stay
   carefully labeled.

## Citation-key problems

- None found in the final `.model.md` entries.

## OCR/encoding or source-transcription issues found

- `2313 learn (iptv.2sg) / liorna` and `2314 learn (3sg) / liornaþ` —
  Brunner's plain-text OCR is noisy around the relevant finite forms, so the
  cited passages were cross-checked against the local vision transcription.
- `2317 show (iptv.2sg) / sċēawa` and `2318 show (3sg) / sċēawaþ` — Bright's
  finite-form evidence was checked in the cleaner local vision-backed material;
  no corrective rewriting was needed in final prose.
- `2310`, `2311`, `2312`, `2315`, `2316`, and `1934` did not require corrective
  rewriting for OCR or encoding artifacts in final prose.

## Google Vision consultation

- Google Vision or equivalent local vision transcriptions were consulted where
  useful for the finite-form rows, especially:
  - Brunner for `2313` and `2314`;
  - Bright for `2317` and `2318`;
  - existing local vision transcriptions for the cited make/bore material.
- Those checks were used to confirm cleaner source readings in support
  documents.
- No unresolved OCR artifact remains in the final `.model.md` entries.

## Source-material sufficiency

- Source material was sufficient for all 10 selected entries.
- Some rows did not have every local support-file type, but each retained enough
  packet/dev-note/memo/reference coverage to support drafting without adding new
  source files.

## Entries that should not be scaled from without human review

- `2310 make (3sg) / macaþ`
- `2311 bore (iptv.2sg) / bora`
- `2312 bore (3sg) / boraþ`
- `2313 learn (iptv.2sg) / liorna`
- `2314 learn (3sg) / liornaþ`
- `2315 lick (iptv.2sg) / licca`
- `2316 lick (3sg) / liccaþ`
- `2317 show (iptv.2sg) / sċēawa`
- `2318 show (3sg) / sċēawaþ`

These nine late-analogy finite-cell rows remain review-sensitive because each
depends on a selected imperative or 3sg comparison form rather than the ordinary
lemma.

## Style issues noticed across the batch

- This batch mixes 9 finite-cell `late_analogy` rows with 1 `regular`-with-note
  row. The compact style for `1934 bake / bacan` should be preserved rather
  than inflating it to match the finite-cell entries.
- The final `.model.md` files were scanned for batch-level banned phrasing and
  OCR/project-facing language. One formulaic line in the initial draft set was
  revised away before completion.
- No unresolved OCR or encoding artifact remains in final prose.

## Scope confirmation

- No TSV, FST, manifest, packet, memo, bibliography, derivation trace, existing
  model entry, writing-skill file, or existing pilot report was changed.
