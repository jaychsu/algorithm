"""
REF: https://leetcode.com/articles/largest-number/
"""


class LgSort(str):
    def __lt__(a, b):
        return a + b > b + a


class Solution:
    def largestNumber(self, A):
        """
        :type A: List[int]
        :rtype: str
        """
        A = ''.join(sorted(map(str, A), key=LgSort))
        return '0' if A[0] == '0' else A
