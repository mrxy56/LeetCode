# 1. Need to remember this pattern.
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        dp = [[[0 for t in range(2)] for kk in range(k + 1)] for pp in range(n + 1)]
        for i in range(n - 1, -1, -1):
            for j in range(1, k + 1):
                for t in range(2):
                    do_nothing = dp[i + 1][j][t]
                    if t:
                        do_something = prices[i] + dp[i + 1][j - 1][0]
                    else:
                        do_something = -prices[i] + dp[i + 1][j][1]
                    dp[i][j][t] = max(do_nothing, do_something)
        return dp[0][k][0]