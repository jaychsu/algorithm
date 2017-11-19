def preorder_iteration_traversal(root, *, callback):
    if not root:
        return

    stack = []
    node = root
    while node or stack:
        while node:
            callback(node.val)
            stack.append(node)
            node = node.left

        node = stack.pop()
        node = node.right


def preorder_recursion_traversal(root, *, callback):
    if not root:
        return

    callback(root.val)
    preorder_recursion_traversal(root.left, callback=callback)
    preorder_recursion_traversal(root.right, callback=callback)
