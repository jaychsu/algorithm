class Solution:
    """
    @param A: the arrays
    @return: the number of the intersection of the arrays
    """
    def intersectionOfArrays(self, A):
        ans = 0
        if not A:
            return ans

        n = len(A)
        C = {}

        for i in range(n):
            if not A[i]:
                return ans

            for a in A[i]:
                if a not in C:
                    C[a] = set()
                C[a].add(i)

        for a, S in C.items():
            if len(S) == n:
                ans += 1

        return ans
