# 1. Negative Marking.
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for num in nums:
            tmp = abs(num)
            if nums[tmp] < 0:
                return tmp
            nums[tmp] *= -1