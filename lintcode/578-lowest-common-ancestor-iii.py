"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""
"""
Test Case:

{1,#,2,#,3,#,4,#,5}
3
8

{1}
1
1
"""

class Solution:
    """
    @param: root: The root of the binary tree.
    @param: A: A TreeNode
    @param: B: A TreeNode
    @return: Return the LCA of the two nodes.
    """
    """
    for each node in tree, we can record whether A or B exists in its subtree
    use post-traversal to make a bottom-up searching
    """
    def lowestCommonAncestor3(self, root, A, B):
        a_exist, b_exist, lca = self._divide_conquer(root, A, B)
        if a_exist and b_exist:
            return lca

    def _divide_conquer(self, node, A, B):
        if not node:
            return False, False, None

        a_exist_in_left,  b_exist_in_left,  left_child  = self._divide_conquer(node.left,  A, B)
        a_exist_in_right, b_exist_in_right, right_child = self._divide_conquer(node.right, A, B)

        a_exist = a_exist_in_left or a_exist_in_right or node == A
        b_exist = b_exist_in_left or b_exist_in_right or node == B

        if node == A or node == B:
            return a_exist, b_exist, node
        if left_child and right_child:
            return a_exist, b_exist, node
        if left_child:
            return a_exist, b_exist, left_child
        if right_child:
            return a_exist, b_exist, right_child
        return a_exist, b_exist, None
