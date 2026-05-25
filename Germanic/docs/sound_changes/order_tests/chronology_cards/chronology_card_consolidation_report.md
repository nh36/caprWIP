# Chronology card consolidation report

## Completed coverage so far

The current chronology-card set now covers thirty-six tested rules:

1. `SC041`, `SC042`, `SC043`, `SC044`, `SC045`, `SC046`, `SC047`, `SC048`, `SC049`, `SC050`, `SC051`, `SC052`, `SC053`, `SC054`, `SC055`, `SC056`, `SC057`, `SC058`, `SC059`, `SC060`, `SC061`
2. `SC063`, `SC064`, `SC065`, `SC066`, `SC067`, `SC068`, `SC069`, `SC070`, `SC071`, `SC072`, `SC073`, `SC074`, `SC075`, `SC076`, `SC078`

This means the pilot rules, batch 04, batch 05, the scaled batch, the gap-filling batch, and the late-corridor batch are all now represented in a single indexed card set. The refreshed `chronology_card_index.tsv` records the current order, safe window, boundary type, failure counts, reciprocal status, broad-boundary flags, and runner-bounded cautions for each completed card.

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
9. `SC066` / `SC068`: `SC066` later and `SC068` earlier now form a reciprocal `spindle`-based relation inside the syncope / degemination corridor.
10. `SC070` / `SC071`: `SC070` later and `SC071` earlier now form a reciprocal six-row unstressed-fronting relation around forms such as `boraþ` / `boreþ` and `mōnaþ` / `mōneþ`.
11. `SC072` / `SC073`: `SC072` later and `SC073` earlier form a reciprocal broad unstressed-vowel boundary.
12. `SC074` / `SC075`: `SC074` later and `SC075` earlier now form a reciprocal `shilling`-based boundary.

The older one-sided links still matter too: `SC063` later still points to `SC072`, and `SC059` later still points to `SC078`, even though neither is yet a full reciprocal pair.

## Broad computational boundaries

Several boundaries need explicit broad-boundary handling rather than narrow adjacency prose:

1. `SC041` earlier breaks far away at `SC020` with 64 newly failing rows and a large class of spurious `-a`-final outputs.
2. `SC047` later and `SC048` earlier form the reciprocal 87-row `-en` failure set.
3. `SC069` earlier breaks far away at `SC023` with 17 newly failing rows that broadly restore final `-an` outcomes such as `nǣdran`, `eorþan`, and `flascan`.
4. `SC072` later and `SC073` earlier form a reciprocal 24-row `-æ` boundary.
5. `SC078` earlier breaks across `SC070` with another 87-row `-en` failure set.

These cards support later chronology prose, but the prose must not flatten them into single-lexeme adjacency claims. The index marks these sides in `broad_boundary_side` so they can be filtered during later chapter drafting.

## Runner-bounded / no-break sides

The runner-bounded set now falls into two groups:

1. Earlier searches blocked by bundled `PWGmcChanges`: `SC050`, `SC053`, `SC058`, `SC065`, `SC067`, `SC076`
2. Later searches that found no real break through last safe order `86` before the current `SC087` search boundary: `SC049`, `SC053`, `SC056`, `SC057`, `SC058`, `SC060`, `SC061`, `SC065`, `SC067`, `SC068`, `SC069`, `SC071`, `SC075`, `SC076`

These sides are computational boundary observations, not positive historical claims about `SC087` or about specific earlier bundled stages. The late-corridor batch matters here because it adds three fully negative cards (`SC065`, `SC067`, `SC076`) and several one-sided later no-break outcomes without turning the current search boundary itself into a historical chronology claim.

## Cards normalized in this pass

All chronology cards still share the same section order:

1. `Current position`
2. `Earlier boundary`
3. `Later boundary`
4. `Chronology statement`
5. `Caveats`
6. `Source files`

This pass extended the normalized card set by:

1. adding cards for `SC065`, `SC066`, `SC067`, `SC068`, `SC069`, `SC070`, `SC071`, `SC074`, `SC075`, and `SC076`;
2. refreshing the README so the expanded runner-bounded set is explicit;
3. refreshing the index so the new reciprocal pairs, broad boundaries, and negative cards are searchable;
4. preserving concrete PGmc > expected OE vs variant OE contrasts from the failures TSV rather than rewriting them as gloss-only prose.

## Issues for human review

The current card set is usable, but several issues still need care before these constraints are turned into chapter prose:

1. The 87-row broad failure sets (`SC047` later, `SC048` earlier, `SC078` earlier) still need careful narrative treatment.
2. `SC041` earlier breaks far away at `SC020`, so the wording should stay broad and computational rather than local and adjacency-like.
3. `SC069` earlier also breaks far away, at `SC023`, so it should be narrated as a broad computational boundary rather than as a tight local adjacency claim.
4. `SC050`, `SC053`, `SC058`, `SC065`, `SC067`, and `SC076` earlier are runner-boundary results inside bundled `PWGmcChanges`, not historical boundaries.
5. `SC049`, `SC053`, `SC056`, `SC057`, `SC058`, `SC060`, `SC061`, `SC065`, `SC067`, `SC068`, `SC069`, `SC071`, `SC075`, and `SC076` later are no-break-before-boundary results, not historical boundaries tied to `SC087`.
6. `SC061` earlier records loss of output (`+?`) for `do`, so later prose should describe that carefully rather than pretending there is an ordinary surface variant.
7. Any wording that implies a runner-bounded side "must precede" or "must follow" another stage is too strong and should be softened before chapter reuse.
8. `SC073` later should still be keyed to `SC085` OE H Loss exactly as the TSV says, even though the variant id is `later_order_84`.

## Recommended next terminal batch

The next terminal batch should now shift to the remaining far-late explicit corridor:

1. `SC079` OE J Loss After Heavy
2. `SC080` OE Final Geminate Simplification
3. `SC081` OE J Strengthening After Front Diphthong
4. `SC082` OE Intervocalic J Vocalization
5. `SC083` OE Unstressed EI Contraction
6. `SC085` OE H Loss
7. `SC086` OE Contraction
8. `SC087` OE R Metathesis

That eight-rule set finishes the remaining explicit late corridor in one contiguous stretch; `SC084` stays out because it is a technical marker rather than an ordinary historical sound-change target.
