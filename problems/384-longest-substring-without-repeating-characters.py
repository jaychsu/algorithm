class Solution:
    """
    @param: s: a string
    @return: an integer
    """
    def lengthOfLongestSubstring(self, s):
        if not s:
            return 0
        n, last = len(s), {}
        ans = l = 0
        for r in range(n):
            # If find the repeated one and position great than before, set the valid left index
            if s[r] in last and last[s[r]] + 1 > l: l = last[s[r]] + 1

            # Record the last time index of each character
            last[s[r]] = r

            # Every time if the interval between left and right is the bigger one, that's answer
            ans = max(ans, r + 1 - l)
        return ans
