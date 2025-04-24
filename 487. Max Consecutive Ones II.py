# 1. Sliding window, maintain the number of ones.
# 2. Pay attention to edge cases.
# 3. I was either in -1 or the value is 0, need to cold start to get to the next 0.
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = len(nums)
        i = -1
        j = 0
        zero = 0
        ans = 0
        while j < n:
            if nums[j] == 0:
                zero += 1
                if zero == 1:
                    ans = max(ans, j - i)
                elif zero > 1:
                    i += 1
                    while nums[i] == 1:
                        i += 1
                    zero -= 1
                    ans = max(ans, j - i)
            else:
                ans = max(ans, j - i)
            j += 1
        return ans