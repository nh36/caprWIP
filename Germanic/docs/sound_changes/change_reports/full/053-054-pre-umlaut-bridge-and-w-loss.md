# Pre-umlaut bridge and W-loss

### Sound-change report

#### Historical formulation

This is a **short adjacent chronological bridge report**, not a major textbook
chapter. It keeps two neighboring ordinary FST changes visible between the
SC052 **OE Velar Palatalization** hinge report and the `SC055-SC056` **umlaut-core** report without pretending that SC053 and SC054 form
one strong traditional chapter.

SC053 **OE Post Velar W Loss** is the weaker and more residual member. It is a
narrow `*ngw > *ng` cleanup rule with only thin comparative anchoring in
derivations such as `*singwan > singan` [@RingeTaylor2014, §6.4.2]. SC054
**OE W Loss Before I** is the stronger positive member. The handbook tradition
does support loss of `w` before unstressed `i`, especially in the `sea`
derivation from earlier `*saiwi-` / `*sawi-` to OE `sǣ`
[@Campbell1959, §406; @RingeTaylor2014, §6.7.1; @Luick1914, §187]. The pair
therefore stays together for practical chronological reasons, not because the
sources present a standard `SC053-SC054` chapter.

#### Source tradition

The source support for SC053 is thin but usable. Ringe and Taylor explicitly
derive PGmc `*singwan` to OE `singan`, which is enough to support CAPR's narrow
`*ngw > *ng` simplification [@RingeTaylor2014, §6.4.2]. That is a legitimate
comparative anchor, but it does **not** make SC053 a large handbook chapter in
its own right. The rule reads more naturally as residual bridge material inside
the pre-umlaut zone.

SC054 is historically more legible. Campbell gives the classic handbook warning
that Old English often loses `w` before `i`, while analogy can restore the
glide in parts of the paradigm [@Campbell1959, §406]. Ringe and Taylor present
the same process in a cleaner derivational sequence, deriving `sea` from
earlier `*saiwiz > *sawi > *sei > sǣ` [@RingeTaylor2014, §6.7.1]. Luick
supports the same trajectory with `sa` / `sǣ` from `*sāwi- < *saiwi-`
[@Luick1914, §187]. That gives SC054 a real handbook footing, though still a
narrow one.

The pair as a pair remains practical rather than doctrinal. The sources support
SC054 far more strongly than SC053, and none of them singles out exactly this
adjacent two-rule unit as a major chapter. The honest historical claim is
therefore modest: SC053 belongs here because every ordinary FST change needs
explicit prose, while SC054 belongs here because it has real source-backed
chronology within the same local stretch of the cascade.

#### CAPR implementation

CAPR keeps both rules sharper than the handbook categories.

SC053 `OEPostVelarWLoss` deletes `*w` in `*ngw` clusters:

```text
*w -> 0 || *n *g _
```

That is exactly the kind of narrow cleanup rule that the model needs but the
handbooks do not usually headline separately. The internal rule comments also
make the restriction explicit by excluding post-vocalic `*gw` material such as
the etyma behind `snow` and `swallow`.

SC054 `OEWLossBeforeI` deletes non-word-initial `*w` before unstressed final
`*i`:

```text
*w -> 0 || EnglishStarVocalic _ *i .#.
```

Here the model aligns more directly with the handbook tradition. The `sea`
derivation is the clearest example, and the ordering comment in the live rule is
historically useful: this loss must remain before the umlaut core so that the
preceding vowel can continue into the later `ǣ` outcome rather than preserving a
too-late glide.

#### Place in the cascade

This unit belongs immediately after SC052 **OE Velar Palatalization** and
immediately before the `SC055-SC056` **umlaut-core** report. That is the
main reason to treat the pair together: both changes are adjacent, both are
ordinary FST changes, and both need explicit prose in the volume.

SC054's later relation to SC063 **OE High Vowel Apocope** should be handled by
cross-reference only. SC063 remains the later report where high-vowel
apocope is discussed in its own right; this bridge report only explains why the
glide-loss rule must already be in place to the left of that later chapter.

#### Order evidence

The order evidence is sharply asymmetric. SC053 has **no positive first-break
boundary in either tested direction**. On the earlier side, the runner reaches
order `13` and then stops at bundled `EarlyEnglishLineChanges` with no real break. On the
later side, it reaches the current safe boundary at SC087 with no real break.
Those are boundary-limited negative results, not hidden chronology claims. This
report therefore does **not** claim that SC053 must follow any specific earlier
historical stage or precede any specific later one.

SC054 is the stronger member. It must follow SC020 **PGmc Final Z Deletion**:
if the rule is moved earlier, the `sea` derivation leaves `sǣw` instead of
expected `sǣ`. It must also precede SC063 **OE High Vowel Apocope**: if the
rule is moved later than SC063, the same witness again yields `sǣw` rather than
`sǣ`. Both positive boundaries are real, but both are narrow because they depend
on the same witness.

Taken together, the cards support `SC020 < SC054 < SC063`, while SC053 remains
card-negative residual bridge material. They do **not** support an internal
reciprocal chronology claim for `SC053-SC054` as a pair.

#### Interpretation

This report is useful because it stays in proportion to the evidence. SC053 is
present because every ordinary FST change needs explicit prose somewhere in the
book, and because its narrow `*ngw > *ng` cleanup still has a plausible
comparative anchor in `singan`. SC054 is present because it has stronger source
backing and a real, if witness-limited, two-sided chronology profile centered on
`sea`.

That makes the pairing practical and chronological rather than traditional. The
book does not need to pretend that SC053 and SC054 form a standard handbook
chapter. It only needs to keep them visible, in order, and properly situated
between the SC052 hinge report and the `SC055-SC056` umlaut
core.

#### Remaining cautions

SC053 should not be made stronger than it is. Its earlier and later card results
are boundary-limited negative evidence, not positive chronology claims. SC054
should not be allowed to sprawl into a non-contiguous `SC054-SC063` chapter just
because its later boundary happens to be SC063. That rightward relation belongs
in cross-reference, not in a larger chapter claim.

More broadly, this report should not duplicate the `SC055-SC056`
**umlaut-core** report on the right or the SC063 **High-vowel
apocope** report farther right. Its purpose is narrower: to keep a weak
residual member and a narrow positive member visible in strict chronological
order without inflating either one into a major chapter.
