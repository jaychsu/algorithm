class Solution:
    """
    @param: V: A list of integer
    @return: An integer, maximum coins
    """
    def maxCoins(self, V):
        if not V:
            return 0

        """
        the value of last balloons is `1 * v * 1`
        """
        V = [1] + V + [1]

        n = len(V)

        """
        `dp[i][j]` means the maximum value when
        all the balloons in [i+1, j-1] was bursted
        """
        dp = [[0] * n for _ in range(n)]
        # pi = [[0] * n for _ in range(n)]

        for i in range(n - 1 - 2, -1, -1):
            for j in range(i + 2, n):

                """
                leave last balloon `k` to burst
                `i + 1 <= k <= j - 1`
                """
                for k in range(i + 1, j):
                    dp[i][j] = max(
                        dp[i][j],
                        dp[i][k] + dp[k][j] + V[i] * V[k] * V[j]
                    )
                    # if dp[i][j] == dp[i][k] + dp[k][j] + V[i] * V[k] * V[j]:
                    #     pi[i][j] = k

        # self.print_paths(0, n - 1, V, pi)

        return dp[0][n - 1]

    # def print_paths(self, i, j, V, pi):
    #     if i + 1 == j:
    #         return

    #     self.print_paths(i, pi[i][j], V, pi)
    #     self.print_paths(pi[i][j], j, V, pi)

    #     print("burst {vk}, get coins {vi} * {vk} * {vj} = {vsum}".format(
    #         vi=V[i],
    #         vk=V[pi[i][j]],
    #         vj=V[j],
    #         vsum=V[i] * V[pi[i][j]] * V[j]
    #     ))
