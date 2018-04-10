class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of = None


class Solution:
    def boggleGame(self, board, words):
        """
        :type board: list[list[str]]
        :type words: list[str]
        :rtype: int
        """
        self.ans = 0

        if not board or not board[0]:
            return self.ans


        root = TrieNode()

        for word in words:
            self.put(root, word)


        m, n = len(board), len(board[0])
        visited = set()

        for x in range(m):
            for y in range(n):
                self.dfs(board, x, y, root, visited, 0)


        return self.ans

    def dfs(self, board, i, j, root, visited, cnt):
        m, n = len(board), len(board[0])

        for x in range(i, m):
            for y in range(j, n):
                next_words = []
                self.find_next_words(board, x, y, visited, cnt, root, next_words, [])

                for pos in next_words:
                    for p in pos:
                        visited.add(p)

                    self.dfs(board, x, y, root, visited, cnt + 1)

                    for p in pos:
                        visited.discard(p)

            j = 0

    def find_next_words(self, board, x, y, visited, cnt, node, next_words, path):
        if (x, y) in visited or board[x][y] not in node.children:
            return

        m, n = len(board), len(board[0])
        node = node.children[board[x][y]]

        path.append((x, y))
        visited.add((x, y))

        if node.end_of is not None:
            next_words.append(path[:])
            self.ans = max(self.ans, cnt + 1)
        else:
            for dx, dy in (
                (-1, 0), (1, 0),
                (0, -1), (0, 1),
            ):
                _x = x + dx
                _y = y + dy

                if not (0 <= _x < m and 0 <= _y < n):
                    continue

                self.find_next_words(board, _x, _y, visited, cnt, node, next_words, path)

        path.pop()
        visited.discard((x, y))

    def put(self, root, word):
        node = root

        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()

            node = node.children[c]

        node.end_of = word
