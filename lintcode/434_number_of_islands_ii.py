"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""


class Solution:
    def __init__(self):
        self.nodes = {}
        self.row_vector = [1, -1, 0, 0]
        self.col_vector = [0, 0, 1, -1]

    def connect(self, a, b):
        # means there is sea, no island
        if a not in self.nodes \
                or b not in self.nodes:
            return False

        root_a = self.find(a)
        root_b = self.find(b)
        if root_a != root_b:
            self.nodes[root_a] = root_b
            return True
        else:
            return False

    def find(self, a):
        if self.nodes[a] == a:
            return a
        self.nodes[a] = self.find(self.nodes[a])
        return self.nodes[a]

    """
    @param: n: An integer
    @param: m: An integer
    @param: operators: an array of point
    @return: an integer array
    """
    def numIslands2(self, n, m, operators):
        if not n or not m \
                or not operators \
                or len(operators) < 1:
            return []
        cell_id = 0
        num_of_island = 0
        result = []
        for op in operators:

            # To convert matrix to line
            cell_id = op.x * m + op.y

            # If a cell becomes an island then `count += 1`
            # and we'll consider the adjacent island in following step
            if cell_id not in self.nodes:
                num_of_island += 1
                self.nodes[cell_id] = cell_id

            # Check the around cells
            for d in range(4):
                x = op.x + self.row_vector[d]
                y = op.y + self.col_vector[d]

                # Using UnionFind to connect the adjacent island together
                # if successful to connect an island, then `count -= 1`
                if 0 <= x < n \
                        and 0 <= y < m \
                        and self.connect(x * m + y, cell_id):
                    num_of_island -= 1
            result.append(num_of_island)
        return result
