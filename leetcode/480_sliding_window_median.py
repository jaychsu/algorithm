import heapq


class HashHeapq:
    def __init__(self):
        self.__heap = []
        self.__deleted = {}
        self.__size = 0

    def __len__(self):
        return self.__size

    def __bool__(self):
        return not self.is_empty()

    def push(self, val):
        heapq.heappush(self.__heap, val)
        self.__size += 1

    def pop(self):
        if self.is_empty():
            return

        self.__size -= 1
        return heapq.heappop(self.__heap)

    def remove(self, val):
        if self.is_empty():
            return

        self.__size -= 1
        self.__deleted[val] = self.__deleted.get(val, 0) + 1

    def top(self):
        if self.is_empty():
            return

        return self.__heap[0]

    def is_empty(self):
        while self.__size and self.__deleted.get(self.__heap[0]):
            val = heapq.heappop(self.__heap)
            self.__deleted[val] -= 1

        return not self.__heap


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

        self.minheap = HashHeapq()
        self.maxheap = HashHeapq()

        for i in range(len(nums)):
            # remove nums[i - k]
            if i >= k:
                if self.minheap and nums[i - k] < self.minheap.top():
                    self.maxheap.remove(- nums[i - k])
                else:
                    self.minheap.remove(nums[i - k])

            # add nums[i]
            if self.minheap and nums[i] < self.minheap.top():
                self.maxheap.push(- nums[i])
            else:
                self.minheap.push(nums[i])

            # get median
            if i >= k - 1:
                ans.append(self.get_median())

        return ans

    def get_median(self):
        if not self.minheap:
            return 0.0

        while len(self.minheap) > len(self.maxheap) + 1:
            self.maxheap.push(- self.minheap.pop())

        while len(self.maxheap) > len(self.minheap):
            self.minheap.push(- self.maxheap.pop())

        if len(self.minheap) > len(self.maxheap):
            return self.minheap.top() * 1.0

        return (self.minheap.top() - self.maxheap.top()) / 2.0
