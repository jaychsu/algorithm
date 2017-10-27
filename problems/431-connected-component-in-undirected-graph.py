"""
Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""


class Solution:
    def __init__(self):
        self.nodes = {}

    """
    @param {UndirectedGraphNode[]} nodes a array of undirected graph node
    @return {int[][]} a connected set of a undirected graph
    """
    def connectedSet(self, nodes):
        for node in nodes:
            for nei in node.neighbors:
                self.connect(nei.label, node.label)
        result = {}
        root_label = ''
        for node in nodes:
            root_label = self.find(node.label)
            if root_label not in result:
                result[root_label] = []
            result[root_label].append(node.label)
        return result.values()

    def connect(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a is not root_b:
            self.nodes[root_a] = root_b

    def find(self, a):
        if a not in self.nodes:
            self.nodes[a] = a
            return a
        elif self.nodes[a] is a:
            return a
        self.nodes[a] = self.find(self.nodes[a])
        return self.nodes[a]
