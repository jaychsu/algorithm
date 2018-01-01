"""
Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""


"""
DFS
"""
class Solution:
    """
    @param: N: a array of Undirected graph node
    @return: a connected set of a Undirected graph
    """
    def connectedSet(self, N):
        ans = []
        if not N:
            return ans

        visited = {}
        for node in N:
            visited[node] = False

        for node in N:
            if visited[node]:
                continue
            nodes = []
            self.dfs(node, visited, nodes)
            nodes.sort()
            ans.append(nodes)

        return ans

    def dfs(self, node, visited, nodes):
        visited[node] = True
        nodes.append(node.label)

        for _node in node.neighbors:
            if visited[_node]:
                continue
            self.dfs(_node, visited, nodes)


"""
Union Found
"""
class Solution:
    """
    @param: N: a array of Undirected graph node
    @return: a connected set of a Undirected graph
    """
    def connectedSet(self, N):
        if not N:
            return []

        nodes = {}

        for node in N:
            for _node in node.neighbors:
                self.connect(nodes, _node.label, node.label)

        ans = {}
        for node in N:
            root = self.find(nodes, node.label)
            if root not in ans:
                ans[root] = []
            ans[root].append(node.label)

        return ans.values()

    def connect(self, nodes, a, b):
        root_a = self.find(nodes, a)
        root_b = self.find(nodes, b)
        if root_a is not root_b:
            nodes[root_a] = root_b

    def find(self, nodes, a):
        if a not in nodes:
            nodes[a] = a
            return a
        if nodes[a] is a:
            return a
        nodes[a] = self.find(nodes, nodes[a])
        return nodes[a]
