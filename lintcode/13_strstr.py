class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        NOT_FOUND = -1
        if haystack is None or needle is None:
            return NOT_FOUND
        if haystack == needle:
            return 0

        m, n = len(haystack), len(needle)

        for i in range(m - n + 1):
            if haystack[i:i + n] == needle:
                return i

        return NOT_FOUND
