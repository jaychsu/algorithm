class Solution:
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        ans = 0
        if not A or not B or not C or not D:
            return ans

        S = {}

        for c in C:
            for d in D:
                key = - (c + d)
                S[key] = S.get(key, 0) + 1

        for a in A:
            for b in B:
                if a + b in S:
                    ans += S[a + b]

        return ans
