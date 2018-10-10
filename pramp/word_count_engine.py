"""
>>> gotcha = []
>>> for _in, _out in (
...     (
...         "Practice makes perfect. you'll only get Perfect by practice. just practice!",
...         [['practice', 3], ['perfect', 2], ['makes', 1], ['youll', 1], ['only', 1], ['get', 1], ['by', 1], ['just', 1]],
...     ),
...     (
...         "Practice makes perfect. just practice! you'll only get Perfect by practice.",
...         [['practice', 3], ['perfect', 2], ['makes', 1], ['just', 1], ['youll', 1], ['only', 1], ['get', 1], ['by', 1]],
...     ),
...     (
...         "Practice makes perfect. you'll only get Perfect by practice. just practice by yourself!",
...         [['practice', 3], ['perfect', 2], ['by', 2], ['makes', 1], ['youll', 1], ['only', 1], ['get', 1], ['just', 1], ['yourself', 1]],
...     ),
... ):
...     res = word_count_engine(_in)
...     if res != _out: print(_in, res)
...     gotcha.append(res == _out)
>>> bool(gotcha) and all(gotcha)
True
"""


def word_count_engine(document):
    """
    :type document: str
    :rtype: list[list[str]]

    count and sort
    time: O(n logn)
    """
    ans = []
    document = document and document.strip()

    if not document:
        return ans

    document = ''.join(c for c in document if c.isalnum() or c == ' ')
    word2idx = {}

    for word in document.lower().strip().split():
        if not word:
            continue

        if word not in word2idx:
            ans.append([word, 0])
            word2idx[word] = len(ans) - 1

        i = word2idx[word]
        ans[i][1] += 1

    ans.sort(key=lambda x: x[1], reverse=True)
    return ans


def word_count_engine2(document):
    """
    :type document: str
    :rtype: list[list[str]]

    # TODO
    LRU
    time: O(n)
    """
    pass
