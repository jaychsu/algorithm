class Solution:
    """
    @param: : string A to be repeated
    @param: : string B
    @return: the minimum number of times A has to be repeated
    """
    def repeatedString(self, A, B):
        if len(B) <= len(A) and B in A:
            return 1
        if not A or not B:
            return -1

        ans = B.count(A)
        S = B.split(A)

        if S[-1] and A.startswith(S[-1]):
            ans += 1

        if S[0] and A.endswith(S[0]):
            ans += 1

        return ans if A.startswith(S[-1]) and A.endswith(S[0]) else -1
