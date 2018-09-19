import collections


class BinaryHashHeap:
    MSG_EMPTY_HEAP = 'access element from empty heap'

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
        if not isinstance(iterable, collections.Iterable):
            return

        for val in iterable:
            self.push(val)

    def push(self, val):
        self.__heap.append(val)
        self.__size += 1
        self.__idxs[val].add(self.__size)

        self._siftdown(self.__size)

    def pop(self):
        if self.__size < 1:
            raise IndexError(self.MSG_EMPTY_HEAP)

        heap = self.__heap
        idxs = self.__idxs

        val = heap[1]
        idxs[val].discard(1)
        idxs[heap[-1]].discard(self.__size)
        idxs[heap[-1]].add(1)

        heap[1] = heap[-1]
        heap.pop()

        self.__size -= 1
        self._siftup(1)
        return val

    def remove(self, val):
        if not self.__idxs.get(val):
            raise KeyError(val)

        heap = self.__heap
        idxs = self.__idxs

        i = idxs[val].pop()
        idxs[heap[-1]].discard(self.__size)
        idxs[heap[-1]].add(i)

        heap[i] = heap[-1]
        heap.pop()

        self.__size -= 1
        self._siftup(i)

    def top(self):
        if self.__size < 1:
            raise IndexError(self.MSG_EMPTY_HEAP)

        return self.__heap[1]

    def _siftdown(self, i):
        heap = self.__heap

        while i // 2 > 0:
            j = i // 2

            if heap[i] < heap[j]:
                self._swap(i, j)

            i = j

    def _siftup(self, i):
        heap = self.__heap
        size = self.__size

        while i * 2 <= size:
            j = i * 2

            if j + 1 <= size and heap[j + 1] < heap[j]:
                j += 1

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
