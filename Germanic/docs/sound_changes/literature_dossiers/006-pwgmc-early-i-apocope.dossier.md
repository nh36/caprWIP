# SC006 Early i-apocope — literature dossier

## Historical phenomenon

This dossier concerns the early loss of final `*i` after unstressed syllables before later i-umlaut, especially in inflectional endings and in the `youth` family.

## CAPR rule

- change_id: `SC006`
- display_name: `PWGmc Early I Apocope`
- rule_name: `PWGmcEarlyIApocope`
- FOMA definition: deletion of final `*i` after a stressed syllable plus an additional unstressed syllable and consonant group, with optional final `*z`

## Example lexemes

1. `thousand`
2. `bore (3sg)`
3. `have`
4. `learn (3sg)`
5. `lick (3sg)`

## Source support found so far

1. Sievers/Brunner argues that the early Common-Germanic loss of final `-i` after unstressed syllables is proved by the absence of later i-umlaut [@SieversBrunner1965, §§145--146].
2. Ringe and Taylor give the classic `youth` example directly: `*jugunþi > *juguþ > OE geoguþ ~ iuguþ` [@RingeTaylor2014, p. 141].
3. Campbell cites outcomes such as `dugup` and `geogup` in the same area of discussion [@Campbell1959, §332].

## Missing source support

1. The current source pass is strongest on the suffixal evidence and the `youth` family.
2. It does not yet supply equally explicit source discussion for every inventory witness such as `have`, `learn (3sg)`, or `lick (3sg)`.

## Chronology/order-test status

1. No validated chronology card exists yet.
2. The old batch-04 manifest skipped SC006 only because `PWGmcChanges` was still bundled for first-break purposes.
3. The current runner can now test SC006 directly with `--order-profile expanded-pwgmc`.
4. No real first-break TSV output exists yet, so no validated earlier or later boundary is currently available.

## Cautions for eventual reader-facing prose

1. Emphasize the chronological importance of the rule for blocking later i-umlaut where the final trigger has already disappeared.
2. Do not state a chronology boundary until real first-break TSV output exists.
3. A later reader-facing chapter should probably foreground the suffixal evidence and `geoguþ`, then treat the other trace examples as supporting detail.
