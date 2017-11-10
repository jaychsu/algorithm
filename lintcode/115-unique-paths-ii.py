class Solution:
    """
    @param: obstacleGrid: A list of lists of integers
    @return: An integer
    """
    def uniquePathsWithObstacles(self, obstacleGrid):
        mp = obstacleGrid
        for x in range(len(mp)):
            for y in range(len(mp[0])):
                if x == 0 and y == 0:
                    mp[x][y] = 1 if not mp[x][y] else 0
                elif x == 0:
                    mp[x][y] = mp[x][y-1] if not mp[x][y] else 0
                elif y == 0:
                    mp[x][y] = mp[x-1][y] if not mp[x][y] else 0
                else:
                    mp[x][y] = mp[x-1][y] + mp[x][y-1] if not mp[x][y] else 0
        return mp[-1][-1]
