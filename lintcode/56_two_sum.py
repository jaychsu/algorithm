class Solution:
    """
    @param: A: An array of Integer
    @param: target: target = A[index1] + A[index2]
    @return: [index1, index2] (index1 < index2)
    """
    def twoSum(self, A, target):
        if not A:
            return [-1, -1]

        remaining = {}
        for i in range(len(A)):
            if A[i] in remaining:
                return [
                    remaining[A[i]],
                    i
                ]

            remaining[target - A[i]] = i

        return [-1, -1]
