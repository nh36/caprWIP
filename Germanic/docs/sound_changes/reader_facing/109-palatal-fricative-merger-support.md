# Technical support: postmutation fricative merger

## SC109. Postmutation merger serialization (`OEPalatalFricativeMerger`) {#rule-OEPalatalFricativeMerger}

```foma
define OEPalatalFricativeMerger [
    {*ʝ} -> {*j}
];
```

The historical commitment is merger after mutation
[@RingeTaylor2014, p. 204]. Its execution after
[SC089 OELateUnstressedAgSuffix](#rule-OELateUnstressedAgSuffix)
is a computational holding zone, not proof of an exact historical date.
It keeps the fricative out of inherited-j normalization while preserving
late palatal raising, syllable weight, reduction and native rendering.
[SC057 OEJClusterCoalescence](#rule-OEJClusterCoalescence) remains a
different cluster process. Stop affrication dates and the precise
disputed eligibility domain are not settled by this merger.
