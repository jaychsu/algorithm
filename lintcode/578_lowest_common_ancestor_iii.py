"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None


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
    def lowestCommonAncestor3(self, root, A, B):
        """
        for each node in tree, we can record whether A or B exists in its subtree
        use post-traversal to make a bottom-up searching

        node A or node B may not exist in tree.
        so we can't directly use divide conquer like lintcode/88_lowest_common_ancestor.py
        => {4,3,7,#,#,5,6}, 1, 3
        => expected `None`
        => got `3` if using divide conquer
        """
        lca, has_a, has_b = self.divide_conquer(root, A, B)

        if has_a and has_b:
            return lca

    def divide_conquer(self, node, A, B):
        if not node:
            return None, False, False

        left,  a_in_left,  b_in_left = self.divide_conquer(node.left, A, B)
        right, a_in_right, b_in_right = self.divide_conquer(node.right, A, B)

        has_a = a_in_left or a_in_right or node is A
        has_b = b_in_left or b_in_right or node is B

        if node is A or node is B:
            return node, has_a, has_b
        if left and right:
            return node, has_a, has_b
        if left:
            return left, has_a, has_b
        if right:
            return right, has_a, has_b

        return None, has_a, has_b
