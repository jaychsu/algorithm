"""
REF: https://leetcode.com/problems/find-all-anagrams-in-a-string/discuss/92007/
"""


class Solution:
    def findAnagrams(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: List[int]
        """
        ans = []
        if not s or not t or len(t) > len(s):
            return ans

        F = {}
        for c in t:
            F[c] = F.get(c, 0) + 1

        n, m, cnt = len(s), len(t), len(F)
        left = right = 0

        while right < n:
            if s[right] in F:
                F[s[right]] -= 1
                if F[s[right]] == 0:
                    cnt -= 1

            right += 1

            while cnt == 0:
                if s[left] in F:
                    F[s[left]] += 1
                    if F[s[left]] == 1:
                        cnt += 1

                if right - left == m:
                    ans.append(left)

                left += 1

        return ans
