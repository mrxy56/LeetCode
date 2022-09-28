class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif nums[m] >= nums[l]: # First determine shape
                if target >= nums[l] and target < nums[m]: # Then finish the determined case
                    r = m - 1
                else:
                    l = m + 1 # leave the rest to else
            else:
                if target <= nums[r] and target > nums[m]:
                    l = m + 1
                else:
                    r = m - 1
        return -1