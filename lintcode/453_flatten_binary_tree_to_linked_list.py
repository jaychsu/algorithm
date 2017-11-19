"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""
"""
For given tree:
1-5-6
 =2-4
   =3
take postorder traversal, and the visited order will be `3,4,2,1,5,6`

1. rebase the right child with the last right child in left child
when visit `2`
1-5-6
 =2=3-4

2. move the left child to the right
when visit `2`
1-5-6
 =2-3-4

3. keep doing (1) and (2)
when visit `1`
1-2-3-4-5-6
"""

class Solution:
    """
    @param: root: a TreeNode, the root of the binary tree
    @return:
    """
    def flatten(self, root):
        if not root:
            return

        self.flatten(root.left)
        self.flatten(root.right)

        node = root
        if not node.left:
            return

        # to pointer the most left node
        node = root.left

        # preparation to receive the `root.right`
        while node.right:
            node = node.right

        # to straighten the curve
        """
          1          1      1
         / \        /        \
        2   3  =>  2    =>    2
                    \          \
                     3          3
        """
        node.right, root.right, root.left = \
        root.right, root.left,  None
