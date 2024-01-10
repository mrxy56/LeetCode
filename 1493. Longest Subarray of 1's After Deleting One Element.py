# 1. Typical variation of sliding window, update the left pointer when zeros exceed 1.
# 2. Pay attention to the edge case that the string only contain ones.
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        i = j = -1
        ans = zero = one = 0
        n = len(nums)
        while i < n - 1 and j < n - 1:
            i += 1
            if nums[i] == 1:
                one += 1
            else:
                zero += 1
                while zero > 1:
                    j += 1
                    if nums[j] == 1:
                        one -= 1
                    else:
                        zero -= 1
            if zero == 1:
                if one > ans:
                    ans = one
            else:
                if one - 1 > ans:
                    ans = one - 1
        return ans