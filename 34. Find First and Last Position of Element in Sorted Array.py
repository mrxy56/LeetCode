class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums) - 1
        start = -1
        end = -1
        while l <= r:
            m = (l + r) // 2
            if m == 0 and nums[m] == target or nums[m] == target and nums[m - 1] < target:
                start = m
                break
            if target <= nums[m]: # Pay attention to the search direction.
                r = m - 1
            else:
                l = m + 1
            if r < 0 or l > len(nums) - 1: # index must be valid
                return [-1, -1]
        
        l = 0
        r = len(nums) - 1
            
        while l <= r:
            m = (l + r) // 2
            if m == len(nums) - 1 and nums[m] == target or nums[m] == target and nums[m + 1] > target:
                end = m
                break
            if target >= nums[m]: # The = is subtle.
                l = m + 1
            else:
                r = m - 1
            if r < 0 or l > len(nums) - 1:
                return [-1, -1]
            
        return [start, end]