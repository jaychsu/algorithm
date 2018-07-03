class BinaryHeap:
    def __init__(self, iterable=None):
        self.__heap = [0]
        self.__size = 0

        if iterable:
            self.heapify(iterable)

    def __len__(self):
        return self.__size

    def __bool__(self):
        return self.__size > 0

    def heapify(self, iterable):
        if not iterable:
            return

        for val in iterable:
            self.push(val)

    def push(self, val):
        self.__heap.append(val)
        self.__size += 1

        self._siftup(self.__size)

    def pop(self):
        if self.__size < 1:
            raise IndexError('index out of range')

        val = self.__heap[1]
        self.__heap[1] = self.__heap[-1]
        self.__size -= 1

        self.__heap.pop()
        self._siftdown(1)
        return val

    def top(self):
        if self.__size < 1:
            raise IndexError('index out of range')

        return self.__heap[1]

    def _siftup(self, i):
        heap = self.__heap

        while i // 2 > 0:
            j = i // 2

            if heap[i] < heap[j]:
                heap[i], heap[j] = heap[j], heap[i]

            i = j

    def _siftdown(self, i):
        heap = self.__heap
        size = self.__size

        while i * 2 <= size:
            j = i * 2

            if i * 2 + 1 <= size and heap[i * 2 + 1] < heap[i * 2]:
                j = i * 2 + 1

            if heap[i] > heap[j]:
                heap[i], heap[j] = heap[j], heap[i]

            i = j
