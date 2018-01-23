class Solution:
    def majorityElement(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        ans = None
        cnt = 0

        for a in A:
            if cnt == 0:
                ans = a
                cnt += 1
                continue

            if ans == a:
                cnt += 1
            else:
                cnt -= 1

        return ans
