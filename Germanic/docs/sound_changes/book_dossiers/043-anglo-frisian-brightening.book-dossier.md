# SC043: Anglo-Frisian Brightening

## 1. Role in the book

SC043 is a strong pilot case for the sound-change half of the book because all of the main dossier layers already exist in usable form. It has a substantial literature dossier, a pilot change-entry scaffold, a compact and historically interpretable chronology card, and a short FOMA definition whose consequences are easy to narrate through familiar examples such as `day`, `beard`, and `bake`.

It is also a good pilot because it shows what the sound-change half of the book should do well: not merely name a rule, but explain how a formally implemented change sits inside a larger cascade in which later rules can both depend on it and partly hide it. Anglo-Frisian Brightening is therefore a good test of whether a mini-chapter can move cleanly from handbook phonology to formal implementation to local chronology without letting the graph/export layer become the main object.

## 2. Name and basic formulation

- **change_id:** `SC043`
- **display_name:** `Anglo Frisian Brightening`
- **rule_name:** `AngloFrisianBrightening`
- **current_order:** `43`
- **card:** `Germanic/docs/sound_changes/order_tests/chronology_cards/SC043-anglo-frisian-brightening.md`

Short formulation: SC043 fronts low Germanic `a` to fronted `æ`-type outputs outside nasal environments, with a special long-final clause for the surviving bimoric `*-ō > *-ā` pathway. In the live EnglishProtoToOE cascade, this fronting creates the input that later rules such as OE Breaking and OE A Restoration either exploit or partially reverse.

## 3. Traditional description and literature

The literature dossier confirms that the standard handbook picture is stable. Campbell gives the classical statement: **"By a very early change Prim. Gmc. a > æ in OE and OFris. when not followed by a nasal consonant."** Hogg gives the most familiar modern label pair and formulation: **"This vowel normally fronted to /ae/ by the sound change of Anglo-Frisian Brightening (or First Fronting)."** Ringe and Taylor sharpen the relative chronology by stating that retraction must be later than both fronting and breaking, while Fulk gives a compact bridge from brightening to later breaking and retraction patterns.

What is standard in the literature is therefore clear:

1. low `a` fronts outside nasal environments;
2. the change is early;
3. OE Breaking presupposes that fronted input;
4. later restoration/retraction is later than the fronting event.

What remains uncertain or disputed is not the local rule itself so much as its wider historical framing. The dossier notes Campbell's caution that English and Frisian may not simply reflect one undifferentiated shared event, and Ringe and Taylor leave open whether the wider spread of fronted outcomes happened mainly on the continent or in Britain. There is also a presentational question about how prominently to foreground the unstressed-vowel side of the change in book prose.

What CAPR adds is not a new historical claim but a tighter formal and chronological articulation. The repository formalization makes explicit:

1. an unstressed clause;
2. a stressed clause;
3. a long-final clause linked to the surviving-bimoric `ō` pathway;
4. a locally testable order relation to SC042, SC044, and SC046.

That combination turns a familiar handbook change into a mini-chapter that can show how formal implementation, chronology testing, and literary exposition fit together.

## 4. Formal implementation

The relevant FOMA material in `Germanic/fsts/germanic.txt` is short enough to quote directly:

```foma
define AngloFrisianBrighteningUnstressed [
    {*a} -> {*æ} || _ [EnglishStarConsonant - EnglishStarNasal]
];
define AngloFrisianBrighteningStressed [
    {*á} -> {*æ} || _ [EnglishStarConsonant - EnglishStarNasal | .#.]
];
define AngloFrisianBrighteningLongFinal [
    {*ā} -> {*ǣ} || EnglishStarVocalic [EnglishStarConsonant | EnglishPalatalConsonant]+ _ .#.
];
define AngloFrisianBrightening [
    AngloFrisianBrighteningUnstressed .o.
    AngloFrisianBrighteningStressed .o.
    AngloFrisianBrighteningLongFinal
];
```

This is mostly a straightforward formalization of the handbook rule, but two caveats matter.

First, the **unstressed clause** is more model-explicit than many short textbook descriptions, though the literature dossier notes that Hogg gives support for extending first fronting into the unstressed system. Second, the **long-final clause** is best read as a formal approximation used to preserve a historically motivated chain across SC042 and later unstressed-long-vowel shortening. In other words, the rule is historically serious, but the exact shape of the FOMA definition is tuned to how this cascade represents intermediate states rather than to a single line in any one handbook.

**Long-final clause narrowing (corpus-maturation pass 01).** The clause was introduced solely for the surviving-bimoric pathway — unstressed final `*-ā` (from `*-ō`) in polysyllables [@RingeTaylor2014, §3.1 pp. 58–59; §6.8.3 pp. 299–300] — but its original context `_ .#.` was broader than that intent and wrongly captured the long `ā` of stressed monosyllables created by SC097 monosyllabic final `*-z` loss. The decisive case is OE *hwā* 'who': Ringe & Taylor derive "PGmc *hwaz > PWGmc *hwaz > OE, OF hwā" with the back vowel intact [@RingeTaylor2014, p. 86]; Campbell states flatly that "the form with West Gmc. lengthening (OE *hwǣ) does not exist" [@Campbell1959, §125, p. 49]; Brunner concurs that no `æ`/`ē` forms occur beside *hwā* [@SieversBrunner1965, §137 Anm. 1, p. 129]. The clause now requires a preceding nucleus (the same "preceded by another nucleus" guard used by `PWGmcSurvivingBimoricOUnrounding`), restricting it to exactly the polysyllabic surviving-bimoric class the sources describe. Validated: all 380 legacy corpus outputs unchanged; `*xwáz` now yields *hwā*. See `audits/corpus-maturation-01-candidate-adjudication.md` §1.

## 5. Place in the cascade

In `EnglishProtoToOE`, SC043 sits inside a very tight local cluster:

```foma
.o. PWGmcFinalBareALoss
.o. PWGmcSurvivingBimoricOUnrounding
.o. AngloFrisianBrightening
.o. OEBreaking
.o. OEVelarFricativePalatalization
.o. OEARestoration
```

For book purposes, the important point is that Anglo-Frisian Brightening is not an isolated vowel shift. It is a **pivot**:

1. SC042 feeds it on the left in the surviving-bimoric `ō` pathway;
2. SC044 depends on it immediately on the right;
3. SC046 later undoes part of its work in back-vowel environments;
4. the export layer also shows a contextual earlier-side support row from `SC035 -> SC043`.

The current graph/export layer records these neighboring relations:

1. **core:** `SC042 < SC043` (reciprocal support)
2. **core:** `SC043 < SC044` (reciprocal support)
3. **core:** `SC043 < SC046`
4. **core:** `SC034 < SC043`
5. **contextual:** `SC035 < SC043`

That makes SC043 especially useful as a pilot mini-chapter: it is locally well anchored, but it also has enough forward and backward links to demonstrate how one rule can organize a small section of the cascade.

## 6. Order-testing evidence

The chronology card gives a **safe computational window of `43-43`**. In other words, the rule is tightly fixed at its current point.

- **earlier boundary:** `SC042` PWGmc Surviving Bimoric O Unrounding
- **representative failure:** `rest`
- **later boundary:** `SC044` OE Breaking
- **representative failure:** `slay`

The evidence is best described as **local and reciprocal**, with an additional contextual earlier-side support row from SC035. The earlier boundary is historically interpretable because the `rest` derivation only reaches the attested fronted/restored output when the SC042 pathway has already produced the right input. The later boundary is equally interpretable because breaking must operate on the fronted vowel created by SC043; if SC043 is delayed, `*sláxaną` yields `sleaan | slēaan` instead of `slēan`.

What this evidence **does** show is that the live cascade has a robust local dependency:

1. SC043 must follow SC042;
2. SC043 must precede SC044;
3. SC043 must also precede SC046 in the wider local neighborhood.

What it **does not** prove by itself is the full historical interpretation of Anglo-Frisian subgrouping or the entire prehistoric chronology of fronting, breaking, and restoration. The order-testing layer records transducer failure behavior. It is strongest when it confirms local dependencies already expected from the literature, which is exactly what happens here.

## 7. Interpretation for the book

For the book, SC043 should be treated as an early fronting rule whose importance lies not only in its own outputs but also in the way later OE developments repeatedly presuppose and then partly obscure it. That is the core narrative value of the chapter.

The prose should therefore present Anglo-Frisian Brightening as an **enabling change**: it creates the front-vowel stage on which breaking operates and from which later restoration retreats in specific environments. In literary terms, this is not a chapter about a single visible surface reflex; it is a chapter about a stage that is often recoverable only because later rules still betray its prior existence.

## 8. Relation to neighbouring changes

1. **SC042 PWGmc Surviving Bimoric O Unrounding:** immediate left-hand reciprocal partner; important for `rest` and for the long-final clause in the implementation.
2. **SC044 OE Breaking:** immediate right-hand reciprocal partner; brightening must feed breaking.
3. **SC046 OE A Restoration:** later rule that reverses part of SC043's effect before back-vowel environments; crucial for forms like `bake` and `fare`.
4. **SC034 OE Aw Long Diphthong:** earlier core neighbor in the export layer, useful as a wider local anchor.
5. **SC035 OE Prefix A Reduction Early:** contextual earlier-side support only; worth noting, but not a core local adjacency claim.

These links show why SC043 is better treated as a **cluster-organizing** chapter than as a rule described in isolation.

## 9. Remaining uncertainty

1. The chapter still needs a human decision on whether to foreground **Anglo-Frisian Brightening** or **First Fronting** as the primary heading term.
2. The unstressed clause in the FOMA rule is defensible, but the final book prose should decide how prominently to feature it.
3. The wider historical question of English-Frisian subgrouping should be handled carefully; the local chronology is strong, but the broader historiography remains more cautious.
4. Final publication-quality quotations should still be checked against page images where appropriate, even though the current dossier is already strong enough for prose drafting.
5. The eventual volume will need a stylistic decision about how tightly to bind SC043 to the later chapters on Breaking and A Restoration.

## 10. Proposed book-section outline

1. **Anglo-Frisian Brightening / First Fronting**
2. **The basic change: `a > æ` outside nasal environments**
3. **How later OE rules mask the fronted stage**
4. **Formal implementation in CAPR**
5. **Why SC042 must precede it**
6. **Why SC044 must follow it**
7. **Restoration and the partial retreat from brightening**
8. **What the local chronology shows, and what it does not show**
9. **Open historiographical cautions**
