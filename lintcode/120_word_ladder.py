"""
Test Case:

"a"
"a"
["b"]
=> should check again words in queue
"""


class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: D: a set of string
    @return: An integer
    """
    def ladderLength(self, start, end, D):
        if (not start or not end or
            len(start) != len(end) or
            not D):
            return 0

        if start not in D:
            D.add(start)
        if end not in D:
            D.add(end)

        n = len(start)
        next_words = [None] * n
        for i in range(n):
            next_words[i] = _words = {}
            for word in D:
                key = word[:i] + word[i + 1:]
                if key not in _words:
                    _words[key] = set()
                _words[key].add(word)

        distance = {end: 1}
        queue = [end]
        for word in queue:
            if word == start:
                return distance[word]

            for _word in self.get_next_word(word, next_words):
                if _word in distance:
                    continue

                distance[_word] = distance[word] + 1
                queue.append(_word)

        return 0

    def get_next_word(self, word, next_words):
        for i in range(len(word)):
            key = word[:i] + word[i + 1:]
            if key not in next_words[i]:
                continue
            for _word in next_words[i][key]:
                if _word == word:
                    continue
                yield _word
