# EAF ai-monophthongization

### Sound-change report

> **Split note (SC004 Outcome-C).** SC004 is now the general/root change
> `*ai/*ái > *ā` only. The word-final unstressed `*-ai > *-ē` outcome that the
> former bundled rule also packaged is a separate, earlier change — now SC014
> `PNWGmcUnstressedAiMonophthongization` (see
> `014-015-opening-vowel-prelude.md`). Implemented on branch
> `historical-cascade-order` (FST split commit `f59b758d`).

#### Historical formulation

SC004 `EAFAiMonophthongization` is the general monophthongization of inherited
`*ai` to `*ā` in the English line: stressed/root `*ái` and unaccented nonfinal
`*ai` both give `*ā` (later fronted to `ǣ` in the relevant OE environments). In
the trace output the rule is visible across families such as `soul`, `stone`,
`bone`, `deal`, and `ghost`, with the two unaccented protoforms `loam` and
`whine` routed through the unaccented rewrite because stress is absent from the
data. It is best understood as a North Sea Germanic / Anglo-Frisian areal
development, not as a single dated node.

#### Source tradition

Ringe and Taylor treat the monophthongization of `*ai` among the widespread
post-PNWGmc vowel developments of the English line [@RingeTaylor2014,
pp. 40--41, §6.1.5]; Fulk lists `ai`/`au` among the North/West-Germanic shared
innovations against Gothic [@Fulk2018, §5.2]; Campbell describes the
Anglo-Frisian `*ai > ā` (later fronted) as an English-line development
[@Campbell1959, §§133--134, §417]. Versloot 2017 — consulted directly (see the
reconciliation dossier) — argues that stressed/root `*ai` monophthongization
spread in two areal waves through a North Sea Germanic dialect continuum
(c. AD 400--900), a diffusion rather than a single inherited Proto-Anglo-Frisian
node, with Old English among the broadest monophthongizers. That source layer
supports the general/root side modelled here; the early unstressed/final side is
SC014's evidence, not SC004's.

#### CAPR implementation

CAPR models the general change as a single EAF-stage rule in the EAF corridor:

```foma
define EAFAiMonophthongization [
    [{*ai} -> {*ā} || _ ?]
    .o.
    [{*ái} -> {*ā}]
];
```

The unaccented sub-rule is explicitly scoped to nonfinal position (`|| _ ?`), so
its correctness does not depend on the early word-final rule (SC014) having run
immediately beforehand. The stressed `*ái -> *ā` and unaccented nonfinal
`*ai -> *ā` rewrites remain two implementation components of one historical
change. The former bundled identifier `PWGmcAiMonophthongization` is retained as
a documented compatibility alias but is not composed in any pipeline.

#### Place in the cascade

SC004 executes at cascade position 25, immediately after SC028
`PNWGmcPreconsonantalXLoss` and before SC029 `OEAwjGlideFormation` — the EAF
corridor. Its SC number stays SC004 even though its executable position no
longer follows numerical order. The former bundled rule opened the cascade
(position 1); that slot is now held by the early final change SC014.

#### Order evidence

The general component carries the entire empirical chronology of the former
bundled rule. The later search finds a real historical break at order `36`
across `SC036` OE Inter Stress Raising: if SC004 is delayed past that stage,
PGmc `*sáiwalō` yields `sāwel` rather than expected OE `sāwol`. The current
placement (executable pos 25 < 33) sits safely before that boundary. The earlier
side is boundary-only — an artefact of the pre-split expanded-PWGmc window — not
a positive constraint on the general component.

#### Interpretation

SC004 is the later, areally diffused North Sea Germanic monophthongization of
`*ai`. The EAF corridor is an operational modelling home for a change whose real
history is a dialect-continuum diffusion rather than a discrete node; the SC036
`soul` boundary is its one usable chronological anchor. Separating out the early
word-final `*-ē` change (SC014) resolves the source imbalance the bundled report
noted: the `*ā` outcome and its areal evidence now stand on their own.

#### Remaining cautions

The EAF stage is a modelling corridor, not a demonstrated discrete
Proto-Anglo-Frisian node; the prose should say so. The later `SC036` relation is
broad/far rather than local. Old English `ā` is fronted to `ǣ` by later change
in the relevant environments, so the surface reflex is not always `ā`.
