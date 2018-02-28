class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs or not strs[0]:
            return ''

        t = strs[0]
        for i in range(len(t)):
            for s in strs:
                if i >= len(s) or s[i] != t[i]:
                    return t[:i]

        return t
