class Solution:
    """
    @param: A: A list of integers
    @return: An integer
    """
    def longestConsecutive(self, A):
        ans = 0
        if not A:
            return ans

        S = set(A)

        for a in A:
            if a not in S:
                continue

            S.discard(a)
            size = 1
            b, c = a - 1, a + 1

            while b in S:
                S.discard(b)
                b -= 1
                size += 1
            while c in S:
                S.discard(c)
                c += 1
                size += 1

            if size > ans:
                ans = size

        return ans
