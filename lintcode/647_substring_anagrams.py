"""
REF: https://leetcode.com/problems/find-all-anagrams-in-a-string/discuss/92007/
"""


class Solution:
    """
    @param: s: a string
    @param: t: a string
    @return: a list of index
    """
    def findAnagrams(self, s, t):
        ans = []
        if not s or not t or len(t) > len(s):
            return ans

        D = {}
        for c in t:
            D[c] = D.get(c, 0) + 1

        n, m = len(s), len(t)
        cnt = len(D)
        left = right = 0

        while right < n:
            if s[right] in D:
                D[s[right]] -= 1
                if D[s[right]] == 0:
                    cnt -= 1

            right += 1

            while cnt == 0:
                if s[left] in D:
                    D[s[left]] += 1
                    if D[s[left]] > 0:
                        cnt += 1

                if right - left == m:
                    ans.append(left)

                left += 1

        return ans
