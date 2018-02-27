"""
time: O(n)
space: O(n)
"""
class Solution:
    """
    @param: nums: an array of integers
    @return: the number of unique integers
    """
    def deduplication(self, nums):
        ans = 0
        if not nums:
            return ans

        exists = set()
        for i in range(len(nums)):
            if nums[i] not in exists:
                exists.add(nums[i])
                ans += 1

        return ans


"""
time: O(nlogn)
space: O(1)
"""
class Solution:
    """
    @param: nums: an array of integers
    @return: the number of unique integers
    """
    def deduplication(self, nums):
        ans = 0
        if not nums:
            return ans

        nums.sort()

        # for `nums[0]`
        ans = 1
        for i in range(1, len(nums)):
            if nums[i - 1] != nums[i]:
                nums[ans] = nums[i]
                ans += 1

        return ans
