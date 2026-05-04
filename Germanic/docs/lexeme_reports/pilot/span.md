### Lexeme report

#### Reconstruction and early-stage alternatives

The relevant OE noun row is the `spanne` row, not the separate verb row `spannan`. For the noun, the project distinguishes citation-form `*spannō` from the selected FST input `*spánnai`. The row note and DEV_NOTES treat the dative singular as the conservative cell that preserves the medial geminate and yields the attested OE form most cleanly.

#### Chronological source dossier

- `Germanic/data/germanic-aligned-final.tsv`: `NOTE` identifies the dative singular as the target cell and cites Brunner on the feminine ō-stem dative in `*-ai`.
- `Germanic/docs/DEV_NOTES.md` records the normalization of the row to `*spánnai → spanne` and treats it as the same general oblique-cell strategy used in other late-analogy rows.
- The broader phonological background for unstressed final developments follows [@RingeTaylor2014], while the morphology note points to Brunner/Sievers-Brunner [@SieversBrunner1965].

#### Old English philology

The target `spanne` is an inflected noun form. The report should therefore say explicitly that the inherited morphology is being captured in a finite paradigm cell rather than in the dictionary-style nominative singular.

#### Project problem and solution

This is a `late_analogy` case. The nominative singular `*spannō` yields `span`, which is regular but not the target. The dative singular `*spánnai` yields `spanne`, so the project chooses the cell-based mapping and leaves the headword/cognate label untouched.

#### Paradigm probe

### Paradigm probe — span / spanne

- PROTO: *spannō
- PROTOFORM: *spánnai
- DERIVATION_CLASS: late_analogy
- Morphology source: Hand-specified pilot comparison for feminine ō-stem singular cells.
- ProtoGate bypassed: no
- Generated cells: nom.sg., dat.sg.
- Omitted cells: gen.sg. and plural cells omitted in v1; dat.sg. is the only selected cell explicitly justified in the row note and DEV_NOTES.
- Winning form unique: yes

| Cell | Candidate input | FST output | Match? | Comment |
|:---|:---|:---|:---|:---|
| nom.sg. | *spannō | span | no | Citation nominative singular. |
| dat.sg. | *spánnai | spanne | yes | Chosen dative singular cell in TSV. |
