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
        solution.point_locations = {}
        solution.machines = {}
        return solution

    """
    @param: machine_id: An integer
    @return: a list of shard ids
    """
    def addMachine(self, machine_id):
        ids = []
        point = -1
        for i in range(self.k):
            point = random.randint(0, self.n - 1)
            while point in self.point_locations:
                point = random.randint(0, self.n - 1)
            self.point_locations[point] = machine_id
            ids.append(point)
        ids.sort()
        self.machines[machine_id] = ids
        return ids

    """
    @param: hashcode: An integer
    @return: A machine id
    """
    def getMachineIdByHashCode(self, hashcode):
        points = sorted(self.point_locations.keys())
        index = bisect.bisect_left(points, hashcode)
        if index >= len(points):
            index = 0
        # # counterclockwise
        # index = bisect.bisect(points, hashcode) - 1
        # if index < 0:
        #     index = len(points) - 1
        #
        return self.point_locations[points[index]]
