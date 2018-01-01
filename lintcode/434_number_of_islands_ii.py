"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""


class Solution:
    V = (
        (-1,  0),
        ( 1,  0),
        ( 0, -1),
        ( 0,  1),
    )

    """
    @param: m: An integer
    @param: n: An integer
    @param: P: an array of point
    @return: an integer array
    """
    def numIslands2(self, m, n, P):
        ans = []
        if not m or not n or not P:
            return ans

        N = {}
        cnt = 0
        for p in P:
            cell = (p.x, p.y)

            if cell not in N:
                N[cell] = cell
                cnt += 1

            for dx, dy in self.V:
                _x = p.x + dx
                _y = p.y + dy
                if not (0 <= _x < m and 0 <= _y < n):
                    continue
                if self.connect(N, cell, (_x, _y)):
                    cnt -= 1

            ans.append(cnt)

        return ans

    def connect(self, N, a, b):
        if a not in N or b not in N:
            return False

        root_a = self.find(N, a)
        root_b = self.find(N, b)
        if root_a is not root_b:
            N[root_a] = root_b
            return True

        return False

    def find(self, N, a):
        if N[a] is a:
            return a

        N[a] = self.find(N, N[a])
        return N[a]
