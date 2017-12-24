"""
Main Concept:

1. building `next_words` in advance to speed up
2. using BFS from `end` to `start` to calculate the distance guide
3. using DFS step by step to find all possible path to get `end`
"""


class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: D: a set of string
    @return: a list of lists of string
    """
    def findLadders(self, start, end, D):
        ans = []
        if (not start or not end or
            len(start) != len(end) or
            not D):
            return ans

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
                break
            for _word in self.get_next_word(word, next_words):
                if _word in distance:
                    continue
                distance[_word] = distance[word] + 1
                queue.append(_word)

        self.dfs(start, end, next_words, distance, ans, [start])

        return ans

    def dfs(self, start, end, next_words, distance, ans, path):
        if start == end:
            ans.append(path[:])
            return

        for _word in self.get_next_word(start, next_words):
            if (_word not in distance or
                distance[_word] != distance[start] - 1):
                continue
            path.append(_word)
            self.dfs(_word, end, next_words, distance, ans, path)
            path.pop()

    def get_next_word(self, word, next_words):
        for i in range(len(word)):
            key = word[:i] + word[i + 1:]
            if key not in next_words[i]:
                continue
            for _word in next_words[i][key]:
                if _word == word:
                    continue
                yield _word
