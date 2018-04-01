"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""
import heapq


class Solution:
    """
    max heap
    """
    def kClosest(self, points, origin, k):
        """
        :type points: list[Point]
        :type origin: Point
        :type k: int
        :rtype: list[Point]
        """
        ans = []

        if not points or not origin or not k:
            return ans

        for i in range(len(points)):
            distance = self.get_distance(origin, points[i])
            heapq.heappush(ans, (-distance, i))

            if len(ans) > k:
                heapq.heappop(ans)

        ans.sort(key=lambda a: (-a[0], points[a[1]].x, points[a[1]].y))

        return [points[i] for _, i in ans]

    def get_distance(self, p, q):
        dx = p.x - q.x
        dy = p.y - q.y
        return dx * dx + dy * dy


import heapq


class Solution:
    """
    min heap
    """
    def kClosest(self, points, origin, k):
        """
        :type points: list[Point]
        :type origin: Point
        :type k: int
        :rtype: list[Point]
        """
        ans = []

        if not points or not origin or not k:
            return ans

        heap = []

        for i in range(len(points)):
            distance = self.get_distance(origin, points[i])
            heapq.heappush(heap, (distance, i))

        for _ in range(k):
            distance, i = heapq.heappop(heap)
            ans.append((distance, points[i]))

        ans.sort(key=lambda a: (a[0], a[1].x, a[1].y))

        return [p for _, p in ans]

    def get_distance(self, p, q):
        dx = p.x - q.x
        dy = p.y - q.y
        return dx * dx + dy * dy
