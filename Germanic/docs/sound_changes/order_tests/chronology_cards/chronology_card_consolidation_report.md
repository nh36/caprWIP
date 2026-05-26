# Chronology card consolidation report

## Completed coverage so far

The current chronology-card set now covers sixty-four tested rules:

1. `SC020`, `SC021`, `SC022`, `SC023`, `SC024`, `SC025`, `SC026`, `SC027`, `SC028`, `SC029`, `SC030`, `SC031`, `SC032`, `SC033`, `SC034`, `SC035`, `SC036`, `SC037`, `SC039`, `SC040`, `SC041`, `SC042`, `SC043`, `SC044`, `SC045`, `SC046`, `SC047`, `SC048`, `SC049`, `SC050`, `SC051`, `SC052`, `SC053`, `SC054`, `SC055`, `SC056`, `SC057`, `SC058`, `SC059`, `SC060`, `SC061`
2. `SC063`, `SC064`, `SC065`, `SC066`, `SC067`, `SC068`, `SC069`, `SC070`, `SC071`, `SC072`, `SC073`, `SC074`, `SC075`, `SC076`
3. `SC078`, `SC079`, `SC080`, `SC081`, `SC082`, `SC083`, `SC085`, `SC086`, `SC087`

This means the lower-early batch, the upper-early batch, the pilot rules, batch 04, batch 05, the scaled batch, the gap-filling batch, the late-corridor batch, and the far-late batch are all now represented in a single indexed card set. The refreshed `chronology_card_index.tsv` records the current order, safe window, boundary type, failure counts, reciprocal status, broad-boundary flags, and runner-bounded or non-historical cautions for each completed card.

## Strong reciprocal boundaries found so far

The strongest reciprocal or near-reciprocal relations visible in the current card set are:

1. `SC026` / `SC027`: `SC026` later and `SC027` earlier now form a tight reciprocal three-row boundary around `fȳst`, `gōs`, and `ġeoguþ`.
2. `SC029` / `SC030`: `SC029` later and `SC030` earlier form a tight reciprocal `hay` / `strew` boundary around `hīeġ` / `hauġ` and `strīeġan` / `strauian`.
3. `SC030` / `SC032`: `SC030` later and `SC032` earlier form a reciprocal eighteen-row no-output boundary around forms such as `ġelīefan`, `brēad`, and `drēam`.
4. `SC031` / `SC034`: `SC031` later and `SC034` earlier form a tight reciprocal `dēaw` / `dawu` and `hēawan` / `hawan` relation.
5. `SC039` / `SC040`: `SC039` later and `SC040` earlier form a reciprocal `widow` boundary around `wuduwe` / `wudowe`.
6. `SC042` / `SC043`: `SC042` later breaks across `SC043`, and `SC043` earlier breaks across `SC042`.
7. `SC043` / `SC044`: `SC043` later breaks across `SC044`, and `SC044` earlier breaks across `SC043`.
8. `SC044` / `SC045`: `SC044` later breaks across `SC045`, and `SC045` earlier breaks across `SC044`.
9. `SC047` / `SC048`: `SC047` later and `SC048` earlier share the same 87-row broad `-en` failure set.
10. `SC050` / `SC052`: `SC050` later and `SC052` earlier form a concrete local relation around `stretch`; `SC050` earlier is still runner-bounded and is not part of a reciprocal historical pair.
11. `SC052` / `SC055`: `SC052` later and `SC055` earlier form a tight reciprocal relation around `cow` and `lung`.
12. `SC055` / `SC056`: `SC055` later and `SC056` earlier form a reciprocal boundary around `gift` and `sheath`.
13. `SC064` / `SC072`: `SC064` later and `SC072` earlier form a reciprocal `fright`-based boundary.
14. `SC066` / `SC068`: `SC066` later and `SC068` earlier form a reciprocal `spindle`-based relation inside the syncope / degemination corridor.
15. `SC070` / `SC071`: `SC070` later and `SC071` earlier form a reciprocal six-row unstressed-fronting relation around forms such as `boraþ` / `boreþ` and `mōnaþ` / `mōneþ`.
16. `SC072` / `SC073`: `SC072` later and `SC073` earlier form a reciprocal broad unstressed-vowel boundary.
17. `SC074` / `SC075`: `SC074` later and `SC075` earlier form a reciprocal `shilling`-based boundary.
18. `SC079` / `SC080`: `SC079` later and `SC080` earlier form a tight reciprocal `lungen` / `lungenn` relation.
19. `SC081` / `SC082`: `SC081` later and `SC082` earlier form a reciprocal `strew`-based boundary.
20. `SC082` / `SC083`: `SC082` later and `SC083` earlier form a reciprocal eight-row verbal boundary around `borian`, `handlian`, `liornian`, `liccian`, and related forms.
21. `SC085` / `SC086`: `SC085` later and `SC086` earlier form a reciprocal four-row contraction boundary around `flēon`, `slēan`, `tēon`, and `tā`.

The older one-sided links still matter too: `SC020` later points to `SC040`, `SC021` later points to `SC040`, `SC023` later points to `SC047`, `SC024` later points to `SC056`, `SC032` later points to `SC040`, `SC035` later points to `SC043`, `SC036` later points to `SC040`, `SC063` later points to `SC072`, `SC073` later points to `SC085`, and `SC059` later points to `SC078`, even though those are not all full reciprocal pairs.

## Broad computational boundaries

Several boundaries need explicit broad-boundary handling rather than narrow adjacency prose:

1. `SC020` later breaks far away at `SC040`, so it should not be narrated as if it were tightly adjacent to OE Med Unstressed U Lowering.
2. `SC021` later also breaks only at `SC040`, so it should likewise stay broad rather than local.
3. `SC023` later breaks far away at `SC047`, and the resulting `do` failure is a no-output (`+?`) derivation.
4. `SC024` later breaks far away at `SC056`, so it should not be flattened into a local adjacency claim.
5. `SC033` later breaks far away at `SC044`, so it should not be narrated as if it were tightly adjacent to OE Breaking.
6. `SC036` earlier breaks far back at `SC019`, even though the current failure set is narrow and centered on `soul`.
7. `SC040` later breaks far away at `SC072`, so it should not be narrated as a tight neighboring-stage adjacency.
8. `SC041` earlier breaks far away at `SC020` with 64 newly failing rows and a large class of spurious `-a`-final outputs.
9. `SC047` later and `SC048` earlier form the reciprocal 87-row `-en` failure set.
10. `SC069` earlier breaks far away at `SC023` with 17 newly failing rows that broadly restore final `-an` outcomes such as `nǣdran`, `eorþan`, and `flascan`.
11. `SC072` later and `SC073` earlier form a reciprocal 24-row `-æ` boundary.
12. `SC078` earlier breaks across `SC070` with another 87-row `-en` failure set.
13. `SC079` earlier breaks broadly across `SC055` with 26 newly failing rows, not with a tight one-lexeme adjacency.
14. `SC081` earlier also breaks far back across `SC055`, even though the current failure set is narrow and centered on `strew`.
15. `SC087` earlier breaks far away at `SC044`, so it should not be narrated as if it were tightly adjacent to the breaking stage.

These cards support later chronology prose, but the prose must not flatten them into single-lexeme adjacency claims. The index marks these sides in `broad_boundary_side` so they can be filtered during later chapter drafting.

## Non-historical computational breaks

Three tested sides currently produce real computational first breaks that should still be kept out of ordinary historical chronology prose:

1. `SC031` earlier crosses bundled `PWGmcChanges` at order `13`.
2. `SC033` earlier also crosses bundled `PWGmcChanges` at order `13`.
3. `SC037` later crosses `SC038` OE Strip Secondary Stress, a technical marker rather than an ordinary historical sound change.

These sides matter as computational evidence, but they should be narrated as non-historical / runner-limited / technical-marker cases rather than as normal chronology constraints.

## Runner-bounded / no-break sides

The runner-bounded set now falls into three groups:

1. Earlier searches blocked by bundled `PWGmcChanges` with no real break: `SC021`, `SC022`, `SC023`, `SC024`, `SC025`, `SC026`, `SC028`, `SC029`, `SC035`, `SC037`, `SC039`, `SC050`, `SC053`, `SC058`, `SC065`, `SC067`, `SC076`
2. Later searches that found no real break through last safe order `86` before the current `SC087` search boundary: `SC022`, `SC025`, `SC027`, `SC028`, `SC049`, `SC053`, `SC056`, `SC057`, `SC058`, `SC060`, `SC061`, `SC065`, `SC067`, `SC068`, `SC069`, `SC071`, `SC075`, `SC076`, `SC080`, `SC083`, `SC086`
3. The terminal later search for `SC087`, which found no real break beyond current order `86` before the current runner limit

These sides are computational boundary observations, not positive historical claims about `SC087` or about specific earlier bundled stages.

## Cards normalized in this pass

All chronology cards still share the same section order:

1. `Current position`
2. `Earlier boundary`
3. `Later boundary`
4. `Chronology statement`
5. `Caveats`
6. `Source files`

This pass extended the normalized card set by:

1. adding cards for `SC020`, `SC021`, `SC022`, `SC023`, `SC024`, `SC025`, `SC026`, `SC027`, `SC028`, and `SC029`
2. refreshing the README so the lower-early runner-limited and no-break cases are explicit
3. refreshing the index so the new reciprocal pairs, broad boundaries, and negative cards are searchable
4. preserving concrete PGmc > expected OE vs variant OE contrasts from the failures TSV
5. preserving `+?` rows in prose as no-output / failed derivations rather than rewriting them as surface forms

## Issues for human review

The current card set is usable, but several issues still need care before these constraints are turned into chapter prose:

1. `SC023` later records `+?`, so the `do` failure must be narrated as a no-output / failed derivation, not as a surface OE form.
2. `SC031` earlier and `SC033` earlier cross bundled `PWGmcChanges`, so they are non-historical computational breaks rather than ordinary chronology constraints.
3. `SC037` later crosses technical-marker `SC038`, so it is a real computational break but not an ordinary historical boundary.
4. `SC020` later, `SC021` later, `SC023` later, and `SC024` later are all broad/far boundaries, so the wording should stay broad and computational rather than local and adjacency-like.
5. `SC033` later, `SC036` earlier, `SC040` later, `SC041` earlier, `SC069` earlier, `SC079` earlier, `SC081` earlier, and `SC087` earlier remain broad/far boundaries that should not be flattened into tight neighboring-stage claims.
6. The 87-row broad failure sets (`SC047` later, `SC048` earlier, `SC078` earlier) still need careful narrative treatment.
7. `SC021`, `SC022`, `SC023`, `SC024`, `SC025`, `SC026`, `SC028`, `SC029`, `SC035`, `SC037`, `SC039`, `SC050`, `SC053`, `SC058`, `SC065`, `SC067`, and `SC076` earlier are runner-boundary results inside bundled `PWGmcChanges`, not historical boundaries.
8. `SC022`, `SC025`, `SC027`, `SC028`, `SC049`, `SC053`, `SC056`, `SC057`, `SC058`, `SC060`, `SC061`, `SC065`, `SC067`, `SC068`, `SC069`, `SC071`, `SC075`, `SC076`, `SC080`, `SC083`, and `SC086` later are no-break-before-boundary results, not historical boundaries tied to `SC087`.
9. `SC087` later is bounded by the current runner limit beyond order `86`, not by a discovered historical stage.
10. Any wording that implies a runner-bounded or non-historical side "must precede" or "must follow" another stage is too strong and should be softened before chapter reuse.
11. `SC073` later should still be keyed to `SC085` OE H Loss exactly as the TSV says, even though the variant id is `later_order_84`.

## Recommended next terminal batch

The next terminal batch should now shift to the remaining early explicit corridor below the newly completed lower-early band:

1. `SC014` NWGmc Unstressed Ai Monophthongization
2. `SC015` NWGmc I Lowering
3. `SC016` OE Ws Palatal Glide
4. `SC017` NWGmc U Lowering
5. `SC018` NWGmc Stressed Monosyllable O Raising
6. `SC019` NWGmc Final Long O Raising

That six-rule set closes the last open explicit-chain gap below the completed `SC020`-`SC040` region while also picking up `SC019`, which is now implicated by both `SC020` earlier and the older `SC036` earlier boundary.
