# SC014 NWGmc Unstressed Ai Monophthongization — chronology evidence card

> **Split note (SC004 Outcome-C).** SC014 is now a standalone rule: word-final
> unstressed `*-ai > *-ē` (early Proto-Northwest Germanic), split out of the
> former bundled SC004 `PWGmcAiMonophthongization`. It replaces the earlier no-op
> `{*ăi} -> {*ē}` card, which was a placeholder with no live rule. The general
> `*ai/*ái > *ā` development is now SC004 `EAFAiMonophthongization` (see
> `SC004-pwgmc-ai-monophthongization.md` and `SC004-components-chronology.md`).

## Current position
- current_order (SC id): `14`
- executable cascade position: `1` (head of `EarlyEnglishLineChanges`, the former SC004 slot)
- rule_name: `PNWGmcUnstressedAiMonophthongization`
- former_rule_name: `NWGmcUnstressedAiMonophthongization`
- live Foma rule: `{*ai} -> {*ē} || _ .#.` (explicit word-final environment)
- safe computational window: **unconstrained** — zero corpus applications
- status: `corpus_inert`

## Earlier boundary
- first earlier break: `none — no corpus witness can be crossed`
- crossed stage: `n/a`
- crossed stage type: `no_corpus_load`
- failure count: `0`
- representative failures: `none`
- concrete failure example: `none — SC014 fires on zero corpus lexemes`
- interpretation: No Old English corpus lexeme carries word-final unstressed `*-ai`; SC014's historical witnesses are inflectional endings (dat.sg `*-ai`, subjunctive `*-ai`, strong-adj pl `*-ai`), not standalone lexemes. There is therefore no earlier break to find.

## Later boundary
- first later break: `none — no corpus witness can be crossed`
- crossed stage: `n/a`
- crossed stage type: `no_corpus_load`
- failure count: `0`
- representative failures: `none`
- concrete failure example: `none — SC014 fires on zero corpus lexemes`
- interpretation: Because SC014 rewrites zero corpus forms, moving it to any cascade position leaves every corpus output unchanged. It has no positive chronology boundary of any kind.

## Chronology statement
SC014 is **corpus-inert** in the current lexical dataset: it has no first-break
boundary in either direction because no corpus derivation passes a word-final
unstressed `*-ai`. Its correct historical stage — early Proto-Northwest Germanic,
with the `*ē` outcome merging into long mid `*ē` — is established by comparison of
inflectional endings and by the literature (R/T pp. 40–41, §6.1.5; Fulk §5.2),
not by any CAPR derivational witness. Its cascade position (executable pos 1) is
therefore historically motivated but computationally free.

## Caveats
This card records a corpus-inert result: SC014 imposes no cascade-order
constraint and cannot be constrained (or justified) by first-break testing. The
earlier negative card that reported a runner limitation against the bundled
`PWGmcChanges` is superseded — the limitation was an artefact of SC014 sharing a
rule with the general change, which the split removes.

## Source files
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_changes.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_failures.tsv`
- `Germanic/docs/sound_changes/sound_change_order_sensitivity.tsv`
