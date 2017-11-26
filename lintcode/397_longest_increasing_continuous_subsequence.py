"""
DP + print path
remove the single line comment to see the path in result
"""
class Solution:
    """
    @param: A: An array of Integer
    @return: an integer
    """
    def longestIncreasingContinuousSubsequence(self, A):
        if not A:
            return 0

        return max(
            self.get_lics_size(A),
            self.get_lics_size(list(reversed(A)))
        )

    def get_lics_size(self, A):
        lics_size = 0
        n = len(A)

        """
        `F[i]` means the size of LICS end at `F[i]`
        note that there is size, so init with `1`
        """
        F = [1] * n

        """
        path
        `path_start` means the previous index if `A[i]` is included in the LICS
        `path_end` means the path end index
        """
        # path_start = [-1] * n
        # path_end = 0

        for i in range(n):
            if i > 0 and A[i] > A[i - 1]:
                F[i] = F[i - 1] + 1
                # path_start[i] = i - 1
            if F[i] > lics_size:
                lics_size = F[i]
                # path_end = i

        # paths = [0] * lics_size
        # for i in range(lics_size - 1, -1, -1):
        #     paths[i] = A[path_end]
        #     path_end = path_start[path_end]
        # print(paths)

        return lics_size


"""
Optimized
"""
class Solution:
    """
    @param: A: An array of Integer
    @return: an integer
    """
    def longestIncreasingContinuousSubsequence(self, A):
        if not A:
            return 0

        return max(
            self.get_lics_size(A),
            self.get_lics_size(list(reversed(A)))
        )

    def get_lics_size(self, A):
        lics_size = size = 1

        for i in range(len(A)):
            if i > 0 and A[i] > A[i - 1]:
                size += 1
            else:
                size = 1
            if size > lics_size:
                lics_size = size

        return lics_size
