# Chronology card consolidation report

## Completed coverage so far

The current chronology-card set now covers forty-four tested rules:

1. `SC041`, `SC042`, `SC043`, `SC044`, `SC045`, `SC046`, `SC047`, `SC048`, `SC049`, `SC050`, `SC051`, `SC052`, `SC053`, `SC054`, `SC055`, `SC056`, `SC057`, `SC058`, `SC059`, `SC060`, `SC061`
2. `SC063`, `SC064`, `SC065`, `SC066`, `SC067`, `SC068`, `SC069`, `SC070`, `SC071`, `SC072`, `SC073`, `SC074`, `SC075`, `SC076`
3. `SC078`, `SC079`, `SC080`, `SC081`, `SC082`, `SC083`, `SC085`, `SC086`, `SC087`

This means the pilot rules, batch 04, batch 05, the scaled batch, the gap-filling batch, the late-corridor batch, and the far-late batch are all now represented in a single indexed card set. The refreshed `chronology_card_index.tsv` records the current order, safe window, boundary type, failure counts, reciprocal status, broad-boundary flags, and runner-bounded cautions for each completed card.

## Strong reciprocal boundaries found so far

The strongest reciprocal or near-reciprocal relations visible in the current card set are:

1. `SC042` / `SC043`: `SC042` later breaks across `SC043`, and `SC043` earlier breaks across `SC042`.
2. `SC043` / `SC044`: `SC043` later breaks across `SC044`, and `SC044` earlier breaks across `SC043`.
3. `SC044` / `SC045`: `SC044` later breaks across `SC045`, and `SC045` earlier breaks across `SC044`.
4. `SC047` / `SC048`: `SC047` later and `SC048` earlier share the same 87-row broad `-en` failure set.
5. `SC050` / `SC052`: `SC050` later and `SC052` earlier form a concrete local relation around `stretch`; `SC050` earlier is still runner-bounded and is not part of a reciprocal historical pair.
6. `SC052` / `SC055`: `SC052` later and `SC055` earlier form a tight reciprocal relation around `cow` and `lung`.
7. `SC055` / `SC056`: `SC055` later and `SC056` earlier form a reciprocal boundary around `gift` and `sheath`.
8. `SC064` / `SC072`: `SC064` later and `SC072` earlier form a reciprocal `fright`-based boundary.
9. `SC066` / `SC068`: `SC066` later and `SC068` earlier form a reciprocal `spindle`-based relation inside the syncope / degemination corridor.
10. `SC070` / `SC071`: `SC070` later and `SC071` earlier form a reciprocal six-row unstressed-fronting relation around forms such as `boraþ` / `boreþ` and `mōnaþ` / `mōneþ`.
11. `SC072` / `SC073`: `SC072` later and `SC073` earlier form a reciprocal broad unstressed-vowel boundary.
12. `SC074` / `SC075`: `SC074` later and `SC075` earlier form a reciprocal `shilling`-based boundary.
13. `SC079` / `SC080`: `SC079` later and `SC080` earlier now form a tight reciprocal `lung` relation around `lungen` / `lungenn`.
14. `SC081` / `SC082`: `SC081` later and `SC082` earlier now form a reciprocal `strew`-based boundary.
15. `SC082` / `SC083`: `SC082` later and `SC083` earlier now form a reciprocal eight-row verbal boundary around `borian`, `handlian`, `liornian`, `liccian`, and related forms.
16. `SC085` / `SC086`: `SC085` later and `SC086` earlier now form a reciprocal four-row contraction boundary around `flēon`, `slēan`, `tēon`, and `tā`.

The older one-sided links still matter too: `SC063` later still points to `SC072`, `SC073` later still points to `SC085`, and `SC059` later still points to `SC078`, even though those are not all full reciprocal pairs.

## Broad computational boundaries

Several boundaries need explicit broad-boundary handling rather than narrow adjacency prose:

1. `SC041` earlier breaks far away at `SC020` with 64 newly failing rows and a large class of spurious `-a`-final outputs.
2. `SC047` later and `SC048` earlier form the reciprocal 87-row `-en` failure set.
3. `SC069` earlier breaks far away at `SC023` with 17 newly failing rows that broadly restore final `-an` outcomes such as `nǣdran`, `eorþan`, and `flascan`.
4. `SC072` later and `SC073` earlier form a reciprocal 24-row `-æ` boundary.
5. `SC078` earlier breaks across `SC070` with another 87-row `-en` failure set.
6. `SC079` earlier breaks broadly across `SC055` with 26 newly failing rows, not with a tight one-lexeme adjacency.
7. `SC081` earlier also breaks far back across `SC055`, even though the current failure set is narrow and centered on `strew`.
8. `SC087` earlier breaks far away at `SC044`, so it should not be narrated as if it were tightly adjacent to the breaking stage.

These cards support later chronology prose, but the prose must not flatten them into single-lexeme adjacency claims. The index marks these sides in `broad_boundary_side` so they can be filtered during later chapter drafting.

## Runner-bounded / no-break sides

The runner-bounded set now falls into three groups:

1. Earlier searches blocked by bundled `PWGmcChanges`: `SC050`, `SC053`, `SC058`, `SC065`, `SC067`, `SC076`
2. Later searches that found no real break through last safe order `86` before the current `SC087` search boundary: `SC049`, `SC053`, `SC056`, `SC057`, `SC058`, `SC060`, `SC061`, `SC065`, `SC067`, `SC068`, `SC069`, `SC071`, `SC075`, `SC076`, `SC080`, `SC083`, `SC086`
3. The terminal later search for `SC087`, which found no real break beyond current order `86` before the current runner limit

These sides are computational boundary observations, not positive historical claims about `SC087` or about specific earlier bundled stages. The far-late batch matters here because it closes the searchable tail of the explicit chain while still leaving several later sides as no-break or search-limited results rather than positive adjacency claims.

## Cards normalized in this pass

All chronology cards still share the same section order:

1. `Current position`
2. `Earlier boundary`
3. `Later boundary`
4. `Chronology statement`
5. `Caveats`
6. `Source files`

This pass extended the normalized card set by:

1. adding cards for `SC079`, `SC080`, `SC081`, `SC082`, `SC083`, `SC085`, `SC086`, and `SC087`;
2. refreshing the README so the expanded runner-bounded and far-late reciprocal sets are explicit;
3. refreshing the index so the new reciprocal pairs, broad boundaries, and search-limited later sides are searchable;
4. preserving concrete PGmc > expected OE vs variant OE contrasts from the failures TSV rather than rewriting them as gloss-only prose.

## Issues for human review

The current card set is usable, but several issues still need care before these constraints are turned into chapter prose:

1. The 87-row broad failure sets (`SC047` later, `SC048` earlier, `SC078` earlier) still need careful narrative treatment.
2. `SC041` earlier breaks far away at `SC020`, so the wording should stay broad and computational rather than local and adjacency-like.
3. `SC069` earlier also breaks far away, at `SC023`, so it should be narrated as a broad computational boundary rather than as a tight local adjacency claim.
4. `SC079` earlier breaks broadly across `SC055`, with 26 newly failing rows, so it should not be flattened into a tight local adjacency claim.
5. `SC081` earlier also crosses `SC055` from far away, so it should not be narrated as if it were a direct neighboring-stage constraint.
6. `SC087` earlier breaks far away across `SC044`, so it should be narrated as a broad/far boundary rather than a local adjacency claim.
7. `SC050`, `SC053`, `SC058`, `SC065`, `SC067`, and `SC076` earlier are runner-boundary results inside bundled `PWGmcChanges`, not historical boundaries.
8. `SC049`, `SC053`, `SC056`, `SC057`, `SC058`, `SC060`, `SC061`, `SC065`, `SC067`, `SC068`, `SC069`, `SC071`, `SC075`, `SC076`, `SC080`, `SC083`, and `SC086` later are no-break-before-boundary results, not historical boundaries tied to `SC087`.
9. `SC087` later is bounded by the current runner limit beyond order `86`, not by a discovered historical stage.
10. Any wording that implies a runner-bounded side "must precede" or "must follow" another stage is too strong and should be softened before chapter reuse.
11. `SC073` later should still be keyed to `SC085` OE H Loss exactly as the TSV says, even though the variant id is `later_order_84`.

## Recommended next terminal batch

The next terminal batch should now shift back to the remaining upper-early explicit corridor immediately below the already interpreted `SC041` region:

1. `SC030` OE Au Fronting
2. `SC031` OE WW Simplification
3. `SC032` OE Diphthong Leveling
4. `SC033` OE Ew Long Diphthong
5. `SC034` OE Aw Long Diphthong
6. `SC035` OE Prefix A Reduction Early
7. `SC036` OE Inter Stress Raising
8. `SC037` OE Compound Linking Syncope
9. `SC039` OE WI Combinative U Umlaut
10. `SC040` OE Med Unstressed U Lowering

That ten-rule set fills the remaining upper-early gap nearest the completed chronology network around `SC041` and the already implicated stages `SC034` and `SC037`; `SC038` remains absent from the explicit-chain candidate set.
