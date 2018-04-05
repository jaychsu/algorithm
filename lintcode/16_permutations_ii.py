class Solution:
    """
    dfs with ignoring self and same num
    """
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
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
            """
            ignore same num
            """
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            """
            ignore self
            """
            path.append(nums[i])
            self.dfs(nums[:i] + nums[i + 1:], ans, path)
            path.pop()


class Solution:
    """
    dfs with visited indices
    """
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        if not nums:
            return [[]]

        ans = []
        visited = [False] * len(nums)

        nums.sort()
        self.dfs(nums, visited, ans, [])

        return ans

    def dfs(self, nums, visited, ans, path):
        if len(path) == len(nums):
            ans.append(path[:])
            return

        for i in range(len(nums)):
            if visited[i]:
                continue

            """
            example: [0, 3, 3', 3"]
            if current iteration is `3"`
            we need to ensure `3`, `3'` is picked
            otherwise repeated result will be included
            """
            if i > 0 and not visited[i - 1] and nums[i] == nums[i - 1]:
                continue

            visited[i] = True
            path.append(nums[i])
            self.dfs(nums, visited, ans, path)
            visited[i] = False
            path.pop()
