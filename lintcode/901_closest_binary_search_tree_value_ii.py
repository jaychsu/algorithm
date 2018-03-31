"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        """
        ans = []

        if not root:
            return ans

        vals = []
        self.inorder_traverse(root, vals)

        n = len(vals)
        i = 0

        while i < n and vals[i] < target:
            i += 1

        i, j = i - 1, i

        while k and i >= 0 and j < n:
            if target - vals[i] < vals[j] - target:
                ans.append(vals[i])
                i -= 1
            else:
                ans.append(vals[j])
                j += 1
            k -= 1

        while k and i >= 0:
            ans.append(vals[i])
            i -= 1
            k -= 1

        while k and j < n:
            ans.append(vals[j])
            j += 1
            k -= 1

        return ans

    def inorder_traverse(self, root, vals):
        if not root:
            return

        self.inorder_traverse(root.left, vals)
        vals.append(root.val)
        self.inorder_traverse(root.right, vals)
