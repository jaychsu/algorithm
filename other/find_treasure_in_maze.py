"""
http://acm.nyist.edu.cn/JudgeOnline/problem.php?pid=82


Description:
一个叫ACM的寻宝者找到了一个藏宝图，它根据藏宝图找到了一个迷宫，
这是一个很特别的迷宫，迷宫里有N个编过号的门（N<=5)，
它们分别被编号为A,B,C,D,E.为了找到宝藏，ACM必须打开门，
但是，开门之前必须在迷宫里找到这个打开这个门所需的所有钥匙（每个门都至少有一把钥匙），
例如：现在A门有三把钥匙，ACM就必须找全三把钥匙才能打开A门。
现在请你编写一个程序来告诉ACM，他能不能顺利的得到宝藏。

每组测试数据的第一行包含了两个整数M,N(1<N,M<20)，分别代表了迷宫的行和列。接下来的M每行有N个字符，描述了迷宫的布局。其中每个字符的含义如下：
.表示可以走的路
S:表示ACM的出发点
G:表示宝藏的位置
X:表示这里有墙，ACM无法进入或者穿过。
A,B,C,D,E表示这里是门，a,b,c,d,e表示对应大写字母的门上的钥匙。
注意ACM只能在迷宫里向上下左右四个方向移动。


Testing:
>>> s = Solution()
>>> gotcha = []
>>> for _in, _out in (
...     (['S.X.', 'a.X.', '..XG', '....'], True),
...     (['S.Xa', '.aXB', 'b.AG'], False),
...     (['aX.S', 'bXAB', 'cXCD', 'dXGX'], False),
...     (['SbAdX.', 'a.BD.G', 'cBCdaX'], True),
...     (['S.Aa.X.', 'a.Xc.C.', 'b.X..DG', '.cB..Xd'], True),
... ):
...     res = s.find_treasure_in_maze(_in)
...     if res != _out: print(_in, res)
...     gotcha.append(res == _out)
>>> bool(gotcha) and all(gotcha)
True
"""


class Solution:
    START = 'S'
    GOLD = 'G'
    OBSTACLE = 'X'
    EMPTY = '.'
    DOORS = 'ABCDE'
    KEYS = 'abcde'

    def find_treasure_in_maze(self, maze):
        """
        :type maze: list[str]
        :rtype: bool
        """
        if not maze or not maze[0]:
            return False

        m, n = len(maze), len(maze[0])
        k = len(self.DOORS)
        keys = [0] * k  # all keys count
        has_gold = False

        queue = []
        doors = [None] * k  # doors meet when bfs
        holds = [0] * k  # keys meet when bfs
        visited = set()  # visited cell when bfs

        for x in range(m):
            for y in range(n):
                if maze[x][y] == self.START:
                    queue.append((x, y))
                elif maze[x][y] == self.GOLD:
                    has_gold = True
                elif maze[x][y] in self.KEYS:
                    i = ord(maze[x][y]) - ord('a')
                    keys[i] += 1

        if not has_gold or not queue:
            return False

        while queue or self.is_possible(maze, keys, holds, doors):
            if self.bfs(maze, queue, keys, holds, doors, visited):
                return True

        return False

    def bfs(self, maze, queue, keys, holds, doors, visited):
        """
        return True if got gold, otherwise False

        :type maze: list[str]
        :type queue: list[tuple[int]]
        :type keys: list[int]
        :type holds: list[int]
        :type doors: list[tuple[int]]
        :type visited: set[tuple[int]]
        :rtype: bool
        """
        m, n = len(maze), len(maze[0])

        for x, y in queue:
            for dx, dy in (
                (0, -1), (0, 1),
                (-1, 0), (1, 0),
            ):
                _x = x + dx
                _y = y + dy

                if not (0 <= _x < m and 0 <= _y < n):
                    continue
                if (_x, _y) in visited or maze[_x][_y] == self.OBSTACLE:
                    continue
                if maze[_x][_y] == self.GOLD:
                    return True

                if maze[_x][_y] in self.DOORS:
                    i = ord(maze[_x][_y]) - ord('A')
                    if holds[i] < keys[i]:
                        doors[i] = (_x, _y)
                        continue
                    doors[i] = None

                if maze[_x][_y] in self.KEYS:
                    i = ord(maze[_x][_y]) - ord('a')
                    holds[i] += 1

                visited.add((_x, _y))
                queue.append((_x, _y))

        queue.clear()
        return False

    def is_possible(self, maze, keys, holds, doors):
        """
        :type maze: list[str]
        :type keys: list[int]
        :type holds: list[int]
        :type doors: list[tuple[int]]
        :rtype: bool
        """
        for door in doors:
            if not door:
                continue

            x, y = door
            i = ord(maze[x][y]) - ord('A')
            if holds[i] >= keys[i]:
                return True

        return False
