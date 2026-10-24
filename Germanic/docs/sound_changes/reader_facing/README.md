# Sound-change reader

The supported reader build is:

```sh
bash Germanic/docs/sound_changes/reader_facing/build_reader_facing_local_section_20_docker.sh
```

It refreshes through `adjudicate.py --refresh`, validates sources and exact
individual executable-order parity, and renders the reader PDF. The combined
book uses the same generated reader. See the [assembly guide](../../assembly/README.md)
for strict lexical and combined builds.

Each published SC has exactly one authoritative Markdown source, owned by
`registry/sc_registry.tsv.source_reader_facing_file`. Component networks of
one SC remain together; separately printed support explanations have their
own source and retain their technical classification. SC113 remains unpublished.

`oe_pipeline` supplies the only sound-change order. The generated
`registry/reader_manifest.tsv` has one row per eligible identity, not one row
per thematic file group. Five SC-anchored chapter beginnings in
`registry/reader_chapters.tsv` divide the global sequence without reordering it.
An executable reorder automatically changes the next book; filenames and SC
numbers are identifiers, not sort keys. Never edit generated order manually.

The executable reconstruction's adopted serialization is not evidence that
every pairwise historical chronology has been demonstrated. Historical
judgements and their strength remain in adjudication records.

Broad shared context belongs in chapter introductions, not multi-SC containers.
Source-file boundaries do not force page breaks. Edit only SOURCE, then run
`python3 Germanic/tools/adjudicate.py --refresh`; source, manifest, reader and
combined-manuscript sequence checks run in normal publication and pytest paths.

The [control-plane map](../registry/CONTROL_PLANE.md) owns classifications and
the [migration record](../../assembly/reader_architecture_migration.md) explains
the structural correction. `archive/` contains unchanged retired source/pilot
documentation. Older `reader_facing_*` pilot aggregates, reports and build
scripts are historical experiments, not alternative supported generators.
