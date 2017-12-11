class Solution:
    """
    @param: s: the maximum length of s is 1000
    @return: the longest palindromic subsequence's length
    """
    def longestPalindromeSubseq(self, s):
        if not s:
            return 0

        n = len(s)
        if n == 1:
            return 1

        # `dp[i][j]` means the length of the longest subsequence
        # included in `s[i:j+1]`
        dp = [[0] * n for _ in range(n)]

        ans = 0
        start = end = 0
        for end in range(n):
            dp[end][end] = 1

            if n < 1:
                continue

            start = end - 1
            if s[start] == s[end]:
                dp[start][end] = 2
            else:
                dp[start][end] = 1

        for size in range(3, n + 1):
            for start in range(n - size + 1):
                end = start + size - 1

                dp[start][end] = max(dp[start][end - 1], dp[start + 1][end])

                if s[start] == s[end]:
                    dp[start][end] = max(
                        dp[start][end],
                        dp[start + 1][end - 1] + 2
                    )

                if dp[start][end] > ans:
                    ans = dp[start][end]

        return ans
