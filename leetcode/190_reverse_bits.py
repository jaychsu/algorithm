# Reverse bit every 4 bits
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        if not n:
            return 0

        # the reversed bins for i = 0 -> 15
        rev = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
        ans = 0
        msk = 15  # 15 (10) == 1111 (2)

        for i in range(8):
            ans <<= 4
            curr = n & msk
            ans |= rev[curr]
            n >>= 4

        return ans


# Reverse bit every 1 bits
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        ans = 0

        if not n:
            return ans

        for i in range(32):
            ans <<= 1
            ans |= n & 1
            n >>= 1

        return ans
