# 0-1 knapsack pay attention to the order of v and i loop should be outside.
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        sums = 0
        for i in range(n):
            sums += nums[i]
        if sums % 2 == 1:
            return False
        sums = sums // 2
        dp = [0 for i in range(sums + 1)]
        dp[0] = 1
        for i in range(n):
            for v in range(sums, -1, -1):
                if v >= nums[i]:
                    dp[v] = dp[v - nums[i]] or dp[v]
        return dp[sums]