# Germanic source extraction skill

## Purpose

Use this skill when extracting evidence for OE/Germanic lexeme reports from the
 local repository sources.

## Evidence hierarchy

1. TSV row data (`germanic-aligned-final.tsv`)
2. Known-problems ledger (`oe_known_problems.tsv`)
3. DEV_NOTES section(s)
4. Analysis / dossier markdown
5. Local reference texts in `docs/references/`
6. Local lookup tables (`old_english_wiktionary.tsv`, `old_english_swadesh.tsv`)

## Extraction rules

1. Quote only when the wording is actually present in the local source.
2. Record page numbers / section numbers whenever available.
3. Prefer short paraphrases to long copied passages unless the wording itself
   matters.
4. Keep a clear boundary between repository evidence and your synthesis.
5. If a source lacks a bibliography key, record it in
   `lexeme_reports/missing_bibliography_keys.md`.

## Output expectations

For each lexeme, try to extract:

- reconstruction disagreements;
- source chronology;
- OE philological status;
- project problem/solution history;
- known unresolved points.

