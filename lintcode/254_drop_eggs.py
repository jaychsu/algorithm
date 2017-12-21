"""
REF: http://blog.csdn.net/shaya118/article/details/40823225

Main Concept:

assuming the minimum times to drop is `x`
according to REF, the relation of `x` is below

         |
         | x
    |....|
. | |....|
   x + 1

0 + 1 + 2 + ... + x
=> x(x + 1) / 2 >= n
"""


"""
cumulative the sum of the triangle
"""
class Solution:
    """
    @param: n: An integer
    @return: The sum of a and b
    """
    def dropEggs(self, n):
        if n <= 0:
            return 0

        _sum = 0
        for i in range(n):
            _sum += i
            if _sum >= n:
                return i

        return n


"""
optimized: cumulative the sum of the triangle

x(x + 1) / 2 >= n
=> sqrt(x(x + 1)) >= sqrt(2n)
=> sqrt(x(x + 1)) >= sqrt(x^2) == x >= sqrt(2n)

so `x` can start from `sqrt(2n)`
"""
from math import sqrt


class Solution:
    """
    @param: n: An integer
    @return: The sum of a and b
    """
    def dropEggs(self, n):
        if n <= 0:
            return 0

        x = int(sqrt(2 * n))
        while x * (x + 1) // 2 < n:
            x += 1

        return x
