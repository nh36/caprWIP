# PGmc reconstruction survey

This is research evidence for all Old English data points, not a second
corpus, historical-stage registry or approved input migration. The survey
now has complete Orel/Kroonen reading coverage and a citation-unit triage
of all393 rows. Explaining every disagreement remains ongoing; a reviewed
triage is not a collection of settled histories or an adoption decision.

## Ownership

- SOURCE: `sources.tsv` declares the reasonable held source universe,
  actual holdings, scope, edition/convention verification, exclusions and
  explicit consultation mode/priority/payoff.
- SOURCE: `forms.tsv` records diplomatic author forms or process evidence,
  exact printed pages, stages/cells, explained comparison notation, argument,
  verification and independent confidence.
- SOURCE: `coverage.tsv` records only actual row/source reviews and their
  evidence links, search basis and assessment. No row means no actual review.
- SOURCE: `review_targets.tsv` records finite non-core commitments, each
  with a selection basis and explicit reading-scope links; the two core
  populations are derived automatically.
- SOURCE: `reading_scopes.tsv` records the scheduled three-source screens,
  method readings and passages, with actual reading/verification distinct
  from planned population and page addresses.
- SOURCE: `reading_accountability/` retains the completed source-specific
  row-applicability manifests and bounded original-page check receipts.
  Each applicability manifest covers393 identities without manufacturing
  lexical consultations; these files also enter projection provenance.
  The Fulk selected-cell guard receipt preserves original inference
  provenance separately from later NOTE/sidecar checks. A surface-form
  guess is not a verified selected-cell identification.
- SOURCE: `analyses.tsv` owns evidence-linked row/unit, relationship,
  attribution, stage interpretation, justified analytical form and features.
- SOURCE: `comparisons.tsv` owns scoped cases, overlapping question/type
  tags, comparability and explanation status. Separate alignment status,
  cited basis and exact limits distinguish feature review from citation
  inventory. Tags are not settled causes.
- SOURCE: `rationales.tsv` owns typed, cited explanations and their premises
  and counterarguments, distinguishing source statements from our inferences.
  `reason_target` separates position support, descriptive bridges and
  explanations of divergence; controlled `conditioning_tags` identify
  cited class membership, never automatic matches of current strings.
- SOURCE: `commentary.md` owns the scientific synthesis and outstanding
  questions, not automatically approved corpus decisions.
- GENERATED: `corpus_inventory.tsv`, `source_coverage.tsv`,
  `reconstruction_ledger.md`, `survey_provenance.json`, `source_priorities.tsv`,
  `analytical_coverage.tsv`, `comparison_map.md` and `reading_progress.md`
  are projections through the canonical artifact graph.

All 393 OE row IDs remain in the population, including six research-only
rows. Current citation/input/stage/context/class fields are read from their
existing owners. Equality-stage resolution is an encoding convention,
not independent source agreement. Confidence does not assign a stage.
Shared evidence may link several rows, but each selected cell retains its
own review. Reconstructed stems, complete words and process statements
are not interchangeable evidence types.

Generated reading coverage contains the786 core targets, explicitly
scheduled non-core targets and every retained actual consultation, not
the bibliography-by-row Cartesian product. An unscheduled source has not
been reviewed or declared absent. A negative search needs an explicit
search basis; a scoped exclusion needs a reason.
Never turn a failed string search into evidence of author silence.
Verification gaps must remain visible. An indirect quotation retains its
quoted-author attribution without claiming the original was checked.

Printed-page strings contain numerals/roman folios, comma-separated ranges
and ASCII hyphens. PDF-sheet markers belong in locator/basis notes, never
in the citation-page field. Diplomatic forms are preserved verbatim.
Comparison normalization must be explained; Foma's symbol restrictions
are not a reason to alter a printed source form.

The validator does not infer scientific agreement from normalized strings,
and does not edit corpus fields, stage metadata, FSTs or fingerprints:

```sh
python3 Germanic/tools/pgmc_reconstruction_survey.py
python3 Germanic/tools/pgmc_reconstruction_survey.py --require-complete
python3 Germanic/tools/pgmc_reconstruction_survey.py --require-core-complete
python3 Germanic/tools/pgmc_reconstruction_survey.py --require-analysis-complete
python3 Germanic/tools/pgmc_reconstruction_survey.py --require-three-source-complete
python3 Germanic/tools/pgmc_reconstruction_survey.py --require-feature-alignment-complete
python3 Germanic/tools/adjudicate.py --refresh
```

The first command reports validity and actual incompleteness. The composite
gate fails while a required row target, three-source passage/screen/method
or core analytical row remains unreviewed, not merely because a background source was
not read. Declared local verification gaps are not silently erased;
a reviewed survey with such limits is not wholly image-verified evidence.
The core-only gate requires both dictionaries, every population row's
actual disposition and reviewed core methods. It cannot be satisfied by
deleting a source, omitting a row or requiring only positive evidence;
it does not certify other sources or diplomatic image verification.
The analytical gate also requires core reading completion and all393
core triage dispositions, retaining every recorded core alternative.
Unknown cause, date, endorsement and non-comparable units are legitimate
explicit dispositions. It does not certify complete explanation, every
source argument, historical equivalence or scientifically preferred inputs.
Only the last command regenerates projections. Do not run separate
generators or hand-edit outputs.

## Active three-source dispatch

The approved next stage completes relevant Ringe2017, Fulk2018 and
RingeTaylor2014 reading before analytical closeout. After extraction it
requires feature/paradigm alignment of all393 core rows, substantive-case
explanation or exact remaining premises, the conditioning census and a
non-adopting consistency watchlist. The current analytical gate still
certifies citation-unit triage only.

All three relevant held-source passes are persisted: Ringe192, Fulk145
and Ringe-Taylor258 actual consultations. Each has393 independent
applicability dispositions; the1179 screens are not1179 grammar
negatives. All786 core reviews remain. Of20 scopes,19 are reviewed
and the Ringe-Taylor conventions scope retains its genuine verification
gap. The fully verified three-source gate therefore still refuses
completion; the held-text reading is finished with named limits, not
newly image-certified.

There are5177 evidence records,1390 actual consultations and5384
analytical positions, with448 comparisons and552 rationales. The RT
occurrence audit removed31 overlapping new extractions before integration;
genuine repeated forms at different positions/cells/stages remain.
The persisted occurrence, remap, passage, page and glyph-limit receipts
document that distinction. Only author attribution and appended notes
change in the three named inherited RT records; their forms, pages,
stages and verification remain intact.

Two hundred seventeen core rows now have individually reconciled, bounded alignment:
1933-2149. The remaining176 are unreviewed. The second tranche builds on
the35 preparatory dictionary decisions rather than treating that preparation
as finished all-source alignment. Each completed
alignment retains all available member positions and names its specific
remaining formation, reflex, representation or selected-cell premise;
none is a settled whole-word equivalence or established whole-case cause.
Ringe's ask-specific following-j reason and RT's bake following-i/lost-trigger
reason are position support, not a completed class census.

The twenty-seventh tranche completes nine, nose, one, oven, ox, rain,
rainbow and raven, rows2142-2149, after released26 base678eafa6.
All79 inherited analytical identities survive. Twenty-seven native
literal occurrences and34 scoped arguments add61 records; five focused
positions reuse evidence and39 rationales are added. The145 positions
link139 distinct records. Exact reversible SOURCE receipts cover98
fields:76 cells,12 stages, two arguments, seven page locators and one
reported-author attribution. No consultation identity or status changes.

Nine's velar-origin question is distinct from its later blocking of
back umlaut. One's accusative raising, old i-stem and compound evidence
are distinct from two's paradigm and Cowgill's reported endingless
alternative. Their two focused substantive comparisons remain
unexplained, not exclusive competing laws
[@Kroonen2013, pp.389-390; @Fulk2018, pp.57-59,120-121,222,225,226-228;
@RingeTaylor2014, pp.17-21,120,165-167,323-325].

Nose's PGmc consonant stem is not its OE u-stem. Fulk/ox and RT/nose
remain discussion_only. Oven's qualified f/h histories do not supply
a third g-protoform. Distinct ox accusative/plural occurrences and
native quantity limits survive. Rainbow's component relations are
row-specific: shared bow/rain SOURCE and outside-row analyses remain
unchanged. Raven's older n-stem cells are not its thematic citation
[@Kroonen2013, pp.61-62,82,240,383,408,557-558,566;
@Orel2003, pp.182-183,281,300,433-434;
@Ringe2017, pp.136-140,221-223,306-308,312-313,324,328;
@Fulk2018, pp.168-172; @RingeTaylor2014, pp.33-35,211-213,329-332,384-386].

All eight whole-row causes remain unestablished; selected inputs and
stages are unchanged. The new receipts are
`reading_accountability/alignment-2142-2149-amendments.tsv` and
`reading_accountability/alignment-2142-2149-occurrences.tsv`.
Never execute/import the persisted tranche27 candidate. Current SOURCE,
receipts and regressions are authority. The full393-row alignment,
aggregate class census and explanatory synthesis remain unfinished.
No scientific adoption, publication, automatic27 release or28 start.

Independent closeout preserves5116 inherited forms except98 exact
fields,5239 outside positions,438 unaffected cases,513 inherited reasons,
1356 outside consultations,81 unaffected research hashes and46 scientific
hashes. All27 native paragraph hashes and whole-token spans independently
resolve. Canonical refresh is clean without a scientific rebuild.
The combined339-test run had two expectation-only failures; both are
corrected, and the11-test targeted rerun passes. All57 new-prose
printed-page references, bibliography, locators and whitespace pass.
Alignment independently refuses176; the RT conventions refusal remains
separate and unchanged.

The twenty-sixth tranche completes neck, need, needle, nest, net,
nettle, night and nightmare, rows2134-2141, on released25 basee8453591.
All91 inherited identities survive; the existing image-checked
Cercignani nest quotation now has its missing analytical position
without a new consultation. Twenty-eight native literal receipts
and31 scoped arguments add59 records; five focused positions reuse
evidence and36 rationales are added. The156 positions link151
distinct records. The120 exact SOURCE amendments cover91 cells,
12 local stages, seven arguments and10 page locators.

The inherited RT desire/eagerness chain on250 is comparandum, not
selected au-bearing need. Actual need on246 is separately quoted.
Needle's instrument-suffix versus accent explanations remain alternatives;
nest's general330 epenthesis record is comparative-only, not direct
nest history [@Ringe2017, pp.302-305;
@RingeTaylor2014, pp.245-247,249-251,329-331].

Image-certified Orel cross-references retain their original pages:
sew287, dragnet282 and nettle-base281. Actual headwords are separately
receipted on286,289 and282. One actual RT/nettle status upgrades
discussion_only to evidence_found because270 supplies an explicitly
reconstructed PWGmc precursor, not because netle is an OE attestation.
The existing consultation identity, target and initial screen remain
[@Orel2003, pp.281-282,286-287,289;
@RingeTaylor2014, pp.268-276].

Repeated night cells, uncertain plural endings, day/home comparanda
and dual PWGmc/PGmc source attribution remain distinct. Selected
*náxti is not automatically a nominative or an adopted source dative.
Nightmare's retained front form and the Kroonen bounded negative
survive; no horse/spirit merger or new grammar negative is introduced
[@Ringe2017, pp.242-243,312-313;
@RingeTaylor2014, pp.116-118,190-193,240-241,379-381].

Both focused neck/nest causes and all eight whole-row causes remain
unestablished. Nest's occurrence, recoverability and common-stage
dating warrants are not flattened into an exclusive opposition
[@Kroonen2013, p.234; @Ringe2017, pp.137-140;
@Fulk2018, pp.55-59; @Cercignani1980, pp.126-132].

The new receipts are
`reading_accountability/alignment-2134-2141-amendments.tsv`,
`reading_accountability/alignment-2134-2141-occurrences.tsv` and
`reading_accountability/alignment-2134-2141-owner-amendments.tsv`.
Never run/import the persisted tranche26 candidate. Current SOURCE,
receipts and regressions are authority. All786 dictionary identities
remain, with1753 dictionary evidence records; new native literals
are text_checked, not image-certified. No corpus/input/stage/context,
FST/baseline adoption, publication, automatic26 release or27 start
is included. All329 focused tests pass; canonical refresh is clean
without a scientific rebuild. Independent post-refresh verification
preserves5057 inherited forms except120 exact fields,5162 outside
positions,436 unaffected cases,477 inherited rationales,1359 outside
consultations,78 unaffected research hashes and46 scientific hashes.
All28 native spans independently resolve; all73 new-prose page references,
bibliography, section locators and whitespace checks pass. Alignment
independently refuses184; RT conventions remain a separate limit.
The full393-row programme remains incomplete.

The twenty-fifth tranche completes milk, month, mood, mother, nail,
name, nave and navel, rows2126-2133, on released24 base75bcc49a.
All105 inherited analytical identities survive; three previously
unlinked, image-checked milk/Cercignani records now have individual
analytical positions in their existing consultation. Twenty-two
native literal occurrences and24 scoped arguments add46 evidence
records; five focused positions reuse evidence and29 rationales
are added. The159 positions link154 distinct records. There are
119 exact SOURCE-field amendments:105 cells, six local stages,
four arguments, two page locators and the two fields correcting
the clipped month index citation. All consultation identities,
statuses, scopes, targets and applicability owners are unchanged.
All786 dictionary reviews remain, with1727 dictionary evidence
records; new native literals are text_checked, not image-certified.

Fulk's original month index is independently rechecked as
*mēnōþi*, not the clipped *mēnōþ*. Its final-i dative precursor
is not a month nominative. The corresponding milk index likewise
points to a dative, with the body's ending alternative retained.
Moon/month, masculine/neuter name, identical nominative/accusative
tokens and mother suffixes/whole words remain separately classified
[@Fulk2018, pp.79-81,388; @Ringe2017, pp.306-308,312-313;
@RingeTaylor2014, pp.11,59,79,143-145,163-164,300-301,381-383].

The focused milk comparison separates continental u-conditioning
from conditional oblique i-triggers, without asserting exclusive
opposition or a universal PGmc date. The focused name genealogy
comparison is substantive but unexplained. Both focused causes
and all eight whole-row causes remain unestablished. Navel's
selected pwgmc input remains distinct from the source's explicit
PNWGmc ancestor
[@Cercignani1979, pp.75-76; @Fulk2018, pp.68-69,79-81;
@Kroonen2013, pp.382-383; @Ringe2017, pp.56-57,91-95;
@RingeTaylor2014, pp.190-192,253-254,270-271].

The new exact receipts are
`reading_accountability/alignment-2126-2133-amendments.tsv` and
`reading_accountability/alignment-2126-2133-occurrences.tsv`.
Never execute/import the persisted tranche25 candidate again.
Current SOURCE, receipts and regressions are authority. No corpus,
input, stage/context, FST, scientific-baseline or publication
adoption is included; the full393-row programme remains open.

The twenty-fourth tranche completes malt, man, boundary march,
mast, time/meal, mean, meed and might, rows2118-2125, on
released23 base5208573f. All97 inherited identities survive.
Thirty-seven literal receipts and28 scoped arguments add65
records; five focused positions reuse evidence and34 rationales
are added. The167 positions link162 records. Exact SOURCE
receipts cover97 cells, four arguments, three stages and five
page locators. One actual RT/might consultation adds one target;
six owner fields preserve the initial scope/screen reversibly.
All786 dictionary reviews remain, with1712 dictionary evidence
records separately counted.

Man's selected genitive differs from nominative, plural, dative,
counterfactual and quasi-PIE units. The focused ancestry case
retains distinct men-u versus mánu/mánw premises, with the
reconciliation warrant unestablished
[@Kroonen2013, pp.353-354; @Ringe2017, pp.164-165;
@Fulk2018, pp.113-114,166-168,388].
RT plural apocope is not syncope or a genitive quotation
[@RingeTaylor2014, pp.228-230,284-287].

Mast's selected sense remains bounded; identical sail/forest
homonyms and their warrants survive. Its focused Latin/Irish
admission explanation is analyst inference, not a named rebuttal
or adopted genealogy [@Kroonen2013, p.357; @Orel2003, p.263].
Meal's time/mark/measure identity is disputed, and the first
RT time intermediate is explicitly PNWGmc
[@Kroonen2013, p.362; @Orel2003, pp.269-270;
@RingeTaylor2014, pp.149-150,238-240].

Meed's whole Kroonen argument is on370; explicit PGmc and
secondary WGmc annotations retain independent glyphs and stages.
Ringe's post-PWGmc loss correction is source-explicit, not two
independent author votes [@Kroonen2013, p.370;
@Orel2003, p.272; @Ringe2017, pp.120-121;
@RingeTaylor2014, pp.83-85].
Might's masculine tu formation and can verb are not the feminine
ti noun; the actual RT history supplies a previously missed
consultation, preserving its endpoint reservations
[@Kroonen2013, pp.347,373; @Orel2003, pp.252-254;
@Ringe2017, pp.133-135,325-327;
@RingeTaylor2014, pp.240-241,336-337].

Malt's az-shaped input does not select an adjective etymon;
boundary compounds and signifying verb are not bare boundary;
mean's causative and reported denominative are not proved
exclusive accounts [@Orel2003, pp.255,258,262,267;
@Kroonen2013, pp.348,351-352,355,363;
@RingeTaylor2014, pp.179-183,312-314].
All eight whole-row causes remain unestablished. Current SOURCE,
exact receipts and regressions are authority; never execute/import
the persisted candidate. Corpus/input/stage/context/FST/baseline
adoption, a new PDF, automatic24 release or25 start are not included.

The twenty-third tranche completes loath, mechanical lock, hairlock,
louse, lung, lust, lye and make, rows2110-2117, on released22 base1e2cb5cb.
All47 inherited identities survive. Twenty-eight literal occurrences
and23 scoped processes add51 records; five focused positions reuse
evidence and29 rationales are added. The103 positions link98 records.
Twenty-eight exact SOURCE fields comprise16 cells, eight qualified
arguments, two dates and two page locators. Two genuine close-family
consultations add two finite targets;13 exact owner fields preserve
the original scopes/applicability by reversal. All786 dictionary
review identities/statuses remain, with1676 dictionary evidence
records separately counted.

Mechanical noun and close/pull verb are different units; Orel and
Kroonen allocate their external comparisons differently
[@Orel2003, pp.250,252; @Kroonen2013, pp.334,343].
Fulk's actual close-family aorist/principal-part argument does not
quote the selected noun, and RT's explicit PGmc close date does
not date that noun [@Fulk2018, pp.246-249,263-265,285-286;
@RingeTaylor2014, pp.39-40]. Hairlock's focused direct-flexible
case remains unexplained, preserving explicit rejection, owned
bend connection and conditional substantivization separately
[@Kroonen2013, p.343; @Orel2003, p.250;
@Ringe2017, pp.137-140].

Loath's actual PNWGmc adjective and PWGmc adjective differ from
the denominative verb [@RingeTaylor2014, p.129]. Louse's root
noun is not its continental i-stems or Celtic plural
[@Orel2003, p.252]. Lung's feminine header/neuter prose and
separate feminine OE derivative survive; source u does not
silently replace the selected a-derivative
[@Kroonen2013, pp.338-339,344; @Orel2003, pp.240-241,251].
Lust's Probably-love and Perhaps-lose ancestries remain conditional;
Ringe's tu-formation date, RT's following-u protection and the
suffixed pleasant adjective are independent
[@Orel2003, pp.238,241,249,251; @Kroonen2013, pp.334,345;
@Ringe2017, pp.324-325; @RingeTaylor2014, pp.29-31,520-521].
Lye's wash family does not establish a dated selected velar law
[@Orel2003, pp.238-239].

Make's focused original-meaning/derivational-direction explanation
is bounded analyst inference, not a named rebuttal or adopted root
[@Kroonen2013, pp.350-351; @Orel2003, p.257].
PWGmc restraint, physical root retraction, later suffix shortening/
syncope, default infinitive and present plural remain distinct;
the general weak-past argument is not an authored make past
[@RingeTaylor2014, pp.126-128,190-192,227-229,257-258,516-518].
All eight whole-row causes remain unestablished. New literal
receipts are text_checked, not newly image-certified; native
corruptions and the combining macron in Ringe's entice form
remain. No corpus/input/target/stage/context/FST/baseline adoption,
introduction/PDF, automatic23 release or24 start is included.
Current SOURCE, receipts and regressions are authority; never
execute/import the persisted tranche23 candidate.

The298-test focused survey/analysis suite passes. All79 new-prose
printed-page references, bibliography, section locators, template
headings and whitespace pass; canonical refresh is clean.
Independent verification preserves all47 identities,4895 inherited
records except28 exact annotations, all786 dictionary review
identities/statuses,65 unaffected research hashes and46 scientific
hashes. One separately receipted RT disposition correction uses
the established consulted_applicable value; the original13 owner
amendments and their reversal remain unchanged. Completion is not
mere preparation, nor is it completion of the393-row programme.

The twenty-second tranche completes light (illumination verb), lime,
linden, line, list (border), live (selected3sg), liver and loam,
rows2102-2109. The preceding tranche is committed and pushed as5275848d.
All77 inherited analytical identities survive individual reconciliation.
Thirty-five exact literal occurrences and22 complete-argument processes
add57 records; four focused positions reuse evidence and27 rationales
are added. The138 positions link134 distinct records. Fifty-six SOURCE
fields have exact old/new/page-backed receipts:41 cells, eight local
dates, five qualified arguments, one page range and one reported author.
There are no new consultations, status changes, targets, scopes or
applicability identities;786 dictionary reviews and1649 dictionary
evidence records remain separately counted.

Four RT records formerly matched as illumination actually concern
lightening a load. Their identical-looking intermediate forms remain
distinct occurrences. The dental illumination verb, sibilant shine
family and noun formations are not interchangeable
[@Orel2003, pp.242-243; @Kroonen2013, pp.333-334;
@RingeTaylor2014, pp.249,310]. Orel's Latin-derived line/rope is
separate from linen/flax and their secondary association; long-i
border is separate from skill/cunning [@Orel2003, pp.233,248].

Linden's explicit rejection versus bibliographically reported
adjective connection remains a focused substantive but unexplained
comparison, without turning Orel's report into his exclusive position.
Liver's possible irregular inherited continuation versus smear ancestry
and probable inherited-word influence has a bounded analyst-inferred
warrant explanation, not a named rebuttal or settled genealogy
[@Kroonen2013, pp.336,338-339; @Orel2003, pp.240-241,245].
All eight whole-row causes remain unestablished.

Live's generic class ending is not an authored assembled third singular.
Source3sg variants remain matched to that grammatical cell without
becoming literal selected lifeþ. The revised Ringe account incorporates
the earlier merger proposal while retaining its own uncertainty
[@Ringe2017, pp.157-158,203-206,286-288;
@Fulk2018, pp.308-313; @RingeTaylor2014, pp.93-94,364-366,518].
Liver's lowering and epenthesis are different questions; loam's
masculine citation does not quote the selected neuter pre-OE input
[@Fulk2018, pp.55-59; @RingeTaylor2014, pp.33-35,327-329;
@Kroonen2013, pp.323-325; @Orel2003, p.233].

Independent verification preserves4838 inherited forms except56 exact
annotation fields,4935 outside positions,428 unaffected cases,358
inherited reasons,1362 outside consultations,67 unaffected prior
research hashes/receipts and46 scientific hashes. All35 literal
paragraph hashes and whole-token Unicode spans independently resolve.
Confidence, verification, diplomatic forms and earlier receipts are
unchanged. Alignment separately refuses216 rows; verified reading
separately refuses the unchanged RT conventions gap. Next alignment
begins2110; tranche22 is uncommitted and no23 or scientific adoption
is included.

The twenty-first tranche completes leaf, learn, leather, leek, let,
lick, lid and life, rows2094-2101. All80 inherited analytical identities
are individually reconciled. Twenty-five literal receipts and21
complete-argument processes add46 records; four focused positions reuse
evidence and26 rationales are added. The130 positions link126 distinct
records. Forty-eight exact SOURCE amendments comprise41 cell fields,
three locally supported dates and four argument repairs. Two actual
existing Fulk consultations are upgraded after lexical evidence is added;
no new consultation, target, scope or applicability record is created.
All786 dictionary reviews survive; their evidence count is1624.

Learn's inherited-fientive versus qualified WGmc-innovation question
remains focused substantive but unexplained. Fulk's109 catalogue and
114 qualification both survive, with the actual313-315 weak-IV
cross-reference; Ringe's289-290 catalogue explicitly projects learn
back to PGmc [@Fulk2018, pp.109,114,313-315; @Ringe2017, pp.289-290].
Let's type2 comparison has a bounded analyst-inferred explanation of
different model domains and explanatory warrants, not a direct named
rebuttal, phonology-versus-analogy opposition, or adopted chronology
[@Fulk2018, pp.260-262,266-272; @RingeTaylor2014, pp.88-92].
All eight whole-row causes remain unestablished.

Orel's leek cross-reference does not uniquely select between his
close and pull-up/weed homonyms. Leather's Celtic-loan account does
not itself fix a borrowing date; image-checked thorn remains unchanged.
Lid's long-vowel verb is family evidence, not the short-vowel selected
noun. Life's noun, live stative and conditional strong-verb account
remain separate [@Orel2003, pp.176-178,239,241,251-252;
@Kroonen2013, pp.329,332,334-338; @Ringe2017, p.287].
Independent verification preserves all4792 inherited forms except the48
exact fields, all outside research and64 unaffected prior research
hashes/receipts, and all46 protected scientific hashes. The source
catalogue, consultation identities, scopes, targets, corpus/input/stage/
context/FST/baseline owners remain unchanged. Next alignment begins2102;
this is neither scientific adoption nor completion of the393-row programme.

The twentieth tranche completed knight, knob, lade, land, lap, last,
laugh and lead, rows2086-2093. All83 inherited identities are individually
reconciled;28 exact literals and26 processes add54 records. Four focused
positions reuse evidence and30 rationales are added. Fifty-five exact
SOURCE amendments cover39 cells, seven local dates, five page ranges,
three reported authors and one component kind. Forty-three owner-field
receipts preserve the original screening while recording six real Fulk
consultations and the previously missed RT/lade consultation; seven
finite targets are added, not a blanket class review
[@Fulk2018, pp.52-53,73-75,114-117,265-266,294-295,301-303;
@RingeTaylor2014, pp.233,343-344].
The141 positions link136 distinct records. Last's know/track commitment
and lead's owned causative versus reported nominal derivation remain
focused substantive but unexplained; all eight whole-row causes remain
unestablished [@Kroonen2013, pp.323-324,339-340; @Orel2003, pp.232-233].
Both RT landu occurrences are plural, not instrumental; landa is
hypothetical Gothic, not an intermediate arrow. Laugh's underlying,
surface and hj-component records remain distinct
[@RingeTaylor2014, pp.15,51,286,348].
Independent verification reverses the exact owner fields and removes
only the seven new targets to reconstruct their frozen original hashes.
All prior receipts, source catalogue,786 dictionary reviews, outside
research and46 protected scientific hashes remain unchanged.
This is not an input/stage/FST adoption or the completed393-row programme.

The nineteenth tranche completed home, honey, hood, hoof, horn, hound,
knead and knee, rows2078-2085. All82 inherited analytical identities
survive individual curation. Twenty-eight exact literal receipts and
nineteen processes add47 records; the missing horn/Cercignani position
reuses existing image-checked evidence. Six focused positions reuse
process evidence, and twenty-five rationales are added. Thirty-eight
SOURCE field amendments retain exact old/new/page-backed receipts:
nine dates, four page ranges, twenty-four cells and one argument.
One owner receipt upgrades the existing Fulk/knee consultation after
three actual Gothic/Old Saxon literal cells are added; consultation
identities and all786 dictionary reviews are unchanged
[@Fulk2018, pp.153-154,264,387; @Cercignani1980, p.127].
The136 positions link130 distinct evidence records.

Home's inherited-comparison versus Baltic-loan premise and honey's
secondary versus original suffixal n are focused substantive differences,
but their causes remain unestablished. Hound's to-formation versus
conditional dental-paradigm preference has a bounded analyst-inferred
warrant explanation, not a named rebuttal or adopted ancestry
[@Orel2003, pp.152,193; @Kroonen2013, pp.201,255-256,267].
All eight whole-row causes remain unestablished. Explicit WGmc hood,
qualified (post-)PNWGmc horn, knead's finite first-plural cells and
body/index distinction, and knee's plural versus short pre-ending stem
remain separate [@Orel2003, p.165; @RingeTaylor2014, pp.45,61,78,187,387;
@Kroonen2013, p.295; @Fulk2018, pp.153-154,264,387].
The protected knee input, target and stage are unchanged. No corpus,
stage/context, FST, baseline, introduction or PDF adoption is included.
The full393-row programme remains unfinished; next alignment begins2086.

The eighteenth tranche completes helmet, help verb, help noun, herd,
hew, hind, hoard and hold, rows2070-2077. All102 inherited analytical
identities are individually reconciled. Thirty-two literal receipts and
sixteen processes add48 records; four focused positions reuse evidence,
and eighteen rationales are added. Twenty-four exact SOURCE amendments
repair seventeen cells, two arguments, two reported-author attributions,
one metalinguistic stem classification, one locally explicit OE date and
one overbroad page range. Two owner-field receipts change actual existing
Fulk help/hew consultations from discussion-only to evidence-found; no
consultation identities or dictionary statuses change
[@Fulk2018, pp.286,291]. The154 positions link147 distinct records.
All prior receipts and outside analytical identities are preserved.
Two additional position-field receipts correct the generic final-u
suffix/ending summary: it is not the following third-plural final-i
example [@RingeTaylor2014, p.56].

Hind's focused young/new versus hornless warrant and hoard's focused
dh-t/Bartholomae versus s-dh formation warrant have bounded
analyst-inferred explanations, not named rebuttals or selected histories.
Neither explains the whole row. In particular, hind's e/i and j/n/ō
formation differences remain open, and Kroonen's conditional hoard
entry remains conditional beside its stronger house cross-reference
[@Orel2003, pp.169,196; @Kroonen2013, pp.206,226,260;
@Ringe2017, p.115]. The finite help cells attached to the noun, the
unrelated restoration comparanda, RT's metalinguistic feolan label,
regional hew preterites, herd derivatives and hold's index/body and
dialect cells are independently matched, not normalized into agreement
[@RingeTaylor2014, pp.55-58,89,182,184-186,347,349-351;
@Fulk2018, pp.64,270,286,290-291,387].
All eight whole-row causes remain unestablished. No corpus/input/stage/
context/FST/baseline adoption, introduction, PDF or automatic release
is included; the full393-row programme remains unfinished.

The seventeenth tranche completes hazel, head, heal, heart, hearth, heath,
heaven and hedge, rows2062-2069. All101 inherited identities are individually
reconciled. Thirty literal receipts and eighteen processes add48 records;
four focused positions reuse evidence and twenty rationales are added.
Twenty-two SOURCE amendments preserve exact old/new values: fourteen dates,
five cells, one stale argument, one reported-author attribution and one
illustrative-table word classification. Eight owner-field receipts preserve
the actual heart follow-up in Fulk's applicability/phonology owners; the
new target and consultation are actual PNorse/Gothic lexical evidence,
not an invented PGmc selected word [@Fulk2018, pp.67-68,85-87].
The153 positions link149 distinct records. The prior sixteenth receipts
and all outside identities remain preserved.

Hearth's focused explanation is bounded analyst inference: Orel's owned
cut/boundary semantic connections differ from Kroonen's burn/to-stem and
coal/fire comparative warrant. Bibliographic burn/coal theories are not
Orel endorsements, and no named rebuttal or settled root ancestry is claimed
[@Orel2003, p.170; @Kroonen2013, pp.222,258].
Head's root-variation comparison remains unexplained: secondary/taboo
variants and a possible original paradigm/metathesis are not proved
exclusive or assigned identical dates [@Orel2003, pp.148,165;
@Kroonen2013, p.215]. Actual/expected head cells, heart versus tongue,
heath's derivative genders, heaven's locative versus remodeled dative
and actual northern stem, and bird cherry versus hedge remain distinct
[@RingeTaylor2014, pp.59,257,270,272,378,387;
@Kroonen2013, pp.198,202,220]. All eight whole-row causes remain
unestablished. Selected heaven `*xébun`, nsgmc and early_analogy are
unchanged; the older ledger's input is a non-adopting watchlist item,
not selected-input authority. No corpus/stage/context/FST/baseline,
introduction or PDF adoption is included.

The sixteenth tranche completes hand, handle (verb), harm, harvest,
have (selected third singular), haw (enclosure), hawk and hay, rows2054-2061.
All116 inherited identities survive. Forty-one literal receipts and
fourteen processes add55 records; four focused positions reuse evidence
and sixteen rationales are added. Thirteen SOURCE annotation receipts
cover nine dates, three cells and one phonetic-stem kind. The existing
Fulk hay consultation changes from discussion-only to evidence-found
because its checked footnote actually quotes a reconstructed stem;
that status change has its own receipt [@Fulk2018, p.128].
No consultation identity is invented. Its175 positions link170 distinct
records, including shared hand/handle evidence and separately identified
have paradigm cells [@Fulk2018, pp.309-313; @RingeTaylor2014, pp.131,269].

Hawk's focused explanation is bounded analyst inference: formal
comparative admissibility separates Orel's own IE/Slavic equation from
Kroonen's correspondence/root-structure objections. It neither establishes
a borrowing date nor attributes both bibliographic borrowing theories
to Orel [@Orel2003, p.148; @Kroonen2013, pp.197-198].
Harvest's focused membership question remains unexplained: RT does not
evaluate the Nordic reflex admitted by Kroonen, and Orel retains an
a-formation beside the u-headwords, precluding an exclusive a/u conflict
[@RingeTaylor2014, pp.126-128; @Kroonen2013, pp.210-211;
@Orel2003, pp.161-162]. Have's analogical finite history, Fulk's explicit
recognition of Ringe's plausible account, and hay's qualified gemination
arguments remain source-specific [@Fulk2018, pp.71-72,128,309-313;
@Ringe2017, pp.157-158; @RingeTaylor2014, pp.53,173,246,363-364].
All eight whole-row causes remain unestablished. No corpus, stage/context,
FST, scientific baseline, introduction or PDF changes are included.

The fifteenth tranche completes grave (the dig verb), gripe, ground,
guest, hail, hair, hall and hammer (selected genitive), rows2046-2053.
All81 inherited identities survive. Thirty-six literal receipts and
twelve processes add48 records within existing consultations; four
focused positions reuse evidence and fourteen rationales are added.
Fourteen exact SOURCE field receipts cover nine dates, three cells and
two hall arguments; one additional post-persistence receipt corrects
the new Orel hammer precursor's full-word kind, not its literal
[@Orel2003, p.158]. No consultation identity or status changes.
Its133 positions link129 distinct records.

Ground's source-explicit comparison concerns the usual n-root derivation
versus Kroonen's Cimbrian-supported original mþ/nd paradigm. His voiced
genitive still underlies OE grund: this is not rejection of every nd
form [@Orel2003, p.144; @Kroonen2013, pp.xxxi-xxxii,192,321,426].
Guest's source-explicit comparison concerns inherited genitive quantity
versus a-stem replacement, not the entire guest history. Fulk's printed
Ringe2017:311 pointer is retained as printed, while the checked i-stem
argument and guest paradigm actually occur on304-305 and312
[@Fulk2018, pp.159-161; @Ringe2017, pp.304-305,310-312].
Distinct Ringe/Fulk/RT cells, Fulk's full-form attestation caveat, the
sal-/heall etymon boundary, conditional dictionary histories and the
selected hammer genitive remain explicit
[@Fulk2018, pp.158-159; @Ringe2017, pp.310-312;
@RingeTaylor2014, pp.114-116,184-186; @Orel2003, pp.156,158].
All eight whole-row causes remain unestablished; no scientific selection,
FST, baseline, introduction or PDF is changed.

The fourteenth tranche completes gang, ghost, gift, give, god, gold,
goose and grass (2038-2045). All141 inherited positions are individually
accounted for, including the two unchanged gift notation-control positions.
Twenty-three literal receipts and ten processes add33 records to existing
consultations; six focused positions reuse evidence and fourteen rationales
are added. Fifteen exact SOURCE annotation receipts and two consultation
status receipts account for the repairs. Its180 positions link171 distinct
records; shared records and different analytical units are not collapsed.

Fulk's directly named dispute with Ringe and Taylor concerns the related
giefu-family genitive: trimoric inherited quantity plus analogical OE -e
versus bimoric quantity plus etymological -e, not selected i-stem ġift
[@Fulk2018, pp.154-156; @RingeTaylor2014, pp.58-61,114].
Give's Irish-cognate admission and gold's collective-accent warrant have
bounded analyst-inferred explanations, not directly named rebuttals or
adopted histories [@Orel2003, p.130; @Kroonen2013, pp.172-173,194;
@Ringe2017, pp.301-303].
Orel's ghost relationship is not an opposite derivational direction;
conditional god origins, goose plural versus later length, and grass
singular versus collective plural remain distinct
[@Orel2003, pp.123,126,140,145; @Kroonen2013, pp.163,168-169,187,193-194;
@Fulk2018, pp.64,72; @RingeTaylor2014, pp.126-128,141,198].
All eight whole-row causes remain unestablished. The existing gift velar-only
control and adopted science are unchanged; corpus, stages/contexts, FSTs,
scientific baselines, introduction and PDF are outside this research increment.

The preceding thirteenth tranche completes fowl, fox, freeze, friend, fright,
frost, furrow and gall (2030-2037). All89 inherited positions have
individual decisions;29 literal receipts and eight processes add37
records to existing consultations. Four focused positions reuse evidence,
twelve rationales are added, and twelve exact old/new SOURCE annotation
receipts preserve date/cell repairs. Its131 positions link126 distinct
records. Friend supplies a directly named, source-explicit disagreement:
Fulk expressly challenges Ringe2017's caution about projecting the
lexical nd-noun class into PGmc, using shared meaning and nonparticipial
inflection while admitting the participle-only account remains possible
[@Ringe2017, p.224; @Fulk2018, p.179, n.1].

Fright's ō/īn citation-formation difference is scoped and substantive,
but its cause and selected-genitive mapping remain unestablished
[@Orel2003, p.120; @Kroonen2013, p.161].
Fowl's fly/dissimilation accounts overlap, and Orel expressly recognizes
OE furrow as a root stem beside his generic ō citation; neither is made
an exclusive etymological conflict
[@Orel2003, pp.116-117,120; @Kroonen2013, pp.157,160].
Fox's feminine counterpart and distinct Nordic loan, freeze/frost's
participle and z/to derivatives, and gall's bile/skin homonyms remain
separate. Kroonen's Latin-fel reservations are not categorical exclusion
[@Orel2003, pp.113,116-117,124; @Kroonen2013, pp.154-155,157-158,165;
@Ringe2017, pp.246-247].
Explicit PWGmc fowl variants and furrow dative plural, post-PIE/PCeltic
roots, a pre-OE compound member, undated index citations, metalinguistic
class labels and native glyphs retain their independent scopes
[@Fulk2018, pp.73,75,178,387;
@RingeTaylor2014, pp.28,202,308,330,386-387].
All eight whole-row causes remain unestablished. Corpus, stages/contexts,
FSTs, scientific baselines, introduction and PDF remain unchanged.

The twelfth tranche completes fly, foal, fodder, fold, folk, follow,
forlorn (selected lose infinitive) and four (2022-2029). All87 inherited
positions have individual decisions;30 literal receipts and eight processes
add38 records to existing consultations. Four focused positions reuse
evidence, twelve rationales are added, and eight exact old/new SOURCE
annotation receipts preserve the corrections. Its129 positions link125
distinct records. Foal's optional comparative root-u versus proposed
laryngeal root noun and follow's admitted/rejected Slavic crawling family
have bounded analyst-inferred explanations, not directly named rebuttals
of Orel2003 or adopted histories
[@Orel2003, pp.117-118; @Kroonen2013, pp.158-159].

Fly is not flutter, flight or the insect noun; Fulk's source-glossed
h-type finite “flies” is identity-limited comparative evidence, not a
certified match to selected g-type *flēogan*
[@Fulk2018, pp.270,301-303,307,387; @RingeTaylor2014, pp.130,309].
The sheath homonym is not selected fodder; explicit PGmc fold and follow
dates come from their lexical sets, not chapter titles. Folk/follow lower
despite their labial contexts; RT's unexplained retained-u indeclinables
are separate comparanda
[@Orel2003, p.109; @Ringe2017, pp.279,287;
@RingeTaylor2014, pp.32-33,327].
Four retains suffix shorthand, reported Stiles cells, preferred versus
reported routes and actual OE inflections; tentative ordinal dissimilation
is not proof of rejection of the coronal account
[@Kroonen2013, p.133; @Fulk2018, pp.224-225].
All eight whole-row causes remain unestablished. Corpus, stages/contexts,
FSTs, scientific baselines, introduction and PDF remain unchanged.

The eleventh tranche completed fish, fist, flask, flax, flea, flee, flesh
and flood (2014-2021). All64 inherited positions have individual
decisions;26 literal receipts and nine process records add35 records to
existing consultations. Six focused positions reuse evidence; fifteen
rationales are added. Twenty-nine old/new annotation receipts cover23
evidence fields and six Fulk applicability/target/consultation fields.
The tranche has105 positions linked to99 distinct evidence records.
Flee's lexical connection and initial-cluster histories have bounded
analyst-inferred explanations, not direct rebuttals or adopted histories
[@Orel2003, pp.106-107; @Kroonen2013, pp.146,544].
Flea's feminine ō versus masculine/feminine z citation is a substantive
formation/gender difference whose cause remains unestablished
[@Orel2003, pp.105-106; @Kroonen2013, p.145].

The formerly matched Fulk fist index examples are actually the damp
adjective. Preserve their original strings and historical IDs as
comparanda, not fist reconstructions; the generic nasal-loss argument
remains a topical consultation. Its applicability and target owners are
corrected without erasing the initial matching error
[@Fulk2018, pp.55,387]. Fish plural metathesis is not an hs-label singular;
flask is not flax; flee's present indicative is not a participle; and
reported Kluge-Seebold/Osthoff proposals are not Orel endorsements
[@Orel2003, pp.104-105; @RingeTaylor2014, pp.188,192,315,345].
Fulk's suffix-accented flood stem does not quote the root-accented
selected full word [@Fulk2018, p.253].
All eight whole-row causes remain unestablished. Corpus, stages/contexts,
FSTs, scientific baselines, introduction and PDF remain unchanged.

The tenth tranche completed fee, fell (hide), fern, field, fight, find,
finger and fire (2006-2013). All117 inherited positions have individual
decisions;18 literal receipts and eight process records add26 evidence
records to existing consultations. Six focused positions reuse evidence;
fifteen rationales and17 old/new SOURCE annotation receipts preserve the
distinctions. The tranche has149 positions linked to143 distinct records.
Field's formation pathways and fire's collective prehistory and
front-vowel/paradigm histories have bounded analyst-inferred explanations,
not direct rebuttals or adopted histories
[@Orel2003, pp.97-98; @Kroonen2013, pp.135-136,151,159;
@Ringe2017, pp.147,162,309; @RingeTaylor2014, pp.119,225].

Orel's written *-an* does not independently establish an n-stem.
Same-string fee cells, field cluster labels/gold comparanda, fight's
analogical past, find's selected inflected participle, and fire's doubtful
dative and unrelated water/wizard/cow evidence remain separate
[@Orel2003, p.97; @Ringe2017, pp.269,271,312;
@RingeTaylor2014, pp.115,119,155-156,318,344,346].
Fern's masculine/neuter difference is substantive but its cause remains
unestablished [@Orel2003, p.94; @Kroonen2013, pp.129-130].
All eight whole-row causes remain unestablished; the exact selected fire
dative is not certified by citation forms. Corpus, stages/contexts, FSTs,
scientific baselines, introduction and PDF remain unchanged.

The ninth tranche individually reconciles146 inherited positions for
drive, earth, eat, eel, fall, fare, fast and father (1998-2005).
Twenty-three literal occurrence receipts and three process records add26
records to existing consultations; four focused positions reuse evidence
and fourteen rationales are added. Twenty SOURCE annotation amendments
retain old/new values. The tranche has176 positions linked to172 distinct
evidence records. Drive's Baltic/Celtic cognate preference and fall's
segmentation/gemination explanation are bounded analyst inference, not
direct rebuttal or an adopted reconstruction
[@Orel2003, pp.76,91; @Kroonen2013, pp.103,125-126].

The corrections distinguish Ringe's intensive/iterative drive from the
preceding causatives, his fasting stative from selected fastening, and
Kroonen's eel/awl comparison from the adjacent feeding verb
[@Ringe2017, pp.282-283,288-289; @Kroonen2013, pp.19,116-117].
RT's coordinated earth n-stem is explicitly PWGmc; the fall label
*pte* is metalinguistic, and calf suffixes do not quote father cells
[@RingeTaylor2014, pp.129,182,385-386].
Expected/leveled fare finite cells and Gothic comparisons remain separate
[@RingeTaylor2014, pp.195-198,232-233].
All eight whole-row causes remain unestablished. Fast retains a
different-units core disposition rather than falsely equating fastening
with fasting. Corpus choices, input stages/contexts, FSTs and scientific
baselines are unchanged; no introduction or PDF is included.

The second tranche reconciles all70 inherited positions for1941-1947
and1949, adds seven occurrence-backed quoted endpoints and four precise
process records to existing consultations, and records seven reasons.
The focused `beaver-colour-direction` case compares opposing derivational
directions and marks its explanatory connection as analyst inference, not
a direct Kroonen rebuttal of Orel or an established whole-word history
[@Orel2003, pp.40-41; @Kroonen2013, pp.56-57].
Its two focused positions reuse existing evidence; core evidence links
are deduplicated without dropping those distinct analytical units.

The amendments receipt preserves the old/new SOURCE annotations: Orel's
bier is literally WGmc, not an expanded PWGmc label; RT's starred Gothic
bag comparison is not an undated PGmc endpoint; Fulk's beaver example
concerns OE back mutation, separately from the explicit PGmc word and
starless index. Berry's Verner paradigm does not supply accented cells
[@Orel2003, p.38; @RingeTaylor2014, p.287;
@Fulk2018, pp.69,386; @Kroonen2013, pp.54-55].
`alignment-1941-1949-occurrences.tsv` records the seven literal source
spans and paragraph hashes; `alignment-1941-1949-amendments.tsv` records
the individually justified reporting corrections. Neither receipt changes
source confidence, diplomatic forms or scientific corpus owners.

The third tranche reconciles all74 inherited positions for1950-1957:
bind, birth, blood, board, bone, book, bore and bosom. Thirteen literal
occurrences and seven process records supplement existing consultations;
nine reasons separate position support, a premised bind representation
bridge and a bounded, analyst-inferred bone-origin comparison.
`alignment-1950-1957-occurrences.tsv` records exact text spans/hashes;
`alignment-1950-1957-amendments.tsv` preserves reporting corrections.
Book's three RT plural citations are explicitly PNWGmc, while Fulk's
plural is explicitly PGmc; Latin profession/loan examples and the selected
OE nominative remain distinct. Native corrupted signs remain unchanged
[@RingeTaylor2014, pp.138,208,227,286; @Fulk2018, pp.64,166-167].
Ringe's actual bone quotation changes its existing consultation from
discussion-only to evidence-found, not into a new consultation
[@Ringe2017, p.328]. Whole-row causes remain unestablished, and neither
bone's origin nor bind's specific written e has been selected as CAPR's
preferred history.

The fourth tranche reconciles all72 inherited positions for1958-1965:
both, bottom, bough, weak causative bow, strong preterite bow, bow noun,
bower and brand. Twenty literal quotations and four processes add24
evidence records, with nine reasons and two focused units reusing evidence.
Fulk's actual strong-present passage is one new consultation; existing
reviews are supplemented, not duplicated [@Fulk2018, pp.263-265].
The source amendment/occurrence receipts are
`alignment-1958-1965-amendments.tsv` and
`alignment-1958-1965-occurrences.tsv`.

The selected strong preterite is not the ring noun quoted by several
sources. The focused `bend-external-cognates` case distinguishes Ringe's
explicit absence claim from Kroonen's external/metathesized connections;
why Ringe excludes those comparisons remains unestablished
[@Ringe2017, p.324; @Kroonen2013, pp.61-62].
Present quantity/origin, weak finite cells, nominal homonyms and selected
preterite remain separate. The current lexical model's RT55 locator does
not support its class-II present claim; the pertinent discussion is39-40.
This is a non-adopting reporting question, not a silent model correction
[@RingeTaylor2014, pp.39-40,55,268,280,296,309].

The fifth tranche reconciles all73 inherited positions for1966-1973:
bread, break, breast, breeches, bride, bring, brook and buck. Twenty-four
literal quotations and four processes add28 evidence records to existing
consultations, with thirteen reasons and four focused positions reusing
evidence. Nine SOURCE annotations are corrected without changing inherited
forms, pages, verification or shared links. The receipts are
`alignment-1966-1973-amendments.tsv` and
`alignment-1966-1973-occurrences.tsv`.

The focused `breast-paradigm-derivation` case distinguishes Kroonen's
qualified single-paradigm hypothesis from Ringe's gender-supported
derivational preference, without claiming a direct rebuttal
[@Kroonen2013, pp.76,80; @Ringe2017, p.223].
The focused `buck-borrowing-direction` case retains opposed donor directions
and their different gemination/formation premises as bounded analyst
inference, not a selected etymology
[@Orel2003, pp.61-62; @Kroonen2013, p.82].
Fulk's expected break participle is an antecedent to the remodelled endpoint
he expressly accepts, not an author opposition. His relevant footnote is
printed290, on holding sheet307, not the earlier class-IV opening
[@Fulk2018, p.290; @Ringe2017, pp.211,272].
Strong dictionary headings, reconstructed weak pasts, actual finite cells,
PNWGmc plurals and pre-OE comparanda remain distinct. The commentary records
non-adopting breast citation-page and breeches input-stage reporting questions;
no model, corpus, stage sidecar, FST or scientific baseline is changed.

The sixth tranche reconciles all100 inherited positions for1974-1981:
burst, calf, chew, climb, comb, corn, cow and craft. Twenty-four literal
occurrence receipts and three process records add27 evidence records to
existing consultations; twelve reasons and four focused positions reuse
evidence. Twelve proved reporting annotations are corrected without
changing any inherited diplomatic/comparison string, page, verification,
confidence, kind or shared-row link. Receipts:
`alignment-1974-1981-amendments.tsv` and
`alignment-1974-1981-occurrences.tsv`.

`calf-greek-cognate-admissibility` contrasts Orel's admitted Greek womb
comparison with Kroonen's two explicit phonological objections
[@Orel2003, p.209; @Kroonen2013, p.278].
`cow-original-formation` contrasts Kroonen's original u-stem/graze account
with Ringe's acrostatic bovine account and unresolved northern stem
[@Kroonen2013, p.299; @Ringe2017, p.223].
Both explanatory relations are bounded analyst inference, not direct
rebuttal or settled whole-row causes. Neuter calf's singular *-az* does
not prove a masculine a-stem; identical Mercian genitive/plural *calfur*
receipts remain separate [@Fulk2018, pp.176-178;
@RingeTaylor2014, pp.205,231,385-386].
Cow's selected *cȳ* remains DAT.SG, even though RT's literal *cy* also
serves NOM.-ACC.PL [@RingeTaylor2014, p.318].
RT's feolan subgroup label is not a burst word, oakum is not comb, and
wizard/fire are not cow-family reconstructions
[@RingeTaylor2014, pp.202,318,347].
Climb preserves explicit PWGmc-only reconstructive restraint and Onions'
reported alternative [@RingeTaylor2014, pp.127-128; @Orel2003, pp.215-216].
The commentary records craft's dictionary-page and selected-input-stage
questions without changing the model or selecting a new history
[@Orel2003, p.220; @Kroonen2013, p.300].

The seventh tranche reconciles all122 inherited positions for1982-1989:
crop, cud, dale, day, deal, deed, deer and dew. Twenty-one literal
occurrence receipts and six process records add27 evidence records;
thirteen reasons and four focused positions reuse evidence. Seven proved
SOURCE annotations and eleven applicability-manifest fields have amendment
receipts, preserving both earlier screens as history:
`alignment-1982-1989-amendments.tsv` and
`alignment-1982-1989-occurrences.tsv`.
Actual omitted consultations are now recorded for Fulk/cud and Ringe/deer;
they are not393 invented negative reviews or a restarted book survey.

`deal-root-derivation` distinguishes Orel's divide-root account with
irregular initial from Kroonen's theoretical put-root account without
direct IE formation parallels [@Orel2003, p.67; @Kroonen2013, p.87].
`cud-e-cognate-admissibility` connects Ringe-Taylor's explicit exclusion of
e-based external cognates to his northern-WGmc u-raising premise, contrasting
Fulk's qualified possible gum/mastic example [@RingeTaylor2014, p.42;
@Fulk2018, pp.57-59]. Both causal relations are bounded analyst inference,
not direct rebuttal or adopted original histories.

Fulk explicitly relates both an iu/i-formation and an eu citation to
OE *dēor* 'beast'; his Finnish-loan claim must not be dismissed as an
unrelated precious-beast etymon [@Fulk2018, pp.12,73,81].
Ringe's independently quoted *diuriz* 'dear' is instead an i-stem
adjective, not an animal noun by string identity [@Ringe2017, p.315].
That formation/lexical-role bridge remains an exact research question.
The separate day/deed paradigm cells, uncertain plurals, reported
s-stem hypothesis, reconstructed OE intermediates, SEED comparator
and conditional DO hypotheses are preserved
[@Ringe2017, p.312; @Fulk2018, pp.129,177,253;
@RingeTaylor2014, pp.114-115,212,239,287,519-520].
The commentary retains non-adopting cud attestation/input and dew
formation questions; scientific owners and released glide history remain
unchanged.

The eighth tranche reconciles all106 inherited positions for1990-1997:
dill, do, door, dough, dove, dream, drench and drink. Twenty-seven
literal receipts and one process add28 evidence records to existing
consultations; four focused positions reuse evidence and fourteen
rationales are added. Five annotation amendments preserve original
form-kind labels, diplomatic strings, glyphs, pages and verification:
`alignment-1990-1997-occurrences.tsv` and
`alignment-1990-1997-amendments.tsv`. The tranche has138 positions linked
to133 distinct evidence records; shared drink/drench evidence is counted once.

`do-present-metrical-history` records a source-explicit rebuttal:
Fulk's light-disyllable metrical evidence challenges the direct athematic
OE present path and motivates thematization/antevocalic shortening
[@Fulk2018, pp.331-332; @RingeTaylor2014, p.369].
It does not settle the ultimate PGmc root, finite past, strong participle
or weak suffix. Ringe-Taylor's older-volume corrigendum is not a correction
of Ringe2017, whose revised paradigm already prefers the same done
participle [@RingeTaylor2014, pp.519-520; @Ringe2017, pp.294-295].
`dream-root-derivation` instead connects Orel's fall/drowse premise
with Kroonen's g-root mo-formation by bounded analyst inference;
Schröder's g-rival remains reported, and the verb homonym/sense bridge
unresolved [@Orel2003, p.75; @Kroonen2013, pp.100-102].

Dill's conditional original NOM/GEN and Fulk's actual accusative remain
distinct [@Kroonen2013, p.92; @Fulk2018, pp.152-153, n.5].
The commentary records a non-adopting model-locator/formation watchlist.
Selected drench is a noun; the causative and u-grade *drync* family
do not establish its a-grade i-stem input
[@Orel2003, pp.74-75; @Kroonen2013, pp.100,103,105;
@Ringe2017, p.282]. Drink's finite cells and cluster/table labels are
not infinitive ancestors or unambiguous postnasal-k chronology
[@RingeTaylor2014, pp.211,347,349-350].
Dove remains research-only with no runnable target; pelican-compound
and onomatopoeia-bibliography evidence do not manufacture one
[@Orel2003, p.80; @Kroonen2013, pp.105-106].
All eight whole-row causes remain unestablished and scientific owners unchanged.

The alignment follow-up corrects eight proved RT extractor clips against
their held paragraphs and preserves four genuinely corrupt native tokens
unchanged. `rt-token_boundary_review.tsv` records the distinction; added
`retained_*` fields in the occurrence receipt retain the original extractor
spans alongside the corrected whole-token spans. Beard's complete optional-z
stem is not an OCR restoration. Bake's omitted OE second singular *becst*
and the cited surrounding paradigm argument supplement its existing
consultation without adding a fake new review [@RingeTaylor2014, pp.180,232-233].

Ringe's bounded original checks resolve the former p.ix and trimoric
glyph limits. Fulk's original checks retain both *sit-j-anaⁿ* and
*setjanaⁿ*, without harmonizing their local dating assertions.
The commentary distinguishes the independently explicit PGmc fight
citations from the PWGmc citation and attestation grouping
[@Ringe2017, pp.ix,108,254,266,271,307,312;
@Fulk2018, pp.43,295].

The historical initial15-scope dispatch was supplemented by a completed Ringe
body-reading block, printed241-266, and its bounded endpoint/method review.
At that checkpoint there were16 scopes: four reviewed and12 pending reading/screening units.
The block adds49 diplomatic records and30 new actual consultations;
Ringe has34 actual reviews, not393 completed applicability screens.
Surface/underlying forms, other cells and conditional or later-stage
reconstructions remain separate [@Ringe2017, pp.242-243,249,252,254-256,262].
Ringe's transcription note is printedix; Fulk's reconstruction discussion
is printed11-12. Full source-convention reconciliation remains pending
[@Ringe2017, p.ix; @Fulk2018, pp.11-12].
Ringe-Taylor's Other conventions must acquire its verified printed roman
folio; PAGE14 is a navigation marker, not a citation.

`population_scope=all_rows` names the live393-row scope of a scheduled
screen/passage; it never says those rows have already been read or directly
mentioned. `named_rows` requires explicit IDs; `source_general` creates no
arbitrary row links. A pending page address identifies where reading starts,
not a claim that the entire relevant passage has been verified.

Completed scopes require actual search/reading assessment and printed
locators. A verification gap retains its specific limit and blocks the
fully reviewed three-source gate. That gate also requires all named sources,
their methods, screens covering the exact population, scheduled passages
and actual target consultations. An empty manifest cannot satisfy it.
Justified amendments must be recorded, not used to delete inconvenient
work. Source-wide relevance/completeness still needs scholarly review;
structural validation alone cannot prove that every useful passage was found.

The existing four-object `load()` API is preserved. Supplementary scopes
are loaded and validated separately. SQL exposes `reading_scopes`,
`scope_rows`, `scope_evidence` and `target_scopes`; membership in a pending
scope is scheduling, not completed review:

```sh
python3 Germanic/tools/pgmc_reconstruction_survey.py --query \
  "SELECT source_key,status,count(*) AS scopes FROM reading_scopes GROUP BY source_key,status"
```

Feature-alignment and position-support versus inter-author explanation
accountability are implemented. They initially migrate every existing
citation-unit case as `alignment_status=unreviewed`, not as completed
feature research. Actual whole-population alignment follows the source
passes. A `bounded_limit` needs cited member evidence and the precise
remaining premise; `feature_aligned` cannot be certified by cell labels
alone. Position-support reasons cannot certify aggregate explanations;
equivalence bridges remain distinct from historical causes.
The new Ringe positions have reviewed citation units and source-supported
features; they do not close the existing393 core comparisons. A local
PGmc-sketch context is recorded without manufacturing an explicit dated
endpoint. The pending parent scopes retain the broader reading commitments.
Production choices, stages, FSTs and baselines remain unchanged; introduction,
PDF, acquisition and release are outside this batch.

The stronger alignment gate first requires the named three-source reading
programme. It then separately requires an aligned or precisely bounded
disposition for every core row. The earlier citation-triage gate retains
its narrower meaning. SQL exposes `alignment_evidence` and
`rationale_conditions`, as well as the explicit scalar depth fields:

```sh
python3 Germanic/tools/pgmc_reconstruction_survey.py --query \
  "SELECT reason_target,count(*) AS reasons FROM rationales GROUP BY reason_target"
python3 Germanic/tools/pgmc_reconstruction_survey.py --query \
  "SELECT alignment_status,count(*) AS cases FROM comparisons WHERE scope='core_triage' GROUP BY alignment_status"
```

## Holding corrections and limitations

### Core dictionary extraction

Orel and Kroonen each have393 actual reviews. This completes the lexical
baseline, not exact selected-cell quotations or scientific explanations.
The page-cited commentary records their different e/i positions.

Orel's preface pp.xi-xiii treats reconstructions as full lexical words,
acknowledges idealized morphology and filters some prefixes/names/loans.
Preserve his barred `đ`, velar sign `ʒ`, quantities and parenthesized segments/endings.
Native PDF text can map `đ` to a pilcrow, and OCR can flatten it to `d`;
neither extraction is diplomatic authority. His indexes are leads, not
guaranteed folios: the light verb indexed at241 is actually on243.

Kroonen's preface pp.vii-viii explicitly warns of omitted established
lexemes/reflexes. His notation/entry structure pp.xii-xiii distinguishes
headwords, reconstructed citations, alternatives and deeper etymological
constructs. Preserve stem dashes and separate homonym labels. Read the
whole relevant discussion: the smear verb is reconstructed inside a noun
entry, and three's short-i headword is not its long-i nominative.
Do not assume a global PDF-sheet offset: printed64 is sheet102,
whereas printed92 is sheet132. The actual running head governs.

For each row, search its OE citation/case aliases, source-specific
reconstruction spellings, semantic entry and cross-references; use the
indexes to locate and then read the actual entries. Search aliases may
vary thorn/theta, h/x, quantity notation and dictionary suffixes, but
they never change the recorded author form. Distinguish desire from
boiling, being from weight, and different paradigm cells. An absent
exact string remains unchecked until a scoped search is actually reviewed.
The initial candidate-class batch is positive evidence, not permission
to fill remaining dictionary pairs with automatic negatives.

### Other holdings

Kluge's held PDF is the 25th edition (2011), verified from its title
and edition-history pages. The older similarly named `.txt` identifies
the 24th edition, not the PDF. `kluge_seebold_2011_25th.txt` was extracted
from the held PDF using `pdftotext -layout`; it retains page breaks and
printed running heads. It requires ordinary glyph/page verification,
not an assertion that every extracted token is correct.

Hirt's held title is part I (1931), not evidence that the complete
three-part handbook is held. The Pokorny holding is a partial page
directory. Ringe-Taylor is held here as a text extract; missing local
images are explicitly distinguished from earlier dossier verification.
Generic Kylstra/Oxford filenames are aliases of identified sources.
The separately held Luehr thousand article is identified as Lühr1993,
Linguistica33, pp.117-136, and catalogued separately from the1998 EWA
contribution. Its scientific argument and forms still require review;
holding identification does not complete its corpus coverage.

No acquisition or whole-library OCR is authorized. Do not include private
correspondence as a published independent reconstruction source.

### Completed identity audit and remaining holding limits

The catalogue now distinguishes the actual seventh-edition Sweet1893
primer from the unheld Sweet1953 revision, and Toller1921's supplement
from the unheld BosworthToller1898 main dictionary. The excluded old
associations remain visible. This routes the same intended local reviews
to their real sources; it does not automatically retag or reverify old
scientific citations.

The two Howell/Salmons text extracts are byte-identical. The original
article and existing bibliography identify1997, pp.83-111;1988 remains
only a legacy key/filename, not a second publication.

Two genuinely additional held works are included: KlugeSeebold2002's
24th-edition text, with no established matching original or folio map,
and Kuiper1991's review, pp.105-120, appended to the MayrhoferIII scan.
Mayrhofer's three volumes are1992/1996/2001; Kuiper's review of early
fascicles is not Mayrhofer's dictionary argument or a review of the
completed three-volume work. Separate editions and reused files do not
provide independent author votes.

Pokorny's700 filenames are sheet identifiers:688 extracts are nonempty,
12 empty; visible printed502 is on sheet12 and1183 on sheet693.
The substantive holding begins around H/interjections, not page1;
no global page map or complete dictionary is certified. Stiles1985 is
only pp.89-94. Ringe1984's14-sheet scan ends at printed151, with a
conclusion/byline there; the cited publication extends to155, whose
remaining pages are not established as held. The bibliography's former
journal/page association is corrected, not substituted into old quotations.

Neri's held Ringe review is numbered1-12 and signed by its author;
the following Casaretto review is separate. Its publication date/venue
are not established by the detached holding, so the unsupported
Kratylos54(2009),156-160 association is withdrawn. Three other detached
articles retain explicit date/issue-verification limits. Bennett's curated
transcription has ellipses; the original PDF remains available for those
omitted passages. A title/edition audit never certifies reconstruction
conventions, entry extraction or whole-source negative searches.

## Prioritized consultation programme

All91 catalogue records are preserved:82 available and nine actual
exclusions;75 available identities are verified and seven have declared
metadata/holding limits. Availability is not a row-review obligation.
The superseded32,226-cell grid and31,749 unchecked checkpoint are historical
measurements of the old policy, not the current workload.

The current evidence has1457 diplomatic records and838 actual reviews:
786 core and52 other-source consultations. The completed dictionary
integration baseline of1408 records/808 reviews is preserved beneath
the Ringe body-reading supplement. Orel has393 positives, including
qualified family/component evidence; Kroonen has360 positives and33 bounded
negatives. These are not393/360 exact selected-cell agreements.
Kroonen's verification now records187 image-checked,503 text-checked and
one ledger-verified item after the spare metadata correction on printed465;
Orel's remainder is not universally image-checked prose.

| Priority / mode | Sources and bounded payoff |
| --- | --- |
| 0 / core_dictionary | Orel2003, Kroonen2013: complete393-row lexical baseline, now reviewed. |
| 1 / systematic_relevant | Ringe2017, Fulk2018, RingeTaylor2014: relevant indexed forms, methods, phonology/chronology and cell explanations; not393 arbitrary grammar negatives. |
| 2 / systematic_relevant | Bammesberger1990, Seebold1970, Kroonen2011: explicit nominal, verb-family and n-stem rosters drawn from unresolved cases. |
| 3 / systematic_relevant | KlugeSeebold2011, LloydSpringer1988: competing etymologies/loans for relevant Germanic families; EWA remains limited to the held volume. |
| 4 / case_triggered | Relevant phonology, numeral, formation, OE-history and subgroup specialists: named consequential questions only. |
| 5 / opportunistic | Mayrhofer, Beekes, Pokorny, Kuiper, attestation/background works and older-edition comparisons: consult exact relevant evidence, never blanket393-row treatment. |

The catalogue owns each entry's explicit mode/payoff; the generated
`source_priorities.tsv` exposes all assignments, including exclusions.
The active three-source stage now has31 finite Ringe row targets in
`review_targets.tsv`, linked to their actual quotations and broader
pending reading scopes. Further target rosters must name the question, applicable source
scope and new information expected. Stop expansion if a reviewed screen
adds no consequential form, argument, counterargument or diagnostic.
Never infer that result from a failed search, source title or bibliography
presence. Existing contextual evidence remains available regardless of mode.

## Analytical layer and query boundaries

There are1515 evidence/row positions,393 core citation-unit cases, one
narrow representation case, one premised stem case and46 cited rationales.
The twelve initial worked
calibrations are adder, cud, drench, find, gift, hind, knee, man, three,
wash, world and hue. Core triage retains all alternatives, including
deeper/conditional/rejected proposals, and records insufficient evidence
where a dictionary has a bounded negative. Much of the remaining triage
is unit-level and deliberately `undetermined`; it is not an explanation
of every visible difference. Twenty-nine core cases have linked reasoning;
a position's cited argument does not necessarily explain the inter-author
difference, so several such cases still have `unestablished` explanations.

`ending` often describes word-versus-stem presentation, not competing
inflectional reconstruction. Other overlapping tags distinguish notation,
transcription error, inventory, vocalism, quantity, ablaut, consonantism,
stem class, gender, suffix, inflection, segmentation, chronological stage,
PGmc membership, lexical/cognate identity and historical analysis.
Tags on an undetermined case identify research questions, not settled
scientific disagreements or independently counted events.

Analyses preserve unknown stage/endorsement and source qualifications.
Dictionary context cannot establish a dated PGmc endpoint. An analytical
form reuses only the diplomatic form or its already explained comparison
notation; the feature JSON and evidence IDs retain its scope. Quantity,
optional material, segmentation and uncertain signs are never stripped.
Equivalence is scoped to unit, features, stage and explicit premises;
no transitive closure is inferred between differently premised cases.
The gift ʒ/g example establishes only representation of one citation,
not a stop/fricative reconstruction or equivalence with inherited i.
The spare example compares differently displayed weak-verb stems under an
explicit citation-segmentation premise, without assigning their date or
silently replacing either author's quoted form.

Queries construct validated tables in memory with Python's stdlib SQLite;
there is no editable database/service. In addition to the SOURCE tables
and live `corpus`, normalized bridges are `comparison_rows`,
`comparison_types`, `comparison_analyses`, `analysis_features`,
`evidence_rows`, `comparison_rationales`, `rationale_evidence` and
`rationale_analyses`. SQL is read-only; results are TSV.

```sh
# Reviewed vocalism questions and their explanatory certainty.
python3 Germanic/tools/pgmc_reconstruction_survey.py --query \
  "SELECT c.comparison_id,c.comparability,c.explanation_status FROM comparisons c JOIN comparison_types t USING(comparison_id) WHERE t.type='vocalism' ORDER BY c.comparison_id"

# Source positions that are explicitly later than the unspecified dictionary level.
python3 Germanic/tools/pgmc_reconstruction_survey.py --query \
  "SELECT a.row_id,f.source_key,f.printed_pages,a.analytical_form,a.stage_interpretation FROM analyses a JOIN forms f USING(evidence_id) WHERE a.stage_interpretation IN ('pwgmc','wgmc','proto_norse') ORDER BY a.row_id,f.evidence_id"

# Why a case is disputed, including source pages and inference/author attribution.
python3 Germanic/tools/pgmc_reconstruction_survey.py --query \
  "SELECT r.comparison_ids,r.basis_type,r.support_mode,r.statement,f.source_key,f.printed_pages FROM rationales r JOIN rationale_evidence re USING(rationale_id) JOIN forms f USING(evidence_id) WHERE r.basis_type IN ('loan_hypothesis','analogy','pie_reconstruction') ORDER BY r.rationale_id,f.evidence_id"
```

The atlas is the page-cited analytical view; the ledger remains the fuller
source argument/verification companion. The shorter introduction, new PDF,
next large extraction and any scientific adoption are separate work.
