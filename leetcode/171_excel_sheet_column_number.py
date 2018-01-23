class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        s = s.upper()

        ans = 0
        BASE = ord('A') - 1

        for char in s:
            ans = ans * 26 + ord(char) - BASE

        return ans
