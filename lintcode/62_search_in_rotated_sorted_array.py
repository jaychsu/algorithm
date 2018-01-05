"""
for given A:
    [ 4, 5, 6, 7, 0, 1, 2 ]
      l        M  m     r

if the `mid` > `l`, then `mid` must be in left side, otherwise in right side

if `mid` in left side, we can check if the `target` between `l` and `mid`
(because we dont know the `M` at where)

otherwise the `mid` in right side, we can also check if the `target` between `mid` and `r`
(same reason, we dont know the `m` at where)
"""


class Solution:
    """
    @param: A: an integer rotated sorted array
    @param: target: an integer to be searched
    @return: an integer
    """
    def search(self, A, target):
        NOT_FOUND = -1
        if not A:
            return NOT_FOUND

        left, right = 0, len(A) - 1
        while left + 1 < right:
            mid = (left + right) // 2

            if A[mid] == target:
                return mid

            if A[mid] < A[0]:
                if A[mid] < target <= A[right]:
                    left = mid
                else:
                    right = mid
            else:
                if A[left] <= target < A[mid]:
                    right = mid
                else:
                    left = mid

        if A[left] == target:
            return left
        if A[right] == target:
            return right

        return NOT_FOUND
