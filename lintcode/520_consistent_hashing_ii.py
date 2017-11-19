import bisect
import random

class Solution:
    """
    @param {int} n a positive integer
    @param {int} k a positive integer
    @return {Solution} a Solution object
    """
    @classmethod
    def create(cls, n, k):
        solution = cls()
        solution.n = n
        solution.k = k
        solution.p2l = {} # point to location
        solution.l2p = {} # location to points
        return solution

    """
    @param: machine_id: An integer
    @return: a list of shard ids
    """
    def addMachine(self, machine_id):
        item = self.l2p[machine_id] = []
        point = -1
        for i in range(self.k):
            point = random.randint(0, self.n - 1)
            while point in self.p2l:
                point = random.randint(0, self.n - 1)
            self.p2l[point] = machine_id
            item.append(point)
        item.sort()
        return item

    """
    @param: hashcode: An integer
    @return: A machine id
    """
    def getMachineIdByHashCode(self, hashcode):
        points = sorted(self.p2l.keys())
        index = bisect.bisect_left(points, hashcode) % len(points)
        # # counterclockwise
        # index = bisect.bisect(points, hashcode) - 1
        # if index < 0:
        #     index = len(points) - 1
        return self.p2l[points[index]]
