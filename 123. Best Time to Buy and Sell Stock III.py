class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = len(prices)
        left_profits = [0 for i in range(l)]
        right_profits = [0 for i in range(l)]
        left_min = prices[0]
        right_max = prices[-1]
        for i in range(1, l):
            left_profits[i] = max(left_profits[i - 1], prices[i] - left_min) # Two-way DP, record the best solution in left part in one turn
            left_min = min(left_min, prices[i])
        for j in range(l - 2, -1, -1):
            right_profits[j] = max(right_profits[j + 1], right_max - prices[j]) # record the best solution in right part in one turn
            right_max = max(right_max, prices[j])
        ans = 0
        for i in range(l):
            ans = max(left_profits[i] + right_profits[i], ans)
        return ans