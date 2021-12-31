# each day two strategies, first is buy yesterday and sell today, second is do not move. 
# Nothing relavant to 2 days before since you cannot keep the stock for 2 days.
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [0 for i in range(n)]
        for i in range(1, n):
            dp[i] = max(dp[i - 1] + prices[i] - prices[i - 1], dp[i - 1])
        return dp[n - 1]