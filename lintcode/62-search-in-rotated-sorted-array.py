class Solution:
    """
    @param: A: an integer rotated sorted array
    @param: target: an integer to be searched
    @return: an integer
    """
    """
    for a given A:
        [ 4, 5, 6, 7, 0, 1, 2 ]
          l        M  m     r

    if the `mid` > `l`, then `mid` must be in left side, otherwise in right side

    if `mid` in left side, we can check if the `target` between `l` and `mid`
    (because we dont know the `M` at where)

    otherwise the `mid` in right side, we can also check if the `target` between `mid` and `r`
    (same reason, we dont know the `m` at where)
    """
    def search(self, A, target):
        if not A:
            return -1

        l, m, r = 0, 0, len(A) - 1
        while l + 1 < r:
            m = l + (r - l) // 2
            if A[m] == target:
                return m

            # in the left side in array
            if A[m] > A[l]:
                if A[l] <= target < A[m]:
                    r = m
                else:
                    l = m

            # in the right side in array
            else:
                if A[m] < target <= A[r]:
                    l = m
                else:
                    r = m

        for end in [l, r]:
            if A[end] == target:
                return end

        return -1
