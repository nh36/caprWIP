# Quantity-distinct English diphthong realization

## Historical discussion

The English histories of inherited diphthongs and their secondary equivalents
must be distinguished from both smoothing and paradigm leveling. Ringe and
Taylor identify a common tensing or lengthening of the syllabic nuclei,
followed by further developments of the offglides; they place that tensing
before breaking. This does not make all the eventual English spellings
the products of a single simultaneous change
[@RingeTaylor2014, pp. 170--175].

The fronted continuation of \emph{*au} gives long *ēa*, including in
*brēad* 'bread', *dēaw* 'dew' and *hēawan* 'hew'.
First-element fronting is distinct from subsequent offglide unrounding
and lowering. The latter was not universal: some Northumbrian varieties
retained a rounded offglide. Thus this outcome is not exclusively West
Saxon, but neither is it an exceptionless description of every English
dialect [@RingeTaylor2014, pp. 172--173; @Campbell1959, pp. 53--54, 116--118].

The long *ēo* outcomes in *ċēowan* 'chew' and *fēower* 'four' belong to
the \emph{*eu} history. Earlier inherited or assimilation-created
geminate-glide reanalysis supplies the diphthong while retaining the
following consonantal glide. Dew and hew similarly acquire \emph{*au}
through [SC031 OEWWSimplification](#rule-OEWWSimplification), then reach
the fronted-au path. Their early reanalysis is not the later English
realization [@RingeTaylor2014, pp. 41--42, 65--66, 172--174].

The \emph{*iu} history is different again. Early *īo* is not simply
another spelling for the initial \emph{*eu} development. Subsequent
io/eo convergence has dialect-specific histories: Northumbrian retains
io, whereas West Saxon and parts of Mercian show convergence.
The long *ēo* of *frēond* 'friend' and *ēow* 'you' is the selected
endpoint here, not evidence that the merger preceded every intervening
English change. Friend's contraction-created input and you's earlier
glide reanalysis are also distinct origins
[@RingeTaylor2014, pp. 41--42, 174--175; @Campbell1959, pp. 124--126].

## SC032. Quantity-distinct diphthong realization (`OEDiphthongLeveling`) {#rule-OEDiphthongLeveling}

```foma
define OEDiphthongLeveling Ctx([
    {*aeu} -> {*ēa},
    {*áeu} -> {*ēa},
    {*eu} -> {*ēo},
    {*éu} -> {*ēo},
    {*iu} -> {*ēo},
    {*íu} -> {*ēo},
    # Split symbols from palatal glide (stress preserved where present):
    {*e} {*u} -> {*eo},
    {*é} {*u} -> {*éo},
    {*i} {*u} -> {*eo}
]);
```

The retained definition is a compound realization proxy. Its atomic
\emph{*aeu}, \emph{*eu} and \emph{*iu} symbols belong to the heavy,
long-output tier; an acute mark does not itself indicate length.
Atomic \emph{*aeu} records a fronted-au intermediate, not a claim
that a three-vowel phonetic sequence is demonstrated. The direct
\emph{*iu} to *ēo* mapping packages the selected later endpoint.
The split-symbol e+u, é+u and i+u clauses instead produce short
*eo*, retaining stress only in the é+u clause. Campbell distinguishes
short breaking and back-umlaut diphthongs from their long equivalents,
but his account does not specify these computational token boundaries
[@Campbell1959, pp. 116--118].

All 32 current applications use atomic long-tier inputs. The unaccented
atomic alternatives and all three split-symbol clauses remain formal
compatibility paths without a selected-word application. Their
retention does not establish an independent palatal-glide origin,
and no additional stressed-i clause is inferred.

The short dative *cneowe* 'knee' remains outside this long-output operation;
its pre-w breaking is supplied by [SC044 OEBreaking](#rule-OEBreaking).
The separately palatalized-glide history of *hīew* 'hue' reaches
long *īo* through [SC110 OEJGlideIO](#rule-OEJGlideIO) before the
ordinary iu matcher. It then receives long *īe* through mutation,
not ordinary *ēo* here. These contrasts preserve quantity and
conditioning within the adopted selected cells
[@Campbell1959, pp. 232--233; @RingeTaylor2014, pp. 187--188, 250, 387].

Fronting must supply its product before its offglide continuation:
[SC030 OEAuBrightening](#rule-OEAuBrightening) feeds this component,
not every clause in the definition. Ringe and Taylor explicitly
distinguish the two developments
[@RingeTaylor2014, p. 172].
Earlier displacement tests that left \emph{*aeu} unrealized produced
\emph{+?}, a computational rejection with no attested linguistic status.
They therefore cannot independently establish
the historical interval.

The input of *hēafod* 'head' must be realized into a recognized vowel
before [SC040 OEMedUnstressedULowering](#rule-OEMedUnstressedULowering)
can lower its remaining medial vowel in the model. That internal
recognition requirement is not proof that historical offglide change
conditioned the lowering. Campbell records both *hēafud* and *hēafod*,
with varying preservation of protected unstressed u
[@Campbell1959, pp. 155--156]. No historical order for the entire
nine-clause bundle follows from that one computational dependency.
