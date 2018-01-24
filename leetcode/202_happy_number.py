class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        slow = self.square_sum(n)
        fast = self.square_sum(slow)

        while slow != fast:
            slow = self.square_sum(slow)
            fast = self.square_sum(
                self.square_sum(fast)
            )

        return True if slow == 1 else False

    def square_sum(self, a):
        res = b = 0

        while a != 0:
            b = a % 10
            res += b * b
            a //= 10

        return res
