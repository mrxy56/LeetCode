# 1. Initial value should be 10 ** 5 + 1 to avoid collisions.
class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        dis = 10 ** 5 + 1
        ans = 0
        for num in nums:
            if abs(num) == dis:
                if num >= 0:
                    ans = num
            elif abs(num) < dis:
                dis = abs(num)
                ans = num
        return ans