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
  - `oe` — Old English
  - `pgmc` — Proto-Germanic
  - `pwgmc` — Proto-West Germanic
  - `nwgmc` — Proto-Northwest Germanic
  - `preoe` — Pre-Old-English and model-internal forms
  - `on` — Old Norse
  - `ohg` — Old High German
  - `ofris` — Old Frisian
  - `goth` — Gothic
- `sort` — ASCII sort key used in the printed index

## Optional attributes

- `display` — override the printed index form while preserving the visible text
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
```

## Production vs audit

- Structured lexical fields, compact derivation traces, generated lexical
  headings/metadata, and explicit `.iv` tags feed the **production** index.
- Broad harvesting of arbitrary marked-up forms feeds only
  `Germanic/docs/book/index_verborum_audit.md`.
- Curated decisions belong in
  `Germanic/docs/book/index_verborum_overrides.tsv`, not in the generated
  `index_verborum_forms.tsv`.

## Scholarly policy

- Structured lexical and trace forms are indexed automatically at the lexical
  entry or trace location that generated them.
- Significant forms in running prose should be tagged explicitly with `.iv`
  spans when they ought to contribute an occurrence-level index reference.
- Broad audit candidates are warnings only. They do **not** enter the
  production index unless they are:
  1. tagged in prose,
  2. added through `action=add` overrides, or
  3. captured by another structured production source.
- Unresolved audit candidates should eventually be:
  1. tagged,
  2. added by override,
  3. ignored by override, or
  4. left in `index_verborum_unresolved_baseline.tsv` with a reason while the
     backlog is still being worked down.

## Baseline stability

- `index_verborum_unresolved_baseline.tsv` is the current guardrail for
  baseline strictness.
- Source line numbers are still kept in `source_ref` for human navigation, but
  baseline comparison is not intended to depend on line numbers alone.
- The unresolved baseline now also carries the source path, nearest heading,
  category, and a short context snippet so that ordinary line shifts do not
  automatically count as newly introduced candidates.
