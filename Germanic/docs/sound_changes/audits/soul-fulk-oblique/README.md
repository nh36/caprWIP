# Soul: Fulk and the regular oblique candidate

Research only, based on approved earthly/SC040 integration `637b30db`.
No production adoption.

- [Template-based scientific memorandum](research.md): question, sources,
  paradigm, current machinery, historical argument and registry boundary.
- [Attestations](attestations.md): case, dialect/date, spelling and metre;
  verified Luke12:20 accusative.
- [Source checks](source-checks.md): original readings and page-image ledger.
- [Experimental results](results.md): full accusative trace, competing
  models, controls, complete population deltas and DEFER adoption decision.
- [Conditional adoption/publication plan](adoption-plan.md): stable2201,
  individual SC adjudications, protected migration and publication owners.
- `results.json.gz`: complete final native experimental data.
- `evidence.tar.gz` / `evidence-manifest.json`: immutable inputs, successful
  and failed attempts, genuine receipts/logs and operational journal.
- `decision.json`: research decision, not a registered scientific change.
- `validation.json` / `validation.tar.gz`: final checks, with exact tested
  scientific commit distinguished from any later archive-only commit.

## Reproduction

Use an isolated worktree based on the stated scientific reference and a
private backend container with `/usr/app` mounted to that worktree's
Germanic tree. The host needs only the repository's existing Python
tooling and Docker; all Foma execution occurs inside the backend.
Provision the declared original holdings for strict validation, without
symlinks escaping that worktree's reference library. Run the normal
preflight/evidence interface before experimenting.

With the private compose project/override selected by
`COMPOSE_PROJECT_NAME` and `COMPOSE_FILE`, execute from the worktree root:

```sh
python3 Germanic/docs/sound_changes/audits/soul-fulk-oblique/experiment.py \
  --experiment-id soul-fulk-fresh
```

Use a new ID: snapshots are immutable and existing receipts must never be
overwritten. The command freezes source, tools, data, variants and controls,
then executes the existing isolated compiler in container-private storage.
Its snapshot execution outcome is not a scientific acceptance verdict.
Inspect the complete output and all negative controls.

Focused committed-evidence checks:

```sh
python3 -m pytest -q Germanic/tests/test_soul_fulk_research.py
```

These are checks of actually executed archived evidence, not a substitute
for fresh runtime experiments or the strict adoption gates.
