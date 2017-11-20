"""
Test Case:

1
[]
"""


class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: the course order
    """
    def findOrder(self, numCourses, prerequisites):
        ans = []
        if not numCourses:
            return ans

        adjacency = [[] for _ in range(numCourses)]
        in_degree = [0 for _ in range(numCourses)]
        for course, prerequisite in prerequisites:
            adjacency[prerequisite].append(course)
            in_degree[course] += 1

        """
        1. if the `in_degree` of a course is 0,
           and then this course is able to take
        2. Use BFS to traversal `adjacency`,
           and reduce the `in_degree` of the downstream courses
        3. repeat (1)
        """
        queue = []
        for course in range(numCourses):
            if in_degree[course] is 0:
                queue.append(course)

        for course in queue:
            ans.append(course)
            for prerequisite in adjacency[course]:
                in_degree[prerequisite] -= 1
                if in_degree[prerequisite] is 0:
                    queue.append(prerequisite)

        return ans if len(ans) == numCourses else []
