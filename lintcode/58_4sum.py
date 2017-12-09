class Solution:
    """
    @param: A: Give an array
    @param: target: An integer
    @return: Find all unique quadruplets in the array which gives the sum of zero
    """
    def fourSum(self, A, target):
        ans = []
        if not A or len(A) < 4:
            return ans

        A.sort()

        n = len(A)
        c = d = _sum = 0
        for a in range(n - 3):
            if a > 0 and A[a] == A[a - 1]:
                continue
            for b in range(a + 1, n - 2):
                if b > a + 1 and A[b] == A[b - 1]:
                    continue
                c = b + 1
                d = n - 1
                while c < d:
                    _sum = A[a] + A[b] + A[c] + A[d]
                    if _sum == target:
                        ans.append([A[a], A[b], A[c], A[d]])
                        c += 1
                        d -= 1
                        while c < d and A[c] == A[c - 1]:
                            c += 1
                        while c < d and A[d] == A[d + 1]:
                            d -= 1
                        continue
                    if _sum < target:
                        c += 1
                    else:
                        d -= 1

        return ans
