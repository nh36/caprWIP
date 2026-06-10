# Reader-facing cross-reference QC 01 report

## Scope

This pass standardizes sound-change cross-references and chronology wording in
the current thirteen-chapter local section 03 reader-facing batch. No new
reader-facing chapters were added.

The enforced standard is:

1. reader-facing sound-change references must normally show both SC number and
   FST rule name;
2. current-section targets use working internal links such as
   `[SC055 OEIUmlaut](#rule-OEIUmlaut)`;
3. outside-section targets remain plain text, for example
   `SC072 OEUnstressedLongVowelShortening`, so the PDF does not contain broken
   internal links;
4. chronology relations are expressed in words such as “must come before” and
   “must follow,” not with symbolic `SC### < SC###` notation.

## Chapter files revised

1. `049-050-b-allophony-and-sievers-law-syncope.md`
2. `051-sk-palatalization.md`
3. `052-velar-palatalization.md`
4. `053-054-pre-umlaut-bridge-and-w-loss.md`
5. `055-056-i-umlaut-core.md`
6. `057-j-cluster-coalescence.md`
7. `059-oe-back-mutation.md`
8. `060-ws-palatal-umlaut-note.md`
9. `061-weak-tail-nasal-loss-note.md`
10. `063-high-vowel-apocope.md`
11. `064-065-post-apocope-tail.md`
12. `066-068-syncope-and-degemination-corridor.md`

`058-nasal-dissimilation.md` did not need revision in this pass.

## Reusable mapping source

The new checker layer derives the SC/rule/anchor mapping from the rule-level
headings already present in the source chapters. The reusable helper is:

1. `Germanic/docs/sound_changes/reader_facing/reader_facing_check_utils.py`

It parses headings of the form:

`## SC051. ... (`OESkPalatalization`) {#rule-OESkPalatalization}`

and exposes:

1. SC number
2. rule name
3. anchor

That derived mapping is then used by the new cross-reference checker and by the
updated chronology checker expectations.

## Before/after examples

| File | Before | After |
| --- | --- | --- |
| `051-sk-palatalization.md` | “This gives the earlier boundary `SC046 < SC051` … This gives the later boundary `SC051 < SC056`.” | “This shows that SC046 OEARestoration must come before [SC051 OESkPalatalization](#rule-OESkPalatalization) … This places [SC051 OESkPalatalization](#rule-OESkPalatalization) before [SC056 OEWsPalatalDiphthongization](#rule-OEWsPalatalDiphthongization).” |
| `060-ws-palatal-umlaut-note.md` | `[the composite i-umlaut rule (`OEIUmlaut`)](#rule-OEIUmlaut)` | `[SC055 OEIUmlaut](#rule-OEIUmlaut)` |
| `064-065-post-apocope-tail.md` | “If the rule is moved before `SC041` … If the rule is delayed until after `SC072` … This gives the earlier boundary `SC041 < SC064` and the later boundary `SC064 < SC072`.” | “If the rule is moved before SC041 PWGmcFinalBareALoss … If the rule is delayed until after SC072 OEUnstressedLongVowelShortening … This shows that SC041 PWGmcFinalBareALoss must come before [SC064 NWGmcInStemNLoss](#rule-NWGmcInStemNLoss), and it places [SC064 NWGmcInStemNLoss](#rule-NWGmcInStemNLoss) before SC072 OEUnstressedLongVowelShortening.” |

## Baseline counts revised

A baseline prose scan across the thirteen chapter files in the pre-change `HEAD`
state found:

1. symbolic `<` chronology relations: 26
2. internal rule-name-only links: 8
3. bare SC tokens in prose without paired rule names: 64

The final cross-reference checker reports zero issues in all of those
categories.

## Outside-section plain-text references retained

Outside-section references remain as plain text only when the target rule is not
present in local section 03 and therefore has no anchor in the current PDF. The
plain-text outside-section references now visible are:

1. `SC020 PGmcFinalZDeletion`
2. `SC023 NWGmcNStemNLoss`
3. `SC037 OECompoundLinkingSyncope`
4. `SC041 PWGmcFinalBareALoss`
5. `SC046 OEARestoration`
6. `SC048 OESecondaryNasalization`
7. `SC072 OEUnstressedLongVowelShortening`
8. `SC078 OEWeakTailReduction`

These remain unlinked by design because local section 03 does not yet include
their rule anchors.

## Checker results

### Cross-reference checker

Command:

```bash
python3 Germanic/docs/sound_changes/reader_facing/check_reader_facing_crossrefs.py \
  --build-script Germanic/docs/sound_changes/reader_facing/build_reader_facing_local_section_03_docker.sh
```

Result:

1. chapter files checked: 13
2. sound-change links checked: 80
3. symbolic `<` relations found: 0
4. bare SC references found: 0
5. rule-name-only references found: 0
6. broken internal anchors found: 0
7. unlinked current-section references found: 0
8. incomplete internal link text found: 0

### Chronology-evidence checker

Command:

```bash
python3 Germanic/docs/sound_changes/reader_facing/check_reader_facing_chronology_evidence.py
```

Result after the boundary-wording change:

1. sections checked: 23
2. warnings: 0
3. symbolic `SC### < SC###` notation no longer counts as boundary evidence

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

1. files checked: 13
2. citation issues: 0

### FOMA-width checker

Command:

```bash
python3 Germanic/docs/sound_changes/reader_facing/check_reader_facing_foma_width.py
```

Result:

1. `foma` blocks checked: 23
2. blocks over the conservative old-rendering threshold: 4
3. width-safe `ReaderFacingFoma` wrapping remains active

### Section-order checker

Command:

```bash
python3 Germanic/docs/sound_changes/reader_facing/check_reader_facing_section_order.py \
  --build-script Germanic/docs/sound_changes/reader_facing/build_reader_facing_local_section_03_docker.sh
```

Result:

1. passes
2. confirms the ordered unique SC sequence
   `SC049, SC050, SC051, SC052, SC053, SC054, SC055, SC056, SC057, SC058, SC059, SC060, SC061, SC063, SC064, SC065, SC066, SC067, SC068`

## PDF build result

Build command:

```bash
bash Germanic/docs/sound_changes/reader_facing/build_reader_facing_local_section_03_docker.sh
```

Result:

1. `reader_facing_local_section_03.md` generated successfully.
2. `reader_facing_local_section_03.pdf` generated successfully.
3. no `SC### < SC###` notation remains in the assembled reader-facing prose.
4. current-section sound-change references now show both SC number and rule name
   and remain internal links in the assembled Markdown.
5. outside-section references now show both SC number and rule name without
   creating broken internal links.
6. rule headings still contain SC numbers.
7. chronology evidence still includes explicit wrong-output diagnostics.
8. the `# References` heading remains present.

## Remaining PDF issues for human review

No automated blocker remains. The only routine visual follow-up still worth a
human glance is the same set of width-wrapped code boxes already identified by
the FOMA-width checker:

1. `SC056` West Saxon palatal diphthongization
2. `SC058` Nasal dissimilation
3. `SC063` High-vowel apocope
4. `SC065` Medial syncope before dentals

The cross-reference checker itself is clean, so no remaining broken-link issue
is known from the current assembled section.

## Scope confirmation

1. No new chapters were added.
2. No FST rules were changed.
3. No TSV files were changed.
4. No chronology cards were substantively changed.
5. No standardized source reports were substantively changed.
6. No source dossiers were substantively changed.
7. No book dossiers were substantively changed.
