# 1. Edge case, n == 0.
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n = len(nums)
        j = 0
        ans = []
        if n == 0:
            return []
        for i in range(n + 1):
            if i == n or i > 0 and nums[i] - nums[i - 1] != 1:
                if j == i - 1:
                    ans.append(str(nums[j]))
                else:
                    ans.append(str(nums[j]) + '->' + str(nums[i - 1]))
                j = i
        return ans