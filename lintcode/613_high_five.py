"""
Definition for a Record
class Record:
    def __init__(self, id, score):
        self.id = id
        self.score = score
"""
from heapq import heappop, heappush


class Solution:
    # @param {Record[]} results a list of <student_id, score>
    # @return {dict(id, average)} find the average of 5 highest scores for each person
    # <key, value> (student_id, average_score)
    def highFive(self, results):
        ans = {}
        if not results:
            return ans

        k = 5
        top_k = {}

        for r in results:
            if r.id not in top_k:
                top_k[r.id] = []

            heappush(top_k[r.id], r.score)

            if len(top_k[r.id]) > k:
                heappop(top_k[r.id])

        _sum = 0
        for id, scores in top_k.items():
            _sum = 0
            for score in scores:
                _sum += score

            ans[id] = _sum * 1.0 / k

        return ans
