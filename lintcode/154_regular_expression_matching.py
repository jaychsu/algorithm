"""
Main Concept:

end by '*' and has no matched
case 1-1: `P[j-2:j]` is `c*` and have no matched in `S`
=> `j-2` in `dp[i][j-2]` means ignored `c` and `*`

end by `*` and is the last matched in `*`
case 1-2: `P[j-2:j]` is `.*` and `.` always matched `S[i-1]`
case 1-3: `P[j-2:j]` is `a*` and `a` == `P[j-2]` == `S[i-1]`
=> `i-1` in `dp[i-1][j]` means to check the `?` below
    '...a?a'
         \|
    '...xa*'

case 2: `P[j-1]` is `.` and `.` always matched `S[i-1]`
case 3: `P[j-1]` is `a` and `a` == `P[j-1]` == `S[i-1]`
=> `-1` in `dp[i-1][j-1]` means previous char
"""


class Solution:
    def isMatch(self, s, p):
        """
        :type s: str, target string
        :type p: str, regex
        :rtype: bool
        """
        if s is None or p is None:
            return False
        if s == '' and p == '':
            return True

        MULTI = '*'
        ANY = '.'
        m, n = len(s), len(p)

        """
        `dp[i][j]` means the substr end at `s[i - 1]` was matched by
        the substr end at `p[j - 1]`
        """
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True
        # dp[i][0] = False
        # dp[0][j] -> need to check

        for i in range(m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == MULTI:
                    if dp[i][j - 2]:
                        dp[i][j] = True
                    elif p[j - 2] == ANY and dp[i - 1][j]:
                        dp[i][j] = True
                    elif p[j - 2] == s[i - 1] and dp[i - 1][j]:
                        dp[i][j] = True
                elif p[j - 1] == ANY and dp[i - 1][j - 1]:
                    dp[i][j] = True
                elif p[j - 1] == s[i - 1] and dp[i - 1][j - 1]:
                    dp[i][j] = True

        return dp[m][n]
