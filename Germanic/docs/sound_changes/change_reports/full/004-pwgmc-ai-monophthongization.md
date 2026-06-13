# PWGmc ai-monophthongization

### Sound-change report

#### Historical formulation

SC004 `PWGmcAiMonophthongization` packages the West Germanic monophthongization of inherited `*ai`, including the special word-final unstressed outcome that merges with long mid `*ē`. In the inventory and trace output the rule is visible across a broad set of lexical families such as `bone`, `deal`, `dough`, `flesh`, and `ghost`.

That makes it historically recognizable, but the present source support is uneven. The clearest repository sources recovered in this pass speak most directly to the unstressed and especially word-final `*ai` outcomes. The broader nonfinal `*ai > *ā` side of the CAPR rule is therefore more explicit in the implementation than in the currently assembled handbook prose.

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

In the inventory ordering, SC004 is the first member of the Proto-West-Germanic bundle and stands immediately before SC005 `NWGmcAToUBeforeM`. In the live pipeline it still sits inside bundled `PWGmcChanges`, but the first-break runner now has an `expanded-pwgmc` order profile that exposes SC004 explicitly for chronology testing without changing the production cascade.

That means the rule now occupies a clearer backend position than it did when the old batch manifest was written. It remains a bundled production rule in the live cascade, but it is no longer blocked from first-break testing in principle.

#### Order evidence

No validated chronology card exists yet for SC004. The older `order_sensitivity_first_break_batch_04_manifest.tsv` marks SC004 as skipped only because that batch used the default bundled profile, where `PWGmcChanges` was not yet expanded into explicit reorderable members.

The current runner can now test SC004 directly through:

1. `--mode first-break`
2. `--order-profile expanded-pwgmc`
3. separate first-break output paths away from the default bundled-profile corpus

In this pass only the lightweight dry-run order inspection was performed. Real earlier/later chronology evidence therefore still depends on future first-break TSV output and should not yet be stated as a historical boundary claim.

#### Interpretation

SC004 is strong enough for backend preparation as a likely singleton opener. The historical phenomenon is real, the trace weight is substantial, and the runner can now test it directly. What is still missing is validated first-break output and somewhat firmer source coverage for the broader nonfinal monophthongization side of the CAPR rule.

#### Remaining cautions

The chief caution is scope. The retrieved sources in this pass support the unstressed `*ai` monophthongization clearly, but they do not yet support every detail of CAPR's wider `*ai -> *ā` packaging equally explicitly. Until real first-break TSV output exists and the source base for the broader side is strengthened, SC004 should remain out of `report_manifest.tsv`.
