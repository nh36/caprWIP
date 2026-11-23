# Reference catalogue

`catalogue.tsv` is the project-wide discovery index for bibliographic works,
editions, and explicitly identified local research assets. `projects/` contains
small source-ID manifests; `projects/hay-article.tsv` is the first example.
These manifests point to catalogue records and do not copy source files.

## Fields and identifiers

All paths are repository-relative. A source ID of `ref:<key>` corresponds to a
BibTeX key in `docs/refs.bib` or a project bibliography. `local:`, `dataset:`,
and `artifact:` identify holdings that have no shared BibTeX key; they do not
create or imply one. When a source has multiple parts, paths and SHA-256 values
are semicolon-separated in corresponding order. `other_known_paths` and
`legacy_filename_aliases` record alternate names, OCR derivatives, and known
containers without treating them as additional independent works. A searchable
text path may be a directory when OCR is stored as per-page files; in that case
there is no aggregate text checksum.

The BibTeX master remains `docs/refs.bib`; existing intake manifests remain the
authority for acquisition details, page-level maps, extraction methods, and
source-specific qualifications. The catalogue consolidates discovery metadata
and links to those records. It does not replace citation keys or claim that a
source has been read or verified beyond what its source record says.

`availability_status` records what was present in the checkout used to build
the catalogue. In particular, paths under `docs/references/local/` are
Git-ignored and may exist in one checkout but not another. Recheck each path
locally; a path listed as unavailable is not a claim that the work is
unobtainable. Rights/access entries are conservative; an available local copy
does not imply redistribution permission.

## Worktree isolation and future storage

The ignored `docs/references/local/` directory is per-worktree, not a shared
Git-worktree resource. During this catalogue pass, the primary checkout had a
local library, one linked worktree had no `docs/references/local/` directory,
and another had a separate directory that did not contain the same Fulk 1992
PDF. The directories had different filesystem identities. Thus a source found
in one checkout is not necessarily available to an agent in another.

Recommended future design: keep one verified private library outside the
worktree directories and link each checkout's ignored
`docs/references/local/` path to it, or add a user-level reference-root setting
with the current path as fallback. A per-worktree symlink is simpler and keeps
existing manifest paths working; a resolver is more explicit but requires
tooling support. Neither should be installed until a non-destructive plan
reconciles path/hash inventories, preserves worktree-specific files, verifies
backups, and tests access from every active worktree. No files were moved or
linked during this task.

## Maintenance and validation

When adding an acquisition or bibliography record, update the catalogue and
the relevant project manifest in the same change. Reuse an existing source ID
for an alternate filename or duplicate copy of the same edition. Create a
separate source record only for a distinct work or edition, and preserve
edition-specific pagination and checksums.

Run from the repository root:

```sh
python3 docs/references/validate_catalogue.py
```

The validator checks identifier uniqueness, project-manifest references,
recorded file and page-map paths, and Git-ignore boundaries for private files.
It reports local files that are inaccessible in the current worktree without
mistaking their absence for a global acquisition failure.
