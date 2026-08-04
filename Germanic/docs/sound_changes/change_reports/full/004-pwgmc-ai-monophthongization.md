# PWGmc ai-monophthongization

### Sound-change report

#### Historical formulation

SC004 `PWGmcAiMonophthongization` packages the West Germanic monophthongization of inherited `*ai`, including the special word-final unstressed outcome that merges with long mid `*ē`. In the inventory and trace output the rule is visible across a broad set of lexical families such as `bone`, `deal`, `dough`, `flesh`, and `ghost`.

That makes it historically recognizable, but the present source support is uneven. The clearest sources assembled here speak most directly to the unstressed and especially word-final `*ai` outcomes. The broader nonfinal `*ai > *ā` side of the CAPR rule is therefore more explicit in the implementation than in the currently assembled handbook prose.

#### Source tradition

Ringe and Taylor treat the monophthongization of unstressed `*ai` as one of the most widespread post-PNWGmc vowel shifts and illustrate it with endings such as PGmc dat. sg. `*-ai`, subjunctive `*-ai`, and strong adjective plural `*-ai`, all of which surface in Northwest Germanic as long mid reflexes [@RingeTaylor2014, pp. 40--41]. Fulk likewise lists the development of unstressed `ai` and `au` among the important similarities shared by North and West Germanic against Gothic [@Fulk2018, §5.2].

That is solid support for the historical phenomenon at least on the unstressed side. It is weaker support for the full CAPR packaging, because the retrieved sources here do not yet give a comparably explicit handbook statement for the wider nonfinal `*ai > *ā` generalization reflected in the trace examples `bone`, `deal`, `dough`, `flesh`, and `ghost`. A fuller source pass should therefore strengthen that side before any broader narrative treatment is attempted.

#### CAPR implementation

CAPR models the change as a single explicit West Germanic stage with a word-final split:

```foma
define PWGmcAiMonophthongization [
    [{*ai} -> {*ē} || _ .#.]
    .o.
    [{*ai} -> {*ā}]
    .o.
    [{*ái} -> {*ā}]
];
```

This implementation is sharper than the narrowest handbook wording recovered in this pass. The special word-final `*ai -> *ē` outcome maps directly onto the retrieved historical discussion, while the broader `*ai -> *ā` generalization functions as CAPR's unified treatment of the wider monophthongization pattern.

#### Place in the cascade

In the inventory ordering, SC004 is the first member of the Proto-West-Germanic bundle and stands immediately before SC005 `PNWGmcAToUBeforeM`. In the live pipeline it still sits inside bundled `EarlyEnglishLineChanges`, but the first-break runner now has an `expanded-pwgmc` order profile that exposes SC004 explicitly for chronology testing without changing the production cascade.

That means the rule now occupies a clearer position in the cascade evidence. It remains a bundled production rule in the live cascade, but it is no longer blocked from first-break testing in principle.

#### Order evidence

Validated order evidence now exists through the expanded-PWGmc first-break output family:

1. `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_expanded_pwgmc_sc004_006_01.tsv`
2. `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_expanded_pwgmc_sc004_006_01_changes.tsv`
3. `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_expanded_pwgmc_sc004_006_01_failures.tsv`

The earlier search stops immediately at the left edge of the tested expanded-PWGmc chain. SC004 is already the first explicitly testable rule in that profile, so the earlier side is boundary-only rather than a positive chronology constraint.

The later search does find a real historical break at order `36` across `SC036` OE Inter Stress Raising. If PWGmc Ai Monophthongization is delayed that far, PGmc `*sáiwalō` yields `sāwel` rather than `sāwol`.

That later boundary is historically interpretable, but it is broad/far rather than a tight local adjacency claim.

#### Interpretation

SC004 works best as a short singleton opening note. The historical phenomenon is real, the chronology layer now gives one usable later boundary, and the source base is strong enough to support the unstressed and word-final side of the change. The report should nevertheless remain modest, because the broader nonfinal `*ai > *ā` packaging is still more explicit in CAPR than in the currently assembled handbook prose.

#### Remaining cautions

The chief caution is scope. The retrieved sources support the unstressed `*ai` monophthongization clearly, but they do not yet support every detail of CAPR's wider `*ai -> *ā` packaging equally explicitly. The earlier side of the chronology card is also only a tested-chain boundary, while the later `SC036` relation is broad/far rather than local. Those limits should remain visible even in a cautious singleton note.
