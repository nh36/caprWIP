# Index verborum tagging

## Old English variety metadata (`variety=`)

Old English index entries may carry optional, **source-backed** dialectal,
chronological, or textual-variety metadata via an orthogonal `variety=`
attribute. Every Old English form stays under `language=oe`; there are **no**
separate `mercian`/`northumbrian`/`oe_ews` language codes.

Controlled variety codes live in the sole source of truth
`Germanic/docs/book/index_verborum_varieties.tsv`:

| code    | printed label | parent | assignable |
| :------ | :------------ | :----- | :--------- |
| `ws`    | *(none)*      | —      | **no** (taxonomy parent only) |
| `ews`   | `(EWS)`       | `ws`   | yes |
| `lws`   | `(LWS)`       | `ws`   | yes |
| `angl`  | `(Angl.)`     | —      | yes |
| `merc`  | `(Merc.)`     | `angl` | yes |
| `north` | `(North.)`    | `angl` | yes |
| `kent`  | `(Kent.)`     | —      | yes |

Rules:

- **Ordinary West Saxon remains unmarked.** Use a **blank** `variety` for
  ordinary unlabelled Old English, ordinary West Saxon, West Saxon-normalized
  forms, and any form whose narrower variety has not been structurally encoded.
- `ws` is an **active but non-assignable** taxonomy parent for the qualified
  West Saxon subdivisions (`ews`, `lws`). `variety=ws` **fails validation**, no
  production row may carry it, and no `(WS)` label can ever print.
- `ews` and `lws` are assignable qualified West Saxon varieties.
- `merc` and `north` are subdivisions of Anglian (`angl`).
- **One scalar variety per occurrence.** No comma-separated values, no synthetic
  combined codes (`merc_north`), no combined labels (`(Merc./North.)`).
- The hierarchy is **classificatory metadata only**: a Mercian occurrence prints
  only `(Merc.)` — it is **not** automatically expanded to also emit `(Angl.)`.
- Variety assignments must be **source-backed**. Never infer variety from
  spelling, sound-change rules, FST/transducer behaviour, selected-target
  normalization, or manuscript location alone.
- `variety` is an **indexing-control** attribute: it is stripped from the
  visible prose span and never appended automatically to the running text. The
  label appears **only** in the Index Verborum entry.

Synthetic examples:

```markdown
[strēgan]{.iv lang=oe variety=angl sort=stregan role=comparison_form}
[for-geofan]{.iv lang=oe variety=merc sort=forgeofan role=comparison_form}
[geafa]{.iv lang=oe variety=north sort=geafa role=comparison_form}
[stīeran]{.iv lang=oe variety=ews sort=stieran role=comparison_form}
[styrian]{.iv lang=oe variety=lws sort=styrian role=comparison_form}
[strīeġan]{.recon .iv lang=oe variety=angl sort=striegan role=comparison_form}
```

### Index Verborum form rendering (all languages)

Every linguistic form printed in the Index Verborum is italicized — in **every**
registered language or historical stage (Old English, Old Norse, Old Frisian,
Old High German, Old Saxon, Gothic, Latin, Greek, Sanskrit, Modern English,
Proto-Germanic, …), whether the form is **attested or reconstructed**, and
whether it is emitted by the Python builder or the Lua filter. Formatting is
never inferred from whether a form begins with `*`: the asterisk marks
reconstruction, italics do not.

A single general macro renders every form entry:

```tex
\iventry{FORM}{OPTIONAL-LABEL}
```

- `FORM` is italicized (a reconstruction asterisk stays inside the italics, and
  exactly one asterisk is printed);
- `OPTIONAL-LABEL` is an Old English variety label (`EWS`, `LWS`, `Angl.`,
  `Merc.`, `North.`, `Kent.`), printed in **roman** after a nonbreaking space;
- a blank label produces no suffix, no extra space, and no empty parentheses.

At present only Old English entries use the label argument; all other languages
pass a blank second argument. In the printed index the form is italic and any
variety label is roman, e.g. `\iventry{strēgan}{Angl.}` renders as
*strēgan* (Angl.); reconstructed forms keep exactly one italic asterisk, e.g.
`\iventry{*strīeġan}{Angl.}`. A blank variety produces no suffix.

**Language headings are not form entries.** They are set by the separate
`\ivlangheader` heading macro (bold title, optional **italic** note, rendered
via `\textit`) and follow the heading style; only `\iventry` form entries are
italicized. (The variety *labels* inside `\iventry`, by contrast, are roman.)

### Reader-facing Old English heading

The language registry supports an optional reader-facing `index_note` field,
rendered as a subordinate italic note after the bold language title. This note
is now **active**:

```
Old English (West Saxon normalization unmarked)
```

This heading indicates that West Saxon normalization is used throughout and left
unmarked in the entry text. Dialect labels such as `(Angl.)`, `(Merc.)`,
`(North.)`, `(Kent.)`, and `(LWS)` appear explicitly on the entries that carry
structural `variety` metadata.

## Explicit `.iv` spans

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
[nǣdrǭ]{.recon .iv lang=pnwgmc sort=naedro}
[bækaną]{.recon .iv lang=preoe sort=baekana}
[*brjóst*]{.iv lang=on sort=brjost}
[*scouwōn*]{.iv lang=ohg sort=scouwon}
[*lēta*]{.iv lang=ofris sort=leta}
[*dags*]{.iv lang=goth sort=dags}
[*λόγος*]{.iv lang=greek sort=logos}
[śrī]{.iv lang=skt sort=sri}
[bocc]{.iv lang=oe sort=bocc role=regular_output}
[bucca]{.iv lang=oe sort=bucca role=comparison_form}
[skúldramaz]{.recon}
[voice]{.lex}
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

### Occurrence identities

Every production occurrence has a deterministic source-locator
**occurrence ID** (`occurrence_id`). For explicit source spans, the canonical
form is `<source_ref>:<ordinal>`, for example:

```
Germanic/docs/lexeme_reports/model_entries/1934-bake-bacan.model.md:21:1
Germanic/docs/lexeme_reports/model_entries/1934-bake-bacan.model.md:21:2
```

The ordinal (1-based) distinguishes separate visible spans even when all
semantic fields (language, form, display, role, variety) and source line are
identical. Non-contiguous ordinals are valid because the counter is over all
`.iv`/`.pred` spans on the line. For most occurrences the ordinal is `:1`.

For generated/curated non-explicit rows (headings, table decisions, broad-prose
decisions, overrides), IDs are deterministic scope-aware structured IDs.

Occurrence IDs are propagated as `occ_id=` attributes on `.iv` spans in
the assembled Markdown, enabling occurrence-level parity verification.

Because explicit IDs encode source line numbers, they are deterministic within
a given source snapshot, not permanently line-independent identities.

### Corpus-wide and book-specific views

The printable occurrence data has two layers:

```
forms.tsv
    → print_main.tsv              corpus-wide print policy (2 264 rows)
    → book_occurrences.tsv        in-book occurrence subset before collapse (2 031 rows)
    → book_emissions.tsv          in-book post-collapse emission plan (1 865 rows)
    → book_main.tsv               compatibility alias of book_emissions.tsv
    → print_unique.tsv            unique corpus-wide entries (1 061 entries)
    → book_print_unique.tsv       unique assembled-book entries (828 entries)
```

**Corpus-wide** (`print_main.tsv`): all printable occurrences across the full
Germanic corpus, including occurrences whose source material (compact-trace
entries not yet written as full model entries) is not included in the current
assembled book. `source_not_in_book` rows are legitimate future index content.

**Book occurrences** (`book_occurrences.tsv`): every corpus-wide printable
occurrence whose source is represented in `capr_book_draft_alpha_01`.

**Book emissions** (`book_emissions.tsv`): one row per actual planned
`\index[iv]{...}` emission after legitimate site+command collapsing for
non-explicit rows. Schema: `emission_id`, `representative_occurrence_id`,
`emission_path`, `site`, `index_command`, `language`, `variety`, `display`,
`sort_key`, `form_role`, `source_scope`, `source_ref`, `source_occurrence_count`,
`source_occurrence_ids`. `source_occurrence_count > 1` indicates collapsed
non-explicit occurrences. The algebraic invariant:
`sum(source_occurrence_count) == len(book_occurrences.tsv)`.

**Collapsed occurrences**: when multiple non-explicit occurrences map to the
same emission site and command, the first has blank `collapsed_into` and the
others have `collapsed_into` set to the shared `emission_id`. All retain their
distinct `occurrence_id`. Explicit (`explicit_tag`) occurrences are never
collapsed.

### Build determinism and page numbers

The assembled `capr_book_draft_alpha_01.md` is the canonical deterministic
Markdown input. Its byte content is fixed for a given source snapshot.

The 3-pass LaTeX build converges in the 3rd pass. The first-pass `.ind` may
differ from the final `.ind` (this is normal LaTeX/MakeIndex behaviour —
cross-references are not fully settled after one pass). The final 3rd-pass
`.ind` is deterministic for a given Markdown input. Page-list differences
between separately-regenerated builds of the same commit reflect this
expected 3-pass convergence, not content changes.

- `Germanic/docs/book/index_verborum_forms.tsv` is the internal production
  form database used by the indexing machinery and audit workflow.
- `Germanic/docs/book/index_verborum_print_main.tsv` is the **corpus-wide**
  printable main Index Verborum view (all sources, including future entries).
- `Germanic/docs/book/index_verborum_book_occurrences.tsv` is the
  in-book occurrence subset (pre-collapse).
- `Germanic/docs/book/index_verborum_book_emissions.tsv` is the
  in-book emission plan (post-collapse).
- `Germanic/docs/book/index_verborum_book_main.tsv` is retained as a
  compatibility alias of `book_emissions.tsv`.
- `Germanic/docs/book/index_verborum_print_excluded.tsv` records production rows
  excluded from the printed main index and the exclusion reason.
- `Germanic/docs/book/index_verborum_print_unique.tsv` collapses **corpus-wide**
  printed occurrences to unique printable entries for spot-checking.
- `Germanic/docs/book/index_verborum_book_print_unique.tsv` is the **book-specific**
  unique-entry list (matches what appears in the printed PDF).
- `Germanic/docs/book/index_verborum_emission_table.tsv` is a machine-generated
  table mapping every `print_main` occurrence ID to exactly one planned
  emission ID and canonical index command (`occurrence_id`, `emission_id`,
  `collapsed_into`, `emission_path`, `site`, `index_command`, ...).
- `Germanic/docs/book/index_verborum_book_emission_audit.tsv` is a diagnostic
  record of each print_main row's actual emission disposition.
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

### Parity verification

The build includes two complementary parity checks:

1. **Occurrence-level (Markdown)**: `check_book_occ_id_parity.py` scans the
   assembled `capr_book_draft_alpha_01.md` and verifies exact explicit-span
   partition/parity by occurrence ID with semantic record matching
   (source_ref, language, role, variety, sort_key, display, normalized form).
   Unknown/duplicate/missing/semantic-mismatch IDs fail.

2. **Command-level (TeX)**: `check_book_draft_tex_indexes.py` proves that every
   expected plan-driven non-explicit (`heading_injection`/`line_injection`)
   command appears in generated TeX exactly as emitted by Lua from the
   canonical plan, and that no spurious commands appear.

## Current emitter architecture and staged migration

The production build uses a **dual-emitter** architecture:

1. Explicit visible `.iv` spans emit through the Lua filter (`span_to_index`
   path in `index_verborum_filter.lua`).
2. Non-explicit structured occurrences (lexical heading and line injections)
   emit via Python, which inserts precomputed raw `\index[iv]{...}` commands
   directly into the assembled Markdown.

### `.iv-anchor` marker syntax

Generated `.iv-anchor` markers are infrastructure, **not hand-authored
scholarly markup**. They carry only `emission_id`; all semantic fields are
resolved from `book_emissions.tsv` at build time.

```markdown
::: {.iv-anchor emission_id="emit:abc"}
:::
```

or inline:

```markdown
[]{.iv-anchor emission_id="emit:abc"}
```

`book_emissions.tsv` is authoritative. Python owns occurrence modelling,
emission policy, collapsing, representative selection, variety validation,
and canonical `index_command` construction. Lua places the precomputed command
verbatim; it never reconstructs or modifies `index_command`.

### Staged migration plan

**Stage 1 (complete)**
Shadow-mode `.iv-anchor` infrastructure and strict parity checks were added.

**Stage 2 (complete)**
Production canonical Markdown now contains generated `.iv-anchor` block markers
for all non-explicit `heading_injection` and `line_injection` emissions.
`check_iv_anchor_production.py` proves raw-vs-anchor emission-ID trace parity
and command-sequence parity. Production canonical Markdown no longer carries
raw non-explicit `\index[iv]{...}` commands.

**Stage 3 (deferred)**
- Make explicit visible `.iv` spans plan-driven through `occ_id` so Lua no
  longer independently reconstructs their index commands.

**Stage 4 (deferred)**
- Move accepted broad-prose emissions from approximate heading sites to
  exact passage-adjacent `.iv-anchor` markers.

**Stage 5 (deferred)**
- Add TeX-level occurrence-ID and emission-ID logging.

At the end of Stage 2:
- anchors are generated infrastructure, not hand-authored scholarly markup;
- `book_emissions.tsv` is authoritative for non-explicit command text;
- Python owns modelling/policy/collapse/representatives/command construction;
- Lua places the precomputed non-explicit command by `emission_id`;
- production defaults to anchor-mode assembly;
- legacy raw mode remains test-only for parity and regression;
- explicit visible `.iv` spans still run through the legacy semantic path and
  are not yet plan-driven via `occ_id` (full command-construction unification
  is deferred to Stage 3).
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
[*sċuldrum*]{.iv lang=oe sort=sculdrum}                        % OE attested form
[skúldramiz]{.recon .iv lang=pgmc sort=skuldramiz}             % PGmc reconstruction
[schulder]{.iv lang=mlg sort=schulder role=comparison_form}    % MLG comparator
```

### `.lex` — Lexical mention, intentionally non-indexed

Use `.lex` to mark forms that are discussed for their semantic/lexical content
**but are not being used as linguistic evidence** for the main derivation or
comparative argument. These forms will appear in prose glosses and semantic
discussions but will **not** enter the Index Verborum.

`.lex` does **not** mean "unimportant form"; it means the form is cited for its
lexical/gloss meaning rather than as phonological or morphological evidence.
Use `.lex` only for attested or ordinary forms; do not use it for reconstructed
proto-forms (use `.recon` for those).

```markdown
[voice]{.lex}                   % English homonym, not linguistic evidence
[weard]{.lex lang=oe}           % OE word cited for its meaning, not as phonological evidence
```

### `.recon` — Proposed historical reconstructed lexical form (may or may not be indexed)

Use `.recon` to mark proposed historical reconstructed forms. `.recon` and `.iv`
are **orthogonal**: `.recon .iv` marks a reconstructed form that **is**
linguistic evidence; `.recon` alone marks a reconstructed form that is
**not** being indexed (typically a model-internal derivation stage or a
secondary reconstruction not nominated as index evidence).

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
