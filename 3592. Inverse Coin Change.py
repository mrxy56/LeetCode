# 1. A variation of unbounded knapsack. Need to be more familiar with common DP questions.
class Solution:
    def findCoins(self, numWays: List[int]) -> List[int]:
        ans = []
        n = len(numWays)
        target = 0
        dp = [0 for i in range(n + 1)]
        dp[0] = 1
        for i in range(n):
            target = i + 1
            if dp[target] != numWays[i]:
                coin = target
                ans.append(coin)
                for j in range(1, n + 1):
                    if j - coin >= 0:
                        dp[j] += dp[j - coin]
                if dp[target] != numWays[i]:
                    return []
        return ans