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
    @param: A: a list of points
    @param: O: a point
    @param: k: An integer
    @return: the k closest points
    """
    def kClosest(self, A, O, k):
        ans = []
        if not A or not O:
            return ans

        for P in A:
            distance = self.get_distance(P, O)
            heappush(ans, (-distance, P))

            if len(ans) > k:
                heappop(ans)

        ans.sort(key=lambda a: (-a[0], a[1].x, a[1].y))
        return [P for _, P in ans]

    def get_distance(self, P, O):
        if not P or not O:
            return float('inf')

        x = P.x - O.x
        y = P.y - O.y
        return x * x + y * y
