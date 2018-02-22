class Solution:
    """
    @param s: a message being encoded
    @return: an integer
    """
    def numDecodings(self, s):
        if not s or s == '0':
            return 0

        n = len(s)
        MOD = 10 ** 9 + 7

        dp = [0] * (n + 1)
        dp[0] = 1

        if s[0] == '*':
            dp[1] = 9  # 9 * dp[0]
        elif s[0] != '0':
            dp[1] = 1  # dp[0]

        for i in range(2, n + 1):
            if s[i - 1] == '*':
                dp[i] += 9 * dp[i - 1]

                if s[i - 2] == '*':
                    dp[i] += 15 * dp[i - 2]
                elif s[i - 2] == '1':
                    dp[i] += 9 * dp[i - 2]
                elif s[i - 2] == '2':
                    dp[i] += 6 * dp[i - 2]

                dp[i] %= MOD
                continue

            if s[i - 1] != '0':
                dp[i] += dp[i - 1]

            if s[i - 2] == '*':
                if int(s[i - 1]) <= 6:
                    dp[i] += 2 * dp[i - 2]
                else:
                    dp[i] += dp[i - 2]
            elif 10 <= int(s[i - 2:i]) <= 26:
                dp[i] += dp[i - 2]

            dp[i] %= MOD

        return dp[n]
