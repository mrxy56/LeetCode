# Stuck in the middle though very classical problem.
# dp[i] means the LIS ending at i, so it records two info,
# one is the longest length, another is where, finally we need to go through all dps.
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1 for i in range(n)]
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[j] + 1, dp[i])
        ans = 0
        for i in range(n):
            ans = max(ans, dp[i])
        return ans        