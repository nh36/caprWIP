# PROTOFORM historical-stage audit (2026)

## Problem

A follow-up audit of commit `97f7e18a` found that the historical-stage sidecar
(`Germanic/data/entry_stage_metadata.tsv`) had been bloated to 159 rows and, in
places, silently equated a reconstruction asterisk (`*`) with Proto-Germanic
(`pgmc`). That conflates two independent axes:

- **reconstruction status** — the `*` / `.recon` marker ("reconstructed, not
  attested");
- **historical stage** — the comparative-Germanic layer a form belongs to
  (`pie … pgmc … pnwgmc … pwgmc … nsgmc … paf … preoe`).

The project convention is explicit: **PROTO is always the Proto-Germanic
lexeme-level reconstruction (`proto_stage = pgmc`)**, whereas **PROTOFORM is the
transducer *input* chosen to yield the correct Old English output**, and it
carries its own, separately-argued stage. A reconstructed PROTOFORM is not
Proto-Germanic by default.

## Scope and population

The audit re-examines only the rows where **PROTOFORM ≠ PROTO** — the exceptional
cases where the selected input differs from the PGmc lexeme reconstruction. There
are **80** such rows. Equality rows (PROTOFORM == PROTO) are Proto-Germanic by
construction and are resolved to `pgmc` in code (`resolve_stages` in
`Germanic/docs/assembly/build_class_manifests.py`); they are *not* listed in the
sidecar, which is now **exception-only**.

A PROTOFORM ≠ PROTO row with no sidecar entry **fails closed** — it is queued for
review, never silently labelled `pgmc`.

## Distribution (80 rows)

`protoform_stage`:

| stage  | rows |
|--------|-----:|
| pgmc   |   74 |
| preoe  |    3 |
| pwgmc  |    2 |
| nsgmc  |    1 |

`protoform_variety`: 76 none, **4 transponent** (loam, spare, thousand, world).

The dominant `pgmc` count is expected and correct: a PROTOFORM ≠ PROTO input is
very often simply a *different Proto-Germanic paradigm cell or formation variant*
(e.g. a genitive-singular stem, an oblique stem, a voiced/voiceless doublet).
Such rows are genuinely still `pgmc`; the divergence is morphological, not
chronological. Of the 74 `pgmc` rows, 72 are `same_stage_pgmc_*` decisions
(49 paradigm cell, 14 model encoding, 9 alternative formation).

## Disputed adjudications (7)

Seven rows were individually re-adjudicated against the primary sources. Each
carries a page-numbered citation in the sidecar `evidence` column.

| row | lexeme | protoform_stage | variety | basis |
|-----|--------|-----------------|---------|-------|
| 2087 | knob | pgmc | — | *knúppaz / *knúbbô are both PGmc morphological variants (Kroonen 2011:297). Confirmed PGmc. |
| 2109 | loam | preoe | transponent | PGmc n-stem *laimô(n) (Orel 2003:272; Kroonen 2013:363); neuter a-stem *láimą is an OE-internal class reformation, not a reconstructible PGmc a-stem. |
| 2133 | navel | pwgmc | — | R/T 2014:270: PNWGmc *nabulaz > PWGmc *nabulō = CAPR *nábulô. (Supersedes prior `pnwgmc` and the erroneous "p.11090" OCR line-number citation.) |
| 2205 | spare | preoe | transponent | PGmc/PWGmc class-III *sparē-; R/T 2014:191 give the pre-OE class-II refashioning *spærōjan > sparian. |
| 2252 | thousand | preoe | transponent | Medial -e- is an OE-specific analogical development (Vorbild *ærende*); PWGmc/OS/OHG retain -u- (DEV_NOTES §14.7). |
| 2302 | world | pgmc | transponent | R/T 2014:341 anchor *weraldiz as PNWGmc; CAPR *wír-àldu keeps the older *wir- vowel but post-PGmc ō/u-stem morphology — a genuine transponent whose vowel and morphology sit at different stages. Base stage kept `pgmc`. |
| 2308 | youth | pwgmc | — | R/T 2014:141: PWGmc *jugunþi > OE ġeoguþ; selected *júgunθ is post-early-apocope (PWGmc-internal). |

## The transponent mechanism

Four PROTOFORMs are **transponents**: inputs deliberately constructed to drive the
OE derivation, mixing features from different stages (e.g. an older vowel with
younger morphology) or reflecting an OE-internal class reformation that is *not*
reconstructible at the PROTO stage.

Rather than invent a pseudo-stage, `transponent` is modelled as an **orthogonal
variety** (analogous to `Anglian` / `Mercian` for OE) in the variety registry
`Germanic/docs/book/index_verborum_varieties.tsv`, with printed label `transp.`
It attaches to any reconstructed base stage. Each transponent therefore keeps its
**honest base stage** — world = `pgmc`, loam/spare/thousand = `preoe` — plus the
shared `transponent` flag. The registry entry uses the sentinel language `recon`
(`CROSS_STAGE_LANGUAGE` in `Germanic/tools/index_verborum_render.py`); validation
permits the cross-stage variety on any reconstructed stage and rejects it on `oe`
or comparison languages.

## Label / confidence independence

The stage (and variety) label is **fully independent** of confidence. Any
confidence-derived `review_status` column was dropped from
`protoform_stage_audit.tsv`; `confidence` is retained as a standalone signal that
never influences which stage label a form receives.

## Code changes

- **Sidecar** reverted to 80 exception-only rows; added `protoform_variety`
  column.
- **`build_index_verborum.py`**: removed the silent `pgmc` / `preoe` fallbacks
  for reconstructed forms — non-model stages now fail closed via a
  `transliterate_sort_key` identity check; genuine PROTO≠PROTO-input differences
  raise instead of defaulting. Deleted a dead duplicate table-semantic pipeline.
- **`build_class_manifests.py`**: `resolve_stages` carries `protoform_variety`
  through to the class manifests; equality rows resolve to `pgmc` in code.
- **Model entries**: `selected_input` markup in the seven audited `*.model.md`
  files re-tagged to the corrected `lang=` stage (+ `variety=transponent` where
  applicable), removing double-headed index entries (e.g. youth's *\*júgunθ* no
  longer appeared under both `pgmc` and `pwgmc`).

## Baseline

The FST is unchanged by this audit (data / registry / tooling / prose only). A
fresh compile of `Germanic/fsts/germanic.txt` followed by
`oe_mismatch_report.py` yields the expected **7 mismatches, all documented, 0
undocumented**. The `--strict-mode=baseline` index build exits 0 (no new
unresolved candidates).

> Note: the canonical tracked `Germanic/fsts/*.bin` files have now been
> recompiled from the current `germanic.txt` (via `foma -q -l germanic.txt -e
> quit` run with CWD `/usr/app/fsts`, the Docker-mounted `Germanic/fsts`), so
> the compiled bins now agree with the source and yield **380 accepted / 373
> matched / 7 mismatched / 0 ambiguous** with `*stámniz -> stefn` (mult 1,
> MATCH) and `*xébun -> heofon` (mult 1, MATCH). Foma bins are byte
> non-deterministic but functionally deterministic; only the 30 functionally
> changed bins were recommitted. The gitignored `backend/*.bin` files are left
> untouched (legacy/noncanonical); `.gitignore` tracks only `Germanic/fsts/*.bin`.

## Follow-up corrections (finishing pass)

A source-markup re-audit of the eight sampled transponents surfaced three
residual leaks that let a selected transponent input appear under Proto-Germanic:

- **spare** (`2205-spare-sparian.model.md`): three occurrences of the *selected*
  class-II transponent *\*spárōjaną* were still tagged `lang=pgmc` (they lacked
  `role=selected_input`, so the earlier grep missed them). Re-tagged to
  `lang=preoe variety=transponent`. The genuinely inherited class-III *\*sparē-*
  comparanda were left as PGmc/PWGmc.
- **loam** (`index_verborum_table_decisions.tsv`): the curated table-decision for
  *\*láimą* was `pgmc`/blank, forcing a stray Proto-Germanic occurrence. Corrected
  to `preoe`/`transponent`. The comparative headword *\*laimōn* stays PGmc.
- **`build_index_verborum.py`**: `trace_proto_input`'s compact-trace production
  did not forward `protoform_variety`, so the trace occurrence of a transponent
  lost its `transp.` label. Now resolves and forwards the variety.

After these fixes the four selected transponents render as: spare *\*spárōjaną*,
thousand *\*θūs-èndi*, loam *\*láimą* at **pre-OE** with `transp.`; world
*\*wír-àldu* at its chosen **PGmc base stage** with an explicit `transp.` marker.
