import collections


class BinaryHashHeap:
    def __init__(self, iterable=None):
        self.__heap = [0]
        self.__size = 0
        self.__idxs = collections.defaultdict(set)

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
        self.__idxs[val].add(self.__size)

        self._siftup(self.__size)

    def pop(self):
        if self.__size < 1:
            raise IndexError('index out of range')

        val = self.__heap[1]
        self.__idxs[val].discard(1)
        self.__idxs[self.__heap[-1]].discard(self.__size)
        self.__idxs[self.__heap[-1]].add(1)

        self.__heap[1] = self.__heap[-1]
        self.__size -= 1

        self.__heap.pop()
        self._siftdown(1)
        return val

    def remove(self, val):
        if not self.__idxs.get(val):
            raise ValueError('value was not in heap')

        i = self.__idxs[val].pop()
        self.__idxs[self.__heap[-1]].discard(self.__size)
        self.__idxs[self.__heap[-1]].add(i)

        self.__heap[i] = self.__heap[-1]
        self.__size -= 1

        self.__heap.pop()
        self._siftdown(i)

    def top(self):
        if self.__size < 1:
            raise IndexError('index out of range')

        return self.__heap[1]

    def _siftup(self, i):
        heap = self.__heap

        while i // 2 > 0:
            j = i // 2

            if heap[i] < heap[j]:
                self._swap(i, j)

            i = j

    def _siftdown(self, i):
        heap = self.__heap
        size = self.__size

        while i * 2 <= size:
            j = i * 2

            if i * 2 + 1 <= size and heap[i * 2 + 1] < heap[i * 2]:
                j = i * 2 + 1

            if heap[i] > heap[j]:
                self._swap(i, j)

            i = j

    def _swap(self, i, j):
        heap = self.__heap
        idxs = self.__idxs

        idxs[heap[i]].discard(i)
        idxs[heap[j]].discard(j)

        idxs[heap[i]].add(j)
        idxs[heap[j]].add(i)

        heap[i], heap[j] = heap[j], heap[i]
