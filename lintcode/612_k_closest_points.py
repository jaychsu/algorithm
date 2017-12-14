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
    @param: points: a list of points
    @param: origin: a point
    @param: k: An integer
    @return: the k closest points
    """
    def kClosest(self, points, origin, k):
        if not points:
            return

        heap = []
        for point in points:
            distance = self.get_distance(origin, point)
            heappush(heap, (-distance, point))

            if len(heap) > k:
                heappop(heap)

        heap.sort(key=lambda item: (-item[0], item[1].x, item[1].y))

        return [p for _, p in heap]

    def get_distance(self, a, b):
        if not a or not b:
            return float('inf')

        a, b = (a.x - b.x), (a.y - b.y)

        return a * a + b * b
