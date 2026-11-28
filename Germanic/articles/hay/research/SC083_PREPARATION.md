# SC083 — read-only preparation for ordinary adjudication

## Identity and question

Ran `python3 Germanic/tools/adjudicate.py SC083 --prepare` on the clean
SC047 candidate `113101ac5f169b589e1a9647cdf24d32cdd4d919`. This is the
intended baseline, not the current `update` or an adoption decision. The
ordinary saved programme currently returns SC050 next; the explicit SC083
preparation bypasses no gate and changes no policy. Obtain authority for
this scoped case after integration; do not silently advance or reset the
canonical programme.

Does the existing weak-vowel proxy delete a stressed root head when the
accent has been decoded, and can the existing one-pretonic foot marker
protect that head without changing true weak-domain reductions?

## Incumbent and exact candidate

The registry lists SC083 as active, English-specific Old English,
confidence A, unadjudicated, with no existing adjudication memorandum.
The controller locates `OEUnstressedEIContraction` at FST line 3222,
manifest position 98. The before-reference fingerprints are
`51953ed3a411b10bfa551de996053bc805ba87525180c4bf13f9b1ba46d4ee0e`
(expanded-396) and `1b53e382bb320caf05c795218fe626bf7d0fd8f4e19da3af7f4ef6190d7892ee`
(legacy-380); they are observations, not optimization targets.

```foma
define OEUnstressedEIContraction [
    {*e} -> 0 || EnglishStarVocalic [EnglishStarConsonant | EnglishPalatalConsonant]+ _ {*i}
];
```

Candidate from [A1](component-proposals/SC083.md), at the same cascade position:

```foma
define OEUnstressedEIContraction FootCtx([
    {*e} -> 0 || EnglishStarVocalic [EnglishStarConsonant | EnglishPalatalConsonant]+ _ {*i}
]);
```

The existing `FootCtx` excludes one annotated pretonic syllable from the
rule's domain. It neither supplies stress nor assumes that all prefixes
are unstressed. SC085 is later and no marker transfer is required.

## Diagnosis, literature and historical scope

Ringe & Taylor 32, 35, 228 describes weak shortening, unrounding and
raising before a palatal and narrower further loss; Campbell §§754–755
supplies weak paradigm controls. The FST's literal *e* deletion following
SC082 is a model proxy, not the whole attested historical development.
Campbell §74 n. 5 distinguishes lexical prefix/root stress, and
Ringe & Taylor 260, 318, Campbell §237.1b and Sweet p. 416 motivate the
separate prefixed ‘call’ root/participle comparison. Sweet Ps 71:9
attests finite *liciað*; the projected infinitive is not that token.
No new geographical claim or analogy follows from this correction.

- **Live weak positives:** ‘bore’ 1956, ‘handle’ 2055, ‘learn’ 2095,
  ‘lick’ 2099, ‘make’ 2117, ‘show’ 2186, ‘spare’ 2205 and ‘sunder’ 2232
  fired in both archived and active captures in canonical, A and B2.
  Their anchors, paths and endpoints survived the private guard. Keep
  the independently projected weak ‘love’ comparison as a stage control;
  its whole-word *lofian* discrepancy is upstream.
- **Out-of-domain firing:** A/B2 prefixed ‘call’ present and participle
  retain `*ᶠ` after the acute is consumed. The incumbent changes
  `*ᶠ*ʝ*e*k*e*i*θ` to `*ᶠ*ʝ*e*k*i*θ` (parallel final `*d`);
  the guard leaves the head intact at SC083. The resulting developmental
  *ġeceiþ/ġeceid* are not asserted historical endpoints or corpus targets.
  Canonical/plain simplex has an upstream non-target nucleus.
- **Negatives and limits:** ‘world’ and ‘believe’ remain unchanged.
  A marked secondary vowel does not match; once decoded to plain *e*,
  the proxy cannot distinguish it. A decoded head after two pretonic
  syllables is likewise unprotected. These latter cases are synthetic
  limits of the serialization, not evidence for a new sound law.
  See the [panel](component-proposals/sc083-panel.tsv) and
  [pinned receipt](component-proposals/sc083-traces.json.gz).

The controller reports the existing reciprocal SC082/SC083 displacement
records, labelled `independently_demonstrated` in the canonical registry.
They show executable feeding in admitted weak forms; their representation
does not independently establish a historical syllabic *i* stage.
The SC087 record is a no-break search boundary, not a requirement that
SC083 precede SC087. Preserve these records; add no chronology edge on
the strength of the guard exercise.

## Pending verdict, verification and propagation

Working question: **restrict the proxy while retaining the historical
scope and order**. This is a preparatory recommendation, not a canonical
verdict. After package 0 and owner authorization:

1. Prepare again if the intended commit changes. Use the ordinary
   `adjudicate.py SC083 --evidence` controller for a live before/after
   census; verify the compatibility diagnostic and both active A/B2
   orders, not just the compatibility count. Verify the genuine weak
   positives, protected marked first head and unaffected compound/plain
   controls; inspect selected outputs, cardinality and stage deltas.
   Preserve the old captures; stop on unexpected differences. Carry the
   minimum distinguishable controls into the owning regression lane
   and document any added execution cost.
2. Record the ordinary verdict in
   `Germanic/docs/sound_changes/audits/sc083-adjudication.md` and
   propagate through canonical authorities only after the decision.
   The reader source `083-unstressed-ei-contraction.md` needs the
   accepted definition, historical operation versus executable proxy,
   page-cited weak/stressed contrast, and bounded interpretation of
   SC082 displacement and the later search. Audit the owning book
   dossier `079-087-final-j-contraction-and-metathesis-cluster.book-dossier.md`
   and chronology-card consistency; preserve original experimental records.
3. Check owning lexical publications for ‘bore’, ‘lick’ and the other
   live positives if their exposed derivation or explanation changes.
   Correct any discussion relying on the erroneous prefixed
   ‘call’ reduction, but do not publish developmental endpoints as
   accepted forms. No target migration or specific lexical chapter
   rewrite is indicated by the unchanged selected paths; if new or
   substantively revised vocabulary is approved, require its own
   source-ledger and mature lexical chapter.
4. Finalize through the ordinary controller/artifact graph, run the
   authorized focused and final strict serial/exclusive validation,
   rebuild and inspect the affected book and both active projections,
   and record the exact resulting source/certificate. Do not edit
   generated material. This packet did not run `--evidence`, change
   SOURCE, or repeat the exploratory investigation.
