# 1. Two pointers, check j - 2 instead of i - 2.
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cnt = 0
        n = len(nums)
        j = 0
        for i in range(n):
            if i == 0 or i == 1:
                j += 1
            else:
                if nums[i] != nums[j - 2]:
                    nums[j] = nums[i]
                    j += 1
        return j