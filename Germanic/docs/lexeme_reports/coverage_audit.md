# Old English lexeme-report coverage audit

- Total OE rows with real counterpart: 380
- Manifest entries loaded: 12
- Rows requiring lexeme report: 148
- Required rows with manifest-backed reports: 11
- Required rows with only fuzzy-matched reports: 0
- Required rows with no report: 137
- Regular rows with empty NOTE and no report required: 231
- Regular rows with empty NOTE but manual report present: 1
- Rows with STATUS=format_test reports: 1
- Regular rows with NOTE (report required): 71
- Non-regular rows with empty NOTE (report required because of DERIVATION_CLASS): 11

## Counts by DERIVATION_CLASS

| DERIVATION_CLASS | Total rows | Required | Manifest-backed | Fuzzy-only | No report |
| :--- | :--- | :--- | :--- | :--- | :--- |
| attested_variant | 4 | 4 | 1 | 0 | 3 |
| early_analogy | 35 | 35 | 2 | 0 | 33 |
| known_unmodelled | 2 | 2 | 2 | 0 | 0 |
| late_analogy | 28 | 28 | 4 | 0 | 24 |
| reconstructed_oe | 3 | 3 | 1 | 0 | 2 |
| regular | 303 | 71 | 0 | 0 | 71 |
| unexplained_unmodelled | 5 | 5 | 1 | 0 | 4 |

## Required rows with manifest-backed reports

| ID | Concept | Counterpart | DERIVATION_CLASS | NOTE? | Coverage source | Report status | Report path(s) | Requirement basis |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1936 | ban | bannes | late_analogy | yes | manifest | pilot | pilot/ban.md | NOTE, DERIVATION_CLASS=late_analogy, production_report |
| 1946 | berry | berġes | late_analogy | yes | manifest | pilot | pilot/berry.md | NOTE, DERIVATION_CLASS=late_analogy, production_report |
| 1959 | bottom | botm | early_analogy | yes | manifest | pilot | pilot/bottom.md | NOTE, DERIVATION_CLASS=early_analogy, production_report |
| 1973 | buck | bucc | unexplained_unmodelled | yes | manifest | pilot | pilot/buck.md | NOTE, DERIVATION_CLASS=unexplained_unmodelled, production_report |
| 1981 | craft | cræft | early_analogy | yes | manifest | pilot | pilot/craft.md | NOTE, DERIVATION_CLASS=early_analogy, production_report |
| 1983 | cud | cwedu | attested_variant | yes | manifest | pilot | pilot/cud.md | NOTE, DERIVATION_CLASS=attested_variant, production_report |
| 2013 | fire | fȳre | known_unmodelled | yes | manifest | pilot | pilot/fire.md | NOTE, DERIVATION_CLASS=known_unmodelled, production_report |
| 2151 | reek | rēac | reconstructed_oe | yes | manifest | pilot | pilot/reek.md | NOTE, DERIVATION_CLASS=reconstructed_oe, production_report |
| 2203 | span | spanne | late_analogy | yes | manifest | pilot | pilot/span.md | NOTE, DERIVATION_CLASS=late_analogy, production_report |
| 2240 | tap | tæppa | known_unmodelled | yes | manifest | pilot | pilot/tap.md | NOTE, DERIVATION_CLASS=known_unmodelled, production_report |
| 2250 | thistle | þistles | late_analogy | yes | manifest | pilot | pilot/thistle.md | NOTE, DERIVATION_CLASS=late_analogy, production_report |

## Required rows with only fuzzy-matched reports

_None_

## Required rows with no report

| ID | Concept | Counterpart | DERIVATION_CLASS | NOTE? | Coverage source | Report status | Report path(s) | Requirement basis |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1934 | bake | bacan | regular | yes | - | - | - | NOTE |
| 1942 | beech | bōc | regular | yes | - | - | - | NOTE |
| 1943 | begin | beġinnan | regular | yes | - | - | - | NOTE |
| 1949 | bier | bǣr | regular | yes | - | - | - | NOTE |
| 1951 | birth | byrd | regular | yes | - | - | - | NOTE |
| 1954 | bone | bān | regular | yes | - | - | - | NOTE |
| 1958 | both | bū | regular | yes | - | - | - | NOTE |
| 1961 | bow | bīeġan | regular | yes | - | - | - | NOTE |
| 1962 | bow | bēag | late_analogy | yes | - | - | - | NOTE, DERIVATION_CLASS=late_analogy |
| 1965 | brand | brandes | early_analogy | no | - | - | - | DERIVATION_CLASS=early_analogy |
| 1968 | breast | brēost | early_analogy | no | - | - | - | DERIVATION_CLASS=early_analogy |
| 1969 | breeches | brēċ | regular | yes | - | - | - | NOTE |
| 1975 | calf | ċealf | regular | yes | - | - | - | NOTE |
| 1979 | corn | corn | regular | yes | - | - | - | NOTE |
| 1980 | cow | cȳ | late_analogy | yes | - | - | - | NOTE, DERIVATION_CLASS=late_analogy |
| 1987 | deed | dǣd | regular | yes | - | - | - | NOTE |
| 1990 | dill | dile | early_analogy | yes | - | - | - | NOTE, DERIVATION_CLASS=early_analogy |
| 1992 | door | dor | regular | yes | - | - | - | NOTE |
| 2003 | fare | faran | regular | yes | - | - | - | NOTE |
| 2004 | fast | festan | early_analogy | yes | - | - | - | NOTE, DERIVATION_CLASS=early_analogy |
| 2007 | fell | fell | regular | yes | - | - | - | NOTE |
| 2008 | fern | fearn | regular | yes | - | - | - | NOTE |
| 2009 | field | feld | regular | yes | - | - | - | NOTE |
| 2011 | find | fundene | late_analogy | yes | - | - | - | NOTE, DERIVATION_CLASS=late_analogy |
| 2016 | flask | flasce | early_analogy | no | - | - | - | DERIVATION_CLASS=early_analogy |
| 2022 | fly | flēogan | regular | yes | - | - | - | NOTE |
| 2027 | follow | fylġan | early_analogy | yes | - | - | - | NOTE, DERIVATION_CLASS=early_analogy |
| 2028 | forlorn | lēosan | regular | yes | - | - | - | NOTE |
| 2030 | fowl | fugol | unexplained_unmodelled | yes | - | - | - | NOTE, DERIVATION_CLASS=unexplained_unmodelled |
| 2034 | fright | fyrhte | late_analogy | yes | - | - | - | NOTE, DERIVATION_CLASS=late_analogy |
| 2037 | gall | ġealla | early_analogy | no | - | - | - | DERIVATION_CLASS=early_analogy |
| 2038 | gang | gang | regular | yes | - | - | - | NOTE |
| 2041 | give | ġiefan | regular | yes | - | - | - | NOTE |
| 2043 | gold | gold | regular | yes | - | - | - | NOTE |
| 2046 | grave | grafan | regular | yes | - | - | - | NOTE |
| 2049 | guest | ġiest | regular | yes | - | - | - | NOTE |
| 2051 | hair | hǣr | regular | yes | - | - | - | NOTE |
| 2053 | hammer | hameres | late_analogy | yes | - | - | - | NOTE, DERIVATION_CLASS=late_analogy |
| 2055 | handle | handlian | regular | yes | - | - | - | NOTE |
| 2057 | harvest | hierfest | regular | yes | - | - | - | NOTE |
| 2058 | have | hæfeþ | late_analogy | yes | - | - | - | NOTE, DERIVATION_CLASS=late_analogy |
| 2068 | heaven | heofon | late_analogy | yes | - | - | - | NOTE, DERIVATION_CLASS=late_analogy |
| 2069 | hedge | heġġ | regular | yes | - | - | - | NOTE |
| 2070 | helm | helm | regular | yes | - | - | - | NOTE |
| 2071 | help | helpan | regular | yes | - | - | - | NOTE |
| 2075 | hind | hind | regular | yes | - | - | - | NOTE |
| 2077 | hold | healdan | regular | yes | - | - | - | NOTE |
| 2082 | horn | horn | regular | yes | - | - | - | NOTE |
| 2086 | knight | cniht | early_analogy | yes | - | - | - | NOTE, DERIVATION_CLASS=early_analogy |
| 2087 | knob | cnobba | reconstructed_oe | yes | - | - | - | NOTE, DERIVATION_CLASS=reconstructed_oe |
| 2088 | lade | hladan | early_analogy | yes | - | - | - | NOTE, DERIVATION_CLASS=early_analogy |
| 2090 | lap | lappa | early_analogy | no | - | - | - | DERIVATION_CLASS=early_analogy |
| 2092 | laugh | hliehhan | early_analogy | yes | - | - | - | NOTE, DERIVATION_CLASS=early_analogy |
| 2093 | lead | lǣdan | regular | yes | - | - | - | NOTE |
| 2095 | learn | liornian | regular | yes | - | - | - | NOTE |
| 2100 | lid | hlid | regular | yes | - | - | - | NOTE |
| 2102 | light | līehtan | regular | yes | - | - | - | NOTE |
| 2104 | linden | lind | regular | yes | - | - | - | NOTE |
| 2107 | live | lifeþ | late_analogy | yes | - | - | - | NOTE, DERIVATION_CLASS=late_analogy |
| 2109 | loam | lām | early_analogy | no | - | - | - | DERIVATION_CLASS=early_analogy |
| 2114 | lung | lungen | early_analogy | yes | - | - | - | NOTE, DERIVATION_CLASS=early_analogy |
| 2119 | man | mannes | late_analogy | yes | - | - | - | NOTE, DERIVATION_CLASS=late_analogy |
| 2120 | march | mearc | regular | yes | - | - | - | NOTE |
| 2124 | meed | meorde | late_analogy | yes | - | - | - | NOTE, DERIVATION_CLASS=late_analogy |
| 2126 | milk | meoloc | regular | yes | - | - | - | NOTE |
| 2129 | mother | mōder | regular | yes | - | - | - | NOTE |
| 2133 | navel | nafola | early_analogy | yes | - | - | - | NOTE, DERIVATION_CLASS=early_analogy |
| 2134 | neck | hnecca | early_analogy | no | - | - | - | DERIVATION_CLASS=early_analogy |
| 2136 | needle | nǣdl | early_analogy | yes | - | - | - | NOTE, DERIVATION_CLASS=early_analogy |
| 2138 | net | nett | regular | yes | - | - | - | NOTE |
| 2140 | night | niht | late_analogy | yes | - | - | - | NOTE, DERIVATION_CLASS=late_analogy |
| 2141 | nightmare | mare | regular | yes | - | - | - | NOTE |
| 2143 | nose | nosu | early_analogy | no | - | - | - | DERIVATION_CLASS=early_analogy |
| 2152 | rest | ræste | late_analogy | yes | - | - | - | NOTE, DERIVATION_CLASS=late_analogy |
| 2155 | coat | rocc | regular | yes | - | - | - | NOTE |
| 2162 | rust | rust | unexplained_unmodelled | yes | - | - | - | NOTE, DERIVATION_CLASS=unexplained_unmodelled |
| 2168 | sap | sæp | early_analogy | yes | - | - | - | NOTE, DERIVATION_CLASS=early_analogy |
| 2169 | sea | sǣ | early_analogy | yes | - | - | - | NOTE, DERIVATION_CLASS=early_analogy |
| 2179 | sheep | sċēap | regular | yes | - | - | - | NOTE |
| 2181 | shilling | sċilling | regular | yes | - | - | - | NOTE |
| 2183 | shoulder | sċuldrum | late_analogy | yes | - | - | - | NOTE, DERIVATION_CLASS=late_analogy |
| 2184 | shove | sċēaf | late_analogy | yes | - | - | - | NOTE, DERIVATION_CLASS=late_analogy |
| 2186 | show | sċēawian | regular | yes | - | - | - | NOTE |
| 2189 | sieve | sife | early_analogy | no | - | - | - | DERIVATION_CLASS=early_analogy |
| 2196 | sleep | slǣpan | regular | yes | - | - | - | NOTE |
| 2198 | smear | smierwan | regular | yes | - | - | - | NOTE |
| 2202 | span | spannan | regular | yes | - | - | - | NOTE |
| 2204 | spar | spearra | regular | yes | - | - | - | NOTE |
| 2205 | spare | sparian | early_analogy | yes | - | - | - | NOTE, DERIVATION_CLASS=early_analogy |
| 2212 | staff | stæf | early_analogy | yes | - | - | - | NOTE, DERIVATION_CLASS=early_analogy |
| 2216 | stem | stefn | early_analogy | yes | - | - | - | NOTE, DERIVATION_CLASS=early_analogy |
| 2217 | still | stillan | regular | yes | - | - | - | NOTE |
| 2227 | strew | strīeġan | reconstructed_oe | yes | - | - | - | NOTE, DERIVATION_CLASS=reconstructed_oe |
| 2230 | summer | sumer | regular | yes | - | - | - | NOTE |
| 2232 | sunder | sundrian | regular | yes | - | - | - | NOTE |
| 2234 | swallow | swealwe | regular | yes | - | - | - | NOTE |
| 2235 | swan | swanes | early_analogy | no | - | - | - | DERIVATION_CLASS=early_analogy |
| 2238 | swine | swīn | regular | yes | - | - | - | NOTE |
| 2242 | ten | tēon | attested_variant | yes | - | - | - | NOTE, DERIVATION_CLASS=attested_variant |
| 2248 | think | þenċan | regular | yes | - | - | - | NOTE |
| 2251 | thorn | þorn | regular | yes | - | - | - | NOTE |
| 2252 | thousand | þūsend | early_analogy | yes | - | - | - | NOTE, DERIVATION_CLASS=early_analogy |
| 2254 | three | þrīe | attested_variant | yes | - | - | - | NOTE, DERIVATION_CLASS=attested_variant |
| 2257 | tide | tīd | regular | yes | - | - | - | NOTE |
| 2258 | timber | timber | early_analogy | yes | - | - | - | NOTE, DERIVATION_CLASS=early_analogy |
| 2260 | token | tācn | regular | yes | - | - | - | NOTE |
| 2263 | town | tūn | regular | yes | - | - | - | NOTE |
| 2266 | wade | wadan | regular | yes | - | - | - | NOTE |
| 2268 | wake | wacan | early_analogy | yes | - | - | - | NOTE, DERIVATION_CLASS=early_analogy |
| 2270 | warp | weorpan | regular | yes | - | - | - | NOTE |
| 2272 | wash | wascan | regular | yes | - | - | - | NOTE |
| 2273 | wasp | wæfs | attested_variant | yes | - | - | - | NOTE, DERIVATION_CLASS=attested_variant |
| 2274 | water | wæter | early_analogy | yes | - | - | - | NOTE, DERIVATION_CLASS=early_analogy |
| 2276 | wax | weaxan | regular | yes | - | - | - | NOTE |
| 2277 | way | weġ | regular | yes | - | - | - | NOTE |
| 2278 | weapon | wǣpn | regular | yes | - | - | - | NOTE |
| 2284 | whale | hwæl | early_analogy | yes | - | - | - | NOTE, DERIVATION_CLASS=early_analogy |
| 2286 | whine | hwīnan | early_analogy | no | - | - | - | DERIVATION_CLASS=early_analogy |
| 2293 | will | willa | regular | yes | - | - | - | NOTE |
| 2294 | wind | windan | regular | yes | - | - | - | NOTE |
| 2296 | withy | wīþiġ | early_analogy | yes | - | - | - | NOTE, DERIVATION_CLASS=early_analogy |
| 2297 | wold | weald | regular | yes | - | - | - | NOTE |
| 2298 | wolf | wulf | unexplained_unmodelled | yes | - | - | - | NOTE, DERIVATION_CLASS=unexplained_unmodelled |
| 2300 | wool | wull | unexplained_unmodelled | yes | - | - | - | NOTE, DERIVATION_CLASS=unexplained_unmodelled |
| 2302 | world | weorold | early_analogy | yes | - | - | - | NOTE, DERIVATION_CLASS=early_analogy |
| 2305 | yarn | ġearn | regular | yes | - | - | - | NOTE |
| 2308 | youth | ġeoguþ | early_analogy | yes | - | - | - | NOTE, DERIVATION_CLASS=early_analogy |
| 2309 | make (iptv.2sg) | maca | late_analogy | yes | - | - | - | NOTE, DERIVATION_CLASS=late_analogy |
| 2310 | make (3sg) | macaþ | late_analogy | yes | - | - | - | NOTE, DERIVATION_CLASS=late_analogy |
| 2311 | bore (iptv.2sg) | bora | late_analogy | yes | - | - | - | NOTE, DERIVATION_CLASS=late_analogy |
| 2312 | bore (3sg) | boraþ | late_analogy | yes | - | - | - | NOTE, DERIVATION_CLASS=late_analogy |
| 2313 | learn (iptv.2sg) | liorna | late_analogy | yes | - | - | - | NOTE, DERIVATION_CLASS=late_analogy |
| 2314 | learn (3sg) | liornaþ | late_analogy | yes | - | - | - | NOTE, DERIVATION_CLASS=late_analogy |
| 2315 | lick (iptv.2sg) | licca | late_analogy | yes | - | - | - | NOTE, DERIVATION_CLASS=late_analogy |
| 2316 | lick (3sg) | liccaþ | late_analogy | yes | - | - | - | NOTE, DERIVATION_CLASS=late_analogy |
| 2317 | show (iptv.2sg) | sċēawa | late_analogy | yes | - | - | - | NOTE, DERIVATION_CLASS=late_analogy |
| 2318 | show (3sg) | sċēawaþ | late_analogy | yes | - | - | - | NOTE, DERIVATION_CLASS=late_analogy |

## Regular rows with empty NOTE and no report required

| ID | Concept | Counterpart | DERIVATION_CLASS | NOTE? | Coverage source | Report status | Report path(s) | Requirement basis |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1937 | barrow | beorg | regular | no | - | - | - | none |
| 1938 | bast | bæst | regular | no | - | - | - | none |
| 1939 | bath | bæþ | regular | no | - | - | - | none |
| 1940 | beard | beard | regular | no | - | - | - | none |
| 1941 | beaver | befer | regular | no | - | - | - | none |
| 1944 | believe | ġelīefan | regular | no | - | - | - | none |
| 1945 | belly | bielġ | regular | no | - | - | - | none |
| 1950 | bind | bindan | regular | no | - | - | - | none |
| 1952 | blood | blōd | regular | no | - | - | - | none |
| 1953 | board | bord | regular | no | - | - | - | none |
| 1955 | book | bōc | regular | no | - | - | - | none |
| 1956 | bore | borian | regular | no | - | - | - | none |
| 1957 | bosom | bōsm | regular | no | - | - | - | none |
| 1960 | bough | bōg | regular | no | - | - | - | none |
| 1963 | bow | boga | regular | no | - | - | - | none |
| 1964 | bower | būr | regular | no | - | - | - | none |
| 1966 | bread | brēad | regular | no | - | - | - | none |
| 1967 | break | brecan | regular | no | - | - | - | none |
| 1970 | bride | brȳd | regular | no | - | - | - | none |
| 1971 | bring | bringan | regular | no | - | - | - | none |
| 1972 | brook | brūcan | regular | no | - | - | - | none |
| 1974 | burst | berstan | regular | no | - | - | - | none |
| 1976 | chew | ċēowan | regular | no | - | - | - | none |
| 1977 | climb | climban | regular | no | - | - | - | none |
| 1978 | comb | camb | regular | no | - | - | - | none |
| 1982 | crop | cropp | regular | no | - | - | - | none |
| 1984 | dale | dæl | regular | no | - | - | - | none |
| 1985 | day | dæġ | regular | no | - | - | - | none |
| 1986 | deal | dǣl | regular | no | - | - | - | none |
| 1988 | deer | dēor | regular | no | - | - | - | none |
| 1989 | dew | dēaw | regular | no | - | - | - | none |
| 1991 | do | dōn | regular | no | - | - | - | none |
| 1993 | dough | dāg | regular | no | - | - | - | none |
| 1995 | dream | drēam | regular | no | - | - | - | none |
| 1996 | drench | drenċ | regular | no | - | - | - | none |
| 1997 | drink | drincan | regular | no | - | - | - | none |
| 1998 | drive | drīfan | regular | no | - | - | - | none |
| 1999 | earth | eorþe | regular | no | - | - | - | none |
| 2000 | eat | etan | regular | no | - | - | - | none |
| 2001 | eel | ǣl | regular | no | - | - | - | none |
| 2002 | fall | feallan | regular | no | - | - | - | none |
| 2005 | father | fæder | regular | no | - | - | - | none |
| 2006 | fee | feoh | regular | no | - | - | - | none |
| 2010 | fight | feohtan | regular | no | - | - | - | none |
| 2012 | finger | finger | regular | no | - | - | - | none |
| 2014 | fish | fisċ | regular | no | - | - | - | none |
| 2015 | fist | fȳst | regular | no | - | - | - | none |
| 2017 | flax | fleax | regular | no | - | - | - | none |
| 2018 | flea | flēah | regular | no | - | - | - | none |
| 2019 | flee | flēon | regular | no | - | - | - | none |
| 2020 | flesh | flǣsċ | regular | no | - | - | - | none |
| 2021 | flood | flōd | regular | no | - | - | - | none |
| 2023 | foal | fola | regular | no | - | - | - | none |
| 2024 | fodder | fōdor | regular | no | - | - | - | none |
| 2025 | fold | fealdan | regular | no | - | - | - | none |
| 2026 | folk | folc | regular | no | - | - | - | none |
| 2029 | four | fēower | regular | no | - | - | - | none |
| 2031 | fox | fox | regular | no | - | - | - | none |
| 2032 | freeze | frēosan | regular | no | - | - | - | none |
| 2033 | friend | frēond | regular | no | - | - | - | none |
| 2035 | frost | forst | regular | no | - | - | - | none |
| 2036 | furrow | furh | regular | no | - | - | - | none |
| 2039 | ghost | gāst | regular | no | - | - | - | none |
| 2040 | gift | ġift | regular | no | - | - | - | none |
| 2042 | god | god | regular | no | - | - | - | none |
| 2044 | goose | gōs | regular | no | - | - | - | none |
| 2045 | grass | græs | regular | no | - | - | - | none |
| 2047 | gripe | grīpan | regular | no | - | - | - | none |
| 2048 | ground | grund | regular | no | - | - | - | none |
| 2050 | hail | hæġl | regular | no | - | - | - | none |
| 2052 | hall | heall | regular | no | - | - | - | none |
| 2054 | hand | hand | regular | no | - | - | - | none |
| 2056 | harm | hearm | regular | no | - | - | - | none |
| 2059 | haw | haga | regular | no | - | - | - | none |
| 2060 | hawk | hafoc | regular | no | - | - | - | none |
| 2061 | hay | hīeġ | regular | no | - | - | - | none |
| 2062 | hazel | hæsl | regular | no | - | - | - | none |
| 2063 | head | hēafod | regular | no | - | - | - | none |
| 2064 | heal | hǣlan | regular | no | - | - | - | none |
| 2065 | heart | heorte | regular | no | - | - | - | none |
| 2066 | hearth | heorþ | regular | no | - | - | - | none |
| 2067 | heath | hǣþ | regular | no | - | - | - | none |
| 2072 | help | help | regular | no | - | - | - | none |
| 2073 | herd | heord | regular | no | - | - | - | none |
| 2074 | hew | hēawan | regular | no | - | - | - | none |
| 2076 | hoard | hord | regular | no | - | - | - | none |
| 2078 | home | hām | regular | no | - | - | - | none |
| 2079 | honey | huniġ | regular | no | - | - | - | none |
| 2080 | hood | hōd | regular | no | - | - | - | none |
| 2081 | hoof | hōf | regular | no | - | - | - | none |
| 2083 | hound | hund | regular | no | - | - | - | none |
| 2084 | knead | cnedan | regular | no | - | - | - | none |
| 2085 | knee | cnēow | regular | no | - | - | - | none |
| 2089 | land | land | regular | no | - | - | - | none |
| 2091 | last | lǣstan | regular | no | - | - | - | none |
| 2094 | leaf | lēaf | regular | no | - | - | - | none |
| 2096 | leather | leþer | regular | no | - | - | - | none |
| 2097 | leek | lēac | regular | no | - | - | - | none |
| 2098 | let | lǣtan | regular | no | - | - | - | none |
| 2099 | lick | liccian | regular | no | - | - | - | none |
| 2101 | life | līf | regular | no | - | - | - | none |
| 2103 | lime | līm | regular | no | - | - | - | none |
| 2105 | line | līne | regular | no | - | - | - | none |
| 2106 | list | līste | regular | no | - | - | - | none |
| 2108 | liver | lifer | regular | no | - | - | - | none |
| 2110 | loath | lāþ | regular | no | - | - | - | none |
| 2111 | lock | loc | regular | no | - | - | - | none |
| 2112 | lock | locc | regular | no | - | - | - | none |
| 2113 | louse | lūs | regular | no | - | - | - | none |
| 2115 | lust | lust | regular | no | - | - | - | none |
| 2116 | lye | lēag | regular | no | - | - | - | none |
| 2117 | make | macian | regular | no | - | - | - | none |
| 2118 | malt | mealt | regular | no | - | - | - | none |
| 2121 | mast | mæst | regular | no | - | - | - | none |
| 2122 | meal | mǣl | regular | no | - | - | - | none |
| 2123 | mean | mǣnan | regular | no | - | - | - | none |
| 2125 | might | miht | regular | no | - | - | - | none |
| 2127 | month | mōnaþ | regular | no | - | - | - | none |
| 2128 | mood | mōd | regular | no | - | - | - | none |
| 2130 | nail | næġl | regular | no | - | - | - | none |
| 2131 | name | nama | regular | no | - | - | - | none |
| 2132 | nave | nafu | regular | no | - | - | - | none |
| 2135 | need | nīed | regular | no | - | - | - | none |
| 2137 | nest | nest | regular | no | - | - | - | none |
| 2139 | nettle | netle | regular | no | - | - | - | none |
| 2142 | nine | nigon | regular | no | - | - | - | none |
| 2144 | one | ān | regular | no | - | - | - | none |
| 2145 | oven | ofn | regular | no | - | - | - | none |
| 2146 | ox | oxa | regular | no | - | - | - | none |
| 2147 | rain | reġn | regular | no | - | - | - | none |
| 2148 | rainbow | reġnboga | regular | no | - | - | - | none |
| 2149 | raven | hræfn | regular | no | - | - | - | none |
| 2150 | read | rǣdan | regular | no | - | - | - | none |
| 2153 | ride | rīdan | regular | no | - | - | - | none |
| 2154 | rind | rind | regular | no | - | - | - | none |
| 2157 | rood | rōd | regular | no | - | - | - | none |
| 2158 | room | rūm | regular | no | - | - | - | none |
| 2159 | rope | rāp | regular | no | - | - | - | none |
| 2160 | rudder | rōþor | regular | no | - | - | - | none |
| 2161 | run | rinnan | regular | no | - | - | - | none |
| 2163 | rye | ryġe | regular | no | - | - | - | none |
| 2164 | sail | seġl | regular | no | - | - | - | none |
| 2165 | sake | sacu | regular | no | - | - | - | none |
| 2166 | salt | sealt | regular | no | - | - | - | none |
| 2167 | salve | sealf | regular | no | - | - | - | none |
| 2170 | seam | sēam | regular | no | - | - | - | none |
| 2171 | seek | sēċan | regular | no | - | - | - | none |
| 2172 | send | sendan | regular | no | - | - | - | none |
| 2173 | set | settan | regular | no | - | - | - | none |
| 2174 | seven | seofon | regular | no | - | - | - | none |
| 2175 | shaft | sċeaft | regular | no | - | - | - | none |
| 2176 | shame | sċamu | regular | no | - | - | - | none |
| 2177 | shear | sċieran | regular | no | - | - | - | none |
| 2178 | sheath | sċēaþ | regular | no | - | - | - | none |
| 2180 | shield | sċield | regular | no | - | - | - | none |
| 2182 | shine | sċīnan | regular | no | - | - | - | none |
| 2185 | shovel | sċofl | regular | no | - | - | - | none |
| 2187 | shower | sċūr | regular | no | - | - | - | none |
| 2188 | side | sīde | regular | no | - | - | - | none |
| 2190 | sing | singan | regular | no | - | - | - | none |
| 2191 | singe | senġan | regular | no | - | - | - | none |
| 2192 | sister | swester | regular | no | - | - | - | none |
| 2193 | sit | sittan | regular | no | - | - | - | none |
| 2194 | six | six | regular | no | - | - | - | none |
| 2195 | slay | slēan | regular | no | - | - | - | none |
| 2197 | slime | slīm | regular | no | - | - | - | none |
| 2199 | snow | snāw | regular | no | - | - | - | none |
| 2200 | sorrow | sorg | regular | no | - | - | - | none |
| 2201 | soul | sāwol | regular | no | - | - | - | none |
| 2206 | spear | speoru | regular | no | - | - | - | none |
| 2207 | spin | spinnan | regular | no | - | - | - | none |
| 2208 | spindle | spinl | regular | no | - | - | - | none |
| 2209 | spoon | spōn | regular | no | - | - | - | none |
| 2210 | spread | sprǣdan | regular | no | - | - | - | none |
| 2211 | spur | spora | regular | no | - | - | - | none |
| 2213 | start | styrtan | regular | no | - | - | - | none |
| 2214 | starve | steorfan | regular | no | - | - | - | none |
| 2215 | steal | stelan | regular | no | - | - | - | none |
| 2219 | stock | stocc | regular | no | - | - | - | none |
| 2220 | stone | stān | regular | no | - | - | - | none |
| 2221 | stool | stōl | regular | no | - | - | - | none |
| 2222 | stork | storc | regular | no | - | - | - | none |
| 2223 | storm | storm | regular | no | - | - | - | none |
| 2224 | straw | strēaw | regular | no | - | - | - | none |
| 2225 | stream | strēam | regular | no | - | - | - | none |
| 2226 | stretch | streċċan | regular | no | - | - | - | none |
| 2228 | string | strenġ | regular | no | - | - | - | none |
| 2229 | stud | stōd | regular | no | - | - | - | none |
| 2231 | sun | sunne | regular | no | - | - | - | none |
| 2233 | sup | sūpan | regular | no | - | - | - | none |
| 2236 | swell | swellan | regular | no | - | - | - | none |
| 2237 | swim | swimman | regular | no | - | - | - | none |
| 2239 | sword | sweord | regular | no | - | - | - | none |
| 2241 | team | tēam | regular | no | - | - | - | none |
| 2243 | thane | þeġn | regular | no | - | - | - | none |
| 2244 | thanks | þanc | regular | no | - | - | - | none |
| 2245 | thatch | þæc | regular | no | - | - | - | none |
| 2246 | thief | þēof | regular | no | - | - | - | none |
| 2247 | thing | þing | regular | no | - | - | - | none |
| 2249 | thirst | þurst | regular | no | - | - | - | none |
| 2253 | thrash | þresċan | regular | no | - | - | - | none |
| 2255 | thunder | þunor | regular | no | - | - | - | none |
| 2256 | tick | ticca | regular | no | - | - | - | none |
| 2259 | toe | tā | regular | no | - | - | - | none |
| 2261 | tongs | tang | regular | no | - | - | - | none |
| 2262 | tongue | tunge | regular | no | - | - | - | none |
| 2264 | tread | tredan | regular | no | - | - | - | none |
| 2265 | trough | trog | regular | no | - | - | - | none |
| 2267 | wain | wæġn | regular | no | - | - | - | none |
| 2269 | warp | wearp | regular | no | - | - | - | none |
| 2271 | wart | wearte | regular | no | - | - | - | none |
| 2275 | wax | weax | regular | no | - | - | - | none |
| 2279 | weasel | wesle | regular | no | - | - | - | none |
| 2280 | weather | weder | regular | no | - | - | - | none |
| 2281 | weave | wefan | regular | no | - | - | - | none |
| 2282 | west | westene | regular | no | - | - | - | none |
| 2283 | wether | weþer | regular | no | - | - | - | none |
| 2285 | while | hwīl | regular | no | - | - | - | none |
| 2287 | whore | hōre | regular | no | - | - | - | none |
| 2288 | widow | wuduwe | regular | no | - | - | - | none |
| 2289 | wield | wealdan | regular | no | - | - | - | none |
| 2290 | wife | wīf | regular | no | - | - | - | none |
| 2291 | wight | wiht | regular | no | - | - | - | none |
| 2292 | will | willan | regular | no | - | - | - | none |
| 2295 | winter | winter | regular | no | - | - | - | none |
| 2299 | wonder | wundor | regular | no | - | - | - | none |
| 2301 | word | word | regular | no | - | - | - | none |
| 2303 | worm | wyrm | regular | no | - | - | - | none |
| 2304 | wring | wringan | regular | no | - | - | - | none |
| 2306 | year | ġēar | regular | no | - | - | - | none |
| 2307 | yoke | ġeoc | regular | no | - | - | - | none |

## Regular rows with empty NOTE but manual report present

| ID | Concept | Counterpart | DERIVATION_CLASS | NOTE? | Coverage source | Report status | Report path(s) | Requirement basis |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1933 | adder | nǣdre | regular | no | manifest_format_test | format_test | pilot/adder.md | none |

## Rows with STATUS=format_test reports

| ID | Concept | Counterpart | DERIVATION_CLASS | NOTE? | Coverage source | Report status | Report path(s) | Requirement basis |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1933 | adder | nǣdre | regular | no | manifest_format_test | format_test | pilot/adder.md | none |

## Ambiguous report files

_None_

## Unmatched report files

_None_

