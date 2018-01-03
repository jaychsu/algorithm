"""
This is the interface that allows for creating nested lists.
You should not implement it, or speculate about its implementation

class NestedInteger(object):
    def isInteger(self):
        # @return {boolean} True if this NestedInteger holds a single integer,
        # rather than a nested list.

    def getInteger(self):
        # @return {int} the single integer that this NestedInteger holds,
        # if it holds a single integer
        # Return None if this NestedInteger holds a nested list

    def getList(self):
        # @return {NestedInteger[]} the nested list that this NestedInteger holds,
        # if it holds a nested list
        # Return None if this NestedInteger holds a single integer
"""


class Solution(object):
    # @param {NestedInteger[]} L a list of NestedInteger Object
    # @return {int} an integer
    def depthSum(self, L):
        return self.dfs(L, 1)

    def dfs(self, L, depth):
        _sum = 0

        for obj in L:
            if obj.isInteger():
                _sum += depth * obj.getInteger()
                continue

            _sum += self.dfs(obj.getList(), depth + 1)

        return _sum


class Solution(object):
    # @param {NestedInteger[]} L a list of NestedInteger Object
    # @return {int} an integer
    def depthSum(self, L):
        ans = 0
        if not L:
            return ans

        queue = L
        depth = 0
        while queue:
            _queue = []
            depth += 1

            for obj in queue:
                if obj.isInteger():
                    ans += depth * obj.getInteger()
                    continue

                _queue.extend(obj.getList())

            queue = _queue

        return ans
