class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        nums = nums + nums
        ans = 0
        for i, num in enumerate(nums):
            if i == 0:
                continue
            ans = max(ans, abs(nums[i] - nums[i - 1]))
        return ans