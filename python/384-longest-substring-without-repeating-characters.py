class Solution:
    """
    @param: s: a string
    @return: an integer
    """
    def lengthOfLongestSubstring(self, s):
        if not s:
            return 0
        ans = left = 0
        last = {}
        for i in range(len(s)):
            if s[i] in last and last[s[i]] + 1 > left:
                left = last[s[i]] + 1
            last[s[i]] = i
            ans = max(ans, i + 1 - left)
        return ans
