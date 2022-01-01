class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        cost = cost + [0]
        dp = [0 for i in range(n + 1)]
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, n + 1):
            dp[i] = min(dp[i - 1] + cost[i], dp[i - 2] + cost[i])
        return dp[n]