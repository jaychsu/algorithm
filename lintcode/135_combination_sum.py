class Solution:
    ans = []

    """
    @param: candidates: A list of integers
    @param: target: An integer
    @return: A list of lists of integers
    """
    def combinationSum(self, candidates, target):
        if not candidates:
            return self.ans

        self.dfs(
            sorted(list(set(candidates))),
            target,
            0,
            []
        )

        return self.ans

    def dfs(self, candidates, remaining, start, combination):
        if remaining == 0:
            self.ans.append(combination)
            return

        for i in range(start, len(candidates)):
            if remaining < candidates[i]:
                # since `nums[i + 1]` > `nums[i]`
                # -> nums[i + 1]` > `nums[i]` > remaining
                # -> no need to iterate
                return
            self.dfs(
                candidates,
                remaining - candidates[i],
                i, # not `i + 1` since pick repeated one is allowed
                combination + [candidates[i]]
            )
