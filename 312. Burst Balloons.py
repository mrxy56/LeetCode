# You need to decide the state transition equation, and also need to decide iterate order. And pay attention to the indexes we use.
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0 for j in range(n)] for i in range(n)]
        for left in range(n - 2, 0, -1):
            for right in range(left, n - 1):
                for i in range(left, right +1):
                    tmp = nums[left - 1] * nums[i] * nums[right + 1]
                    dp[left][right] = max(dp[left][i - 1] + dp[i + 1][right] + tmp, dp[left][right])
        return dp[1][n - 2]
        
        