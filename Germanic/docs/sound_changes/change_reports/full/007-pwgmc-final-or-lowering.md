# PWGmc final *ō-lowering before *r

### Sound-change report

#### Historical formulation

SC007 `PWGmcFinalOrLowering` isolates the lowering of final bimoric `*ō` to `*a` before word-final `*r`. In the compact trace it is concentrated in a very small witness set, above all `four` and `water`.

That narrowness matters. This is not a general long-`ō` lowering rule, but a specific final/pre-final environment whose historical value lies in a small set of well-known forms.

#### Source tradition

Ringe and Taylor state that surviving bimoric long `ō` became PWGmc `a` word-finally and before word-final `r`, and they illustrate the outcome with `four` and `water` [@RingeTaylor2014, pp. 58--59]. Fulk likewise notes that final `r` was preserved and that `ō` before it developed to `a` in West Germanic [@Fulk2018, §5.3].

That is solid support for the underlying phenomenon. It is not broad support for a large lexical class, because the historical discussion is anchored chiefly in `four`- and `water`-type material. The report should therefore remain explicit about the rule's narrow environment.

#### CAPR implementation

CAPR models the change as a single explicit environment:

```foma
define PWGmcFinalOrLowering [
    {*ō} -> {*a} || _ {*r} .#.
];
```

The implementation matches the narrow final environment described in the sources. It is also the place where an older duplicated shortening treatment was consolidated in the FST comments, so the current CAPR rule should be read as a compact formalization of a very specific historical setting.

#### Place in the cascade

In the inventory ordering, SC007 follows SC006 `PWGmcEarlyIApocope` and precedes SC008 `PWGmcCoronalWAssimilation`. In the live cascade it remains inside bundled `PWGmcChanges`, but the first-break runner can now expose it directly through the `expanded-pwgmc` order profile.

That means the rule already has a clean chronology-test path even though it remains bundled in production.

#### Order evidence

No validated chronology card exists yet for SC007. The current runner can test it directly with `--order-profile expanded-pwgmc`, and dry-run order inspection in this pass confirmed that SC007 resolves as the fourth rule in that expanded profile.

What is still missing is real earlier/later first-break TSV output. Until those TSVs exist, no historical boundary should be claimed.

#### Interpretation

SC007 is a plausible singleton backend note. The source support is real, but narrow, and the historical story is tied closely to a small lexical set. That makes it suitable for backend preparation now, but not yet strong enough to stand as a fully anchored historical note on its own.

#### Remaining cautions

The chief caution is scope. The rule is narrowly conditioned and strongly tied to the `four` and `water` evidence. Any later prose should resist turning this into a broad long-vowel chapter or implying that the small witness set supports a much larger phenomenon than the sources actually state.
