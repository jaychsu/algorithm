from heapq import heappush, heappop

class HashHeap:
    def __init__(self):
        self.heap = []
        self.deleted = {}
        self._len = 0

    def push(self, val):
        heappush(self.heap, val)
        self._len += 1

    def pop(self):
        self._clean_top()
        self._len -= 1
        return heappop(self.heap)

    def remove(self, val):
        self.deleted[val] = self.deleted.get(val, 0) + 1
        self._len -= 1

    def top(self):
        self._clean_top()
        return self.heap[0]

    def _clean_top(self):
        while self.heap and self.deleted.get(self.heap[0]):
            self.deleted[self.heap[0]] -= 1
            heappop(self.heap)

    def __len__(self):
        return self._len

    def __repr__(self):
        return repr(self.heap)

class Solution:
    """
    @param: nums: A list of integers
    @param: k: An integer
    @return: The maximum number inside the window at each moving
    """
    def maxSlidingWindow(self, nums, k):
        ans = []
        if not nums or len(nums) < 1 or not k:
            return ans
        self.hashheap = HashHeap()
        for r in range(len(nums)):
            self.hashheap.push(- nums[r])
            if r >= k:
                self.hashheap.remove(- nums[r - k])
            if r + 1 >= k:
                ans.append(- self.hashheap.top())
        return ans


'''
Failed Solution
Since its a O(n*k) solution
'''
class Solution:
    """
    @param: nums: A list of integers
    @param: k: An integer
    @return: The maximum number inside the window at each moving
    """
    def maxSlidingWindow(self, nums, k):
        ans = []
        if not nums or len(nums) < 1:
            return ans
        for r in range(len(nums)):
            if r >= k - 1:
                ans.append(max(nums[r - k + 1 : r + 1]))
        return ans
