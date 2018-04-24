from _test.python import *
from searching.python import *
from tree.python import BinaryTree


class TestBinaryTreeTraversal(TestBase):
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
        super(TestBinaryTreeTraversal, cls).setUpClass()

        cls.trees = {
            case: BinaryTree.deserialize(case)
            for case in cls.CASES
        }

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

    def test_preorder_recursion_traverse(self):
        self._run_traversal_test(
            preorder_recursion_traverse,
            type='preorder'
        )

    def test_preorder_iteration_traverse(self):
        self._run_traversal_test(
            preorder_iteration_traverse,
            type='preorder'
        )

    def test_preorder_morris_traverse(self):
        self._run_traversal_test(
            preorder_morris_traverse,
            type='preorder'
        )

    def test_inorder_recursion_traverse(self):
        self._run_traversal_test(
            inorder_recursion_traverse,
            type='inorder'
        )

    def test_inorder_iteration_traverse(self):
        self._run_traversal_test(
            inorder_iteration_traverse,
            type='inorder'
        )

    def test_inorder_morris_traverse(self):
        self._run_traversal_test(
            inorder_morris_traverse,
            type='inorder'
        )

    def test_postorder_recursion_traverse(self):
        self._run_traversal_test(
            postorder_recursion_traverse,
            type='postorder'
        )

    def test_postorder_iteration_traverse(self):
        self._run_traversal_test(
            postorder_iteration_traverse,
            type='postorder'
        )

    def test_postorder_morris_traverse(self):
        self._run_traversal_test(
            postorder_morris_traverse,
            type='postorder'
        )
