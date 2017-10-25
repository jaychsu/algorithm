class ConnectingGraph:
    """
    @param: n: An integer
    """
    def __init__(self, n):
        if n < 1:
            return
        self.nodes = [i for i in range(n + 1)]

    def find(self, a):
        if self.nodes[a] == a:
            return a
        self.nodes[a] = self.find(self.nodes[a])
        return self.nodes[a]

    """
    @param: a: An integer
    @param: b: An integer
    @return: nothing
    """
    def connect(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a != root_b:
            self.nodes[root_a] = root_b

    """
    @param: a: An integer
    @param: b: An integer
    @return: A boolean
    """
    def query(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        return root_a == root_b
