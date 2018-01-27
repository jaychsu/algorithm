class Solution:
    def nextGreatestLetter(self, L, target):
        """
        :type L: List[str]
        :type target: str
        :rtype: str
        """
        n = len(L)
        left, right = 0, n - 1

        while left + 1 < right:
            mid = (left + right) // 2
            if L[mid] <= target:
                left = mid
            else:
                right = mid

        if target < L[left]:
            return L[left]

        if target < L[right]:
            return L[right]

        return L[0]
