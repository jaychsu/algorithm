class Solution:
    is_palindrome = None

    # @param s, a string
    # @return an integer
    def minCut(self, s):
        if not s:
            return 0

        n = len(s)
        INFINITY = float('inf')

        self.check_palindrome(s)

        # `dp[i]` means the palindrome partitioning of `s[0:i-1]`
        dp = [INFINITY] * (n + 1)
        dp[0] = 0

        for end in range(1, n + 1):
            for start in range(end):
                if (not self.is_palindrome[start][end - 1]
                    or dp[start] is INFINITY):
                    continue
                dp[end] = min(dp[end], dp[start] + 1)

        # since `cuts = partitions - 1`
        return dp[n] - 1

    def check_palindrome(self, s):
        n = len(s)
        self.is_palindrome = [[False] * n for _ in range(n)]
        start = end = 0

        for end in range(n):
            self.is_palindrome[end][end] = True

            if end > 0:
                start = end - 1
                self.is_palindrome[start][end] = (
                    s[start] == s[end]
                )

        for start in range(n - 1 - 2, -1, -1):
            for end in range(start + 2, n):
                self.is_palindrome[start][end] = (
                    self.is_palindrome[start + 1][end - 1]
                    and s[start] == s[end]
                )
