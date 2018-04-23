"""
Inorder Traversal in Binary Tree
without Recursion or Stack or Modification

Recursion: The simplest way
Iteration: With Stack
Morris Traversal: With Modification

And the following code is for the 4th way
to inorder traverse binary tree
if we have parent pointers available to us.

REF: Inorder Non-threaded Binary Tree Traversal without Recursion or Stack
https://www.geeksforgeeks.org/inorder-non-threaded-binary-tree-traversal-without-recursion-or-stack/


Node Structure:

>>> class TreeNode:
...     def __init__(self, val, left=None, right=None, parent=None):
...         self.val = val
...         self.left = left
...         self.right = right
...         self.parent = parent


Process:

0. go_left = True
1. keep moving to the most left
2. print val
3. if has right child, move on it. and go_left = True to repeat (1)
4. keep moving to the most parent
   if no right and its just the right of its parent
5. move one more to its parent and go_left = False


Testing:

>>> trees = []
>>> tree_infos = [
...     ((
...         (1, None, None, 2),
...         (2, 1, None, None),
...     ), '1,2'),
...     ((
...         (20, None, 8, 22),
...         (8, 20, 4, 12),
...         (22, 20, None, None),
...         (4, 8, None, None),
...         (12, 8, 10, 14),
...         (10, 12, None, None),
...         (14, 12, None, None),
...     ), '4,8,10,12,14,20,22'),
...     ((
...         (10, None, 5, 100),
...         (5, 10, None, None),
...         (100, 10, 80, 120),
...         (80, 100, None, None),
...         (120, 100, None, None),
...     ), '5,10,80,100,120'),
...     ((
...         (1, None, 2, 3),
...         (2, 1, 4, None),
...         (3, 1, None, 5),
...         (4, 2, None, 6),
...         (5, 3, None, None),
...         (6, 4, 7, 8),
...         (7, 6, None, None),
...         (8, 6, None, None),
...     ), '4,7,6,8,2,1,3,5'),
...     ((
...         (1, None, None, 2),
...         (2, 1, None, 3),
...         (3, 2, None, 4),
...         (4, 3, None, 5),
...         (5, 4, None, 6),
...         (6, 5, None, 7),
...         (7, 6, None, None),
...     ), '1,2,3,4,5,6,7'),
... ]

>>> for info, _ in tree_infos:
...     nodes = {node[0]: TreeNode(node[0]) for node in info}
...
...     for val, parent, left, right in info:
...         if parent:
...             nodes[val].parent = nodes[parent]
...         if left:
...             nodes[val].left = nodes[left]
...         if right:
...             nodes[val].right = nodes[right]
...
...     trees.append(nodes[info[0][0]])

>>> gotcha = []

>>> for i in range(len(trees)):
...     res = []
...     inorder_traverse(trees[i], callback=lambda val: res.append(str(val)))
...     gotcha.append(','.join(res) == tree_infos[i][1])

>>> bool(gotcha) and all(gotcha)
True
"""


def inorder_traverse(root, *, callback):
    go_left = True

    while root:
        while go_left and root.left:
            root = root.left

        callback(root.val)

        if root.right:
            root = root.right
            go_left = True
            continue

        # if no right child,
        # and its just a right child of its parent
        while root.parent and root is root.parent.right:
            root = root.parent

        root = root.parent
        go_left = False
