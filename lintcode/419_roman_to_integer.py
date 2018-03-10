class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        symb = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        ans = symb[s[-1]]

        for i in range(len(s) - 2, -1, -1):
            if symb[s[i]] < symb[s[i + 1]]:
                ans -= symb[s[i]]
            else:
                ans += symb[s[i]]

        return ans
