# Index verborum tagging

Use explicit Pandoc spans when a prose passage should contribute a form to the
`index verborum`:

```markdown
[*sċuldrum*]{.iv lang=oe sort=sculdrum}
[*skúldramiz*]{.iv lang=pgmc display=*skúldramiz sort=skuldramiz}
```

The visible text stays exactly as written. During the combined-book build, the
Lua filter `Germanic/tools/index_verborum_filter.lua` appends the matching
LaTeX `\index[...]` command after the tagged span **only when that explicit tag
is eligible in** `Germanic/docs/book/index_verborum_print_main.tsv`.

## Required attributes

- `lang` — one of:
<!-- BEGIN AUTO-LANGUAGE-LIST -->
- `pie` — Proto-Indo-European
- `oe` — Old English
- `pgmc` — Proto-Germanic
- `pnwgmc` — Proto-Northwest Germanic
- `pwgmc` — Proto-West Germanic
- `paf` — Proto-Anglo-Frisian
- `preoe` — Pre-Old English / prehistoric English
- `on` — Old Norse
- `ohg` — Old High German
- `ofris` — Old Frisian
- `goth` — Gothic
- `os` — Old Saxon
- `odutch` — Old Dutch
- `mdutch` — Middle Dutch
- `dutch` — Dutch
- `german` — German
- `lat` — Latin
- `greek` — Greek
- `skt` — Sanskrit
- `me` — Middle English
- `modeng` — Modern English
- `oirish` — Old Irish
- `mlg` — Middle Low German
<!-- END AUTO-LANGUAGE-LIST -->
- `sort` — ASCII sort key used in the printed index

## Optional attributes

- `display` — override the printed index form while preserving the visible text
- `role` — optional form-role override; defaults to `evidence_form`
- `source_scope` — optional provenance hint for future tooling; ignored by the
  Lua filter for rendering, but retained in production data

## Examples

```markdown
[*sċuldrum*]{.iv lang=oe sort=sculdrum}
[skúldramiz]{.recon .iv lang=pgmc sort=skuldramiz}
[búkkaz]{.recon .iv lang=pgmc sort=bukkaz}
[*nǣdrǭ*]{.iv lang=pnwgmc sort=naedro}
[*bækaną*]{.iv lang=preoe sort=baekana}
[*brjóst*]{.iv lang=on sort=brjost}
[*scouwōn*]{.iv lang=ohg sort=scouwon}
[*lēta*]{.iv lang=ofris sort=leta}
[*dags*]{.iv lang=goth sort=dags}
[*λόγος*]{.iv lang=greek sort=logos}
[śrī]{.iv lang=skt sort=sri}
[bocc]{.iv lang=oe sort=bocc role=regular_output}
[bucca]{.iv lang=oe sort=bucca role=comparison_form}
[skúldramaz]{.recon}
```

## Stage ontology

The historical stages recognized for Index Verborum purposes follow the standard comparative-Germanic cascade:

```
PIE → PGmc → PNWGmc → PWGmc → Pre-OE → OE
```

Proto-Anglo-Frisian (`paf`) is an optional analytical stage used between PWGmc and Pre-OE when a source or adopted analysis reconstructs an Anglo-Frisian common stage. Language/stage codes and computational provenance are **independent**: a form may be tagged `lang=preoe` because it belongs to the historical Pre-OE stage, not because the transducer predicted it.

## Semantic markup classes

Each class classifies **how the form is used**, not its linguistic properties:

| Class | Meaning | Indexed? |
| :--- | :--- | :---: |
| `.iv` | Index-worthy lexical, philological, or comparative evidence | yes |
| `.recon` | Proposed historical reconstructed form (use `.recon .iv` to index) | only with `.iv` |
| `.pred` | Counterfactual / model-predicted output; not attested evidence | never |
| `.lex` | Lexical mention for semantic/gloss context; not phonological evidence | never |
| `.ex` | Pedagogical example in reader-facing rule illustration | never |

`.recon` and `.iv` are **orthogonal**: use `.recon .iv` for a reconstructed form that is cited as comparative evidence; use `.recon` alone for a model-internal stage form that is not indexed.

## Production vs audit

- `Germanic/docs/book/index_verborum_forms.tsv` is the internal production
  form database used by the indexing machinery and audit workflow.
- `Germanic/docs/book/index_verborum_print_main.tsv` is the conservative
  printable main Index Verborum view.
- `Germanic/docs/book/index_verborum_print_excluded.tsv` records production rows
  excluded from the printed main index and the exclusion reason.
- `Germanic/docs/book/index_verborum_print_unique.tsv` collapses printed
  occurrences to unique printable entries for final spot-checking.
- `Germanic/docs/book/index_verborum_print_anomalies.tsv` flags suspicious
  printed rows and marks hard policy violations.
- Explicit `.iv` tags are render-gated by the printable main view: excluded
  `regular_output` tags remain visible in prose but do not emit printed index
  commands. Pre-OE (`preoe`) tags print by default since `preoe` is a
  historical stage, not a model-internal provenance category.
- `Germanic/docs/book/index_verborum_preoe_review.tsv` tracks `preoe` rows for
  explicit print-policy review without deleting them from production data.
- `Germanic/docs/book/reader_facing_example_forms.tsv` is a scaffold for a
  separate reader-facing example-form index and is not mixed into the printed
  main index by default.
- Structured lexical fields, generated lexical headings/metadata, selected
  derivational inputs, explicit `.iv` tags, and curated overrides feed the
  **production** index.
- Automatic compact-trace intermediate stages do **not** feed the production
  index verborum by default.
- Mechanical trace outputs do **not** enter production automatically merely
  because the transducer can generate them. If a regular output matters as
  evidence, contrast, or comparison, tag it explicitly or add it through a
  curated source.
- In the **printed main** index, `regular_output` rows are excluded by default.
  They print only through an explicit `include_main` decision for the exact row.
- Broad harvesting of arbitrary marked-up forms feeds only
  `Germanic/docs/book/index_verborum_audit.md`.
- Broad model-entry prose suggestions are generated into
  `Germanic/docs/book/index_verborum_broad_prose_suggestions.tsv`.
- Curated broad-prose review decisions belong in
  `Germanic/docs/book/index_verborum_broad_prose_decisions.tsv`.
- Main-print overrides belong in
  `Germanic/docs/book/index_verborum_print_decisions.tsv`.
- Markdown comparison/paradigm tables in model entries are audited separately so
  untagged evidence forms still surface for review.
- Curated table-review decisions belong in
  `Germanic/docs/book/index_verborum_table_decisions.tsv`; non-table manual
  adds/ignores still belong in `Germanic/docs/book/index_verborum_overrides.tsv`.

## Scholarly policy

- The main Index Verborum does not attempt to list every form-like string that
  CAPR can generate or discuss. It lists forms used as lexical, philological,
  or comparative evidence. Model-internal stages, counterfactual outputs, and
  pedagogical rule-ordering examples are recorded elsewhere.

- The index verborum includes every form cited as linguistic evidence,
  irrespective of language.
- Ordinary English glosses and prose words do **not** belong in the index.
- Reconstructed forms are indexed with their asterisks in the printed index.
- Reconstructed Old English forms belong in the **Old English** index with an
  asterisk, not under Proto-Germanic or generic pre-Old-English.
- Production indexing is organized around form roles:
  1. `source_protoform`
  2. `selected_input`
  3. `target_form`
  4. `comparison_form`
  5. `regular_output` when explicitly contrasted
  6. `evidence_form`
- Optional `.iv role=...` support exists for cases where an explicit tag should
  preserve a more specific role than the default `evidence_form`.
- Mechanical `intermediate_trace_form` rows belong to the derivation apparatus,
  not to the production index verborum, unless they are explicitly promoted by
  tagging or another curated source.
- Reader-facing sound-change examples are quarantined by adopted policy: they
  are not mixed into the main index verborum by default.
- The main index remains a lexical/evidential index; reader-facing examples are
  held for a separate example-form index rather than auto-promoted into
  production.
- Explicitly tagged or curated reader-facing forms may still enter the main
  index when they are used as ordinary linguistic evidence, not merely as
  pedagogical examples.
- Significant forms in running prose should be tagged explicitly with `.iv`
  spans when they ought to contribute an occurrence-level index reference.
- Broad audit candidates are warnings only. They do **not** enter the
  production index unless they are:
  1. tagged in prose,
  2. added through `action=add` overrides, or
  3. accepted through a curated table decision, or
  4. accepted through a curated broad-prose decision, or
  5. captured by another structured production source.
- Unresolved audit candidates should eventually be:
  1. tagged,
  2. added by override,
  3. accepted/deferred/ignored through a curated table decision when the source
     is a reviewed comparison table,
  4. accepted/deferred/ignored through a curated broad-prose decision when the
     source is running lexical prose,
  5. ignored by override, or
  6. left in `index_verborum_unresolved_baseline.tsv` with a reason while the
     backlog is still being worked down.

## Semantic markup types

CAPR model entries use specialized Pandoc span markup to classify linguistic
forms and control their treatment in output and indexing:

### `.iv` — Index-worthy linguistic evidence

Use `.iv` to mark forms that are cited as lexical, philological, comparative, or
attested linguistic evidence. These forms **will** contribute to the Index
Verborum (subject to print-policy decisions in `print_main.tsv`).

```markdown
[*sċuldrum*]{.iv lang=oe sort=sculdrum}                    % OE attested form
[*skúldramiz*]{.iv lang=pgmc sort=skuldramiz}             % PGmc reconstruction
[schulder]{.iv lang=mlg sort=schulder role=comparison_form} % MLG comparator
```

### `.lex` — Lexical mention, intentionally non-indexed

Use `.lex` to mark forms that are discussed for their semantic/lexical content
**but are not being used as linguistic evidence** for the main derivation or
comparative argument. These forms will appear in prose glosses and semantic
discussions but will **not** enter the Index Verborum.

`.lex` does **not** mean "unimportant form"; it means the form is cited for its
lexical/gloss meaning rather than as phonological or morphological evidence.

```markdown
[*brunaz*]{.lex lang=pgmc}     % mentioned only for semantic context
[voice]{.lex}                   % English homonym, not linguistic evidence
```

### `.recon` — Reconstructed form (may or may not be indexed)

Use `.recon` to mark reconstructed or hypothetical forms. `.recon` and `.iv`
are **orthogonal**: `.recon .iv` marks a reconstructed form that **is**
linguistic evidence; `.recon` alone marks a reconstructed form that is
**not** being indexed (usually a model-internal stage).

```markdown
[búkkaz]{.recon .iv lang=pgmc sort=bukkaz}  % indexed reconstruction
[skúldramaz]{.recon}                        % model stage, not indexed
```

### `.pred` — Counterfactual or predicted form

Use `.pred` to mark forms that are counterfactual outputs from the transducer
or predicted forms that are **not** attested or used as linguistic evidence.
These forms are **never** indexed and never receive glosses.

```markdown
[*sċuldrum-x]{.pred}  % hypothetical variant, not attested
```

### `.ex` — Example or pedagogical form

Use `.ex` to mark forms that appear in pedagogical sound-change examples or
reader-facing rule ordering illustrations. These forms are **not** indexed
automatically; they serve to illustrate derivational processes rather than as
standalone evidence.

```markdown
[*g-*]{.ex} becomes [*j-*]{.ex} before front vowels
```

## Baseline stability

- `index_verborum_unresolved_baseline.tsv` is the current guardrail for
  baseline strictness.
- Source line numbers are still kept in `source_ref` for human navigation, but
  baseline comparison is not intended to depend on line numbers alone.
- The unresolved baseline now also carries the source path, nearest heading,
  category, and a short context snippet so that ordinary line shifts do not
  automatically count as newly introduced candidates.
