from _test.python import *
from tree.python import BinaryTree


class TestBinaryTree(TestBase):
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
