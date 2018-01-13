"""
time: O(n)
space: O(n)
"""
class Solution:
    """
    @param: A: an array of Integer
    @param: target: target = A[index1] + A[index2]
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum(self, A, target):
        NOT_FOUND = [-1, -1]
        if not A:
            return NOT_FOUND

        remaining = {}
        for i in range(len(A)):
            if A[i] in remaining:
                return [
                    remaining[A[i]] + 1,
                    i + 1,
                ]
            remaining[target - A[i]] = i

        return NOT_FOUND


"""
time: O(n)
space: O(1)
"""
class Solution:
    """
    @param: A: an array of Integer
    @param: target: target = A[index1] + A[index2]
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum(self, A, target):
        NOT_FOUND = [-1, -1]
        if not A:
            return NOT_FOUND

        left, right = 0, len(A) - 1
        while left < right:
            _sum = A[left] + A[right]
            if _sum == target:
                return [left + 1, right + 1]
            if _sum < target:
                left += 1
            else:
                right -= 1

        return NOT_FOUND
