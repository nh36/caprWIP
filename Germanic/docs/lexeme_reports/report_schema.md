# Old English lexeme-report schema

## Purpose

This schema defines the **lexeme-level research report** that will replace the
flat `NOTE:` line in the generated Old English derivation report.

The TSV `NOTE` and `HISTORY` fields remain source material. They are not the
final prose.

## Entry structure inside the generated derivation report

Each generated OE entry should eventually follow this structure:

```md
# concept

PROTO: ...
EXPECTED: ...
OUTPUTS: ...
DERIVATION_CLASS: ...

### Proto-Germanic consonant inheritance

...

| Earlier Germanic developments | Old English developments |
|:---|:---|
| ... | ... |

### Orthography & surface

...

### Lexeme report

#### Reconstruction and early-stage alternatives
...

#### Chronological source dossier
...

#### Old English philology
...

#### Project problem and solution
...

#### Paradigm probe
...
```

`#### Paradigm probe` is included only when relevant, especially for
`late_analogy` and analogical `known_unmodelled` cases.

## Citation convention

- Use **pandoc-style citations**: `[@Kroonen2013]`,
  `[@Campbell1959, §547]`, `[@RingeTaylor2014, p. 385]`.
- Bibliography keys must come from `docs/refs.bib`.
- If a needed source lacks a key, record it in
  `Germanic/docs/lexeme_reports/missing_bibliography_keys.md`.
- Do **not** invent a bibliography key silently in report prose.

## Evidence vs inference

Each lexeme report must distinguish:

- **Evidence:** what the TSV, local references, dictionaries, ledgers, and
  DEV_NOTES actually say.
- **Inference:** what the project concludes from that evidence.

Practical rule:

- Use declarative sentences for source-backed facts.
- Use explicit signals such as “the project infers”, “the working hypothesis
  is”, “the report treats”, or “the chosen FST input assumes” when moving from
  evidence to project reasoning.

Do not claim:

- that an OE form is attested unless a source supports attestation;
- that a dialect label is secure unless a source supports it;
- that a form is regular if the repo treats it as analogical or unresolved.

## Section-by-section guidance

### `#### Reconstruction and early-stage alternatives`

This section compares the forms used in:

- `PROTO`
- `PROTOFORM`
- TSV `NOTE`
- TSV `HISTORY`
- `oe_known_problems.tsv` if relevant
- DEV_NOTES / analysis dossiers if relevant
- local reference works

It should name concrete disagreements, for example:

- root-vowel disagreement
- stem-class disagreement
- gender disagreement
- suffix disagreement
- paradigm-cell disagreement
- wrong lexeme / extraction garbage
- attested OE target vs reconstructed OE target

### `#### Chronological source dossier`

This is a curated dossier, not a long essay. Use short blocks arranged by
source chronology where practical. Each item should identify:

- source,
- year or publication chronology,
- page or section,
- and the specific relevance to the lexeme or sound change.

Short paraphrases are acceptable when no exact quotation is being copied.
Do not fabricate quotations.

### `#### Old English philology`

This section records:

- attested vs reconstructed status,
- dictionary headword(s),
- spelling variants,
- dialectal labels,
- manuscript / glossary / poetic / normalized status when known,
- whether the project intentionally targets a non-default form.

### `#### Project problem and solution`

This section is keyed to `DERIVATION_CLASS`.

#### `regular`

- Keep it brief.
- State that the citation protoform and the deterministic FST path produce the
  OE target.
- Mention only non-obvious regular sound changes if they matter.

#### `early_analogy`

- Explain why the citation Proto-Germanic form was not the right FST input.
- Identify the later stem / class / stage chosen as `PROTOFORM`.
- Explain why that choice is philologically defensible.

#### `late_analogy`

- Identify the citation form and the selected paradigm cell.
- Explain why the ordinary citation form fails to reach the attested OE target.
- Explain how the chosen cell reaches the target lautgesetzlich.
- State what analogical spread or leveling is being hypothesized.

#### `attested_variant`

- Explain why the FST output is a genuine OE form but not the default headword.
- Identify dialect, date, register, or manuscript context if known.

#### `reconstructed_oe`

- State explicitly that the target is reconstructed rather than directly
  attested.
- Explain why the reconstruction is useful to the project.

#### `known_unmodelled`

- Explain the understood historical/analogical process.
- Explain why the deterministic FST does not model it directly.
- Identify what the FST produces and why the attested target differs.

#### `unexplained_unmodelled`

- Explain the regular FST output.
- Explain the attested OE target.
- Summarize why the repo does not currently have a satisfactory explanation.

#### `lexeme_retarget`

- Explain the old and new etymon or cognate assignment.
- State why the new alignment is better.

## Paradigm probe policy

Include `#### Paradigm probe` when:

- the row is `late_analogy`;
- the row is an analogical `known_unmodelled` case;
- or the report’s argument depends on comparing multiple paradigm-cell inputs.

Each probe should record:

- generated cells,
- omitted cells and why,
- whether morphology was hand-specified or template-generated,
- whether ProtoGate was bypassed,
- whether the winning form is unique.

## Placeholder policy before full integration

Before every row has a finished lexeme report, entries without a completed
report should receive:

```md
### Lexeme report

#### Project note

Original TSV note: ...
```

The original `NOTE` content must be preserved here. Do not silently drop it.

## Validation rules

The generation workflow should enforce:

1. Every OE row with a non-empty TSV `NOTE` has either a full lexeme report or
   a placeholder preserving the note.
2. Every `late_analogy` row has either a paradigm probe or an explicit reason
   why no probe was generated.
3. Every `known_unmodelled` and `unexplained_unmodelled` row cites
   `oe_known_problems.tsv` or a corresponding DEV_NOTES / analysis source.
4. Every citation key used in report prose exists in `docs/refs.bib`.
5. Generated output contains no unresolved placeholders such as `TODO`,
   `FIXME`, `citation needed`, or `???`, except in a separate audit report.
6. The generated lexeme report must not alter `PROTO`, `EXPECTED`, `OUTPUTS`,
   or the derivation trace/table itself.

## LaTeX-friendly Markdown rules

- Use short subsections rather than very long Markdown tables.
- Avoid deeply nested bullet lists.
- Avoid raw HTML except the already-established `<br>` in compact trace tables.
- Keep reconstructed forms in plain text with a leading asterisk.
- Do not use Markdown emphasis around reconstructed forms when it risks
  clashing with the initial asterisk.
- Do not place citations inside code blocks.
- Prefer normal prose paragraphs and short bullet lists over prose embedded in
  tables.

