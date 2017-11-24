class Solution:
    ans = []

    """
    @param: nums: Given the candidate numbers
    @param: target: Given the target number
    @return: All the combinations that sum to target
    """
    def combinationSum2(self, nums, target):
        if not nums:
            return self.ans

        self.dfs(
            sorted(nums),
            target,
            0,
            []
        )

        return self.ans

    def dfs(self, nums, remaining, start, combination):
        if remaining == 0:
            self.ans.append(combination)
            return

        for i in range(start, len(nums)):
            if remaining < nums[i]:
                return

            # to prevent [1', 2, 5] and [1", 2, 5]
            # appear in result at same time
            if i > start \
                    and nums[i] == nums[i - 1]:
                continue

            self.dfs(
                nums,
                remaining - nums[i],
                i + 1,
                combination + [nums[i]]
            )
