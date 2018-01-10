class Solution:
    """
    @param: A: Give an array A of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum(self, A):
        ans = []
        if not A or len(A) < 3:
            return ans

        n = len(A)
        A.sort()

        for a in range(n - 2):
            if a > 0 and A[a] == A[a - 1]:
                continue

            b = a + 1
            c = n - 1
            while b < c:
                _sum = A[a] + A[b] + A[c]
                if _sum == 0:
                    ans.append([A[a], A[b], A[c]])
                    b += 1
                    c -= 1
                    while b < c and A[b] == A[b - 1]:
                        b += 1
                    while b < c and A[c] == A[c + 1]:
                        c -= 1
                    continue

                if _sum < 0:
                    b += 1
                else:
                    c -= 1

        return ans
