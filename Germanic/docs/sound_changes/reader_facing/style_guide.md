# Reader-facing sound-change style guide

This checklist is based on the lexical writing skill and the accepted model
entry `Germanic/docs/lexeme_reports/model_entries/2183-shoulder-sċuldrum.model.md`.

## Structural model

1. Begin with the **historical phenomenon**, not the repository workflow.
2. Keep internal metadata brief and secondary.
3. Use short, functional subsectioning; each section should do one job.
4. Prefer prose paragraphs over status-language bullet lists.

## Pilot section sequence

1. Historical discussion
2. Comparison of the traditions
3. Formalization in the present project
4. Chronological placement
5. Consequences for reconstructed forms
6. Remaining cautions

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
2. Quote the core rule and only the immediately necessary helper definitions.
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

## Numbering

The later reader-facing assembly should enable Pandoc section numbering with
`--number-sections` (or an equivalent metadata setting) instead of relying on
manual workflow prose.
