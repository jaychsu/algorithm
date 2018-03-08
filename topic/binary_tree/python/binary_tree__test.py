from _test.python import *
from binary_tree.python import *


class TestBinaryTree(TestBase):
    CASES = {
        '{1,2,3,4,#,#,5,#,6,#,#,7,8}': {
            'preorder': '1,2,4,6,7,8,3,5',
            'inorder': '4,7,6,8,2,1,3,5',
            'postorder': '7,8,6,4,2,5,3,1',
        },
        '{1,#,2,#,3,#,4,#,5,#,6,#,7}': {
            'preorder': '1,2,3,4,5,6,7',
            'inorder': '1,2,3,4,5,6,7',
            'postorder': '7,6,5,4,3,2,1',
        },
    }

    trees = None

    @classmethod
    def setUpClass(cls):
        super(TestBinaryTree, cls).setUpClass()

        cls.trees = {
            case: BinaryTree.deserialize(case)
            for case in cls.CASES
        }

    def test_serialization(self):
        case = '{1,2,3,4,#,#,5,#,6,#,#,7,8}'
        tree = BinaryTree.deserialize(case)

        self.assertIsNotNone(tree)
        self.assertEqual(
            case,
            BinaryTree.serialize(tree)
        )

        left = right = None

        # level 1
        self.assertEqual(1, tree.val)

        # level 2
        left, right = tree.left, tree.right
        self.assertEqual(2, left.val)
        self.assertEqual(3, right.val)

        # level 3
        self.assertIs(None, left.right)
        self.assertIs(None, right.left)
        left, right = left.left, right.right
        self.assertEqual(4, left.val)
        self.assertEqual(5, right.val)

        # level 4
        self.assertIs(None, left.left)
        self.assertIs(None, right.left)
        self.assertIs(None, right.right)
        tree = left.right
        self.assertEqual(6, tree.val)

        # level 5
        left, right = tree.left, tree.right
        self.assertEqual(7, left.val)
        self.assertEqual(8, right.val)

        # empty level
        self.assertIs(None, left.left)
        self.assertIs(None, left.right)
        self.assertIs(None, right.left)
        self.assertIs(None, right.right)

    def _run_traversal_test(self, traverse, *, type):
        for _in, _out in self.CASES.items():
            result = []
            traverse(
                self.trees[_in],
                callback=lambda val: result.append(str(val))
            )
            self.assertEqual(
                _out[type],
                ','.join(result)
            )

    def test_preorder_iteration_traversal(self):
        self._run_traversal_test(
            preorder_iteration_traversal,
            type='preorder'
        )

    def test_preorder_recursion_traversal(self):
        self._run_traversal_test(
            preorder_recursion_traversal,
            type='preorder'
        )

    def test_inorder_iteration_traversal(self):
        self._run_traversal_test(
            inorder_iteration_traversal,
            type='inorder'
        )

    def test_inorder_recursion_traversal(self):
        self._run_traversal_test(
            inorder_recursion_traversal,
            type='inorder'
        )

    def test_postorder_iteration_traversal(self):
        self._run_traversal_test(
            postorder_iteration_traversal,
            type='postorder'
        )

    def test_postorder_recursion_traversal(self):
        self._run_traversal_test(
            postorder_recursion_traversal,
            type='postorder'
        )
