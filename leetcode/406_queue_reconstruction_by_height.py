"""
Main Concept:

1. group the mans with same height and record origin index
2. record all heights
3. sort heights and iterate from end to start
4. get the corresponding mans and insert to `k` index

input: [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]

heights: [4, 5, 6, 7]

process:

7 [(0, 0), (1, 2)]  # input[0], input[2]
[[7, 0]]
[[7, 0], [7, 1]]

6 [(1, 4)]
[[7, 0], [6, 1], [7, 1]]

5 [(0, 3), (2, 5)]
[[5, 0], [7, 0], [6, 1], [7, 1]]
[[5, 0], [7, 0], [5, 2], [6, 1], [7, 1]]

4 [(4, 1)]
[[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]]
"""


class Solution:
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        ans = []

        if not people:
            return ans

        people.sort(key=lambda p: (p[0], -p[1]))

        for i in range(len(people) - 1, -1, -1):
            ans.insert(people[i][1], people[i])

        return ans


class Solution:
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        ans = []

        if not people:
            return ans

        h2mans = {}
        heights = []

        for i in range(len(people)):
            h, k = people[i]

            if h in h2mans:
                h2mans[h].append((k, i))
            else:
                h2mans[h] = [(k, i)]
                heights.append(h)

        heights.sort()

        for height in heights[::-1]:
            for k, i in sorted(h2mans[height]):
                ans.insert(k, people[i])

        return ans
