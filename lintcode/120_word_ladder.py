"""
Test Case:

"a"
"a"
["b"]
=> should check again words in queue
"""


class Solution:
    def ladderLength(self, s, e, D):
        """
        :type s: str
        :type e: str
        :type D: List[str]
        :rtype: int
        """
        if (not s or not e or
            len(s) != len(e) or not D):
            return 0
        if s == e:
            return 1

        if s not in D:
            D.append(s)
        if e not in D:
            D.append(e)

        n = len(s)
        next_words = [None] * n
        for i in range(n):
            next_words[i] = _words = {}
            for word in D:
                key = word[:i] + word[i + 1:]
                if key not in _words:
                    _words[key] = set()
                _words[key].add(word)

        queue = [e]
        distance = {e: 1}
        for word in queue:
            for _word in self.get_next_word(word, next_words):
                if _word in distance:
                    continue
                distance[_word] = distance[word] + 1
                if _word == s:
                    return distance[_word]
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
