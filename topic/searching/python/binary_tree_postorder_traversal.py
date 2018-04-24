from tree.python import TreeNode


def postorder_recursion_traverse(root, *, callback):
    if not root:
        return

    postorder_recursion_traverse(root.left, callback=callback)
    postorder_recursion_traverse(root.right, callback=callback)
    callback(root.val)


def postorder_iteration_traverse(root, *, callback):
    stack = []
    node = last_visit = root

    while node or stack:
        while node:
            stack.append(node)
            node = node.left

        # check the peek of stack,
        # that is, back to parent
        node = stack[-1]

        if (not node.right or
            last_visit is node.right):

            # same as `stack[-1]`, so no re-assign
            stack.pop()

            callback(node.val)
            last_visit = node
            node = None
        else:
            node = node.right


def postorder_morris_traverse(root, *, callback):
    dummy = TreeNode(0)
    dummy.left = root

    root = dummy
    node = None

    while root:
        if not root.left:
            root = root.right
            continue

        node = root.left

        while node.right and node.right is not root:
            node = node.right

        if not node.right:
            node.right = root
            root = root.left
        else:
            postorder_morris_reverse_visit(root.left, node, callback)
            node.right = None
            root = root.right


def postorder_morris_reverse_visit(from_node, to_node, callback):
    postorder_morris_reverse(from_node, to_node)

    node = to_node
    callback(node.val)

    while node and node is not from_node:
        node = node.right
        callback(node.val)

    postorder_morris_reverse(to_node, from_node)


def postorder_morris_reverse(from_node, to_node):
    a, b, c = from_node, from_node.right, None

    while a is not to_node:
        c = b.right
        b.right = a
        a = b
        b = c
