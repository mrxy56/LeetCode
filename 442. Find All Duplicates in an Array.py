# 1. Negative mark, make sure to recover the number to the positive one before mapping to its position.
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            x = abs(num)
            if nums[x - 1] < 0:
                ans.append(x)
            nums[x - 1] *= -1
        return ans