class Solution:
    """
    @param: A: a list of integers.
    @param: k: length of window.
    @return: the sum of the element inside the window at each moving.
    """
    def winSum(self, A, k):
        ans = []
        if (not A or not k or k <= 0 or
            len(A) < k):
            return ans

        _sum = 0
        for i in range(len(A)):
            _sum += A[i]

            if i < k - 1:
                continue

            ans.append(_sum)

            _sum -= A[i - k + 1]

        return ans
