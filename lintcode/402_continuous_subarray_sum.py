class Solution:
    """
    @param: A: An integer array
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def continuousSubarraySum(self, A):
        ans = [-1, -1]
        if not A:
            return ans

        left = right = 0
        _max = _sum = float('-inf')
        for i in range(len(A)):
            if _sum < 0:
                _sum = A[i]
                left = right = i
            else:
                _sum += A[i]
                right = i

            if _sum > _max:
                _max = _sum
                ans = [left, right]

        return ans
