class UnionFind:
    def __init__(self):
        self.nodes = {}

    def union(self, u, v):
        a = self.find(u)
        b = self.find(v)

        if a is not b:
            self.nodes[b] = a

        return a

    def find(self, u):
        if u not in self.nodes:
            self.nodes[u] = u
            return u
        if self.nodes[u] is u:
            return u

        self.nodes[u] = self.find(self.nodes[u])
        return self.nodes[u]
