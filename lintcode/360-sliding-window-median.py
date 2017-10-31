from heapq import heappush, heappop

class Heap:
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
    @return: The median of the element inside the window at each moving
    """
    """
    Assuming nums = [1,2,7,8,5]
    i | max_heap |m| min_heap
    =============|=|=========
    0 |          |1|
    1 |          |1| 2
    2 |        1 |2| 7
    3 |    -1- 2 |7| 8
    4 |    -2- 5 |7| 8
    """
    def medianSlidingWindow(self, nums, k):
        ans = []
        if not nums or len(nums) < 1 or k <= 0:
            return ans
        self.min_heap = Heap()
        self.max_heap = Heap()

        for i in range(len(nums)):
            if i >= k:
                if len(self.min_heap) and nums[i - k] >= self.min_heap.top():
                    self.min_heap.remove(nums[i - k])
                else:
                    self.max_heap.remove(- nums[i - k])

            if len(self.min_heap) and nums[i] > self.min_heap.top():
                self.min_heap.push(nums[i])
            else:
                self.max_heap.push(- nums[i])

            self.balance()

            if i + 1 >= k:
                ans.append(self.get_median())

        return ans

    def balance(self):
        l = len(self.max_heap)
        r = len(self.min_heap)
        if abs(r - l) <= 1:
            return
        if r > l:
            self.max_heap.push(- self.min_heap.pop())
        else:
            self.min_heap.push(- self.max_heap.pop())
        self.balance()

    def get_median(self):
        l = len(self.max_heap)
        r = len(self.min_heap)
        if r > l:
            return self.min_heap.top()
        else:
            return - self.max_heap.top()
