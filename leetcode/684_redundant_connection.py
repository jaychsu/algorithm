"""
given input is an undirected graph

1. iterate edges
2. if u and v are connected before we add edge in nodes (graph)
   => that is the edge should be removed
"""


class Solution:
    """
    UnionFind
    """
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if not edges:
            return []

        nodes = {}

        for u, v in edges:
            if not self.union(nodes, u, v):
                return [u, v]

        return []

    def union(self, nodes, u, v):
        a = self.find(nodes, u)
        b = self.find(nodes, v)

        if a == b:
            return False

        nodes[a] = b
        return True

    def find(self, nodes, u):
        if u not in nodes:
            nodes[u] = u
            return u
        if nodes[u] == u:
            return u

        nodes[u] = self.find(nodes, nodes[u])
        return nodes[u]


import collections


class Solution:
    """
    DFS
    """
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if not edges:
            return []

        nodes = collections.defaultdict(set)

        for u, v in edges:
            # dfs to check u and v are connected already => cycle
            if u in nodes and v in nodes and self.dfs(nodes, u, v, set()):
                return [u, v]

            nodes[u].add(v)
            nodes[v].add(u)

        return []

    def dfs(self, nodes, u, v, visited):
        if u == v:
            return True
        if u in visited:
            return False

        visited.add(u)

        for x in nodes[u]:
            if self.dfs(nodes, x, v, visited):
                return True

        return False
