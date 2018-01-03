from lintcode import ListNode


class Stack:
    def __init__(self):
        self.dummy = self.tail = ListNode(-1)

    """
    @param: x: An integer
    @return: nothing
    """
    def push(self, x):
        node = ListNode(x)
        node.pre = self.tail
        self.tail.nxt = node
        self.tail = node

    """
    @return: nothing
    """
    def pop(self):
        if self.isEmpty():
            return
        node = self.tail
        self.tail = node.pre
        self.tail.nxt = node.pre = None

    """
    @return: An integer
    """
    def top(self):
        if self.isEmpty():
            return
        return self.tail.val

    """
    @return: True if the stack is empty
    """
    def isEmpty(self):
        return self.dummy is self.tail
