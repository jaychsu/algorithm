"""
The read4 API is already defined for you.
@param buf, a list of characters
@return an integer

def read4(buf):
    pass
"""


class Solution:
    def read(self, buf, n):
        """
        :type buf: List[str], Destination buffer
        :type n: int, Maximum number of characters to read
        :rtype: int, The number of characters read
        """
        if not buf or n <= 0:
            return 0

        i = 0
        k = 4
        tmp = [0] * k

        while i < n and k == 4:
            k = read4(tmp)
            j = 0

            while i < n and j < k:
                buf[j] = tmp[j]
                i += 1
                j += 1

        return i


if __name__ == '__main__':
    data = 'abcdferrdsjfklsdjfdsr'
    n = len(data)
    i = 0
    k = 4

    def read4(buf):
        global i
        j = 0

        while i < n and j < k:
            buf[j] = data[i]
            i += 1
            j += 1

        return j

    s = Solution()
    res = s.read([0] * 4, 4)
    print(res)
