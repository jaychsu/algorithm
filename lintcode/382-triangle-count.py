class Solution:
    """
    @param: S: A list of integers
    @return: An integer
    """
    def triangleCount(self, S):
        if not S \
        or len(S) < 3:
            return 0
        ans, n = 0, len(S)
        l = m = 0 # left, middle
        S.sort()
        for r in range(2, n):
            l, m = 0, r - 1
            while l < m:
                # if S[l] + S[m] > S[r], then S[l] ~ S[m-1] are meet the demands.
                if S[l] + S[m] > S[r]:
                    ans += m - l # m-1 - l + 1 = m - l
                    m -= 1
                else:
                    l += 1
        return ans
