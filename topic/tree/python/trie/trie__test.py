from _test.python import *
from tree.python import Trie


class TestTrie(TestBase):
    def test_init(self):
        trie = Trie()

        for attr, default_val in (
            ('children', {}),
            ('end_of', None),
        ):
            self.assertTrue(hasattr(trie.root, attr))
            self.assertEqual(getattr(trie.root, attr), default_val)

    def test_put(self):
        trie = Trie()
        node = None
        TEST_WORD = 'aabbccdefg'

        trie.put(TEST_WORD)

        for char in TEST_WORD:
            node = trie.get_node(char, node)
            if node.end_of == TEST_WORD:
                self.assertTrue(len(node.children) == 0)
            else:
                self.assertTrue(len(node.children) == 1)

        # for case in empty string ''
        self.assertEqual(trie.root.end_of, None)
        trie.put('')
        self.assertEqual(trie.root.end_of, '')

    def test_has_word_or_prefix(self):
        trie = Trie()

        trie.put('abc')

        self.assertTrue(trie.has_word('abc'))
        self.assertTrue(trie.has_prefix('a'))
        self.assertTrue(trie.has_prefix('ab'))
        self.assertTrue(trie.has_prefix('abc'))
        self.assertFalse(trie.has_word(''))
        self.assertFalse(trie.has_word('abd'))
        self.assertFalse(trie.has_word('abcd'))
        self.assertFalse(trie.has_prefix('abcd'))

        node = None
        trie.put('abd')

        for char in 'abd':
            node = trie.get_node(char, node)
            if char == 'a':
                self.assertTrue(len(node.children) == 1)
            elif char == 'b':
                self.assertTrue(len(node.children) == 2)
            elif node.end_of == 'abd':
                self.assertTrue(len(node.children) == 0)
            else:
                # should not visit here
                self.assertTrue(False)

        # for case in empty string ''
        self.assertEqual(trie.root.end_of, None)
        self.assertFalse(trie.has_word(''))
        self.assertFalse(trie.has_prefix(''))
        trie.put('')
        self.assertEqual(trie.root.end_of, '')
        self.assertTrue(trie.has_word(''))
        self.assertTrue(trie.has_prefix(''))

    def test_invalid_put(self):
        trie = Trie()

        for word, cnt, end_of in (
            (None, 0, None),
            ({}, 0, None),
            ({'a': 1}, 0, None),
            ([], 0, None),
            ([1, 2, 3], 0, None),
            ('a', 1, None),
            (u'b', 2, None),
            (b'c', 3, None),
            ('', 3, ''),
        ):
            trie.put(word)
            self.assertTrue(len(trie.root.children) == cnt)
            self.assertTrue(trie.root.end_of == end_of)
