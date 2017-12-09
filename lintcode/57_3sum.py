"""
Test Case:

[-2,-3,5,-1,-4,5,-11,7,1,2,3,4,-7,-1,-2,-3,-4,-5]
"""


class Solution:
    """
    @param: A: Give an array A of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum(self, A):
        ans = []
        if not A or len(A) < 3:
            return ans

        A.sort()

        n = len(A)
        for i in range(n - 2):
            # `A[n - 1]`, `A[n - 2]` was ignored
            # since `-A[n - 1]`, `-A[n - 2]` are the minimums
            # its impossible to be target
            if i > 0 and A[i] == A[i - 1]:
                continue

            self.twoSum(A, i, i + 1, n - 1, ans)

        return ans

    def twoSum(self, A, a, b, c, results):
        target = -A[a]

        _sum = 0
        while b < c:
            _sum = A[b] + A[c]
            if _sum == target:
                results.append([A[a], A[b], A[c]])
                b += 1
                c -= 1
                while b < c and A[b] == A[b - 1]:
                    b += 1
                while b < c and A[c] == A[c + 1]:
                    c -= 1
                continue
            if _sum < target:
                b += 1
            else:
                c -= 1
