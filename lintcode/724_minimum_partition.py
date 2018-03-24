class Solution:
    def findMin(self, nums):
        """
        :type nums: list[int]
        :rtype: int
        """
        if not nums:
            return 0

        target = sum(nums)
        dp = [False] * (target + 1)
        dp[0] = True

        ans = float('inf')

        for num in nums:
            for i in range(target, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]

                if dp[i]:
                    ans = min(
                        ans,
                        abs(target - i * 2)
                    )

        return ans
