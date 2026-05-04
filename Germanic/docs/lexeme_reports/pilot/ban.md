### Lexeme report

#### Reconstruction and early-stage alternatives

This row deliberately separates the cognate-set headword from the FST input. The etymological headword remains `*bánną`, but the row's `PROTOFORM` is the genitive singular `*bánnas`. The point is not that the noun lacked a nominative singular, but that the inherited nominative does not preserve the medial geminate needed for the attested Old English target. The project therefore treats `bannes` as a paradigm-cell match rather than as the direct continuation of the citation form.

#### Chronological source dossier

- `Germanic/data/germanic-aligned-final.tsv`: `NOTE` states explicitly that the winning input is the genitive singular `*bannas → bannes`, because word-final geminates are simplified while the medial geminate survives in the oblique form.
- The report schema for this project treats that as a late-analogical / paradigm-cell solution: retain the cognate-set headword, but feed the conservative inflectional cell into the FST when that is what matches the attested Old English form most directly.

#### Old English philology

The target `bannes` is not a dictionary headword but an inflected noun form. That matters: this report is not claiming that the inherited nominative singular produced `bannes`. It is claiming that the inherited paradigm contains an oblique singular cell whose regular development gives an actually attested Old English form with the preserved geminate.

#### Project problem and solution

This is a `late_analogy` case. Running the citation form `*bánną` produces `ban`, which is regular but not the attested target. Running the genitive singular `*bánnas` produces `bannes`, so the row is best understood as a cell-based mapping rather than as a lemma-to-lemma mapping.

#### Paradigm probe

### Paradigm probe — ban / bannes

- PROTO: *bánną
- PROTOFORM: *bánnas
- DERIVATION_CLASS: late_analogy
- Morphology source: Hand-specified pilot comparison for n-stem singular cells.
- ProtoGate bypassed: no
- Generated cells: nom.sg., gen.sg.
- Omitted cells: dat.sg. and plural cells omitted in v1; the pilot only compares the citation-form nomination against the selected gen.sg. cell.
- Winning form unique: yes

| Cell | Candidate input | FST output | Match? | Comment |
|:---|:---|:---|:---|:---|
| nom.sg. | *bánną | ban | no | Citation-form comparison. |
| gen.sg. | *bánnas | bannes | yes | Chosen paradigm-cell input in TSV. |
