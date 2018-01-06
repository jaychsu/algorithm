class Solution:
    """
    @param: A: A list of integers
    @return: An integer
    """
    def longestConsecutive(self, A):
        ans = 0
        if not A:
            return ans

        C = set(A)  # candidates

        for a in A:
            if a not in C:
                continue

            C.discard(a)
            size = 1
            b, c = a - 1, a + 1

            while b in C:
                C.discard(b)
                b -= 1
                size += 1

            while c in C:
                C.discard(c)
                c += 1
                size += 1

            if size > ans:
                ans = size

        return ans
