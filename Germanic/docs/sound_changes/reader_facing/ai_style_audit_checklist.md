# AI-style audit checklist: em dashes, colon-lists, and rhetorical negation

Use this checklist when reviewing prose that may have been drafted or heavily
revised with AI. The aim is not to remove every instance mechanically, but to
catch recurring stylistic habits that make the prose sound synthetic,
over-general, or formulaic.

## Scope of the audit

Review the entire document for three patterns:

1. **Em-dash overuse**
2. **Colon followed by a loose or scattershot list**
3. **Rhetorical negation**, especially straw-man contrasts such as `not X, but
   Y`, `not merely X, but Y`, and `rather than X, Y`

For each problem, produce a table with these columns:

| Location | Pattern | Current wording | Why it is a problem | Suggested revision |
|---|---|---|---|---|

Quote the current wording exactly enough for the writer to find it. Do not
rewrite the whole document unless asked; offer targeted substitutions.

## 1. Em-dash overuse

### What to search for

Search for the em dash character:

```text
—
```

Also check for spaced em dashes (` — `), unspaced em dashes (`word—word`), and
malformed combinations such as `word —the`.

### Why it matters

A single em dash can be useful, but repeated em dashes often create a
recognisable AI rhythm: sentence interruption, dramatic qualification, and
parenthetical explanation where ordinary syntax would be better. In formal grant
prose, repeated em dashes can make the argument sound less controlled.

### Revision strategies

Replace the em dash with one of the following, depending on the sentence:

- a comma pair for a light parenthesis
- parentheses for a brief gloss
- a semicolon where two independent clauses are joined
- a full stop followed by a new sentence
- an integrated relative clause
- a simple appositive phrase

### Examples

Problem:

```text
Spelling variants—traditionally known as tōngjiǎ 通假—play a central role...
```

Better:

```text
Spelling variants, traditionally known as tōngjiǎ 通假, play a central role...
```

Problem:

```text
The project evaluates what the evidence can—and cannot—warrant.
```

Better:

```text
The project evaluates the evidential scope and limits of the evidence.
```

## 2. Colon followed by a loose or scattershot list

### What to search for

Search for colons, then inspect whether the colon introduces a loose sequence of
examples, abstractions, or nouns:

```text
:
```

Common patterns:

```text
X includes: A, B, C, and D.
X addresses several issues: A, B, C, D.
The project is about: A, B, C.
```

### Why it matters

AI-generated prose often uses a colon to create the appearance of specificity
while placing loosely related examples after it. This can make prose feel
inflated or under-argued. In grant prose, a colon-list is acceptable when it
introduces a formal numbered list, but it is usually weaker inside a paragraph
unless the list is sharply governed by the preceding claim.

### Revision strategies

- Turn the colon into an ordinary sentence.
- Reduce the list to the two or three items that matter.
- Make the governing relation explicit.
- Use a numbered list only when the structure is genuinely part of the
  argument.
- Replace vague accumulations with a sentence explaining the causal,
  chronological, evidential, or methodological relation among the items.

### Examples

Problem:

```text
The project studies many fruits: apples, almonds, figs, pears, and grapes.
```

Better:

```text
The project focuses on apples and figs, because these two fruits best illustrate the contrast at issue.
```

Problem:

```text
The corpus has three components: manuscripts, received texts, and reference corpora.
```

Better:

```text
The corpus brings manuscript witnesses into direct comparison with received texts and with existing reference works on spelling variants.
```

## 3. Rhetorical negation

### What to search for

Search for the following expressions and inspect the context:

```text
not
not only
not merely
not just
not X but Y
rather than
instead of
cannot
can and cannot
unlike
by contrast
```

Not every negation is bad. Keep factual negation where it is necessary,
especially in ethics or eligibility sections. The problem is rhetorical negation
that sets up an artificial contrast or states a point more dramatically than
necessary.

### Why it matters

AI prose often frames claims as a contrast against a straw man: `not X, but Y`;
`rather than X, the project Y`; `not merely X, but Y`. This can make the
writing sound over-managed and formulaic, especially when the rejected
alternative is not a real position in the field.

### Revision strategies

- State the positive claim directly.
- Name the actual contrast only if it is real and important.
- Replace `can and cannot warrant` with `the evidential scope and limits of`.
- Replace `rather than` with a concrete verb where possible.
- Avoid `not merely/not just` unless the sentence genuinely needs an additive
  contrast.

### Examples

Problem:

```text
The project is not merely a repository, but a research instrument.
```

Better:

```text
The project’s digital environment functions as a research instrument.
```

Problem:

```text
The project treats circularity as a condition to be controlled rather than ignored.
```

Better:

```text
The project makes circularity explicit and builds controls for it into the analysis.
```

## Judgement calls

Leave untouched when the structure is genuinely needed, for example:

- a factual legal or ethical negation: `The project does not involve human participants.`
- a form heading or bibliographic title
- a formal budget list
- a contrast that names a real methodological distinction

Even when a sentence is substantively correct, consider revision if the same
pattern occurs repeatedly nearby.

## Deliverable format

After reviewing the document, provide:

1. A brief count or overview of each pattern.
2. A complete table of substantive instances requiring revision.
3. A short list of instances that were checked but can probably remain.
4. Suggested replacement wording for each problem sentence.
