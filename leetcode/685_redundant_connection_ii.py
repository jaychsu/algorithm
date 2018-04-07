"""
given input is an directed graph

3 corner cases:

1. There is a loop in the graph, and no vertex has more than 1 parent.
2. A vertex has more than 1 parent, but there isn’t a loop in the graph.
3. A vertex has more than 1 parent, and is part of a loop.

REF: https://leetcode.com/problems/redundant-connection-ii/discuss/108070/Python-O(N)-concise-solution-with-detailed-explanation-passed-updated-testcases
"""


import collections


class Solution:
    def findRedundantDirectedConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        ans = edge = None  # `edge` is the last edge in a loop
        adj = collections.defaultdict(set)
        uf = collections.defaultdict(int)
        has_parent = set()

        for u, v in edges:
            adj[u].add(v)

            if v in has_parent:
                ans = (u, v)

            if not self.union(uf, u, v):
                edge = (u, v)

            has_parent.add(v)

        if not ans:
            return edge

        res = self.dfs(ans[1], adj, set())
        return res if res else ans

    def union(self, uf, u, v):
        a = self.find(uf, u)
        b = self.find(uf, v)

        if a == b:
            return False

        uf[b] = a
        return True

    def find(self, uf, u):
        if uf[u] == 0:
            uf[u] = u
            return u
        if uf[u] == u:
            return u

        uf[u] = self.find(uf, uf[u])
        return uf[u]

    def dfs(self, u, adj, visited):
        # to detect cycle
        visited.add(u)

        for v in adj[u]:
            if v in visited:
                return (u, v)

            res = self.dfs(v, adj, visited)
            if res:
                return res
