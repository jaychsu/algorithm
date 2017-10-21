import heapq

"""
Assuming: len(A) == len(B) == 3

To find the result(min of A[i]+B[j]), we got a 3x3 matrix:
AB | 0 | 1 | 2 |
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
        ans = j = 0
        heap = []
        for i in range(min(m, k)): heapq.heappush(heap, (A[i] + B[0], i, 0))
        while k > 0:
            ans = heapq.heappop(heap)
            j = ans[2] + 1
            if j < n:
                heapq.heappush(heap, (A[ans[1]] + B[j], ans[1], j))
            k -= 1
        return ans[0]
