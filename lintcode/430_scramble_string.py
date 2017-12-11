class Solution:
    """
    @param: s1: A string
    @param: s2: Another string
    @return: whether s2 is a scrambled string of s1
    """
    def isScramble(self, s1, s2):
        if not s1 or not s2 or len(s1) != len(s2):
            return False

        n = len(s1)

        """
        `dp[i][j][k]` means the substring in `s1` (start: `i`, len: `k`)
        could be transformed into the substring in `s2` (start: `j`, len: `k`)
        """
        dp = [[[False] * (n + 1) for _ in range(n)] for _ in range(n)]

        for i in range(n):
            for j in range(n):
                dp[i][j][1] = (s1[i] == s2[j])

        for k in range(2, n + 1):

            for i in range(n):
                """
                allow: i < n - k + 1 => i <= n - k
                disallow: i > n - k
                """
                if i + k > n:
                    continue

                for j in range(n):
                    if j + k > n:
                        continue

                    for l in range(1, k):
                        """
                        If its already calculated and possible to transform
                        """
                        if dp[i][j][k]:
                            continue

                        """
                        * u1, u2: substring in s1
                        * v1, v2: substring in s2
                        * `l` == len(u1) == len(v1)
                        * `k - l` == len(u2) == len(v2)

                        case1: u1 -> v1, u2 -> v2
                        `(dp[i][j][l] and dp[i + l][j + l][k - l])`
                        - `dp[i][j][l]` means its possible to u1 -> v1
                        - `dp[i + l][j + l][k - l]` => u2 -> v2

                                   u1              u2
                        s1: |`i`---`l`--->|`i+l`---`k-l`--->|
                                   v1              v2
                        s2: |`j`---`l`--->|`j+l`---`k-l`--->|

                        case2: u1 -> v2, u2 -> v1
                        `(dp[i][j + k - l][l] and dp[i + l][j][k - l])`
                        - `dp[i][j + k - l][l]` => u1 -> v2
                        - `dp[i + l][j][k - l]` => u2 -> v1

                                   u1              u2
                        s1: |`i`---`l`--->|`i+l`---`k-l`--->|
                                   v1              v2
                        s2: |`j`---`k-l`--->|`j+k-l`--`l`-->|
                        """
                        if dp[i][j][l] and dp[i + l][j + l][k - l]:
                            dp[i][j][k] = True
                            continue

                        if dp[i][j + k - l][l] and dp[i + l][j][k - l]:
                            dp[i][j][k] = True

        return dp[0][0][n]
