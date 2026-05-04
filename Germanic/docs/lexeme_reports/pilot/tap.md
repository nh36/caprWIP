### Lexeme report

#### Reconstruction and early-stage alternatives

The aligned row keeps both `PROTO` and `PROTOFORM` as `*táppô`, because the project is not claiming that a different inherited protoform solves the Old English target. Instead, the note says the opposite: no paradigm cell of the inherited nominal paradigm yields lautgesetzlich `tæpp-`. This makes `tap` a good pilot for the distinction between a known historical explanation and a form the deterministic FST should not be forced to derive.

#### Chronological source dossier

- `Germanic/data/germanic-aligned-final.tsv`: the note classifies `tæppa` as an analogical n-stem levelling case and cites [@Orel2003], [@Kroonen2013], and [@Fulk2018].
- `Germanic/docs/DEV_NOTES.md` §17.10.16a-c argues that nominal cells keep back-vowel environments at the relevant stage, while the co-radical weak-verb pathway would produce `tepp-`, not `tæpp-`.
- The row is therefore one of the clearest examples of a historically intelligible but unmodellable analogical result in the present cascade.

#### Old English philology

The target `tæppa` is a genuine Old English noun form. The issue is not its attestation but its historical derivation: the project notes treat the `æ` as analogical and explicitly reject any claim that it is the direct phonological continuation of an inherited Proto-Germanic noun cell.

#### Project problem and solution

This is a `known_unmodelled` case. The FST's regular output from the nominative singular is `tappa`, and representative oblique cells remain in the same back-vocalic zone. Since no inherited cell gives `tæppa` by regular sound change, the row is correctly left as a documented exception rather than retargeted to a misleading pseudo-solution.

#### Paradigm probe

### Paradigm probe — tap / tæppa

- PROTO: *táppô
- PROTOFORM: *táppô
- DERIVATION_CLASS: known_unmodelled
- Morphology source: Hand-specified pilot comparison for n-stem singular cells drawn from DEV_NOTES and oe_known_problems.tsv.
- ProtoGate bypassed: no
- Generated cells: nom.sg., gen./dat./acc. stem
- Omitted cells: Plural cells omitted in v1; the ledger already states that no paradigm cell yields lautgesetzlich tæpp-.
- Winning form unique: no

| Cell | Candidate input | FST output | Match? | Comment |
|:---|:---|:---|:---|:---|
| nom.sg. | *táppô | tappa | no | TSV input; ledger says this yields regular tappa. |
| gen./dat./acc. stem | *táppan | tappan | no | Representative oblique-stem comparison from DEV_NOTES. |
