class Solution:
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        ans = 0
        if not s:
            return ans

        n = len(s)
        _F = dict.fromkeys(s, 0)

        for m in range(1, len(_F) + 1):
            F = _F.copy()
            left = right = 0
            kind = valid = 0

            while right < n:
                if kind <= m:
                    F[s[right]] += 1
                    if F[s[right]] == 1:
                        kind += 1
                    if F[s[right]] == k:
                        valid += 1

                    right += 1
                else:
                    if F[s[left]] == 1:
                        kind -= 1
                    if F[s[left]] == k:
                        valid -= 1
                    F[s[left]] -= 1

                    left += 1

                if kind == valid == m and right - left > ans:
                    ans = right - left

        return ans
