class Solution:
    ans = [[]]

    """
    @param: nums: A set of numbers.
    @return: A list of lists. All valid subsets.
    """
    def subsetsWithDup(self, nums):
        if not nums:
            return self.ans

        self.dfs(sorted(nums), 0, [])

        return self.ans

    def dfs(self, nums, start, combination):
        n = len(nums)
        if start >= n:
            return

        for i in range(start, n):
            # to prevent [1, 2'] and [1, 2"]
            # appear in result at same time
            if i > start \
                    and nums[i] == nums[i - 1]:
                continue
            _combination = combination + [nums[i]]
            self.ans.append(_combination)
            self.dfs(nums, i + 1, _combination)
