from _test.python import *
from traversal.python import *
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

    def setUp(self):
        super(TestBinaryTreeTraversal, self).setUp()

        self.trees = {
            case: BinaryTree.deserialize(case)
            for case in self.CASES
        }

    def _run_traversal_test(self, Traversal):
        for traverse in (
            Traversal.preorder_traverse,
            Traversal.inorder_traverse,
            Traversal.postorder_traverse,
        ):
            for i, o in self.CASES.items():
                res = []
                traverse(
                    self.trees[i],
                    callback=lambda val: res.append(str(val))
                )

                key = traverse.__name__.replace('_traverse', '')
                self.assertEqual(o[key], ','.join(res))

    def test_recursive_traversal(self):
        self._run_traversal_test(RecursiveTraversal)

    def test_iterative_traversal(self):
        self._run_traversal_test(IterativeTraversal)

    def test_morris_traversal(self):
        self._run_traversal_test(MorrisTraversal)
