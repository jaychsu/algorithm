def inorder_recursion_traverse(root, *, callback):
    if not root:
        return

    inorder_recursion_traverse(root.left, callback=callback)
    callback(root.val)
    inorder_recursion_traverse(root.right, callback=callback)


def inorder_iteration_traverse(root, *, callback):
    stack = []
    node = root

    while node or stack:
        while node:
            stack.append(node)
            node = node.left

        node = stack.pop()
        callback(node.val)
        node = node.right


def inorder_morris_traverse(root, *, callback):
    node = None

    while root:
        if not root.left:
            callback(root.val)
            root = root.right
            continue

        node = root.left

        while node.right and node.right is not root:
            node = node.right

        if not node.right:
            node.right = root
            root = root.left
        else:
            callback(root.val)
            node.right = None
            root = root.right
