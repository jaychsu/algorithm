class Solution:
    """
    @param: s: Roman representation
    @return: an integer
    """
    def romanToInt(self, s):
        if not s:
            return 0

        R = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        ans = R[s[-1]]
        for i in range(len(s) - 2, -1, -1):
            if R[s[i]] < R[s[i + 1]]:
                ans -= R[s[i]]
            else:
                ans += R[s[i]]

        return ans
