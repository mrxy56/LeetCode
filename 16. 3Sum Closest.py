# 1. Note that minnum could be negative, but we compare the absolute value.
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        minnum = 2 ** 31 - 1
        nums.sort()
        for i in range(n):
            l, r = i + 1, n - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if abs(target - s) < abs(minnum):
                    minnum = target - s
                if s < target:
                    l += 1
                else:
                    r -= 1
            if minnum == 0:
                break
        return target - minnum