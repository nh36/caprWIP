# SC004 sandbox split candidate + equivalence proof

Sandbox / research only. Records a behaviour-neutral component split of the
production rule `PWGmcAiMonophthongization` (SC004) and the formal proof that it
is compositionally identical. **The production rule is not modified.**

## Candidate (research identifiers)

```foma
define SC004FinalAiToE      [ {*ai} -> {*ē} || _ .#. ];
define SC004GeneralAiToA    [ [{*ai} -> {*ā}] .o. [{*ái} -> {*ā}] ];
define SC004SplitCandidate  [ SC004FinalAiToE .o. SC004GeneralAiToA ];
```

Production rule for reference:

```foma
define PWGmcAiMonophthongization [
    [{*ai} -> {*ē} || _ .#.]
    .o.
    [{*ai} -> {*ā}]
    .o.
    [{*ái} -> {*ā}]
];
```

`SC004SplitCandidate = A .o. (B .o. C)` and the production rule is
`A .o. B .o. C`; by associativity of composition these are the same relation.

## Formal equivalence result

Reproduce with `tools/sc004_split_equivalence.py` (run in the backend container,
CWD `/usr/app`). Using foma `test equivalent`:

| Comparison | Result |
| --- | --- |
| `SC004SplitCandidate` == `PWGmcAiMonophthongization` (unrestricted relation) | **TRUE (1)** |
| `EnglishProtoInput .o. SC004SplitCandidate` == `EnglishProtoInput .o. PWGmcAiMonophthongization` | **TRUE (1)** |

## Lexical and trace identity

- **Lexical identity** follows from relation equivalence over the admitted input
  language `EnglishProtoInput`: for every accepted proto the split candidate and
  the production rule yield the identical output set. Substituting
  `SC004SplitCandidate` for `PWGmcAiMonophthongization` anywhere in the cascade
  therefore leaves the frozen lexical baseline unchanged
  (`outputs_sha256 = aaf19ba9…480e`).
- **Trace identity**: because the two are the same transducer relation, every
  intermediate and final derivational form in the full-cascade trace is
  preserved under the substitution; the split only *exposes* the internal A / B /
  C stages that the single `define` already computes in the same order. See the
  per-lexeme before/after-component forms in
  `order_tests/sc004_component_application_report.tsv`.

## Status

This is a **sandbox candidate only**. It is committed as evidence that a split is
behaviour-neutral; it does **not** replace the production rule, assign an SC
number, or move anything in the cascade (task §6, §10). Whether to adopt the
split — and under which historical analysis — is decided in the SC004 options
report.
