"""
DP:
time: O(n^2)
space: O(n)
"""
class Solution:
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False

        n = len(nums)
        dp = [0] * n

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                dp[j] = max(
                    nums[i] - dp[j],
                    nums[j] - dp[j - 1]
                )

        return dp[n - 1] >= 0


"""
DP:
time: O(n^2)
space: O(n^2)
"""
class Solution:
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False

        n = len(nums)
        dp = [[0] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                dp[i][j] = max(
                    nums[i] - dp[i + 1][j],
                    nums[j] - dp[i][j - 1]
                )

        return dp[0][n - 1] >= 0
