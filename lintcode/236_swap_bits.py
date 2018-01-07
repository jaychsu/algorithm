class Solution:
    """
    @param: x: An integer
    @return: An integer
    """
    def swapOddEvenBits(self, x):
        """
        0x55555555 == 01010101010101010101010101010101 (2)
        0xAAAAAAAA == 10101010101010101010101010101010 (2)
        """
        return ( ((x & 0xAAAAAAAA) >> 1) | ((x & 0x55555555) << 1) )
