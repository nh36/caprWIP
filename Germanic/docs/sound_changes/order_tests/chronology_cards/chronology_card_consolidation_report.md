# Chronology card consolidation report

## Completed coverage so far

The current chronology-card set now covers fifty-four tested rules:

1. `SC030`, `SC031`, `SC032`, `SC033`, `SC034`, `SC035`, `SC036`, `SC037`, `SC039`, `SC040`, `SC041`, `SC042`, `SC043`, `SC044`, `SC045`, `SC046`, `SC047`, `SC048`, `SC049`, `SC050`, `SC051`, `SC052`, `SC053`, `SC054`, `SC055`, `SC056`, `SC057`, `SC058`, `SC059`, `SC060`, `SC061`
2. `SC063`, `SC064`, `SC065`, `SC066`, `SC067`, `SC068`, `SC069`, `SC070`, `SC071`, `SC072`, `SC073`, `SC074`, `SC075`, `SC076`
3. `SC078`, `SC079`, `SC080`, `SC081`, `SC082`, `SC083`, `SC085`, `SC086`, `SC087`

This means the upper-early batch, the pilot rules, batch 04, batch 05, the scaled batch, the gap-filling batch, the late-corridor batch, and the far-late batch are all now represented in a single indexed card set. The refreshed `chronology_card_index.tsv` records the current order, safe window, boundary type, failure counts, reciprocal status, broad-boundary flags, and runner-bounded or non-historical cautions for each completed card.

## Strong reciprocal boundaries found so far

The strongest reciprocal or near-reciprocal relations visible in the current card set are:

1. `SC030` / `SC032`: `SC030` later and `SC032` earlier now form a reciprocal eighteen-row no-output boundary around forms such as `ġelīefan`, `brēad`, and `drēam`.
2. `SC031` / `SC034`: `SC031` later and `SC034` earlier form a tight reciprocal `dēaw` / `dawu` and `hēawan` / `hawan` relation.
3. `SC039` / `SC040`: `SC039` later and `SC040` earlier form a reciprocal `widow` boundary around `wuduwe` / `wudowe`.
4. `SC042` / `SC043`: `SC042` later breaks across `SC043`, and `SC043` earlier breaks across `SC042`.
5. `SC043` / `SC044`: `SC043` later breaks across `SC044`, and `SC044` earlier breaks across `SC043`.
6. `SC044` / `SC045`: `SC044` later breaks across `SC045`, and `SC045` earlier breaks across `SC044`.
7. `SC047` / `SC048`: `SC047` later and `SC048` earlier share the same 87-row broad `-en` failure set.
8. `SC050` / `SC052`: `SC050` later and `SC052` earlier form a concrete local relation around `stretch`; `SC050` earlier is still runner-bounded and is not part of a reciprocal historical pair.
9. `SC052` / `SC055`: `SC052` later and `SC055` earlier form a tight reciprocal relation around `cow` and `lung`.
10. `SC055` / `SC056`: `SC055` later and `SC056` earlier form a reciprocal boundary around `gift` and `sheath`.
11. `SC064` / `SC072`: `SC064` later and `SC072` earlier form a reciprocal `fright`-based boundary.
12. `SC066` / `SC068`: `SC066` later and `SC068` earlier form a reciprocal `spindle`-based relation inside the syncope / degemination corridor.
13. `SC070` / `SC071`: `SC070` later and `SC071` earlier form a reciprocal six-row unstressed-fronting relation around forms such as `boraþ` / `boreþ` and `mōnaþ` / `mōneþ`.
14. `SC072` / `SC073`: `SC072` later and `SC073` earlier form a reciprocal broad unstressed-vowel boundary.
15. `SC074` / `SC075`: `SC074` later and `SC075` earlier form a reciprocal `shilling`-based boundary.
16. `SC079` / `SC080`: `SC079` later and `SC080` earlier now form a tight reciprocal `lung` relation around `lungen` / `lungenn`.
17. `SC081` / `SC082`: `SC081` later and `SC082` earlier now form a reciprocal `strew`-based boundary.
18. `SC082` / `SC083`: `SC082` later and `SC083` earlier now form a reciprocal eight-row verbal boundary around `borian`, `handlian`, `liornian`, `liccian`, and related forms.
19. `SC085` / `SC086`: `SC085` later and `SC086` earlier now form a reciprocal four-row contraction boundary around `flēon`, `slēan`, `tēon`, and `tā`.

The older one-sided links still matter too: `SC032` later still points to `SC040`, `SC035` later still points to `SC043`, `SC036` later still points to `SC040`, `SC063` later still points to `SC072`, `SC073` later still points to `SC085`, and `SC059` later still points to `SC078`, even though those are not all full reciprocal pairs.

## Broad computational boundaries

Several boundaries need explicit broad-boundary handling rather than narrow adjacency prose:

1. `SC033` later breaks far away at `SC044`, so it should not be narrated as if it were tightly adjacent to OE Breaking.
2. `SC036` earlier breaks far back at `SC019`, even though the current failure set is narrow and centered on `soul`.
3. `SC040` later breaks far away at `SC072`, so it should not be narrated as a tight neighboring-stage adjacency.
4. `SC041` earlier breaks far away at `SC020` with 64 newly failing rows and a large class of spurious `-a`-final outputs.
5. `SC047` later and `SC048` earlier form the reciprocal 87-row `-en` failure set.
6. `SC069` earlier breaks far away at `SC023` with 17 newly failing rows that broadly restore final `-an` outcomes such as `nǣdran`, `eorþan`, and `flascan`.
7. `SC072` later and `SC073` earlier form a reciprocal 24-row `-æ` boundary.
8. `SC078` earlier breaks across `SC070` with another 87-row `-en` failure set.
9. `SC079` earlier breaks broadly across `SC055` with 26 newly failing rows, not with a tight one-lexeme adjacency.
10. `SC081` earlier also breaks far back across `SC055`, even though the current failure set is narrow and centered on `strew`.
11. `SC087` earlier breaks far away at `SC044`, so it should not be narrated as if it were tightly adjacent to the breaking stage.

These cards support later chronology prose, but the prose must not flatten them into single-lexeme adjacency claims. The index marks these sides in `broad_boundary_side` so they can be filtered during later chapter drafting.

## Non-historical computational breaks

Three tested sides now produce real computational first breaks that should still be kept out of ordinary historical chronology prose:

1. `SC031` earlier crosses bundled `PWGmcChanges` at order `13`.
2. `SC033` earlier also crosses bundled `PWGmcChanges` at order `13`.
3. `SC037` later crosses `SC038` OE Strip Secondary Stress, a technical marker rather than an ordinary historical sound change.

These sides matter as computational evidence, but they should be narrated as non-historical / runner-limited / technical-marker cases rather than as normal chronology constraints.

## Runner-bounded / no-break sides

The runner-bounded set now falls into three groups:

1. Earlier searches blocked by bundled `PWGmcChanges` with no real break: `SC035`, `SC037`, `SC039`, `SC050`, `SC053`, `SC058`, `SC065`, `SC067`, `SC076`
2. Later searches that found no real break through last safe order `86` before the current `SC087` search boundary: `SC049`, `SC053`, `SC056`, `SC057`, `SC058`, `SC060`, `SC061`, `SC065`, `SC067`, `SC068`, `SC069`, `SC071`, `SC075`, `SC076`, `SC080`, `SC083`, `SC086`
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

1. adding cards for `SC030`, `SC031`, `SC032`, `SC033`, `SC034`, `SC035`, `SC036`, `SC037`, `SC039`, and `SC040`;
2. refreshing the README so the new non-historical and runner-limited upper-early cases are explicit;
3. refreshing the index so the new reciprocal pairs, broad boundaries, and technical-marker cautions are searchable;
4. preserving concrete PGmc > expected OE vs variant OE contrasts from the failures TSV;
5. preserving `+?` rows in prose as no-output / failed derivations rather than rewriting them as surface forms.

## Issues for human review

The current card set is usable, but several issues still need care before these constraints are turned into chapter prose:

1. The `SC030` later and `SC032` earlier failure sets use `+?`; those rows must be narrated as no-output / failed derivations, not as surface OE forms.
2. `SC031` earlier and `SC033` earlier cross bundled `PWGmcChanges`, so they are non-historical computational breaks rather than ordinary chronology constraints.
3. `SC037` later crosses technical-marker `SC038`, so it is a real computational break but not an ordinary historical boundary.
4. `SC033` later breaks far away at `SC044`, so the wording should stay broad and computational rather than local and adjacency-like.
5. `SC036` earlier breaks far back at `SC019`, so it should not be flattened into a tight neighboring-stage claim.
6. `SC040` later breaks far away at `SC072`, so it should be narrated as a broad/far later boundary rather than as a local adjacency claim.
7. The 87-row broad failure sets (`SC047` later, `SC048` earlier, `SC078` earlier) still need careful narrative treatment.
8. `SC041` earlier breaks far away at `SC020`, so the wording should stay broad and computational rather than local and adjacency-like.
9. `SC069` earlier also breaks far away, at `SC023`, so it should be narrated as a broad computational boundary rather than as a tight local adjacency claim.
10. `SC079` earlier breaks broadly across `SC055`, with 26 newly failing rows, so it should not be flattened into a tight local adjacency claim.
11. `SC081` earlier also crosses `SC055` from far away, so it should not be narrated as if it were a direct neighboring-stage constraint.
12. `SC087` earlier breaks far away across `SC044`, so it should be narrated as a broad/far boundary rather than a local adjacency claim.
13. `SC035`, `SC037`, `SC039`, `SC050`, `SC053`, `SC058`, `SC065`, `SC067`, and `SC076` earlier are runner-boundary results inside bundled `PWGmcChanges`, not historical boundaries.
14. `SC049`, `SC053`, `SC056`, `SC057`, `SC058`, `SC060`, `SC061`, `SC065`, `SC067`, `SC068`, `SC069`, `SC071`, `SC075`, `SC076`, `SC080`, `SC083`, and `SC086` later are no-break-before-boundary results, not historical boundaries tied to `SC087`.
15. `SC087` later is bounded by the current runner limit beyond order `86`, not by a discovered historical stage.
16. Any wording that implies a runner-bounded or non-historical side "must precede" or "must follow" another stage is too strong and should be softened before chapter reuse.
17. `SC073` later should still be keyed to `SC085` OE H Loss exactly as the TSV says, even though the variant id is `later_order_84`.

## Recommended next terminal batch

The next terminal batch should now shift back to the remaining lower-early explicit corridor immediately below the newly completed upper-early band:

1. `SC020` PGmc Final Z Deletion
2. `SC021` NWGmc Unstressed O Raising
3. `SC022` NWGmc Mn Dissimilation
4. `SC023` NWGmc N Stem N Loss
5. `SC024` NWGmc Long E Lowering
6. `SC025` NWGmc Long E Nasal Rounding
7. `SC026` NWGmc Nasal Spirant Lengthening
8. `SC027` NWGmc Nasal Spirant Loss
9. `SC028` NWGmc Preconsonantal X Loss
10. `SC029` OE Awj Glide Formation

That ten-rule set fills the remaining lower-early gap nearest the completed chronology network around `SC030`-`SC041`. `SC019` remains an immediate follow-up singleton already implicated by `SC036` earlier, but keeping the next batch to ten rules makes `SC020`-`SC029` the cleaner contiguous follow-up set.
