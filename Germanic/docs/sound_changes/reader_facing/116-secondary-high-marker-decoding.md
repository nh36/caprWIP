# Secondary high-vowel annotation decoding

This independently traced support operation decodes retained subordinate
high-vowel marks only after their phonological consumers have finished.
It is a computational identity, not an additional historical sound change.

## SC116. Technical secondary high-marker decoding (`OEHighStressDecode`) {#rule-OEHighStressDecode}

```foma
define OEHighStressDecode Ctx([{*ì} -> {*i}, {*ù} -> {*u}, {*ỳ} -> {*y}]);
```

The decoder follows [SC066 OELAdjacentSyncope](#rule-OELAdjacentSyncope)
and precedes later weak-vowel lowering. Marked subordinate vowels are
protected from [SC065 OEMedialSyncope](#rule-OEMedialSyncope), early
weak-vowel unrounding at [SC115 OEHighLinkSyncope](#rule-OEHighLinkSyncope),
and the light-syllable deletion component before these marks are removed.
No historical date for obligatory loss of subordinate stress follows
from this serialization.
