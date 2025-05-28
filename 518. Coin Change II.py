# 1. For example, 8 = 2 + 6 = 6 + 2, so we need another state to mark the latest coin under consideration.
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[0 for j in range(amount + 1)] for i in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = 1
        for i, c in enumerate(coins):
            for j in range(1, amount + 1):
                if j - c >= 0:
                    dp[i + 1][j] = dp[i + 1][j - c] + dp[i][j]
                else:
                    dp[i + 1][j] = dp[i][j]
        return dp[n][amount]