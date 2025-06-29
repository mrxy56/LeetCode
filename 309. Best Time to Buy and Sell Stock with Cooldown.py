class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [0 for i in range(n + 2)]
        if n < 2:
            return 0
        if n == 2:
            return max(prices[1] - prices[0], 0)
        for i in range(3, n + 2):
            dp[i] = dp[i - 1]
            for j in range(i - 1, 1, -1):
                if prices[i - 2] - prices[j - 2] > 0:
                    dp[i] = max(dp[j - 2] + prices[i - 2] - prices[j - 2], dp[i])
        return dp[n + 1]