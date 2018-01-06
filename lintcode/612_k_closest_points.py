"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""
from heapq import heappop, heappush


class Solution:
    """
    @param: P: a list of points
    @param: o: a point
    @param: k: An integer
    @return: the k closest points
    """
    def kClosest(self, P, o, k):
        ans = []
        if not P or not o:
            return ans

        for p in P:
            distance = self.get_distance(p, o)
            heappush(ans, (-distance, p))

            if len(ans) > k:
                heappop(ans)

        ans.sort(key=lambda a: (-a[0], a[1].x, a[1].y))
        return [a[1] for a in ans]

    def get_distance(self, p, o):
        if not p or not o:
            return float('inf')

        dx = p.x - o.x
        dy = p.y - o.y
        return dx * dx + dy * dy
