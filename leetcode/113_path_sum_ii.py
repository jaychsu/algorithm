# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def pathSum(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []
        self.dfs(root, target, ans, [])
        return ans

    def dfs(self, node, remaining, ans, path):
        if not node:
            return

        path.append(node.val)
        remaining -= node.val

        if remaining == 0 and not node.left and not node.right:
            ans.append(path[:])

        self.dfs(node.left, remaining, ans, path)
        self.dfs(node.right, remaining, ans, path)

        path.pop()
