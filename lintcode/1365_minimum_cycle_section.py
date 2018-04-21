class Solution:
    """
    @param array: an integer array
    @return: the length of the minimum cycle section
    """
    def minimumCycleSection(self, array):
        if not array:
            return 0

        n = len(array)

        for size in range(1, n + 1):
            gotcha = True

            for i in range(size):
                if any(array[i] != array[j] for j in range(i + size, n, size)):
                    gotcha = False

            if gotcha:
                return size

        return n
