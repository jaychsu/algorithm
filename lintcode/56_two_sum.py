"""
time: O(n)
space: O(n)

it works even if it's not sorted
"""
class Solution:
    """
    @param: A: An array of Integer
    @param: target: target = A[index1] + A[index2]
    @return: [index1, index2] (index1 < index2)
    """
    def twoSum(self, A, target):
        NOT_FOUND = [-1, -1]
        if not A or len(A) < 2:
            return NOT_FOUND

        remaining = {}
        for i in range(len(A)):
            if A[i] in remaining:
                return [
                    remaining[A[i]],
                    i,
                ]

            remaining[target - A[i]] = i

        return NOT_FOUND


"""
time: O(nlogn)
space: O(n)

needs to sort in advance
"""
class Solution:
    """
    @param: A: An array of Integer
    @param: target: target = A[index1] + A[index2]
    @return: [index1, index2] (index1 < index2)
    """
    def twoSum(self, A, target):
        NOT_FOUND = [-1, -1]
        if not A or len(A) < 2:
            return NOT_FOUND

        n = len(A)
        A = [(A[i], i) for i in range(n)]
        A.sort()

        left, right = 0, n - 1
        while left < right:
            _sum = A[left][0] + A[right][0]
            if _sum == target:
                return sorted([
                    A[left][1],
                    A[right][1],
                ])

            if _sum < target:
                left += 1
            else:
                right -= 1

        return NOT_FOUND
