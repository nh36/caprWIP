# Dental hardening

## Historical discussion

Ringe and Taylor state directly that in PWGmc voiced dental fricative `*ð` became stop `*d` in all positions [@RingeTaylor2014, p. 43].

That makes the change historically clear and systemic. The chapter treats an explicit consonantal adjustment in the early West Germanic sequence, not one narrow lexical family.

## SC013. Dental hardening (`PWGmcDentalHardening`) {#rule-PWGmcDentalHardening}

The implementation keeps the dental-hardening step explicit.

```foma
define PWGmcDentalHardening [
    {*ð} -> {*d}
];
```

In prose, the rule turns voiced dental fricative \emph{*ð} into stop \emph{*d}. It preserves a systemic step in the consonant history, not a single isolated lexical anecdote.

Its chronology is deliberately modest. If [SC013 PWGmcDentalHardening](#rule-PWGmcDentalHardening) is moved earlier within the tested range, it crosses [SC012 PWGmcLThVoicing](#rule-PWGmcLThVoicing), [SC011 PWGmcSyllabicJ](#rule-PWGmcSyllabicJ), [SC010 PWGmcJGemination](#rule-PWGmcJGemination), [SC009 PWGmcIjContraction](#rule-PWGmcIjContraction), [SC008 PWGmcCoronalWAssimilation](#rule-PWGmcCoronalWAssimilation), [SC007 PWGmcFinalOrLowering](#rule-PWGmcFinalOrLowering), [SC006 PWGmcEarlyIApocope](#rule-PWGmcEarlyIApocope), [SC005 NWGmcAToUBeforeM](#rule-NWGmcAToUBeforeM), and [SC004 PWGmcAiMonophthongization](#rule-PWGmcAiMonophthongization) safely to order `4` and then reaches the start of the tested expanded-PWGmc chain with no real break. If it is moved later, the search reaches order `86`, the current [SC087 OERMetathesis](#rule-OERMetathesis) boundary, with no real break. The order evidence is therefore negative or boundary-only on both sides. It does not place the rule before or after any specific neighboring stage. The rule is included because the source support for dental hardening itself is strong, and the order test supplies no positive local boundary.

The prose should therefore stay precise and systemic. Neither side of the current order evidence provides a positive local anchor.
