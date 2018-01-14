class Solution:
    """
    @param: n: An integer
    @return: True or false
    """
    def checkPowerOf2(self, n):
        if not n or n <= 0:
            return False

        return n & (n - 1) == 0
