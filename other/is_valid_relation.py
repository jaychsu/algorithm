"""
Question:

The rules look like this:
'A NE B' - means this means point A is located northeast of point B.
'A SW C' - means that point A is southwest of C.
'A N D' - means that point A is north of D but maybe true north, northeast, or northwest.

Given a list of rules, check if the sum of the rules validates. For example:
['A N B', 'B NE C', 'C N A'], returns False
['A N B', 'B NE C', 'C S A'], returns True


Testing:

>>> gotcha = []
>>> for _in, _out in (
...     ([], False),
...     ([''], False),
...     (['A N B', 'B NE C', 'C N A'], False),
...     (['A N B', 'B NW C', 'C N C'], False),
...     (['A N B', 'B N C', 'C N B'], False),
...     (['A N B', 'B NE C', 'C S A'], True),
...     (['A N B', 'B NW C', 'C S A'], True),
...     (['A E B', 'B E C', 'C S D', 'D S E'], True),
...     (['A N B', 'B S A', 'C E D', 'D W C'], True),
... ):
...     res = is_valid_relation(_in)
...     if res != _out: print(_in, res)
...     gotcha.append(res == _out)
>>> bool(gotcha) and all(gotcha)
True
"""
import collections


def is_valid_relation(strs):
    """
    :type strs: list[str]
    :rtype: bool
    """
    if not strs:
        return False

    # egraph => scan from east to west
    egraph = collections.defaultdict(set)
    wgraph = collections.defaultdict(set)
    ngraph = collections.defaultdict(set)
    sgraph = collections.defaultdict(set)

    for s in strs:
        if not s:
            return False

        dst, d, src = s.split()

        if 'E' in d:
            egraph[dst].add(src)
            wgraph[src].add(dst)
        elif 'W' in d:
            wgraph[dst].add(src)
            egraph[src].add(dst)

        if 'N' in d:
            ngraph[dst].add(src)
            sgraph[src].add(dst)
        elif 'S' in d:
            sgraph[dst].add(src)
            ngraph[src].add(dst)

    for graph in (egraph, wgraph, ngraph, sgraph):
        for node in graph.keys():
            if dfs(graph, node, set()):
                return False

    return True


def dfs(graph, node, visited):
    """
    returns True if there is cycle in graph
    :type graph: dict{str: set}
    :type node: str
    :type visited: set
    :rtype: bool
    """
    if node not in graph:
        return False
    if node in visited:
        return True

    visited.add(node)

    for nxt in graph[node]:
        if dfs(graph, nxt, visited):
            return True

    return False
