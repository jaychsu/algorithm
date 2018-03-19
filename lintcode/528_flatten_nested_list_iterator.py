"""
Your NestedIterator object will be instantiated and called as such:
i, v = NestedIterator(nestedList), []
while i.hasNext(): v.append(i.next())


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


class NestedIterator(object):
    def __init__(self, nestedList):
        self.stack = [[nestedList, 0]]

    # @return {int} the next element in the iteration
    def next(self):
        if not self.hasNext():
            return -1

        lst, i = self.stack[-1]
        self.stack[-1][1] += 1

        return lst[i].getInteger()

    # @return {boolean} true if the iteration has more element or false
    def hasNext(self):
        stack = self.stack

        while stack:
            lst, i = stack[-1]

            if i >= len(lst):
                stack.pop()
            elif lst[i].isInteger():
                return True
            else:
                # lst[i] is list
                stack[-1][1] += 1
                stack.append([lst[i].getList(), 0])

        return False
