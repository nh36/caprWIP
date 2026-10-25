# Technical support: palatalized-glide long-io realization

## SC110. Palatalized-glide long-io realization (`OEJGlideIO`) {#rule-OEJGlideIO}

```foma
define OEJGlideIO Ctx([
    [{*iu}|{*íu}] -> {*īo} || _ {*w} {*j}
]);
```

The palatalized-glide product realizes long \emph{īo}, not the
ordinary long \emph{ēo} supplied by
[SC032 OEDiphthongLeveling](#rule-OEDiphthongLeveling).
Ringe and Taylor explicitly supply pre-OE long \emph{īow} and early
West Saxon long \emph{īew}; the retained semivowel still conditions
mutation [@RingeTaylor2014, p. 250].
Existing [SC055 OEIUmlaut](#rule-OEIUmlaut) supplies the latter
change. Ordinary inherited \emph{iu} without this palatal
conditioner remains outside the component, as does short
\emph{io}. This distinct realization does not adjudicate all the
inherited atomic and split-symbol clauses in
[SC032 OEDiphthongLeveling](#rule-OEDiphthongLeveling).
