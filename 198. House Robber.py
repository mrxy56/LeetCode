# 1. Pay attention that j can be any number with at least 2 differences with i.
# 2. Edge cases.
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0 for i in range(n)]
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        for i in range(n):
            dp[i] = nums[i]
        for i in range(2, n):
            for j in range(0, i - 1):
                dp[i] = max(dp[i], dp[j] + nums[i])
        ans = 0
        for i in range(n):
            ans = max(ans, dp[i])
        return ans