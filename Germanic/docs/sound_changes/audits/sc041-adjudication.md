# SC041: final short low-vowel loss and the late oral-a proxy

## Identity

- SC041; executable identifier `PWGmcFinalBareALoss` (not a dating argument).
- 11 November 2026; `research/sc041-final-bare-a-loss`; base and explicit scientific reference `77b295cb00a241984ab4266c4d5a20baaaf54cec`.

## Question

The hypothesis, pinned before the new execution, was that every present application deletes in-domain unstressed final short oral a, but the operation is narrower than historical West Germanic low-vowel apocope. Final-z loss should feed the operation without proving adjacency; removing the vowel should bleed, not feed, a-restoration.

An application outside that phonological domain, a required negative control undergoing loss, an unexplained nonfiring short oral a, or absence of the predicted local restoration contrast would refute the corresponding claim. Historical stage and scope require literature and comparative evidence independently of successful outputs.

## Current state (before any edits)

The registry had `hist_stage=pwgmc`, `hist_scope=pan_wgmc`, confidence B and unadjudicated status. These axes are independent. The numbered cascade position was 47; the complete composition index, including its input adapter, was 48. Neither is historical dating.

The unchanged rule is:

```foma
define PWGmcFinalBareALoss Ctx([
    {*a} -> 0 || _ .#.
]);
```

It targets unmarked short oral `*a`, not nasal `*ą`, long `*ā`, accented `*á`, or a vowel before a surviving consonant. Its actual firing domain must nevertheless be checked, rather than equating an unmarked symbol with independently established historical stress in every hypothetical input.

The selected corpus has394 accepted derivations,386 matches and eight inherited mismatches. Selected PROTOFORMs, not necessarily citation PROTOs or one common case, enter the transducer. Final-z loss, vowel quantity/quality operations, selected endings and the retained annotations already encode parts of their histories.

Consulted authorities: the SC041 preparation packet, original chronology card and its original changes/failures tables, grouped039–041 dossier, accepted SC020 split and SC043 adjudication, current SC046 discussion, SC047 representation and the adopted SC064 account. SC039 remains deferred; SC040 and the HVD/syncope decisions are not reopened.

## Diagnosis

### Complete firing census and controls

Canonical `SC041 --evidence` completed successfully in505.14 seconds, after healthy-container and exact host/container source checks. FST SHA256 is `37b7811ca68c0358d26e25d58fe5d697e7d560a61a1896190c5c72f93583af0e`; corpus SHA256 is `c1ebc87c2c535fe24628bf34b8b7b25e73602b1cad59072fcd9d5a289543edf9`. The full population remains394/386/eight.

There are70 live firings. In every one, the immediately preceding form ends in short oral `*a` and the result is exactly that form minus its last `*a`; all selected inputs end in `az`. All70 local deletions are in-domain. This is not a claim that all70 complete selected histories have thereby been independently established.

The complete population is: beard, bosom, bottom, buck, calf, comb, craft, crop, dale, day, dough, dream, eel, fern, finger, fish, fowl, fox, fright, gang, ghost, hammer, harm, hawk, hazel, hearth, hedge, helm, home, hood, hoof, hound, knight, leek, loath, lock, malt, mast, mood, nail, one, oven, raven, reek, coat, rudder, rust, seam, shilling, snow, staff, stock, stone, stool, stork, storm, stream, summer, team, thane, thanks, thief, thorn, thunder, wain, wasp, way, whale, wolf and dart.

The full selected input, exact immediately-before/after starred forms, final output and target of every firing are preserved in [the frozen evidence](sc041-experiments/evidence.json), `canonical.firings`; the archive also contains the complete fresh394-entry trace. No additional application is hidden by the representative list.

Of these,69 belong to the original380 identity lineage under their current approved selections; dart is a later admission. This is an identity-lineage partition, not a fresh execution of the literal original380 inputs. The immutable original380 snapshot is unchanged and was not replayed. The original boundary experiment changed67 outputs:64 newly failed and buck, fowl and wolf remained failing. The difference between its67 changed outputs and today's70 is hammer's approved `*xámaras`→`*xámaraz` cell change, rust's approved `*rústō`→`*rústaz` input change, and dart's admission. Rust remains an inherited mismatch, so the current earlier displacement newly fails66, not70. The original card's64 is a failure count, not the complete historical firing census.

Nonfiring selected controls include bake `*bákaną`, horn `*xúrną`, rest `*rástōz`, who `*xwáz`, ban `*bánnas`, earth `*érθōn` and earthly `*érθa-kùnðǭ`. Their immediately preceding forms respectively retain final nasal a, nasal a, long ō, long ā, consonant-protected a, long nasal ǭ and long nasal ǭ; none undergoes SC041. Stone uses nominative `*stáinaz`, not the literature's accusative comparison. Fright's inherited oblique `*fúrxtīnaz` demonstrates that the70 are not one nominative declension class.

### Principal traces and witness roles

Stars below delimit the actual Foma segment symbols, not reconstructed syllable boundaries.

| Witness; selected input | Immediately before SC041 | Immediately after | Live final | SC041 before z-loss |
|---|---|---|---|---|
| beard; `*bárdaz` | `*b*á*r*d*a` | `*b*á*r*d` | beard | bearda |
| comb; `*kámbaz` | `*k*á*m*b*a` | `*k*á*m*b` | camb | camba |
| bosom; `*bōsmaz` | `*b*ō*s*m*a` | `*b*ō*s*m` | bōsm | bōsma |
| bottom; `*búttmaz` | `*b*ó*t*t*m*a` | `*b*ó*t*t*m` | botm | botma |
| calf; `*kálbaz` | `*k*á*l*b*a` | `*k*á*l*b` | ċealf | ċealfa |
| coat; `*rúkkaz` | `*r*ó*k*k*a` | `*r*ó*k*k` | rocc | rocca |
| craft; `*kráftaz` | `*k*r*á*f*t*a` | `*k*r*á*f*t` | cræft | crafta |
| day; `*dágaz` | `*d*á*g*a` | `*d*á*g` | dæġ | daga |
| fright; `*fúrxtīnaz` | `*f*ú*r*x*t*ī*n*a` | `*f*ú*r*x*t*ī*n` | fyrhte | fyrhtena |
| hedge; `*xágjaz` | `*x*á*g*g*j*a` | `*x*á*g*g*j` | heġġ | heġġa |

All70 are live applications. Beard/comb/bosom/bottom/calf/coat exemplify SC020 feeding SC041: before SC020 the vowel is still followed by z, so moved loss does nothing; SC020 then exposes a vowel too late for that moved operation. Downstream breaking, restoration, epenthesis and spelling cannot generally repair the residual ending. There is no adjacency inference.

Craft/dale/day/hazel/mast/staff/whale are restoration-bleeding witnesses. With loss immediately before restoration, day has `*d*æ*g*a`→`*d*æ*g`; restoration then leaves it unchanged and the final is dæġ. With loss immediately after restoration, restoration first gives `*d*a*g*a`, then loss gives `*d*a*g`, finally dag. Craft similarly contrasts cræft/craft. The complete seven-row paired difference is in `local_restoration_difference`.

Fright is a technical feeding witness for SC064, not an independent historical date. Live loss exposes `*f*ú*r*x*t*ī*n`, allowing final-n loss. In both late variants, SC064 instead receives `*f*ú*r*x*t*ī*n*a` and does nothing; later SC041 cannot recover that missed application, and the final is fyrhten. This shared residual must not be attributed to restoration.

The protected negative controls are nonapplications, not concealed failures; the nasal-final controls also demonstrate the proxy's limitation relative to the broader historical phenomenon. There is no out-of-domain firing. Hedge's full ja-stem history is a separate acknowledged limitation below.

### Current counterfactuals

All three variants use the original journaled immutable source snapshot, a separately hashed recipe/probe/driver supplement, all394 canonically context-encoded inputs and the existing isolated compiler. They run sequentially inside the backend with the runtime lock held. One verified common-definition image supplies the fresh full-source identity control and is reused with its integrity and environment checks intact. No production source or bins are altered.

| Variant | Changed finals | Newly failing | Matches |
|---|---:|---:|---:|
| Fresh isolated identity control | 0 | 0 | 386 |
| SC041 immediately before current SC020 | 70 | 66 | 320 |
| SC041 immediately before SC046 | 1, fright | 1 | 385 |
| SC041 immediately after SC046 | 8 | 8 | 378 |

Every variant singly accepts all394: zero missing or multiple outputs. The paired before/after-SC046 contrast isolates the seven restoration witnesses despite the common fright residual. A new complete first-break sweep was neither required nor performed; the old safe window21–45 is not asserted for today's cascade.

Ten component predictions pass: short oral a after the day and craft shapes is deleted; nasal a, long a, stressed a, a protected by s, final i and final u remain; restoration changes `*d*æ*g*a` to `*d*a*g*a` but leaves `*d*æ*g` unchanged. The last two controls establish the mechanism of bleeding without a morphological filter.

The receipted counterfactual command took517.69 seconds. [The manifest](sc041-experiments/manifest.json) authenticates every member of [the compressed immutable record](sc041-experiments/experiments.zip), including snapshots, exact recipes, driver, all394 outputs/intermediates, ten component results, original command receipts and full execution logs. Original failed recipe-schema preparation attempts occurred before snapshot creation or any Foma experiment; no failed scientific experiment was relabelled as successful.

## Literature

| Original consulted; printed pages | Supported claim and limitation |
|---|---|
| Campbell1959,137–138 §331, especially138 §331.4/n.4;143 §341 | Earlier absolutely-final Indo-European vowel loss is distinct from later protected-a loss. The nominative/accusative examples, old Norse runic retention and genitive-as question are preserved. Section341's retrospective mention is not an OE date for apocope or an equation with medial syncope. |
| RingeTaylor2014,44–47 §3.1.2 | Broad WG unstressed oral/nasal short-low-vowel loss; dialect-community qualification; economy of z-first ordering rather than logical necessity; comparative-s/r controls; possible Matronae exceptions; glide vocalization and loss before Cj gemination. Printed45n4 warns against secure absolute dating from insecure Latinized/runic interpretations. |
| RingeTaylor2014,189–190 §6.3.1 | English retraction needs the surviving back-vowel trigger after the relevant consonantal material; this independently explains why removing a blocks restoration. |
| Fulk2018,25n1;91 §5.6;92 | Frienstedt kaba, interpreted kamba, c250–300, is local evidence for z-loss with a retained, not universal completion by that date. Final short oral/nasal a loss is independent of preceding weight and distinct from subsequent high-vowel reductions. |

The principal pages were checked in held originals, including Campbell137–138/143, Ringe–Taylor44–47 and Fulk25/91–92 as page images; Ringe–Taylor189–190 was read from the original PDF's native text. The archive's source-review record preserves holding hashes and the exact consultation limits, not copyrighted page reproductions.

The old Ringe–Taylor60–61 citation confused PDF-sheet numbers with printed pagination: sheets60–61 contain printed45–46. Actual printed60–61 was separately checked and is not the cited final-short-vowel account. Correct the current exposition, not the frozen experiment records.

Schmidt/Nedoma/Düwel2011, Stiles1995 and Page2001 were not independently freshly consulted. Fulk's and Ringe–Taylor's reports are identified as secondary evidence, not invented primary verification. The existing hedge survey distinguishes Orel2003 p150's masculine citation from Kroonen2013 p198's feminine hedge formation; that previously recorded distinction is reused, not a new original-dictionary verification.

## Historical analysis

- Historical stage: retain Proto-West Germanic for the ancestral short-low-vowel loss, with Ringe–Taylor's qualification that the community may already have differentiated. The identifier's prefix and the late serialized position supply no evidence.
- Historical scope: retain pan-West-Germanic as the comparative shared development. It does not assert an instantaneous change throughout all dialects at the date of the Frienstedt object. Confidence B is retained independently of the stage/scope labels.
- Conditioning: unstressed short low vowels in the relevant final phonological environment, independent of preceding syllable weight. Oral/nasal distinctions and consonantal protection must be represented explicitly. No declension, lexeme list, grammatical filter or lexical diffusion is introduced.
- Counterexamples: surviving-as and-r environments test the economical ordering, while the possible Matronae cases remain qualified rather than dismissed by a grammatical exception. Nasal-a controls are not counterexamples to historical nasal-a loss; they show that SC041 alone is not its full implementation.
- Analogy: none is needed for the70 local deletion events. Ringe–Taylor positively discusses ja-stem leveling generally, but this is not positive, word-specific evidence that licenses an analogical repair of hedge here. The selected hedge history is not silently declared settled.
- Proxy: the operation faithfully deletes exposed short oral a in the current population. Broad historical loss also includes nasal endings, glide vocalization and an earlier relation to gemination which this late fragment does not independently reconstruct. Retention of the fragment is not adoption of its serialized neighbors as historical chronology.

Chronology:

1. SC020 before SC041: retain `independently_demonstrated`, with role **feeding**, but distinguish the current broad executable boundary from the independent historical argument. Ringe–Taylor46 favors z-first by comparative economy; Fulk25n1 supplies a local retained-a/z-less witness on the stated interpretation. Neither proves adjacency or an exact pan-WG date.
2. SC041 before SC046: retain `independently_demonstrated`, role **bleeding**, on the paired seven-row counterfactual and the independently source-supported restoration trigger. Historical PWGmc-before-English ordering is also stage-entailed; that is corroboration, not another lexical experiment.
3. SC041 before SC064: retain **technical feeding** only. The fright encoding exposes n; the source-grounded early final-n account is not independently dated by this dependency. The accepted SC064 order is unchanged.
4. Broad historical low-vowel apocope before WG Cj gemination: independently argued by Ringe–Taylor47. Do not insert a false current executable-order edge pretending that the late oral-a fragment is the entire historical change. The discrepancy is explicit, especially in hedge.

## Verdict

**REFORMULATE historical/executable exposition and chronology roles / RETAIN the rule, its current implementation order, historical stage, scope and confidence.**

Registry-verdict: SC041=REFORMULATE/RETAIN

The sources support early West Germanic low-vowel loss, whereas the complete census supports this operation only as its short-oral-a fragment. All observed local applications and required negative controls behave regularly without lexical or grammatical repairs. The experiments distinguish broad z-loss feeding, genuine restoration bleeding and the separate n-visibility dependency. No executable revision or baseline migration is scientifically warranted by these results; a claim to have resolved every whole-word history would go beyond them.

## Propagation (only after verdict)

Authoritative targets: SC041 registry row, three relevant edge interpretations, human inventory note, this memorandum, SC041 reader, grouped dossier, dated card addendum, current-phase routing, focused tests and a bounded qualification of hedge's existing model/ledger. Earlier literature and the original chronology measurements remain.

Regression controls protect the complete current local domain, actual positive/negative trace witnesses, the ten assayed component predictions, authenticated immutable experiment inputs/logs, and the paired restoration contrast separating fright. They do not turn an archival assay into a claim of fresh execution in portable CI.

FST bytes, order, selected corpus/cells/classes, contexts and both protected fingerprints are unchanged. Expected expanded fingerprint remains `43a57847b70b39ec130b4b52a17065be8cedd0e5fe7c6cc801ae1bcecae9fe2c`; active legacy fingerprint remains `a004ea461f76e5ca0c00d4ab407648247222a5123ccad31e2c6a89fe0223ed47`. No baseline is refrozen. Generated reader/book/registry views are owned solely by the artifact graph; exact-state publication and strict-validation receipts remain completion gates, not conclusions asserted by this memorandum.

### Publication completion and propagation reconciliation

Publication checks exposed an obsolete index-report assumption that all four failure comparisons shared one paragraph. The report now checks the actual extracted triples, with positive and negative regression controls; scholarly prose was not rewritten to accommodate the checker. Exact rule-name links were also completed in the reader.

That subsequent reader formatting correctly invalidated the initial completed propagation's target hashes. The original journal is preserved intact, including its invalidation and authentic receipts. A separate completion journal explicitly adopts the final reader bytes and authorizes this memorandum's completion note before editing, with fresh canonical finalization. It reuses the authenticated experiments only for their unchanged executable model, corpus and contexts, retains the original scientific reference, and requires new exact-state A/B/C certification. No prior receipt is relabelled as execution against the final committed state.

## Residue

The exact absolute date, dialectal synchrony and primary runological assessment remain limited as described. The full representation of nasal endings and stranded glides is not resolved by the oral-a fragment.

Hedge is a concrete limit, not a hidden successful control for historical chronology: its current pre-SC041 form already contains geminated gg, while Ringe–Taylor47 puts broad apocope before gemination and distinguishes later leveling. Orel's and Kroonen's differing formations do not establish which complete selected cell supplies an uninterrupted regular history. Its selected data and derivation class remain protected; the lexical prose now labels the serialized path as computational and explicitly leaves the historical-cell reconciliation open. Neither a lexical exception nor unsupported analogy is introduced. This bounded residue does not falsify deletion of its actually exposed short final a.

No adjudication of gemination, SC039/040, SC042, SC047, the parked Barrack/index/control programmes or a new corpus admission is begun. The next sequential selection is obtained from the registry only after SC041 completion.
