# Reader-facing chronology evidence QC 01 report

## Chapters checked

The chronology-evidence pass covered the current ten-chapter reader-facing local
section:

1. `049-050-b-allophony-and-sievers-law-syncope.md`
2. `051-sk-palatalization.md`
3. `052-velar-palatalization.md`
4. `053-054-pre-umlaut-bridge-and-w-loss.md`
5. `055-056-i-umlaut-core.md`
6. `057-j-cluster-coalescence.md`
7. `058-nasal-dissimilation.md`
8. `059-oe-back-mutation.md`
9. `060-ws-palatal-umlaut-note.md`
10. `061-weak-tail-nasal-loss-note.md`

No new reader-facing chapters were added in this pass.

## Chronology sources consulted

Primary sources consulted for chronology prose:

- `Germanic/docs/sound_changes/change_reports/full/049-050-onset-allophony-and-sievers-law-bridge.md`
- `Germanic/docs/sound_changes/change_reports/full/051-oe-sk-palatalization.md`
- `Germanic/docs/sound_changes/change_reports/full/052-velar-palatalization-hinge.md`
- `Germanic/docs/sound_changes/change_reports/full/053-054-pre-umlaut-bridge-and-w-loss.md`
- `Germanic/docs/sound_changes/change_reports/full/055-056-umlaut-core.md`
- `Germanic/docs/sound_changes/change_reports/full/057-oe-j-cluster-coalescence-note.md`
- `Germanic/docs/sound_changes/change_reports/full/058-oe-nasal-dissimilation-residual-note.md`
- `Germanic/docs/sound_changes/change_reports/full/059-oe-back-mutation.md`
- `Germanic/docs/sound_changes/change_reports/full/060-ws-palatal-umlaut-note.md`
- `Germanic/docs/sound_changes/change_reports/full/061-weak-tail-nasal-loss-note.md`

Shared dossier context consulted where needed:

- `Germanic/docs/sound_changes/literature_dossiers/059-061-back-mutation-and-weak-tail-bridge.dossier.md`
- `Germanic/docs/sound_changes/book_dossiers/059-061-back-mutation-and-weak-tail-bridge.book-dossier.md`

The internal chronology control files created in this pass are:

- `reader_facing_chronology_evidence_audit_01.md`
- `reader_facing_chronology_evidence_check_01.md`

## Summary of chronology-evidence coverage

### Rules with two-sided evidence

- `SC051` `OESkPalatalization` — two-sided, though the later wrong output is not
  uniform across all witnesses
- `SC052` `OEVelarPalatalizationKFront` — shared two-sided evidence with the main
  SC052 rule
- `SC052` `OEVelarPalatalization`
- `SC054` `OEWLossBeforeI`
- `SC055` `OEIUmlautFronting`
- `SC055` `OEIUmlautRaising`
- `SC055` `OEIUmlautDiphthong`
- `SC055` `OEIUmlaut`
- `SC059` `OEBackMutation`

### One-sided rules

- `SC049` `PGmcBAllophony`
- `SC050` `SieversLawSyncope`
- `SC056` `OEWsPalatalDiphthongization`
- `SC057` `OEJClusterCoalescence`
- `SC060` `OEWsPalatalUmlaut`
- `SC061` `OEWeakTailNasalLoss`

### Boundary-limited or no-exact-wrong-form sections

- `SC053` `OEPostVelarWLoss` — no positive earlier or later boundary recovered
- `SC058` `OENasalDissimilation` — boundary-limited in both directions, no exact
  wrong early/late outputs
- `SC051` later boundary — real, but no single uniform later wrong form for the
  whole witness set

## Reader-facing chronology paragraphs revised

Chronology-specific revisions were made in:

- `049-050-b-allophony-and-sievers-law-syncope.md`
- `051-sk-palatalization.md`
- `052-velar-palatalization.md`
- `053-054-pre-umlaut-bridge-and-w-loss.md`
- `055-056-i-umlaut-core.md`
- `057-j-cluster-coalescence.md`
- `058-nasal-dissimilation.md`
- `059-oe-back-mutation.md`
- `060-ws-palatal-umlaut-note.md`
- `061-weak-tail-nasal-loss-note.md`

## Examples of improved diagnostics

1. **SC049 / rainbow**
   - Earlier boundary: `SC037 < SC049`
   - Expected form: *reġnboga* ‘rainbow’
   - Wrong early output: *reġnfoga* ‘rainbow’

2. **SC054 / sea**
   - Earlier boundary: `SC020 < SC054`
   - Later boundary: `SC054 < SC063`
   - Expected form: *sǣ* ‘sea’
   - Wrong early and late output: *sǣw* ‘sea’

3. **SC059 / give, steal, weave**
   - Earlier boundary: `SC048 < SC059`
   - Later boundary: `SC059 < SC078`
   - Expected forms: *ġiefan* ‘give’, * 'give'stelan* ‘steal’, *wefan* ‘weave’
   - Wrong outputs: *ġeofan*, *steolan*, *weofan*

4. **SC060 / might, night**
   - Earlier boundary: `SC055 < SC060`
   - Expected forms: *miht* ‘might’, *niht* ‘night’
   - Wrong early outputs: *mieht*, *nieht*

5. **SC061 / do**
   - Earlier boundary: `SC023 < SC061`
   - Expected form: *dōn* ‘do’
   - Wrong early result: no output

## Checker result

Commands run:

```bash
python3 Germanic/docs/sound_changes/reader_facing/check_reader_facing_style.py
python3 Germanic/docs/sound_changes/reader_facing/check_reader_facing_chronology_evidence.py
```

Results:

- the strengthened style checker passes with no warnings
- the chronology-evidence check reports **17 sections checked, 0 warnings**

## PDF build result

Command run:

```bash
bash Germanic/docs/sound_changes/reader_facing/build_reader_facing_local_section_02_docker.sh
```

Result:

- `reader_facing_local_section_02.md` regenerated successfully
- `reader_facing_local_section_02.pdf` regenerated successfully
- the build still verifies chapter order from `SC049` through `SC061`
- the References heading remains present

## Remaining places where exact wrong outputs were not available

- `SC051` later boundary: the notes show loss of the `*sċea-* 'sea' / *sċie-*` outputs,
  but they do not isolate one single uniform later wrong form for the entire
  witness set
- `SC053`: no decisive wrong early or late output is currently available
- `SC058`: no exact wrong early or late output is currently available

## Scope confirmation

- No FST rules were changed.
- No TSV files were changed.
- No chronology cards were changed.
- No standardized source reports were substantively changed.
- No source dossiers or book dossiers were substantively changed.
- The changes in this pass were confined to the current ten reader-facing chapter
  files, the reader-facing local-section-02 build/output files, the reader-facing
  style and chronology check scripts, and the new chronology audit/report files.
