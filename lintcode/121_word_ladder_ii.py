class Solution:
    """
    0. Build `transform_set` in advance to speed up
    1. Use BFS from `end` to `start` to calculate the distance guide
    2. Use DFS step by step to find all possible path to get `end`
    """

    ans = []

    transform_set = None
    distance = None

    """
    @param: start: a string
    @param: end: a string
    @param: dictionary: a set of string
    @return: a list of lists of string
    """
    def findLadders(self, start, end, dictionary):
        if not start or not end \
                or len(start) != len(end) \
                or not dictionary:
            return self.ans

        dictionary.add(start)
        dictionary.add(end)

        self.build_transform_set(dictionary, len(start))
        self.bfs(start, end)
        self.dfs(start, end, [start])

        return self.ans

    def build_transform_set(self, dictionary, word_size):
        self.transform_set = []
        for i in range(word_size):
            transforms = {}
            for word in dictionary:
                key = word[:i] + word[i + 1:]
                if key not in transforms:
                    transforms[key] = []
                transforms[key].append(word)
            self.transform_set.append(transforms)

    def get_next_word(self, word):
        for i in range(len(word)):
            key = word[:i] + word[i + 1:]
            if key not in self.transform_set[i]:
                continue
            for next_word in self.transform_set[i][key]:
                if next_word != word:
                    yield next_word

    def bfs(self, start, end):
        self.distance = {}
        self.distance[end] = 0
        queue = [end]
        for word in queue:
            if word == start:
                break
            for next_word in self.get_next_word(word):
                if next_word in self.distance:
                    continue
                self.distance[next_word] = self.distance[word] + 1
                queue.append(next_word)

    def dfs(self, start, end, path):
        if start == end:
            # method 1: backtracking
            # note that need to shallow clone
            self.ans.append(path[:])

            # method 2: return new list
            # self.ans.append(path)

            return
        for next_word in self.get_next_word(start):
            if next_word not in self.distance:
                continue
            if self.distance[start] - 1 == self.distance[next_word]:
                # method 1: backtracking
                path.append(next_word)
                self.dfs(next_word, end, path)
                path.pop()

                # method 2: return new list
                # self.dfs(next_word, end, path + [next_word])
