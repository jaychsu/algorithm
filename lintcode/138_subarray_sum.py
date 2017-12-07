class Solution:
    """
    @param: nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def subarraySum(self, nums):
        """
        len(nums) == 5
        if `A[1] + A[2] + A[3] == 0`
        the cumulative sum in the `i == 3` iteration
        is same as the cumulative sum in `A[0]`

        => save every sum in hashmap
        => if got the same sum in following iteration
        => start = hashmap[sum] + 1, end = i
        """
        if not nums:
            return []

        sum_to_start = {}
        sum_to_start[0] = -1

        _sum = 0
        for i in range(len(nums)):
            _sum += nums[i]

            if _sum in sum_to_start:
                return [
                    sum_to_start[_sum] + 1,
                    i
                ]

            sum_to_start[_sum] = i

        return []
