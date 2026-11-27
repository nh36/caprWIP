"""Component-only controls for an explicit, private compound boundary."""

import candidates
import palatal

RULES = {
    name: candidates.RULES[name]
    for name in (candidates.CONTRACT, candidates.GLIDE, candidates.FINAL_GLIDE, candidates.C_GLIDE)
}
RULES.update(palatal.RULES)
RULES.update({
    "HiMemberGlide": """[
        [{*e}{*i} -> {*e}{*j} || HiHeadContext _ [{*⊕}|.#.]]
        .o. [{*é}{*i} -> {*é}{*j} || _ [{*⊕}|.#.]]
    ]""",
    "DaMemberLoss": """[
        {*j} -> 0 || [EnglishStarLongVowel | EnglishStarDiphthong] _ [{*⊕}|.#.]
    ]""",
})


def definitions():
    return candidates.PREFIX + "".join(f"define {name} {body};\n" for name, body in RULES.items())
