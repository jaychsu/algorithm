class Solution:
    """
    @param: S: A string
    @param: P: A string includes "?" and "*"
    @return: is Match?
    """
    def isMatch(self, S, P):
        if S is None or P is None:
            return False

        if S is '' and P is '':
            return True

        ANY_CHAR = '?'
        ANY_MULTI_CHAR = '*'
        m, n = len(S), len(P)

        """
        `dp[i][j]` means the substr end at `S[i - 1]` was matched by
        the substr end at `P[j - 1]`
        """
        dp = [[False] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0 and j == 0:
                    dp[i][j] = True
                    continue

                if j == 0:
                    dp[i][j] = False
                    continue

                if P[j - 1] == ANY_MULTI_CHAR:
                    """
                    case 1-1: `dp[i-1][j]` means `*` may start to matched new char
                    => `i-1` in `dp[i-1][j]` means to check the `?` below
                                                            '...a?a'
                                                                 \|
                                                            '...xa*'

                    case 1-2: `dp[i][j-1]` means `*` continue to matched same char
                    => `j-1` in `dp[i][j-1]` means to check the `?` below
                                                            '...aa?'
                                                                 /
                                                            '...xa*'
                    """
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
                    continue

                """
                case 2: `P[j-1]` is `.` and `.` always matched `S[i-1]`
                case 3: `P[j-1]` is `a` and `a` == `P[j-1]` == `S[i-1]`

                => `-1` in `dp[i-1][j-1]` means previous char
                """
                if P[j - 1] == ANY_CHAR and dp[i - 1][j - 1]:
                    dp[i][j] = True
                    continue

                if P[j - 1] == S[i - 1] and dp[i - 1][j - 1]:
                    dp[i][j] = True

        return dp[m][n]
