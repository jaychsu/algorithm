"""
Test Case:

{1}
[0]
1
0
"""
"""
Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""


class Solution:
    """
    @param {UndirectedGraphNode[]} graph a list of undirected graph node
    @param {dict} values a dict, <UndirectedGraphNode, (int)value>
    @param {UndirectedGraphNode} node an Undirected graph node
    @param {int} target an integer
    @return {UndirectedGraphNode} a node
    """
    def searchNode(self, graph, values, node, target):
        if not graph:
            return

        queue = [node]
        visited = {_node: False for _node in graph}

        for _node in queue:
            visited[_node] = True
            if values[_node] == target:
                return _node
            for _neighbor in _node.neighbors:
                if not visited[_neighbor]:
                    queue.append(_neighbor)
