def postorder_iteration_traversal(root, *, callback):
    if not root:
        return

    stack = []
    node = last_visit = root
    while node or stack:
        while node:
            stack.append(node)
            node = node.left

        # check the peek of stack,
        # that is, back to parent
        node = stack[-1]

        if not node.right \
                or node.right is last_visit:

            # same as `stack[-1]`, so no re-assign
            stack.pop()

            callback(node.val)
            last_visit = node
            node = None
        else:
            node = node.right


def postorder_recursion_traversal(root, *, callback):
    if not root:
        return

    postorder_recursion_traversal(root.left, callback=callback)
    postorder_recursion_traversal(root.right, callback=callback)
    callback(root.val)
