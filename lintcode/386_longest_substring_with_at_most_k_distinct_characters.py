import collections


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        ans = 0

        if not s or not k:
            return ans

        freq = collections.defaultdict(int)
        n = len(s)
        left = right = cnt = 0

        while right < n:
            freq[s[right]] += 1
            if freq[s[right]] == 1:
                cnt += 1

            right += 1

            while cnt > k:
                freq[s[left]] -= 1
                if freq[s[left]] == 0:
                    cnt -= 1

                left += 1

            if right - left > ans:
                ans = right - left

        return ans
