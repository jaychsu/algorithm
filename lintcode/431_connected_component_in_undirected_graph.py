"""
Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""


class Solution:
    """
    Union Find
    """
    def connectedSet(self, nodes):
        """
        :type nodes: list[UndirectedGraphNode]
        :rtype: list[list[UndirectedGraphNode]]
        """
        if not nodes:
            return []

        uf = {}

        for node in nodes:
            for neib in node.neighbors:
                self.union(uf, node, neib)

        ans = {}

        for node in nodes:
            # to correct root again
            root = self.find(uf, node)

            if root not in ans:
                ans[root] = []

            ans[root].append(node.label)

        return list(ans.values())

    def union(self, nodes, a, b):
        _a = self.find(nodes, a)
        _b = self.find(nodes, b)

        if _a is not _b:
            nodes[_b] = _a

    def find(self, nodes, a):
        if a not in nodes:
            nodes[a] = a
            return a
        if nodes[a] is a:
            return a

        nodes[a] = self.find(nodes, nodes[a])
        return nodes[a]


class Solution:
    """
    DFS
    """
    def connectedSet(self, nodes):
        """
        :type nodes: list[UndirectedGraphNode]
        :rtype: list[list[UndirectedGraphNode]]
        """
        ans = []

        if not nodes:
            return ans

        visited = set()

        for node in nodes:
            if node in visited:
                continue

            path = []
            self.dfs(node, visited, path)
            ans.append(sorted(path))

        return ans

    def dfs(self, a, visited, path):
        visited.add(a)
        path.append(a.label)

        for b in a.neighbors:
            if b in visited:
                continue

            self.dfs(b, visited, path)
