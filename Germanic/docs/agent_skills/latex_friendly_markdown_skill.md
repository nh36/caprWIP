# LaTeX-friendly Markdown skill

## Purpose

Use this skill when writing Markdown that is expected to convert later into a
LaTeX article or report.

## Rules

1. Use plain heading levels rather than deeply nested bullet lists.
2. Avoid raw HTML except established table-internal `<br>` line breaks.
3. Keep prose out of large Markdown tables unless the table is genuinely the
   best structure.
4. Use pandoc-style bibliography citations `[@Key]`.
5. Keep reconstructed forms as plain text with a leading asterisk.
6. Do not italicize reconstructed forms if the asterisk would become ambiguous.
7. Do not put citations inside code blocks.
8. Prefer short paragraphs and explicit subsection headings.

## For lexeme reports

- Use subsections for philology and source dossiers.
- Keep tables narrow and mechanical.
- Put long discussion in prose sections, not inside tables.

