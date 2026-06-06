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

1. Use short, relevant quotations from both older German and newer
   English-language scholarship where available.
2. Compare how the traditions frame the same phenomenon.
3. Do not overquote; one or two compact quotations per subsection is usually
   enough.

## Formalization

1. Show the actual FOMA definition in a fenced `foma` block.
2. Quote the core rule and only the immediately necessary helper definitions.
3. Explain what the code does in linguistic prose after the code block.

## Chronology

1. Explain chronology with **words and wrong outputs**, not bare `SC###`
   relations.
2. Say what breaks when the change is moved too early or too late.
3. Distinguish real lexical breakpoints from search-boundary limits.

## Numbering

The later reader-facing assembly should enable Pandoc section numbering with
`--number-sections` (or an equivalent metadata setting) instead of relying on
manual workflow prose.
