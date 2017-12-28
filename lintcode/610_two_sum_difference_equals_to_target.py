"""
time: O(n)
space: O(n)

it works even if it's not sorted
"""
class Solution:
    """
    @param: A: an array of Integer
    @param: target: an integer
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum7(self, A, target):
        NOT_FOUND = [-1, -1]
        if not A or len(A) < 2:
            return NOT_FOUND

        remaining = {}
        for i in range(len(A)):
            """
            if a - b = t
            => a = b + t
            """
            if A[i] + target in remaining:
                return [
                    remaining[A[i] + target] + 1,
                    i + 1
                ]

            """
            if b - a = t
            => a = b - t
            """
            if A[i] - target in remaining:
                return [
                    remaining[A[i] - target] + 1,
                    i + 1
                ]

            remaining[A[i]] = i

        return NOT_FOUND


"""
time: O(n)
space: O(n)

needs to sort in advance
"""
class Solution:
    """
    @param: A: an array of Integer
    @param: target: an integer
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum7(self, A, target):
        NOT_FOUND = [-1, -1]
        if not A or len(A) < 2:
            return NOT_FOUND

        if target < 0:
            target = -1 * target

        n = len(A)
        A = [(A[i], i) for i in range(n)]
        A.sort()

        left = 0
        for right in range(1, n):
            while left + 1 < right and A[right][0] - A[left][0] > target:
                left += 1
            if A[right][0] - A[left][0] == target:
                return sorted([
                    A[left][1] + 1,
                    A[right][1] + 1
                ])

        return NOT_FOUND
