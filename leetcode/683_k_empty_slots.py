"""
>>> gotcha = []
>>> for s in (Solution(), Solution2()):
...     for _in, _out in (
...         (([1,3,2], 1), 2),
...         (([1,2,3], 1), -1),
...     ):
...         res = s.kEmptySlots(*_in)
...         if res != _out: print(_in, res)
...         gotcha.append(res == _out)
>>> bool(gotcha) and all(gotcha)
True
"""
import bisect


class Solution:
    """
    Maintain pos by bloom order
    """
    def kEmptySlots(self, flowers, k):
        """
        :type flowers: List[int]
        :type k: int
        :rtype: int
        """
        bloom = []

        for day in range(len(flowers)):
            x = flowers[day]
            i = bisect.bisect_left(bloom, x)
            for _x in bloom[max(0, i - 1):i + 1]:
                if abs(_x - x) - 1 == k:
                    return day + 1  # changed to 1-based
            bloom.insert(i, x)

        return -1


class Solution2:
    """
    Two Pointer:
    https://blog.csdn.net/magicbean2/article/details/79235465
    """
    def kEmptySlots(self, flowers, k):
        """
        :type flowers: List[int]
        :type k: int
        :rtype: int
        """
        n = len(flowers)
        x2day = [0] * n
        for day in range(n):
            """
            day: 0-based => 1-based
            x:   1-based => 0-based
            """
            x = flowers[day]
            x2day[x - 1] = day + 1

        ans = INF = float('inf')
        left, right = 0, k + 1
        i = 0

        while right < n:
            if any((
                x2day[i] < x2day[left],
                x2day[i] <= x2day[right],
            )):
                if i == right:
                    ans = min(ans, max(x2day[left], x2day[right]))
                left, right = i, k + i + 1
            i += 1

        return ans if ans < INF else -1
