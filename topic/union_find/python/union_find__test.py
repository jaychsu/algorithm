from _test.python import *
from union_find.python import *


class TestUnionFind(TestBase):
    def test_init(self):
        uf = UnionFind()

        self.assertEqual(uf.nodes, {})

    def test_connect(self):
        uf = UnionFind()

        for i in range(1, 6):
            query = uf.connect(i, 0)
            self.assertEqual(query, 0)

        for i in range(1, 6):
            self.assertEqual(uf.nodes[i], 0)

    def test_compression(self):
        uf = UnionFind()

        uf.connect(3, 2)
        uf.connect(2, 1)

        self.assertEqual(uf.nodes[3], 2)
        self.assertEqual(uf.nodes[2], 1)

        query = uf.find(3)

        self.assertEqual(query, 1)
        self.assertEqual(uf.nodes[3], 1)
