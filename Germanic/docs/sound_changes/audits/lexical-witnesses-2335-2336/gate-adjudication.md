# Lexical-witness input-gate extension

## Identity

- SC id: n/a; input coverage, not a historical sound change.
- Executable identifiers: `pgrmInputTailVowel`, `pgrmSimpleWord`,
  `pgrmCompoundSecond`.
- Branch / base: `update`, `0dd533e3f15c85f20a976a3781a9b4d79bf6f928`.
- Authorization: the user's subsequent instruction expressly permits
  extending the PGmc proto-phonotactic gate. All downstream sound-law,
  stress, chronology and existing lexical-input prohibitions remain.

## Question

Does a finite input-tail inventory, rather than an invalid reconstruction,
prevent the independently attested feminine-genitive earthly cell from
being evaluated? Confirmation requires admission of the source-supported
ending without changing the existing 389 outputs or any downstream
definition. A changed old output, ambiguous encoding or a required
sound-law repair would refute this gate-only implementation.

## Current state (before any edits)

The preserved `pre_gate.json.gz` contains the complete isolated first run:
22 candidates, every actual stage including nonfirings, parser rejection
locations and the original 389-record baseline.

Hyphenated *xwí-līkaz* and *érθa-kundaz* already parse. The hyphen is
the existing input separator and is deleted immediately; it adds no
historical sound change or surviving boundary. Unsegmented equivalents
are outside this finite grammar. The inherited genitive ending *-aizōz*
is absent even with the compound separator. A parser refusal does not
make the source reconstruction linguistically invalid.

## Diagnosis

`gate_experiment.json.gz` preserves an isolated, generic extension,
with canonical source and binaries protected against mutation. Every
old input produces exactly its old output. The original population
remains 389 accepted, 381 exact and eight mismatches, with no ambiguity:
`d6e8b90551e4bb57d8d161a8f2334c29620533a487a0e64f8857f500380d5e45`.

| Candidate | Pre-extension | Extended gate and unchanged laws |
| --- | --- | --- |
| *xwí-līkaz* | accepted: hwileċ | hwileċ |
| *érθa-kunðaizōz* | input rejected | eorþocundere |
| *érθa-kùnðaizōz* | input rejected | eorþcondere |
| *wír-àldiz* | weorold | weorold |
| *régna-bùgô* | reġnboga | reġnboga |

These are accepted predictions, not claimed attestations or regular
derivations. The genitive target is *eorþcundre*. Bosworth–Toller's
supplement quotes *Ealre eorþcundre gesceafte*, with Latin *totius
terrestris ... creaturae* (An. Ox.691), whereas the bare lemma alone
would not establish a selected attested cell. The Genesis quotation's
*eorþcunde eád* is not silently assigned a masculine accusative: the
dictionary identifies *eád* as neuter.

The grave hypothesis triggers linking-a syncope and is then removed by
SC038. It does not protect the later u from SC040. The plain hypothesis
retains the linking vowel, which SC036 raises before SC040 lowers it.
Both genitives also retain an extra medial e in the ending. Which
retains long ī through the earlier syncope region, subsequently shortens
and lowers it, and produces an extra e; dotted ċ is an orthographic
representation, not the primary segmental mismatch.

Witness roles here are input-coverage positives and phonological
diagnostics, not newly demonstrated chronology edges.

## Literature

- Orel2003 pp.85,201 supplies the formations *erþa-kunđaz* and
  *xwi-līkaz*. His barred đ is not silently quoted as ordinary d.
- Fulk2018 §9.2 pp.209–210 supplies strong-adjective gen.sg.f.
  *-(a)izōz*. Adding that ending to the compound is a CAPR cell
  assembly, not Orel's quotation of a complete inflected word.
- HoggGrammar2011 §2.89 pp.49–50 supplies the compound-like history
  of -cund/-līc and the accented comparison gódcùnd. It does not
  independently certify the exact prehistoric accent of earthly.
- Fulk2018 §5.6 pp.92–94, HoggGrammar2011 §6.68 p.244 and §7.16
  pp.253–254 motivate investigating the shortening, syncope and
  palatalization history of which separately.

## Historical analysis

Stage and scope of all historical rules remain unchanged. The new
network maps input notation to existing starred symbols; it neither
rewrites a historical vowel nor inserts a morphological sound-law
condition. Its separate input-only tail is intentional: changing the
old `pgrmWeakTailVowel` directly would also alter definitions that
reference it downstream. The new endings are generic and carry no
word identity or exception flag.

The source establishes the available adjective ending, not a new
phonological rule or a complete successfully modelled history.
No new analogy, secondary-stress survival claim, or chronology edge
is adopted. The two accent hypotheses remain separate.

## Verdict

REFORMULATE input coverage / RETAIN every historical rule and order.
Registry-verdict: n/a; no registry verdict changes.

The gate should permit source-supported inherited cells to expose
the cascade's actual limitations. Acceptance is not correctness of
the resulting derivation. No attempt is made to remove the recorded
downstream mismatches.

## Propagation

Only the two grammar definitions and one new input-only helper change
in canonical Foma SOURCE. Sandbox, runtime evidence and projections
are owned by `adjudicate.py --refresh`. The experiment receipts are
frozen records, not generated-current-state substitutes.
Tests compare the complete definition set and executable sequence,
conserve every old result and distinguish parsing from successful
derivation. No baseline is refrozen for the gate extension.

The production checks executed through the backend container: generic
simple-adjective and compound genitives are accepted, malformed endings
remain rejected, and every original selected output agrees with the
preserved receipt. The focused run passed 60 tests and 413 subtests,
including the existing baseline, input-context, SC112 and registry
protections. Duplicate identical Flookup paths are collapsed, as in the
shared evaluator; distinct outputs are not hidden.

Canonical refresh rebuilt runtime bins, full traces and the input-root
interaction matrix. No matrix row changed; only its provenance needed
updating for the expanded admitted language. The first attempt failed
to write its definition image. Small diagnostic reproductions did not
reproduce that failure, and the subsequent stable-source canonical
refresh succeeded without changing the harness. No speculative tooling
repair or relaxed validation was introduced.

Reproduction from this gate-extended state:

```sh
python3 Germanic/tools/adjudicate.py --refresh
CAPR_TEST_MODE=full python3 -m pytest -q \
  Germanic/tests/test_lexical_witness_input_gate.py \
  Germanic/tests/test_cascade_baseline.py \
  Germanic/tests/test_oe_input_context.py \
  Germanic/tests/test_sc112_monosyllabic_final_r.py \
  Germanic/tests/test_registry_consolidation.py
```

The private receipts were produced by `experiment.py` before the SOURCE
extension; `--extend-input-gate` tested the proposed generic ending
without editing canonical files. On the extended SOURCE, the ordinary
invocation now traces the admitted cells directly. The recorded base
commit, source hash and explicit extension flag distinguish the
historical experiments from a fresh run.

## Residue

The two lexical admissions and their publication are a subsequent
part of the existing assignment, not completed by this gate extension.
Lord remains deferred. Its source *rð* cluster still lacks input
coverage; underlying-stop diagnostics do not prove that the source
form was historically invalid. No such input is selected here.
World and soul are not reopened.
