class Solution:
    """
    @param: s: A string
    @param: k: An integer
    @return: An integer
    """
    def lengthOfLongestSubstringKDistinct(self, s, k):
        if not s or not k:
            return 0
        n = len(s)
        ans, found = 0, {}
        i = j = 0 # i for right pointer, j for left pointer
        while j < n:

            while j < n \
            and (s[j] in found or len(found) < k):
                found[s[j]] = found.get(s[j], 0) + 1
                j += 1

            ans = max(ans, j - i) # the j here already after the legal char, since `j += 1` in above

            while i < j and len(found) >= k:
                found[s[i]] -= 1
                if found[s[i]] == 0: del found[s[i]]
                i += 1

        return ans
