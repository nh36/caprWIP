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

Its chronology is deliberately modest. If the rule is moved earlier or later within the tested sequence, no checked form yields a form different from the expected one. The tested forms therefore do not place [SC012 PWGmcLThVoicing](#rule-PWGmcLThVoicing) before or after any specific neighboring stage.

That does not make the change itself doubtful. The comparative evidence for northern West Germanic \emph{lþ > ld} is strong, so CAPR keeps the rule here as an early consonant note. The placement should be read as approximate and source-based, not as a local ordering forced by the checked forms. After this scope-limited note, [SC013 PWGmcDentalHardening](#rule-PWGmcDentalHardening) returns to a broader systemic consonant adjustment.
