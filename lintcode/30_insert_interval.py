"""
Main Concept:
1. iterate from end, find the position to insert new one
2. append new one to `intvs`
3. iterate from end, and swap `intvs[i]` and `intvs[i - 1]`
   til meet the position found in (1)
4. iterate from start, do merge intv


Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    def insert(self, intvs, intv):
        """
        :type intvs: list[Interval]
        :type intv: Interval
        :rtype: list[Interval]
        """
        if not intvs and not intv:
            return []
        if not intvs:
            return [intv]
        if not intv:
            return intvs

        ans = []
        index = len(intvs)

        for i in range(len(intvs) - 1, -1, -1):
            if intvs[i].start <= intv.start:
                break
            index -= 1

        intvs.append(intv)
        for i in range(len(intvs) - 1, index, -1):
            intvs[i], intvs[i - 1] = intvs[i - 1], intvs[i]

        for i in range(len(intvs)):  # since there is one more child in intvs
            if ans and intvs[i].start <= ans[-1].end:
                ans[-1].end = max(ans[-1].end, intvs[i].end)
            else:
                ans.append(intvs[i])

        return ans
