"""
>>> pairs = [['great', 'fine'], ['acting', 'drama'], ['skills', 'talent']]
>>> gotcha = []
>>> for s in (Solution(), Solution2()):
...     for _in, _out in (
...         ((['great', 'acting'], ['fine', 'drama'], pairs), True),
...         ((['great', 'acting'], ['fine', 'talent'], pairs), False),
...         ((['great'], ['great'], []), True),
...         ((['great'], ['fine', 'drama'], pairs), False),
...     ):
...         res = s.areSentencesSimilarTwo(*_in)
...         if res != _out: print(_in, res)
...         gotcha.append(res == _out)
>>> bool(gotcha) and all(gotcha)
True
"""


class Solution:
    """
    UnionFind
    """
    def areSentencesSimilarTwo(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        if len(words1) != len(words2):
            return False

        nodes = {}

        for a, b in pairs:
            self.union(nodes, a, b)

        for i in range(len(words1)):
            a = words1[i]
            b = words2[i]
            _a = self.find(nodes, a)
            _b = self.find(nodes, b)

            if a != b and _a != _b:
                return False

        return True

    def union(self, nodes, a, b):
        _a = self.find(nodes, a)
        _b = self.find(nodes, b)

        if _a is not _b:
            nodes[_a] = _b

        return _b

    def find(self, nodes, a):
        if a not in nodes:
            nodes[a] = a
            return a
        if nodes[a] is a:
            return a

        nodes[a] = self.find(nodes, nodes[a])
        return nodes[a]


import collections


class Solution2:
    """
    DFS
    """
    def areSentencesSimilarTwo(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        if len(words1) != len(words2):
            return False

        simils = collections.defaultdict(set)

        for a, b in pairs:
            simils[a].add(b)
            simils[b].add(a)

        for i in range(len(words1)):
            a = words1[i]
            b = words2[i]

            if a != b and not self.dfs(a, b, simils, set()):
                return False

        return True

    def dfs(self, start, end, simils, path):
        # check start and end are connected
        if start == end:
            return True
        if start not in simils or start in path:
            return False

        path.add(start)

        for nxt in simils[start]:
            if nxt in path:
                continue

            res = self.dfs(nxt, end, simils, path)
            if res:
                return True

        path.discard(start)
        return False
