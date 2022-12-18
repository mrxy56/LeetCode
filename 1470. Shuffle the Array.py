# 1. An index-mapping game. Turn 0-based to 1-based then do the mapping.
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = [0 for i in range(2 * n)]
        for i in range(2 * n):
            if i < n:
                ans[2 * (i + 1) - 2] = nums[i]
            else:
                ans[2 * (i - n + 1) - 1] = nums[i]
        return ans