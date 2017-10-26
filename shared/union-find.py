class UnionFind:
    def __init__(self):
        self.nodes = {}

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
