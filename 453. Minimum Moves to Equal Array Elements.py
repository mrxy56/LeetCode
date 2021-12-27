# Every move makes the difference of diff between two numbers, think about pouring water.
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        for i in range(len(nums)):
            if i == 0:
                continue
            else:
                ans += nums[i] - nums[0]
        return ans
            