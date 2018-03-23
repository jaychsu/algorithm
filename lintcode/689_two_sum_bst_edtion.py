"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: : the root of tree
    @param: : the target sum
    @return: two numbers from tree which sum is n
    """
    def twoSum(self, root, n):
        self.left = self.right = None
        self.head = self.tail = root

        self.pre()
        self.nxt()

        while self.left != self.right:
            _sum = self.left.val + self.right.val

            if _sum == n:
                return [self.left.val, self.right.val]

            if _sum < n:
                self.nxt()
            else:
                self.pre()

    def pre(self):
        while self.tail:
            cur = self.tail.right

            if cur and cur != self.right:
                while cur.left and cur.left != self.tail:
                    cur = cur.left

                if cur.left == self.tail:
                    self.right = self.tail

                    cur.left = None
                    self.tail = self.tail.left
                    break
                else:
                    cur.left = self.tail
                    self.tail = self.tail.right
            else:
                self.right = self.tail
                self.tail = self.tail.left
                break

    def nxt(self):
        while self.head:
            cur = self.head.left

            if cur and cur != self.left:
                while cur.right and cur.right != self.head:
                    cur = cur.right

                if cur.right == self.head:
                    self.left = self.head

                    cur.right = None
                    self.head = self.head.right
                    break
                else:
                    cur.right = self.head
                    self.head = self.head.left
            else:
                self.left = self.head
                self.head = self.head.right
                break
