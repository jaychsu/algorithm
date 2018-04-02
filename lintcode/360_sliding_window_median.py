import heapq


class HashHeapqWithLazy:
    def __init__(self):
        self.__heap = []
        self.__deleted = {}
        self.__size = 0

    def __len__(self):
        return self.__size

    def __bool__(self):
        return self.__size > 0

    def push(self, val):
        heapq.heappush(self.__heap, val)
        self.__size += 1

    def pop(self):
        if self._is_empty():
            return

        self.__size -= 1
        return heapq.heappop(self.__heap)

    def remove(self, val):
        if self._is_empty():
            return

        self.__size -= 1
        self.__deleted[val] = self.__deleted.get(val, 0) + 1

    def top(self):
        if self._is_empty():
            return

        return self.__heap[0]

    def _is_empty(self):
        while self.__heap and self.__deleted.get(self.__heap[0]):
            val = heapq.heappop(self.__heap)
            self.__deleted[val] -= 1

        return self.__size == 0


class Solution:
    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        ans = []

        if not nums or k <= 0 or len(nums) < k:
            return ans

        self.minheap = HashHeapqWithLazy()
        self.maxheap = HashHeapqWithLazy()

        for i in range(len(nums)):
            # remove nums[i - k]
            if i >= k:
                if self.minheap and nums[i - k] >= self.minheap.top():
                    self.minheap.remove(nums[i - k])
                else:
                    self.maxheap.remove(-1 * nums[i - k])

            # add nums[i]
            if self.minheap and nums[i] >= self.minheap.top():
                self.minheap.push(nums[i])
            else:
                self.maxheap.push(-1 * nums[i])

            # get median
            if i >= k - 1:
                ans.append(self.get_median())

        return ans

    def get_median(self):
        if not self.maxheap and not self.minheap:
            return 0

        while len(self.maxheap) > len(self.minheap) + 1:
            self.minheap.push(-1 * self.maxheap.pop())

        while len(self.minheap) > len(self.maxheap):
            self.maxheap.push(-1 * self.minheap.pop())

        return -1 * self.maxheap.top()
