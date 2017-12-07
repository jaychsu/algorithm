from collections import namedtuple

Pair = namedtuple('Pair', ['sum', 'index'])

class Solution:
    """
    @param: nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def subarraySumClosest(self, nums):
        """
        Prefix Sum
        prefix_sum[i] means the culmulative sum before `i + 1` in `nums`
        => if we want to know the sum of [1, 2]
        => sum(nums[1:3]) == sum(nums[0:3]) - sum(nums[0:0])
        """
        ans = [0] * 2
        if not nums:
            return ans

        n = len(nums)
        if n == 1:
            return ans

        prefix_sum = [0] * n

        prefix_sum[0] = Pair(nums[0], 0)
        for i in range(1, n):
            prefix_sum[i] = Pair(prefix_sum[i - 1].sum + nums[i], i)

        # since the closest sum occurred when the sum is closest
        # so we can simply calculate the difference
        # between every two adjacent indexes
        prefix_sum.sort(key=lambda p: p.sum)

        closest_sum = float('inf')
        tmp_sum = 0
        for i in range(1, n):
            # calculate all the closest sum occurred in two adjacent indexes
            tmp_sum = prefix_sum[i].sum - prefix_sum[i - 1].sum

            # keep finding the minimum closest sum
            if tmp_sum >= closest_sum:
                continue

            closest_sum = tmp_sum
            ans = sorted([prefix_sum[i].index, prefix_sum[i - 1].index])

        # sum(nums[1:3]) == sum(nums[0:3]) - sum(nums[0:0])
        # so start need `+1`
        ans[0] += 1
        return ans
