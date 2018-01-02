class Solution:
    # @param S, a string
    # @return an integer
    def minCut(self, S):
        if not S:
            return -1

        n = len(S)
        INFINITY = float('inf')
        is_palindrome = self.get_palin_map(S)

        """
        `dp[i]` means the minimum palindrome count
        broken from the substring ended at `i`
        """
        dp = [INFINITY] * (n + 1)
        dp[0] = 0

        for end in range(1, n + 1):
            for start in range(end):
                if (not is_palindrome[start][end - 1] or
                    dp[start] is INFINITY):
                    continue
                if dp[start] + 1 < dp[end]:
                    dp[end] = dp[start] + 1

        return dp[n] - 1

    def get_palin_map(self, S):
        n = len(S)
        is_palindrome = [[False] * n for _ in range(n)]
        is_palindrome[0][0] = True

        for end in range(1, n):
            is_palindrome[end][end] = True

            start = end - 1
            is_palindrome[start][end] = (S[start] == S[end])

        for start in range(n - 1 - 2, -1, -1):
            for end in range(start + 2, n):
                if not is_palindrome[start + 1][end - 1]:
                    continue
                is_palindrome[start][end] = (S[start] == S[end])

        return is_palindrome
