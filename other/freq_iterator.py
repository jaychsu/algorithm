"""
Testing:

>>> gotcha = []
>>> for _in, _out in (
...     (
...         ['foo', 'foo', 'bar', 'foo'],
...         [['foo', 2], ['bar', 1], ['foo', 1]]
...     ),
...     (
...         ['a', 'a', 'a', 'b', 'b', 'c', 'a', 'b', 'b'],
...         [['a', 3], ['b', 2], ['c', 1], ['a', 1], ['b', 2]]
...     ),
...     (
...         ['a', 'a', 'a', 'b', 'b', 'c', 'a', 'b', 'c'],
...         [['a', 3], ['b', 2], ['c', 1], ['a', 1], ['b', 1], ['c', 1]]
...     ),
...     (
...         ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'],
...         [['a', 1], ['b', 1], ['c', 1],
...          ['d', 1], ['e', 1], ['f', 1],
...          ['g', 1], ['h', 1], ['i', 1]]
...     ),
... ):
...     origin_iterator = ListIterator(_in)
...     res = [origin_iterator.next() for _ in range(len(_in))]
...     if _in != res: print(_in, res)
...     gotcha.append(_in == res)
...     gotcha.append(origin_iterator.has_next() is False)
...     gotcha.append(origin_iterator.next() is None)
...
...     res = []
...     origin_iterator = ListIterator(_in)
...     freq_iterator = FreqIterator(origin_iterator)
...     while freq_iterator.has_next():
...         res.append(freq_iterator.next())
...
...     if res != _out: print(_in, res)
...     gotcha.append(res == _out)
>>> bool(gotcha) and all(gotcha)
True
"""


class FreqIterator:
    def __init__(self, iterator):
        if not iterator or not iterator.has_next():
            return

        self.iterator = iterator
        self.pre = None
        self.word = iterator.next()

    def next(self):
        if not self.has_next():
            return

        cnt = 1
        nxt = None

        while self.iterator.has_next():
            nxt = self.iterator.next()
            if nxt != self.word:
                break
            cnt += 1

        self.pre = self.word
        self.word = nxt
        return [self.pre, cnt]

    def has_next(self):
        return self.pre != self.word and self.word is not None


class ListIterator:
    def __init__(self, words):
        self.words = words
        self.i = 0

    def next(self):
        if not self.has_next():
            return

        res = self.words[self.i]
        self.i += 1
        return res

    def has_next(self):
        if self.i < len(self.words):
            return True

        return False
