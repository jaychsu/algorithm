"""
Definition for a Directed graph node
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""


class Solution:
    """
    @param: graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """
    def topSort(self, graph):
        ans = []
        if not graph:
            return ans

        indegs = {}
        for node in graph:
            if node not in indegs:
                indegs[node] = 0
            for _node in node.neighbors:
                if _node not in indegs:
                    indegs[_node] = 0
                indegs[_node] += 1

        queue = [node for node, indeg in indegs.items() if indeg == 0]
        for node in queue:
            ans.append(node)
            for _node in node.neighbors:
                indegs[_node] -= 1
                if indegs[_node] == 0:
                    queue.append(_node)

        return ans
