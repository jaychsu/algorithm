"""
Test Case:

[3,3,0,3]
"""

"""
Directly pass `nums` but without `nums[i]`
"""
class Solution:
    ans = []

    """
    @param: :  A list of integers
    @return: A list of unique permutations
    """
    def permuteUnique(self, nums):
        if nums is None:
            return self.ans
        if len(nums) is 0:
            self.ans.append([])
            return self.ans

        self.dfs(sorted(nums), [])

        return self.ans

    def dfs(self, nums, permutation):
        if not nums:
            self.ans.append(permutation)
            return
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            self.dfs(
                nums[:i] + nums[i + 1:],
                permutation + [nums[i]]
            )

"""
Record visited index
"""
class Solution:
    ans = []

    """
    @param: :  A list of integers
    @return: A list of unique permutations
    """
    def permuteUnique(self, nums):
        if nums is None:
            return self.ans
        if len(nums) is 0:
            self.ans.append([])
            return self.ans

        visited = [False] * len(nums)
        self.dfs(sorted(nums), [], visited)

        return self.ans

    def dfs(self, nums, permutation, visited):
        n = len(nums)
        if len(permutation) == n:
            self.ans.append(permutation)
            return
        for i in range(n):
            if visited[i]:
                continue

            """
            example: [0, 3, 3', 3"]
            if current iteration is `3"`
            we need to ensure `3`, `3'` is picked
            otherwise repeated result will be included
            """
            if i > 0 and not visited[i - 1] \
                    and nums[i] == nums[i - 1]:
                continue

            visited[i] = True
            self.dfs(
                nums,
                permutation + [nums[i]],
                visited
            )
            visited[i] = False
