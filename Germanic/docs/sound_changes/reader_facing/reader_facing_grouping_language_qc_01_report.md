# Reader-facing grouping and language QC 01 report

## Scope

This pass makes two local cleanup changes to the current reader-facing section.

1. `B allophony and Sievers-law syncope` is no longer carried by one generic
   shared historical discussion.
2. Remaining internal planning language such as `bridge`, `corridor`, and
   `cleanup rule` has been removed from reader-facing chapter titles and prose.

No new sound-change chapters were added.

## `B allophony and Sievers-law syncope` restructuring

`049-050-b-allophony-and-sievers-law-syncope.md` was restructured so that the
two changes are presented separately inside the shared chapter shell.

### Before

The file had one generic `## Historical discussion` section covering both:

1. B allophony
2. Sievers-law syncope

That shared discussion explicitly said the point of keeping the two changes
together was “practical and chronological,” which was not reader-facing enough
for two historically different phenomena.

### After

The file now has:

1. `## Historical discussion of B allophony`
2. `## SC049. ...`
3. `## Historical discussion of Sievers-law syncope`
4. `## SC050. ...`

This preserves the combined chapter shell while making the historical prose
clearer about the fact that the two rules are not one shared phenomenon.

## Other grouped chapters reviewed

The grouped-chapter check now flags multi-SC chapters that keep one generic
`## Historical discussion` heading. After this pass, no grouped chapter is left
in that generic state.

The following grouped chapters were reviewed and retained with explicit shared
historical-discussion headings because the prose already explains their close
interaction:

1. `053-054-pre-umlaut-bridge-and-w-loss.md` ->
   `## Historical discussion of early \emph{*w}-loss before umlaut`
2. `055-056-i-umlaut-core.md` ->
   `## Historical discussion of i-umlaut and West Saxon palatal diphthongization`
3. `064-065-post-apocope-tail.md` ->
   `## Historical discussion of post-apocope \emph{*n}-loss and medial syncope`
4. `066-068-syncope-and-degemination-corridor.md` ->
   `## Historical discussion of late syncope and degemination`
5. `070-071-early-unstressed-fronting-shortening-bridge.md` ->
   `## Historical discussion of early unstressed fronting and later o-shortening`
6. `072-073-unstressed-long-vowel-shortening-and-ae-merger-core.md` ->
   `## Historical discussion of unstressed long-vowel shortening and ae-merger`

No grouped chapter remains flagged for review by the updated style checker.

## Internal lingo removed or retained

### Removed

The current chapter prose had 16 matches for internal-planning language before
this pass; after revision, the count is 0.

Key removals:

1. `The pre-umlaut bridge and loss of \emph{*w} before \emph{*i}` ->
   `Post-velar \emph{*w}-loss and loss of \emph{*w} before final \emph{*i}`
2. `narrow bridge`, `local bridge rule`, and `genuine bridge into that later vowel chapter`
   removed from `053-054-pre-umlaut-bridge-and-w-loss.md`
3. `The post-apocope tail` ->
   `Post-apocope \emph{*n}-loss and medial syncope`
4. `cleanup rule`, `cluster cleanup`, and similar wording replaced with
   `simplification`, `degemination`, or `reductions` in the late weak-tail
   chapters
5. `hinge of the bridge`, `same bridge` removed from
   `070-071-early-unstressed-fronting-shortening-bridge.md`
6. `earlier bridge` removed from
   `072-073-unstressed-long-vowel-shortening-and-ae-merger-core.md`

### Retained with justification

One occurrence of the English word `bridge` remains in the assembled Markdown:

1. `\emph{brycg} ‘bridge’` in `052-velar-palatalization.md`

That instance is retained because it is an ordinary lexical gloss, not internal
planning language.

No reader-facing `corridor` occurrence remains in current chapter prose or in
the rebuilt local-section-04 Markdown.

## Style/checker changes

### Style guide

`style_guide.md` now states that:

1. grouped chapters may share one historical discussion only when the prose
   explains the members' close historical, phonological, morphological, or
   derivational interaction;
2. merely adjacent cascade neighbors should not rely on one generic shared
   historical discussion;
3. internal planning labels such as `bridge`, `corridor`, and `cleanup rule`
   should not appear in reader-facing chapter prose.

### Style checker

`check_reader_facing_style.py` now:

1. allows explicit grouped-chapter headings such as
   `## Historical discussion of ...`
2. warns on multi-SC chapters that still contain only one generic
   `## Historical discussion`
3. flags internal-lingo terms such as `bridge` and `cleanup`, with a narrow
   exception for lexical glosses like `‘bridge’`
4. skips `reader_facing_grouping_language_qc_01_report.md`

## Checker results

### Style checker

Command:

```bash
python3 Germanic/docs/sound_changes/reader_facing/check_reader_facing_style.py
```

Result:

1. no warnings

### Citation checker

Command:

```bash
python3 Germanic/docs/sound_changes/reader_facing/check_reader_facing_citations.py
```

Result:

1. files checked: 16
2. citation issues: 0

### FOMA-width checker

Command:

```bash
python3 Germanic/docs/sound_changes/reader_facing/check_reader_facing_foma_width.py
```

Result:

1. `foma` blocks checked: 28
2. blocks over the conservative old-rendering threshold: 6

### Section-order checker

Command:

```bash
python3 Germanic/docs/sound_changes/reader_facing/check_reader_facing_section_order.py \
  --build-script Germanic/docs/sound_changes/reader_facing/build_reader_facing_local_section_04_docker.sh
```

Result:

1. passes
2. confirms the ordered unique SC sequence through `SC073`

### Cross-reference checker

Command:

```bash
python3 Germanic/docs/sound_changes/reader_facing/check_reader_facing_crossrefs.py \
  --build-script Germanic/docs/sound_changes/reader_facing/build_reader_facing_local_section_04_docker.sh
```

Result:

1. files checked: 16
2. links checked: 115
3. issues: 0

### Chronology-evidence checker

Command:

```bash
python3 Germanic/docs/sound_changes/reader_facing/check_reader_facing_chronology_evidence.py
```

Result:

1. sections checked: 28
2. warnings: 0

### Generated-prose checker

Command:

```bash
python3 Germanic/docs/sound_changes/reader_facing/check_reader_facing_generated_prose.py \
  --build-script Germanic/docs/sound_changes/reader_facing/build_reader_facing_local_section_04_docker.sh
```

Result:

1. introduction paragraphs checked: 2
2. issues: 0

## PDF build result

Build command:

```bash
bash Germanic/docs/sound_changes/reader_facing/build_reader_facing_local_section_04_docker.sh
```

Result:

1. `reader_facing_local_section_04.md` generated successfully
2. `reader_facing_local_section_04.pdf` generated successfully
3. the grouped-discussion restructuring is reflected in the rebuilt current PDF
4. no internal `bridge`, `corridor`, or `cleanup rule` language remains in the
   reader-facing prose
5. the `# References` heading remains present

## Scope confirmation

1. No new chapters were added.
2. No FST rules were changed.
3. No TSV data were changed.
4. No chronology cards were changed.
5. No standardized source reports were substantively changed.
6. No source dossiers were substantively changed.
7. No book dossiers were substantively changed.
