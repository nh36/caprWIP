# SC047 production integration

PR #21 was fast-forwarded on `update` from
`545ba40ab3fa363249562bc032f7df1c3923dc47` to its exact reviewed and
certified head `113101ac5f169b589e1a9647cdf24d32cdd4d919`. GitHub records
that commit as the PR's merge commit. PR #20 was not merged separately.

The original bundle certification tested `ddd7f92a`; the production
commit has its own certification, with source identity
`954ee49d1e1deb9d47e391fafe522fc5f91b13c1f4293af9593e5edcc9488136`.
The [production evidence release](https://github.com/nh36/caprWIP/releases/tag/sc047/production-113101ac)
retains both sets of receipts, full logs, JUnit output and provenance.
The exact-head lanes passed 2,146 tests with 9,800 subtests and five
prescribed historical skips, then 26 exclusive tests. The inspected
book had 344 pages, 180 lexical dossiers and 396 active entries.

Fresh application binaries for A and B2 reproduced the captured model
results. The SHA-256 digests are
`206ba8e39e1bcad593ba73a7f48cc45d604cb8934c095cd82c16fffab259134e`
(A) and `9014137cd2769c559837f5bf3aee345b194f3e7dc68a2719b1f795835a0095c9`
(B2). The isolated local Flask deployment exercised model selection,
forward lookup, board comparison and refishing, compatibility selection,
stale/missing model rejection and representative modern lookups.
External deployment was not verified. A remains the interface default,
not a historical verdict. Both models and the compatibility cascade
remain available; historical captures are unchanged.

The selected accusative of ‘rest’, \emph{*rástǭ} > *ræste*, is attested
in the *Blickling Homilies* (Morris, p. 101, l. 26). Its derivation is
regular. `late_analogy` documents possible levelling of nominative
*ræst*, as distinct from the regular model prediction *rast* from the
citation form, and does not imply that the selected accusative needs
analogy. The superseded genitive in the stage audit needed correction.
For ‘hue’, the Cotton witness *hwites hiewes* is in Sweet's *Pastoral
Care*, p. 86, l. 20; facing Hatton p. 87, l. 20 reads *hwites hiwes*.
The Zupitza locator in the proposal and live metadata was erroneous;
the adoption memorandum and lexical ledger give the right witness.
These follow-up metadata corrections change no selections, inputs,
targets, or comparative forms and do not amend the certified commit.
