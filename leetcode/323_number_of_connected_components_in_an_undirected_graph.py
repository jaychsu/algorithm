"""
Testing:
>>> gotcha = []
>>> for s in (Solution(), Solution2()):
...     for _in, _out in (
...         ((5, [[0, 1], [1, 2], [3, 4]]), 2),
...         ((5, [[0, 1], [1, 2], [2, 3], [3, 4]]), 1),
...     ):
...         res = s.countComponents(*_in)
...         if res != _out: print(_in, res)
...         gotcha.append(res == _out)
>>> bool(gotcha) and all(gotcha)
True
"""


class Solution:
    """
    Union Find
    """
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: list[int]
        :rtype: int
        """
        if not n or not edges:
            return 0

        nodes = [i for i in range(n)]

        ans = n

        for a, b in edges:
            if self.union(nodes, a, b):
                ans -= 1

        return ans

    def union(self, nodes, a, b):
        _a = self.find(nodes, a)
        _b = self.find(nodes, b)

        if _a == _b:
            return False

        nodes[_b] = _a
        return True

    def find(self, nodes, a):
        if a not in nodes:
            nodes[a] = a
            return a
        if nodes[a] == a:
            return a

        nodes[a] = self.find(nodes[a])
        return nodes[a]


class Solution2:
    """
    DFS
    """
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: list[int]
        :rtype: int
        """
        ans = 0

        if not n or not edges:
            return ans

        adj = {}

        for i in range(n):
            adj[i] = set()

        for a, b in edges:
            adj[a].add(b)
            adj[b].add(a)

        visited = set()

        for i in range(n):
            if i in visited:
                continue

            ans += 1
            self.dfs(i, adj, visited)

        return ans

    def dfs(self, a, adj, visited):
        if a not in adj:
            return

        visited.add(a)

        for b in adj[a]:
            if b in visited:
                continue

            self.dfs(b, adj, visited)
