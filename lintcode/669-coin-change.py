# REF: https://leetcode.com/articles/coin-change/
"""
Test Case:

[21,31,51]
91
-> P[amount] > amount

"""
class Solution:
    """
    @param: coins: a list of integer
    @param: amount: a total amount of money amount
    @return: the fewest number of coins that you need to make up
    """
    def coinChange(self, coins, amount):
        if not coins or not amount:
            return 0
        m, n = amount + 1, len(coins)
        P = [m for _ in range(m)]
        P[0] = 0

        for total in range(m):
            for deno in range(n):
                if coins[deno] <= total \
                        and P[total - coins[deno]] + 1 < P[total]:
                    P[total] = P[total - coins[deno]] + 1

        # since the init value of each child in `P` is `m == amount + 1`
        # so if `P[amount] > amount` means it not changed -> not valid
        return -1 if P[amount] > amount else P[amount]
