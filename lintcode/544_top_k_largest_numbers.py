from heapq import heappush, heappop


class Solution:
    """
    @param: nums: an integer array
    @param: k: An integer
    @return: the top k largest numbers in array
    """
    def topk(self, nums, k):
        """
        min heap (normal case in heapq, max heap needs to times -1)
        """
        if not nums:
            return

        ans = []
        for num in nums:
            heappush(ans, num)

            if len(ans) > k:
                heappop(ans)

        ans.sort(reverse=True)

        return ans
