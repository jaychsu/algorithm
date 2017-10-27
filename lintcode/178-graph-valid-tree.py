class Solution:
    """
    @param: n: An integer
    @param: edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def validTree(self, n, edges):
        nodes = [i for i in range(n)]
        for a, b in edges:
            root_a = self.find(nodes, a)
            root_b = self.find(nodes, b)
            if root_a == root_b:
                # If the node pair has the same root node, then the incoming edge will make a closed area
                return False
            else:
                nodes[root_a] = root_b
        return len(edges) == n - 1

    def find(self, nodes, a):
        if nodes[a] == a:
            return a
        nodes[a] = self.find(nodes, nodes[a])
        return nodes[a]
