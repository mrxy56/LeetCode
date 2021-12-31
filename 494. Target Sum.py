# A variation of 0-1 knapsack, pay attention to the 'sums < 0' situation.
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        sums = sum(nums)
        sums -= target
        if sums < 0:
            return 0
        if sums % 2 == 1:
            return 0
        sums = sums // 2
        dp = [0 for i in range(sums + 1)]
        dp[0] = 1
        for num in nums:
            for v in range(sums, -1, -1):
                if v >= num:
                    dp[v] += dp[v - num]
        return dp[sums]