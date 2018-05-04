def largest_smaller_bst_node(root, target):
    ans = -1

    if not root:
        return ans

    while root:
        if root.val < target:
            ans = root.val
            root = root.right
        else:
            root = root.left

    return ans
