class Solution:
    def dominantIndex(self, A):
        """
        :type A: List[int]
        :rtype: int
        """

        _max = __max = float('-inf')
        _max_i = -1

        for i in range(len(A)):
            if A[i] > _max:
                __max = _max
                _max = A[i]
                _max_i = i
                continue

            if A[i] > __max:
                __max = A[i]

        if _max >= __max * 2:
            return _max_i

        return -1
