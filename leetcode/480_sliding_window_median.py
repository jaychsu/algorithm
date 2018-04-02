import heapq


class HashHeapq:
    def __init__(self):
        self.__heap = []

    def __repr__(self):
        return repr(self.__heap)

    def __len__(self):
        return len(self.__heap)

    def __bool__(self):
        return bool(self.__heap)

    def push(self, val):
        heapq.heappush(self.__heap, val)

    def pop(self):
        if not self.__heap:
            return

        return heapq.heappop(self.__heap)

    def remove(self, val):
        if not self.__heap:
            return

        i = 0
        n = len(self.__heap)

        while i < n and self.__heap[i] != val:
            i += 1

        if i == n:
            return

        if i == n - 1:
            self.__heap.pop()
        else:
            self.__heap[i] = self.__heap[-1]
            self.__heap.pop()
            heapq._siftup(self.__heap, i)
            heapq._siftdown(self.__heap, 0, i)

    def top(self):
        if not self.__heap:
            return

        return self.__heap[0]


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
                if self.minheap and nums[i - k] >= self.minheap.top():
                    self.minheap.remove(nums[i - k])
                else:
                    self.maxheap.remove(- nums[i - k])

            # add nums[i]
            if self.minheap and nums[i] >= self.minheap.top():
                self.minheap.push(nums[i])
            else:
                self.maxheap.push(- nums[i])

            # get median
            if i >= k - 1:
                ans.append(self.get_median())

        return ans

    def get_median(self):
        if not self.minheap and not self.maxheap:
            return 0.0

        while len(self.minheap) > len(self.maxheap) + 1:
            self.maxheap.push(- self.minheap.pop())

        while len(self.maxheap) > len(self.minheap):
            self.minheap.push(- self.maxheap.pop())

        if len(self.minheap) > len(self.maxheap):
            return self.minheap.top() * 1.0

        return (self.minheap.top() - self.maxheap.top()) / 2.0
