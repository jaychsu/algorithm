class Solution:
    """
    @param: S: A list of strings
    @return: A list of strings
    """
    def anagrams(self, S):
        ans = []
        if not S:
            return ans

        D = {}
        for s in S:
            _s = ''.join(sorted(s))
            if _s not in D:
                D[_s] = []
            D[_s].append(s)

        for k, S in D.items():
            if len(S) > 1:
                ans.extend(S)

        return ans
