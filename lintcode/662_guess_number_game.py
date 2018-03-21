"""
The guess API is already defined for you.
@param num, your guess
@return -1 if my number is lower, 1 if my number is higher, otherwise return 0
you can call Guess.guess(num)
"""


class Solution:
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if not n or n <= 1:
            return 1

        left, right = 1, n

        while left + 1 < right:
            mid = (left + right) // 2
            res = Guess.guess(mid)

            if res == 0:
                return mid
            elif res == 1:
                left = mid
            else:
                right = mid

        return left if Guess.guess(left) == 0 else right
