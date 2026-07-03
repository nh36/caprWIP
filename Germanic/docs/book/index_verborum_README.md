# Index verborum tagging

Use explicit Pandoc spans when a prose passage should contribute a form to the
`index verborum`:

```markdown
[*sċuldrum*]{.iv lang=oe sort=sculdrum}
[*skúldramiz*]{.iv lang=pgmc display=*skúldramiz sort=skuldramiz}
```

The visible text stays exactly as written. During the combined-book build, the
Lua filter `Germanic/tools/index_verborum_filter.lua` appends the matching
LaTeX `\index[...]` command after the tagged span.

## Required attributes

- `lang` — one of:
<!-- BEGIN AUTO-LANGUAGE-LIST -->
- `oe` — Old English forms
- `pgmc` — Proto-Germanic forms
- `pwgmc` — Proto-West Germanic forms
- `nwgmc` — Proto-Northwest Germanic forms
- `preoe` — Pre-Old-English and model-internal forms
- `on` — Old Norse forms
- `ohg` — Old High German forms
- `ofris` — Old Frisian forms
- `goth` — Gothic forms
- `os` — Old Saxon forms
- `odutch` — Old Dutch forms
- `mdutch` — Middle Dutch forms
- `dutch` — Dutch forms
- `german` — German forms
- `lat` — Latin forms
- `greek` — Greek forms
- `skt` — Sanskrit forms
- `me` — Middle English forms
- `modeng` — Modern English linguistic forms
- `oirish` — Old Irish forms
<!-- END AUTO-LANGUAGE-LIST -->
- `sort` — ASCII sort key used in the printed index

## Optional attributes

- `display` — override the printed index form while preserving the visible text
- `role` — optional form-role override; defaults to `evidence_form`
- `source_scope` — optional provenance hint for future tooling; ignored by the
  Lua filter

## Examples

```markdown
[*sċuldrum*]{.iv lang=oe sort=sculdrum}
[*skúldramiz*]{.iv lang=pgmc display=*skúldramiz sort=skuldramiz}
[*nǣdrǭ*]{.iv lang=nwgmc sort=naedro}
[*bækaną*]{.iv lang=preoe sort=baekana}
[*brjóst*]{.iv lang=on sort=brjost}
[*scouwōn*]{.iv lang=ohg sort=scouwon}
[*lēta*]{.iv lang=ofris sort=leta}
[*dags*]{.iv lang=goth sort=dags}
[*λόγος*]{.iv lang=greek sort=logos}
[śrī]{.iv lang=skt sort=sri}
[`bocc`]{.iv lang=oe sort=bocc role=regular_output}
[bucca]{.iv lang=oe sort=bucca role=comparison_form}
[`*búkkaz`]{.iv lang=pgmc sort=bukkaz role=selected_input}
```

## Production vs audit

- Structured lexical fields, generated lexical headings/metadata, selected
  derivational inputs, explicit `.iv` tags, and curated overrides feed the
  **production** index.
- Automatic compact-trace intermediate stages do **not** feed the production
  index verborum by default.
- Mechanical trace outputs do **not** enter production automatically merely
  because the transducer can generate them. If a regular output matters as
  evidence, contrast, or comparison, tag it explicitly or add it through a
  curated source.
- Broad harvesting of arbitrary marked-up forms feeds only
  `Germanic/docs/book/index_verborum_audit.md`.
- Broad model-entry prose suggestions are generated into
  `Germanic/docs/book/index_verborum_broad_prose_suggestions.tsv`.
- Curated broad-prose review decisions belong in
  `Germanic/docs/book/index_verborum_broad_prose_decisions.tsv`.
- Markdown comparison/paradigm tables in model entries are audited separately so
  untagged evidence forms still surface for review.
- Curated table-review decisions belong in
  `Germanic/docs/book/index_verborum_table_decisions.tsv`; non-table manual
  adds/ignores still belong in `Germanic/docs/book/index_verborum_overrides.tsv`.

## Scholarly policy

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
- Reader-facing sound-change examples are currently quarantined in the audit
  pending a policy decision. They do not enter production automatically unless
  they are explicitly tagged or otherwise curated.
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

## Baseline stability

- `index_verborum_unresolved_baseline.tsv` is the current guardrail for
  baseline strictness.
- Source line numbers are still kept in `source_ref` for human navigation, but
  baseline comparison is not intended to depend on line numbers alone.
- The unresolved baseline now also carries the source path, nearest heading,
  category, and a short context snippet so that ordinary line shifts do not
  automatically count as newly introduced candidates.
