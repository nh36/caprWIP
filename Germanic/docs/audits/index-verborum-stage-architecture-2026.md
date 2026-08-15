# Index Verborum historical-stage architecture (2026)

## Problem

The Index Verborum conflated two independent properties of a reconstructed
form: **reconstruction status** (the `*` / `.recon` marker, "this form is
reconstructed, not attested") and **historical stage** (which comparative-
Germanic layer it belongs to: `pie … preoe`). Reconstructed lexical inputs were
labelled Proto-Germanic (`pgmc`) by construction — a computational convenience
silently promoted to a historical claim.

The demonstrated symptom: heaven's selected input *\*xébun* (Ringe & Taylor's
northern West Germanic *hebun*) was indexed as `pgmc`, even though the same form
is dated `pwgmc` in reader-facing section 19 — so one lexeme carried two
different chronological labels.

## Audit findings

Sources of `pgmc` on reconstructed forms in `build_index_verborum.py`:

- `lexical_protoform`, `lexical_proto` — hard-coded `language="pgmc"` from the
  manifest PROTO/PROTOFORM.
- `trace_proto_input` — hard-coded `language="pgmc"` for the selected input from
  the compact trace.
- `infer_table_semantic_language` — silent `return "pgmc"` fallback for a starred
  form in a derivation table with no explicit language hint (≈9 forms).
- `infer_broad_prose_language` — silent `return "pgmc"` fallback (suggestion path;
  the printed broad-prose entries were already curated decisions).

Stage of the selected input, audited across all 147 model entries: every
early_analogy / analogy PROTOFORM carries Proto-Germanic morphology
(`-az/-iz/-ą/-as/-aną/-ō/-ôn …`) **except heaven's *\*xébun*** (the `-un`
remodelled u-stem, whose labial was generalised at a post-PGmc stage). Prose
mentions of later stages in other entries (world, whine, timber, …) describe the
*derivation path*, not the *input*, whose reconstruction is PGmc. Heaven is the
sole row whose selected input is genuinely later than Proto-Germanic.

## Decisions (do not re-litigate)

1. **Stage is an explicit, per-row datum.** It lives in the canonical sidecar
   `Germanic/docs/assembly/entry_stage_metadata.tsv`
   (`row_id → proto_stage, protoform_stage`), propagated into
   `manifest_all_by_class.tsv` and read by the index builder. The sidecar was
   chosen over inline model-entry headers (which would shift every line-anchored
   index decision) and over TSV columns (the corpus TSV has a pre-existing
   embedded-tab row, 2034/fright, that makes positional columns fragile).

2. **Fail closed, never default.** `require_reconstructed_stage(...)` raises on a
   blank or unrecognised stage. The table/broad-prose inference now returns "" for
   an unresolved reconstructed form, routing it to the curated decision queue
   instead of `pgmc`. A corpus selected input with no model entry is the PGmc
   reconstruction heading its derivation; any post-PGmc input must declare its
   stage in the sidecar.

3. **heaven `*xébun` / `*hebun` / `*hebunas` → `pwgmc`.** This matches the
   established reader-facing convention (section 19 already dates *hebun*
   `pwgmc`) and follows the task guidance to reuse an existing PWGmc/NWGmc
   mechanism rather than inventing a stage. The deeper mn-stem obliques
   (*\*xémenaz*, *\*xémnas*, *\*xémni*, *\*xémnum*, *\*hemnaz*, *\*hemō*) stay
   `pgmc`: the labial itself comes regularly from those PGmc obliques, and only
   the remodelled input is later.

4. **Notation.** R&T's `h`-spelling and CAPR's canonical `x`-spelling are the
   same lexeme; both are dated `pwgmc`, so *hebun* and *xébun* never appear as two
   differently-dated Proto-Germanic headwords. Dating them to a single stage
   merges the previously duplicated *hebun* label (pgmc + pwgmc → pwgmc).

## Migration scope

- New: `Germanic/docs/assembly/entry_stage_metadata.tsv` (147 rows).
- `build_class_manifests.py` — reads the sidecar; adds `proto_stage` /
  `protoform_stage` manifest columns; notes rows with missing stage.
- `build_index_verborum.py` — `require_reconstructed_stage(...)` fail-closed
  helper; lexical/trace occurrences read the manifest stage; inference fallbacks
  return "" instead of `pgmc`.
- heaven model entry — five `.iv` spans moved `lang=pgmc → lang=pwgmc`; a
  net-zero prose note records the `x`/`h` notation and the `pwgmc` dating.
- `index_verborum_table_decisions.tsv` — 9 curated `accept language=pgmc`
  decisions make the previously silent table-inferred PGmc inputs explicit.
- Tests: `test_index_verborum_stage_architecture.py` (new);
  `test_index_verborum_variety.py` unique-count snapshots `-1` (the *hebun*
  merge); `check_index_verborum.py` `*kráftaz` assertion relaxed from
  `table_auto_rows` to `table_rows` (auto → curated decision).

## Invariants preserved

The FST, the corpus rows (2068 `*xémenaz`/`*xébun`/heofon/early_analogy; 2216
`*stámnaz`/`*stámniz`/stefn/early_analogy), SC022, the cascade baseline
(380 / 373 / 7 / 0, `outputs_sha256` unchanged) and the mismatch set are
untouched. This is metadata-only: it changes how reconstructed forms are dated in
the index, not the phonology or the score.
