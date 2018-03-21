"""
Main Concept:

Topological Sort
1. record `edges` and `indegrees` from `seqs`, and only allow `num` in `org`
2. iterate `org` in order, check if there is only one path to get `org[-1]`
"""


class Solution:
    def sequenceReconstruction(self, org, seqs):
        """
        :type org: list[int]
        :type seqs: list[list[int]]
        :rtype: bool
        """
        if org is None or seqs is None:
            return False

        n = len(org)
        edges = dict.fromkeys(org)
        indeg = dict.fromkeys(org, 0)

        cnt = 0
        for seq in seqs:
            if not seq:
                continue

            cnt += len(seq)

            for i in range(len(seq)):
                if not (1 <= seq[i] <= n):
                    return False
                if not edges[seq[i]]:
                    edges[seq[i]] = set()

                # dedup same edge
                if i > 0 and seq[i] not in edges[seq[i - 1]]:
                    indeg[seq[i]] += 1
                    edges[seq[i - 1]].add(seq[i])

        # for case: org == [1], seqs == [[], []]
        if cnt < n:
            return False

        for i in range(n - 1):
            if indeg[org[i]] != 0:
                return False
            if org[i + 1] not in edges[org[i]]:
                return False
            indeg[org[i + 1]] -= 1

        return True
