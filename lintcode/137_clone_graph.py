"""
Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""


class Solution:
    new_nodes = {}

    """
    @param: node: A undirected graph node
    @return: A undirected graph node
    """
    def cloneGraph(self, node):
        if not node:
            return

        if node.label in self.new_nodes:
            return self.new_nodes[node.label]

        self.new_nodes[node.label] = UndirectedGraphNode(node.label)
        for neighbor in node.neighbors:
            self.new_nodes[node.label].neighbors.append(self.cloneGraph(neighbor))

        return self.new_nodes[node.label]
