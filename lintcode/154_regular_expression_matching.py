class Solution:
    """
    @param S: A string
    @param P: A string includes "." and "*"
    @return: A boolean
    """
    def isMatch(self, S, P):
        if S is None or P is None:
            return False

        if S is '' and P is '':
            return True

        MULTI_CHAR = '*'
        ANY_CHAR = '.'
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

                if P[j - 1] == MULTI_CHAR:
                    """
                    end by '*' and has no matched

                    case 1-1: `P[j-2:j]` is `c*` and have no matched in `S`

                    => `j-2` in `dp[i][j-2]` means ignored `c` and `*`
                    """
                    if dp[i][j - 2]:
                        dp[i][j] = True

                    """
                    end by `*` and is the last matched in `*`

                    case 1-2: `P[j-2:j]` is `.*` and `.` always matched `S[i-1]`
                    case 1-3: `P[j-2:j]` is `a*` and `a` == `P[j-2]` == `S[i-1]`

                    => `i-1` in `dp[i-1][j]` means to check the `?` below
                                                            '...a?a'
                                                                 \|
                                                            '...xa*'
                    """
                    if P[j - 2] == ANY_CHAR and dp[i - 1][j]:
                        dp[i][j] = True

                    if P[j - 2] == S[i - 1] and dp[i - 1][j]:
                        dp[i][j] = True
                    continue

                """
                case 2: `P[j-1]` is `.` and `.` always matched `S[i-1]`
                case 3: `P[j-1]` is `a` and `a` == `P[j-1]` == `S[i-1]`

                => `-1` in `dp[i-1][j-1]` means previous char
                """
                if P[j - 1] == ANY_CHAR and dp[i - 1][j - 1]:
                    dp[i][j] = True

                if P[j - 1] == S[i - 1] and dp[i - 1][j - 1]:
                    dp[i][j] = True

        return dp[m][n]
