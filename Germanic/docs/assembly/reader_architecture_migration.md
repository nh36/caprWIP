# Individual reader ownership and executable-order migration

This is the architectural migration record against validated revision
`15de2d3dba21fee3b5ac3d4cd3bb1414ce63597e` on `update`, not an additional
ordering authority or a sound-change adjudication. The current sequence is
always generated in
[`reader_manifest.tsv`](../sound_changes/registry/reader_manifest.tsv).
No historical verdict, sound law, reconstruction, lexical selection or
accepted scientific baseline is revised by this migration.

## Defect and replacement

Previously, 91 declared published identities occupied 68 reader files.
Seventeen files contained multiple independent entries. The generator sorted
each file by the minimum executable position of its contents, then assembled
whole files. Consequently an entry could remain beside an earlier companion
even when its own executable stage occurred much later.

The registry's existing `source_reader_facing_file` is now the sole map from
published identity to authoritative Markdown source. Each active row with
`include_in_volume=yes` and `is_reader_facing=yes` owns one file; independent
published identities cannot share it. Internal component networks remain with
their parent entry. Filenames and SC numbers identify sources, not positions.
Obsolete grouped files have been removed from the live source population;
Git retains their history. The retired SC021 source and old pilot README
are preserved byte-for-byte under `reader_facing/archive/`.

The resulting population is 97 files and 97 manifest rows: 87 historical
sound-change entries, nine explicitly classified support stages and one
orthographic/surface entry. This is not an expansion to 97 historical laws.
Six already printed technical explanations, SC105--SC110, formerly appeared
inside other entries despite unpublished registry flags. They now have
explicit publication flags and their own sources, without changing
`entry_type`, `staging_row` or historical judgements. SC002 and SC088 had
publication flags but no reader source or existing reader entry; their flags
are corrected to unpublished. SC113 remains unpublished annotation machinery,
with its contextual navigation pointer following the relocated SC035 source.

## Single ordering authority and chapter insertion

`generate_registry_views.build_reader_manifest()` obtains the canonical stages
from `oe_pipeline.stages()`, resolves each eligible registry identifier to
exactly one named stage, and sorts solely by that stage's `exec_index`.
Each generated row exposes the SC identity, Foma identifier, execution index,
cascade position, source file, reader position and chapter.

Only after generating that global sequence does the builder insert the five
chapters. `reader_chapters.tsv` owns their titles, introductions and
`starts_at_sc` boundary identities. The current boundaries are SC103, SC096,
SC020, SC004 and SC016. Each chapter contains the interval beginning at its
boundary and ending before the next. An entry moving across a boundary
automatically changes chapter without a filename, source-location or
membership edit. Missing, duplicate, crossed or noninitial boundaries fail.
Chapter labels cannot move a rule to accommodate historical terminology.

`reader_files.tsv` is retired; there is no replacement per-SC order or
membership table. The reader builder regenerates its expected manifest in
memory and refuses stale or manually reordered rows. Canonical refresh and
publication still use `adjudicate.py` and the existing artifact graph.

The book now explicitly follows the serialization adopted by the executable
reconstruction. That is not a claim that every pairwise historical chronology
has independently been demonstrated. The evidence and strength of historical
relations remain matters for the existing adjudication records.

## Observed sequence and exact parity

The following is an audit snapshot of the generated sequence, not editable
presentation metadata:

```text
SC103 SC096 SC014 SC005 SC024 SC006 SC007 SC008 SC031 SC009
SC010 SC011 SC028 SC012 SC013 SC111 SC015 SC017 SC018 SC019
SC020 SC098 SC097 SC112 SC003 SC022 SC023 SC026 SC027 SC102
SC025 SC104 SC101 SC004 SC029 SC030 SC033 SC106 SC110 SC032
SC034 SC036 SC037 SC039 SC041 SC042 SC107 SC043 SC108 SC044
SC045 SC046 SC047 SC048 SC049 SC050 SC051 SC052 SC035 SC053
SC054 SC056 SC055 SC105 SC057 SC059 SC060 SC061 SC063 SC064
SC065 SC066 SC067 SC068 SC069 SC070 SC071 SC099 SC100 SC072
SC073 SC074 SC075 SC040 SC076 SC078 SC079 SC080 SC081 SC082
SC083 SC085 SC086 SC087 SC089 SC109 SC016
```

The independently projected eligible canonical-stage sequence, generated
manifest sequence, actual reader section sequence and combined manuscript's
sound-change sequence are exactly equal, including order, not just set
membership. Component headings do not constitute new published identities.

| Identity | Executable index | Cascade position | Reader position |
| --- | ---: | ---: | ---: |
| SC014 | 5 | 3 | 3 |
| SC015 | 19 | 17 | 17 |
| SC036 | 45 | 43 | 42 |
| SC037 | 46 | 44 | 43 |
| SC039 | 48 | 46 | 44 |
| SC052 | 62 | 60 | 58 |
| SC035 | 63 | 61 | 59 |
| SC056 | 66 | 64 | 62 |
| SC055 | 67 | 65 | 63 |
| SC040 | 89 | 87 | 84 |

Thus SC014 and SC015 are separated, as are SC039 and SC040. SC052 directly
precedes SC035; SC036 and SC037 remain earlier. SC056 precedes SC055. The same
mechanism applies to every other former grouping, not only these examples.

## Scholarly-content conservation

All 17 grouped sources were divided by substantive entry ownership rather
than blindly at headings. Shared context from the SC014/015, SC029/030,
SC053/054 and SC055/056 groups moved into existing chapter introductions.
Technical material formerly embedded in SC033, SC043, SC052 and the SC055/056
group received explicit independent homes. SC052 retains its component
analysis and SC055 retains its component networks and assembled i-umlaut rule.
The only source-prose markup adjustment links an existing SC107 reference to
its newly explicit published heading.

A systematic comparison of the old and new sources, including chapter
introductions but excluding structural headings, established:

| Material | Conservation result |
| --- | --- |
| Prose paragraphs | All 675 conserved after whitespace and visible-link-text normalization |
| Foma code blocks | All 105 byte-identical |
| Citation occurrences | All 778 retained with identical multiplicities |
| Semantic annotations | All 433 retained with identical multiplicities |
| Existing rule anchors | All 101 retained |
| Added technical anchors | Two, for the existing SC107 and SC108 explanations |

The 103 rule headings include component headings belonging to the same
registered entry. Relocated sources retain their canonical `#rule-...`
anchors, so lexical and reader links do not require scientific or editorial
reidentification. The citation whitelist follows the moved SC015 source and
locator. Historical receipts and tests that intentionally inspect earlier
commits retain their historical filenames.

Normal regression tests check Foma, citation and semantic-markup propagation
into both manuscripts, unique actual destinations for rule links in entries
and shared context, and ownership of primary definitions. Missing or duplicate
definitions and a published rule buried in another entry fail closed.

## Rendered structure

Source-file boundaries no longer insert page breaks. Five actual chapter
headings and the References break remain; source titles and rule/component
headings are nested beneath those chapters. The combined assembler preserves
that hierarchy instead of interpreting file boundaries as chapter structure.

| Presentation | Before | After |
| --- | ---: | ---: |
| Reader PDF pages | 134 | 102 |
| Combined PDF pages | 324 | 295 |
| Lexical PDF pages | 158 | 158 |
| Explicit reader page breaks | 69 | 6 |

There are no blank text pages in the rebuilt reader or combined PDF.
Rendered combined pages were inspected at the separated SC014/015 positions,
SC037/039, SC052/035, SC054/056/055, SC105, SC040 and SC109. On physical
page 79, SC035 begins naturally after SC052's concluding palatalization
discussion; page 80 continues SC035 and then SC053 without a forced file
break. Physical page 83 shows the SC055 composite and the separately labelled
SC105 technical explanation. SC040 appears at its actual late position on
physical page 93. Page-number and source-location changes in indexes were
regenerated, not manually corrected.

## Validation and scientific non-regression

The complete strict command, `python3 -m pytest -q Germanic/tests`, ran with
the original holdings and container runtime. Its final complete run recorded
1538 passing tests and 9061 passing subtests, with two failures subsequently
resolved and rechecked. A coarse whole-file guard mistook the new Markdown
definition-name regex for executable identity extracted from an annotation;
the reader validator now reuses `executable_facts.parse_defines()` instead
of adding a definition parser or weakening the guard. The other failure was
a transient Docker temporary-mount cleanup permission error during the
commit-pinned SC035 replay, not a changed scientific receipt. Its inspected
disposable directory was removed after the mount released. No historical
helper, receipt or expected result was changed.

All 59 final focused rechecks passed, including both failed cases, the fresh
commit-pinned replay's exact receipt comparison, the 32 architecture tests
and the relocated SC029/SC030 source fixture. The complete non-runtime suite
was then rerun against the final shared-parser implementation:

| Run | Result |
| --- | --- |
| Complete strict suite | 1538 passed, two subsequently resolved failures, 9061 subtests passed |
| Final complete non-runtime suite in strict mode | 1501 passed, 39 runtime tests deselected, 9028 subtests passed |
| Final focused rechecks, including the fresh historical runtime replay | 59 passed |

All 39 runtime cases are covered by the complete strict run's 38 passing
runtime cases and the successful replay recheck. All 1501 non-runtime cases
pass against the final implementation. These are separate runs, not a claim
that the complete strict invocation passed without subsequent corrections.

The strict combined publication wrapper also builds the reader-only and
lexical presentations. Its completed run reports zero unresolved internal
references, 103 rule headings, all 58 long headings wrapped, 1961 accepted
index entries, zero paragraph-gloss violations and passing index negative
fixtures. Citation and reader cross-reference checks pass. Architecture tests
include an isolated SC035 movement across a chapter boundary without changing
its identity or source file, full sequence equality, stale-manifest refusal,
and diagnostic failures for ambiguous stage, source, anchor and chapter
configuration.

The executable source, its stage sequence, corpus/data, accepted baselines,
historical receipts, lexical model sources, class manifests and lexical
manuscript are unchanged against the starting revision. All registry fields
outside `source_reader_facing_file`, `include_in_volume` and
`is_reader_facing` are byte-identical.

The scientific invariants remain 389 selected identities, 381 matches, eight
mismatches and 167 elaborated lexical entries in unchanged editorial order.
The mismatch identities remain
`1973,2013,2030,2162,2224,2240,2298,2300`.

| Protected observation | SHA256 |
| --- | --- |
| Executable Foma source | `aee807522c71595eda22fdf7c14f6a096937a6f70909b4e48b925a7eafd4c615` |
| Selected-389 outputs | `53769ef582dd6d119bacc18f808612980a1f02dfed2f94a6e30645bb9de00a9e` |
| Original-380 active subset | `43de8a47b7aaf17f860c9e3009617002ddb36e4d32a90ede1a99525858a417ce` |
| Lexical-input projection | `c44d73698e2fa2717366e951a75bbb02d19aa677faf51fc86dfa25187556b6da` |

## Explicitly deferred existing residue

SC040 retains its pre-existing prose statement that the lowering precedes
SC072, whereas the canonical executable serialization places SC040 after
SC075. This migration exposes that disagreement; it neither changes the
historical claim nor promotes an evidential chronology relation.

Existing PDF warnings for U+0002 and U+27E8/U+27E9 remain. The predicted
SC052 form written as `[\emph{*dejæ}]{.pred}` renders as a dagger without
the form in both the committed starting PDF and the rebuilt PDF. These are
pre-existing rendering limitations, not repaired by this structural migration.
The existing breakable-code-box policy can still split a rule box across
pages; inspection confirmed that its text remains present.

No subsequent sound-change adjudication is part of this work.
