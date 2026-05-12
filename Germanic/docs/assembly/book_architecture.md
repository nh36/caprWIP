# Germanic Lexeme Reports: Lexical Derivation Volume

## Purpose of this document

This is a **design document**, not final front matter. It sets out the planned
architecture for a full lexical derivation volume built from the current
Germanic `.model.md` corpus and the compact derivation-trace report, while
keeping the later sound-change volume or report separate.

The current assembly layer is mature enough to support a full lexical-volume
alpha:

- generated derivation summary under each headword
- boxed derivation trace
- model-entry prose below the trace
- live bibliography citations
- Unicode-safe PDF path

The remaining architectural task is to order the full corpus coherently by
derivation class and to supply volume-level framing around the individual
entries.

## Proposed volume title

**Germanic Lexeme Reports: Lexical Derivation Volume**

This title keeps the book aligned with the existing lexeme-report corpus while
marking it as a publication-format synthesis rather than a folder of separate
row files.

## Front matter / introductory chapters

### 1. Introduction

Purpose:

- explain what the project is
- define what this lexical volume covers
- distinguish this lexical volume from any later sound-change volume or
  rule-ordering report
- explain what counts as a lexical derivation report in the current project

Planned content:

- the project models derivational pathways from selected Proto-Germanic or
  pre-Old-English inputs to Old English targets
- the lexical volume assembles row-level reports, not the whole transducer
  implementation history
- the lexical volume is word-centered, while the later sound-change volume can
  be rule-centered

### 2. Data and sources

Purpose:

- define the source stack used for the lexical entries
- explain how comparative and Old English evidence are cited
- record the current citation policy for the assembled book

Planned content:

- Germanic aligned dataset as the current lexical data layer
- Old English target forms from the row-level model-entry corpus
- comparative dictionaries
- Old English dictionaries
- historical grammars
- citation policy, including the fact that some citations remain honestly broad
  rather than page-saturated

### 3. Transducer and derivation method

Purpose:

- explain what the derivation trace shows
- explain why the trace is split into Earlier Germanic changes and Old English
  changes
- define the key labels used in the generated summary and trace presentation

Planned content:

- what “citation reconstruction” means
- what “selected input” means
- what “transducer output” means
- what “selected target” means
- how to read the boxed derivation trace

### 4. Derivation classes

Purpose:

- explain why the catalogue is divided by derivation class rather than presented
  as one undifferentiated alphabetical list
- give the reader the interpretive frame for each section

Planned class chapters:

1. **Regular**
2. **Attested variants and selected comparison forms**
3. **Early analogy / pre-Old-English input selection**
4. **Late analogy / paradigm-cell selection**
5. **Reconstructed Old English comparators**
6. **Known but unmodelled remodellings**
7. **Unexplained or deliberately unmodelled exceptions**

## Main lexical catalogue

The main catalogue should be divided into seven parts in this order:

### Part I. Regular derivations

These entries form the baseline of the lexical volume. The selected input and
selected Old English target stand in a straightforward relation under the
current cascade.

### Part II. Attested variants and selected comparison forms

These entries treat the chosen Old English target as one member of an attested
or historically documented variant set. The lexical problem is not that the
target is arbitrary, but that the comparison must be framed against a documented
variant network rather than against a single isolated citation form.

### Part III. Early analogy and pre-Old-English input selection

These entries require a distinction between the lexeme-level reconstruction and
the pre-Old-English form selected as input to the derivation. The special step
is upstream of Old English.

### Part IV. Late analogy and paradigm-cell selection

These entries are best explained through a conservative finite form, an
inflectional cell, or another later analogical comparison rather than through
the citation form alone.

### Part V. Reconstructed Old English comparators

These entries use an explicitly reconstructed Old English-stage comparator for
the branch being modelled. The relevant comparison is therefore later than the
Proto-Germanic citation form but still belongs to the lexical derivation layer.

### Part VI. Known but unmodelled remodellings

These entries preserve cases where the historical remodelling is understood, but
the current deterministic transducer does not model the later reshaping that
produced the selected Old English target.

### Part VII. Unexplained or deliberately unmodelled exceptions

These entries retain a mismatch between regular transducer output and selected
Old English target and should be carried as documented exceptions rather than as
evidence for further rule repair in the lexical volume.

## Ordering principles

### Catalogue order

- order the main parts by derivation class:
  1. regular
  2. attested variant
  3. early analogy
  4. late analogy
  5. reconstructed Old English comparator
  6. known but unmodelled remodelling
  7. unexplained / unmodelled
- order entries within each part by numeric row ID
- break ties lexicographically by filename if needed

### Heading hierarchy

Proposed hierarchy for the future assembled book:

- `#` volume title
- `##` front-matter chapters
- `##` catalogue parts
- `###` lexical entries
- `####` internal entry sections such as `Derivation trace`,
  `Reconstruction and comparative evidence`, `Old English evidence`, and so on

This will require a deeper demotion of the model-entry headings than the pilot
used, because the final book will nest entries under part headings rather than
placing every entry directly under the document title.

## Appendices

The following appendices are plausible and should stay outside the main lexical
catalogue:

1. **Source and citation caveats**
   - summary of remaining broad citations
   - source limitations that do not block assembly

2. **Machine-readable manifest**
   - class-based entry order used for the assembled book
   - reference to the manifest TSV files rather than hand-maintained order

3. **Known exceptions and non-actionable phonology**
   - brief bridge to the documented exception layer
   - avoids reopening transducer repair inside the lexical volume itself

4. **Placeholder for later sound-change volume or report**
   - notes that the lexical volume is not the full rule-history volume
   - preserves a clean boundary between lexical and rule-centered presentation

## Relation to the later sound-change volume / report

The lexical volume should remain **word-centered**:

- each entry shows one lexical derivation and its supporting prose
- the boxed trace is illustrative and local to that entry
- the volume is not the place for a complete rule-by-rule history of the
  cascade

The later sound-change volume or report should remain **rule-centered**:

- global chronology
- sound-law interaction
- diagnostic comparisons across lexemes
- exception handling at the level of the system rather than the single word

## Architectural recommendation

The volume architecture is ready for a first full lexical assembly alpha **by
class**, with all seven current TSV derivation classes treated as first-class
book sections. Unknown future labels should still be surfaced explicitly rather
than silently folded into one of the seven sections.
