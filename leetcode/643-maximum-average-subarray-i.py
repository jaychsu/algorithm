class Solution:
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        """
        Assuming the answer we want is `Ans = Max(A[i] + A[i+1] + ... + A[i+k-1])`,
        and we define the `P[i] = A[0] + A[1] + ... + A[i-1]`,
        so that `Ans = Max(P[i+k] - P[i])`, and `i+k-1 < n -> i < n-k+1`
        * max index in P is `i+k`, so in A is `(i+k)-1`, `i+k-1 < n`
        """
        """
        P[0] = 0
        P[1] = P[0] + A[0]
        P[2] = P[1] + A[1]
        P[i] = P[i-1] + A[i-1]
             = A[0] + A[1] + ... + A[i-1]
        """
        P = [0]
        for x in nums: P.append(P[-1] + x)
        max_sum = max(P[i+k] - P[i] for i in range(len(nums) - k + 1))
        return max_sum / float(k)

class Solution:
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        """
        Assuming k = 3
        i: 0 1 2 3
              |--> Start to find max sum
                |--> Start to remove past child
        """
        max_sum, tmp_sum = float('-inf'), 0
        for i in range(len(nums)):
            tmp_sum += nums[i]
            if i >= k:
                tmp_sum -= nums[i-k]
            if i + 1 >= k:
                max_sum = max(max_sum, tmp_sum)
        return max_sum / float(k)
