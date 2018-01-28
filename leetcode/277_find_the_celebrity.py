"""
REF: https://discuss.leetcode.com/topic/25720/java-python-o-n-calls-o-1-space-easy-to-understand-solution
"""


class Solution:
    def findCelebrity(self, n):
        if not n:
            return -1

        x = 0

        for i in range(n):
            if knows(x, i):
                x = i

        for i in range(x):
            if knows(x, i):
                return -1

        for i in range(n):
            if not knows(i, x):
                return -1

        return x
