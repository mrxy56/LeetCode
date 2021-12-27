# Simple DP, for each state, you transit to another state, while step + 1, pay attention to initialization.
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [10000 for i in range(n)]
        dp[0] = 0
        for i in range(n):
            for j in range(i - nums[i], i + nums[i] + 1):
                if j >= 0 and j < n:
                    dp[j] = min(dp[i] + 1, dp[j])
        return dp[-1]