class Solution:
    ans = []

    """
    @param: nums: A list of integers.
    @return: A list of permutations.
    """
    def permute(self, nums):
        if nums is None:
            return self.ans
        if len(nums) is 0:
            self.ans.append([])
            return self.ans

        self.dfs(nums, [])

        return self.ans

    def dfs(self, nums, permutation):
        n = len(nums)
        if len(permutation) >= n:
            self.ans.append(permutation)
            return

        for i in range(n):
            if nums[i] in permutation:
                continue
            self.dfs(nums, permutation + [nums[i]])
