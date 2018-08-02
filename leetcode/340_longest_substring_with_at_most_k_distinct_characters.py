"""
- count chars: minimum length: `while cnt == k` to reduce window size if possible
- count chars: maximum length: `while cnt > k` to record the maximum window size
"""


import collections


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        ans = 0

        if not s or not k or k < 0:
            return ans

        freqs = collections.defaultdict(int)
        i = cnt = 0

        for j in range(len(s)):
            freqs[s[j]] += 1
            if freqs[s[j]] == 1:
                cnt += 1

            while cnt > k:
                freqs[s[i]] -= 1
                if freqs[s[i]] == 0:
                    cnt -= 1

                i += 1

            ans = max(ans, j - i + 1)

        return ans
