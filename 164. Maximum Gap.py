class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        n = len(nums)
        for i in range(1, n):
            ans = max(ans, nums[i] - nums[i - 1])
        return ans