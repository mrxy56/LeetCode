# many states if loop from left to right, since the problem requires jumping from left to right, calculate reversely can significantly reduce the states
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [0 for i in range(n)]
        dp[n - 1] = 1
        for i in range(n - 2, -1, -1):
            left = max(0, i - nums[i])
            right = min(n - 1, i + nums[i])
            for j in range(right, left - 1, -1):
                    if dp[j] == 1:
                        dp[i] = 1
                        break
        if dp[0] == 1:
            return True
        return False