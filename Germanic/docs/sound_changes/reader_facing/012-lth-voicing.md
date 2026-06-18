# \emph{lþ}-voicing

## Historical discussion

Ringe and Taylor treat word-internal \emph{*lþ} > \emph{*ld} as a regular sound change in northern West Germanic and illustrate it with forms such as *fealdan*, *beald*, *wuldor*, and *gylden* [@RingeTaylor2014, pp. 170--171]. Campbell gives a similar West-Germanic-facing formulation with examples such as *fealdan*, *wuldor*, *beald*, *gold*, and *feld* [@Campbell1959, p. 169, §414].

That makes the change substantial enough for a short chapter, but the scope should stay cautious. The internal CAPR implementation places the rule at this early stage, while the source discussion points most clearly to a northern West Germanic development. It does not support an unqualified pan-PWGmc law.

## SC012. \emph{lþ}-voicing (`PWGmcLThVoicing`) {#rule-PWGmcLThVoicing}

The implementation keeps the \emph{lþ > ld} step explicit.

```foma
define PWGmcLThVoicing [
    {*θ} -> {*d} || {*l} _
];
```

In prose, the rule voices \emph{*lþ} to \emph{*ld}. This is the development behind families such as `field`, `fold`, `gold`, and `wold`, while the historical discussion keeps the scope cautious about how widely the rule should be projected.

Its chronology is deliberately modest. If [SC012 PWGmcLThVoicing](#rule-PWGmcLThVoicing) is moved earlier within the tested range, it crosses [SC011 PWGmcSyllabicJ](#rule-PWGmcSyllabicJ), [SC010 PWGmcJGemination](#rule-PWGmcJGemination), [SC009 PWGmcIjContraction](#rule-PWGmcIjContraction), [SC008 PWGmcCoronalWAssimilation](#rule-PWGmcCoronalWAssimilation), [SC007 PWGmcFinalOrLowering](#rule-PWGmcFinalOrLowering), [SC006 PWGmcEarlyIApocope](#rule-PWGmcEarlyIApocope), [SC005 NWGmcAToUBeforeM](#rule-NWGmcAToUBeforeM), and [SC004 PWGmcAiMonophthongization](#rule-PWGmcAiMonophthongization) safely to order `4` and then reaches the start of the tested expanded-PWGmc chain with no real break. If it is moved later, the search reaches order `86`, the current [SC087 OERMetathesis](#rule-OERMetathesis) boundary, with no real break. The order test therefore does not place [SC012 PWGmcLThVoicing](#rule-PWGmcLThVoicing) before or after any specific neighboring stage.

The chronology is weak on both sides. No exact wrong output is available in either direction, because neither side yields a historical first-break witness. The rule is included because the source support for the \emph{lþ > ld} development is strong, not because the order test supplies a positive local boundary. Its place here is best read as an informed placement within the early consonant sequence, guided by the comparative evidence for northern West Germanic \emph{lþ}-voicing rather than by a close diagnostic failure. After this scope-limited note, [SC013 PWGmcDentalHardening](#rule-PWGmcDentalHardening) returns to a broader systemic consonant adjustment.
