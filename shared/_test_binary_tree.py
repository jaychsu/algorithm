"""
% python -i _test_binary_tree.py
Serialization lib is valid.
============
Traversal Case: {1,2,3,4,#,#,5,#,6,#,#,7,8}
------------
preorder_iteration_traversal: 1, 2, 4, 6, 7, 8, 3, 5
preorder_recursion_traversal: 1, 2, 4, 6, 7, 8, 3, 5
inorder_iteration_traversal: 4, 7, 6, 8, 2, 1, 3, 5
inorder_recursion_traversal: 4, 7, 6, 8, 2, 1, 3, 5
postorder_iteration_traversal: 7, 8, 6, 4, 2, 5, 3, 1
postorder_recursion_traversal: 7, 8, 6, 4, 2, 5, 3, 1
============
Traversal Case: {1,#,2,#,3,#,4,#,5,#,6,#,7}
------------
preorder_iteration_traversal: 1, 2, 3, 4, 5, 6, 7
preorder_recursion_traversal: 1, 2, 3, 4, 5, 6, 7
inorder_iteration_traversal: 1, 2, 3, 4, 5, 6, 7
inorder_recursion_traversal: 1, 2, 3, 4, 5, 6, 7
postorder_iteration_traversal: 7, 6, 5, 4, 3, 2, 1
postorder_recursion_traversal: 7, 6, 5, 4, 3, 2, 1
============
"""

from binary_tree_serialization import BinaryTree

from binary_tree_preorder_traversal import (
    preorder_iteration_traversal,
    preorder_recursion_traversal,
)
from binary_tree_inorder_traversal import (
    inorder_iteration_traversal,
    inorder_recursion_traversal,
)
from binary_tree_postorder_traversal import (
    postorder_iteration_traversal,
    postorder_recursion_traversal,
)

METHODS = (
    preorder_iteration_traversal,
    preorder_recursion_traversal,
    inorder_iteration_traversal,
    inorder_recursion_traversal,
    postorder_iteration_traversal,
    postorder_recursion_traversal,
)
CASES = (
    '{1,2,3,4,#,#,5,#,6,#,#,7,8}',
    '{1,#,2,#,3,#,4,#,5,#,6,#,7}',
)

result = None
def show_result(x):
    result.append(str(x))

case = CASES[0]
if case == BinaryTree.serialize(BinaryTree.deserialize(case)):
    print('Serialization lib is valid.')
else:
    quit('Serialization lib is not valid.')

print('============')
for case in CASES:
    root = BinaryTree.deserialize(case)
    print('Traversal Case: %s\n------------' % case)

    for traversal in METHODS:
        result = []
        traversal(root, callback=show_result)
        print('%s: %s' % (
            traversal.__name__,
            ', '.join(result),
        ))
    print('============')
