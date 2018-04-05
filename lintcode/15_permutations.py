class Solution:
    def permute(self, nums):
        """
        :type nums: list[int]
        :rtype: list[list[int]]
        """
        if not nums:
            return [[]]

        ans = []

        nums.sort()
        self.dfs(nums, ans, [])

        return ans

    def dfs(self, nums, ans, path):
        if not nums:
            ans.append(path[:])
            return

        for i in range(len(nums)):
            path.append(nums[i])
            self.dfs(nums[:i] + nums[i + 1:], ans, path)
            path.pop()
