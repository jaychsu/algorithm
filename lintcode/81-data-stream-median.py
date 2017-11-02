from heapq import heappush, heappop

class Solution:
    """
    @param: nums: A list of integers
    @return: the median of numbers
    """
    def medianII(self, nums):
        ans = []
        if not nums or len(nums) < 1:
            return ans
        self.min_heap, self.max_heap = [], []
        for i in range(len(nums)):
            if ans and nums[i] > ans[-1]:
                heappush(self.min_heap, nums[i])
            else:
                heappush(self.max_heap, - nums[i])

            # To compute the median from the dual heap
            self.balance()

            ans.append(self.get_median())
        return ans

    def balance(self):
        l = len(self.max_heap)
        r = len(self.min_heap)
        if abs(r - l) <= 1:
            return
        if r > l:
            heappush(self.max_heap, - heappop(self.min_heap))
        else:
            heappush(self.min_heap, - heappop(self.max_heap))
        self.balance()

    def get_median(self):
        l = len(self.max_heap)
        r = len(self.min_heap)
        if r > l:
            return self.min_heap[0]
        else:
            return - self.max_heap[0]
