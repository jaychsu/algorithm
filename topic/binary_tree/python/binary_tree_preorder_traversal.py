def preorder_recursion_traverse(root, *, callback):
    if not root:
        return

    callback(root.val)
    preorder_recursion_traverse(root.left, callback=callback)
    preorder_recursion_traverse(root.right, callback=callback)


def preorder_iteration_traverse(root, *, callback):
    stack = []
    node = root

    while node or stack:
        while node:
            callback(node.val)
            stack.append(node)
            node = node.left

        node = stack.pop()
        node = node.right


def preorder_morris_traverse(root, *, callback):
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
            callback(root.val)
            node.right = root
            root = root.left
        else:
            node.right = None
            root = root.right
