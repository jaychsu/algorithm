"""
>>> gotcha = []
>>> for words, _out in (
...     (['apple', 'price', 'tuple', 'agile'], 'apple'),
...     (['apple', 'apple', 'apple', 'apple'], 'apple'),
...     (['aa', 'ab', 'ac', 'ad', 'ae', 'af', 'ag'], 'ae'),
...     (['aa', 'ab', 'ac', 'ad', 'ae', 'af', 'ag'], 'ag'),
...     (['aa', 'ab', 'ab', 'ac'], 'ab'),
... ):
...     secret = Secret(_out)
...     res = find_secret(secret, words)
...     if res != _out: print(words, res, secret.score)
...     gotcha.append(res == _out)
>>> bool(gotcha) and all(gotcha)
True
"""


def find_secret(secret, words):
    if not isinstance(secret, Secret):
        return ''

    while len(words) > 1:
        has_got, correct_cnt = secret.guess(words[-1])
        guess_word = words.pop()

        if has_got:
            return guess_word

        _words = []
        n = len(guess_word)

        for word in words:
            cnt = 0

            for i in range(n):
                if word[i] == guess_word[i]:
                    cnt += 1

            if cnt == len(word):
                return word
            if cnt == correct_cnt:
                _words.append(word)

        words = _words

    return words[0]


class Secret:
    def __init__(self, word):
        self.secret = word
        self.score = 0

    def guess(self, word):
        if not word or len(word) != len(self.secret):
            return

        cnt = 0

        for i in range(len(word)):
            if word[i] == self.secret[i]:
                cnt += 1

        self.score -= 1

        return [cnt == len(word), cnt]
