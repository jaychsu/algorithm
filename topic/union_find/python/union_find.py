class UnionFind:
    def __init__(self):
        self.nodes = {}

    def __repr__(self):
        return repr(self.nodes)

    def connect(self, a, b):
        _a = self.find(a)
        _b = self.find(b)
        if _a is not _b:
            self.nodes[_a] = _b
        return _b

    def find(self, a):
        if a not in self.nodes:
            self.nodes[a] = a
            return a
        if self.nodes[a] is a:
            return a
        self.nodes[a] = self.find(self.nodes[a])
        return self.nodes[a]
