class Solution:
    """
    @param: n: An integer
    @return: A boolean which equals to true if the first player will win
    """
    def firstWillWin(self, n):
        if not n:
            return False
        if n < 2:
            return True

        # `dp[i]` means first play will win if left `i` stones in line
        dp = [False] * n

        dp[0] = dp[1] = True

        for i in range(2, n):
            """
            `dp[i]` =
            True,  if dp[i - 1] == False and dp[i - 2] == False
            True,  if dp[i - 1] == True  and dp[i - 2] == False
            True,  if dp[i - 1] == False and dp[i - 2] == True

            False, if dp[i - 1] == True  and dp[i - 2] == True
            => dp[i - 1] == False or dp[i - 2] == False
            """
            dp[i] = (
                dp[i - 1] == False
                or dp[i - 2] == False
            )

        return dp[n - 1]
