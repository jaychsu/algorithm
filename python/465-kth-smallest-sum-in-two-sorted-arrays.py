import heapq

"""
Assuming: len(A) == len(B) == 3

To find the result(min of A[i]+B[j]), we got a 3x3 matrix:
BA | 0 | 1 | 2 |
 0 | a | b | c |
 1 | d | e | f |
 2 | g | h | i |

 1. put the first column (0, j) into heap, these child is the min for each row
 2. get the minest one, and move the `x` pointer forward, put the child at (x+1, y)
 3. keep find the minest one in current heap, then we can find the kth child
"""

class Solution:

    """
    @param: A: an integer arrays sorted in ascending order
    @param: B: an integer arrays sorted in ascending order
    @param: k: An integer
    @return: An integer
    """
    def kthSmallestSum(self, A, B, k):
        m, n = len(A), len(B)
        heap = []
        min_child = -1
        for i in range(min(k, n)):
            heapq.heappush(heap, (A[0] + B[i], 0, i))
        while k > 0:
            min_child = heapq.heappop(heap)
            x, y = min_child[1], min_child[2]
            if x + 1 < m:
                heapq.heappush(heap, (A[x + 1] + B[y], x + 1, y))
            k -= 1
        return min_child[0]
