import collections


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0

        if not s:
            return ans

        freqs = collections.defaultdict(int)
        i = rep = 0

        for j in range(len(s)):
            if freqs[s[j]] == 1:
                rep += 1
            freqs[s[j]] += 1

            while rep > 0:
                freqs[s[i]] -= 1
                if freqs[s[i]] == 1:
                    rep -= 1

                i += 1

            ans = max(ans, j - i + 1)

        return ans
