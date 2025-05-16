class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        n = len(nums)
        m = len(multipliers)
        @lru_cache
        def dp(i, left):
            if i == m:
                return 0
            right = n - 1 - (i - left)
            return max(dp(i + 1, left) + nums[right] * multipliers[i], dp(i + 1, left + 1) + nums[left] * multipliers[i])
        return dp(0, 0)