"""
Optimize Space
"""
class Solution:
    """
    @param: A: an integer array
    @param: V: an integer array
    @param: m: an integer
    @return: an integer
    """
    def backPackIII(self, A, V, m):
        if not A or not V or not m:
            return 0

        # `dp[w]` means the maximum value
        # with weight `w`
        dp = [0] * (m + 1)

        _val = 0
        for i in range(len(A)):
            for w in range(A[i], m + 1):
                _val = dp[w - A[i]] + V[i]
                if _val > dp[w]:
                    dp[w] = _val

        return dp[m]


"""
Origin
"""
class Solution:
    """
    @param: A: an integer array
    @param: V: an integer array
    @param: m: an integer
    @return: an integer
    """
    def backPackIII(self, A, V, m):
        if not A or not V or not m:
            return 0

        n = len(A)

        # `dp[i][w]` means the maximum value
        # with weight `w` in the former `i` items
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for w in range(1, m + 1):
                dp[i][w] = dp[i - 1][w]

                if w >= A[i - 1]:
                    dp[i][w] = max(
                        dp[i][w],
                        dp[i][w - A[i - 1]] + V[i - 1]
                    )

        return dp[n][w]
