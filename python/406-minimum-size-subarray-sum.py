class Solution:
    """
    @param: nums: an array of integers
    @param: s: An integer
    @return: an integer representing the minimum size of subarray
    """
    def minimumSize(self, nums, s):
        n = len(nums)
        if n == 0:
            return -1
        left = right = total = 0
        min_size = n + 1
        while right < n:

            # Keep adding the next int into total until total >= s
            while right < n and total < s:
                total += nums[right]
                right += 1

            # Terminate iteration if all the children in nums have been added
            if total < s:
                break

            # Keep substracting the prev int from total until total < s
            while left < right and total >= s:
                total -= nums[left]
                left += 1

            # Save the min_size
            min_size = min(min_size, right + 1 - left)
        return -1 if min_size > n else min_size
