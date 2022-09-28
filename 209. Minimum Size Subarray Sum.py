class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        s = 0
        j = 0
        ans = -1
        for i in range(len(nums)):
            s += nums[i]
            while s >= target: # Two pointers, classical.
                ans = min(ans, i - j + 1) if ans >= 0 else i - j + 1
                s -= nums[j]
                j += 1
        return ans if ans >= 0 else 0