"""
Definition for Undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""


class Solution:
    """
    @param: graph: a list of Undirected graph node
    @param: s: Undirected graph node
    @param: t: Undirected graph nodes
    @return: an integer
    """
    def sixDegrees(self, graph, s, t):
        if not graph or not s or not t:
            return -1
        if s is t:
            return 0

        degree = {s: 0}
        queue = [s]
        for node in queue:
            for _node in node.neighbors:
                if _node in degree:
                    continue
                degree[_node] = degree[node] + 1
                if _node is t:
                    return degree[_node]
                queue.append(_node)

        return -1
