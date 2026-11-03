#!/usr/bin/env python3
"""Complete functionality test for finite, closed-alphabet ATT transducers.

The input-synchronized twin graph includes independent epsilon moves.
Only twins admitting a common accepting continuation are relevant.
Each live twin must have exactly one prefix-cancelled output delay; every
accepting twin must have empty delay. No bound on delay or word length is
assumed. Unknown/identity labels are rejected rather than approximated.
"""
from collections import defaultdict, deque
import hashlib
import json


EPSILON = "@0@"
SPECIAL = {"@_UNKNOWN_SYMBOL_@", "@_IDENTITY_SYMBOL_@"}


def read_att(text):
    arcs, finals = [], set()
    for line in text.splitlines():
        fields = line.split("\t")
        if len(fields) == 1:
            finals.add(int(fields[0]))
        elif len(fields) == 4:
            source, target, upper, lower = fields
            if upper in SPECIAL or lower in SPECIAL:
                raise ValueError("Symbolic unknown/identity arcs require a different proof")
            arcs.append((int(source), int(target), upper, lower))
        else:
            raise ValueError("Expected unweighted ATT with explicit symbol labels")
    return arcs, finals


def cancel(left, right):
    index = 0
    while index < min(len(left), len(right)) and left[index] == right[index]:
        index += 1
    return left[index:], right[index:]


def twins(arcs, finals):
    epsilon, consuming = defaultdict(list), defaultdict(lambda: defaultdict(list))
    for index, (source, target, upper, lower) in enumerate(arcs):
        if upper == EPSILON:
            epsilon[source].append(index)
        else:
            consuming[source][upper].append(index)
    graph, reverse, parents = {}, defaultdict(list), {(0, 0): None}
    pending = deque([(0, 0)])
    while pending:
        pair = pending.popleft()
        p, q = pair
        edges = [(arcs[i][1], q, i, None) for i in epsilon[p]]
        edges += [(p, arcs[j][1], None, j) for j in epsilon[q]]
        for symbol in consuming[p].keys() & consuming[q].keys():
            edges += [(arcs[i][1], arcs[j][1], i, j)
                      for i in consuming[p][symbol] for j in consuming[q][symbol]]
        graph[pair] = []
        for p2, q2, i, j in edges:
            target = (p2, q2)
            edge = (target, i, j)
            graph[pair].append(edge)
            reverse[target].append((pair, i, j))
            if target not in parents:
                parents[target] = (pair, i, j)
                pending.append(target)
    live = {pair: None for pair in graph if pair[0] in finals and pair[1] in finals}
    pending = deque(live)
    while pending:
        pair = pending.popleft()
        for previous, i, j in reverse[pair]:
            if previous not in live:
                live[previous] = (pair, i, j)
                pending.append(previous)
    return graph, live


def extend(delay, i, j, arcs):
    left, right = delay
    if i is not None and arcs[i][3] != EPSILON:
        left += (arcs[i][3],)
    if j is not None and arcs[j][3] != EPSILON:
        right += (arcs[j][3],)
    return cancel(left, right)


def prefix(parents, pair):
    result = []
    while parents[pair] is not None:
        previous, i, j = parents[pair]
        result.append((i, j))
        pair = previous
    return list(reversed(result))


def suffix(live, pair):
    result = []
    while live[pair] is not None:
        pair, i, j = live[pair]
        result.append((i, j))
    return result


def witness(path, arcs, finals):
    states, inputs, outputs, paths = [0, 0], [[], []], [[], []], [[], []]
    for edge in path:
        for side, index in enumerate(edge):
            if index is None:
                continue
            source, target, upper, lower = arcs[index]
            assert source == states[side]
            states[side] = target
            paths[side].append(index)
            if upper != EPSILON:
                inputs[side].append(upper)
            if lower != EPSILON:
                outputs[side].append(lower)
    assert inputs[0] == inputs[1] and all(s in finals for s in states)
    if outputs[0] == outputs[1]:
        return None
    return dict(input=inputs[0], outputs=outputs, arc_paths=paths)


def analyze(text):
    arcs, finals = read_att(text)
    graph, live = twins(arcs, finals)
    common = dict(
        att_sha256=hashlib.sha256(text.encode()).hexdigest(),
        arcs=len(arcs), reachable_twins=len(graph), live_twins=len(live),
        alphabet="finite closed, labels treated as indivisible symbols")
    if (0, 0) not in live:
        return dict(common, functional=True, delays=[], maximum_delay=0)
    delays, parents = {(0, 0): ((), ())}, {(0, 0): None}
    pending = deque([(0, 0)])
    while pending:
        pair = pending.popleft()
        if pair[0] in finals and pair[1] in finals and any(delays[pair]):
            found = witness(prefix(parents, pair), arcs, finals)
            assert found
            return dict(common, functional=False, witness=found)
        for target, i, j in graph[pair]:
            if target not in live:
                continue
            delay = extend(delays[pair], i, j, arcs)
            if (delay[0] and delay[1]) or (target in delays and delays[target] != delay):
                choices = [prefix(parents, pair) + [(i, j)] + suffix(live, target)]
                if target in parents:
                    choices.append(prefix(parents, target) + suffix(live, target))
                for path in choices:
                    found = witness(path, arcs, finals)
                    if found:
                        return dict(common, functional=False, witness=found)
                raise AssertionError("Distinct delays must yield a distinguishing completion")
            if target not in delays:
                delays[target] = delay
                parents[target] = (pair, i, j)
                pending.append(target)
    assert len(delays) == len(live)
    return dict(
        common, functional=True,
        maximum_delay=max(len(a) + len(b) for a, b in delays.values()),
        delays=[[p, q, list(a), list(b)] for (p, q), (a, b) in sorted(delays.items())])


def verify(text, certificate):
    def require(condition):
        if not condition:
            raise ValueError("Invalid global functionality certificate")

    arcs, finals = read_att(text)
    graph, live = twins(arcs, finals)
    require(certificate["functional"])
    require(hashlib.sha256(text.encode()).hexdigest() == certificate["att_sha256"])
    debts = {(p, q): (tuple(a), tuple(b)) for p, q, a, b in certificate["delays"]}
    require(set(debts) == set(live))
    if not live:
        return
    require(debts[(0, 0)] == ((), ()))
    for pair in live:
        if pair[0] in finals and pair[1] in finals:
            require(debts[pair] == ((), ()))
        for target, i, j in graph[pair]:
            if target in live:
                require(extend(debts[pair], i, j, arcs) == debts[target])


if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("att", type=Path)
    parser.add_argument("result", type=Path)
    args = parser.parse_args()
    source = args.att.read_text()
    result = analyze(source)
    if result["functional"]:
        verify(source, result)
    args.result.write_text(json.dumps(result, ensure_ascii=False, sort_keys=True) + "\n")
    print(json.dumps({k: v for k, v in result.items() if k != "delays"}))
    raise SystemExit(0 if result["functional"] else 1)
