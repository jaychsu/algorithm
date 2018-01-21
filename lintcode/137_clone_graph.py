"""
Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""


"""
Iteration
"""
class Solution:
    def cloneGraph(self, node):
        """
        :type node: UndirectedGraphNode
        :rtype: UndirectedGraphNode
        """
        if not node:
            return

        queue = [node]
        root = UndirectedGraphNode(node.label)
        N = {root.label: root}

        for node in queue:
            for neighbor in node.neighbors:
                _node = None
                if neighbor.label in N:
                    _node = N[neighbor.label]
                else:
                    _node = UndirectedGraphNode(neighbor.label)
                    N[neighbor.label] = _node
                    queue.append(neighbor)

                N[node.label].neighbors.append(_node)

        return root


"""
Recursion
"""
class Solution:
    def cloneGraph(self, node):
        """
        :type node: UndirectedGraphNode
        :rtype: UndirectedGraphNode
        """
        if not node:
            return

        return self.dfs(node, {})

    def dfs(self, node, N):
        if node.label in N:
            return N[node.label]

        N[node.label] = UndirectedGraphNode(node.label)
        for neighbor in node.neighbors:
            N[node.label].neighbors.append(self.dfs(neighbor, N))

        return N[node.label]
