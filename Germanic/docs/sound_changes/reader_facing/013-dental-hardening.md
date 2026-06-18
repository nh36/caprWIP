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

Its chronology is deliberately modest. If the rule is moved earlier or later within the tested sequence, no checked form yields a form different from the expected one. The tested forms therefore do not place [SC013 PWGmcDentalHardening](#rule-PWGmcDentalHardening) before or after any specific neighboring stage.

That does not make the change itself doubtful. The comparative history of dental hardening in early West Germanic is clear, so CAPR keeps the rule here as a broad systemic consonant development. The placement should be read as approximate and source-based, while the tested forms leave the exact local neighborhood open. From here the sequence turns to [SC014 NWGmcUnstressedAiMonophthongization](#rule-NWGmcUnstressedAiMonophthongization) and [SC015 NWGmcILowering](#rule-NWGmcILowering), where the first unstable unstressed vowels come into view.
