"""Exact ambiguity domains and subsequential alignment of closed ATT relations."""
from collections import defaultdict, deque

from functionality import EPSILON, analyze, extend, read_att, twins


def att_text(arcs, finals):
    return "".join(f"{p}\t{q}\t{a}\t{b}\n" for p, q, a, b in arcs) + "".join(
        f"{p}\n" for p in sorted(finals))


def ambiguity_domain(text):
    """Explore every live twin and residual; None denotes irreversible mismatch.

    Unlike the functionality decision, this construction need not terminate for
    arbitrary transducers. A returned finite graph is closed under every move;
    no residual, word-length or state-count cutoff is used.
    """
    arcs, finals = read_att(text)
    graph, live = twins(arcs, finals)
    start = ((0, 0), ((), ()))
    states, pending = {start: 0}, deque([start])
    result, accepting = [], set()
    while pending:
        pair, delay = key = pending.popleft()
        number = states[key]
        if pair not in live:
            continue
        if pair[0] in finals and pair[1] in finals and (delay is None or any(delay)):
            accepting.add(number)
        for target, i, j in graph[pair]:
            if target not in live:
                continue
            debt = None if delay is None else extend(delay, i, j, arcs)
            if debt is not None and debt[0] and debt[1]:
                debt = None
            next_key = (target, debt)
            if next_key not in states:
                states[next_key] = len(states)
                pending.append(next_key)
            symbol = arcs[i if i is not None else j][2]
            result.append((number, states[next_key], symbol, symbol))
    certificate = [
        dict(state=n, twin=list(pair),
             delay=None if delay is None else [list(x) for x in delay])
        for (pair, delay), n in states.items()]
    return att_text(result, accepting), certificate


def subsequentialize(text):
    """Exact output-prefix determinization; returns only upon finite closure.

    Not every functional rational relation is subsequential. Termination here
    is demonstrated by the returned complete subset graph, not assumed from
    functionality. Original labels remain indivisible symbols.
    """
    arcs, finals = read_att(text)
    if not analyze(text)["functional"]:
        raise ValueError("Subsequential alignment requires a functional relation")
    reverse = defaultdict(set)
    for p, q, _, _ in arcs:
        reverse[q].add(p)
    live, pending = set(finals), list(finals)
    while pending:
        for p in reverse[pending.pop()]:
            if p not in live:
                live.add(p)
                pending.append(p)
    if 0 not in live:
        return "", dict(subsets=[], transitions=[], final_outputs={})
    epsilon, consuming = defaultdict(list), defaultdict(list)
    for p, q, a, b in arcs:
        if q in live:
            (epsilon if a == EPSILON else consuming)[p].append((q, a, b))

    def closure(items):
        reached, pending = set(items), deque(items)
        while pending:
            p, word = pending.popleft()
            for q, _, b in epsilon[p]:
                target = (q, word + (() if b == EPSILON else (b,)))
                if target not in reached:
                    reached.add(target)
                    pending.append(target)
        return frozenset((p, w) for p, w in reached if p in finals or consuming[p])

    def normalize(items):
        words = [w for _, w in items]
        prefix = words[0]
        for word in words[1:]:
            i = 0
            while i < min(len(prefix), len(word)) and prefix[i] == word[i]:
                i += 1
            prefix = prefix[:i]
        return prefix, frozenset((p, w[len(prefix):]) for p, w in items)

    initial = closure([(0, ())])
    states, pending = {initial: 0}, deque([initial])
    edges, final_words = [], {}
    while pending:
        subset = pending.popleft()
        number = states[subset]
        endings = {w for p, w in subset if p in finals}
        if len(endings) > 1:
            raise ValueError("Nonfunctional final outputs in determinization")
        if endings:
            final_words[number] = endings.pop()
        targets = defaultdict(set)
        for p, word in subset:
            for q, a, b in consuming[p]:
                targets[a].add((q, word + (() if b == EPSILON else (b,))))
        for a, items in sorted(targets.items()):
            closed = closure(items)
            if not closed:
                continue
            word, target = normalize(closed)
            if target not in states:
                states[target] = len(states)
                pending.append(target)
            edges.append((number, states[target], a, word))

    next_state = len(states)
    expanded, accepting = [], set()

    def emit(source, target, upper, word):
        nonlocal next_state
        if not word:
            expanded.append((source, target, upper, EPSILON))
            return
        for index, symbol in enumerate(word):
            destination = target if index == len(word) - 1 else next_state
            if destination == next_state:
                next_state += 1
            expanded.append((source, destination, upper if index == 0 else EPSILON, symbol))
            source = destination

    for p, q, a, word in edges:
        emit(p, q, a, word)
    for p, word in final_words.items():
        if not word:
            accepting.add(p)
        else:
            sink = next_state
            next_state += 1
            emit(p, sink, EPSILON, word)
            accepting.add(sink)
    certificate = dict(
        subsets=[dict(state=n, members=[[p, list(w)] for p, w in sorted(s)])
                 for s, n in states.items()],
        transitions=[[p, q, a, list(w)] for p, q, a, w in edges],
        final_outputs={str(p): list(w) for p, w in final_words.items()})
    return att_text(expanded, accepting), certificate


def domain_check(texts, predicate):
    """Exhaustive DFA-product check of a Boolean domain invariant.

    The predicate must hold at every reachable tuple of acceptance flags.
    A failed check includes a concrete distinguishing input symbol sequence.
    """
    machines = []
    alphabet = set()
    for text in texts:
        arcs, finals = read_att(text)
        eps, move = defaultdict(set), defaultdict(lambda: defaultdict(set))
        for p, q, a, _ in arcs:
            if a == EPSILON:
                eps[p].add(q)
            else:
                move[p][a].add(q)
                alphabet.add(a)

        def closure(items, epsilon=eps):
            reached, pending = set(items), list(items)
            while pending:
                for q in epsilon[pending.pop()]:
                    if q not in reached:
                        reached.add(q)
                        pending.append(q)
            return frozenset(reached)

        machines.append((move, finals, closure))
    start = tuple(close([0]) for _, _, close in machines)
    parents, pending = {start: None}, deque([start])
    while pending:
        states = pending.popleft()
        flags = [bool(s & m[1]) for s, m in zip(states, machines)]
        if not predicate(flags):
            word, current = [], states
            while parents[current] is not None:
                current, symbol = parents[current]
                word.append(symbol)
            return dict(valid=False, input=list(reversed(word)), flags=flags)
        for a in sorted(alphabet):
            target = tuple(
                close({q for p in s for q in move[p][a]})
                for s, (move, _, close) in zip(states, machines))
            if target not in parents:
                parents[target] = (states, a)
                pending.append(target)
    return dict(valid=True, reachable_states=len(parents))
