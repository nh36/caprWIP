# Reader-facing sound-change style guide

This checklist is based on the lexical writing skill and the accepted model
entry `Germanic/docs/lexeme_reports/model_entries/2183-shoulder-sċuldrum.model.md`.

## Structural model

1. Begin with the **historical phenomenon**, not the repository workflow.
2. Keep internal metadata brief and secondary.
3. Use short, functional subsectioning; each section should do one job.
4. Prefer prose paragraphs over status-language bullet lists.

## Rule-level architecture

1. The FOMA rule is the basic reader-facing unit.
2. Grouped introductions are allowed, but individual rule discussions must be
   separate.
3. Each FOMA rule gets one code box.
4. Each code box contains one `define`.
5. Each rule gets a prose equivalent.
6. Rule sections should be labelled for cross-reference.
7. Chronology should refer to rule titles and cross-references, not `SC###`.
8. Internal report numbers and file paths stay out of the chapter body.

## Tone

1. Write as historical-linguistic prose, not as project administration.
2. Use ordinary scholarly titles for the change.
3. Treat reports, dossiers, cards, and code as **evidence tools**, not as the
   subject of the prose.
4. Keep uncertainty explicit; do not inflate residual changes.

## Quotations and comparison

1. Use short, relevant quotations from the most useful scholarship available.
2. Prefer a chronological discussion of individual authors and works.
3. Do not bold quotations.
4. Use inline quotation marks for short quotations and block quotes for longer
   passages.
5. Do not overquote; one or two compact quotations per subsection is usually
   enough.
6. Give a brief translation or gloss after a longer German quotation where it
   helps readability.
7. Compare sources only after explaining what each source actually says.

## Citations

1. Book citations in the reader-facing chapters must include page numbers.
2. Section numbers may follow page numbers when they help the reader.
3. If a page number cannot be verified, paraphrase or replace the passage rather
   than presenting an unverified quotation as final prose.

## Formalization

1. Show the actual FOMA definition in a fenced `foma` block.
2. Each code box should contain one `define`.
3. Explain what the code does in linguistic prose after the code block.
4. The FOMA code box is the one place where the technical implementation should
   be shown directly.

## Chronology

1. Explain chronology with words and wrong outputs, not bare internal
   identifiers.
2. Say what breaks when the change is moved too early or too late.
3. Distinguish real lexical breakpoints from search-boundary limits.
4. Present chronology evidence through lexical consequences, not through file
   references or test-harness language.

## Internal material

1. Internal file paths do not belong in the reader-facing chapters.
2. Internal `SC###` labels should be confined to source notes or maintainer
   metadata.
3. Reports, dossiers, chronology cards, and debug files are evidence tools, not
   the visible subject of the prose.
4. Do not describe whether a sound change “deserves” a chapter or section.
5. Do not call the prose “reader-facing” inside the chapter body.
6. Discuss scope and scale linguistically, not editorially.

## Framing

1. Avoid a mechanical contrast between “German” and “English” traditions.
2. If there is a real intellectual contrast, describe the contrast in terms of
   arguments, chronology, or phonological interpretation rather than language
   alone.
3. Keep implementation details in the formalization section, not in the
   historical discussion.

## AI-style audit rules

1. Avoid repeated em dashes in ordinary prose; prefer commas, parentheses,
   semicolons, or a new sentence.
2. Avoid colon-led loose lists inside prose paragraphs.
3. Avoid formulaic rhetorical negation such as `not merely X, but Y`,
   `not X but Y`, and overused `rather than`.
4. Remove meta-chapter language from the chapter body.
5. Do not describe whether a sound change “deserves” a chapter.
6. Do not call the prose “reader-facing” inside the chapter body.
7. Discuss scale linguistically, not editorially.
8. Keep implementation details in the formalization section.
9. Keep internal identifiers and file references out of the chapter body.
10. Fold “Development of the discussion” into the final paragraph of
    “Historical discussion.”
11. Do not use “Remaining cautions” as a section heading in reader-facing prose.
12. Express chronology temporally, not spatially.
13. Avoid “left edge,” “right edge,” “left-hand,” and “right-hand” in
    chronology prose.
14. In block quotations, keep the citation inside the quoted block.

## Audit command

Run this after drafting or revising a chapter:

```bash
python3 Germanic/docs/sound_changes/reader_facing/check_reader_facing_style.py
```

Use `--strict` only when the chapter is expected to be free of flagged lines.

## Numbering

The later reader-facing assembly should enable Pandoc section numbering with
`--number-sections` (or an equivalent metadata setting) instead of relying on
manual workflow prose.
