class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        ind = 0
        for i, num in enumerate(nums):
            if num > nums[ind]:
                ind = i
        for i, num in enumerate(nums):
            if i != ind and nums[i] * 2 > nums[ind]:
                return -1
        return ind