class Solution:
    """
    @param: A: Given an integer array
    @return: nothing
    """
    def heapify(self, A):
        # start from mid-depth to sift down
        for i in range(len(A) // 2, -1, -1):
            self.siftdown(A, i)

    def siftdown(self, A, i):
        """
        sift down
        1. pick the smaller child to swap
        2. if parent is already small than both children, no need to continue
        3. continue to sift down in next depth
        """
        n = len(A)
        while i * 2 + 1 < n:
            # left child
            _i = i * 2 + 1
            if _i + 1 < n and A[_i + 1] < A[_i]:
                # right child
                _i += 1
            if A[_i] >= A[i]:
                # if its already steady
                break

            A[i], A[_i] = A[_i], A[i]
            i = _i
