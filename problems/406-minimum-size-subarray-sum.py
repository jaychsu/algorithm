class Solution:
    """
    @param: nums: an array of integers
    @param: s: An integer
    @return: an integer representing the minimum size of subarray
    """
    def minimumSize(self, nums, s):
        if not nums or len(nums) == 0:
            return -1
        n = len(nums)
        min_len = n + 1
        l = r = t = 0
        while r < n:
            # Keep adding the next int into total until total >= s
            while r < n and t < s:
                t += nums[r]
                r += 1

            # Terminate iteration if all the children in nums have been added
            if r >= n and t < s:
                break

            # Keep substracting the prev int from total until total < s
            while l < r and t >= s:
                t -= nums[l]
                l += 1

            # Save the min_size
            min_len = min(min_len, r - l + 1)
        return -1 if min_len > n else min_len
