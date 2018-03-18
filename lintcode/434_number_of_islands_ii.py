"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""


class Solution:
    def numIslands2(self, m, n, operators):
        """
        :type m: int
        :type n: int
        :type operators: list[Point]
        :rtype list[int]:
        """
        ans = []
        if not m or not n or not operators:
            return ans

        nodes = {}
        cnt = 0

        for p in operators:
            node = (p.x, p.y)

            if node not in nodes:
                nodes[node] = node
                cnt += 1

            for dx, dy in (
                ( 0, -1),
                ( 0,  1),
                (-1,  0),
                ( 1,  0),
            ):
                _x = p.x + dx
                _y = p.y + dy

                if not (0 <= _x < m and 0 <= _y < n):
                    continue
                if self.connect(nodes, node, (_x, _y)):
                    cnt -= 1

            ans.append(cnt)

        return ans

    def connect(self, nodes, a, b):
        if a not in nodes or b not in nodes:
            return False

        _a = self.find(nodes, a)
        _b = self.find(nodes, b)

        if _a is _b:
            return False

        nodes[_a] = _b
        return True

    def find(self, nodes, a):
        if nodes[a] is a:
            return a

        nodes[a] = self.find(nodes, nodes[a])
        return nodes[a]
