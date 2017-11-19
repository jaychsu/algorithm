def inorder_iteration_traversal(root, *, callback):
    if not root:
        return

    stack = []
    node = root
    while node or stack:
        while node:
            stack.append(node)
            node = node.left

        node = stack.pop()
        callback(node.val)
        node = node.right


def inorder_recursion_traversal(root, *, callback):
    if not root:
        return

    inorder_recursion_traversal(root.left, callback=callback)
    callback(root.val)
    inorder_recursion_traversal(root.right, callback=callback)
