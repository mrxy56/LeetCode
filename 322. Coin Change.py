# CompletePack again, pay attention to the index
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [10010 for i in range(amount + 1)]
        dp[0] = 0
        coins.sort()
        for v in range(amount + 1):
            for coin in coins:
                if coin > v:
                    break
                dp[v] = min(dp[v], dp[v - coin] + 1)
        if dp[amount] == 10010:
            return -1
        else:
            return dp[amount]