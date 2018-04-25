"""
Given a robot cleaner in a room modeled as a grid.
Each cell in the grid can be empty or blocked.
The robot cleaner with 4 given APIs can move forward, turn left or turn right.
When it tries to move into a blocked cell,
its bumper sensor detects the obstacle and it stays on the current cell.

The 4 APIs are:
clean(): clean the current location.
turnleft(k=1): turn left k*90 degrees.
turnrigt(k=1): turn right k*90 degrees.
move(direction=None): move forward for 1 position, return False if that’s not possible.

- How do you clean the entire space?
- How long will it take? (1 step == 1 time unit)
- Can you show paths?


Need to ask:

- is there an api to detect the cell need to clean?
- are both the robot's direction and coordinate need to same as room?
- once we called the `move` api and passed a direction.
  will the robot turn its face in that direction?
  and move forward with 1 unit?


REF:

- http://www.hoangvancong.com/2016/10/28/bfs-backtrack-robot-don-dep-cleaning-robot
- https://blog.csdn.net/aozil_yang/article/details/52177644
- http://www.1point3acres.com/bbs/thread-289514-1-1.html
- http://www.1point3acres.com/bbs/thread-345555-1-1.html


Testing:

1. is the mock api working?

>>> room = Room([
...     [0, 0, 0, 0, 0, 0, 0, 0],
...     [0, 0, 0, 1, 0, 0, 0, 0],
...     [0, 2, 0, 0, 0, 0, 0, 0],
...     [2, 2, 2, 0, 2, 2, 2, 2],
...     [0, 0, 0, 0, 0, 0, 0, 3],
... ])
>>> robot = Robot(room)
>>> all((
...     room._get_robot() == (4, 7),
...     robot._get_face() == Dirs.DOWN,
...     robot.move() is False,
...     robot.turnleft() is None,
...     robot.move() is False,
...     robot.turnrigt() is None,
...     robot.move() is False,
...     robot.turnleft(3) is None,
...     robot.move() is True,
...     room._get_robot() == (4, 6),
... ))
True
>>> all((
...     robot.move() is True,
...     robot.move(Dirs.LEFT) is True,
...     robot.turnleft(2) is None,
...     robot.turnrigt(2) is None,
...     robot.move() is True,
...     room._get_robot() == (4, 3),
... ))
True
>>> all((
...     robot._get_face() == Dirs.LEFT,
...     robot.move(Dirs.UP) is True,
...     robot.turnleft() is None,
...     robot.move() is False,
...     robot.turnrigt(2) is None,
...     robot.move() is False,
...     robot.turnleft() is None,
... ))
True
>>> all((
...     robot.move() is True,
...     robot.turnleft() is None,
...     robot.move() is True,
...     robot.move() is False,
...     robot.move() is False,
...     robot.move() is False,
...     robot.turnrigt() is None,
...     robot.move() is True,
...     robot.turnrigt() is None,
... ))
True
>>> all((
...     room._get_robot() == (1, 2),
...     robot.move() is True,
...     room.is_clear() is False,
...     robot.clean() is None,
...     room.is_clear() is True,
...     robot.clean() is None,
...     room.is_clear() is True,
...     room.is_clear() is True,
... ))
True

2. test cleaner

>>> CASES = (
...     (
...         (3, 0, 0, 0, 0, 0, 1, 0),
...         (0, 0, 0, 0, 0, 0, 0, 0),
...         (0, 2, 0, 0, 0, 0, 0, 0),
...         (2, 2, 2, 0, 2, 2, 2, 2),
...         (0, 0, 1, 0, 0, 0, 1, 0),
...     ),
...     (
...         (0, 0, 0, 0, 0, 0, 0, 0),
...         (0, 0, 1, 0, 2, 0, 0, 0),
...         (1, 2, 0, 0, 2, 1, 0, 0),
...         (2, 2, 2, 0, 2, 2, 2, 2),
...         (1, 0, 0, 0, 0, 0, 0, 3),
...     ),
...     (
...         (1, 0, 0, 0, 0, 0, 0, 1),
...         (0, 0, 0, 1, 0, 0, 0, 0),
...         (0, 2, 0, 0, 0, 0, 1, 0),
...         (2, 2, 2, 0, 2, 2, 2, 2),
...         (0, 1, 0, 3, 0, 1, 0, 1),
...     ),
...     (
...         (0, 0, 0, 0, 0, 0, 0, 1),
...         (0, 0, 0, 1, 2, 0, 3, 0),
...         (0, 2, 0, 0, 2, 1, 0, 0),
...         (2, 2, 2, 1, 2, 2, 2, 2),
...         (0, 1, 0, 0, 1, 0, 0, 1),
...     ),
... )

>>> cleaners = (
...     RobotCleanerDFS(),
...     RobotCleanerDFS2(),
...     # RobotCleanerBFS(),
... )

>>> gotcha = []
>>> for grid in CASES:
...     for cleaner in cleaners:
...         room = Room([list(r) for r in grid])
...         robot = Robot(room)
...
...         gotcha.append(not room.is_clear())
...         cleaner.clean_room(robot)
...
...         if not room.is_clear(): room._print_room(); print(cleaner)
...         gotcha.append(room.is_clear())
>>> bool(gotcha) and all(gotcha)
True
"""


class Dirs:
    """
    The directions should be in order
    to make turnleft/right in Robot more convient
    if need 8-dirs, the order becomes:
    D, DR, R, UR, U, UL, L, DL
    """
    DOWN = 0
    RIGHT = 1
    UP = 2
    LEFT = 3
    DELTA = (
        ( 1,  0),
        ( 0,  1),
        (-1,  0),
        ( 0, -1),
    )


class Room:
    EMPTY = 0
    CLEANUP = 1
    OBSTACLE = 2
    ROBOT = 3

    def __init__(self, grid):
        """
        :type grid: list[list[int]]
        """
        self.__room = grid
        self.__cleanups = 0
        self.__robot_at = (0, 0)

        m, n = len(grid), len(grid[0])

        for x in range(m):
            for y in range(n):
                if grid[x][y] == self.CLEANUP:
                    self.__cleanups += 1
                elif grid[x][y] == self.ROBOT:
                    grid[x][y] = self.EMPTY
                    self.__robot_at = (x, y)

    def is_clear(self):
        """
        :rtype: bool
        """
        return self.__cleanups == 0

    def move_robot(self, direction):
        """
        :type direction: int, defined in Dirs
        :rtype: bool
        """
        m, n = len(self.__room), len(self.__room[0])
        x, y = self.__robot_at
        dx, dy = Dirs.DELTA[direction]
        _x, _y = x + dx, y + dy

        if not (0 <= _x < m and 0 <= _y < n):
            return False

        if self.__room[_x][_y] == self.OBSTACLE:
            return False

        self.__robot_at = (_x, _y)
        return True

    def clean(self, robot):
        """
        :type robot: Robot
        :rtype: void
        """
        if not isinstance(robot, Robot):
            return

        x, y = self.__robot_at

        if self.__room[x][y] == self.CLEANUP:
            self.__room[x][y] = self.EMPTY
            self.__cleanups -= 1

    def _get_robot(self):
        # for testing
        return self.__robot_at

    def _print_room(self):
        # for testing
        print(
            '\n'.join(str(r) for r in self.__room),
            '\nRobot at: ', self.__robot_at,
            '\nCleanups: ', self.__cleanups,
            '\n'
        )


class Robot:
    def __init__(self, room):
        """
        :type room: Room
        """
        self.__room = room
        self.__face = Dirs.DOWN

    def move(self, direction=None):
        """
        :type direction: int, defined in Dirs
        :rtype: bool
        """
        if direction in range(len(Dirs.DELTA)):
            self.__face = direction

        return self.__room.move_robot(self.__face) is True

    def turnleft(self, k=1):
        """
        :type k: int
        :rtype: void
        """
        n = len(Dirs.DELTA)
        self.__face = (self.__face + k) % n

    def turnrigt(self, k=1):
        """
        :type k: int
        :rtype: void
        """
        # note that, -1 % 4 == 3 in Python, or just (x - k + n) % n
        n = len(Dirs.DELTA)
        self.__face = (self.__face - k) % n

    def clean(self):
        """
        :rtype: void
        """
        self.__room.clean(self)

    def _get_face(self):
        # for testing
        return self.__face


class RobotCleanerDFS:
    """
    this approach is for we need to adjust `dir` manually
    the `robot.move()` only can move forward with 1 step
    """
    def clean_room(self, robot):
        """
        :type robot: Robot
        """
        if not isinstance(robot, Robot):
            return

        """
        robot's direction and coord no needs to same as room
        just start as (0, 0),
        and face 0 (this 0 just ref of dirs, no needs to treat it as Dirs.DOWN)

        Dirs.DELTA => D, R, U, L
        (1, 0), (0, 1), (-1, 0), (0, -1)
        """
        self.dfs(0, 0, 0, robot, set())

    def dfs(self, x, y, to_dir, robot, visited):
        robot.clean()
        visited.add((x, y))

        # down
        d = to_dir
        _x = x + Dirs.DELTA[d][0]
        _y = y + Dirs.DELTA[d][1]

        if (_x, _y) not in visited and robot.move():
            self.dfs(_x, _y, d, robot, visited)
            robot.turnrigt()
        else:
            robot.turnleft()

        # right
        d = (to_dir + 1) % len(Dirs.DELTA)
        _x = x + Dirs.DELTA[d][0]
        _y = y + Dirs.DELTA[d][1]

        if (_x, _y) not in visited and robot.move():
            self.dfs(_x, _y, d, robot, visited)
        else:
            robot.turnleft(2)

        # left
        d = (to_dir + 3) % len(Dirs.DELTA)
        _x = x + Dirs.DELTA[d][0]
        _y = y + Dirs.DELTA[d][1]

        if (_x, _y) not in visited and robot.move():
            self.dfs(_x, _y, d, robot, visited)
            robot.turnleft()
        else:
            robot.turnrigt()

        # up
        d = (to_dir + 2) % len(Dirs.DELTA)
        _x = x + Dirs.DELTA[d][0]
        _y = y + Dirs.DELTA[d][1]

        if (_x, _y) not in visited and robot.move():
            self.dfs(_x, _y, d, robot, visited)
            robot.turnrigt(2)

        # move robot when the recursion is back
        robot.move()


class RobotCleanerDFS2:
    """
    this approach is for we can just pass `dir` into `robot.move(dir)`
    """
    def clean_room(self, robot):
        """
        :type robot: Robot
        """
        if not isinstance(robot, Robot):
            return

        """
        robot's direction and coord no needs to same as room
        just start as (0, 0),
        and face 0 (this 0 just ref of dirs, no needs to treat it as Dirs.DOWN)
        """
        self.dfs(0, 0, 0, robot, set())

    def dfs(self, x, y, from_dir, robot, visited):
        # is there a api to detect the cell need to clean?
        robot.clean()
        visited.add((x, y))

        for to_dir in range(len(Dirs.DELTA)):
            if to_dir == from_dir:
                continue

            # to_dir is index and also the direction defined in Dirs
            dx, dy = Dirs.DELTA[to_dir]
            _x = x + dx
            _y = y + dy

            if (_x, _y) in visited:
                continue

            if robot.move(to_dir):
                self.dfs(_x, _y, (to_dir + 2) % len(Dirs.DELTA), robot, visited)
            else:
                visited.add((_x, _y))

        robot.move(from_dir)


class RobotCleanerBFS:
    def clean_room(self, robot):
        """
        :type robot: Robot
        """
        if not isinstance(robot, Robot):
            return

    def bfs(self):
        pass


if __name__ == '__main__':
    # for debugging
    room = Room([
        [1, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 1, 0, 0, 0, 0],
        [0, 2, 0, 0, 0, 0, 1, 0],
        [2, 2, 2, 0, 2, 2, 2, 2],
        [0, 1, 0, 3, 0, 1, 0, 1],
    ])
    robot = Robot(room)
    s = RobotCleanerDFS()

    room._print_room()
    s.clean_room(robot)
    room._print_room()
