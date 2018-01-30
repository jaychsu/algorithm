class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ''

        return ''.join(reversed(list(s)))
