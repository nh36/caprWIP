# Lord: deferred source and executable preparation

Research dossier only. No corpus row, reserved identifier, production
selection, published model or new sound law is authorized here.
The experimental base is `0dd533e3f15c85f20a976a3781a9b4d79bf6f928`.
See `gate-adjudication.md` for the protocol-based scope decision.

## Formation and source differences

Fulk2018 §5.6 pp.92–94 discusses a formation of the type
*xlaiƀa-warðaz*, including the weak vowel's retraction/rounding history.
CAPR's ordinary input b is its phonemic serialization, not denial of a
fricative realization. The printed source and the selected CAPR
representation must not be conflated.

The original historical OED was consulted directly after modern OED
URLs returned HTTP403. The public-domain 1908 L volume, printed p.442,
s.v. *lord*, was read in searchable text and checked against its actual
page image: Internet Archive `oed6aarch`, zero-based sheet455.
The OED reconstructs the prehistoric stem *hlaiƀward-* and the two
components *hlaiƀ* 'bread' and *ward* 'keeper'. It does not print the
same complete linking-a nominative as the Fulk-type candidate, or
independently label its prehistoric stem Proto-Germanic.
The forms must therefore remain distinct [@OED1908L, p.442].

The OED records OE *hlāford* and *hlāfweard*, cites the latter in
Ps.civ.17 and notes a misprint in Thorpe. This is the dictionary's
text-critical report, not a new inspection of that manuscript or edition.
It treats the whole word as absent from the other Germanic languages
and the late Norse comparison as borrowed. That is a substantive limit
on reconstructing the compound's age from inherited components alone.
Its phonological references are Bülbring §§367,411,562, not an
independent modern derivation of every step.

Barrack1975 p.53, checked in the newly ingested original PDF, compares
alternative lord histories with different compounding/accent-loss
assumptions. His discussion includes *hlāfweard*, *hlāferd*,
*hlāford*, *hlāfurd* and *hlāfard*. Rule468b removes w;333b/c
provide rounded/raised outcomes, while338/369 belong to a front-vowel
branch. These are source-local rule numbers, not CAPR SC identities.
He rejects a necessary retraction intermediary in Campbell's account
as redundant within his analysis. This genuine analytical difference
must survive future synthesis [@Barrack1975, p.53].

HoggGrammar2011 §6.7 pp.217–218 compares lord/world weak-vowel
variants. That resemblance does not establish identical compounding,
prosody, input level or rule domain for the two words.

## Unchanged-cascade diagnostics

`pre_gate.json.gz` and `gate_experiment.json.gz` preserve every stage.
The source-dental candidates *xláiba-warðaz* and *xláiba-wàrðaz*
are rejected by the finite input grammar: rð is not an admitted
complex coda. This is parser coverage, not a historical refutation.
The isolated feminine-genitive extension does not alter that fact.

The b/underlying-stop diagnostics *xláiba-wardaz* and
*xláiba-wàrdaz* parse and both predict `hlāfēaweard`, not the
intended *hlāford*. These are clearly labelled notation/stop
diagnostics, not newly adopted historical inputs. Their common actual
firing sequence is:

1. Input normalization.
2. Final z-loss.
3. Ai monophthongization: first-element *ái* becomes *ā*.
4. `OEAwLongDiphthong`: linking *a* before w becomes *ēa*.
5. In the grave candidate only, `OEStripSecondaryStress` removes the grave.
6. Final bare-a loss.
7. Unstressed brightening of the second-member a.
8. Breaking before rd.
9. B allophony.
10. Orthography and star/accent removal.

No linking-vowel syncope, medial rounding-to-u, or w-loss appears.
The earliest output-relevant positive divergence is the retained linking
vowel's treatment by `OEAwLongDiphthong`; identifying that application
does not independently settle whether the historical problem is its
scope, earlier reduction, or the formation's input/staging premise.
The grave is not an output-saving flag: it neither prevents that
application nor improves the result.

The explicit beta-notation diagnostic *xláiβa-warðaz* is also
input-rejected. A phonetic symbol's existence in an internal alphabet
does not guarantee its admission as input. A later admission should
settle the source's consonantal normalization rather than silently
substitute a later stage.

## What remains before admission

The historical OED's compact stem and Fulk-type linking-a form are
real alternatives, not corroborating transcriptions of one word.
Future authorized work should compare their formation/accent premises,
the dating of compound formation, linking-vowel reduction and w-loss,
and which attested variant/cell supplies the longest defensible regular
span. It may also extend the generic input coda inventory if the
source-dental form is chosen; the user permits input-gate changes.

The existing world decision is neither a result to undo nor a template
that selects lord's input by analogy. No world/soul rule is reopened,
and none of these research diagnostics enters the production population.
