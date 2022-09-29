class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        if len(nums) == 1:
            return 0
        while l <= r:
            m = (l + r) // 2
            if m == 0 and nums[m] > nums[m + 1] or m == len(nums) - 1 and nums[m] > nums[m - 1]:
                return m
            if nums[m] > nums[m + 1] and nums[m] > nums[m - 1]:
                return m
            if nums[m + 1] > nums[m]:
                l = m + 1
            else:
                r = m - 1
                