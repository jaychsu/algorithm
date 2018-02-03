class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        if not s:
            return ans

        n = len(s)
        F = {}  # frequency for every char between `left`, `right`
        rep = 0  # contained repeated char between `left`, `right`

        left = right = 0
        while right < n:
            F[s[right]] = F.get(s[right], 0) + 1
            if F[s[right]] == 2:
                rep += 1
            right += 1

            while rep > 0:
                if F[s[left]] == 2:
                    rep -= 1
                F[s[left]] -= 1
                left += 1

            if right - left > ans:
                ans = right - left

        return ans
