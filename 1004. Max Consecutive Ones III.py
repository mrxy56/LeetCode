# 1. Just have two variables to record the ones and zeros honestly.
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i = j = -1
        n = len(nums)
        zero = one = ans = 0
        while i < n - 1 and j < n - 1:
            i += 1
            if nums[i] == 1:
                one += 1
            else:
                zero += 1
                while k < zero:
                    j += 1
                    if nums[j] == 0:
                        zero -= 1
                    else:
                        one -= 1
            if zero + one > ans:
                ans = zero + one
        return ans