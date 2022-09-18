class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r: # loop stops when l > r, since nums[l] > nums[r], insert l
            p = (l + r)//2
            if nums[p] == target:
                return p
            if target < nums[p]:
                r = p - 1
            else:
                l = p + 1
        return l