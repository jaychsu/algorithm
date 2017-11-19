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
