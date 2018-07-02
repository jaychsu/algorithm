from _test.python import *
from hash.python import HashTable


class TestHashTable(TestBase):
    def test_operation(self):
        d = HashTable()
        self.assertEqual(len(d), 0)

        d[1] = 1
        self.assertEqual(d[1], 1)
        self.assertEqual(len(d), 1)

        d[2] = 2
        self.assertEqual(d[2], 2)
        self.assertEqual(len(d), 2)

        d['ab'] = 3
        self.assertEqual(d['ab'], 3)
        self.assertEqual(len(d), 3)

        d['ba'] = 4
        self.assertEqual(d['ba'], 4)
        self.assertEqual(len(d), 4)

        self.assertEqual(d['ab'], 3)
        self.assertEqual(len(d), 4)
        del d['ab']
        self.assertEqual(len(d), 3)
        with self.assertRaises(KeyError):
            d['ab']

    def test_collision(self):
        d = HashTable(4000, 31)
        self.assertEqual(len(d), 0)

        self.assertEqual(d._encode('ab'), d._encode('bC'))
        self.assertEqual(d._encode('ab'), d._encode('c$'))

        d['ab'] = 1
        self.assertEqual(d['ab'], 1)
        self.assertEqual(len(d), 1)

        d['bC'] = 2
        self.assertEqual(d['bC'], 2)
        self.assertEqual(len(d), 2)

        d['c$'] = 3
        self.assertEqual(d['c$'], 3)
        self.assertEqual(len(d), 3)

        del d['bC']
        self.assertEqual(len(d), 2)
        with self.assertRaises(KeyError):
            d['bC']

        del d['c$']
        self.assertEqual(len(d), 1)
        with self.assertRaises(KeyError):
            d['c$']
            d['bC']

        del d['ab']
        self.assertEqual(len(d), 0)
        with self.assertRaises(KeyError):
            d['ab']
            d['c$']
            d['bC']
