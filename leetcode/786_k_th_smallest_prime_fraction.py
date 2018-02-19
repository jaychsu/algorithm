"""
Main Concept:
just like found kth smallest num in matrix

example: [1, 2, 5, 7]

    7   5   2   1
1  1/7 1/5 1/2 1/1
2  2/7 2/5 ...
5  ...
7  ...
"""
from heapq import heappush, heappop


class Solution:
    def kthSmallestPrimeFraction(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        heap = []
        n = len(A)

        A.sort()

        for i in range(n):
            heappush(heap, (A[i]/A[-1], i, n - 1))

        for _ in range(K - 1):
            _, i, j = heappop(heap)

            j -= 1
            if j >= 0:
                heappush(heap, (A[i]/A[j], i, j))

        _, i, j = heappop(heap)
        return [A[i], A[j]]
