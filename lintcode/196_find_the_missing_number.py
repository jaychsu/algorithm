class Solution:
    def findMissing(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        ans = n = len(nums)

        for i in range(n):
            ans ^= i ^ nums[i]

        return ans


class Solution:
    def findMissing(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        nums.sort()

        for i in range(len(nums)):
            if i != nums[i]:
                return i

        return i + 1
