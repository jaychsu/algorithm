class Solution:
    """
    @param: A: An integer array
    @return: The length of LIS (longest increasing subsequence)
    """
    def longestIncreasingSubsequence(self, A):
        lis_size = 0
        if not A:
            return lis_size

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

        for end in range(n):
            for start in range(end):
                """
                `F[start] + 1 > F[end]`
                since `F[i]` may be traversed many times,
                so we need to ensure the value is the LIS size
                """
                if A[end] > A[start] and F[start] + 1 > F[end]:
                    F[end] = F[start] + 1
                    # path_start[end] = start
                if F[end] > lis_size:
                    lis_size = F[end]
                    # path_end = end

        # paths = [0] * lis_size
        # for end in range(lis_size - 1, -1, -1):
        #     paths[end] = A[path_end]
        #     path_end = path_start[path_end]
        # print(paths)

        return lis_size
