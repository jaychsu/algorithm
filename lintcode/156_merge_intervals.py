# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e


class Solution:
    def merge(self, A):
        """
        :type A: List[Interval]
        :rtype: List[Interval]
        """
        ans = []
        if not A:
            return ans

        A.sort(key=lambda I: (I.start, I.end))

        for I in A:
            if not ans or ans[-1].end < I.start:
                ans.append(I)
            elif I.end > ans[-1].end:
                ans[-1].end = I.end

        return ans
