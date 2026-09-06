# Infrastructure authority architecture (internal engineering note)

Internal engineering documentation for the 2026 infrastructure-consistency
pass ("one logical authority for each fact"). Not reader-facing.

## Authorities

| Fact | Single authority | Access point |
|---|---|---|
| Executable OE rule definitions and order | `Germanic/fsts/germanic.txt` (production composition rooted at `regex OldEnglish`) | parsed by `Germanic/tools/oe_pipeline.py` |
| Executable stage model (stage names, exec indices, cascade positions, snapshot-bin names, bundle expansion) | `oe_pipeline.py` (derived, in-memory) | `stages()`, `named_stages()`, `cascade_position()`, `rules_between()`, `expected_snapshot_bins()`, `sandbox_text()` |
| SC ↔ Foma identifier mapping; SC lifecycle; verdicts | `Germanic/docs/sound_changes/registry/sc_registry.tsv` | `generate_registry_views.py` |
| Historical/semantic SC metadata | `sc_registry.tsv` + `sc_inventory_annotations.tsv` + `chronology_edges.tsv` | `generate_registry_views.build_all()` |
| Runtime locations (bin dir, fsts dir, data dir; host vs container) | `Germanic/tools/capr_runtime.py` `layout()` | all active tools |
| Compiled-artifact freshness | `oe_build_manifest.json` in the runtime bin dir (source sha256s + expected bin set), written by the rebuild entry points | `capr_runtime.write_build_manifest()` / `check_build_manifest()`; checked by `oe_bin_sync_check.py` |
| Corpus | `Germanic/data/germanic-aligned-final.tsv` | `oe_pipeline.load_rows()` |

Structural bundles in `germanic.txt` (defines whose bodies are pure
composition of other rules) are marked with a trailing `# capr:bundle`
comment; `oe_pipeline` expands them recursively. A define without the
marker is a leaf stage even if its body is compositional.

## Generated projections (never hand-edited)

| File | Generator | Semantics |
|---|---|---|
| `cascade_baseline/cascade_order_manifest.tsv` | `cascade_order_manifest.py` | legacy-compatible view (cascade positions 1–95) |
| `cascade_baseline/executable_model.tsv` | `cascade_order_manifest.py` | complete view: exec_index 1–98 ↔ cascade_position, origin block, snapshot bin, SC id |
| `Germanic/fsts/old_english_sandbox.txt` | `generate_oe_sandbox.py` | stage-by-stage snapshot compile (98 checkpoints); sources `germanic.txt` |
| `chronology_card_index.tsv` `cascade_position` column | `sync_chronology_card_positions.py` | projected from registry `cascade_position` (retired → `retired`) |
| `cascade_baseline/rule_coverage_census.tsv` | `rule_coverage_census.py` | joins committed trace-report firing counts to model positions |
| registry views (8 files) + audit table + rename manifest | `generate_registry_views.py` + chained builders | see `adjudicate.py CHAINED_BUILDERS` |

Each generator has a `--check` mode (or equivalent) and is run by
`adjudicate.py --finalize`; `adjudicate.py --check` and the guard tests
fail if any projection is stale.

## Consumers (no independent copies)

- `oe_full_trace_report.py`: `STAGES`/headers derived from `oe_pipeline`;
  labels are canonical Foma identifiers.
- `sc_evidence.py`: stage lookup from `oe_pipeline`; no alias table;
  fail-closed bin validation (`--min-mtime`, `MIN_BIN_BYTES`).
- `rule_coverage_census.py`: positions from `oe_pipeline`; no
  `STAGE_ALIASES`.
- `sc004_interaction_analysis.py`: crossed-rule sets derived via
  `oe_pipeline.rules_between()` (previously hand-coded and stale).
- `adjudicate.py`: orchestrates evidence (checks generated artifacts,
  compiles the sandbox via the shared runner, writes the build manifest,
  runs the census) and finalization (regenerates every projection, then
  checks, including registry-position ↔ model-position agreement).

## Retired duplication

- `EnglishAfter*` instrumentation chain in `germanic.txt` (28 defines +
  27 regex/save blocks + tracked bins): deleted — zero consumers; the
  generated sandbox is the only instrumentation, and it is derived from
  the production composition itself.
- `trace_old_english_sandbox.py`, `annotate_old_english_sandbox_results.py`,
  `run_old_english_sandbox_workflow.sh`: deleted — hard-coded stale stage
  universe, stale `server/` layout, no consumers.
- Tracked `.bin` files under `backend/` and `Germanic/fsts/`: untracked —
  bins are runtime artifacts rebuilt into the single authoritative bin
  directory (host `backend/` ≡ container `/usr/app`); freshness is the
  build manifest, not git or mtimes.
- mtime-skew heuristics in `oe_bin_sync_check.py`: replaced by the build
  manifest (mtime survives only as `sc_evidence.py --min-mtime`, which
  proves bins were rebuilt during the current evidence run).

## Deliberately left duplicated

- `cascade_order_manifest.tsv` remains byte-compatible with the legacy
  format (many committed tools/tests read it); `executable_model.tsv`
  carries the complete truth. Both are generated from the same model, so
  they cannot drift from each other.
- `sound_change_order_sensitivity.py` keeps its own
  `PWGMC_COMPONENT_RULES` list, but it is validated fail-closed against
  `germanic.txt` at runtime.
- The card index's `earliest_safe_order` / `latest_safe_order` /
  `*_boundary_order` columns are ARCHIVAL first-break experiment results
  in the original chronology-test order space; only `cascade_position`
  is synchronized to the current model.
- Registry `staging_order` / `inventory_order` / `v1_reader_position`
  are distinct, hand-curated order spaces (not executable order) and are
  unaffected.
- `Germanic/tests` intentionally pin literal positions, bin names and
  firing counts: tests are supposed to break when the model changes.

## Known future work (out of scope for this pass)

- `EarlyEnglishLineChanges` mixes historical stages (PNWGmc/PWGmc/EAF/OE)
  in one structural block.
- The larger cascade-generation refactor (generating `germanic.txt`
  block order itself) has not been started.
