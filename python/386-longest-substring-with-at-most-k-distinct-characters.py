class Solution:
    """
    @param: s: A string
    @param: k: An integer
    @return: An integer
    """
    def lengthOfLongestSubstringKDistinct(self, s, k):
        if not s or not k:
            return 0
        ans = l = r = 0
        n, freq = len(s), {}
        while r < n:
            while r < n and (s[r] in freq or len(freq) < k):
                freq[s[r]] = freq.get(s[r], 0) + 1
                r += 1

            # the r here already after the legal char, since `r += 1` in above
            ans = max(ans, r - l)

            while l < r and len(freq) >= k:
                freq[s[l]] -= 1
                if freq[s[l]] == 0:
                    del freq[s[l]]
                l += 1
        return ans
