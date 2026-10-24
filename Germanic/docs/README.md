# Germanic pipeline — navigation

Read this first. Every file relevant to current work is SOURCE (hand-edited),
GENERATED (never hand-edited), or ARCHIVE (historical; never authoritative).

| Task | Start here |
| --- | --- |
| Sound-change adjudication | [CURRENT_STATE.md](CURRENT_STATE.md), then the required research protocol |
| Lexical investigation and source verification | [Survey README](lexeme_reports/pgmc_reconstructions/README.md) |
| Lexical publication and selection | [Report schema](lexeme_reports/report_schema.md) and [editorial integration](lexeme_reports/pgmc_integration/README.md) |
| Manuscript and PDF production | [Assembly README](assembly/README.md) |
| CI failure diagnosis | [Validation capabilities](../../docs/CI_VALIDATION.md) |
| Superseded lexical research/process | [Lexical archive](lexeme_reports/archive/README.md) |

## Routine operations (the paved road)

Use these entry points instead of searching the repository. Each states what
it changes, what it checks, and what you must not touch. The control plane and
the SOURCE/GENERATED/ARCHIVE map below decide which files are which.

| Operation | Entry point | Checks | Do not |
| --- | --- | --- | --- |
| Pick the next SC (read-only) | `python3 Germanic/tools/adjudicate.py --next` | derived from the registry | state it by hand |
| Prepare one SC (read-only) | `adjudicate.py SCNNN --prepare` | reading list, authoritative files, permitted edits and commands | start adjudicating before reading it |
| Gather evidence, finalize one SC (rewrite GENERATED files; need Docker, see below) | `adjudicate.py SCNNN --evidence`, `--finalize` | container rebuild and firing census, propagation | run `foma`/`flookup` or trace scripts by hand |
| Regenerate after any SOURCE edit (rewrites GENERATED files; needs Docker) | `adjudicate.py --refresh` (ends `CONTROL PLANE CLEAN`) | every generated artefact via the artifact graph | hand-edit a generated file or pick generators |
| Verify without mutating | `python3 Germanic/tools/artifact_graph.py --check [--mode full]` | freshness and provenance | |
| Change where a lexical entry is published | add a row to `assembly/lexical_editorial_order.tsv`, then `--refresh` | `tests/test_lexical_editorial_order.py` | reorder generated manifests or renumber entries |
| Publish the book | `INDEX_VERBORUM_STRICT=1 bash Germanic/docs/assembly/build_capr_book_draft_docker.sh` | semantic, citation, index and PDF checks | skip inspecting the rendered pages |
| Diagnose CI | `python3 Germanic/tools/run_portable_checks.py` | portable validation only; it does not certify original PDFs or fresh Foma runs | read a portable pass as full science validation |
| Full strict validation | `cd Germanic/tests && python3 -m pytest -q` with holdings and Docker | everything, including runtime execution | run the protected Anglo-Frisian assays in the same session |

Docker prerequisite: `--evidence`, `--finalize` and `--refresh` run
`foma`/`flookup` through the backend container. Start Docker, run
`docker compose up -d`, and confirm `docker compose ps` is healthy first.
`--next`, `--prepare`, `--check` and `artifact_graph.py --check` need no
container and change nothing.

Four kinds of file, never mixed: authoritative scientific SOURCE (registries,
FST, corpus, adjudication memos, frozen baselines); editorial SOURCE
(publication prose, `reader_chapters.tsv` boundaries,
`lexical_editorial_order.tsv`, index decisions); GENERATED projections
(manifests, volumes, indexes, provenance); ARCHIVE (never authoritative).
Editorial SOURCE decides how the book presents the science and can never
change it. Sound laws follow the individual canonical executable sequence;
chapter boundaries cannot override it. Lexical order and indexes retain
their independent editorial sort policies. None is a transcription of
scientific identifiers or storage order.

Failure modes recorded from SC112; guard against them in every task:

- comparing against an inconsistent experimental baseline: use only the frozen baselines and named receipts in `CURRENT_STATE.md`;
- historical replay that depends on a live binary: verify recorded hashes, never trust a rebuilt `.bin` as history;
- receipt and source identities taken on trust: verify them explicitly;
- tests that silently skip runtime execution: strict validation must execute the runtime, and portable passes are labelled portable;
- treating scientific completion as publication completion: the lexical and book publication, with its receipt, is a separate step;
- stale publication documentation: update the phase pointer and README tables in the same change as the work;
- unbounded repair loops: after two distinct failed repairs, stop and report the evidence.

## What you may edit (SOURCE)

SOURCE files come in three kinds; all are hand-edited, everything else is
generated or archived.

**Machine-state SOURCE** (structured facts; one owner per fact):

- `sound_changes/registry/sc_registry.tsv` — **the canonical SC registry.**
  One row per SC ever used (including retired). Owns identity, lifecycle,
  executable identifier, display names, historical stage/scope,
  confidence, adjudication status/verdict/memo path, chronology-node facts,
  and document pointers (evidence dossiers, chronology card, reader-facing
  chapter). It carries NO position columns: executable order is derived
  from the model and published in the generated
  `registry/current_sc_state.tsv`.
- `sound_changes/registry/chronology_edges.tsv` — **the canonical
  chronology-edge registry.** Owns all chronology relations, witnesses,
  witness roles, and evidence basis.
- `sound_changes/registry/reader_chapters.tsv` — reader chapter titles,
  introductions and stable `starts_at_sc` boundaries. One authoritative reader
  file per published SC is owned by `sc_registry.tsv.source_reader_facing_file`.
  The generated `reader_manifest.tsv` follows individual `oe_pipeline` execution
  order exactly; neither chapter divisions, filenames nor SC numbers sort it.
  Changing executable order automatically changes the next generated book;
  never manually rearrange generated output. `reader_files.tsv` is retired.
- `sound_changes/registry/sc_inventory_notes.tsv` — human inventory judgements
  only (plain descriptions, order sensitivity, editorial examples, notes).
  The `sc_inventory_annotations.tsv` beside it is a GENERATED projection.
- `../fsts/germanic.txt` — the FST cascade (only as an adjudication verdict
  requires).

**Scientific-reasoning SOURCE** (prose arguments and evidence):

- `sound_changes/audits/scNNN-adjudication.md` — per-SC adjudication memos
  (copy `sound_changes/audits/ADJUDICATION_TEMPLATE.md`; must carry a
  `Registry-verdict:` line agreeing with the registry).
- `lexeme_reports/pgmc_reconstructions/` — source-faithful evidence/
  actual reviews, consultation policy/finite linked targets, reading scopes,
  analytical positions, comparisons, cited rationales and `commentary.md`. These do not own live
  corpus/input/stage choices. See its README; the population ledger, reading
  coverage/progress, analytical map/coverage, source priorities and provenance are
  GENERATED by the same artifact graph, not an all-library review obligation.

**Publication-prose SOURCE** (reader-facing text; inspect after a verdict):

- `lexeme_reports/model_entries/*.model.md` — mature lexical arguments,
  consumed by the class-manifest lexical and combined-book builders.
- `lexeme_reports/pgmc_integration/editorial_cases.tsv` — scoped philological
  judgements and explicit publication-source certification, independent of
  scientific classifications or adoption. A certified short entry may reuse
  `lexeme_reports/research_memos/`; unselected materials remain drafting evidence.
- `assembly/lexical_editorial_order.tsv` — explicit exceptions to the default
  lexical presentation order (derivation class, then alphabetical English
  headword). Position is editorial and never derived from row IDs or filenames.
- `assembly/book_prose/` — optional shorter regular-entry prose, used only
  when explicitly selected; not a replacement for default mature models.
- `sound_changes/reader_facing/*.md` chapters and
  `sound_changes/book_dossiers/*.md` — `adjudicate.py SCNNN --prepare`
  lists exactly which of these are relevant to a given SC.
- `CURRENT_STATE.md` (phase/commands only; no per-SC facts).

## What is GENERATED (do not edit; regenerate)

`python3 Germanic/tools/adjudicate.py --refresh` (also run by `--finalize`)
regenerates all of these deterministically through the ONE artifact graph
(`tools/artifact_graph.py`) and ends with `CONTROL PLANE CLEAN` — you never
decide which generator to run, and any stale-artifact error tells you to run
the control-plane refresh. Obtain the actual node kinds, authorities and
output paths with `python3 Germanic/tools/artifact_graph.py --inventory`.
This replaces a manually synchronized generated-file list. Runtime evidence
is rebuilt only when its recorded input provenance is stale.
The existing complete derivation-report insertion layer and
`lexeme_reports/coverage_audit.md` are also GENERATED by the same graph:
all runnable traces are preserved, with independently certified lexical
commentary inserted in audit/publish mode. Its missing-report sidecar is
an editorial obligation view, not a claim that derivation write-ups are absent.
(Debugging only: `python3 Germanic/tools/artifact_graph.py [--check|--refresh]`.)

## What is ARCHIVE (never authoritative)

`archive/` (old project states, DEV_NOTES research log, old workflow/plans),
`sound_changes/archive/`, batch reports, frozen baselines' historical
snapshots, the chronology-card programme records, and the frozen audit
snapshots `sound_changes/cascade_baseline/historical_audit_table.tsv` and
`sound_changes/cascade_baseline/rename_migration_manifest.tsv` (ARCHIVE/FROZEN
banners; not regenerated by `--finalize`). See `archive/README.md`.

## One SC adjudication, start to finish

1. `python3 Germanic/tools/adjudicate.py --next` — the next SC (derived
   from the registry; never hand-maintained).
2. `python3 Germanic/tools/adjudicate.py SCNNN --prepare` — assembles the
   packet: registry row, rule text, edges, fingerprints, and a
   registry-driven reading list (required sources, existing
   adjudication, chronology evidence, publication prose, historical
   support). Do not search the repository for evidence; the packet is the
   reading list.
3. `python3 Germanic/tools/adjudicate.py SCNNN --evidence` — rebuilds the
   full cascade and stage bins in the backend container, verifies their
   freshness, and prints the complete live firing census plus witness
   pre/post forms. Never run `foma`/`flookup` or trace scripts by hand.
4. Follow `RESEARCH_ADJUDICATION_PROTOCOL.md`; record everything in the memo.
5. Propagate the verdict by editing SOURCE files only (registries, memo,
   FST/corpus only if the verdict requires, relevant publication prose).
6. `python3 Germanic/tools/adjudicate.py SCNNN --finalize` — regenerates
   all derived artifacts and validates propagation consistency.
7. `cd Germanic/tests && python3 -m pytest -q` — full suite must pass.
8. Commit and push; STOP after one SC.

Current phase and frozen baselines: `CURRENT_STATE.md`.
