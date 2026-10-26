# World: complete-cascade candidate assay

Scientific decision: [world adjudication](../world-2302-adjudication.md).
The initial receipt below belongs to the first investigation published at
`61a0d67e`. The follow-up A–F reassessment is documented separately below;
neither rewrites the original receipt or frozen SC036 staged experiments.
All Foma work runs privately in the backend; no production file is replaced.

```sh
python3 Germanic/tools/adjudicate.py SC036 --evidence
docker compose exec -T backend python3 \
  /usr/app/docs/sound_changes/audits/world-2302-experiments/experiment.py \
  > /tmp/world-first-replay.json
```

The runner validates the fresh canonical manifest, compiles isolated
components and a complete identity, and compares every cumulative named
snapshot against production. Each alternative evaluates all389 selected
inputs. Membership of the migration-aware380 is joined by stable row ID;
it overlaps selected389 and is not another380 independent observations.
The complete protected baseline directory, canonical source, sandbox,
corpus, manifest and bins are hashed before and after:169 files unchanged.
No archival fingerprint is adopted. Runtime failures or ambiguities are
fatal for production rows. Candidate rejection records its first component
and is not silently converted into a successful output.

## Mandatory twelve candidates, from the complete input parser

| Candidate family (initial í or é) | Identity final | Interpretation |
| --- | --- | --- |
| `*wír-àldu`, `*wér-àldu` | weorold | Current compact input and inherited-e alternative |
| `*wír-aldu`, `*wér-aldu` | weorold | Grave dispensable for this final alone |
| `*wír-àldō`, `*wér-àldō` | weorold | Additionally feeds SC019 |
| `*wír-aldō`, `*wér-aldō` | weorold | Earlier ending, no grave |
| `*wíra-àldō`, `*wéra-àldō` | weorauld | Literal hiatus survives SC037; not a valid final |
| `*wír-àldiz`, `*wér-àldiz` | wereald | Early third-nucleus i apocope, then medial fronting/breaking; no surviving umlaut trigger |

No candidate is a new attestation. Root *i/e*, morphology, literal hiatus
and accent are independent dimensions. Complete full-start i-stem
acceptance supersedes using a deliberately later staged-entry rejection
as if it were the entire cascade's prediction; the old receipt is unchanged.
Candidate spelling follows the existing CAPR input conventions: `d`,
primary acute, optional secondary grave and a non-syllabifying hyphen.
Orel's comparative `đ` and unaccented headword are quoted separately;
the CAPR spelling is not an independently verified transcription of them.

Six further schematic inflection comparisons are recorded for every model.
They use Fulk2018's general class endings, not invented actual *world*
paradigms: short-i, long-i dative, genitive *-aiz*, ō-stem nasal accusative,
and trimoric/bimoric genitive alternatives. The long-i dative,
*-aiz* and trimoric-genitive shapes are rejected at `EnglishProtoInput`,
not refuted historically. Accepted short-i gives `wereald`; the nasal
accusative and bimoric genitive give `werealde` under identity. Thus
no accepted oblique probe supplies an independently proven regular
replacement cell. The wider diagnostic gives `weorolde` for those two
ō-stem obliques, but that does not prove a new sound law.

## Complete alternative models and every selected final delta

| Model | Final deltas against production | Meaning |
| --- | --- | --- |
| identity | none | Canonical controls agree |
| strip-after-input |2148 rainbow: reġnboga → reġnofuga | Premature grave removal loses a needed compound marker |
| strip-before-SC036 | same rainbow delta | Not an adoptable general stress correction |
| strip-after-SC037-before-raising | none | Move SC036 after linking syncope and strip before raising; marker-compatible serialization, not a historically dated stage |
| rounding-only-same-context |2201 soul: sāwol → sāwal;2302 world: weorold → weorald | Substituting o alone encounters later final-unstressed-o lowering; do not change soul |
| factored-rounding-then-raising | none | a/à→o→u with identical context; formal factorisation, not two independently demonstrated laws |
| wide-before-l-diagnostic | same two finals as rounding-only | Drops following-u restriction and allows weak rounding before l; domain-sensitivity bound, not endorsed universal law |

All listed changed rows also belong to380. Every unlisted selected final
is unchanged. Intermediate differences and focal world/rainbow traces
remain in JSON, including early-strip extra linking vowel and later
b-allophony. No successful alternative is selected by output fit.
The wider phonological proposal is supported only in broad qualitative
terms by weak-vocalism literature; its exact synthetic domain lacks
independent positive/negative lexical evidence for production adoption.

## Controls and limitations

Eight component probes pair a real-world-shaped positive with right-j,
following-i, primary-stress, lack-of-u, grave versus plain, literal hiatus
and inserted-consonant linking controls. Plain/grave mappings share the
u-conditioned context. SC037 leaves the literal adjacent vowels intact
but removes the weak linking vowel in the consonant-separated synthetic
control. Neither probe is an attested word.

The broader generic control set, including *lunganjō*, is retained in the
accepted SC036 receipt; this scoped assay adds world/paradigm/prosody
questions, not a new census of historical attestations.
Earliest stripping is an experiment, not a proposal for lexical stress
loss. No independently dated later deaccentuation law was found, so the
late-marker-compatible model cannot honestly be labelled one.
Source hashes/manifest, not the hard-coded research base alone, identify
the exact runnable state. An editorial NOTE change alters the corpus-file
hash without changing any selected phonological input.

## Follow-up: six historical families A–F

Base: `61a0d67ef02a8da681ab21fba741b0ad63ea0a95`. New evidence:
[`reassessment.json`](reassessment.json), with the same full-start parser,
current component semantics and complete cascade. Reproduce separately:

```sh
docker compose exec -T backend python3 \
  /usr/app/docs/sound_changes/audits/world-2302-experiments/experiment.py \
  --reassessment > /tmp/world-reassessment-replay.json
```

Fourteen configurations evaluate all389 production inputs,18 candidates
and six schematic paradigm comparisons each. Identity agrees with every
canonical cumulative snapshot and final. All172 protected files remain
unchanged; no candidate is installed. Exact definitions and component
orders are in `experiment.py` and the receipt, including the fresh build
manifest, source/corpus/bin fingerprints,23 probes, all changing stages,
all production intermediate deltas and every final delta.

### Input and historical assumptions

| Family | Starting point / pre-encoded intervention | Historically regular opportunity / remaining assumption |
| --- | --- | --- |
| A incumbent | Compact `*wír-àldu`; class shift and reduced junction already supplied; root grave retained | Initial lowering, proxy raising, back mutation, apocope, medial lowering; analogy's early date and proxy's domain unproved |
| B inherited/current | Compact `*wír-àldiz` or schematic short-i `*wír-aldi`; no class shift | Early final-i loss is regular in this model; no raising, then medial fronting/breaking gives `wereald` |
| C inherited/improved weak vocalism | Same inherited input; source-motivated pre-lC high-vowel candidate | Can derive `weorold` without analogical u; exact prosodic domain/high outcome is not independently established |
| D separate rounding/raising | Same inherited input, weak low→o and optionally o→u | Distinguishes actual weak rounding from further raising; o-only later encounters SC100, while further raising succeeds |
| E earlier ō-stem/improved phonology | Compact `*wír-àldō`, grave or plain; class shift still pre-encoded | Derives SC019 additionally; does not independently date analogy before SC019 or select a donor cell |
| F compact plain/grave | `*wír-aldu` vs `*wír-àldu`, also inherited grave/plain and nasal-accusative probes | World final alone does not require grave; global stripping damages rainbow; no new general deaccentuation law |

Initial `*wér-` is compared in parallel without treating that reconstruction
as a means of collecting another firing. Literal `*wíra-àldō` still yields
`weorauld`: changing weak rounding does not settle the compound junction.
The compact early compound is a legitimate comparative candidate; no
new contraction law is inferred from this failure.

Accepted inherited candidates trace early short-i apocope at exec8,
initial lowering19, final-z loss23, missing SC03645, stripping47,
weak fronting51 and medial breaking54. The first uncorrected medial
path is therefore visible before the wrong final, not as an input
rejection. The conservative actual endingless OE accusative is a
stronger historical cell lead than any fabricated full paradigm.
Schematic long-i/genitive/trimoric forms and the additional `*wír-aldį`,
`*wír-àldį` are rejected at `EnglishProtoInput`; this is a software
coverage limit, not a historical result.

### Exact private operations and placement

`WToU` maps plain a, grave à or æ to u after a preceding vowel/
consonants, before l + consonant; `WToO` maps the same targets to o.
`WOToU` raises o in that pre-lC domain. None requires following u.
`WOUOnly` instead raises o only in the incumbent following-u/ū,
no-right-j context. These are source-motivated bounds, **not** approved
exceptionless historical laws. The definitions use the existing symbol
classes rather than treating literal starred strings as single symbols.

- C-early-high replaces SC036 in place; C-postfront-high replaces it
  with identity and inserts `WToU` after exec51 fronting.
- C-supplement-high retains SC036 and adds `WToU` after51.
  C-after-breaking delays it until after54.
- D-rounded-only omits SC036 and inserts `WToO` after51;
  D-rounded-then-high also places
  `WOToU` before back mutation70. D-high-before-u-only uses `WOUOnly`
  there instead.
- D-existing-raising-earlier moves existing SC099 before back mutation.
  D-no-final-lowering uses `WToO` but omits SC10084.
- The strict-back controls explicitly compose e→eo and é→éo before
  labial/liquid + u, keeping the broad æ→ea branch. They compare high
  and o-only candidates against the **actual** production definition.
- F-global-strip-control removes grave after the parser. This is a
  negative control, not a proposed historical stress-loss rule.

### Every final production difference

`i` below means compact inherited i-stem; `ō` means earlier ō-stem.
Both initial-vowel choices and grave/plain counterparts are available
in the receipt, not independent witnesses.

| Configuration | i final | ō final | Every selected-row final delta |
| --- | --- | --- | --- |
| identity | wereald | weorold | none |
| C-early-high | weorold | weorold |2201 sāwol→sāwel |
| C-postfront-high | weorold | weorold |2201 sāwol→sāwel |
| C-supplement-high | weorold | weorold |none |
| C-after-breaking | wereald | wereald |2201→sāwel;2302 weorold→wereald |
| D-rounded-only | weorald | weorald |2201→sāwel;2302→weorald |
| D-rounded-then-high | weorold | weorold |2201→sāwel |
| D-high-before-u-only | weorald | weorold |2201→sāwel |
| D-existing-raising-earlier | weorald | weorold |2201→sāwel;2327 wundude→wundode |
| D-no-final-lowering | weorold | weorold |2127 mōnaþ→mōnoþ;2201→sāwel;2310 macaþ→macoþ;2312 boraþ→boroþ;2314 leornaþ→leornoþ;2316 liccaþ→liccoþ;2318 sċēawaþ→sċēawoþ |
| back-u-only-control | wereald | weorold |none |
| D-rounded-u-only-back | werald | werald |2201→sāwel;2302→werald |
| D-high-u-only-back | weorold | weorold |2201→sāwel |
| F-global-strip-control | wereald | weorold |2148 reġnboga→reġnofuga |

Every listed delta except2327 (*wundude*) also belongs to migration-aware380.
That later lexical addition is outside380; the moving-SC099 experiment
therefore changes two selected389 outputs but only soul within380.
Those are overlapping populations, not independent confirmations. Unlisted selected
finals are unchanged. Soul's deltas are reported as protected side effects,
not adjudicated here; none is adopted or hidden with a lexical exception.

### What actually discriminates

1. **Analogy is not computationally necessary.** C-postfront-high gives
   inherited `*wír-àldiz → *w*é*r*æ*l*d → *w*é*r*u*l*d →
   *w*éo*r*u*l*d → *w*éo*r*o*l*d → weorold`. The high candidate
   can act before or after early fronting, but not after atomic ea has
   formed. Supplementing rather than replacing SC036 changes no
   production final; that controls the soul dependency without certifying
   the additional domain historically.
2. **O-only failure has two separable causes.** The real production
   back-mutation component accepts o and a for acute/plain e because
   Foma shares the comma contexts. Thus `*w*é*r*o*l*d` really becomes
   `*w*éo*r*o*l*d`. SC100 then maps the now final-syllabic o to a.
   Explicitly composed u-only branches instead leave initial e:
   `werald`. Neither result disproves a historical rounded stage.
   No back-mutation production change is adopted.
3. **Further raising can work without following u.** D-rounded-then-high
   succeeds for the inherited input, including with strict-u back
   mutation. It has two synthetic operations where the sources do not
   establish their exact independent boundary or dates.
4. **Moving another operation is not an explanation.** Earlier SC099
   misses final-syllabic o after early i apocope and also deprives
   *wundude* of later raising. Bypassing SC100 rescues the o-only
   world candidate but changes six other lexical items plus soul.
   These are diagnoses of current architecture, not reasons to change it.
5. **Prosodic conditioning remains the historical obstacle.** Primary
   acute, no preceding nucleus, no lC, and immediate right-j controls
   stay unchanged. Synthetic ordinary-weak and twofold-shaped controls
   raise under `WToU`; a plain/grave class is not an independent measure
   of reduced compound prominence. Attested *twifald/twifold* supports
   weak low/o variation, not an invented *twifuld* or proof of an earlier
   universal high stage. The candidate therefore cannot yet be installed
   as a demonstrated general sound law.

### Adopted decision

Choice6 of the assignment: provisional production hold, with a substantive
correction to the historical claim. Early analogy is compatible but its
necessity is **not established**. The inherited source-led alternative is
retained as genuinely viable; failure of B cannot choose between it and A.
What blocks adoption is the independently unestablished prosodic domain,
o/u boundary and compact-junction history, not a wish to preserve389 outputs.
No confidence upgrade, chronology edge, lexical exception, new selected row,
rule change, baseline refreeze or historical receipt rewrite is made.

### Follow-up validation and publication receipt

Source intake verifies eight bibliography identities from six local PDFs,
their complete searchable extracts, sheet maps and hashes. The two new
originals, complete text and private acquisition receipt remain Git-ignored.
Čermák was read completely; Sauer selectively, with the precise image
checks recorded in the intake and claim ledger. No new full-volume or
blanket diplomatic-image certification is claimed.

Canonical strict refresh and `SC036 --check` passed. The affected strict
test run passed92 tests, including fresh Docker replay of the original
world assay, all14 reassessment configurations, and the existing SC036
clause/chronology experiment. Fourteen additional scoped override/emission
tests passed. A first documentary assertion incorrectly classified later
addition2327 as a legacy380 member; correcting it followed the actual
stable-ID membership, not a receipt or baseline edit. The first strict
publication attempt stopped before rendering on three index candidates:
the moved *a+a* override and two model checkpoints under the newly named
projection heading. Scoped SOURCE ignores resolve those false positives
without rewriting scholarly prose. The resumed supported build passed;
this was not a second exploratory publication.

```sh
INDEX_VERBORUM_STRICT=1 ASSEMBLY_KEEP_DEBUG_TEX=1 \
  bash Germanic/docs/assembly/build_capr_book_draft_docker.sh
```

The complete combined book has303 PDF sheets, the lexical volume160,
and sound-change reader108. Exact executable/reader/combined parity
holds for97 published identities. Bibliography, printed Foma definitions,
source links, strict index readiness,18 negative index fixtures and
publication references passed; unresolved internal references and paragraph
gloss violations are zero. Pandoc's nonfatal interrupted-ticker diagnostics
remain visible in the build log; all renderer/checker exits succeeded.
Final strict graph freshness reports CONTROL PLANE CLEAN.

Original rendered images were inspected for combined sheets69–70
(printed67–68, world discussion and unchanged SC036 definition),233–235
(printed231–233, lexical argument/projection/table),292 and294
(printed290/292, both new bibliography identities),300 (printed298,
OE variant index); standalone lexical109 and reader68 were also inspected.
Accents, quantity marks, Czech diacritics, citations, wrapping, cross-references
and the world continuation table are legible. No layout-source change
was needed. The newly retained, untracked combined debug TeX was removed;
tracked generated lexical TeX and publication PDFs remain generated outputs.

| Scientific observation | Unchanged result |
| --- | --- |
| Selected population |389 accepted,381 matches,eight mismatches,zero ambiguity/rejection |
| Selected389 fingerprint |`53769ef582dd6d119bacc18f808612980a1f02dfed2f94a6e30645bb9de00a9e` |
| Migration-aware380 fingerprint |`43de8a47b7aaf17f860c9e3009617002ddb36e4d32a90ede1a99525858a417ce` |
| Lexical fingerprint |`c44d73698e2fa2717366e951a75bbb02d19aa677faf51fc86dfa25187556b6da` |
| Immutable380 archive |`fae656520e9ebf446854643907a1ba48a511877fc25b1fae39649d5b97e9a6cf` |

No new full hour-long suite pass is claimed: the previous full run belongs
to the original closeout, which remains byte-identical. This follow-up
validates the affected documentary/runtime surfaces and strict publication.

Changed SOURCE comprises this report, the world adjudication/claim ledger,
optional reassessment harness/receipt, world model/source ledger, world-only
SC036 prose, source intake/bibliography/navigation, three scoped index
decisions and regression tests. Canonical refresh/build owns the changed
reader/lexical/combined manuscripts and PDFs, lexical TeX/build log,
publication check reports, index projections and source/survey provenance.
No corpus, stage/context metadata, production/sandbox Foma, SC registry,
chronology, original experiment receipt or frozen baseline changes.
Pre-existing scratch `tmp_probe.foma` and the Node diagnostic report remain
untouched and excluded.

The14 final decisions are in the authoritative adjudication. The remaining
historical limits are the universal prosodic domain, o/u boundary, earliest
compact-junction history, exact analogy/stress-loss dates and complete
source-backed conservative cell. Parser coverage gaps are not substituted
for those scientific uncertainties. Stop after world; no soul or SC037
investigation is begun.
